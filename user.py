#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
#! -*- coding: utf8 -*-
from trytond.pool import *
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pyson import Id
import base64
from trytond.transaction import Transaction

__all__ = ['User']
__metaclass__ = PoolMeta

class User:
    __name__ = 'res.user'

    limite_usuario = fields.Integer('Limite de Usuarios del Sistema')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()

    @classmethod
    def validate(cls, users):
        transaction = Transaction()
        user_id = transaction.user

        pool = Pool()
        User = pool.get('res.user')
        users_admin = User.search([('id', '=', 1)])

        for user_admin in users:
            if user_admin.id == 1 and user_id != 1:
                cls.raise_user_error ('No puede modificar los datos de ADMINISTRADOR')

            for group in user_admin.groups:
                if group.id == 1 and user_id != 1:
                    cls.raise_user_error('No puede agregar el grupo Administrador a este usuario')

        for u in users_admin:
            user = u

        if user.limite_usuario:
            limite = user.limite_usuario
        else:
            limite = 5

        users_all = User.search([('id', '>', 1)])
        if len(users_all) > limite:
            cls.raise_user_error('No puede agregar usuarios. Ha pasado el limite')
