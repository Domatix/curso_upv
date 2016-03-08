# -*- coding: utf-8 -*-

from openerp import models, fields

class TodoAppCategory(models.Model):
    _name = 'todo.app.category'

    name = fields.Char(
        string="Name",
        required=True,
        translate=True)
    todo_ids = fields.Many2many(
        comodel_name='todo.app',
        relation='todo_app_category_rel',
        column1='categ_id',
        column2='todo_id',
        string='Categories')


class TodoAppRev(models.Model):
    _name = 'todo.app.rev'

    name = fields.Char(
        string="Tittle",
        required=True,
        translate=True)
    todo_id = fields.Many2one(
        comodel_name='todo.app',
        string='Todo')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User')
    

class TodoApp(models.Model):
    _name = 'todo.app'

    name = fields.Char(
        string="Tittle",
        required=True,
        translate=True)
    description = fields.Text(
        string="Description")
    date = fields.Date(
        string="Date")
    # tipo normal, urgente...
    type = fields.Selection(
        [('normal','Normal'),
         ('prior','Prior')],
        string="Type",
        default="normal",
        required=True)
    # etiquetas m2m
    category_ids = fields.Many2many(
        comodel_name='todo.app.category',
        relation='todo_app_category_rel',
        column1='todo_id',
        column2='categ_id',
        string='Categories')
    # revisiones o2m
    rev_ids = fields.One2many(
        comodel_name='todo.app.rev',
        inverse_name='todo_id',
        string='Revs')