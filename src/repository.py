from src.models.token import Token

class Repository():
    @classmethod
    def parse(self, response):
        token = Token(response["name"], response["symbol"], response["price"], response["price_BNB"])
        print(token)