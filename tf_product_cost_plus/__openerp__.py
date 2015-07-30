# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Business Tec Systems S.A.(<http://businesstec.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Custom Cost Plus Pricing',
    'version': '1.0',
    'category': 'Sales Management',
    'author': 'Business Tec Systems',
    'summary': 'Creates cost margin and calculation for public price ',
    'description': """
Cost Plus Pricing
=======================
Creates cost margin and calculation for public price - customer specific.
Target margin and price are calculated as needed
    """,
    'website': 'https://www.businesstec.net',
    'images': [],
    'depends': ['product', 'sale'],
    'sequence': 18,
    'data': [
        'tf_cost_plus_price.xml',
    ],
    'installable': True,
    'auto_install': False,
}