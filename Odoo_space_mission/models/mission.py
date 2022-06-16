# -*- coding: utf-8 -*-
from pyexpat import model
from odoo import models, fields, api

class Mission(models.Model):
    _name= 'mission'
    _description  = "Mission details"
    
    spaceship_id = fields.Many2one(comodel_name='spaceship2', string='Spaceship', ondelete='cascade',required = True)
    
 
    name = fields.Char(string='name') 
    spaceship = fields.Char(string='spaceship', related='spaceship_id.name')
    description = fields.Char('description')
    launchdate = fields.Date(string ='launchdate' )
    returndate = fields.Date(string ='returndate' )
    fuel_amount = fields.Float(string='fuel_amount',default=1000)
    engines = fields.Integer(string='engines',default=1)
    contacts_id = fields.Many2many(comodel_name='res.partner', string="Crew")
    project_ids = fields.One2many(comodel_name='project.project', inverse_name='mission_id', string='Projects')
    
    
    
    
    