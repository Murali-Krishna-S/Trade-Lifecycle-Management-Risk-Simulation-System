import pandas as pd
from config.db_config import get_connection
from front_office.order_manager import Trade
from middle_office.risk_engine import calculate_mtm, calculate_exposure, calculate_margin
from back_office.settlement_engine import settle_trade
from reporting.reports import trade_report

# DB setup
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trades (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    quantity INTEGER,
    trade_price REAL,
    trade_date TEXT,
    settlement_date TEXT,
    status TEXT
)
""")
conn.commit()

# Load prices
prices = pd.read_csv("data/prices.csv").set_index("symbol")

# Front Office: Create Trades
trade1 = Trade(1, "AAPL", 10, 190)
trade2 = Trade(2, "MSFT", 5, 400)

trades = [trade1, trade2]

for trade in trades:
    cursor.execute("""
INSERT INTO trades (symbol, quantity, trade_price, trade_date, settlement_date, status)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    trade.symbol,
    trade.quantity,
    trade.price,
    trade.trade_date,
    trade.settlement_date,
    trade.status
))

conn.commit()

# Middle Office: Risk & MTM
print("\n--- RISK & P&L ---")
for trade in trades:
    market_price = prices.loc[trade.symbol, "price"]
    mtm = calculate_mtm(trade.price, market_price, trade.quantity)
    exposure = calculate_exposure(trade.quantity, market_price)
    margin = calculate_margin(exposure)

    print(f"{trade.symbol} | MTM: {mtm} | Exposure: {exposure} | Margin: {margin}")

# Back Office: Settlement
print("\n--- SETTLEMENT ---")
for trade in trades:
    status = settle_trade(trade)
    cursor.execute(
        "UPDATE trades SET status=? WHERE trade_id=?",
        (status, trade.trade_id)
    )
conn.commit()

# Reporting
trade_report(conn)

conn.close()
