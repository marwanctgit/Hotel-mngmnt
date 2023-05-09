from odoo import fields,models

class AdditionalGuests(models.Model):
    _name = "additional.guests"
    _description = "Additional Guests"

    guests_id = fields.Many2one('hotel.reception')
    newname = fields.Char(string="Additional Guests")
    gender = fields.Char(string="Gender")
    age = fields.Integer(string="Age")