from odoo import fields,models,_

class PaymentDetails(models.Model):
    _name = "payment.details"
    _description = "Payment Details"

    informations =fields.Char(string="Informations")
    luggagetype =fields.Char(string="Luggage Type")



