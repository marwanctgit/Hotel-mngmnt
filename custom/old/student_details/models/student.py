from odoo import fields,models

class StudentDetails(models.Model):
    _name = "student.details"
    _description = "student Details"


    studentname= fields.Char(string="Student Name")
    rollnumber = fields.Integer(string="Roll Number")
    gender = fields.Selection([('male' , 'Male'),('female', 'Female')])


