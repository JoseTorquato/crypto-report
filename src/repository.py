from src.config.client import ClientPancakeSwap
from src.services.token import Token


class Repository:

    @classmethod
    def parse(self, list_address):
        for i in range(len(list_address)):
            response = ClientPancakeSwap().get_token(list_address[i]["address"])
            if response["status"] == 200:
                token = Token(response["body"]["name"], response["body"]["symbol"], response["body"]["price"], response["body"]["price_BNB"], list_address[i]["qtd"])
                print(token)
            else:
                print(response["body"])
