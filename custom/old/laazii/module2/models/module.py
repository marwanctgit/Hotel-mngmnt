# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class TestModule(models.Model):
    _name = 'test.module2'
    _description = 'Test Module2'

    name = fields.Char(string="Name")
    age = fields.Integer(string="age")