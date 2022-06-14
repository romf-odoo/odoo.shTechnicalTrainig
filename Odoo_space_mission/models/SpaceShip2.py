#-*- coding: utf-8 -*-

from odoo import models, fields, api

class SpaceShip(models.Model):
    _name = 'spaceship2'
    __description = "this is a spaceship to go to the moon"
    
    dimensions_height = fields.Float('height', required=True)
    dimensions_width = fields.Float('width', required=True)
    fuel_type = fields.Char('fuel_type', required=True)
    passengers = fields.Integer('passengers', required=True)
    active = fields.Boolean('is_active', default=True)
    
    
    
    