from lib2to3.pgen2 import token
from urllib import response
from src.config.client import ClientPancakeSwap
from src.repository import Repository

if __name__ == "__main__":
    address = "0xba96731324de188ebc1ed87ca74544ddebc07d7f"
    response = ClientPancakeSwap().get_token(address)["body"]["data"]

    Repository.parse(response)