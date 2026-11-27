import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.BraidKnot.A3OperatorCombinerMagnitude — the operator-valued branching
combiner supplies **zero** additional magnitude over the scalar Markov trace

## The A=3 magnitude question (ROUTE 1)

The A=3 triton `Δ_λ` magnitude factor `r* = μ₃/c₃ ≈ 1.585` (μ₃ = +0.4708 the
target simplex moment; c₃ = 0.297 = E₀·(1 − τ_Borr) the *derived* single
Markov-trace near-miss) is bracketed out of every single-Markov-trace
ingredient. The surviving hypothesis (bean `qou-tnvz`) is that the missing
`1.585×` is a genuinely **many-body / cross-channel** object.

**ROUTE 1** proposed: replace the scalar `Σ_λ y_λ χ_λ` Frobenius pairing with
the **operator-valued branching combiner** — the `H₉ → H₆ → H₃` (peel one
nucleon at a time) Wenzl branching, *keeping the operator (matrix) structure*
instead of collapsing to a scalar trace at each level — on the premise that a
single trace *loses* the cross-channel information the branching *retains*.

## What this file proves — the structural claim, formalized FIRST

The premise is **false at the observable level**, and this file proves *why* and
*by how much*.

The observable read off the operator-valued combiner is a **cyclic, additive
trace** `τ` of the assembled operator, sliced by the isotypic projector family
`{P i}` of the branching (`i = (ξ,ν)`). The invariant that governs it is the
**partition-of-unity trace collapse**:

  `τ X = Σ i, τ (P i · X · P i)`      (`trace_partition_collapse`)

for any orthogonal resolution of unity (`P i · P j = 0` for `i ≠ j`, `Σ P i = 1`)
and any cyclic additive `τ`. Consequently the block-resolved readout of the
operator combiner **equals the scalar Markov trace exactly** — the per-block
weight is *identically 1*:

  `operatorCombinerReadout = τ X`      (`operatorCombiner_eq_scalarTrace`)

so retaining the operator structure supplies a factor of **exactly `1.0`**
(0 % of the needed `+58.5 %`; gap identically `0`).

The **only** way a block decomposition can produce a value `≠ τ X` is a
**non-uniform per-block weight** `w i ≠ 1` — and the deviation is exactly

  `(Σ i, w i · τ (P i·X·P i)) − τ X  =  Σ i, (w i − 1) · τ (P i·X·P i)`
                                       (`weightedReadout_sub_trace`)

which vanishes when the weights are uniform (`weightedReadout_eq_of_uniform`) and,
contrapositively, a magnitude change *forces* a non-uniform weight
(`magnitude_change_forces_nonuniform_weight`).

That non-uniform per-block weight is **precisely the `Δ_λ` per-partition weight**
— a *different functional* than the trace, not something any trace-based operator
combiner "retains". A `Δ_λ` fixed by inverting `μ₃` is a **fit** (the standing
`Δ_λ` gate), not supplied by ROUTE 1. Verdict: **scope-(b) structural exclusion**;
cited invariant = the partition-of-unity trace collapse below.

## Scope and base ring (§7c)

Generic commutative ring `R` as the trace codomain, generic (noncommutative)
ring `A` as the operator algebra. No archimedean structure, no `ℝ`, no fitted
constant. Idempotency of `P i` is **not** assumed — only an orthogonal
resolution of unity — so the identity holds for any resolution, the isotypic
projectors being the intended case (mirrors `InterfaceOperatorBlockDiagonal`).

## References

- Bean `qou-tnvz` (surviving-route record); `qou-jv64` (this ROUTE-1 task).
- `QOU/BraidKnot/InterfaceOperatorBlockDiagonal.lean` (the `W·I·β` block-diagonal
  companion; this file is the `W = β = 1` magnitude corollary + weighted-readout
  deviation, which that file does not state).
- `computations/canonical_tr_m_via_branching.py` (branching ≡ transfer to 4.7e-15
  — the numerical shadow of `operatorCombiner_eq_scalarTrace`).
- `computations/a_operator/canonical_tr_m_combiner_crosscheck.py`.
- [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.BraidKnot.A3OperatorCombinerMagnitude

open Finset

variable {R : Type*} [CommRing R]
variable {A : Type*} [Ring A]
variable {ι : Type*} [Fintype ι]

/-- **Partition-of-unity trace collapse (the cited invariant).**

Let `{P i}` be an orthogonal resolution of unity in `A` (`P i · P j = 0` for
`i ≠ j`, `Σ i, P i = 1`), and let `τ : A →+ R` be cyclic. Then the trace of any
`X` equals the sum of its diagonal block compressions:

  `τ X = Σ i, τ (P i · X · P i)`.

Off-diagonal blocks vanish under the cyclic trace; the per-block weight is
identically `1`. This is the `W = β = 1` specialisation of the interface-operator
block-diagonality, isolated here as the magnitude invariant for ROUTE 1. -/
theorem trace_partition_collapse
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (X : A) :
    τ X = ∑ i, τ (P i * X * P i) := by
  -- Off-diagonal blocks vanish under the closed (cyclic) trace.
  have offdiag : ∀ i j, i ≠ j → τ (P i * X * P j) = 0 := by
    intro i j hij
    have rot : τ (P i * X * P j) = τ ((P j * P i) * X) := by
      rw [hcyc (P i * X) (P j)]
      congr 1
      noncomm_ring
    rw [rot, horth j i hij.symm]
    simp
  -- Expand `X = (Σ P i) · X · (Σ P j)` and keep only the diagonal.
  have key : (∑ i, P i) * X * (∑ j, P j) = ∑ i, ∑ j, P i * X * P j := by
    rw [Finset.sum_mul, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.mul_sum]
  have hX : X = (∑ i, P i) * X * (∑ j, P j) := by rw [hsum, one_mul, mul_one]
  -- Rewrite only the left-hand `X` (the right-hand side already carries its
  -- own `X` in the diagonal compressions and must be left untouched).
  have step1 : τ X = ∑ i, ∑ j, τ (P i * X * P j) := by
    conv_lhs => rw [hX, key]
    rw [map_sum]
    simp_rw [map_sum]
  rw [step1]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [Finset.sum_eq_single i
        (fun j _ hji => offdiag i j hji.symm)
        (fun hi => absurd (mem_univ i) hi)]

/-- The observable read off the operator-valued branching combiner: the sum of
the diagonal per-block trace compressions `τ (P i · X · P i)`. This is the
"keep the matrix structure, then close the trace" readout. -/
def operatorCombinerReadout
    (τ : A →+ R) (P : ι → A) (X : A) : R :=
  ∑ i, τ (P i * X * P i)

/-- A general **weighted** block readout with per-block weight `w i : R` — the
shape any `Δ_λ`-type per-partition weight would take. `w ≡ 1` recovers the plain
operator-combiner readout. -/
def weightedBlockReadout
    (τ : A →+ R) (P : ι → A) (w : ι → R) (X : A) : R :=
  ∑ i, w i * τ (P i * X * P i)

/-- **ROUTE 1 conclusion — the operator combiner supplies zero extra magnitude.**

The block-resolved readout of the operator-valued combiner equals the scalar
Markov trace exactly:

  `operatorCombinerReadout τ P X = τ X`.

Hence keeping the operator (matrix) structure through the branching multiplies
the scalar trace by a factor of **exactly `1`**: it reproduces `c₃`, never `μ₃`,
and supplies `0` of the missing `r* − 1 ≈ 0.585`. -/
theorem operatorCombiner_eq_scalarTrace
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (X : A) :
    operatorCombinerReadout τ P X = τ X := by
  rw [operatorCombinerReadout, ← trace_partition_collapse τ hcyc P horth hsum X]

/-- **The deviation of a weighted readout is carried entirely by the weight.**

  `(Σ i, w i · τ (P i·X·P i)) − τ X = Σ i, (w i − 1) · τ (P i·X·P i)`.

The right-hand side is `0` when every `w i = 1`; a magnitude change is possible
*only* through a non-uniform per-block weight. This is the "by how much" answer:
the operator structure contributes nothing on its own — all of `μ₃ − c₃` must
live in a per-block weight `w i ≠ 1` (the `Δ_λ`). -/
theorem weightedReadout_sub_trace
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (w : ι → R)
    (X : A) :
    weightedBlockReadout τ P w X - τ X
      = ∑ i, (w i - 1) * τ (P i * X * P i) := by
  rw [weightedBlockReadout, trace_partition_collapse τ hcyc P horth hsum X,
      ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  ring

/-- Uniform per-block weights (`w ≡ 1`) recover the scalar trace: no magnitude
change. -/
theorem weightedReadout_eq_of_uniform
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (w : ι → R)
    (hw : ∀ i, w i = 1)
    (X : A) :
    weightedBlockReadout τ P w X = τ X := by
  have h := weightedReadout_sub_trace τ hcyc P horth hsum w X
  have hzero : ∑ i, (w i - 1) * τ (P i * X * P i) = 0 := by
    refine Finset.sum_eq_zero (fun i _ => ?_)
    rw [hw i]; ring
  rw [hzero] at h
  exact sub_eq_zero.mp h

/-- **Contrapositive — a magnitude change forces a non-uniform weight.**

If a weighted block readout differs from the scalar trace, then some per-block
weight is `≠ 1`. The operator-valued combiner alone (`w ≡ 1`) can never do it;
the missing `1.585×` requires a genuine `Δ_λ`-type per-partition weight — a
different functional than the trace, and (per the `Δ_λ` gate) one that may only
be *derived*, never fitted. -/
theorem magnitude_change_forces_nonuniform_weight
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (w : ι → R)
    (X : A)
    (hne : weightedBlockReadout τ P w X ≠ τ X) :
    ∃ i, w i ≠ 1 := by
  by_contra hall
  push_neg at hall
  exact hne (weightedReadout_eq_of_uniform τ hcyc P horth hsum w hall X)

end QOU.BraidKnot.A3OperatorCombinerMagnitude
