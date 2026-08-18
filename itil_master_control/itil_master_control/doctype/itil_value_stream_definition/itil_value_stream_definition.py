import frappe
from frappe.model.document import Document

class ITILValueStreamDefinition(Document):
	def validate(self):
		self.calculate_aggregates()

	def calculate_aggregates(self):
		total_pt = sum(n.target_process_time_hrs or 0 for n in self.nodes)
		total_wt = sum(n.target_wait_time_hrs or 0 for n in self.nodes)
		total_lt = total_pt + total_wt
		
		self.total_target_lead_time_hrs = total_lt
		self.total_target_process_time_hrs = total_pt
		self.total_target_wait_time_hrs = total_wt
		
		if total_lt > 0:
			self.target_flow_efficiency = round((total_pt / total_lt) * 100, 2)
		else:
			self.target_flow_efficiency = 0.0
