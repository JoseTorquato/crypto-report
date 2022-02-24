from email import message
import json
from src.services.send_email import Email
from src.repository import Repository


if __name__ == "__main__":
    # address = [{"address":"0xba96731324de188ebc1ed87ca74544ddebc07d7f", "qtd":1665}, {"address":"0x61073ed3acefafc5e8f87afaedacf9b8586fb28c", "qtd":492}]
    # address_tokens = []
    # while True:
    #     address = input("Digite um endereco de token ")
    #     qtd = float(input("Digite a quantidade que você possui do token "))
    #     address_tokens.append({"address" : address, "quantity" : qtd})
    #     quit = input("Gostaria de adicionar um novo token? [Y/N] ")

    #     if quit == "n":
    #         break

    # with open("resources/vault_address.json", "a") as outfile: 
    #     json.dump(address_tokens, outfile)
            
    with open("resources/vault_address.json", "r") as vault_tokens:     
        tokens = json.loads(vault_tokens.read())
        report = Repository.parse(tokens)
        Email().send(report[0])

