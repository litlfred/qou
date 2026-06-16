# VolDensity(𝓑₃, q₀) refinement — research-direction scope

**Date:** 2026-06-01
**Branch:** `claude/vol-density-bz3-refinement-2026-06-01`
**Goal arm:** L2 100× closure on m_p, m_n, Δ_pn (3 of 4 misses share one root)
**Status:** **OPEN — research-grade**. Canonical reference: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md).

## The gap (current m_p baseline, 2026-06-01)

From `m_p_borromean_verification_50dps.py`:

| Observable | Predicted | CODATA | Δ |
|---|---|---|---|
| m_avg | 966.05 MeV | 938.92 MeV | **+2.89%** |
| Δm/M_N | 0.001377 | 0.001377 | +305 ppm (0.030 %) |
| m_p | 965.38 MeV | 938.27 MeV | +2.89% |
| m_n | 966.71 MeV | 939.57 MeV | +2.89% |
| Δm_pn | 1.330 MeV | 1.293 MeV | +2.86% |

**The 2.89% is on m_avg (the mass scale).** The p/n split is already 99.97% correct via substrate flavor (PR #690). All four misses (m_p, m_n, Δm_pn, derivatives) reflect this single gap.

## What's been REFUTED (do not redo)

Per [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) §"What canonical code does":

| Attempt | Status | Why refuted |
|---|---|---|
| Bring-Bloch tier 0-5 PSLQ | REFUTED | no integer combination matches (PR #904) |
| V_7 substrate (Strategy H) | REFUTED non-canonical | no `[4]_q`-normaliser substrate justification (PR #916, #952) |
| q^10 pentagon Bloch-Wigner | REFUTED | q-locality non-smooth (PR #951) |
| Unit-circle Bloch-Wigner class | REFUTED | literal-rfl loophole + substrate-q₀ coincidence (PR #952, #985) |
| Yekutieli per-cell curvature | PURGED 2026-05-24 | bijection NEGATIVE, Reading A was substrate-q₀ coincidence (PR #985) |
| **"Derive λ_scale from H_4 substrate" (general)** | **WRONG FRAME** | λ_scale is absorbed into VolDensity; no separate constant exists |

Strategies named "F/G/H to derive λ_scale from H_4 substrate" are explicitly called out as **wrong frame** in the canonical reference.

## Queued routes (research-grade)

1. **Bring color-tube quark-weighted averaging** ([`probe_pn_flavor_asymmetry.py`](../../computations/script-qa/probe_pn_flavor_asymmetry.script-qa.json) — script archived; QA sidecar surviving): per-sheet PL integration on Bring's surface (Scheme 4) gives `Δm_{n−p}` to ~0.14% — **but this closes the p/n split, not the m_avg gap**. Path forward: extend this color-tube formalism to the BASE mass scale of `VolDensity(𝓑₃)`, not just the difference. Open: define canonical color-sheet ↔ quark-flavor mapping (research-level — not explicitly in the paper).

2. **g·g' substrate-derived couplings** ([`SubstrateEWHypotheses.lean`](../../content/quantum-observable-universe/braids-and-knots/) class-conditional theorems): `g = π·h_0` matches SM 0.6535 to **+0.26%**; `v_framework / v_SM = log(6) = log(|S_3|)` matches at **−0.50%**. Open: rigorously derive π·h_0 from connection 1-form integration on substrate (Yekutieli MI machinery); upgrade `sorry` markers in SubstrateEWHypotheses.lean.

3. **Bloch-Wigner / dilogarithm cohomology higher-rank classes** — the unit-circle class was refuted, but the BlochWigner module under PR #956's Lake-wiring roadmap may admit a higher-rank class beyond the literal-rfl loophole. Phase-1b Lake-wiring queued.

4. **"Wenzl-annihilator-at-ζ_8 applied to H_4 Wedderburn"** (CAUTION) — the just-completed PR #1642 + PR #1649 work identified the level-2 SU(2) Wenzl annihilator killing partitions with first column ≥ 4. Applied to H_4, this kills `(1,1,1,1)` (the alternating sign partition), leaving 4 active partitions. The current Family A `λ_A = 5/2 + (3/4)h²` linking_weight uses H_4 Wedderburn data — restricting to Wenzl-active partitions might give a different value. **This is named "H_4 substrate" framing, which is explicitly called out as wrong frame in the canonical reference.** Risk of pattern-matching into a refuted direction is high. Needs explicit user direction before proceeding.

## Cross-references that survive

- Canonical reference: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- Cheat sheet §3 + §5: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- m_p baseline script: [`computations/m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py)
- Bloch-Wigner phase-1b Lake-wiring (PR #956 roadmap status): queued
- SubstrateEWHypotheses.lean — three conjectural matches with class-conditional theorems
- Mass-table comprehensive witness: `mass-table-comprehensive.witness.json` (per-isotope error budget)

## Why I'm pausing before launching compute

The canonical reference has 5+ explicit refutations + a warning that agents pattern-match on `λ_scale` derivation into refuted directions. This branch needs explicit user direction on which queued route to pursue before launching expensive compute (50-dps mpmath at H_4+ scales).

The three concretely tractable options:

A. **Bring color-tube extension to base mass scale** — extend the existing PR #690 substrate-flavor split formalism (which already gives 0.030% p/n split) to the m_avg scale. This is research-level (color-sheet ↔ flavor mapping not in paper) but builds on a proven foundation.

B. **g·g' substrate hypotheses upgrade** — close the `sorry` markers in `SubstrateEWHypotheses.lean` by deriving `g = π·h_0` from connection 1-form integration (Yekutieli MI machinery). Long-horizon but provides a concrete formal target.

C. **Bloch-Wigner higher-rank class** — phase-1b Lake-wiring under PR #956 roadmap.

D. **STOP — Topic 1 is genuinely research-grade and not productive in a session-bounded context.** Pivot to Topic 3 (Δ_λ binding) or Topic 5 (A≥3 per-rep collapse) instead.
