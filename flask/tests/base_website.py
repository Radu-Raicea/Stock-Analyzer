
from flask_testing import TestCase
from project import create_app, logger
import os
import logging

app = create_app()


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        logger.setLevel(logging.ERROR)
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
