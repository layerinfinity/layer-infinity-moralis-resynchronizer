import os
from dataclasses import dataclass
import requests
import time
import urllib.parse

from config import API_KEY


@dataclass
class ChainNFTSet:
    chain: str
    tokenId: int
    tokenAddress: str


# Gems
gemNftEthTestnet = ChainNFTSet(
    chain="eth", tokenAddress="0x5e37Eb26aAF8E34c49FB57f43F118a3FF73BBf0b", tokenId=1
)
gemNftAvaxTestnet = ChainNFTSet(
    chain="avalanche testnet",
    tokenAddress="0xF457e1DB610B0A6F5d41d8CEf7655A5C68d67D71",
    tokenId=1,
)
gemNftPolygonTestnet = ChainNFTSet(
    chain="mumbai", tokenAddress="0x0Ca472FbfA460bC45e7DCF2faf97321Be4CF9eB0", tokenId=1
)


queue: list[ChainNFTSet] = []

# Blanks
queue.append(
    ChainNFTSet(
        chain="goerli",
        tokenAddress="0xC99e68b19B8eAdd849317A8221ecF55185B0a400",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche testnet",
        tokenAddress="0x87316fBDCe129b287420431d36f1182412B4b70d",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="mumbai",
        tokenAddress="0x4a132EcaBBdF61E34f14b513D0c4845468c6BA18",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="eth",
        tokenAddress="0xEfe075c5cA6342a09cC9715D823C56465E6a6dbC",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche",
        tokenAddress="0x358A609653D05153901F8791347f357E3ec58cC5",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="polygon",
        tokenAddress="0x358A609653D05153901F8791347f357E3ec58cC5",
        tokenId=1,
    )
)

# Gems
queue.append(
    ChainNFTSet(
        chain="goerli",
        tokenAddress="0x5e37Eb26aAF8E34c49FB57f43F118a3FF73BBf0b",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche testnet",
        tokenAddress="0xF457e1DB610B0A6F5d41d8CEf7655A5C68d67D71",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="mumbai",
        tokenAddress="0x0Ca472FbfA460bC45e7DCF2faf97321Be4CF9eB0",
        tokenId=1,
    )
)

queue.append(
    ChainNFTSet(
        chain="eth",
        tokenAddress="0x0FB768c93FA9f0268EF5eb65F6B06E199Ee68c15",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche",
        tokenAddress="0xceedB5A30dcdd2BB9Ce8e75905a0Dedf96628801",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="polygon",
        tokenAddress="0xD4A554B125672CE8dA053205bC9DA4E26aA78f44",
        tokenId=1,
    )
)


def start_sync():
    for item in queue:
        url = f"https://deep-index.moralis.io/api/v2/nft/{item.tokenAddress}/{item.tokenId}/metadata/resync?chain={urllib.parse.quote(item.chain)}&flag=uri&mode=async"
        headers = {"accept": "application/json", "X-API-Key": API_KEY}
        response = requests.get(url, headers=headers)
        print(f"Processing address {item.tokenAddress} on chain {item.chain}:")
        print(response.text)

        time.sleep(2)
    return
