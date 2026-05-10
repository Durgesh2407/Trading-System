from bot.client import get_client

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    response = client.futures_create_order(**params)

    return response