// Copyright (c) 2016, kavin and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS payroll"] = {
	"filters": [
		{
			fieldname: "absentdays",
			label: __("Absentdays"),
			fieldtype: "Int",
			mandatory: true,
			default: frappe.defaults.get_user_default("absentdays")
		}

	]
};
