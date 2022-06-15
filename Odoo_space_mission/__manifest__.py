# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': 'Odoo space mission',
    
    'summary': """Module to get to the moon""",
    
    'description': """Module to help organize the logistcs Including crew and the space ship""",
    
    'author': 'Odoo',
    
    'website':'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'views/spaceship_menuitem.xml',
        'views/spaceship_views.xml',
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo': [
        'demo/spaceship2_demo.xml',
    ],
    
}