"""
Blockchain RPCs
More info: https://developer.bitcoin.org/reference/rpc/
"""

import json
from bitcaviar.__helpers import __run


def get_best_block_hash(bitcoin):
    """
    Get the hash of the best (tip) block in the most-work fully-validated chain
    More info: https://developer.bitcoin.org/reference/rpc/getbestblockhash.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: string
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getbestblockhash']
    best_block_hash = __run(command)
    best_block_hash = best_block_hash.rstrip()

    return best_block_hash


def get_block(bitcoin, blockhash, verbosity=1):
    """
    Get block data
    More info: https://developer.bitcoin.org/reference/rpc/getblock.html
    :param blockhash: string, required
    :param verbosity: int, optional, default=1
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: if verbosity=0 returns string, else returns dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblock', blockhash, str(verbosity)]
    block = __run(command)

    if verbosity == 1 or verbosity == 2:
        block = json.loads(block)

    return block


def get_blockchain_info(bitcoin):
    """
    Get an object containing various state info regarding blockchain processing
    More info: https://developer.bitcoin.org/reference/rpc/getblockchaininfo.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockchaininfo']
    blockchain_info = __run(command)
    blockchain_info = json.loads(blockchain_info)

    return blockchain_info


def get_block_count(bitcoin):
    """
    Get the height of the most-work fully-validated chain
    More info: https://developer.bitcoin.org/reference/rpc/getblockcount.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: int
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockcount']
    block_count = __run(command)
    block_count = int(block_count)

    return block_count


def get_block_filter(bitcoin, block_hash, filter_type='basic'):
    """
    Get a BIP 157 content filter for a particular block.
    To enable the compact block filter, you need to start bitcoind with the -blockfilterindex=basic
    (or simply -blockfilterindex) command line option, or put that option in your bitcoin.conf file
    More info: https://developer.bitcoin.org/reference/rpc/getblockfilter.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param block_hash: string, required
    :param filter_type: string, optional, default=basic
    :return: dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockfilter', block_hash, filter_type]
    block_filter = __run(command)
    block_filter = json.loads(block_filter)

    return block_filter


def get_block_hash(bitcoin, height):
    """
    Get hash of block in best-block-chain at height provided
    More info: https://developer.bitcoin.org/reference/rpc/getblockhash.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param height: int, required
    :return: string
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockhash', str(height)]
    block_hash = __run(command)
    block_hash = block_hash.rstrip()

    return block_hash


def get_block_header(bitcoin, block_hash, verbose=True):
    """
    Get block header information
    More info: https://developer.bitcoin.org/reference/rpc/getblockheader.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param block_hash: string, required
    :param verbose: boolean, optional, default=True
    :return: if verbose=false returns string, else returns dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockheader', block_hash, str(verbose).lower()]
    block_header = __run(command)

    if verbose:
        block_header = json.loads(block_header)

    return block_header


def get_block_stats(bitcoin, hash_or_height, stats='all'):
    """
    Compute per block statistics for a given window. All amounts are in satoshis.
    It won’t work for some heights with pruning.
    More info: https://developer.bitcoin.org/reference/rpc/getblockstats.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param hash_or_height: string, required
    :param stats: list of strings, optional, default=all values
    :return: dict
    """

    if len(hash_or_height) == 64:  # It's a hash
        hash_or_height = json.dumps(hash_or_height)

    if stats == 'all':
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockstats', hash_or_height]
    else:
        stats = json.dumps(stats)
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'getblockstats', hash_or_height, stats]

    block_stats = __run(command)
    block_stats = json.loads(block_stats)

    return block_stats


def get_chain_tips(bitcoin):
    """
    Get information about all known tips in the block tree, including the main chain as well as orphaned branches
    More info: https://developer.bitcoin.org/reference/rpc/getchaintips.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: list of dicts
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getchaintips']
    chain_tips = __run(command)
    chain_tips = json.loads(chain_tips)

    return chain_tips


# noinspection PyIncorrectDocstring
def get_chain_tx_stats(bitcoin, nblocks=None):
    # noinspection PyUnresolvedReferences
    """
        Get statistics about the total number and rate of transactions in the chain
        More info: https://developer.bitcoin.org/reference/rpc/getchaintxstats.html
        :param bitcoin: src.bitcaviar.config.Bitcoin, required
        :param nblocks: int, optional, default=one month
        :param blockhash: currently not supported
        :return: dict
        """

    if nblocks:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'getchaintxstats', str(nblocks)]
    else:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'getchaintxstats']

    chain_tx_stats = __run(command)
    chain_tx_stats = json.loads(chain_tx_stats)

    return chain_tx_stats


def get_difficulty(bitcoin):
    """
    Get the proof-of-work difficulty as a multiple of the minimum difficulty
    More info: https://developer.bitcoin.org/reference/rpc/getdifficulty.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: string
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getdifficulty']
    difficulty = __run(command)

    return difficulty


def get_mempool_ancestors(bitcoin, txid, verbose=False):
    """
    Get all in-mempool ancestors if txid is in the mempool
    More info: https://developer.bitcoin.org/reference/rpc/getmempoolancestors.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param txid: string, required
    :param verbose: boolean, optional, default=False
    :return: if verbose=False returns list of dicts, else dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getmempoolancestors', txid, str(verbose).lower()]
    mempool_ancestors = __run(command)
    mempool_ancestors = json.loads(mempool_ancestors)

    return mempool_ancestors


def get_mempool_descendants(bitcoin, txid, verbose=False):
    """
    Get all in-mempool descendants if txid is in the mempool
    More info: https://developer.bitcoin.org/reference/rpc/getmempooldescendants.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param txid: string, required
    :param verbose: boolean, optional, default=False
    :return: if verbose=False returns list, else dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getmempooldescendants', txid, str(verbose).lower()]
    mempool_descendants = __run(command)
    mempool_descendants = json.loads(mempool_descendants)

    return mempool_descendants


def get_mempool_entry(bitcoin, txid):
    """
    Get mempool data for given transaction
    The transaction id must be in mempool
    More info: https://developer.bitcoin.org/reference/rpc/getmempoolentry.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param txid: string, required
    :return: dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getmempoolentry', txid]
    mempool_entry = __run(command)
    mempool_entry = json.loads(mempool_entry)

    return mempool_entry


def get_mempool_info(bitcoin):
    """
    Get details on the active state of the TX memory pool
    :param bitcoin:
    :return: dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getmempoolinfo']
    mempool_info = __run(command)
    mempool_info = json.loads(mempool_info)

    return mempool_info


def get_raw_mempool(bitcoin, verbose=False, mempool_sequence=False):
    """
    Get all transaction ids in memory pool
    More info: https://developer.bitcoin.org/reference/rpc/getrawmempool.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param verbose: boolean, optional, default=False
    :param mempool_sequence: boolean, optional, default=False
    :return: if verbose=False returns list, else dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'getrawmempool', str(verbose).lower(), str(mempool_sequence).lower()]
    raw_mempool = __run(command)
    raw_mempool = json.loads(raw_mempool)

    return raw_mempool


def get_tx_out(bitcoin, txid, n, include_mempool=True):
    """
    Get details about an unspent transaction output
    More info: https://developer.bitcoin.org/reference/rpc/gettxout.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param txid: string, required
    :param n: int, required
    :param include_mempool: boolean, optional, default=true
    :return: dict
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'gettxout', txid, str(n), str(include_mempool).lower()]
    tx_out = __run(command)

    if tx_out:
        tx_out = json.loads(tx_out)
    else:
        tx_out = {'message': 'no unspent transaction'}

    return tx_out


def get_tx_out_proof(bitcoin, txids, blockhash=None):
    """
    Get a hex-encoded proof that “txid” was included in a block
    NOTE: By default this function only works sometimes. This is when there is an unspent output in the utxo for
    this transaction. To make it always work, you need to maintain a transaction index, using the -txindex command
    line option or specify the block in which the transaction is included manually (by blockhash)
    More info: https://developer.bitcoin.org/reference/rpc/gettxoutproof.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param txids: list, required
    :param blockhash: string, optional
    :return: string
    """

    txids = json.dumps(txids)  # Convert list to json array

    if blockhash:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'gettxoutproof', txids, blockhash]
    else:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'gettxoutproof', txids]

    tx_out_proof = __run(command)
    tx_out_proof = tx_out_proof.rstrip()

    return tx_out_proof


def get_tx_out_set_info(bitcoin, hash_type=None):
    """
    Get statistics about the unspent transaction output set
    Note this call may take some time
    More info: https://developer.bitcoin.org/reference/rpc/gettxoutsetinfo.html
    :param bitcoin:  src.bitcaviar.config.Bitcoin, required
    :param hash_type: string, optional, default=hash_serialized_2
    :return: dict
    """

    if hash_type:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'gettxoutsetinfo', hash_type]
    else:
        command = [bitcoin.cli_dir, bitcoin.data_dir, 'gettxoutsetinfo']

    tx_out_set_info = __run(command)
    tx_out_set_info = json.loads(tx_out_set_info)

    return tx_out_set_info


def get_precious_block(bitcoin, blockhash):
    """
    Treats a block as if it were received before others with the same work.
    A later precious block call can override the effect of an earlier one.
    The effects of precious block are not retained across restarts.
    More info: https://developer.bitcoin.org/reference/rpc/preciousblock.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param blockhash: string, required
    :return: None
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'preciousblock', blockhash]
    precious_block = __run(command)

    return precious_block


def prune_blockchain(bitcoin, height):
    """
    Get prune blockchain height
    You have to set your node into prune mode to make this call work.
    More info: https://developer.bitcoin.org/reference/rpc/pruneblockchain.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param height: int, required
    :return: string
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'pruneblockchain', str(height)]
    prune_blockchain_height = __run(command)
    prune_blockchain_height = int(prune_blockchain_height)

    return prune_blockchain_height


def save_mempool(bitcoin):
    """
    Dumps the mempool to disk. It will fail until the previous dump is fully loaded
    More info: https://developer.bitcoin.org/reference/rpc/savemempool.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :return: None
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'savemempool']
    __run(command)

    return None


"""
Currently not supported scantxoutset: https://developer.bitcoin.org/reference/rpc/scantxoutset.html
"""


def verify_chain(bitcoin, checklevel=3, nblocks=6):
    """
    Verifies blockchain database
    More info: https://developer.bitcoin.org/reference/rpc/verifychain.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param checklevel: int, optional, default=3, range=0-4
    :param nblocks: int, optional, default=6, 0=all
    :return: boolean
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'verifychain', str(checklevel), str(nblocks)]
    verification = __run(command).rstrip()

    if verification == 'true':
        verification = True
    elif verification == 'false':
        verification = False

    return verification


def verify_tx_out_proof(bitcoin, proof):
    """
    Get the txid(s) which the proof commits to
    Verifies that a proof points to a transaction in a block, returning the transaction it commits to and throwing
    an RPC error if the block is not in our best chain
    More info: https://developer.bitcoin.org/reference/rpc/verifytxoutproof.html
    :param bitcoin: src.bitcaviar.config.Bitcoin, required
    :param proof: string, required
    :return: list
    """

    command = [bitcoin.cli_dir, bitcoin.data_dir, 'verifytxoutproof', proof]
    txids = __run(command)
    txids = json.loads(txids)

    return txids
