import Mathlib.Tactic
import QOU.Eightfold.HeckeBraidingNonSymmetric

/-!
# QOU.MassTheory.TraceSignFlipRegime — the trace tower is sign-flip blind only where the braiding is symmetric

Bean `qou-bn8e`, continuing `QOU.MassTheory.InvolutionSelectionRule`. That file
proved the localisation argument's valid core and measured what it rests on: of
the four sectors `rem:isospin-mass-split-em-localisation` calls sign-flip
invariant, only the shell correction has a proof. This file settles the **trace
tower**, and the answer is not the one the remark needs.

## What was already in the corpus, and what this adds

**Found after writing this file, which is the wrong order.**
[`prop:chirality-dual-space-derivation`](../../../mass-theory/chirality-dual-space-derivation.md)
already records the symmetric-channel case, in the same notation:

  `τ_sym(σ) − τ_sym(σ⁻¹) = h`,  with  `h = q − q⁻¹`,

which is `trace_inv_sub_trace` below specialised to the one-dimensional
symmetric representation, where `σ` acts by `q` and `tr 1 = 1`. Anyone citing
this file should cite that one too.

What is genuinely added here is not the deviation but **when it vanishes**:

1. It holds for **any** `R`-linear functional on **any** algebra whose element
   satisfies the Hecke relation — the corpus statement is about `τ_sym`
   specifically, over `ℝ`.
2. The **iff**: `tr σ⁻¹ = tr σ ↔ q² = 1`, rather than the value of the
   difference alone.
3. The **tie to the braiding**: by `double_braiding_eq_one_iff`, that locus is
   exactly `σ² = 1`. So "the trace is sign-flip blind" and "the braiding is
   symmetric" are the *same condition*, which is what makes this a statement
   about the framework rather than an arithmetic identity.
4. Generic over a field, with the `ℝ` specialisation kept on the archimedean
   side of the §7c wall.

## The result

The Hecke relation itself forces the inverse of a generator:
`σ⁻¹ = σ − (q − q⁻¹)`. So for any linear functional `tr`,

  `tr σ⁻¹ − tr σ = −(q − q⁻¹) · tr 1`,

which vanishes exactly when `q² = 1`. By
`QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff` that is
exactly the locus where the braiding is **symmetric**. Hence:

> **The trace tower is sign-flip invariant precisely on the symmetric-braiding
> locus — and QOU sits off it.**

At the substrate `q₀ ≈ 1.10998` the flip changes the trace by
`(q₀ − q₀⁻¹) · tr 1 ≈ 0.209 · tr 1`, which is not a small correction.

## What this does to the remark

`rem:isospin-mass-split-em-localisation` lists the trace tower among the
functionals that *"respect these structural involutions"*. As a claim about the
mass functional **at the substrate**, that is false, and this file proves it.

The remark is not simply wrong, though, and the distinction is the whole point.
Its cited support, `prop:crystal-isospin-degeneracy`, is a statement about the
**crystal limit `q → 0`**, where — in that proposition's own words — *"the
crystal limit completely masks generator inversions"*. Both facts hold:

| regime | trace tower under generator sign-flip |
|---|---|
| crystal limit `q → 0` | **blind** (`prop:crystal-isospin-degeneracy`, conditional on `CrystalEigenlineSignBlind`) |
| substrate `q₀ > 1` | **not blind** — `trace_sign_flip_iff_symmetric` below |

So the defect is a **regime conflation**: a `q → 0` invariance is used to license
a claim about the functional at `q₀`. That is the `da-arity-conflation` shape
one level over from the two-involutions confusion recorded in
`InvolutionSelectionRule` — same family, different axis.

**Scope.** Scope-**(a)**, and pointed. This refutes *one premise* of the
localisation argument, at *one regime*. It does **not** refute the conclusion:
the mirror-isobar split may well be entirely Coulomb-sourced, and nothing here
bears on the co-Casimir or chirality sectors. What it removes is the right to
assert the trace tower drops out at the substrate without further argument.

**What it does not do.** It derives no `E_EM`, and it does not close
`qou-bn8e`. A selection rule constrains where a quantity lives; this one now
constrains it less than the corpus claimed.
-/

namespace QOU.MassTheory.TraceSignFlipRegime

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A]

/-- **The Hecke relation forces the inverse.** If `σ` satisfies the Hecke
relation and `τ` is a right inverse, then `τ = σ − (q − q⁻¹)`. This is the skein
relation `σ − σ⁻¹ = q − q⁻¹` (AGENTS.md §7a) read as a definition of `σ⁻¹`. -/
theorem inv_eq_sub (q : R) (σ τ : A)
    (hHecke : σ ^ 2 = algebraMap R A (q - q⁻¹) * σ + 1) (hinv : σ * τ = 1) :
    τ = σ - algebraMap R A (q - q⁻¹) := by
  have h : σ ^ 2 * τ = (algebraMap R A (q - q⁻¹) * σ + 1) * τ := by rw [hHecke]
  rw [pow_two, mul_assoc, hinv, mul_one, add_mul, mul_assoc, hinv, mul_one, one_mul] at h
  exact (eq_sub_of_add_eq' h.symm)

/-- **The sign-flip changes the trace by exactly `(q − q⁻¹) · tr 1`.** Stated for
any `R`-linear functional, so it applies to the Markov trace `tr_M` without
needing any of its Markov properties — the whole effect comes from the Hecke
relation. -/
theorem trace_inv_sub_trace (q : R) (σ τ : A) (tr : A →ₗ[R] R)
    (hHecke : σ ^ 2 = algebraMap R A (q - q⁻¹) * σ + 1) (hinv : σ * τ = 1) :
    tr σ - tr τ = (q - q⁻¹) * tr 1 := by
  rw [inv_eq_sub q σ τ hHecke hinv, map_sub, Algebra.algebraMap_eq_smul_one,
    map_smul, smul_eq_mul]
  ring

/-- **The trace tower is sign-flip blind exactly on the symmetric-braiding
locus.** With `tr 1 ≠ 0` — a Markov trace is normalised so this holds — flipping
a generator leaves the trace unchanged **iff** `q² = 1`, which by
`double_braiding_eq_one_iff` is exactly `σ² = 1`, the symmetric braiding.

So at any `q` where the braiding is genuinely non-symmetric, and in particular at
the substrate, the trace tower is **not** sign-flip invariant. -/
theorem trace_sign_flip_iff_symmetric (q : R) (σ τ : A) (tr : A →ₗ[R] R)
    (hq : q ≠ 0) (htr : tr 1 ≠ 0)
    (hHecke : σ ^ 2 = algebraMap R A (q - q⁻¹) * σ + 1) (hinv : σ * τ = 1) :
    tr τ = tr σ ↔ q ^ 2 = 1 := by
  have hdiff := trace_inv_sub_trace q σ τ tr hHecke hinv
  constructor
  · intro h
    rw [h, sub_self] at hdiff
    have hq' : q - q⁻¹ = 0 := by
      rcases mul_eq_zero.mp hdiff.symm with h' | h'
      · exact h'
      · exact absurd h' htr
    field_simp at hq'
    linear_combination hq'
  · intro h2
    have hq' : q - q⁻¹ = 0 := by field_simp; linear_combination h2
    rw [hq', zero_mul] at hdiff
    exact (sub_eq_zero.mp hdiff).symm

end QOU.MassTheory.TraceSignFlipRegime
