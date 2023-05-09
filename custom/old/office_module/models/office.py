from odoo import fields,models,api,_

class OfficeModule(models.Model):
    _name = "office.module"
    _description = "Office Module"


    name = fields.Char("Name", default="New")
    employee = fields.Char(string="Employee Name")
    number  = fields.Integer(string="Mobile Number")
    dateofbirth = fields.Datetime(string="D.O.B")
    gender = fields.Selection([('male', 'Male'),('female','Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([
        ('draft', 'Draft' ),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')])
    office_lines_ids = fields.One2many('office.module.lines', 'office_id', string= 'office')
    currency_id = fields.Many2one('res.currency', 'Currency', required = True,
        default = lambda self: self.env.company.currency_id.id )
    amount_total = fields.Monetary(string="Total", compute="get_amount_total")
    details = fields.Html(string="Other Details")
    priority = fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High')])
    image = fields.Html(string="Product Image")


    @api.depends('office_lines_ids.subtotal')
    def get_amount_total(self):
        for order in self:
            total = 0
            for line in self.office_lines_ids:
                total = total + line.subtotal
            order.write({'amount_total' : total})

    @api.model
    def create (self,vals):
        if vals.get('name', _('New')) == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('office.sequence') or _('New')
            return super(OfficeModule,self).create(vals)


    def action_done(self):
        self.write({'state':'done'})
     


