class Cake:
    def __init__(self, price: float, name: str):
        self._price = price
        self._name = name
    
    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
    def set_name(self, name : str):
        self._name += name