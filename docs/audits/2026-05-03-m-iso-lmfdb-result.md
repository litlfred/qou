# M_iso LMFDB lookup — result memo

**Date:** 2026-05-03
**Branch:** `claude/m-iso-lmfdb-lookup`
**Task:** Path A from
[`2026-05-02-m-iso-l-function-handoff.md`](2026-05-02-m-iso-l-function-handoff.md)
(lines 53-63) — match QOU substrate `M_iso` Frobenius coefficients
against the LMFDB modular-forms database to identify a weight-5
rational newform whose `a_p` agree with the table at the first seven
good primes.

## Verdict

**`query-error` — sandbox egress to `lmfdb.org` is blocked.**

All probes against `www.lmfdb.org` (HTTPS API, HTTPS human URL, HTTP,
`beta.lmfdb.org`, `robots.txt`) return HTTP 403 with a 21-byte body.
The TLS handshake completes, but the server certificate identifies as
`Anthropic sandbox-egress-production TLS Inspection CA` rather than
LMFDB's own cert — i.e. the 403 originates at the sandbox egress
proxy, not at the LMFDB origin.

Control probe to `api.github.com` returns 200, confirming the block
is host-specific.

No LMFDB content was retrieved. The lookup must be rerun from an
environment with allowlisted egress to `lmfdb.org` (typically: a
local Claude Code CLI session on the repo owner's workstation, or a
CI job with an explicit network policy granting `lmfdb.org`).

## Method

WebFetch and curl probes against the URL list captured in the
[witness](../../folio-assistant/computations/m-iso-lmfdb-lookup.witness.json)
under `method.endpoints_attempted`. Probe matrix:

| Variant | Result |
|---------|--------|
| `https://www.lmfdb.org/api/mf_newforms/?weight=5&dim=1&level={N}` for N ∈ {10, 20, 40, 50} | 403 |
| `https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/?level={N}&weight=5&dim=1` | 403 |
| `https://www.lmfdb.org/api/mf_newforms/?...&_format=json` | 403 |
| `https://beta.lmfdb.org/api/mf_newforms/?...` | 403 |
| `https://www.lmfdb.org/robots.txt` | 403 |
| `http://www.lmfdb.org/` (HTTP, not HTTPS) | 403 |
| `https://api.github.com/` (control) | 200 |

Headers / UA tested: default WebFetch UA; `Mozilla/5.0 (X11; Linux
x86_64) AppleWebKit/537.36`. No variation in response.

## Target signature (unchanged from handoff)

| p  | a_p   | reduction |
|----|-------|-----------|
|  3 |  −1   | good      |
|  7 |  13   | good      |
| 11 |  63   | good      |
| 13 | −285  | good      |
| 17 |  239  | good      |
| 19 | −315  | good      |
| 23 | −356  | good      |
|  2 | (in conductor) | bad |
|  5 | (in conductor) | bad |

Expected newform: weight 5 (or ≥ 4), rational Hecke field
(`dim = 1`), conductor `2^a · 5^b` with `a ∈ {1..6}`, `b ∈ {0,1,2}`.

## Recommendation

The half-day Path-A budget cannot be spent in this environment.
Three onward options, in priority order:

1. **Rerun Path A from an allowlisted host** (≈ 30 min wall-clock).
   The LMFDB JSON API still works as documented; the witness file
   already encodes the exact endpoint sequence to issue. Suggested
   loop:

   ```bash
   for N in 2 4 8 10 16 20 32 40 50 64 80 100 160 200 320 400 800 1600; do
     curl -fsS "https://www.lmfdb.org/api/mf_newforms/?weight=5&dim=1&level=$N" \
       | jq '.data[] | {label, level, dim, traces}' \
       >> lmfdb-w5-rational.jsonl
   done
   ```

   Then for each label whose `traces` array (0-indexed,
   `traces[k] = a_{k+1}`) contains
   `(-1, 13, 63, -285, 239, -315, -356)` at the 0-based indices
   `(2, 6, 10, 12, 16, 18, 22)` corresponding to primes
   `(3, 7, 11, 13, 17, 19, 23)`, fetch the q-expansion
   (`/{label}/?qexpansion=true`) to confirm.

2. **Use Sage / Pari locally** if LMFDB stays unreachable. Both ship
   newform tables sufficient to enumerate weight-5 rational newforms
   at every candidate conductor:

   ```python
   from sage.all import Newforms
   for N in [2, 4, 8, 10, 16, 20, 32, 40, 50, 64, 80,
             100, 160, 200, 320, 400, 800, 1600]:
       for f in Newforms(N, 5, names='a'):
           if f.hecke_eigenvalue_field() == QQ:
               aps = [f[p] for p in (3, 7, 11, 13, 17, 19, 23)]
               if aps == [-1, 13, 63, -285, 239, -315, -356]:
                   print(f, "MATCH")
   ```

3. **Escalate to Path B / Path C** if Path A returns no match.
   See the handoff doc lines 65-85 for the substantive Hecke-operator
   build-out (Path B, 2-3 weeks) and recursive-ascent extension to
   A ≥ 4 atoms (Path C). The combined Path B + C closes R6 step 4
   without needing LMFDB at all.

## Files

- Witness: [`folio-assistant/computations/m-iso-lmfdb-lookup.witness.json`](../../folio-assistant/computations/m-iso-lmfdb-lookup.witness.json)
- Memo (this file): [`docs/audits/2026-05-03-m-iso-lmfdb-result.md`](2026-05-03-m-iso-lmfdb-result.md)

No existing scripts modified; only the two new files above were
created on `claude/m-iso-lmfdb-lookup`.
