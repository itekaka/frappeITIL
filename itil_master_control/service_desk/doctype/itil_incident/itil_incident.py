import frappe
from frappe.model.document import Document

class ITILIncident(Document):
	"""
	ITIL Incident Document Controller (Service Desk Module).
	Handles ticket lifecycle and calculates priority automatically based on urgency & impact matrix.
	"""
	def validate(self):
		self.calculate_priority()

	def calculate_priority(self):
		"""
		Calculates priority automatically based on Urgency and Impact.
		"""
		matrix = {
			("High", "High"): "Critical",
			("High", "Medium"): "High",
			("Medium", "High"): "High",
			("High", "Low"): "Medium",
			("Low", "High"): "Medium",
			("Medium", "Medium"): "Medium",
			("Medium", "Low"): "Low",
			("Low", "Medium"): "Low",
			("Low", "Low"): "Low",
		}
		
		urgency = self.urgency or "Medium"
		impact = self.impact or "Medium"
		
		self.priority = matrix.get((urgency, impact), "Medium")
