# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now
class scan(Document):
    @frappe.whitelist()
    def get_data(self):
        item_list=frappe.get_all("User Registration",filters={"url":self.qrcode_data},fields=["user_name","event_name"])
        # frappe.throw(str(item_list))
        for item in item_list:
            # frappe.throw(str(item.event_name))
            # self.user_name =str(item.user_name)
            # self.event_name=str(item.event_name)
            # frappe.throw(str(self.user_name))
            p =str(item.user_name)
            q = str(item.event_name)

            self.user_name =p
            self.event_name=q
            # hh=now()
            # frappe.throw(str(hh))
            self.current_time = now()
            # return 
        
        # self.save()

