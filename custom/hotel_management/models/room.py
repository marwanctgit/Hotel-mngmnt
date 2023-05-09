from odoo import fields,models

class HotelRoom(models.Model):
    _name = "hotel.room"
    _description = "Hotel Room"
    

    name = fields.Integer(string="Room Number")
    customer_id = fields.Many2one('res.partner', string = "Customer")
    cost = fields.Float(string="Cost")
    facility_ids = fields.Many2many('hotel.facility', string="Facilities")
    bed = fields.Selection([('single','Single'),('double','Double'),('dormetry','Dormetry')])
    image_rom = fields.Image(string="Image")
