def calculate_mtm(trade_price, market_price, quantity):
    return (market_price - trade_price) * quantity

def calculate_exposure(quantity, market_price):
    return quantity * market_price

def calculate_margin(exposure):
    return exposure * 0.15  # 15% margin
