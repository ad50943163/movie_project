# -*- coding:utf-8 -*- 
#!/usr/bin/env python
# @Author  : tianbao
# @Contact : gmu1592618@gmail.com
# @Time    : 2018/5/13 9:34
# @File    : flask_sqlalchemy_create_preview.py
# @Software: PyCharm
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@205.266.87.91:3306/movie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "HelloWorld"

db = SQLAlchemy(app)

# 上映预告
class Preview(db.Model):
    __tablename__ = 'preview'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique=True)
    logo = db.Column(db.String(255),unique=True) # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Preview %s>'%self.title

if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
    # role = Role(
    #     name='超级管理员',
    #     auths=''
    # )
    # from werkzeug.security import generate_password_hash
    # admin = Admin(
    #     name='imoocmovie1',
    #     pwd=generate_password_hash('imoocmovie1'),
    #     is_super=0,
    #     roleid=1,
    # )
    # db.session.add(admin)
    # db.session.commit()
    # pass