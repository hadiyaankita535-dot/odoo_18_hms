{
    'name': 'School Module',
    'version': '18.0',
    'summary': 'Simple School Module with Students',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}
