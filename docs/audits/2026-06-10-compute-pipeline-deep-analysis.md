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
3. Does it violate **NO FITTING** (only the 3 calibrations are inputs)? Are there
   hardcoded CODATA literals or duplicated magic values instead of importing from
   a central registry (`codata_constants` / `content/values/registry.ts`, using
   canonical validation aliases like `M_P_MEV_VALIDATION`)?
4. Is it **wired** (consumed by the mass/binding sweep + L1/L2 dashboards) or
   orphaned?
5. Can it be **optimized** without losing precision (Rust port, batched FFI,
   caching, closed form replacing sympy)? Do long-compute scripts (>5 min) adhere
   to the Long-compute logging discipline (units/sec, wall elapsed, ETA)?

## 1. Axis A — FLOAT64 violations (canonical path)

_(pending — float64 audit pass)_

## 2. Axis B — FITTING / numerology leaks  ✅ clean on production

**Verdict: 0 production-leak violations.** The NO-FITTING / 3-calibration
discipline holds on every live prediction path. Genuine fits all sit in
`_deprecated/`, `probe_*`, §3b-cond conjecture classes, or carry truth-in-naming
suffixes (`*_FITTED_FROM_CODATA`, `*_AUDIT_ONLY`). Repo has strong self-audit
infra (`cal4_disguise_hunt.py` scans 972 scripts). LP/SDP `scipy.optimize`
solves and `lstsq` *structure-diagnostics* are correctly not fits.

**3 REVIEW-tier fixes (label/kind only — none wired to a prediction):**

| id | item | file | fix |
|----|------|------|-----|
| R1 | `prop:term6-binding-density` is `kind: proposition` but embeds a 2-param AME fit (α≈339.4, β≈1.14 MeV; R²=0.84). Producer `term6_scaling_heavy.py` is in `_deprecated/`; production binding uses the open `B=m_e·Σ y_λ χ^λ Δ_λ`, does NOT consume α/β. Lean side already correct (§3b-cond `class`). | `mass-theory/term6-binding-density.{md,ts,lean}` | recategorize proposition→conjecture (or §3b-cond banner) + move α,β to `authorNotes` |
| R2 | `qbeta_physics.py` hardcodes `c_3=-2`, `c_4=b²+½` under comment "STRUCTURAL PREDICTIONS, not empirical fits" — contradicts settled near-match tiering. Only caller is a `_deprecated/` probe (dormant). | `folio-assistant/computations/qbeta/qbeta_physics.py:95-114` | comment → proved(`c_2`)/near-match(`c_3,c_4`) tiering, or move to `probes/` |
| R3 | a derivation `.md` calls `c_3=-2` "exactly … canonical" — overstates settled status (dashboard: Q_β misses 100× by 164×). | `stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md:117-124` | soften to proved/near-match tiering |

These are documentation/kind corrections; no witness or dashboard number
changes. Scheduled in the synthesis as low-risk cleanups (R1 has content-kind
propagation implications — handle with care).

## 3. Axis C — Canonical-chain wiring map + orphans + gaps

_(pending — compute-integration audit pass)_

### 3a. Generalized-infra (`qou-mass`) state

**Finding (facade read, `qou-mass/src/qou_mass/api.py`):** the public
`predict(atom, observable)` is live but **reads vendored pre-computed shards**
(`canonical-isotope-witness-Z<NN>.witness.json`), described in-code as
**"current: f64 precision"** — a float64 leak at the facade layer. The live /
exact paths are stubbed:

| API | current state | gap |
|-----|---------------|-----|
| `predict(atom, q=…)` | `NotImplementedError` for `q != q_0` | no custom-q |
| `predict(..., method="rust_canonical_chi")` | declared in `Method` literal, not implemented | **the hook for the merged scalable χ** |
| `compute_tr_M(Z,N)` | reads vendored `canonical-mass-table-extended.witness.json`; raises outside vendored range | no live recompute |
| `canonical_braid(Z,N)` | explicit word only p..⁶Li; else empty generators | no live word for arbitrary A |

**Conclusion → top Phase-2 item.** The merged scalable transfer-matrix χ +
`tr_m_atom_via_transfer` (#2097, `270801d6`) produce **50-dps mpmath** `χ^λ`
and canonical `tr_M(atom/free)` for **any A** with no float64. Wiring that as
the live `compute_tr_M` / `rust_canonical_chi` method (and a live
`canonical_braid` via `atom_braid_word_3A`) makes `predict(Z,N)` answer for an
**arbitrary nuclide from the outset at exact precision** — simultaneously
closing the generalized-infra goal AND the facade-layer float64 leak. This is
the spine of the whole tranche.

## 4. Axis D — Performance hotspots + FFI roundtrips

_(pending — compute-audit / ffi-roundtrip pass)_

## 5. Synthesis — prioritized work-plan

_(filled after the four axes land — ordered by accuracy impact, then wall-time
saved, with NO-FLOAT64 / NO-FITTING gates on every item)_

## 6. Execution log

_(commits referenced here as the plan is worked)_
