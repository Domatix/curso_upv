#!/usr/bin/env python

import xmlrpclib

url = 'http://192.168.56.102:8099'
db = 'odoo'
username = 'admin'
password = 'admin'


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

domain = [['is_company', '=', True], ['name', '!=', 'Agroalit']]
ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [domain])

for id in ids:
    partner = models.execute_kw(db, uid, password,
        'res.partner', 'read',
        [id], {'fields': ['name', 'country_id', 'comment']})
    print partner['name']
    
partner = models.execute_kw(db, uid, password,
    'res.partner', 'read',
    [ids[0]], {'fields': ['name', 'country_id', 'comment']})
print partner['name']

models.execute_kw(db, uid, password, 'res.partner', 'write', [[ids[0]], {
    'name': "Newer partner"
}])

partner = models.execute_kw(db, uid, password,
    'res.partner', 'read',
    [ids[0]], {'fields': ['name', 'country_id', 'comment']})
print partner['name']