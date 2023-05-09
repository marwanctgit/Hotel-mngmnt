from odoo import fields,models,api,_
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError

class HotelReception(models.Model):
    _name = "hotel.reception"
    _description = "Hotel Reception"
    
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char("Name", default="New")
    guest_id = fields.Many2one('res.partner', string="Guest",required = True,tracking = True)
    addons = fields.Integer(string="Additional Guests")
    checkin = fields.Datetime(string="Check In")
    days = fields.Integer(string="Expected Days")
    dates = fields.Date(string="Expected Date",compute="compute_date", tracking=True)
    state = fields.Selection([('draft','Draft'), ('checkin','Checkin'), ('checkout','Checkout'),('cancel','Cancel'), ('invoiced','Invoiced')],default = "draft")
    bed_type = fields.Selection([('single','Single'),('double','Double'),('dormetry','Dormetry')],required = True)
    facility_ids=fields.Many2many('hotel.facility',string="Facilities",required = True)
    rooms_id=fields.Many2one('hotel.room',string="Room",domain="[('facility_ids', '=' , facility_ids)]",required = True)
    guest_ids = fields.One2many('additional.guests','guests_id', string="Additional Guest")
    image_cus = fields.Image(string="Image")
    # active = fields.Boolean(string="Active",default=True)
   

    @api.depends('checkin','days')
    def compute_date(self):
        for rec in self:
            today=date.today()
            if rec.checkin and rec.days:
                rec.dates = rec.checkin + timedelta(days=rec.days)
            else:
                rec.dates = today
    
    @api.model
    def create (self,vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.sequence') or _('New')
            return super(HotelReception,self).create(vals)

    def action_check_in(self):
        
        if len(self.guest_ids) == self.addons:
            self.state = 'checkin'
        else:
            raise ValidationError("Please Provide The Required Guest Details")
        # self.write({'state':'checkin'})

    def action_check_out(self):
        self.write({'state':'checkout'})

    def action_cancel(self):
        self.write({'state':'cancel'})

