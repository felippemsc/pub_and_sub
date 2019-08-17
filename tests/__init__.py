import base64
import logging
import os
import sys

from falcon import testing

from project.api import create_app
from config import TestConfig


LOG = logging.getLogger()


def encode_base_auth_header(basic_auth: str):
    return 'Basic {}'.format(
        base64.b64encode(basic_auth.encode('utf-8')).decode('utf-8'))


class BaseTestCase(testing.TestCase):
    """
    Base Class for the unit tests.
    """
    dir_ = os.path.dirname(__file__)
    files_dir = os.path.join(dir_, "tables")

    tests_handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        format=("\n%(asctime)s [%(levelname)s] "
                "[%(module)s:%(funcName)s:%(lineno)s] "
                "[%(threadName)s-%(thread)d] \n%(message)s"),
        datefmt="%Y-%m-%d %H:%M:%S")

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def set_logging(self):
        """
        Configures the logs for the tests.

        For the output to be "clean", the level is by default as high as possible.

        This level can be changed if necessary to indicate further test details.

        Separated into a function, you can also override the level for specific tests as needed.
        """
        LOG.level = logging.CRITICAL  # modify to a lower level when needed
        LOG.addHandler(self.tests_handler)

    def setUp(self):
        """Configures whatever is required for testing."""
        super().setUp()

        self.set_logging()
        self.app = create_app(TestConfig)

    def tearDown(self):
        """Undo testing setup if necessary."""
        LOG.removeHandler(self.tests_handler)
