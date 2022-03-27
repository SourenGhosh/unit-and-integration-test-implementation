import unittest

from client.external_musician_client import ExternalMusicianClient
from config.external_musicians_client_config import ExternalMusicianClientConfig
from resources.abstract_integration_test_class import AbstractIntegrationTestClass


class ExternalMusicianClientIntegrationTest(unittest.TestCase, AbstractIntegrationTestClass):

    @classmethod
    def setUpClass(cls) -> None:
        cls.set_up_class()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down_class()

    def test_should_get_all_musicians_names(self):
        # given
        external_musician_client_url = "http://localhost"
        external_musician_client_port = 8081
        config = ExternalMusicianClientConfig(url=external_musician_client_url, port=external_musician_client_port)
        external_musician_client = ExternalMusicianClient(config)

        # when
        musician_names = external_musician_client.get_all_musicians_names()

        # then
        self.assertIsNotNone(musician_names)
        self.assertListEqual(musician_names, ['kurt', 'jim', 'noel'])
