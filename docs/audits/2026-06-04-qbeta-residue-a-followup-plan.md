# Residue-A follow-up — sl_6 control · 2×1.03 residual · transcendental reframe

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-residue-a-followup-2026-06-04`)
**Status:** PLAN (compute pending)
**Predecessor:** [PR #1797 — mixed chains NEGATIVE](./2026-06-04-qbeta-mixed-chains-verdict.md)

## Context

All **four** catalogued categorical residue-A families are now NEGATIVE:

| Family | Verdict |
|---|---|
| single-chain partitions (n ≤ 5) | NEGATIVE (PR #1772, #1787) |
| Demazure chars at ω_j (sl_3/4/5) | NEGATIVE (PR #1787) |
| ℏ_q^N / b^N·ℏ_q^M / Q_β·ε (38) | NEGATIVE (residue-A probe) |
| mixed Wenzl × Kashaev × Kashiwara | NEGATIVE (PR #1797) |

The author chose **three** follow-up directions. This PR runs all three.

| Target | Value |
|---|---|
| Residue A | `1.804e-15` (PR #1727; simple pole, fibre-level, anchor-independent) |
| ℏ_q | `(q - 1)/q` (NEVER hard-coded) |
| Prefactor | `A / ℏ_q^15 ≈ 2.0717` at proton anchor |

## Direction 1 — sl_6 Demazure control

Extend the PR #1787 real-D_i Demazure-character probe to **sl_6**
(720 permutations × 5 fundamental weights ω_1…ω_5 ≈ 3600 candidates).
Reuses `sample_reduced_words`, `demazure_char_at_word`,
`report_proximity` verbatim. **Expected LOW yield** — sl_3/4/5 showed
no scaling toward target — so this is a *control* that closes the
higher-rank door, not a hopeful probe. TIERED; cross-anchor any
NEAR-1PCT.

## Direction 2 — the 2×1.03 residual

The prefactor `A/ℏ_q^15 ≈ 2.0717` keeps factoring as `2 × 1.0359`
across unrelated families (here `2·Li_2^q(ℏ_q)`, in PR #1787 `1+q`, in
the residue probe `2·ℏ_q^15·(1+ε)`). Treat the **`2`** as a structural
doubling (candidate `[2]_q → 2` at q→1) and characterise the **residual
`R = A/(2·ℏ_q^15) ≈ 1.0359`** as its own object: TIERED-test R against
canonical small q₀-factors (`[2]_q/2`, `1+h²`, `1+ℏ_q·c`, `b`, `√q`,
products) and report whether any reaches NEAR-1PCT. **Anti-fit
discipline:** report TIERED; a NEAR-FUZZY match is NOT a closure; no
free parameters.

## Direction 3 — transcendental / period reframe

Hypothesis: A is **not** a finite categorical (algebraic-at-q₀)
invariant but a **period** — e.g. a ℚ-linear combination of
`{1, π, π², ζ(3), Catalan G, log q₀, Li_2(ℏ_q), Bloch-Wigner D(q₀),
Vol(4_1), Vol(Borromean)}`. Run an integer-relation (PSLQ /
`mpmath.pslq`) probe at high precision on the prefactor `A/ℏ_q^15` and
on A itself against this period basis. A clean low-height relation is a
positive signal for the period framing; no relation up to a height
bound is evidence A is "generic" w.r.t. these periods. Either way an
**audit doc** frames the reframe and records the PSLQ outcome with its
height/precision bound (so it is falsifiable, per the
declare-open discipline).

## Anti-pattern guards (STRICT)

- TIERED reporting; no ansatz/fit at NEAR-FUZZY or coarser.
- Cross-anchor before any structural claim.
- ℏ_q from `(q - 1)/q`, never hard-coded.
- PSLQ relations reported with explicit height + precision bound
  (a relation found only at huge height is not a closure).
- Diagnostic-only; no production wiring; no λ_scale; no Δ_λ closure.
- 4-grep corpus check before any "open"/"closed" declaration.

## Deliverables

```
docs/audits/
  2026-06-04-qbeta-residue-a-followup-plan.md    # this file
  2026-06-04-qbeta-residue-a-followup-verdict.md # combined TIERED verdict
computations/qbeta/
  qbeta_residue_followup_sl6_demazure.py
  qbeta_residue_followup_residual_2x.py
  qbeta_residue_followup_pslq_periods.py
  (+ auto-emitted *.witness.json per script)
```
