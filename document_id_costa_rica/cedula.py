# -*- coding: utf-8 -*- 
from openerp import models, fields

class res_partner(models.Model):

	_inherit = 'res.partner'
	cedula = fields.Char('Número de cédula', size=20)
	tipo_de_cedula=fields.Selection([
            ('company', 'Cedula Jurídica'),
            ('person', 'Cédula de Identidad'),
            ('resident', 'Cédula de Residencia'),
            ('forein', 'Pasaporte'),
            ('auto', 'Institución Autónoma'),
            ('govern', 'Gobierno Central'),
            ('other', 'Otro'),
            ], 'Tipo de cédula')    	  

