import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.LinearAlgebra.Span.Defs

/-!
# Degree growth of the Gröbner–Shirshov normal-form walk

This file formalises the structural claims behind
`computations/probes/symbolic_nf_q_degree_magic_probe.py`, which walks the
atom braid word carrying each normal-form coefficient as an exact Laurent
polynomial in `q` rather than as a floating-point number at `q₀`.

## What is and is not proved here

The probe makes claims of two different kinds and only one kind is a theorem.

**Formalised here** — the algebraic facts that justify the representation:

* `hQ_mul_T` — multiplying a monomial by `h = q - q⁻¹` is a *shift and
  subtract*, `h · qᵉ = qᵉ⁺¹ - qᵉ⁻¹`. This is the load-bearing claim: it is
  why no general polynomial multiplication occurs anywhere in the walk.
* `hQ_mul_mem` — multiplying by `h` widens the exponent range by exactly one
  on each side, and no more.
* `step_mem` — one normal-form step, whose multipliers are `1` and `h` scaled
  by ring elements, widens the range by at most one on each side.
* `walk_mem_spanRange` — after `n` such steps from the identity the state
  lies in `[-n, n]`. **The degree span grows linearly in the number of
  crossings**, at most `2` per crossing, which is the formal content of "the
  state does not grow with the nucleon number; only the polynomial degree
  does".

**NOT formalised, because they are not theorems.** That the atom path's
multipliers are exactly `1`, `0`, `-h`, `-h/2` is a fact about a particular
Python function, not about mathematics; it enters here as the *hypothesis*
`hstep` of `walk_mem_spanRange`, which is the honest encoding — the theorem
says what follows *if* a walk has that shape, and a walk using a general
polynomial multiplier falsifies it. Likewise the measured degrees (proton
`10, 11, 9, 8, 10, 5`; neutron `9, 10, 2, 5, 7, 8`) and the timings are
witness data, not propositions.

## Base ring

Everything is stated over a generic `CommRing R` (§7c): the walk is pure
`ℚ[q^{±1}]` algebra with no archimedean content, and the rational multiplier
`-1/2` appears only as *some* ring element `d`, so no division is needed in
any statement.
-/

namespace QOU.BraidKnot.LaurentWalk

open LaurentPolynomial

variable {R : Type*} [CommRing R]

/-- The Hecke quantum integer `h = q - q⁻¹`, as a Laurent polynomial. -/
noncomputable def hQ : R[T;T⁻¹] := T 1 - T (-1)

/-- **Multiplying a monomial by `h` is a shift-and-subtract.**

`h · qᵉ = qᵉ⁺¹ - qᵉ⁻¹`: the exponent moves by `±1` and nothing else happens.
This is why the normal-form walk needs no general polynomial multiplication —
every step is a shift plus a scalar, so the cost is linear in the number of
monomials rather than quadratic. -/
theorem hQ_mul_T (e : ℤ) : (hQ : R[T;T⁻¹]) * T e = T (e + 1) - T (e - 1) := by
  have h₁ : (T 1 : R[T;T⁻¹]) * T e = T (e + 1) := by
    rw [← T_add]; congr 1; ring
  have h₂ : (T (-1) : R[T;T⁻¹]) * T e = T (e - 1) := by
    rw [← T_add]; congr 1; ring
  rw [hQ, sub_mul, h₁, h₂]

/-- The `R`-submodule spanned by the monomials `qᵉ` with `a ≤ e ≤ b`. -/
noncomputable def spanRange (a b : ℤ) : Submodule R R[T;T⁻¹] :=
  Submodule.span R {p : R[T;T⁻¹] | ∃ e : ℤ, a ≤ e ∧ e ≤ b ∧ p = T e}

theorem T_mem_spanRange {a b e : ℤ} (h₁ : a ≤ e) (h₂ : e ≤ b) :
    (T e : R[T;T⁻¹]) ∈ spanRange (R := R) a b :=
  Submodule.subset_span ⟨e, h₁, h₂, rfl⟩

/-- A wider window contains a narrower one. -/
theorem spanRange_mono {a a' b b' : ℤ} (ha : a' ≤ a) (hb : b ≤ b') :
    spanRange (R := R) a b ≤ spanRange (R := R) a' b' := by
  refine Submodule.span_le.mpr ?_
  rintro p ⟨e, he₁, he₂, rfl⟩
  exact T_mem_spanRange (le_trans ha he₁) (le_trans he₂ hb)

/-- **Multiplying by `h` widens the exponent window by exactly one on each
side.** Together with `hQ_mul_T` this is the whole degree-growth story. -/
theorem hQ_mul_mem {a b : ℤ} {p : R[T;T⁻¹]} (hp : p ∈ spanRange (R := R) a b) :
    hQ * p ∈ spanRange (R := R) (a - 1) (b + 1) := by
  induction hp using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨e, he₁, he₂, rfl⟩ := hx
      rw [hQ_mul_T]
      exact Submodule.sub_mem _
        (T_mem_spanRange (by omega) (by omega))
        (T_mem_spanRange (by omega) (by omega))
  | zero => simp
  | add x y _ _ hx hy => rw [mul_add]; exact Submodule.add_mem _ hx hy
  | smul r x _ hx =>
      rw [mul_smul_comm]; exact Submodule.smul_mem _ r hx

/-- Scaling by a coefficient keeps the window. -/
theorem C_mul_mem {a b : ℤ} {p : R[T;T⁻¹]} (c : R)
    (hp : p ∈ spanRange (R := R) a b) :
    C c * p ∈ spanRange (R := R) a b := by
  have : C c * p = c • p := by
    rw [smul_eq_C_mul]
  rw [this]
  exact Submodule.smul_mem _ c hp

/-- **One normal-form step widens the window by at most one on each side.**

The step is `new = c · old + d · (h · old)`: the two multiplier shapes the
atom path actually uses (`1` and `h`, each scaled by a ring element — `0`,
`-1` and `-1/2` in the walk itself). No general polynomial multiplication
appears, and that is what bounds the growth. -/
theorem step_mem {a b : ℤ} {old new : R[T;T⁻¹]} (c d : R)
    (hold : old ∈ spanRange (R := R) a b)
    (hnew : new = C c * old + C d * (hQ * old)) :
    new ∈ spanRange (R := R) (a - 1) (b + 1) := by
  subst hnew
  refine Submodule.add_mem _ ?_ ?_
  · exact spanRange_mono (by omega) (by omega) (C_mul_mem c hold)
  · exact C_mul_mem d (hQ_mul_mem hold)

/-- **The walk's degree span grows linearly in the number of steps.**

After `n` steps from the identity `q⁰`, every exponent lies in `[-n, n]`.
So a walk of `n` crossings carries at most `2n + 1` distinct monomials per
coefficient: the *state* does not grow with the nucleon number, only the
polynomial degree does, and only linearly in the crossing count.

The hypothesis `hstep` is where the atom path's restricted multipliers enter.
A walk that multiplied by a general polynomial would not satisfy it, and the
conclusion would genuinely fail — the bound is not an artifact of the
statement. -/
theorem walk_mem_spanRange (f : ℕ → R[T;T⁻¹]) (h0 : f 0 = T 0)
    (hstep : ∀ k, ∃ c d : R, f (k + 1) = C c * f k + C d * (hQ * f k)) :
    ∀ n : ℕ, f n ∈ spanRange (R := R) (-(n : ℤ)) (n : ℤ) := by
  intro n
  induction n with
  | zero =>
      rw [h0]
      exact T_mem_spanRange (by norm_num) (by norm_num)
  | succ k ih =>
      obtain ⟨c, d, hk⟩ := hstep k
      have := step_mem (a := -(k : ℤ)) (b := (k : ℤ)) c d ih hk
      refine spanRange_mono ?_ ?_ this <;> push_cast <;> omega

/-- **The hypothesis of `walk_mem_spanRange` is satisfiable.**

The pure-`h` walk `f k = h^k` has exactly the required shape (`c = 0`,
`d = 1`), so the degree bound is not vacuously true for want of any walk
meeting its premise. Recorded because a bound whose hypothesis nothing
satisfies would prove nothing about the probe. -/
theorem exists_walk :
    ∃ f : ℕ → R[T;T⁻¹], f 0 = T 0 ∧
      (∀ k, ∃ c d : R, f (k + 1) = C c * f k + C d * (hQ * f k)) := by
  refine ⟨fun k => hQ ^ k, by simp, fun k => ⟨0, 1, ?_⟩⟩
  simp [pow_succ, mul_comm]

/-- The identity element sits at the origin of the grading: a walk of zero
steps has zero degree span. Recorded separately because it is the base case
the linear bound is anchored on. -/
theorem one_mem_spanRange_zero :
    (1 : R[T;T⁻¹]) ∈ spanRange (R := R) 0 0 := by
  have : (1 : R[T;T⁻¹]) = T 0 := (T_zero).symm
  rw [this]
  exact T_mem_spanRange le_rfl le_rfl

end QOU.BraidKnot.LaurentWalk
