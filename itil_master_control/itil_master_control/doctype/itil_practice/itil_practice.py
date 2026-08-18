import frappe
from frappe.model.document import Document
from frappe.utils import flt

class ITILPractice(Document):
	def calculate_health_score(self):
		"""
		Calculate dynamic Health Score based on SLA Compliance and open item backlog.
		Formula: Health = (0.6 * SLA_Compliance) + (0.4 * Backlog_Score)
		"""
		sla_pct = flt(self.sla_compliance_pct or 100.0)
		
		# Backlog penalty calculation
		backlog = flt(self.open_items_count or 0)
		if backlog <= 10:
			backlog_score = 100.0
		elif backlog <= 50:
			backlog_score = 85.0
		elif backlog <= 100:
			backlog_score = 70.0
		else:
			backlog_score = 50.0

		health = flt((0.6 * sla_pct) + (0.4 * backlog_score), 2)
		return min(100.0, max(0.0, health))
