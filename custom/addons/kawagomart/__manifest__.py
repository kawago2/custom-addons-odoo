# -*- coding: utf-8 -*-
{
    'name': "kawagomart",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ ir_module_category_data.xml  # noqa
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizzard/barangdatang_wizzard_view.xml',
        'wizzard/penjualanreport_wizzard_view.xml',
        'views/menu.xml',
        'views/kelompokbarang_view.xml',
        'views/barang_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/konsumen_view.xml',
        'views/supplier_view.xml',
        'views/penjualan_view.xml',
        'views/direksi_view.xml',
        'report/print_faktur_penjualan.xml',
        'report/wizzard_penjualanreport_template.xml',
        'report/report.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
