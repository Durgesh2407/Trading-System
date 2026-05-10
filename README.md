# Binance Futures Testnet Trading Bot

A simplified Python trading bot for Binance USDT-M Futures Testnet.

This project allows users to place MARKET and LIMIT orders using a command-line interface (CLI) with proper validation, logging, and exception handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- CLI-based input using argparse
- Input validation
- Exception handling
- Logging of requests, responses, and errors
- Clean modular project structure

---

## Project Structure

```text
trading_system/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env