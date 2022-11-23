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


queue: list[ChainNFTSet] = []

# Blanks
queue.append(
    ChainNFTSet(
        chain="goerli",
        tokenAddress="0x41CE00De36E94fbFE06D694A7e14d7C514256D56",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche testnet",
        tokenAddress="0x9d9d99f32294215fbd40279367D50d74BC185825",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="mumbai",
        tokenAddress="0x2E478697c9E403938C9076e00d0b15680536F4A4",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="eth",
        tokenAddress="0x90B9a29628Dc1b2674777f6293490ebE3289F2EF",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche",
        tokenAddress="0x90B9a29628Dc1b2674777f6293490ebE3289F2EF",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="polygon",
        tokenAddress="0x90B9a29628Dc1b2674777f6293490ebE3289F2EF",
        tokenId=1,
    )
)

# Gems
queue.append(
    ChainNFTSet(
        chain="goerli",
        tokenAddress="0x732C6dc15E58742DD559295Dd7F1eed2fD234D3B",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche testnet",
        tokenAddress="0x19F510B942e5d7D323229cd9171bCcB47ba73573",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="mumbai",
        tokenAddress="0x291f290a552779954838737D54951b6dfdD50688",
        tokenId=1,
    )
)

queue.append(
    ChainNFTSet(
        chain="eth",
        tokenAddress="0xD4a49C9fBD384E8cb8C70A2E53A00595BDE073B8",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche",
        tokenAddress="0xD4a49C9fBD384E8cb8C70A2E53A00595BDE073B8",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="polygon",
        tokenAddress="0xD4a49C9fBD384E8cb8C70A2E53A00595BDE073B8",
        tokenId=1,
    )
)

# Fusion
queue.append(
    ChainNFTSet(
        chain="goerli",
        tokenAddress="0xd9A50766CCF5cd17ef643dfc89a4129ab90D2537",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche testnet",
        tokenAddress="0x0F9bCea9317735437bF7b1f1ccA28281D01cF686",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="mumbai",
        tokenAddress="0x71881245F6a512BefD5DD0d89688171F56Fb8f59",
        tokenId=1,
    )
)

queue.append(
    ChainNFTSet(
        chain="eth",
        tokenAddress="0x5c79FC6ed88a3BB36c0E0abefF56dCE6D7E74176",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="avalanche",
        tokenAddress="0x5c79FC6ed88a3BB36c0E0abefF56dCE6D7E74176",
        tokenId=1,
    )
)
queue.append(
    ChainNFTSet(
        chain="polygon",
        tokenAddress="0x5c79FC6ed88a3BB36c0E0abefF56dCE6D7E74176",
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
