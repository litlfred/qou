/-
The join: a degree shift IS multiplication by `X`, and an interface with a
scalar IS multiplication by `X + C d`.

## What this closes

`QOU.Knot.JetGradePromotion` proves that a generator meeting no existing
inversion raises every filtration grade by exactly one with coefficients
intact. `QOU.Knot.InterfaceKernel` proves the single-generator power identity.
Both are `∀`-quantified and sorry-free.

What was verified only computationally, at finite `A` and `k`, was the STEP
BETWEEN them: that a grade shift becomes multiplication by `x` in the grade
generating function, and hence that composing interfaces multiplies. This file
proves that step, for arbitrary index sets, coefficients and degrees.

## The modelling choice, stated because it is where the honesty lives

Promotion is modelled as *the same coefficient function with a shifted degree
function* -- `deg` versus `fun i => deg i + 1` -- rather than as a bijection on
indices. That is exactly what the promotion theorem delivers ("every grade up
by one, coefficients intact") and it avoids bijection bookkeeping that would
add nothing.

What this does NOT do: it does not prove that Hecke multiplication *produces*
such a shift. That is `JetGradePromotion`'s job at the permutation level, and
connecting the two needs the Hecke algebra itself in Lean -- the `qou-e6db`
project, which is Mathlib-contribution scale and is not attempted here. So the
chain is: promotion (proved) → shift ⇒ ×X (proved here) → product over bonds
(proved here), with the arrow from "Hecke multiply" to "shift" carried by
`JetGradePromotion` at the level of permutations and lengths rather than at the
level of algebra elements.
-/
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.BigOperators.Finprod
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Pi
import Mathlib.Tactic.Ring

namespace QOU.Knot.GradedGeneratingFunction

open Polynomial

variable {ι R : Type*} [CommSemiring R]

/-- The grade generating function `∑_{i ∈ s} c i · X^(deg i)`.

Over `ℤ[q,q⁻¹]` with `deg` the Coxeter length and `c` the normal-form
coefficients, this is the `G_E(x)` the arc measures. -/
noncomputable def gf (s : Finset ι) (c : ι → R) (deg : ι → ℕ) : R[X] :=
  ∑ i ∈ s, C (c i) * X ^ (deg i)

@[simp] theorem gf_empty (c : ι → R) (deg : ι → ℕ) : gf (∅ : Finset ι) c deg = 0 := by
  simp [gf]

/-- **Congruence in the degree**: only degrees at indices actually present in
`s` can matter. Used to replace a per-block degree sum by the length of the
assembled word, which agree only on the product index set. -/
theorem gf_congr (s : Finset ι) (c : ι → R) {deg deg' : ι → ℕ}
    (h : ∀ i ∈ s, deg i = deg' i) : gf s c deg = gf s c deg' :=
  Finset.sum_congr rfl fun i hi => by rw [h i hi]

/-- **Multiplicativity over a dependent product index set.**

When the index set is `∏ᵢ S i`, the coefficient multiplicative across factors
and the degree additive, the generating function is the product of the factors'
generating functions.

This is the form the block factorisation needs: nucleon blocks are *not*
identical to one another -- block `i` is supported on strands `[bᵢ, bᵢ₊₁)` --
so the family `S i` must be allowed to vary with `i`. The constant-family case
is `QOU.Knot.BodyOrderExpansion.gf_pow`. -/
theorem gf_pi {κ : Type*} [Fintype κ] [DecidableEq κ] {α : κ → Type*}
    [∀ i, DecidableEq (α i)] (S : ∀ i, Finset (α i)) (c : ∀ i, α i → R)
    (deg : ∀ i, α i → ℕ) :
    gf (Fintype.piFinset S) (fun f => ∏ i, c i (f i)) (fun f => ∑ i, deg i (f i))
      = ∏ i, gf (S i) (c i) (deg i) := by
  simp only [gf]
  rw [Finset.prod_univ_sum]
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [Finset.prod_mul_distrib, ← map_prod, Finset.prod_pow_eq_pow_sum]

/-- **A degree shift is multiplication by `X`.**

This is the promotion theorem's image in the generating function: raising every
degree by one, with coefficients untouched, multiplies `G` by `X`. -/
theorem gf_shift (s : Finset ι) (c : ι → R) (deg : ι → ℕ) :
    gf s c (fun i => deg i + 1) = X * gf s c deg := by
  simp only [gf, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  ring

/-- **The canonical interface is multiplication by `X + C d`.**

The interface `σ_g + d·I` acts as (promotion) + (`d` times the original), and
the generating function turns that into `(X + C d) · G`. With `d = 0` it
degenerates to `gf_shift`, which is the bare-word bridge. -/
theorem gf_interface (s : Finset ι) (c : ι → R) (deg : ι → ℕ) (d : R) :
    gf s c (fun i => deg i + 1) + C d * gf s c deg = (X + C d) * gf s c deg := by
  rw [gf_shift]; ring

/-- Applying a list of interfaces with scalars `ds` multiplies by the product
`∏ (X + C d)`. Induction on the list; this is the composition across `A`. -/
theorem gf_bonds (ds : List R) (P : R[X]) :
    (ds.map (fun d => X + C d)).prod * P
      = ds.foldr (fun d acc => (X + C d) * acc) P := by
  induction ds with
  | nil => simp
  | cons d rest ih =>
      simp only [List.map_cons, List.prod_cons, List.foldr_cons, ← ih]
      ring

/-- With every interface scalar zero the product collapses to `X ^ n` -- the
bare-word composition law `G_A = x^(A-1) · G_1^A` measured in
`body_order_composition_probe`. -/
theorem gf_bonds_zero (n : ℕ) (P : R[X]) :
    ((List.replicate n (0 : R)).map (fun d => X + C d)).prod * P = X ^ n * P := by
  simp [List.map_replicate, List.prod_replicate]

end QOU.Knot.GradedGeneratingFunction
