# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 FactorLibre (http://www.factorlibre.com)
#                  Hugo Santos <hugo.santos@factorlibre.com>
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
    'name': 'Delivery Carrier File: Gefco',
    'version': '1.0',
    'author': "FactorLibre, Odoo Community Association (OCA)",
    'category': 'Generic Modules/Warehouse',
    'depends': [
        'base_delivery_carrier_files',
        'base_delivery_carrier_label',
    ],
    'website': 'http://factorlibre.com',
    'data': [
        'security/ir.model.access.csv',
        'views/carrier_file_view.xml',
        'views/gefco_destination_view.xml',
        'wizard/gefco_destination_config_wizard_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
