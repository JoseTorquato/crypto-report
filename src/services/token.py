class Token():

    def __init__(self, name, symbol, price_usd, price_bnb):
        self._name = name
        self._symbol = symbol
        self._price_usd = price_usd
        self._price_bnb = price_bnb
    
    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def price_usd(self):
        return self._price_usd
    
    @property
    def price_bnb(self):
        return self._price_bnb

    def __str__(self):
        return f"Nome: {self.name} | Simbolo: {self.symbol} | Preço em USD: {float(self.price_usd):.5f} | Preço em BNB: {float(self.price_bnb):.5f}"

