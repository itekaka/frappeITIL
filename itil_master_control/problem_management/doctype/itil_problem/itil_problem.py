import frappe
from frappe.model.document import Document

class ITILProblem(Document):
	"""
	ITIL Problem Document Controller (Problem Management Module).
	Tracks root cause analysis, known errors, and permanent resolution planning.
	"""
	def validate(self):
		if self.known_error_status and self.status == "Under Investigation":
			self.status = "Known Error Identified"
