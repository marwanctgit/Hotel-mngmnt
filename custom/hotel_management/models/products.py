from odoo import fields,models

class NewProducts(models.Model):
    _name = "new.products"
    _description = "New Products"
    _rec_name = "productname"



    productname = fields.Char(string="Name")
    productcost = fields.Float(string="Cost")
    category_id = fields.Many2one('products.categories', string="Category")
    image = fields.Image(string="Image")      
