from src.config.client import ClientPancakeSwap
from src.services.token import Token


class Repository:

    @classmethod
    def parse(self, list_address):
        message = ""
        for obj in list_address:
            response = ClientPancakeSwap().get_token(obj["address"])
            if response["status"] == 200:
                token = Token(response["body"]["name"], response["body"]["symbol"], response["body"]["price"], response["body"]["price_BNB"], obj["quantity"])
                message += f"<p>{token.__str__()}</p>"
            else:
                print(response["body"])
        print(message)
        return message