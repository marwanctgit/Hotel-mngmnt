from odoo import fields,models

class TeacherDetails(models.Model):
    _name = "teacher.details"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "teacher details"


    teachername = fields.Char(string="Teacher Name")
    gender = fields.Selection([('male' , 'Male'),('female', 'Female')])
    adress = fields.Char(string="Adress")
    dateofbirth = fields.Date(string="Date Of Birth")
    

