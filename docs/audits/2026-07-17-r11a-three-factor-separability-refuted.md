# R11-a — the 3-factor multiplicative closure of the ladder miss is REFUTED; the structure is additive 2-channel

**Date:** 2026-07-17 · **Task:** R11-a (round-11, follows R10) · **Bean:** `z2bn` · **Coordinates with** [#3808](https://github.com/litlfred/qou/pull/3808)
**Probe:** [`computations/deltalambda/r11a_three_factor_separability_probe.py`](../../computations/deltalambda/r11a_three_factor_separability_probe.py)
**Witness:** [`r11a-three-factor-separability.witness.json`](../../computations/deltalambda/r11a-three-factor-separability.witness.json) (allPassed, witness-fed from R10 — no recompute)
**Discipline:** derive-or-refute / falsification (`compute-author.md §3.3`); scope-(a); no fit, no wiring.

## Context

R10 ([`deuteron-ladder-falsification.md`](2026-07-14-deuteron-ladder-falsification.md)) established
that the Model-G miss `miss(k,A_light) = deficit − [3b·C(k,2)·[k≥3] + k·A_light·b]` peaks at a
**fixed k=3** across all three `(kα)+X` ladders (X = n/d/t, A_light = 1/2/3) — the 3-α Brunnian
onset, not a resonance at `k = A_light`. Round-11 (#3808) proposed the residual miss factorizes as a
**3-factor product** `miss(k,A_light) = E(k)·amp(A_light)·parity(k)` — a fixed k-envelope, an
A_light-amplitude, a bar-parity fall. This note tests that separability directly.

## The miss table (from the R10 witness, MeV)

| k | A_light=1 | A_light=2 | A_light=3 |
|--:|--:|--:|--:|
| 1 | — | −0.090 | 0.122 |
| 2 | 0.009 | 2.807 | 6.440 |
| 3 | **2.838** ★ | **5.818** ★ | **8.048** ★ |
| 4 | 1.377 | 1.632 | 2.679 |

## (T1) Multiplicative separability — REFUTED

If `miss = E(k)·amp(A_light)`, then normalizing each ladder by its own k=3 peak yields an
A_light-**independent** envelope `Ê(k) = miss(k,A)/miss(3,A)`. It is not:

| k | Ê \| A=1 | Ê \| A=2 | Ê \| A=3 |
|--:|--:|--:|--:|
| 2 | 0.003 | 0.482 | 0.800 |
| 3 | 1.000 | 1.000 | 1.000 |
| 4 | 0.485 | 0.281 | 0.333 |

The normalized k=2 envelope runs **0.003 / 0.482 / 0.800** across A_light = 1/2/3 — the k=2 weight
*grows* with A_light rather than being fixed. So the miss is **not** a clean `E(k)·amp(A_light)`
product; multiplicative separability is refuted.

## (T2) Brunnian triple hard-gate — REFUTED as the *sole* mechanism

The Milnor triple-linking invariant `μ̄₁₂₃` is the first genuinely 3-cluster topological invariant:
pairwise linking (k ≤ 2 α-pairs) cannot detect a Borromean triple (all pairwise `lk = 0` yet
`μ̄₁₂₃ ≠ 0`). A **pure** triple-gate would force `miss(k<3) = 0`. But the miss is **nonzero at k=2**
(¹⁰B 2.81, ¹¹B 6.44 MeV), so a triple-linking-only envelope is excluded. The `μ̄₁₂₃` structure
grounds the k=3 **peak** (the first irreducible 3-cluster term, hence the interior maximum) — it is
not a hard gate.

## Net (scope-(a))

The proposed **3-factor multiplicative closure is refuted**. The honest structure is
**additive 2-channel**:

- a **k=3-peaked 3-cluster term** (the Brunnian `μ̄₁₂₃` onset — grounds the fixed peak / interior
  maximum), plus
- an **A_light-graded pairwise term** whose k=2 weight grows with A_light (a pairwise-detectable
  channel present below the triple onset).

This is consistent with R9's P1 (additive non-negative cone) and P2 (monotone-saturating) interior-
maximum prunes, which **stand**. It **narrows R11-a**: the derivation target is the *additive split*
(a 3-cluster term ⊕ a pairwise term), **not** a multiplicative product. No fitted constant is wired;
specific magnitudes are not interpreted (numerology guard).
