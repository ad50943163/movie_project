# -*- coding:utf-8 -*- 
#!/usr/bin/env python
# @Author  : tianbao
# @Contact : gmu1592618@gmail.com
# @Time    : 2018/5/5 17:55
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

admin = Blueprint('admin',__name__)

import app.admin.views