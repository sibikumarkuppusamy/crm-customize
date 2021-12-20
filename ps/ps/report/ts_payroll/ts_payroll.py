# Copyright (c) 2013, kavin and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns=get_columns(filters)
	data=get_data(filters)
	return columns, data


def get_columns(filters):
	columns =[
		{
			"label": _("Name"),
			"fieldtype": "Data",
			"fieldname": "name1",
			"options": "Name"
			
		},
		{
			"label": _("ID"),
			"fieldtype":"Int",
			"fieldname": "id",
			"options": "ID"
			
		},
		{
			"label": _("Role"),
			"fieldtype":"Select",
			"fieldname": "role",
			"options": [
				{"value":"Intern","label":("Intern")},
				{"value":"Developer","label":("Developer")},
				{"value":"HR","label":("HR")},
				{"value":"House keeping","label":("House keeping")}
			]
			
		}


	]
	return columns
def get_conditions(filters):
	conditions = {}
		
	if filters.absentdays:
		conditions["absentdays"]=filters.absentdays

	return conditions
def get_data(filters):

	data = []
	conditions =get_conditions(filters)
	print(conditions)
	accounts = frappe.db.get_all("TS Employee Payroll",fields=["name1","id","role"],filters=conditions,order_by="id")
	for d in accounts:
		row= {"name1": d.name1,"id":d.id,"role":d.role}

		data.append(row)

	return data