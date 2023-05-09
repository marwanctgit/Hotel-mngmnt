from odoo import fields, models, api

class vehicleDetailslines (models.Model):
    _name = "vehicle.details.lines"
    _description = "vehicle detals"


    vehicle_id = fields.Many2one('sale.module', string = "sale")
    product_id = fields.Many2one('product.product', string = "Product")
    description = fields.Char(string = "Description")
   



 