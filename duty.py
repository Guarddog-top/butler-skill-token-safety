"""Pre-trade token safety check via GuardDog API.

Checks a token against 4 live data sources before trade execution.
Returns PASS/WARN/BITE verdict. BITE = abort trade.

Conventions: stdlib only; config via params; fail-open on API errors.
"""
import json
import os
import urllib.parse
import urllib.request

GUARDDOG_BASE = os.environ.get("GUARDDOG_BASE", "https://api.guarddog.top")
TOKEN = os.environ.get("ATG_TOKEN", "")  # optional; free 50/day without


def run(token_address: str, chain: str = "base") -> dict:
    """Check token safety. Returns verdict with reasons."""
    params = urllib.parse.urlencode(dict(chain=chain, target=token_address))
    url = GUARDDOG_BASE + "/v1/check?" + params
    req = urllib.request.Request(url)
    if TOKEN:
        req.add_header("X-ATG-Token", TOKEN)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            result = json.loads(r.read())
        # BITE = BLOCK = abort
        result["abort"] = result.get("verdict") == "BLOCK"
        return result
    except Exception as e:
        # Fail-open: API down = allow trade + note
        return dict(verdict="PASS", risk_score=0,
                    reasons=["guarddog-unreachable(fail-open)"],
                    covered=True, data_limited=True,
                    unknown_token=False, abort=False,
                    degraded=str(e)[:80])


if __name__ == "__main__":
    addr = os.environ.get("TOKEN_ADDRESS", "")
    chain = os.environ.get("CHAIN", "base")
    if not addr:
        print("TOKEN_ADDRESS required")
        raise SystemExit(1)
    print(json.dumps(run(addr, chain), indent=2))
