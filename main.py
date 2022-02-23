from src.repository import Repository


if __name__ == "__main__":
    address = [{"address":"0xba96731324de188ebc1ed87ca74544ddebc07d7f", "qtd":1665}, {"address":"0x61073ed3acefafc5e8f87afaedacf9b8586fb28c", "qtd":492}]
    Repository.parse(address)
