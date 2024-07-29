# Copyright (c) 2022 Meita Dmitry
# MIT License (https://mit-license.org/)

{
    'name': 'Hospital Management',
    'version': '1.0',
    "development_status": "Test",
    "website": "https://github.com/tendil/demo_odoo_project_2",
    'category': 'Management',
    'summary': 'Module for managing hospital operations',
    'author': 'Meita Dmitry',
    'depends': ['base'],
    "maintainers": ["TenDil"],
    "license": "OPL-1",
    "price": 89.99,
    "currency": "EUR",
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/diagnosis_views.xml',
        'data/disease_data.xml',
        'data/doctor_demo.xml',
        'data/patient_demo.xml',
        'views/specialty_views.xml',
    ],
    'demo': [
        'data/doctor_demo.xml',
        'data/patient_demo.xml',
    ],
    'installable': True,
    'application': False,
    "external_dependencies": {"python": [], },
}
