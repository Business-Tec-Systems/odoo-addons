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
    'name': 'TF custom QWeb footer',
    'version': '1.0',
    'author': 'Business Tec Systems S.A.',
    'category': 'Base',
    'summary': 'Client specific external footer',
    'description': """
TF custom QWeb footer
=======================
Client specific external footer overriding Odoo standard template
    """,
    'website': 'https://www.businesstec.net',
    'images': [],
    'depends': ['report'],
    'sequence': 18,
    'data': [
        'tf_report_custom_footer.xml',
    ],
    'installable': True,
    'auto_install': False,
}
