---
# qou-rsrg
title: 'SEPARATE LANE (not a dependency): resurgence / Stokes as an INDEPENDENT check on S(0) = 3·S(π) = −3π²/2'
status: in-progress
pr: 8204
type: task
priority: low
tags:
    - 5two
    - resurgence
    - independent-check
    - qou-0yqu
    - reorg-2026-10-04
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-10-04T15:26:00Z
parent: qou-frzo
---

## What this is, and what it is NOT

**Not a route to proving the sum rule**, and nothing in the transport chain
depends on it. It is a proposal for an **independent check** on a relation the
lane currently knows only from its own machinery:

    S(0) = 3 · S(π) = −3π²/2

The factor **3** is suggestive: it is the number of saddles. The GGM
(Garoufalidis–Gu–Mariño) deformed 5₂ curve is the native frame in which the
saddle count and the Stokes data are the primary objects, so if that framework
independently produces the same factor, it is corroboration from machinery that
shares nothing with the envelope argument.

Independent corroboration is exactly what this lane's error record argues for:
twelve of its recorded failures are "a check that tests something adjacent to
what it claims", and the fix for that class is a check built on **different**
machinery, not a more careful version of the same one.

## Why it is low priority, stated honestly

* It is corroboration, not proof. Even complete success moves nothing from
  "verified to 80 dps, unproved".
* Alien calculus was considered earlier in this lane as an *attack* route and
  set aside — the Stokes constants for this curve are not known in closed form
  in a way that would give the identity, only in a way that would let one check
  it numerically. That assessment has not changed.
* The transport work (`qou-glbl`, `qou-asem`) and the analytic work
  (`qou-invr`) are all strictly more valuable per hour.

Recorded so it is not silently forgotten, and so nobody re-derives the "is
alien calculus a route?" question from scratch a third time.

## Attack vectors

### F1 — Check the saddle count against the factor 3, numerically, first
Before any theory: does the deformed curve have exactly 3 saddles on the
relevant contour at `x = 1` and at `x = −1`, and does the count change across
`φ₀`? If the count is not 3 at both ends, the "factor 3 = saddle count" reading
is wrong and this whole bean is a misreading worth closing. **Cheapest possible
test of the premise, and it should be done before anything else.**

### F2 — Stokes constants from the GGM curve, numerically
Compute the Stokes data for the 5₂ deformed curve at 50+ dps and check whether
the relation `S(0) = 3·S(π)` falls out of the connection formulae. Use
`mcp__sage__sage_faddeev_dilog` / `sage_eval` if the Sage MCP server is
available — it has the quantum-dilogarithm primitives and is *independently
implemented* from this lane's mpmath code, which is the point.

### F3 — Cross-check against the `S_leak` retraction on main
Main's `d4c9a36022` **retracted** an `S_leak` filter and added a generic guard
so it would not recur. Anyone entering this area should read that commit first —
it is the nearest prior art and it went wrong once already.

## ⚠ Guardrails, because this area invites overclaiming

* Any result here is a **check**, and must be reported as one. "Resurgence
  confirms the sum rule" is not a sentence that can be true at the current state
  of knowledge.
* The independence is the whole value. If the computation ends up reusing this
  lane's own root-finding or its `cLiTwoExt`, it is **not** an independent check
  and should not be described as one.
* `mpf("...")` constants, `int(nint(x))` not `round(float(x))`, and run
  `scripts/probe-float64-guard.py --diff` on anything new.

## Refs

* `qou-0yqu` (the sum rule), `qou-trns` (the transport this would corroborate)
* Route 32 (where `S(0) = 3·S(π)` was measured), Route 31 (the arc data)
* GGM: Garoufalidis–Gu–Mariño, deformed 5₂ curve
* Prior art on main: the `S_leak` retraction, `d4c9a36022`

**The 5₂ sum rule remains verified to 80 dps, unproved.**

## Progress Note (2026-11-16, PR #8204)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/QGevreyCauchyAndFWGGMStokes.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/qgevrey_cauchy_and_fw_ggm_stokes_probe.py` and witness `computations/probes/qgevrey-cauchy-and-fw-ggm-stokes.witness.json` (`scriptCommitSha: 8ee650e779786706f931cf4f825d18b2810370eb`, `scriptHash: 7ed9e0953101`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8204 (`6b9e46ecf45f518a03c0a6fb1de251bf59b285da`).
