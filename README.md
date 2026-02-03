# AI Trading System
Long-term + intraday RL-based trading system


What this project does (current state)
1️⃣ Fully automated decision-making

✔ Fetches market data
✔ Builds indicators & features
✔ Detects market regime (trend / range / no-trade)
✔ Selects stocks for long-term investing
✔ Chooses intraday strategy automatically

➡️ No manual stock picking

2️⃣ Multi-agent intelligence (core strength)

SectorAgent → analyzes stocks sector-wise

ChiefAgent → final authority, picks best 5 stocks

IntradayRegimeAgent → decides when & how to trade

Execution layer → sends orders to OpenAlgo

➡️ Works like a small autonomous trading desk

3️⃣ Human interaction required (minimum)
Step	Needed?
Start OpenAlgo	✅ once
Start trading_ai	✅ once
Strategy selection	❌
Stock selection	❌
Trade timing	❌
Order placement	❌

👉 After start → fully automatic

What it CANNOT do yet (important)

❌ Auto-start on system boot
❌ Auto-kill on abnormal loss
❌ Capital rebalancing
❌ Compliance / audit logs
❌ Multi-broker failover

(These are Phase-2 / Phase-3 features)

Can it trade with almost zero human interaction?
✅ Answer: YES (in paper mode now)
⚠️ Live trading: YES, with safety limits

Once running:

Trades autonomously

Stops trading in no-trade regimes

Follows fixed rules

Uses OpenAlgo as execution firewall

What this project really is

Not a bot.
Not a script.

👉 It’s a foundation of an autonomous trading company

Think:

Analysts → agents

CIO → chief agent

Trader → execution engine

Risk desk → upcoming module

Final verdict (architect view)

✔ Safe to run in paper mode
✔ Architecturally correct
✔ Extendable to hedge-fund-grade system
✔ Human acts only as supervisor

next logical upgrades:

🔒 Risk / failsafe agent

📉 Daily drawdown guard

🤖 Auto-restart watchdog

📊 Performance dashboard
