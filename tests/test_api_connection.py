from unittest import TestCase
import pytest

import requests

from connections import Connect


class APIConnectionTestCase(TestCase):
    """
    Unit test to SpaceX API connection
    """

    def setUp(self):
        """
        Execute before each test
        """

        self.connection = Connect("https://api.spacexdata.com/v3/launches/next")

    def tearDown(self):
        """
        Execute after each test
        """

        del self.connection

    def test_connection_success(self):
        """
        Verify if connection is a success
        """

        self.assertTrue(self.connection.response.status_code == requests.codes.ok)

    def test_response_dict(self):
        """
        Verify the result of request
        """

        connection = requests.get("https://api.spacexdata.com/v3/launches/next")

        self.assertEqual(
            self.connection.response.text,
            connection.text
        )

    def test_response_list(self):
        """
        Verify the result of request
        """

        connection = requests.get("https://api.spacexdata.com/v3/launches/upcoming")

        my_connection = Connect("https://api.spacexdata.com/v3/launches/upcoming")

        self.assertEqual(
            my_connection.response.text,
            connection.text
        )