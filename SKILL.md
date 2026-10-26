---
name: token-safety-check
description: Check if a token is safe before trading — one call, PASS/WARN/BITE. Use before every buy/swap/approve to detect honeypots and scams.
version: 0.1.0
metadata: {"openclaw":{"emoji":"🐕"},"butler":{"tier":"on-demand","modes":["one-off"],"moneyMoving":false,"keywords":["token","safety","check","honeypot","scam","risk"],"requires":{"routes":[],"features":[],"gates":[],"bins":[]},"params":[{"name":"TOKEN_ADDRESS","type":"string","required":true,"ask":"Which token contract address?"},{"name":"CHAIN","type":"string","required":false,"ask":"Which chain? (eth/bsc/base/solana, default base)"}]}}
---

## When to use

Use this skill before your agent executes any token buy, swap, or approve. It checks the token against four live data sources (honeypot simulation, contract audit, liquidity structure, on-chain footprint) and returns a verdict in 23ms.

## What it returns

- **PASS** — token is clean, proceed with trade
- **WARN** — risk factors found, read `reasons[]` before deciding
- **BITE** (BLOCK) — honeypot/scam detected, **abort trade immediately**

## Safety rules

- BITE verdict = do NOT execute the trade, no exceptions
- `data_limited=true` means partial data was available; treat with caution
- `unknown_token=true` means no on-chain footprint; treat as WARN

## API

REST: `GET https://api.guarddog.top/v1/check?chain={chain}&target={address}`
MCP: `check_address(chain, address, action)` via `guarddog-mcp` npm package
Free 50 calls/day/IP, no signup.
