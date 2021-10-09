from unittest import TestCase
from src.pybitcoin import helpers
from src.pybitcoin import config


class TestHelpers(TestCase):
    bitcoin = config.Bitcoin(cli_dir='bitcoin-cli', data_dir='/Users/dennis/Bitcoin')

    def test_run(self):
        output = helpers.run(command=[self.bitcoin.cli_dir, self.bitcoin.data_dir, 'getblockhash', '1'])
        self.assertIsInstance(output, str)
