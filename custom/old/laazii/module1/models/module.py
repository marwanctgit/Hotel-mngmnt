# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class TestModule(models.Model):
    _name = 'test.module'
    _description = 'Test Module'

    name = fields.Char(string="Name")
    number = fields.Integer(string="Number")