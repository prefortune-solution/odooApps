{
    'name': 'Varahi Hospital Managment System',
    'version': '1.0.0',
    'category': 'Managment',
    'author': 'Prefortune Softweb Solution, Rushiraj',
    'sequence': -200,
    'summary': 'Hospital Managment System',
    'description': """Handle Hospital Records With Minimum Effort""",
    'license': 'LGPL-3',
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_number_data.xml',
        'data/patient_reg_mail_template_data.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/employee_view.xml',
        'views/pharmacy_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'Varahi_Multispeciality_Hospital/static/src/legacy/css/style.css',
        ],
    },
    'demo': [],
    'application': True,
    'auto_install': False,
}