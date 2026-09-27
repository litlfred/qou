import QOU.Machinery.MarkovTraceH4

/-!
# `QOU.Machinery.H4AsciiPresentation` — the Hecke presentation on the ASCII basis

The tree carries two 24-word normal-form bases for `H₄(q)`. The **subscript**
basis (`HeckeH4StabilizationRung`) has the full presentation proved on it:
`mulσ₀_hecke`, `mulσ₁_hecke`, `mulσ₂_hecke`, `braid_σ₀σ₁`, `braid_σ₁σ₂`,
`far_commute_σ₀σ₂`. The **ASCII** basis (`MarkovTraceH4`, the one carrying
`trM` and the sorry-free `trM_cyclic`) is a *different table*, so none of those
transfer for free; until `H4BasisBridge` closes `phi_mulNF` they have to be
checked on each side separately.

This file is that check, on the ASCII generator actions `mulσ0/1/2`:

| lemma | depth | relation | subscript counterpart |
|---|---|---|---|
| `mulσ_sq0/1/2` | 2 | `σₖ² = 1 + h·σₖ` | `HeckeH4StabilizationRung.mulσₖ_hecke` |
| `mulσ_farcomm02` | 2 | `σ₀σ₂ = σ₂σ₀` | `…far_commute_σ₀σ₂` |
| `mulσ_braid01/12` | 3 | `σᵢσⱼσᵢ = σⱼσᵢσⱼ` | `…braid_σ₀σ₁`, `…braid_σ₁σ₂` |

All six by `fin_cases` + `simp` + `ring`, on a free vector at depth ≤ 3 — about
thirteen seconds for the lot. Base ring is generic `[CommRing R]`: none of them
uses inversion, so none needs a field.

`n = 4` is where **far-commutativity** first has content at all: `Generator n`
carries `idx : Fin (n - 1)`, and `Generator.farCommuting` needs two indices
differing by `≥ 2`, so it is unsatisfiable until `n - 1 ≥ 3`.

## Provenance

These were proved in `QOU/Hecke/InstanceH4.lean`, which wrapped them as the
relation fields of a `HeckeAlgebra R 4 q` instance on `Algebra.adjoin R {L0,L1,L2}
⊆ Module.End R (Fin 24 → R)` — the right regular representation, so that
associativity was function composition. That carrier has been retired
(bean qou-ti7p): `QOU.Hecke.InstanceOnH4A.instHeckeAlgebraH4A` now puts the class
on `H4A`, the tree's actual `H₄` ring, where `IsHeckeOfFullRank K 4` holds of the
*same* carrier (`FullRankFromWedderburn.isHeckeOfFullRank_H4A`) — which the
operator algebra never delivered. The relations themselves were not duplicated
anywhere, because they are on the ASCII table; they are what survives, and they
live here.

`mulσ_farcomm02` was also proved a second time in `H4BasisBridge`, which needs it
to normalise the six words where the two bases differ. That copy is gone; the
bridge imports this module.
-/

namespace QOU.Machinery.H4

universe u

variable {R : Type u} [CommRing R] (h : R)

/-! ## The quadratic relation -/

theorem mulσ_sq0 (v : Fin 24 → R) : mulσ0 h (mulσ0 h v) = v + h • mulσ0 h v := by
  funext i; fin_cases i <;> simp [mulσ0]

theorem mulσ_sq1 (v : Fin 24 → R) : mulσ1 h (mulσ1 h v) = v + h • mulσ1 h v := by
  funext i; fin_cases i <;> simp [mulσ1]

theorem mulσ_sq2 (v : Fin 24 → R) : mulσ2 h (mulσ2 h v) = v + h • mulσ2 h v := by
  funext i; fin_cases i <;> simp [mulσ2]

/-! ## Far-commutativity

`σ₀σ₂ = σ₂σ₀`. Indices `0` and `2` differ by `2`, which is why this relation
exists at `n = 4` and at no smaller `n`. -/

theorem mulσ_farcomm02 (v : Fin 24 → R) :
    mulσ0 h (mulσ2 h v) = mulσ2 h (mulσ0 h v) := by
  funext i; fin_cases i <;> simp [mulσ0, mulσ2] <;> ring

/-! ## The braid relations -/

theorem mulσ_braid01 (v : Fin 24 → R) :
    mulσ0 h (mulσ1 h (mulσ0 h v)) = mulσ1 h (mulσ0 h (mulσ1 h v)) := by
  funext i; fin_cases i <;> simp [mulσ0, mulσ1] <;> ring

theorem mulσ_braid12 (v : Fin 24 → R) :
    mulσ1 h (mulσ2 h (mulσ1 h v)) = mulσ2 h (mulσ1 h (mulσ2 h v)) := by
  funext i; fin_cases i <;> simp [mulσ1, mulσ2] <;> ring

/-! ## The actions do not commute

Enough to exclude every commutative model of the presentation — including
`QOU.Hecke.InstanceH2.rankOneModel`, which inhabits `HeckeAlgebra ℚ n 1 ℚ` at
every `n` — before any rank computation. -/

/-- The identity basis vector of the ASCII normal-form module, written as a
`Matrix.vecCons` literal so that `mulσ` indexing reduces by the standard
`cons_val` simp set. -/
def e0 (R : Type u) [CommRing R] : Fin 24 → R :=
  ![1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

/-- `σ₀σ₁` sends the identity basis vector to basis position 8. -/
theorem mulσ01_e0_apply_eight : mulσ0 h (mulσ1 h (e0 R)) 8 = 1 := by
  simp [mulσ0, mulσ1, e0]

/-- `σ₁σ₀` sends it to position 7 instead, so position 8 is zero. -/
theorem mulσ10_e0_apply_eight : mulσ1 h (mulσ0 h (e0 R)) 8 = 0 := by
  simp [mulσ0, mulσ1, e0]

theorem mulσ0_mulσ1_ne [Nontrivial R] :
    mulσ0 h (mulσ1 h (e0 R)) ≠ mulσ1 h (mulσ0 h (e0 R)) := by
  intro hcon
  have h8 := congrFun hcon 8
  rw [mulσ01_e0_apply_eight, mulσ10_e0_apply_eight] at h8
  exact one_ne_zero h8

/-! ## The right basis action

`mulNF` is a 24-term sum `∑ⱼ vⱼ · (u · bⱼ)`, with the composites written out
inline. Packaging them as a function of the index — exactly what
`HeckeH4AlgebraLaws.wordAction` does for the subscript basis — turns that
inline sum into a `Finset.sum`, which is the only form in which the 24 terms can
be *reindexed* rather than expanded. `H4BasisBridge` needs precisely that: the
two bases differ by the permutation `piIdx`, so the products correspond by
reindexing the sum, not by unfolding it (three `simp`-based unfolding attempts
failed, one producing 70 terms where 24 were expected).

`wordActionA` is transcribed from `mulNF`'s own term list and cross-checked
against it, and against the 24 `H4BasisBridge.phi_word_*` statements — all 24
agree — so it cannot silently drift from the table it describes. -/

/-- The right action of the `j`-th ASCII NF basis word, `u ↦ u · b_j` — the same
24 composites `mulNF` sums over, packaged as a function of the index.
Counterpart of `HeckeH4AlgebraLaws.wordAction`, on the other table. -/
def wordActionA (h : R) : Fin 24 → (Fin 24 → R) → (Fin 24 → R) := ![
  fun u => u,
  fun u => mulσ2 h u,
  fun u => mulσ1 h u,
  fun u => mulσ0 h u,
  fun u => mulσ2 h (mulσ1 h u),
  fun u => mulσ1 h (mulσ2 h u),
  fun u => mulσ0 h (mulσ2 h u),
  fun u => mulσ1 h (mulσ0 h u),
  fun u => mulσ0 h (mulσ1 h u),
  fun u => mulσ1 h (mulσ2 h (mulσ1 h u)),
  fun u => mulσ2 h (mulσ1 h (mulσ0 h u)),
  fun u => mulσ1 h (mulσ0 h (mulσ2 h u)),
  fun u => mulσ0 h (mulσ2 h (mulσ1 h u)),
  fun u => mulσ0 h (mulσ1 h (mulσ0 h u)),
  fun u => mulσ0 h (mulσ1 h (mulσ2 h u)),
  fun u => mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h u))),
  fun u => mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h u))),
  fun u => mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h u))),
  fun u => mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h u))),
  fun u => mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h u))),
  fun u => mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h u)))),
  fun u => mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h u)))),
  fun u => mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h u)))),
  fun u => mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h u)))))]

theorem mulNF_zero_right (h : R) (u : Fin 24 → R) :
    mulNF h u (0 : Fin 24 → R) = 0 := by
  funext i; simp [mulNF]

/-- `mulNF u ·` commutes with finite sums in the right argument. -/
theorem mulNF_sum_right (h : R) (u : Fin 24 → R) (s : Finset (Fin 24))
    (f : Fin 24 → (Fin 24 → R)) :
    mulNF h u (∑ j ∈ s, f j) = ∑ j ∈ s, mulNF h u (f j) := by
  induction s using Finset.induction with
  | empty => exact mulNF_zero_right h u
  | @insert a s h1 ih =>
    rw [Finset.sum_insert h1, Finset.sum_insert h1, mulNF_add_right, ih]

/-- Basis decomposition `u = ∑ᵢ uᵢ • e i` on the ASCII basis. -/
theorem basis_decompA (u : Fin 24 → R) : u = ∑ i, u i • (e (R := R) i) := by
  funext j
  rw [Finset.sum_apply]
  simp [e, Pi.single_apply, smul_eq_mul, Finset.sum_ite_eq]

/-- **Right basis action**: `u · b_j = wordActionA j u`; the coefficient vector
`e j` selects exactly the `j`-th composite. -/
theorem mulNF_e_right (h : R) (u : Fin 24 → R) (j : Fin 24) :
    mulNF h u (e j) = wordActionA h j u := by
  fin_cases j <;> (funext i; simp [mulNF, e, wordActionA])

/-- Expansion of the ASCII NF product along the right basis:
`u · v = ∑_j v_j • (u · b_j)`. This is the form the basis bridge reindexes. -/
theorem mulNF_expand_right (h : R) (u v : Fin 24 → R) :
    mulNF h u v = ∑ j, v j • wordActionA h j u := by
  conv_lhs => rw [basis_decompA v]
  rw [mulNF_sum_right]
  exact Finset.sum_congr rfl fun j _ => by
    rw [mulNF_smul_right, mulNF_e_right]

end QOU.Machinery.H4
