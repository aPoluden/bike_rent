{
    'name': "Bike Rent",

    'summary': """
        Bike rental to person for undefined period of time""",

    'description': """
        Bike rental application
    """,

    'author': "Artiom Poluden",
    'website': "http://www.versada.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/bike_rent_views.xml',
        'views/product_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
