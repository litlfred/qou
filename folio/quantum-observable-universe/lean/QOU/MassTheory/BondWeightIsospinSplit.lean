import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Bond-weight isospin split — the T/³He degeneracy break is exactly `(a/b)²`

Formalization of the structural core of the per-knot `p ≠ n` extensivity LEAD
(PR #3841, bean `qou-r1sr`; witness
`computations/deltalambda/perknot-pn-bond-mayer-grounding.witness.json`).

In the Mayer/Ursell pairwise (`b₂`) cluster level, each nucleon–nucleon bond
`(x,y)` carries the ideal-gas normalization weight `w(x,y) = 1 / (τ x · τ y)`,
where `τ` is the per-knot Markov trace `tr_M` (here `a := τ(proton)`,
`b := τ(neutron)`). The product aggregate over a nucleus' bonds is the product
of its bond weights.

`T = (p,n,n)` has bonds `{pn, pn, nn}`; `³He = (p,p,n)` has bonds
`{pp, pn, pn}`. The two share `A = 3` and the same bond count `3`, and differ in
exactly one bond: `T` carries an `nn` where `³He` carries a `pp` (both carry two
`pn`). Every symmetric / type-blind bond model therefore gives their ratio as
`1`. The inverse-product weight instead gives their ratio **exactly** `(a/b)²`
— a split the type-blind model cannot produce. (The numerical agreement once
quoted here, `(a/b)² ≈ 1.3315` vs 1.3501, −1.38%, used retired convention-C
traces and stale targets. On the canonical traces — borromean word,
convention D, proton pin — `(a/b)² ≈ 1.7544` against the live target 1.3671,
+28.3%; see `perknot-pn-bond-mayer-grounding.witness.json`. The identity
proved below is unaffected.)

This file proves the **exact algebraic identity** behind that reduction. It is a
generic-field statement (§7c: no `ℝ`, no ordering — a pure `GroupWithZero`
identity); the archimedean evaluation `a,b := tr_M(p), tr_M(n)` at the substrate
`q₀` lives in the witness, not here. The lemma does **not** assert the split
*closes* the extensivity gap (a `b₂`/pairwise object, orthogonal to the open
connected-`b₄` magnitude — see the coordination note); it isolates the exact
factor `(a/b)²` supplied by the `p ≠ n` bond resolution.
-/

namespace QOU.MassTheory

open scoped Classical

variable {R : Type*} [Field R]

/-- Inverse-product (Mayer ideal-gas) bond weight `w(x,y) = 1/(x·y)`. -/
def bondWeight (x y : R) : R := (x * y)⁻¹

/-- Product aggregate of the three bond weights of the mass-3 isotope
`T = (p,n,n)`, whose bonds are `{pn, pn, nn}` (here `a := τ p`, `b := τ n`). -/
def tritonAggregate (a b : R) : R :=
  bondWeight a b * bondWeight a b * bondWeight b b

/-- Product aggregate of the three bond weights of `³He = (p,p,n)`, whose bonds
are `{pp, pn, pn}`. -/
def helium3Aggregate (a b : R) : R :=
  bondWeight a a * bondWeight a b * bondWeight a b

/-- **Isospin split identity.** The only bond difference between `T` and `³He`
is a single `pp ↔ nn` swap, so under the inverse-product weight their aggregate
ratio is exactly `(a/b)²` — the degeneracy break a symmetric bond model gives as
`1`. Requires `a, b ≠ 0` (the traces are nonzero at `q₀`). -/
theorem triton_helium3_split (a b : R) (ha : a ≠ 0) (hb : b ≠ 0) :
    tritonAggregate a b / helium3Aggregate a b = (a / b) ^ 2 := by
  unfold tritonAggregate helium3Aggregate bondWeight
  field_simp

/-- The split factor is precisely `bondWeight b b / bondWeight a a` — i.e. the
`nn`-for-`pp` swap, the two shared `pn` bonds cancelling. -/
theorem split_is_nn_over_pp_swap (a b : R) (ha : a ≠ 0) (hb : b ≠ 0) :
    tritonAggregate a b / helium3Aggregate a b
      = bondWeight b b / bondWeight a a := by
  unfold tritonAggregate helium3Aggregate bondWeight
  field_simp

end QOU.MassTheory
