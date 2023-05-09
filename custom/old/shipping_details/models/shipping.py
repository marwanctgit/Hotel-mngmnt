from odoo import fields, models,_

class ShippingDetails(models.Model):
    _name ="shipping.details"
    _description ="shipping_Details"

    informations =fields.Char(string="Informations")
    luggagetype =fields.Char(string="Luggage Type")

