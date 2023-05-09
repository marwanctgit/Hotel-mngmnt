from odoo import fields,models

class SchoolDetails(models.Model):
    _name = "school.details"
    _description = "school Details"


    studentname = fields.Char(string="Student Name")
    rollnumber = fields.Integer(string="Roll Number")
    gender = fields.Selection([('male' , 'Male'),('female', 'Female')])




