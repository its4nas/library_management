# Copyright (c) 2023, anas abdullah and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime # from python std library
from frappe.utils import add_to_date

class MemberShip(Document):
	def before_save(self):
    		self.to_date = add_to_date(self.from_date, days=365)
