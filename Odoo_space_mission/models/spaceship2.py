#-*- coding: utf-8 -*-

from unicodedata import name
from odoo import models, fields, api

class spaceship2(models.Model):
    _name = 'spaceship2'
    __description = "this is a spaceship to go to the moon"
    
    name = fields.Char('name', required=True)
    height = fields.Float('height', required=True)
    width = fields.Float('width', required=True)
    fuel_type = fields.Char('fuel_type', required=True)
    passengers = fields.Integer('passengers', required=True)
    active = fields.Boolean('is_active', default=True)
    
    
    
    