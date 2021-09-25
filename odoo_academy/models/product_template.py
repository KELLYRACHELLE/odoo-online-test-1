# -- coding: utf-8 --

from odoo import models,fields, api

class ProductTemplate(models.model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string='Use as Session Poduct',
                                        help='Check this box to use this as a product for Session Fee',
                                        default=False)
    