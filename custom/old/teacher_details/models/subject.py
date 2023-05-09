from odoo import fields,models

class SubjectDetails(models.Model):
    _name = "subject.details"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "subject details"

