# -*- coding: utf-8 -*-

{
        'author': 'Guijin Ding',
        'price': 10,
        'currency': 'EUR',
    'name': 'PPMessage',
    'category': 'website',
    'summary': 'Profession web live chat',
    'version': '1.0',
    'description': """
        """,
    'depends': ['mail'],
    'data': [
        'views/views.xml'
    ],
    'assets': {
        'web.assets_qweb': [
        ],
        'web.assets_backend': [
            'ppmessage/static/src/**/*',
        ],
        'web.assets_frontend': [
            'ppmessage/static/src/css/*.scss',
        ],
        'web.tests_assets': [
        ],
        'web.qunit_mobile_suite_tests': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_hook',
}
