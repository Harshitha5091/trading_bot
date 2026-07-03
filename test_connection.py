from bot.client import client

try:
    account = client.futures_account()
    print("✅ Connected Successfully!")
    print("Wallet Balance:", account["totalWalletBalance"])
except Exception as e:
    print("❌ Connection Failed")
    print(e)