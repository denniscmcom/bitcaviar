
# Table of Contents

1.  [Installation](#orgdb921af)
2.  [Usage](#org9fd02ba)
    1.  [Example](#orgfc928cc)

![img](https://denniscm.com/static/bitcaviar-logo.png)

A simple Python wrapper for Bitcoin JSON-RPC API. If you are looking for a Bitcoin blockchain parser check my other project -> [bitcaviar-plus](https://git.sr.ht/~denniscmartin/bitcaviar-plus).


<a id="orgdb921af"></a>

# Installation

    pip install bitcaviar


<a id="org9fd02ba"></a>

# Usage

    from bitcaviar import config
    
    bitcoin = config.Bitcoin(
        cli_dir='your/dir/to/bitcoin-cli', 
        data_dir='/where/is/the/blockchain'
    )


<a id="orgfc928cc"></a>

## Example

Get the number of blocks in the blockchain.

    from bitcaviar import config
    from bitcaviar import blockchain
    
    
    def main():
        bitcoin = config.Bitcoin(
    	cli_dir='bitcoin-cli', 
    	data_dir='/Users/dennis/Bitcoin'
        )
    
        block_count = blockchain.get_block_count(bitcoin=bitcoin)
    
        print(block_count)
    
    
    if __name__ == '__main__':
        main()

