{
    'name': 'Event management system',
    'version': '1.0.0',
    'category': 'Event',
    'author': 'Event',
    'sequence': -200,
    'summary': 'Event_management_system',
    'description': """Event management system""",
    'depends': ['mail','base','web','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/events_views.xml',
        'views/menu.xml',
        'views/visitor.xml',
        'views/creator.xml',
        'views/gatepass.xml',
        'report/report.xml',
        'report/gatepass_report.xml',
        'report/custom_order_report.xml',
        'report/custom_order_report_templetecopy.xml'
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
