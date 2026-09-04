import QOU.Hecke.TwBasis

/-!
# The two `rsFun` branches combine to `q · (T_w + T_{w sᵢ})`

`QOU.BraidKnot.HeckeCellular` describes what the Murphy element `x_λ` needs:

> pairing each `w` with `w sᵢ` — one of the two has length going up, the other
> down, and **the two `rsFun` branches combine to `q·(T_w + T_{w s_i})`**

`rsFun_add_rsFun` is that sentence, for an arbitrary Coxeter system.

## What this is, and is not

The **dichotomy** it rests on is not new: `CoxeterSystem.length_mul_simple` is in
Mathlib, and `TwBasis.length_flip` already packages it.  What is new is the
*consequence* — that summing the two branches over a pair collapses to `q` times
the pair, with the `(q-1)` and the `1` combining exactly.

That is the identity a sum over a Young subgroup is reorganised by, and it holds
over any `CommRing`: nothing here divides by `2`, which the naive
"sum equals its own reindexing" argument would need.
-/

open Classical

namespace QOU.Hecke.ParabolicSum

open QOU.Hecke.TwBasis

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)
variable {R : Type*} [CommRing R] (q : R)

/-- **The pair identity.**  Whichever way the length goes, the two `rsFun`
branches over `{w, w sᵢ}` sum to `q` times that pair.

This is the step that turns `Σ_{w ∈ S} T_w` into an eigenvector: each pair
contributes `q` times itself, so the whole sum is scaled by `q`. -/
theorem rsFun_add_rsFun (i : B) (w : W) :
    rsFun cs q i w + rsFun cs q i (w * cs.simple i)
      = q • (Finsupp.single w (1 : R)
          + Finsupp.single (w * cs.simple i) (1 : R)) := by
  have hinv : w * cs.simple i * cs.simple i = w := by
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  by_cases h : cs.length (w * cs.simple i) = cs.length w + 1
  · -- `w` ascends, so `w sᵢ` descends
    have hdesc : ¬ (cs.length (w * cs.simple i * cs.simple i)
        = cs.length (w * cs.simple i) + 1) := by rw [hinv]; omega
    unfold rsFun
    rw [if_pos h, if_neg hdesc, hinv]
    module
  · -- `w` descends, so `w sᵢ` ascends
    have hasc : cs.length (w * cs.simple i * cs.simple i)
        = cs.length (w * cs.simple i) + 1 := by
      rw [hinv]
      rcases cs.length_mul_simple w i with h1 | h1
      · exact absurd h1 h
      · omega
    unfold rsFun
    rw [if_neg h, if_pos hasc, hinv]
    module

/-- The same, read as: applying `Rs i` to a pair of basis vectors scales it by
`q`.  This is the eigenvector property, one pair at a time. -/
theorem Rs_pair (i : B) (w : W) :
    Rs cs q i (Finsupp.single w (1 : R) + Finsupp.single (w * cs.simple i) (1 : R))
      = q • (Finsupp.single w (1 : R)
          + Finsupp.single (w * cs.simple i) (1 : R)) := by
  rw [map_add, Rs_single, Rs_single]
  exact rsFun_add_rsFun cs q i w

/-- Applied at `w = 1`: the rank-one Murphy element `1 + T_{sᵢ}` is a
`q`-eigenvector.  `HeckeCellular.sigma_mul_parabolicSym` proves this from the
quadratic relation; deriving it here instead is a cross-check that the pair
identity is the right generalisation of it. -/
theorem Rs_one_add_simple (i : B) :
    Rs cs q i (Finsupp.single (1 : W) (1 : R) + Finsupp.single (cs.simple i) (1 : R))
      = q • (Finsupp.single (1 : W) (1 : R) + Finsupp.single (cs.simple i) (1 : R)) := by
  have := Rs_pair cs q i (1 : W)
  simpa using this

end QOU.Hecke.ParabolicSum
