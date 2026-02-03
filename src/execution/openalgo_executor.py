import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("OPENALGO_BASE_URL")
API_KEY = os.getenv("OPENALGO_API_KEY")
CLIENT_CODE = os.getenv("OPENALGO_CLIENT_CODE")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

RATE_LIMIT = 1.2  # seconds
_last_call = 0


def _rate_limit():
    global _last_call
    delta = time.time() - _last_call
    if delta < RATE_LIMIT:
        time.sleep(RATE_LIMIT - delta)
    _last_call = time.time()


def place_order(symbol, side, quantity, order_type="MARKET"):
    _rate_limit()

    payload = {
        "clientcode": CLIENT_CODE,
        "symbol": symbol,
        "exchange": "NSE",
        "transactiontype": side,   # BUY / SELL
        "quantity": quantity,
        "ordertype": order_type,
        "producttype": "MIS",
        "price": 0
    }

    r = requests.post(
        f"{BASE_URL}/placeorder",
        json=payload,
        headers=HEADERS,
        timeout=5
    )

    return r.json()


def stay_flat():
    return {"status": "NO_TRADE"}
