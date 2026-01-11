import pandas as pd

def trade_report(conn):
    df = pd.read_sql("SELECT * FROM trades", conn)
    print("\n--- TRADE REPORT ---")
    print(df)
