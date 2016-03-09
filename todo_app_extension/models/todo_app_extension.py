# -*- coding: utf-8 -*-

from openerp import models, fields

# Añadir partner_id a todo
class TodoApp(models.Model):
    _inherit = 'todo.app'

    # m2o 'res.partner'
    
    
# Añadir todo_ids a partner