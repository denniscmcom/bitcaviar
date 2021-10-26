<p align="center">
  <img src="https://user-images.githubusercontent.com/66180929/136657868-0ec6971b-ed76-43f3-9689-f643e8893706.png" />
</p>


# bitcaviar 
A simple Python wrapper for Bitcoin JSON-RPC API.   

*If you are looking for a Bitcoin blockchain parser check [bitcaviar-plus](https://github.com/denniscm190/bitcaviar-plus).*

## Installation
```bash
pip install bitcaviar
```

## Usage
You should pass your `bitcoin-cli` directory and where you have the blockchain stored to each method.

```python
from bitcaviar import config

bitcoin = config.Bitcoin(
    cli_dir='your/dir/to/bitcoin-cli', 
    data_dir='/where/is/the/blockchain'
)
```

### Example 1
Get the number of blocks in the blockchain

```python
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
```
