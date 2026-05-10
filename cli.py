import argparse
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
import logging
from bot.logging_config import *
parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()
args.symbol = args.symbol.upper()
args.side = args.side.upper()
args.type = args.type.upper()
try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.type, args.price)
    
    logging.info(
        f"Placing order | Symbol={args.symbol} "
        f"Side={args.side} Type={args.type} "
        f"Quantity={args.quantity} Price={args.price}"
    )
    print("\n===== ORDER REQUEST =====")

    print(f"Symbol        : {args.symbol}")
    print(f"Side          : {args.side}")
    print(f"Order Type    : {args.type}")
    print(f"Quantity      : {args.quantity}")

    if args.price:
        print(f"Price     : {args.price}")

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )
    logging.info(f"Order Response: {response}")
    print("\n===== ORDER RESPONSE =====")

    print(f"Order ID      : {response['orderId']}")
    print(f"Symbol        : {response['symbol']}")
    print(f"Side          : {response['side']}")
    print(f"Order Type    : {response['type']}")
    print(f"Status        : {response['status']}")
    print(f"Executed Qty  : {response['executedQty']}")
    print(f"Average Price : {response['avgPrice']}")
    print("\nOrder placed successfully.")

except ValueError as e:
    print(f"\nValidation Error: {e}")   
    logging.error(f"Validation Error: {e}")

except Exception as e:
    print(f"\nAPI Error: {e}")
    logging.error(f"API Error: {e}")