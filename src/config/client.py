import requests


class ClientPancakeSwap:

    API_GET_TOKEN = "https://api.pancakeswap.info/api/v2/tokens"

    @classmethod
    def get_token(self, address):
        response = requests.get(f"{self.API_GET_TOKEN}/{address}")
        
        if response.status_code == 200:
            return {"status": 200, "body": response.json()["data"]} 
        else:
            return {"status": response.status_code, "body":"Address not found"}
