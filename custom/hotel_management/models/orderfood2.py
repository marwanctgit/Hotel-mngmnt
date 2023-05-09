from odoo import fields,models,api,_

class OrderFoodLines(models.Model):
    _name="order.food.lines"
    _description="Food Order Lines"

    food_id = fields.Many2one('order.food',string="Food ID")
    quantity = fields.Integer(string="Quantity")
    price = fields.Float(string="Price")
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
        default=lambda self: self.env.company.currency_id.id)
    subtotal = fields.Monetary(compute='_compute_amount', string="SubTotal")
    food_items_id = fields.Many2one('new.products', string="Food")
