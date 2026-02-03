def signal(row):
    # Ensure scalar values
    rsi = row["rsi"].iloc[0] if hasattr(row["rsi"], "iloc") else row["rsi"]
    ema20 = row["ema20"].iloc[0] if hasattr(row["ema20"], "iloc") else row["ema20"]
    ema50 = row["ema50"].iloc[0] if hasattr(row["ema50"], "iloc") else row["ema50"]

    if rsi < 30 and ema20 > ema50:
        return 1   # BUY
    if rsi > 70:
        return -1  # SELL
    return 0      # HOLD
