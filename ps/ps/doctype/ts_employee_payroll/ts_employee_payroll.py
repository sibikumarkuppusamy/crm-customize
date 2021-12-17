# Copyright (c) 2021, kavin and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class TSEmployeePayroll(Document):
	def validate(self):
		kavin={"Intern":200,"Developer":500,"House Keeping":300,"HR":700}
		self.basicpay=kavin[self.role]