#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class spaceship2(models.Model):
    _name = 'spaceship2'
    _description = "this is a spaceship to go to the moon"
    
    name = fields.Char('name', required=True)
    height = fields.Float('height', required=True)
    width = fields.Float('width', required=True)
    fuel_type = fields.Char('fuel_type', required=True)
    shiptype = fields.Char('shiptype', default="Rover")
    passengers = fields.Integer('passengers', required=True)
    active = fields.Boolean('is_active', default=True)
    
    
    mission_ids = fields.One2many(comodel_name="mission",inverse_name="spaceship_id",string="missions")
    
    @api.onchange('passengers')
    def _onchange_(self):
        if self.height < self.width:
            raise UserError('Height can not be smaller than width')  
        if self.passengers > 50:
            self.shiptype = "passengerShip" 
            
    
    
    @api.constrains('height' , 'width')
    def _constrains_height(self):
        for record in self:
            if record.height < record.width:
                raise ValidationError('Height must be gratter than width')
                
                
                            
