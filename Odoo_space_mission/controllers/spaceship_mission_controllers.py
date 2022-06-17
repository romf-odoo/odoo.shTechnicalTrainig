# -*- coding: utf-8 -*-
from odoo import http

class SpaceshipMission(http.Controller):
    @http.route('/spaceship', auth='public', website=True)
    def index(self, **kw):
        return "hello word"
    @http.route('/spaceship/missions/', auth='public', website=True)
    def spaceships(self, **kw):
        spaceship = http.request.env['spaceship2'].search([])
        return http.request.render('Odoo_space_mission.spaceship_website',{
            'spaceships': spaceship
        })
    
    @http.route('/spaceship/<model("mission"):mission>/', auth='public', website=True)
    def mission(self, mission):
        return http.request.render('Odoo_space_mission.mission_website',{
            'mission': mission,
        })
        
    