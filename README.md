> **Check if a token is safe before trading — one call, PASS/WARN/BITE.**

Butler skill for Virtuals Protocol G.A.M.E. Checks tokens before trade
execution via GuardDog API (4 data sources, 23ms, Base chain default).

**BITE = auto-abort trade.** Fail-open on API errors.

```bash
TOKEN_ADDRESS=0x4200...0006 python duty.py
```

Free 50 calls/day/IP. https://api.guarddog.top/llms.txt
