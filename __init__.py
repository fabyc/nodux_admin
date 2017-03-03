#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from .user import *
from .company import *
from .party import *

def register():
    Pool.register(
        User,
        Company,
        Party,
        module='nodux_admin', type_='model')
