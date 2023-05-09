from odoo import fields, models, api, _

class VehicleDetails(models.Model):
    _name = "vehicle.details"
    _description = "VehicleDetails"

    vehiclename = fields.Char("Name", default="New")
    vehicle_id = fields.Many2one('res.partner', string="vehicle name")
    chaseisnumber = fields.Integer(string = "chase Number")
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')])
    vehicle_lines_ids = fields.One2many('vehicle.module.lines', 'sale_id', string = 'sale')

    @api.onchange('vehicle_id')
    def onchange_vehicle_id(self):
        self.number = self.vehicle_id.vehiclename

   
    def action_done(self):
        self.write({'state':'done'})

