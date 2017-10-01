
from flask_testing import TestCase
from project import create_app, logger, db
import os
import logging

app = create_app()


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        logger.setLevel(logging.ERROR)
        return app

    def setUp(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
