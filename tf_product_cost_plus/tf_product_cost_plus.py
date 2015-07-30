# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class price_product_template(models.Model):

    _inherit = "product.template"
    target_margin = fields.Float(string='Margen previsto', digits=(6,2))

    @api.one
    @api.onchange('standard_price','list_price')
    def new_margin(self):
        if self.standard_price != 0:
            self.target_margin = ((self.list_price/self.standard_price) -1) * 100
        else:
            self.target_margin = 0
    @api.one
    @api.onchange('target_margin')
    def new_price(self):
        self.list_price = self.standard_price * (1 + self.target_margin/100)