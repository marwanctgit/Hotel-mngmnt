from odoo import fields,models

class HotelFacility(models.Model):
    _name = "hotel.facility"
    _description = "Hotel Facility"
    _rec_name="facilites"

    facilites = fields.Char(string="Facilities")
    color_one = fields.Integer(string="Color")