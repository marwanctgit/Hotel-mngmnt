from odoo import fields,models,api,_

class OrderFood(models.Model):
    _name = "order.food"
    _description = "Order Food"
    _rec_name = "room_no"

    
    customer = fields.Many2one('res.partner',string="Customer",required = True)
    room_no = fields.Many2one('hotel.room', string="Room No",required = True)
    order_time = fields.Float(string="Order Time")
    meal_type_ids = fields.Many2many('products.categories', string="Meal Type",required = True)
    items_ids = fields.Many2many('new.products', string="Items")
    item_ids = fields.One2many('order.food.lines','food_id',string="Food Items")

    @api.onchange('meal_type_ids')
    def onchange_meal_type_ids(self):
        if self.meal_type_ids:
            self.items_ids = self.meal_type_ids.food_item_ids
        else:
            self.items_ids = False
            