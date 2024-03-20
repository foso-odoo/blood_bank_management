{
    'name': "   Blood Bank Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Foram Solanki",
    'description': """This is the Real Estate Module which describes what is expected price for property for seller and buyer can see this
    """,
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        
        'views/bloodbank_property_views.xml',
        'views/bloodbank_patient_views.xml',
        'views/bloodbank_hospital_views.xml',
        'views/bloodbank_blood_views.xml',
        'views/bloodbank_bloodstock_views.xml',

        
        'views/bloodbank_menus.xml',
        ],
}