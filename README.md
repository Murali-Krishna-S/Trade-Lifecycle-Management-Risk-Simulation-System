This project simulates the complete lifecycle of a financial trade as it would be processed inside an investment bank, covering activities across the front office, middle office, and back office. The goal of the system is to model how trades move from order placement to execution, risk validation, clearing, settlement, and finally profit and loss reporting.

The front-office component acts as an Order Management System (OMS), where clients can place buy or sell orders for financial instruments using market or limit order types. Orders are validated and routed to a simplified execution engine that matches trades based on price and time priority. Once an order is executed, it is converted into a trade with a unique trade identifier and execution details.

The middle-office layer focuses on risk management and trade validation. Before trades are finalized, the system performs margin and exposure checks to ensure that clients have sufficient funds and remain within predefined risk limits. Trades that fail these checks are rejected, closely reflecting real-world pre-trade risk controls used by banks.

Executed trades are then captured and stored in a PostgreSQL database as part of the bank’s official books. The back-office module simulates clearing and settlement by netting positions and applying a T+2 settlement cycle, where cash and securities balances are updated accordingly. Failed settlements are flagged to highlight operational risk scenarios.

To support ongoing monitoring, the system calculates mark-to-market profit and loss using simulated market price data. Both realized and unrealized P&L are computed at the client and portfolio level. Summary reports and dashboards provide visibility into open positions, margin utilization, settlement status, and daily P&L.

Overall, this project is designed to mirror real investment banking trading and operations workflows while demonstrating strong skills in system design, financial concepts, database management, and data analysis using Python, SQL, and Pandas.
