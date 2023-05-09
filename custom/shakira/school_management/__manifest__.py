{
    'name':'school Management',
    'version':'15.0.0.1',
    'summary':'school management',
    'description':'school management',
    'sequence':-190 ,
    'depends' :  [ 'product'],
    'data' : [ 'security/ir.model.access.csv',
                'data/sequence_data.xml',
                'views/menu.xml',
                'views/student_view.xml'
                ],
    'demo' : [ ],
    'installable' : True,
    'auto install' : False }