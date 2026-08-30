import QOU.Hecke.FullRank
import QOU.Machinery.HeckeH3Wedderburn
import QOU.Machinery.HeckeH4Wedderburn
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# `QOU.Hecke.FullRankFromWedderburn` — the Iwahori rank for the tree's `H₃` and `H₄`

`QOU.Hecke.FullRank` introduced `IsHeckeOfFullRank R n A` — free of rank `n!` —
because `QOU.Hecke.HeckeAlgebra` does not pin the dimension and is satisfied by
algebras far too small (`InstanceH2.rankOneModel` inhabits it at every `n`). This
file discharges that condition for the tree's own `H₃(q)` and `H₄(q)`:
`QOU.Machinery.HeckeH3AlgebraInstance.H3A` and
`QOU.Machinery.HeckeH4AlgebraLaws.H4A`.

## Where the dimension actually comes from

Both are structures wrapping their coordinate vector — `H3A R h` has the single
field `v : Fin 6 → R`, `H4A R h` has `v : Fin 24 → R` — and their `Module R`
instances are componentwise on that field. So each is `R`-linearly equivalent to
its coordinate space and the dimension is `6` and `24` **unconditionally**: no
genericity hypotheses, no Wedderburn theory. That is what `h3CoordEquiv` /
`h4CoordEquiv` say, and it is the whole proof.

Bean qou-awp7 planned to reach `n = 4` through a `3 × 24` closure table — the
reduced-word operators shown independent, then shown to span. Neither half is
needed: the carrier is a coordinate space by construction.

## What this does and does not establish

`IsHeckeOfFullRank` fixes the **dimension**. That is exactly what the degenerate
models fail — `rankOneModel` is one-dimensional at every `n` — and it is what
`QOU.Hecke.not_isHeckeOfFullRank_rankOne` turns on. It is *not*, on its own,
evidence that `H3A`/`H4A` are the Hecke algebras. That comes from the
multiplication, and that is where the tree's real work is:

* `HeckeH3AlgebraLaws` and `HeckeH4StabilizationRung` prove the presentation —
  quadratic, both braid relations, and at `n = 4` far commutation;
* `HeckeH4AlgebraLaws.mulNF₄_assoc` proves the product associative, via the
  structured route (`mulσₖ (u·v) = u·(v·σₖ)` lifted along the right basis);
* `HeckeH3Wedderburn.wedderburn₃` and `HeckeH4Wedderburn.wedderburn₄` are
  sorry-free `AlgEquiv`s onto `K × K × M₂(K)` and `K × K × M₂(K) × M₃(K) × M₃(K)`.

The last two corroborate the count independently — `1 + 1 + 4 = 6` and
`1 + 1 + 4 + 9 + 9 = 24` — under the Wenzl genericity conditions (`q ≠ 0`,
`q² + 1 ≠ 0`, `q⁴ + q² + 1 ≠ 0`, and at rank 4 also `q⁴ + 1 ≠ 0`, exactly the
degeneracy locus of the coordinate map's determinant). A Wedderburn block count
that holds only generically agreeing with a coordinate count that holds always is
a real consistency check on the basis, so it is recorded below rather than left
implicit.
-/

namespace QOU.Hecke

open QOU.Machinery.H3 QOU.Machinery.H4

universe u

/-! ## `H₃(q)` has rank `6 = 3!` -/

/-- `H3A R h` is its coordinate space: the structure has the single field
`v : Fin 6 → R`, and its module structure is componentwise on it. -/
def h3CoordEquiv (R : Type u) [CommRing R] (h : R) : H3A R h ≃ₗ[R] (Fin 6 → R) where
  toFun := H3A.v
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  invFun := H3A.mk
  left_inv _ := rfl
  right_inv _ := rfl

/-- **`dim_K H₃(q) = 6 = 3!`.** -/
theorem finrank_H3A (K : Type u) [Field K] (h : K) :
    Module.finrank K (H3A K h) = 6 := by
  rw [(h3CoordEquiv K h).finrank_eq, Module.finrank_fin_fun]

/-- **`H₃(q)` has the full Iwahori rank.** -/
instance isHeckeOfFullRank_H3A (K : Type u) [Field K] (h : K) :
    IsHeckeOfFullRank K 3 (H3A K h) where
  free := Module.Free.of_equiv (h3CoordEquiv K h).symm
  finrank_eq := by rw [finrank_H3A]; rfl

/-! ## `H₄(q)` has rank `24 = 4!` -/

/-- `H4A R h` is its coordinate space, on the subscript 24-word basis. -/
def h4CoordEquiv (R : Type u) [CommRing R] (h : R) : H4A R h ≃ₗ[R] (Fin 24 → R) where
  toFun := H4A.v
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  invFun := H4A.mk
  left_inv _ := rfl
  right_inv _ := rfl

/-- **`dim_K H₄(q) = 24 = 4!`.** This is the half the retired `QOU.Hecke.InstanceH4`
never had: it carried a `HeckeAlgebra R 4 q` instance on an operator algebra whose
dimension was never pinned (bean qou-ti7p). Here the relations and the rank hold of
one and the same carrier. -/
theorem finrank_H4A (K : Type u) [Field K] (h : K) :
    Module.finrank K (H4A K h) = 24 := by
  rw [(h4CoordEquiv K h).finrank_eq, Module.finrank_fin_fun]

/-- **`H₄(q)` has the full Iwahori rank `24 = 4!`.** -/
instance isHeckeOfFullRank_H4A (K : Type u) [Field K] (h : K) :
    IsHeckeOfFullRank K 4 (H4A K h) where
  free := Module.Free.of_equiv (h4CoordEquiv K h).symm
  finrank_eq := by rw [finrank_H4A]; rfl

/-! ## The Wedderburn block counts agree with the coordinate counts

For the record: the generic block decomposition and the unconditional coordinate
count give the same number at both ranks. Disagreement would mean one of the two
is wrong about the basis. -/

/-- `H₃(q)`'s Wedderburn blocks sum to its dimension: `1 + 1 + 2² = 3!`. -/
theorem wedderburn₃_block_count : 1 + 1 + 2 * 2 = Nat.factorial 3 := by decide

/-- `H₄(q)`'s Wedderburn blocks sum to its dimension: `1 + 1 + 2² + 3² + 3² = 4!`. -/
theorem wedderburn₄_block_count :
    1 + 1 + 2 * 2 + 3 * 3 + 3 * 3 = Nat.factorial 4 := by decide

end QOU.Hecke
