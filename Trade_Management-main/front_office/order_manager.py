from datetime import datetime, timedelta

class Trade:
    def __init__(self, trade_id, symbol, quantity, price):
        self.trade_id = trade_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.trade_date = datetime.today().date()
        self.settlement_date = self.trade_date + timedelta(days=2)
        self.status = "EXECUTED"

    def to_tuple(self):
        return (
            self.trade_id,
            self.symbol,
            self.quantity,
            self.price,
            str(self.trade_date),
            str(self.settlement_date),
            self.status
        )
