/-
# A bilinear pairing sees what every linear trace cannot

`qou-xzrj`. The Q_β ansatz's functional `epsNPq` has a part — 7.67 % of it at
the substrate anchor — that lies in the commutator subspace `[H,H]` of `H₃(q)`.
Every Markov trace annihilates that part, so no trace, no augmentation and no
character `χ^λ` can see it.

This file isolates the two structural facts behind the resolution, and the one
concrete witness that keeps the claim from being vacuous.

* `cyclic_annihilates_commutator` — why nothing linear-and-cyclic works.
* `trace_pairing_sees_a_commutator` — the **converse guard**: a bilinear pairing
  built from the *same* trace does not vanish on a commutator. Without this the
  first theorem would read as an impossibility rather than as a signpost.
* `eq_of_pairing_eq_of_nondegenerate` — uniqueness of a Riesz representative.
  This is what makes the representing element a *derived* object rather than a
  fitted choice, which is the whole epistemic weight of the result.

The base ring stays generic (`CommRing`) wherever the statement allows it, per
AGENTS.md §7c; the concrete witness is over `ℚ`, which is exact and carries no
archimedean content. Nothing here is specialised to `ℝ`.

## What this file does NOT claim

It does not derive `epsNPq`, does not show the single-wrap presentation is
forced, and does not close step 8's postulate. The *existence* of the
representative is a finite-dimensional dual-space fact instantiated by the
symbolic probe (`qbeta_trace_invisible_is_pairing_representable_probe.py`,
12/12, rank 6/6); what is proved here is that if it exists it is unique, and
that the pairing genuinely reaches the commutator subspace at all.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-! ## 1. Why nothing linear works -/

/-- A **cyclic** functional annihilates every commutator.

This is the obstruction in one line: `τ` need not be a Markov trace, an
augmentation or a character — cyclicity alone is enough to make the commutator
subspace invisible. So the failure is not a defect of a particular trace, and no
search over traces can repair it. -/
theorem cyclic_annihilates_commutator {A : Type*} [Ring A] (τ : A → R)
    (hτ : ∀ x y, τ (x * y) = τ (y * x)) (x y : A) :
    τ (x * y) - τ (y * x) = 0 := by
  rw [hτ]; ring

/-! ## 2. Why a bilinear pairing does -/

open Matrix in
/-- **The converse guard.** The trace *pairing* `⟨x,y⟩ = tr(x*y)` does not
vanish on the commutator subspace, even though the trace itself does.

Exhibited on `d = diag(1,-1) ∈ sl₂(ℚ)`, which is a genuine commutator
(`d = e*f - f*e` for the standard nilpotents, proved below):

* `trace d = 0` — invisible to the linear functional;
* `trace (d * d) = 2 ≠ 0` — visible to the bilinear one.

Without this theorem `cyclic_annihilates_commutator` reads as an impossibility
result. With it, the two together say the remainder needs a pairing rather than
a functional — which is the actual content. -/
theorem trace_pairing_sees_a_commutator :
    letI d : Matrix (Fin 2) (Fin 2) ℚ := !![1, 0; 0, -1]
    Matrix.trace d = 0 ∧ Matrix.trace (d * d) = 2 := by
  constructor
  · simp [Matrix.trace_fin_two]
  · simp [Matrix.trace_fin_two]
    norm_num

open Matrix in
/-- `diag(1,-1)` really is a commutator, so the guard above is about the
commutator subspace and not merely about some traceless matrix. -/
theorem diag_one_neg_one_is_commutator :
    letI e : Matrix (Fin 2) (Fin 2) ℚ := !![0, 1; 0, 0]
    letI f : Matrix (Fin 2) (Fin 2) ℚ := !![0, 0; 1, 0]
    e * f - f * e = !![1, 0; 0, -1] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp

/-! ## 3. Why the representative is derived, not chosen -/

/-- **Uniqueness of a Riesz representative.**

If the pairing `B` is nondegenerate in the second slot, two elements that pair
identically against everything are equal.

This is the epistemically load-bearing statement. The probe solves a linear
system for a representing element `y₀` and finds it; on its own that is a
*computation*, and a computation that produced one answer among many would be a
fitted choice. Nondegeneracy is what upgrades it: there is at most one such
element, so `y₀` is determined by `net` and the pairing together, with nothing
left to select. -/
theorem eq_of_pairing_eq_of_nondegenerate {M : Type*} [AddCommGroup M]
    [Module R M] (B : M → M → R)
    (hadd : ∀ x u v, B x (u - v) = B x u - B x v)
    (hnd : ∀ y : M, (∀ x, B x y = 0) → y = 0)
    (y₁ y₂ : M) (h : ∀ x, B x y₁ = B x y₂) :
    y₁ = y₂ := by
  have hz : y₁ - y₂ = 0 := hnd _ fun x => by rw [hadd x y₁ y₂, h x, sub_self]
  exact sub_eq_zero.mp hz

end QOU.QBeta
