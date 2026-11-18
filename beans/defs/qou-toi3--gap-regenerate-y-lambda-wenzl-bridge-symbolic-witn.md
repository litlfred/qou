---
# qou-toi3
title: 'GAP: regenerate y-lambda-wenzl-bridge-symbolic-witness under D; 3 consumers still sympify its C strings past the gate'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T13:42:48Z
updated_at: 2026-10-04T15:20:21Z
parent: qou-5vkl
---


Surfaced closing qou-eea0 pass 2 (PR #4929).

`y-lambda-wenzl-bridge-symbolic-witness.json` is convention C — its entries
carry `sqrt(q)`, `q**(3/2)`, `q**(5/2)`, the half-argument variable of
`z = 1/(q^{1/2}+q^{-1/2})`. D cannot produce those; D stays inside ℚ(q).

`y_lambda_wenzl_bridge._cached_symbolic_agrees` (qou-wgta item 3) already
guards it — re-checks the cached string against the live numeric y_λ and
recomputes on disagreement. Its docstring calls that *"the right trade until
the witness is regenerated under D"*. That regeneration is this bean.

**The gate only covers callers that use the module API.** Four consumers open
the JSON and `sp.sympify` the strings themselves, so the gate never runs:

| consumer | line | status |
|---|---|---|
| `y_lambda_at_q0_cache.py` | 117 | **FIXED** in #4929 — now takes the number from `y_lambda_wenzl_bridge_numeric` |
| `delta_lambda_empirical_tabulation.py` | 316 | open — needs *symbolic*, so the numeric route does not substitute |
| `phase5/phase1c_proton_h3_symbolic_decomposition.py` | 155 | open — same |
| `regenerate_y_lambda_mpfr.py` | 105 | open — numeric at q₀, so the cache's fix applies directly |

**Why this is not "retire it as history".** qou-eea0 filed this witness under
*producer in `_deprecated/` → retire rather than regenerate; history is
allowed to be convention C provided it says so*. It is not history: it is a
live input to the four above. Retiring it would have left the nuclear layer
on C with every downstream producer reporting a clean migration — which is
exactly what pass 2's first sweep did (2 of 54 cleared, 90 producers "ok").

Generalises: **an orphaned witness is only safe to retire once you know
nothing live still READS it.** The orphan triage sorted by whether a producer
still exists, which answers who can *write* it.

**To close:** regenerate the symbolic table for n = 2..12 under D. The live
`y_lambda_wenzl_bridge.main()` writes a *different* file
(`y-lambda-wenzl-witness.json`) and only does symbolic for `n <= 4` because
sympy is slow at n >= 5; the only writer of this file is
`_deprecated/y_lambda_wenzl_bridge_extended.py:176`. So this needs either
un-deprecating that script or extending `main()`. Budget it: the module
docstring records ~6 s at n=3 and >60 s at n=6 for symbolic recompute, and
this goes to n=12 — long-compute logging discipline applies.
