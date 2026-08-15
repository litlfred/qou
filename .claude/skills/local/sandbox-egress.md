---
name: sandbox-egress
description: Egress workarounds for firewalled sandboxes — github.com clones and PyPI work when a tool's own data host 403s. Route table + worked examples (mathlib, SnapPy/ptolemy). Read before declaring an external resource unreachable.
roles:
  - reader
  - collaborator
  - owner
---

# Sandbox egress — what's open, what's blocked, and the mirror route

**Rule (mirrors the AGENTS.md "route, don't give up" STRICT rule): a 403/
blocked-host error from a tool's OWN download path does NOT mean the data is
unreachable.** The sandbox proxy allowlists a few big hosts; most
project-specific data hosts are blocked. Before declaring an external
resource unavailable, walk the route table below.

## What is open (verified, 2026-08-15)

| Channel | Status | Evidence |
|---|---|---|
| `github.com` git clone / ls-remote / push | **OPEN** | mathlib4 shallow clone (AGENTS.md fallback); `3-manifolds/SnapPy` clone this session |
| PyPI (`pip install`) | **OPEN** | `pip install snappy` (3.3.2 + 30 deps) worked first try |
| `raw.githubusercontent.com` | usually open (rides the github allowance) | — |
| WebSearch (MCP) | OPEN (out-of-band) | used to locate repos |

## What is blocked (and does NOT mean "give up")

| Host | Blocked path | Working route |
|---|---|---|
| `release.lean-lang.org` | elan toolchain download | GitHub release asset (allowlisted) — see `lean-environment-setup.md` |
| Mathlib olean cache server (`lake exe cache get` 403) | prebuilt oleans | `lake-cache/*` orphan branches in THIS repo, or local mathlib clone |
| `ptolemy.unhyperbolic.org` | SnapPy `retrieve_solutions()` (403 on CONNECT) | **the snappy wheel itself ships certified magma fixtures** — see below |
| Arbitrary hosts via WebFetch (MCP) | `EGRESS_BLOCKED` | WebFetch rides the same proxy — do not assume it is out-of-band for data hosts |

## The route table (try in order)

1. **Is the data on a GitHub repo?** Clone it (`--depth 1`). WebSearch for
   `<project> github repository` to find the name; `git ls-remote
   https://github.com/<owner>/<repo>.git HEAD` is a cheap existence probe
   (public repos answer; remember private repos 404 unauthenticated).
2. **Is the data bundled in a pip package?** Many projects ship regression
   fixtures inside the wheel. Worked example: SnapPy's
   `snappy/ptolemy/testing_files/` contains **certified Magma
   primary-decomposition outputs for the `4_1` and `5_2` sl2 ptolemy
   varieties** — the exact data the firewalled ptolemy DB would have
   served — processable with
   `snappy.ptolemy.processMagmaFile.solutions_from_magma`. Consumed by
   `computations/qbeta/dt_crossknot_connection_count_certified_probe.py`
   (R1 connection counts 3/4, previously literature recall).
3. **Does the tool honor a data-URL env override?** SnapPy:
   `PTOLEMY_DATA_URL` (point at a local mirror / `file://` path). Lake:
   the `insteadOf` git redirect. Check the tool's source for
   `os.environ` reads before giving up.
4. **Proxy self-diagnosis**: `curl -sS "$HTTPS_PROXY/__agentproxy/status"`
   lists per-tool fixes and proxy state (see `/root/.ccr/README.md`).
   Never disable TLS verification or unset `HTTPS_PROXY`.
5. **Still blocked?** Record the residual precisely in the bean (which
   host, which path, what a network-open environment should run) — the
   qou-btvl handoff-note pattern.

## History

- 2026-08-15: ptolemy DB 403 nearly ended the D3 connection-count
  hardening as "needs open env"; the owner's hint ("egress github.com
  clone repos") led to route 1 → route 2: the data was in the installed
  wheel all along. Counts 3 (4₁) and 4 (5₂) certified locally, trace
  fields cross-checked. Skill created from that session so the next agent
  walks the table instead of stopping at the 403.
