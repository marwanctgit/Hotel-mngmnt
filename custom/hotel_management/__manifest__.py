{
    'name' : 'Hotel Management',
    'version' : '15.0.0',
    'summary' : 'hotel.management',
    'description' : ' ',
    'category' : ' ',
    'depends' :  ['mail'],
    'data' : ['security/ir.model.access.csv',
               'views/facilityview.xml', 
               'views/hotelview.xml',
               'views/receptionview.xml',
               'views/roomview.xml',
               'views/productview.xml',
               'views/categoryview.xml',
               'views/foodorderview.xml',
               'views/sequence.xml'
               
                ],
    'demo' : [ ],
    'installable' : True,
    'auto install' : False,
    'assets' : {}, 

}