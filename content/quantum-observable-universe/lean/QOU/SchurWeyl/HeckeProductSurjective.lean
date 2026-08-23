import QOU.SchurWeyl.PiBlockSeparation
import QOU.SchurWeyl.SeminormalInequivalence
import QOU.SchurWeyl.SeminormalRangeTop
import QOU.Mathlib.SchenstedPartitionShape

/-!
# QOU.SchurWeyl.HeckeProductSurjective — the block product map is surjective

SW-7 (`qou-0h5k`), the step that needed an argument rather than an assembly.

`Φ = ⊕_{λ ⊢ n+1} ρ_λ : H_{n+1}(q) → ∏_λ M_{#SYT λ}(ℝ)` is **surjective**.

## Why this is not the classical route

`BraidKnot.SpechtWedderburnGeneral` settles the `q = 1` case by **injectivity + equal finrank**.
That does not transfer.  On the `q`-side the corpus has `HeckeCoset.finrank_le_factorial`
(`dim H ≤ (n+1)!`) but *not* the matching lower bound — that is the open Gröbner–Shirshov item
`qou-auq3` — and injectivity together with `dim source ≤ dim target` proves nothing at all.

Surjectivity is what the `q`-side actually has, from two results that landed separately:

* `seminormalRep_range_eq_top` — **each block is surjective**;
* `youngDiagram_eq_of_contentPowSum_eq` — the central Murphy power sums **separate the shapes**.

## Why no density theorem is needed

Mathlib has no Jacobson density and no bicommutant, and the usual proof wants one.  It is avoidable:
`PiBlockSeparation.eq_top_of_separating_of_blockSurj` gets `A = ⊤` from separation plus per-block
surjectivity by finite Lagrange interpolation and nothing else — block simplicity is never used.
Separation supplies the block idempotents; per-block surjectivity supplies the entries.

Once this lands, the Wedderburn isomorphism follows by counting: surjective, with
`dim H ≤ (n+1)!` and `dim (∏_λ M_{d_λ}) = Σ_λ d_λ² = (n+1)!` (SW-3, now available for every `n`),
forces bijectivity — and yields `dim H_{n+1}(q) = (n+1)!` as a corollary, the Iwahori–Hecke basis
theorem's lower bound, without the Gröbner–Shirshov route.

LaTeX label: `thm:hecke-product-surjective`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

/-- Every partition of `n+1` has a shape with `n+1` cells — the hypothesis `seminormalRep` wants. -/
theorem partitionShape_card_succ {n : ℕ} (lam : Partition (n + 1)) :
    (QOU.Mathlib.partitionShape lam).cells.card = n + 1 :=
  QOU.Mathlib.partitionShape_card lam

/-- **The block product map** `Φ = ⊕_λ ρ_λ`. -/
noncomputable def heckeProduct (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Hecke ℝ q q⁻¹ n →ₐ[ℝ] (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) ℝ) :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq0 hq2 n (partitionShape_card_succ lam))

@[simp] theorem heckeProduct_apply (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (x : Hecke ℝ q q⁻¹ n) (lam : Partition (n + 1)) :
    heckeProduct q hq0 hq2 n x lam
      = seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x := rfl

/-- **The central Murphy power sums land on scalar tuples.**  Block `λ` sees the scalar
`Σ_{c ∈ λ} (q^{2c})^m`, which is what `PiBlockSeparation` consumes as its separating family. -/
theorem heckeProduct_jmPowSum (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) (m : ℕ) :
    heckeProduct q hq0 hq2 n (∑ k ∈ Finset.range (n + 1), (qJM ℝ q q⁻¹ n k) ^ m)
      = piScalarHom (fun lam : Partition (n + 1) =>
          ∑ c ∈ (QOU.Mathlib.partitionShape lam).cells, (q ^ (2 * cellContent c)) ^ m) := by
  funext lam
  rw [heckeProduct_apply, piScalarHom_apply,
    seminormalRep_jmPowSum q hq0 hq2 n (partitionShape_card_succ lam) m,
    Algebra.algebraMap_eq_smul_one]

/-- **The block scalars separate the partitions.**  Contrapositive of
`youngDiagram_eq_of_contentPowSum_eq`, plus injectivity of `partitionShape`. -/
theorem contentPowSum_separates (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (lam lam' : Partition (n + 1)) (hne : lam ≠ lam') :
    ∃ m : ℕ, (∑ c ∈ (QOU.Mathlib.partitionShape lam).cells, (q ^ (2 * cellContent c)) ^ m)
      ≠ ∑ c ∈ (QOU.Mathlib.partitionShape lam').cells, (q ^ (2 * cellContent c)) ^ m := by
  by_contra hcon
  push_neg at hcon
  exact hne (QOU.Mathlib.partitionShape_injective
    (youngDiagram_eq_of_contentPowSum_eq q hq0 hq2 n
      (partitionShape_card_succ lam) (partitionShape_card_succ lam')
      (fun m => (hcon m).symm)))

/-- **`Φ` is surjective.**  Separation gives the block idempotents, `seminormalRep_range_eq_top`
gives the entries, and `eq_top_of_separating_of_blockSurj` puts them together — with no density
theorem anywhere. -/
theorem heckeProduct_range_eq_top (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    (heckeProduct q hq0 hq2 n).range = ⊤ := by
  classical
  refine eq_top_of_separating_of_blockSurj (V := ℕ) _
    (fun lam m => ∑ c ∈ (QOU.Mathlib.partitionShape lam).cells, (q ^ (2 * cellContent c)) ^ m)
    (fun m => ?_) (fun lam lam' hne => contentPowSum_separates q hq0 hq2 n lam lam' hne)
    (fun lam x => ?_)
  · exact ⟨∑ k ∈ Finset.range (n + 1), (qJM ℝ q q⁻¹ n k) ^ m,
      heckeProduct_jmPowSum q hq0 hq2 n m⟩
  · -- per-block surjectivity is `seminormalRep_range_eq_top`
    have hb : x ∈ (seminormalRep q hq0 hq2 n (partitionShape_card_succ lam)).range := by
      rw [seminormalRep_range_eq_top]
      exact Algebra.mem_top
    obtain ⟨h, hh⟩ := hb
    exact ⟨heckeProduct q hq0 hq2 n h, ⟨h, rfl⟩, hh⟩

theorem heckeProduct_surjective (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    Function.Surjective (heckeProduct q hq0 hq2 n) := by
  intro x
  have hx : x ∈ (heckeProduct q hq0 hq2 n).range := by
    rw [heckeProduct_range_eq_top]; exact Algebra.mem_top
  obtain ⟨h, hh⟩ := hx
  exact ⟨h, hh⟩

end QOU.SchurWeyl
