import QOU.Basic


/-!
# QOU.BraidKnot.LocalShadowOrdering — local ≤_q ordering of shadow prices

A ≤_q B iff |y_A(q')| ≤ |y_B(q')| on a neighborhood of q.

LaTeX: `\label{def:local-shadow-ordering}`
-/

namespace QOU.BraidKnot

universe u

/-- **Local shadow-price ordering** `λ₁ ≼_q λ₂` at point `q : R`.

    `LocalShadowOrdering R` records two partitions, their shadow-price
    functions, the point `q`, and the witnessing neighborhood data:
    a predicate `nbhd` cutting out an open set containing `q` on which
    `|y₁| ≤ |y₂|` pointwise.  This is the `.md` definition
    `λ₁ ≼_q λ₂ ⟺ ∃ U ∋ q open, |y_{λ₁}(q')| ≤ |y_{λ₂}(q')| ∀ q' ∈ U`,
    with `nbhd` standing in for the open set `U` (the topological
    openness of `U` is an external hypothesis — for `ℝ` the Euclidean
    topology, for `ℚ_p` the `p`-adic — but the *order content*, the
    pointwise magnitude inequality on `U`, is encoded here).

    §7c: only the ordered-ring structure is used — `|·|` needs a `Neg` and a
    lattice order, nothing here divides — so `[CommRing R]` is the weakest
    typeclass admitting the construction; no field is required. -/
structure LocalShadowOrdering (R : Type u) [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  /-- Partition λ₁ ⊢ k₁. -/
  partition_low  : List ℕ
  /-- Partition λ₂ ⊢ k₂. -/
  partition_high : List ℕ
  /-- Substrate parameter at which the ordering is asserted. -/
  q : R
  /-- Shadow price `y_{λ₁}(·)` of the low partition. -/
  y_low  : R → R
  /-- Shadow price `y_{λ₂}(·)` of the high partition. -/
  y_high : R → R
  /-- A predicate cutting out the neighborhood `U ∋ q` of the `.md`
      definition (membership `nbhd q'` ↔ `q' ∈ U`); `mem_self`
      records `q ∈ U`. -/
  nbhd : R → Prop
  /-- The point `q` lies in its own neighborhood. -/
  mem_self : nbhd q
  /-- **The ordering's content**: the low partition has at-most-equal
      shadow-price magnitude throughout the neighborhood —
      `|y_{λ₁}(q')| ≤ |y_{λ₂}(q')|` for every `q' ∈ U`. -/
  holds_on_neighborhood : ∀ q' : R, nbhd q' → |y_low q'| ≤ |y_high q'|

end QOU.BraidKnot
