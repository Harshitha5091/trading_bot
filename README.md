 # Binance Futures Testnet Trading Bot

## Overview
This is a Python CLI application that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

## Features
- MARKET Orders
- LIMIT Orders
- BUY and SELL support
- Input validation
- Logging
- Error handling
- Modular code structure

## Setup

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```text
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## Usage

### Market Order

```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

## Assumptions

- Uses Binance Futures Testnet/Demo API.
- API credentials are stored in a `.env` file.