from odoo import models,fields

class EstatesModule(models.Model):
    _name = 'estates.module'
    _description = 'Estate Module'

    customer_id = fields.Many2one('res.partner', string="Customer Name")
    number = fields.Integer(string="Number")
    address = fields.Char(string="address")
    image = fields.Html(string="Customer Image")