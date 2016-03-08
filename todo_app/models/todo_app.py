# -*- coding: utf-8 -*-

from openerp import models, fields

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
        string="Type")
    # etiquetas m2m
    # revisiones o2m 