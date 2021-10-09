from unittest import TestCase
from src.bitcaviar.blockchain import *
from src.bitcaviar import config


class TestBlockchain(TestCase):
    bitcoin = config.Bitcoin(cli_dir='bitcoin-cli', data_dir='/Users/dennis/Bitcoin')

    def test_get_best_block_hash(self):
        best_block_hash = get_best_block_hash(bitcoin=self.bitcoin)
        self.assertIsInstance(best_block_hash, str)

    def test_get_block(self):
        block_hash = '00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09'
        block = get_block(bitcoin=self.bitcoin, blockhash=block_hash, verbosity=0)
        self.assertIsInstance(block, str)

        block = get_block(bitcoin=self.bitcoin, blockhash=block_hash)
        self.assertIsInstance(block, dict)

        block = get_block(bitcoin=self.bitcoin, blockhash=block_hash, verbosity=2)
        self.assertIsInstance(block, dict)

    def test_get_blockchain_info(self):
        blockchain_info = get_blockchain_info(bitcoin=self.bitcoin)
        self.assertIsInstance(blockchain_info, dict)

    def test_get_block_count(self):
        block_count = get_block_count(bitcoin=self.bitcoin)
        self.assertIsInstance(block_count, int)

    def test_get_block_filter(self):
        block_hash = '00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09'
        block_filter = get_block_filter(bitcoin=self.bitcoin, block_hash=block_hash)
        self.assertIsInstance(block_filter, dict)

    def test_get_block_hash(self):
        block_hash = get_block_hash(bitcoin=self.bitcoin, height='1000')
        self.assertIsInstance(block_hash, str)

    def test_get_block_header(self):
        block_hash = '00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09'
        block_header = get_block_header(bitcoin=self.bitcoin, block_hash=block_hash)
        self.assertIsInstance(block_header, dict)

        block_header = get_block_header(bitcoin=self.bitcoin, block_hash=block_hash, verbose=False)
        self.assertIsInstance(block_header, str)

    def test_get_block_stats(self):
        block_hash = '00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09'
        block_height = '1000'
        stats = ['avgfeerate']

        block_stats = get_block_stats(bitcoin=self.bitcoin, hash_or_height=block_hash)
        self.assertIsInstance(block_stats, dict)

        block_stats = get_block_stats(bitcoin=self.bitcoin, hash_or_height=block_height)
        self.assertIsInstance(block_stats, dict)

        block_stats = get_block_stats(bitcoin=self.bitcoin, hash_or_height=block_hash, stats=stats)
        self.assertIsInstance(block_stats, dict)

        block_stats = get_block_stats(bitcoin=self.bitcoin, hash_or_height=block_height, stats=stats)
        self.assertIsInstance(block_stats, dict)

    def test_get_chain_tips(self):
        chain_tips = get_chain_tips(bitcoin=self.bitcoin)
        self.assertIsInstance(chain_tips, list)
        self.assertIsInstance(chain_tips[0], dict)

    def test_get_chain_tx_stats(self):
        chain_tx_stats = get_chain_tx_stats(bitcoin=self.bitcoin)
        self.assertIsInstance(chain_tx_stats, dict)

        chain_tx_stats = get_chain_tx_stats(bitcoin=self.bitcoin, nblocks=10)
        self.assertIsInstance(chain_tx_stats, dict)

    def test_get_difficulty(self):
        difficulty = get_difficulty(bitcoin=self.bitcoin)
        self.assertIsInstance(difficulty, str)

    def test_get_mempool_ancestors(self):
        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin)
        txid = raw_mempool[50]

        mempool_ancestors = get_mempool_ancestors(bitcoin=self.bitcoin, txid=txid)
        self.assertIsInstance(mempool_ancestors, list)

        mempool_ancestors = get_mempool_ancestors(bitcoin=self.bitcoin, txid=txid, verbose=True)
        self.assertIsInstance(mempool_ancestors, dict)

    def test_get_mempool_descendants(self):
        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin)
        txid = raw_mempool[50]

        mempool_descendants = get_mempool_descendants(bitcoin=self.bitcoin, txid=txid)
        self.assertIsInstance(mempool_descendants, list)

        mempool_descendants = get_mempool_descendants(bitcoin=self.bitcoin, txid=txid, verbose=True)
        self.assertIsInstance(mempool_descendants, dict)

    def test_get_mempool_entry(self):
        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin)
        txid = raw_mempool[50]

        mempool_entry = get_mempool_entry(bitcoin=self.bitcoin, txid=txid)
        self.assertIsInstance(mempool_entry, dict)

    def test_get_mempool_info(self):
        mempool_info = get_mempool_info(bitcoin=self.bitcoin)
        self.assertIsInstance(mempool_info, dict)

    def test_get_raw_mempool(self):
        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin)
        self.assertIsInstance(raw_mempool, list)

        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin, verbose=True)
        self.assertIsInstance(raw_mempool, dict)

        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin, mempool_sequence=True)
        self.assertIsInstance(raw_mempool, dict)

    def test_get_tx_out(self):
        raw_mempool = get_raw_mempool(bitcoin=self.bitcoin)
        txid = raw_mempool[50]

        tx_out = get_tx_out(bitcoin=self.bitcoin, txid=txid, n=2)
        self.assertIsInstance(tx_out, dict)

    def test_get_tx_out_proof(self):
        # noinspection DuplicatedCode
        block_count = get_block_count(bitcoin=self.bitcoin)
        block_hash = get_block_hash(bitcoin=self.bitcoin, height=block_count)
        block = get_block(bitcoin=self.bitcoin, blockhash=block_hash)
        txid = block['tx'][0]

        tx_out_proof = get_tx_out_proof(bitcoin=self.bitcoin, txids=[txid])
        self.assertIsInstance(tx_out_proof, str)

        tx_out_proof = get_tx_out_proof(bitcoin=self.bitcoin, txids=[txid], blockhash=block_hash)
        self.assertIsInstance(tx_out_proof, str)

    def test_get_tx_out_set_info(self):
        tx_out_set_info = get_tx_out_set_info(bitcoin=self.bitcoin)
        self.assertIsInstance(tx_out_set_info, dict)

    def test_get_precious_block(self):
        block_count = get_block_count(bitcoin=self.bitcoin)
        block_hash = get_block_hash(bitcoin=self.bitcoin, height=block_count)
        precious_block = get_precious_block(bitcoin=self.bitcoin, blockhash=block_hash)
        print(precious_block)

    def test_prune_blockchain(self):
        # To test it node must be in prune mode (delete old blocks)
        pass

    def test_save_mempool(self):
        save_mempool(bitcoin=self.bitcoin)

    def test_verify_chain(self):
        verification = verify_chain(bitcoin=self.bitcoin)
        self.assertIsInstance(verification, bool)

    def test_verify_tx_out_proof(self):
        # noinspection DuplicatedCode
        block_count = get_block_count(bitcoin=self.bitcoin)
        block_hash = get_block_hash(bitcoin=self.bitcoin, height=block_count)
        block = get_block(bitcoin=self.bitcoin, blockhash=block_hash)
        txid = block['tx'][0]
        tx_out_proof = get_tx_out_proof(bitcoin=self.bitcoin, txids=[txid])

        txids = verify_tx_out_proof(bitcoin=self.bitcoin, proof=tx_out_proof)
        self.assertIsInstance(txids, list)
