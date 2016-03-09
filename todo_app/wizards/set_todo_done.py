# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TodoSetDone(models.TransientModel):
    _name = 'todo.set.done'
    
    name = fields.Char(
        string="Rev")
    todo_id = fields.Many2one(
        comodel_name='todo.app',
        required=True,
        string='Todo')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User')
    
    @api.one
    def set_todo_done(self):
        # Crear la revision
        app_rev_obj = self.env['todo.app.rev']
        values = {
            'name': self.name,
            'todo_id': self.todo_id.id,
            'user_id': self.user_id and self.user_id.id}
        rev_id = app_rev_obj.create(values)
        # pasar el todo a estado done
        #self.todo_id.write({'state':'done'})
        #self.todo_id.state = 'done'
        self.todo_id.set_done_state()
    
    @api.model
    def default_get(self, fields):

        res = super(TodoSetDone, self).default_get(fields)
        
        res.update({
            'todo_id':self.env.context.get('active_id'),
            'user_id':self.env.context.get('uid'),})
        return res