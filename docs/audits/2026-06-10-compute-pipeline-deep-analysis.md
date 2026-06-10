# Compute-pipeline deep analysis + accuracy wiring / optimization

**Branch:** `claude/compute-pipeline-audit-generalize-2026-06-10`
**Date:** 2026-06-10
**Mandate (owner):** generalized infra so a user can request any nuclide /
observable from the outset; wire up everything possible for accuracy and
optimize; **NO FLOAT64** on the canonical path; **NO FITTING** beyond the
three calibrations (CAL-1 m_e, CAL-2 q₀, CAL-3 m_π).

This document is the synthesis target for a four-axis deep audit of the
current compute pipeline. Each axis is produced by a dedicated pass; the
findings are merged here into a single prioritized work-plan.

## 0. Scope and method

Anchored on `docs/canonical-derivation-cheat-sheet.md`. The audit asks, for
every script under `folio-assistant/computations/` and `tools/**`:

1. Is it on the **canonical path** (feeds a production observable) or
   exploratory?
2. Does it violate **NO FLOAT64** (canonical math must be mpmath/MPFR ≥50 dps)?
3. Does it violate **NO FITTING** (only the 3 calibrations are inputs)?
4. Is it **wired** (consumed by the mass/binding sweep + L1/L2 dashboards) or
   orphaned?
5. Can it be **optimized** without losing precision (Rust port, batched FFI,
   caching, closed form replacing sympy)?

## 1. Axis A — FLOAT64 violations (canonical path)

_(pending — float64 audit pass)_

## 2. Axis B — FITTING / numerology leaks

_(pending — production-vs-exploratory audit pass)_

## 3. Axis C — Canonical-chain wiring map + orphans + gaps

_(pending — compute-integration audit pass)_

### 3a. Generalized-infra (`qou-mass`) state

_(pending — `predict(Z, N) -> observable` facade assessment)_

## 4. Axis D — Performance hotspots + FFI roundtrips

_(pending — compute-audit / ffi-roundtrip pass)_

## 5. Synthesis — prioritized work-plan

_(filled after the four axes land — ordered by accuracy impact, then wall-time
saved, with NO-FLOAT64 / NO-FITTING gates on every item)_

## 6. Execution log

_(commits referenced here as the plan is worked)_
