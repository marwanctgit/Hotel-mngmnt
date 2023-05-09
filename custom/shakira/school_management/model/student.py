from datetime import date
from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name ="school.student"
    _description = "school student"
    _rec_name = 'admsn_no'

    name_id = fields.Many2one( 'res.partner' , string = "Student")
    date_of_birth = fields.Date("Date Of Birth")
    age = fields.Integer(string = "Age", compute='_compute_age')
    gender = fields.Selection([('male' ,'Male'), ('female', 'Female')], string = "Gender")
    admsn_no =fields.Char(string ="Admission Number")
    image = fields.Image(string ="Image")
    student_store_ids =fields.One2many('student.store','student_id',string ="student store")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
                return rec.age
            else:
                rec.age = 0
    @api.model
    def create(self, vals):
        vals['admsn_no']=self.env['ir.sequence'].next_by_code('admission.sequence')

        return super(SchoolStudent, self).create(vals)

class StudentStore(models.Model):
    _name ="student.store"
    _description = "Student Store"    

    product_id = fields.Many2one('product.product', string="Item")  
    price = fields.Float(string ="Price")
    qty = fields.Integer(string="Quantity")     
    student_id = fields.Many2one('school.student', string ="Student Id")
            