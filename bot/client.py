from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

client = Client(api_key, secret_key)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

server_time = client.get_server_time()
client.timestamp_offset = server_time["serverTime"] - int(time.time() * 1000)

def get_client():
    return client