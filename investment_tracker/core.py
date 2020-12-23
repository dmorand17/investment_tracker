
class Ticker:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = None

    def __str__(self):
        return f'[{self.symbol}] {self.name}'

    """
    Returns a dict representation of Stock
    """
    def get_data(self):
        # Return a json representation of this class
        print(f'{self.symbol} - {self.name}')

