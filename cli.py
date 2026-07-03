import argparse

from bot.orders import place_order
from bot.validators import validate_side, validate_order_type

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

args = parser.parse_args()

try:
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)

    if order_type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT orders require --price")

    print("\n========== ORDER SUMMARY ==========")
    print(f"Symbol    : {args.symbol.upper()}")
    print(f"Side      : {side}")
    print(f"Type      : {order_type}")
    print(f"Quantity  : {args.quantity}")

    if args.price:
        print(f"Price     : {args.price}")

    response = place_order(
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\n========== ORDER RESPONSE ==========")
    print("Order ID      :", response.get("orderId"))
    print("Status        :", response.get("status"))
    print("Executed Qty  :", response.get("executedQty"))
    print("Average Price :", response.get("avgPrice"))

    print("\n✅ Order placed successfully!")

except Exception as e:
    print("\n❌ Order Failed")
    print(e)