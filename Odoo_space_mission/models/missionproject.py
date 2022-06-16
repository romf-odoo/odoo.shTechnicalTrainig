# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name= 'mission', string='Related mission', ondelete='set null')
    
    contacts_id = fields.Many2many(string='Mission Crew', related = 'mission_id.contacts_id')
