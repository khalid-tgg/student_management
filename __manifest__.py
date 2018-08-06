##############################################################################
{
    'name': 'Student Management',
    'version': '1.0.0',
    'category': 'Others',
    'license': 'AGPL-3',
    'author': 'Phat Nguyen',
    'depends': ['base'],
    'data': [
        # Views
        'views/student_views.xml',
        # Menu
        'menu/menu.xml',
    ],
    'installable': True,
    'application': True,

}
