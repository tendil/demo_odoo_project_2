# Copyright (c) 2022 Meita Dmitry
# MIT License (https://mit-license.org/)
{
    "name": "My Super Demo Module",
    "summary": "This my module for demo",
    "version": "17.0.0.1",
    "development_status": "Test",
    "category": "Main Tools",
    "website": "https://github.com/tendil/demo_odoo_project_2",
    "author": "Meita Dmitry",
    "maintainers": ["TenDil"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "price": 0,
    "currency": "EUR",
    "data": [
        "security/ir.model.access.csv",
        "views/my_demo_views.xml",
    ],
    "demo": [
        "demo/my_demo.xml"
    ],
    "depends": [
        "base",
    ],
    "external_dependencies": {"python": [], },
}
