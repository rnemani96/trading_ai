import datetime

class Monitor:
    def log_trade(self, trade):
        print(f"[{datetime.datetime.now()}] TRADE:", trade)

    def alert(self, msg):
        print("🚨 ALERT:", msg)
