# -*- coding: utf-8 -*-
{
    'name': "POS Dashboard Ninja",

    'summary': """
    Revamp your POS Dashboard like never before! It is one of the best POS dashboard odoo apps in the market.
    """,

    'description': """
        Dashboard Ninja,
        Odoo Dashboard, 
        Dashboard,
        Odoo apps,
        Dashboard app,
        HR Dashboard,
        Sales Dashboard, 
        inventory Dashboard, 
        Lead Dashboard, 
        Opportunity Dashboard, 
        CRM Dashboard,
        POS,
        POS Dashboard,
        Connectors,
        Web Dynamic,
        Report Import/Export,
        Date Filter,
        HR,
        Sales,
        Theme,
        Tile Dashboard,
        Dashboard Widgets,
        Dashboard Manager,
        Debranding,
        Customize Dashboard,
        Graph Dashboard,
        Charts Dashboard,
        Invoice Dashboard,
        Project management,
        Ksolves,
        Point Of Sale,
        Point Of Sale Alert,
        POS,
        POS Dashboard
    """,

    'author': "Ksolves India Pvt. Ltd.",
    'license': 'LGPL-3',
    'website': "https://www.ksolves.com",
    'maintainer': 'Ksolves India Pvt. Ltd.',
    'live_test_url': 'https://dashboardninja.kappso.com',
    'category': 'Tools',
    'version': '1.0.0',
    'support': 'sales@ksolves.com',
    'images': ['static/description/banner.png'],

    'depends': ['base', 'web','ks_dashboard_ninja', 'base_setup','point_of_sale'],

    'data': [
        'data/ks_pos_sales_data.xml'
    ],

    'uninstall_hook': 'uninstall_hook',

}
