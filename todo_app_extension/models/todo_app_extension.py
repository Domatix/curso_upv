# -*- coding: utf-8 -*-

from openerp import models, fields

# Añadir partner_id a todo
class TodoApp(models.Model):
    _inherit = 'todo.app'

    # m2o 'res.partner'
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        domain=[("customer","=",True)])
    
    
# Añadir todo_ids a partner

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    todo_ids = fields.One2many(
        comodel_name="todo.app",
        inverse_name="partner_id",
        string="Todo List")