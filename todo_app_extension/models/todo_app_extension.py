# -*- coding: utf-8 -*-

from openerp import models, fields

# Añadir partner_id a todo
class TodoApp(models.Model):
    _inherit = 'todo.app'

    # m2o 'res.partner'
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner")
    
    
# Añadir todo_ids a partner