import json
from src.services.send_email import Email
from src.repository import Repository


if __name__ == "__main__":
    address_tokens = []
    while True:
        init = input("Gostaria de adicionar um novo token? [Y/N] ")
        if init.lower() == "n":
            break
        address = input("Digite um endereco de token ")
        qtd = float(input("Digite a quantidade que você possui do token "))
        address_tokens.append({"address" : address, "quantity" : qtd})
        quit = input("Gostaria de adicionar um novo token? [Y/N] ")

        if quit.lower() == "n":
            break
    if init.lower() != "n":
        with open("resources/vault_address.json", "a") as outfile: 
            json.dump(address_tokens, outfile)
            
    with open("resources/vault_address.json", "r") as vault_tokens:     
        tokens = json.loads(vault_tokens.read())
        report = Repository.parse(tokens)
        Email().send(report)
