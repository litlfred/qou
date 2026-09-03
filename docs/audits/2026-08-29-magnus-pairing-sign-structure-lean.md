# The Magnus-pairing sign dichotomy, formalized — and where it meets the existing cyclic-trace infrastructure

**Date:** 2026-08-29 · **Bean:** `qou-dp32` (deuteron Magnus continuation) ·
**Lean:** [`QOU/MassTheory/MagnusPairingSignStructure.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MagnusPairingSignStructure.lean) ·
**Scope:** (a); formalizes a structural dichotomy; no MeV value claimed; nothing wired.

## Why this exists

The deuteron Magnus probe
([`deuteron_magnus_omega2_sign_probe.py`](../../computations/deltalambda/deuteron_magnus_omega2_sign_probe.py),
PR #6047) decided the second-order pairing `tr_M(ρ·Ω₂)` is **sign-indefinite** at A=2 —
the property the traceless interface curvature `F_q` could not have, because a traceless
curvature enters binding only through the non-negative quadrature `‖F_q‖²`. That was a
numerical verdict. This file supplies the **proved structural reason**.

## The corpus-grep that shaped it

Before adding any Lean, the checklist found that **one half of the dichotomy is already
proved** — so this file does not re-claim it:

- **Mathlib `matrix_trace_commutator_zero`** (`Mathlib/Algebra/Lie/Classical.lean`):
  `Matrix.trace ⁅X, Y⁆ = 0`.
- **`QOU.MassTheory.MilnorExactCoefficient.cyclic_trace_kills_iterCommTower`** and
  **`QOU.MassTheory.MilnorMagnusCoefficient.trace_magnusGen_realization_eq_zero`**: the
  cyclic trace annihilates the whole iterated-commutator (Magnus) tower.

These are the `ρ = I` control of the pairing: with the identity density the linear Magnus
term is identically zero. The probe's own control (`tr_M(Ω₂)=0`) is an instance of this
**already-proved** fact, not a new one.

## What is genuinely new here — the escape

The corpus proves the pairing vanishes *under the cyclic trace*. It does **not** anywhere
prove what happens under a **non-cyclic (density) weighting** — which is exactly what the
binding pairing is. This file adds that missing half:

| theorem | statement | role |
|---|---|---|
| `trace_commutator_eq_zero` | `(A·B − B·A).trace = 0`, generic `CommRing` | the control, restated locally (the general fact is the Mathlib/corpus lemmas above — **cited, not claimed**) |
| `trace_mul_transpose_nonneg` | `0 ≤ tr(F·Fᵀ)` over `ℝ` | **the wall**: the quadrature is a sum of squares, so `‖F_q‖²` can never be the negative-at-A=2 term |
| `magnus_pairing_sign_indefinite` | `∃ A B ρ₊ ρ₋, 0 < tr(ρ₊·⁅A,B⁆) ∧ tr(ρ₋·⁅A,B⁆) < 0` | **the escape** (new): one commutator, two densities, *both* strict signs — so the density-weighted pairing is not sign-fixed, unlike the quadrature |

`magnus_pairing_sign_indefinite` is the formal content of the probe's observation (2 partitions
positive, 7 negative): a *single* fixed commutator, paired against two densities, provably
realizes strictly opposite signs. That is the exact reason `qou-dp32` is LIVE where the
quadrature route `qou-jqof` was excluded by non-negativity.

## The connection to `qou-v7ro` (the open bridge)

This same structure is where the deuteron **binding-sign convention** — follow-on #1 of the
probe — actually lives, and it already has a bean. `qou-v7ro` records that the sign-carrying
Magnus/Milnor coefficient `μ̄(12…A) = ±1` survives as the **off-diagonal `(0,A)` matrix
coordinate** — a *non-cyclic* functional — while its cyclic trace is zero. That is the same
phenomenon as `magnus_pairing_sign_indefinite`: breaking cyclicity (a density weight, or an
off-diagonal projection) exposes a sign the cyclic trace hides. The open bridge — Magnus
`μ̄=±1` → the QOU Markov-trace deficit `D_A(h)` leading coefficient — **is** the binding-sign
convention this arc needs. It is not new territory; it is `qou-v7ro`.

## Honest scope

- Proves a **sign-structure dichotomy**, not a MeV value. No Δ_λ normalization; nothing wired.
- The control theorem is a **restatement** of existing Mathlib/corpus lemmas, cited above — not
  a novelty claim.
- Does not close `qou-v7ro`; it names the connection and adds the density-weighted escape as a
  standalone proved fact.

## Cross-references

- Probe + verdict: [`2026-08-29-deuteron-magnus-omega2-clears-non-negativity-wall.md`](2026-08-29-deuteron-magnus-omega2-clears-non-negativity-wall.md)
- Existing cyclic-trace tower: `QOU/MassTheory/MilnorExactCoefficient.lean`, `MilnorMagnusCoefficient.lean` (bean `qou-v7ro`)
