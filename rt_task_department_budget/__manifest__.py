# -*- coding: utf-8 -*-
{
    'name': "RT task department budget",

    'summary': "RT task department budget",

    'description': """
        RT task department budget
    """,

    'author': "Rightechs Solutions",
    'website': "https://www.rightechs.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/employee_task.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
