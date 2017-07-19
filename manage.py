#!/usr/bin/env python3
#-*- coding:UTF-8 -*-


from flask_script import Manager
from dashboard import create_app, db
from dashboard.api.models import User
import unittest


app = create_app()
manager = Manager(app)

@manager.command
def recreate_db():
    """ Recreate the database """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """ Runs the tests without code coverage """
    tests = unittest.TestLoader().discover('dashboard/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    return 1



if __name__ == "__main__":
    manager.run()