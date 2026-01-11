from datetime import date

def settle_trade(trade):
    if trade.status == "EXECUTED" and trade.settlement_date <= date.today():
        trade.status = "SETTLED"
    return trade.status
