import frappe
from frappe import _
from frappe.utils import now_datetime, date_diff, time_diff_in_hours, flt, getdate

@frappe.whitelist()
def get_practice_dashboard_metrics():
	"""
	Returns real-time health scores and KPI indicators for all 24 ITIL 4 Practices
	grouped by their 4 Dimensions.
	"""
	practices = frappe.get_all(
		"ITIL Practice",
		fields=["name", "practice_name", "dimension", "health_score", "icon", "practice_owner", "open_items_count", "sla_compliance_pct", "trend_direction"]
	)

	grouped_metrics = {
		"Organizations & People": [],
		"Information & Technology": [],
		"Partners & Suppliers": [],
		"Value Streams & Processes": []
	}

	for p in practices:
		dim = p.get("dimension") or "Value Streams & Processes"
		if dim in grouped_metrics:
			grouped_metrics[dim].append(p)

	return grouped_metrics


@frappe.whitelist()
def recalculate_all_practice_health():
	"""
	Background job running every 15 mins to calculate Health Scores (0-100%) for all 24 practices.
	Formula: Health = (w1 * SLA_Compliance) + (w2 * Backlog_Score) + (w3 * Quality_Score)
	"""
	practices = frappe.get_all("ITIL Practice", fields=["name", "doctype_reference"])
	
	for p in practices:
		doc = frappe.get_doc("ITIL Practice", p.name)
		health = doc.calculate_health_score()
		doc.health_score = health
		doc.last_calculated = now_datetime()
		doc.save(ignore_permissions=True)
	
	frappe.db.commit()
	return {"status": "success", "recalculated_count": len(practices)}


@frappe.whitelist()
def generate_daily_health_snapshots():
	"""
	Daily scheduler job creating historical records in ITIL Practice Health Snapshot.
	"""
	practices = frappe.get_all("ITIL Practice", fields=["name", "health_score", "open_items_count", "sla_compliance_pct"])
	today = getdate()
	
	for p in practices:
		snapshot = frappe.get_doc({
			"doctype": "ITIL Practice Health Snapshot",
			"practice": p.name,
			"snapshot_date": today,
			"health_score": p.health_score,
			"open_items_count": p.open_items_count,
			"sla_compliance_pct": p.sla_compliance_pct
		})
		snapshot.insert(ignore_permissions=True)
	
	frappe.db.commit()


@frappe.whitelist()
def get_value_stream_graph(value_stream_id=None):
	"""
	Returns nodes, edges, transaction counts, lead times, wait times, and Flow Efficiency 
	for rendering in the Service Value Stream Mapper canvas.
	"""
	if not value_stream_id:
		# Fetch default active Value Stream
		vs_list = frappe.get_all("ITIL Value Stream Definition", filters={"is_active": 1}, fields=["name", "stream_name"])
		if not vs_list:
			return {"error": "No active Value Stream definition found."}
		value_stream_id = vs_list[0].name

	vs_doc = frappe.get_doc("ITIL Value Stream Definition", value_stream_id)
	
	nodes = []
	for n in vs_doc.nodes:
		# Calculate real-time node metrics from linked practice DocType
		open_count = frappe.db.count(n.practice_doctype, filters={"docstatus": 0}) if n.practice_doctype else 0
		nodes.append({
			"id": n.node_id,
			"label": n.step_name,
			"practice": n.practice,
			"practice_doctype": n.practice_doctype,
			"target_process_time_hrs": n.target_process_time_hrs,
			"target_wait_time_hrs": n.target_wait_time_hrs,
			"avg_actual_lead_time": n.avg_actual_lead_time or (n.target_process_time_hrs + n.target_wait_time_hrs),
			"open_count": open_count,
			"pos_x": n.pos_x,
			"pos_y": n.pos_y
		})

	edges = []
	for e in vs_doc.edges:
		edges.append({
			"id": e.name,
			"source": e.source_node_id,
			"target": e.target_node_id,
			"label": e.edge_label,
			"auto_trigger": e.auto_trigger_action
		})

	# Calculate aggregate Lean metrics
	total_process_time = sum(n["target_process_time_hrs"] for n in nodes) or 1
	total_lead_time = sum(n["avg_actual_lead_time"] for n in nodes) or 1
	flow_efficiency = flt((total_process_time / total_lead_time) * 100, 2)

	return {
		"value_stream": {
			"name": vs_doc.name,
			"stream_name": vs_doc.stream_name,
			"trigger_condition": vs_doc.trigger_condition,
			"target_outcome": vs_doc.target_outcome,
			"flow_efficiency": flow_efficiency,
			"total_lead_time_hrs": total_lead_time,
			"total_process_time_hrs": total_process_time,
			"total_wait_time_hrs": flt(total_lead_time - total_process_time, 2)
		},
		"nodes": nodes,
		"edges": edges
	}


# --- Event Hooks for Auto-Linking Cross-Practice Artifacts ---

def on_incident_update(doc, method):
	"""
	Auto-link Incident to Problem if problem_reference is set.
	Update Value Stream transaction logs.
	"""
	if doc.linked_problem:
		_create_practice_link(
			source_doctype="ITIL Incident",
			source_name=doc.name,
			target_doctype="ITIL Problem",
			target_name=doc.linked_problem,
			link_type="Caused By / Investigated Via"
		)

def on_problem_update(doc, method):
	"""
	Auto-link Problem to Change Request if change_request is set.
	"""
	if doc.linked_change_request:
		_create_practice_link(
			source_doctype="ITIL Problem",
			source_name=doc.name,
			target_doctype="ITIL Change Request",
			target_name=doc.linked_change_request,
			link_type="Resolved Via Change"
		)

def on_change_update(doc, method):
	"""
	Auto-link Change Request to Deployment Log when status moves to Approved / Scheduled.
	"""
	if doc.status == "Approved" and doc.deployment_log:
		_create_practice_link(
			source_doctype="ITIL Change Request",
			source_name=doc.name,
			target_doctype="ITIL Deployment Log",
			target_name=doc.deployment_log,
			link_type="Deployed Via"
		)

def on_deployment_submit(doc, method):
	"""
	Complete Value Stream transaction execution cycle when Deployment Log is submitted.
	"""
	if doc.change_request:
		frappe.db.set_value("ITIL Change Request", doc.change_request, "status", "Completed")

def _create_practice_link(source_doctype, source_name, target_doctype, target_name, link_type):
	exists = frappe.db.exists("ITIL Practice Link", {
		"source_doctype": source_doctype,
		"source_name": source_name,
		"target_doctype": target_doctype,
		"target_name": target_name
	})
	if not exists:
		link = frappe.get_doc({
			"doctype": "ITIL Practice Link",
			"source_doctype": source_doctype,
			"source_name": source_name,
			"target_doctype": target_doctype,
			"target_name": target_name,
			"link_type": link_type,
			"created_on": now_datetime()
		})
		link.insert(ignore_permissions=True)
