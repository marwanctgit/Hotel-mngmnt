from odoo import fields,models

class ProductsCategories(models.Model):
    _name = "products.categories"
    _description = "Products Categories"
    _rec_name = "categories"

    categories = fields.Char(string="Categories")
    food_item_ids = fields.Many2many('new.products', string="Item")
