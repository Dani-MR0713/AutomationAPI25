import logging
import unittest
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestExample:

    @classmethod
    def setup(cls):
        """
         Setup class
         :return:
        """
        LOGGER.info("Setup class")

    def test_one(self):
        LOGGER.info("test one")
    def test_two(self):
        LOGGER.info("test two")
    def test_three(self):
        LOGGER.info("test three")

    @classmethod
    def teardown(cls):
        LOGGER.info("teardown")
