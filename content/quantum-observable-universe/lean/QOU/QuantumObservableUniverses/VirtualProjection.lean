import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Module.Basic

/-!
# QOU.Virtual — off-shell non-observability of virtual particles

A level-`n` virtual excitation lives in the recursive brane tower and is a
base state `f ∈ A_0` dressed by `n` internal 1-forms `ω_1, …, ω_n ∈ Ω^1`.
The canonical projection `π_0 : A_n → A_0` back to the observable base
level acts through the counit `ε : Ω^1 → K`:

  `π_0(f ⊗ ω_1 ⊗ ⋯ ⊗ ω_n) = f · ε(ω_1) ⋯ ε(ω_n)`

(`virtual-particles-exceptional-divisor`,
`prop:vertex-is-exceptional-divisor`).  A form with no constant part
(`ε(ω) = 0`) is *off-shell*; the physical content is that off-shell
excitations "project no shadow" onto the base level — they are
non-observable — while on-shell excitations survive.

This file proves that dichotomy exactly, as a biconditional (not merely
the one-way "a product with a zero factor is zero"): the projection
vanishes **iff** the base state is zero or some dressing form is off-shell.

Base ring: a generic commutative domain `K` (§7c — algebraic, counit and
scalar action only; no archimedean input).

LaTeX label: `prop:virtual-offshell-projection`
-/

namespace QOU.Virtual

open scoped BigOperators

variable {K : Type*} [CommRing K]
  {A : Type*} [AddCommGroup A] [Module K A]

/-- The base-level projection of a level-`n` excitation: base state `f`
dressed by forms with counits `e i` projects to `(∏ i, e i) • f`. -/
def pi0 {n : ℕ} (e : Fin n → K) (f : A) : A := (∏ i, e i) • f

/-- **Off-shell ⇒ no shadow.**  If some dressing form is off-shell
(`e i = 0`), the excitation projects to zero at the base level — it is
non-observable. -/
theorem pi0_offshell {n : ℕ} {e : Fin n → K} (f : A)
    (h : ∃ i, e i = 0) : pi0 e f = 0 := by
  obtain ⟨i, hi⟩ := h
  have : (∏ j, e j) = 0 := Finset.prod_eq_zero (Finset.mem_univ i) hi
  rw [pi0, this, zero_smul]

/-- **On-shell survives; off-shell vanishes — exactly.**  Over a domain
with no zero smul-divisors, the base-level projection vanishes iff the
base state is zero or some dressing form is off-shell.  Equivalently, the
excitation is observable (`π_0 ≠ 0`) iff `f ≠ 0` and every form has a
nonzero constant part. -/
theorem pi0_eq_zero_iff {n : ℕ} [IsDomain K] [NoZeroSMulDivisors K A]
    (e : Fin n → K) (f : A) :
    pi0 e f = 0 ↔ (∃ i, e i = 0) ∨ f = 0 := by
  rw [pi0, smul_eq_zero, Finset.prod_eq_zero_iff]
  constructor
  · rintro (⟨i, _, hi⟩ | hf)
    · exact Or.inl ⟨i, hi⟩
    · exact Or.inr hf
  · rintro (⟨i, hi⟩ | hf)
    · exact Or.inl ⟨i, Finset.mem_univ i, hi⟩
    · exact Or.inr hf

end QOU.Virtual
