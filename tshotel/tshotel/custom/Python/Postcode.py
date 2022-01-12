import frappe
import re

def post(self, postalcode):
    if(self.postal_code == None):
        frappe.throw("Please enter the postal code.")
    else:
        postal_val = r"^[1-9][\d]{5}$"
        if(re.match(postal_val, self.postal_code)):
            pass
        else:
            frappe.throw("Please give the correct postal code format")

def gst(self, gstin):
    gs = r"^[0-9]{2}[A-Z]{5}[0-9]{4}" + "[A-Z]{1}[1-9A-Z]{1}" + "Z[0-9A-Z]{1}$";
    if(re.match(gs,self.gstin)):
        pass
    else:
        frappe.throw("Please enter the correct GST Number")
def ph(self, phone):
    pho = r"^[+][0-9]{2,3}[ ][0-9]{10}$";
    if(re.match(pho,self.phone)):
        pass
    else:
        frappe.throw("Please enter the correct Phone Number")


