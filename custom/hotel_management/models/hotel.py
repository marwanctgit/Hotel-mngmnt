from odoo import fields,models

class HotelManagement(models.Model):
    _name = "hotel.management"
    _description = "Hotel Management"
    _rec_name="bed"

    roomnumber = fields.Integer(string="Room Number")
    bed = fields.Selection([('single','Single'),('double','Double'),('dormetry','Dormetry')])
    rent = fields.Float(string="Rent")