class Bitcoin:
    """
    Store the directory of bitcoin-cli and where the blockchain data is.
    """
    def __init__(self, cli_dir, data_dir):
        """
        :param cli_dir: string, required
        :param data_dir: string, required
        """
        self.cli_dir = cli_dir
        self.data_dir = '-datadir=' + data_dir
