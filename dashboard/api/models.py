#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from datetime import datetime

from dashboard import db


class User(db.Model):
    """ User table """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.Date, nullable=False)


    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.date_created = datetime.now()