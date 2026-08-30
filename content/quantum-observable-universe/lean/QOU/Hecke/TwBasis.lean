import Mathlib.GroupTheory.Coxeter.Length
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Tactic

/-!
# QOU.Hecke.TwBasis — the `T_w` right-multiplication operators

Toward the `T_w` basis of `H_n(q)` (bean `qou-twwf`), which is what `det(Gram)`
must be stated against and hence what the `WenzlCriterion` /
`SchurElementCriterion` discharge ultimately needs.

## Why this route, and not reduced words

The obvious construction — define `T_w` as the product along a reduced word for
`w` — needs **Matsumoto's theorem** for well-definedness (any two reduced words
differ by braid moves).  Mathlib does **not** have it: `Coxeter/Basic.lean:78`
lists *"State and prove Matsumoto's theorem"* as an explicit TODO.

So this file takes the standard Bourbaki route instead, which avoids Matsumoto
entirely.  Build the free module `W →₀ R` with basis indexed by `W`, define
right multiplication by each `T_{s i}` **directly on that basis** by the length
dichotomy, and verify the Hecke relations for those operators.  A representation
of `H_n(q)` on the free module is what makes the `T_w` linearly independent —
well-definedness is then a consequence rather than a prerequisite.

## What is proved here (sorry-free, any Coxeter system)

* `rsFun` / `Rs i` — right multiplication by `T_{s i}`:
  `T_w ↦ T_{w s_i}` when the length goes up, `↦ (q-1)T_w + q T_{w s_i}` when it
  goes down.  Stated for an arbitrary `cs : CoxeterSystem M W` and `[CommRing R]`.
* `length_flip` — the branch condition genuinely flips when `s i` is applied
  twice, which is what makes the two cases fit together.
* **`Rs_Rs_single`** and **`Rs_sq`** — the Hecke quadratic relation
  `Rs i ∘ Rs i = (q-1)·Rs i + q·id`, on basis vectors and then as an operator
  identity.

## What is NOT proved yet

The **braid relations** for `Rs`, and hence the algebra map
`H_n(q) → End (W →₀ R)` and the independence of the `T_w`.  The braid case needs
more Coxeter combinatorics than the quadratic case, which only needed
`length_mul_simple`.  Nothing here bears on it.

This file is general in `cs`; it becomes a statement about `S_{n+1}` by feeding
it `QOU.Hecke.SymmetricCoxeter.permCoxeterSystem` — the type-`Aₙ` system proved
in this same PR, which is what put `cs.length` within reach of `Equiv.Perm` in
the first place.
-/

open Classical
namespace QOU.Hecke.TwBasis

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)
variable {R : Type*} [CommRing R] (q : R)

/-- The image of the basis vector `T_w` under right multiplication by `T_{s i}`:
    `T_{w s_i}` when the length goes up, `(q-1)T_w + q T_{w s_i}` when it goes down. -/
noncomputable def rsFun (i : B) (w : W) : W →₀ R :=
  if cs.length (w * cs.simple i) = cs.length w + 1 then
    Finsupp.single (w * cs.simple i) 1
  else
    (q - 1) • Finsupp.single w (1 : R) + q • Finsupp.single (w * cs.simple i) (1 : R)

/-- Right multiplication by `T_{s i}` on the free module with basis `W`. -/
noncomputable def Rs (i : B) : (W →₀ R) →ₗ[R] (W →₀ R) :=
  Finsupp.linearCombination R (rsFun cs q i)

@[simp] theorem Rs_single (i : B) (w : W) :
    Rs cs q i (Finsupp.single w (1 : R)) = rsFun cs q i w := by
  simp [Rs]

/-- The two length branches are exclusive and exhaustive, and applying `s i`
    twice returns to `w`. -/
theorem length_flip (i : B) (w : W) :
    (cs.length (w * cs.simple i) = cs.length w + 1) ↔
      ¬ (cs.length (w * cs.simple i * cs.simple i) = cs.length (w * cs.simple i) + 1) := by
  have hinv : w * cs.simple i * cs.simple i = w := by
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  rw [hinv]
  rcases cs.length_mul_simple w i with h | h <;> omega


/-- **The Hecke quadratic relation for the right-multiplication operator.**
    `Rs i ∘ Rs i = (q-1) Rs i + q · id` on every basis vector. -/
theorem Rs_Rs_single (i : B) (w : W) :
    Rs cs q i (Rs cs q i (Finsupp.single w (1 : R)))
      = (q - 1) • Rs cs q i (Finsupp.single w (1 : R)) + q • Finsupp.single w (1 : R) := by
  have hinv : w * cs.simple i * cs.simple i = w := by
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  by_cases h : cs.length (w * cs.simple i) = cs.length w + 1
  · have h1 : Rs cs q i (Finsupp.single w (1 : R))
        = Finsupp.single (w * cs.simple i) (1 : R) := by
      rw [Rs_single]; unfold rsFun; rw [if_pos h]
    have h2 : Rs cs q i (Finsupp.single (w * cs.simple i) (1 : R))
        = (q - 1) • Finsupp.single (w * cs.simple i) (1 : R)
          + q • Finsupp.single w (1 : R) := by
      rw [Rs_single]; unfold rsFun
      rw [if_neg (by rw [hinv]; omega), hinv]
    rw [h1, h2]
  · have h1 : Rs cs q i (Finsupp.single w (1 : R))
        = (q - 1) • Finsupp.single w (1 : R)
          + q • Finsupp.single (w * cs.simple i) (1 : R) := by
      rw [Rs_single]; unfold rsFun; rw [if_neg h]
    have h2 : Rs cs q i (Finsupp.single (w * cs.simple i) (1 : R))
        = Finsupp.single w (1 : R) := by
      rw [Rs_single]; unfold rsFun
      rw [if_pos (by
        rw [hinv]; rcases cs.length_mul_simple w i with hh | hh <;> omega), hinv]
    rw [h1, map_add, map_smul, map_smul, h1, h2]


/-- **The Hecke quadratic relation, as an operator identity.** -/
theorem Rs_sq (i : B) :
    (Rs cs q i) ∘ₗ (Rs cs q i)
      = (q - 1) • Rs cs q i + q • (LinearMap.id : (W →₀ R) →ₗ[R] (W →₀ R)) := by
  apply Finsupp.lhom_ext'
  intro w
  apply LinearMap.ext_ring
  simpa using Rs_Rs_single cs q i w

end QOU.Hecke.TwBasis
