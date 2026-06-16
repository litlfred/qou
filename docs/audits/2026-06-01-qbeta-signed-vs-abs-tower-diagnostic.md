# Signed vs `|...|` mass-tower convention — diagnostic findings (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/hoefsmit-chi-lambda-q-evaluator-2026-06-01)
**Status:** DIAGNOSTIC — quantifies the `|...|` choice's structural impact.
**Triggered by:** user question 2026-06-01 "so we don't need the `|...|`?"

## TL;DR

The mass-tower convention `Φ_q(|tr_M(ξ)|)` (used in `mass_formula_6term`,
`mass_endomorphism`, `paper_six_term_isotope_sweep`, etc.) is a **structural
choice, not a convergence requirement**. At v = ±0.142 (typical Δtr_M
scale at q_proton):

- `Φ_q(+0.142) = 3.8092`
- `Φ_q(-0.142) = 0.2865`
- **Ratio Φ_q(+v)/Φ_q(-v) ≈ 13.3** — 92% per-term divergence

The `|...|` makes `Φ_q(-v) → Φ_q(+v)`, throwing away the bar-asymmetric
distinction in the Faddeev q-dilogarithm. If the categorical chain
should produce signed V̂ (and any is negative), the `|...|` is a
substantial structural correction.

## Test cases

| Sub-braid V̂ list | Φ_q(|...|) total | Φ_q(signed) total | rel diff |
|---|---|---|---|
| all positive small | 1.x | 1.x | **0%** |
| all positive medium | y | y | **0%** |
| mixed sign | 31.38 | 23.26 | **-25.9%** |
| all negative | 15.95 | 3.37 | **-78.9%** |
| one strong negative | 124.05 | 61.28 | **-50.6%** |
| realistic single-nucleon | 58.15 | 58.15 | **0%** (all V̂ > 0) |

**Key observation:** at single-nucleon level, all V̂ are positive
(tr_M(β_p) = +1.07, tr_M(β_n) = +0.92) — so `|...|` is no-op at level 0.
The structural difference only matters at **deeper levels** where
sub-braid V̂ values can turn negative (pair joints, jets).

## Where Φ_q(|v|) is used

```
computations/mass_formula_6term.py:141:        single += Phi_q(abs(v))
computations/mass_formula_6term.py:143:        pair += Phi_q(abs(vols[i] * vols[i + 1]))
computations/mass_endomorphism.py:145,255,264,273
computations/multi_level_jet_sum.py:68
computations/sweeps/paper_six_term_isotope_sweep.py:291
computations/brane_tower_isospin_diagnosis.py:178
computations/atom_level_wedderburn_tower.py:120
computations/mass_formula_6term_mpfr_50dps.py:254
```

Li_2^q context (binding — Q_β, Δ_λ) also uses `|...|` in places:
```
computations/_li_2_q_util.py:143,147
computations/binding_via_interface_knot.py:119  (Li_2_q(-mp.fabs(v)))
computations/hydrogen_qshuffle_compound.py:145
```

## Categorical context

Per `_phi_q_util.py` docstring (`prop:li2q-phiq-bar-symmetrization`):

> Φ_q is the **archimedean / post-τ** form of the q-dilogarithm —
> **bar-asymmetric**, lives on ℝ via the Faddeev state integral.

**bar-asymmetric** means `Φ_q(z) ≠ Φ_q(-z)` in general. The structural
content of Φ_q distinguishes signed inputs. Applying `|...|` BEFORE
Φ_q discards this bar-asymmetric distinction.

The framework's CHOICE to use `Φ_q(|v|)` rather than `Φ_q(v)` is not
justified by:

- **Convergence** — Φ_q converges for both signs when `|v| < q`
- **Positivity of mass** — m_atom is positive, but individual tower
  contributions can sum to positive even with mixed-sign Φ_q
- **Bar-asymmetry preservation** — `|...|` actively breaks bar-asymmetry

The justification (per per-braid mass-tower) is implicit: the formula
states `Φ_q(|tr_M(ξ)|)` as the convention. There is no audit doc
deriving this from a categorical principle. **OPEN STRUCTURAL QUESTION:**
should it be signed?

## Implication for c_k saga

INDIRECT. The c_3 saga lives in BINDING context (Q_β = m_n − m_p − m_e),
which uses **Li_2^q** (bar-symmetric), not Φ_q. The `|...|` in the
Φ_q mass-tower affects m_p and m_n individually; if their tower-V̂
lists have correlated sign patterns, the difference Q_β = m_n − m_p
might be insensitive to the `|...|` choice (correlated changes cancel).

A future probe could quantify this by:
1. Computing the actual sub-braid V̂ lists for β_p and β_n at q_proton
2. Computing m_p_abs, m_p_signed, m_n_abs, m_n_signed (4 values)
3. Comparing Q_β_abs = m_n_abs − m_p_abs vs Q_β_signed = m_n_signed − m_p_signed
4. Reporting whether the `|...|` choice changes Q_β at observable level

Out of scope for this diagnostic. Recorded as FOLLOW-UP.

## Anti-pattern guard

- ❌ Do NOT remove `|...|` from production scripts without categorical justification — this is a STRUCTURAL change with up to 92% per-term impact
- ❌ Do NOT propose `Φ_q(signed v)` as a new c_3 candidate — the c_k saga is in Li_2^q (binding), not Φ_q (mass)
- ✓ DO investigate the categorical derivation: should the per-braid mass tower's V̂ inputs be signed or `|...|`?

## What this PR does NOT do

- ❌ Does NOT modify any production wiring
- ❌ Does NOT resolve the c_3 saga
- ❌ Does NOT compute m_p_signed vs m_p_abs at full per-isotope V̂ resolution

## Files

- `computations/qbeta/qbeta_signed_vs_abs_tower_diagnostic.py`
- `computations/qbeta/qbeta-signed-vs-abs-tower-diagnostic.witness.json`
- `docs/audits/2026-06-01-qbeta-signed-vs-abs-tower-diagnostic.md` (this file)

## Cross-refs

- PR #1616 — Im(q) fibre/observable distinction (motivated this thread)
- PR #1626 — complex-c_3 fibre diagnostic (under-diagnostic finding)
- PR #1630 — Li_2^q × spectral cross-anchor completion
- `prop:li2q-phiq-bar-symmetrization` — the bar-asymmetric Φ_q vs bar-symmetric Li_2^q split
- `content/quantum-observable-universe/mass-theory/per-braid-mass-tower.md`
- `computations/_phi_q_util.py` — Φ_q implementation + convention
