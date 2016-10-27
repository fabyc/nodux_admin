#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from .user import *

def register():
    Pool.register(
        User,
        module='nodux_admin', type_='model')
