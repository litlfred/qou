/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.FormalGroups.PBWFilteredData
import QOU.FormalGroups.PBWMultiIndex
import QOU.FormalGroups.SplayBialgebra
import QOU.FormalGroups.PBWAssembly

/-!
# Thm. 3.7 of arXiv:math/0602138: `U = T / J` is the distribution algebra of a formal group

Setting: finitely many one-dimensional commutative formal groups `Hᵢ`, given by their
distribution algebras `Aᵢ = Dist(Hᵢ)`. Each `Aᵢ` is a commutative bialgebra with a divided-power
basis `bᵢ(n)`, `n ∈ ℕ`, `bᵢ(0) = 1`, `Δ bᵢ(n) = ∑_{p+q=n} bᵢ(p) ⊗ bᵢ(q)` (here indexed by
`Option ℕ+`, `none ↦ 0`). Let `π` be a Poisson structure on the splay `T = ∐ Aᵢ` that is

* internally symmetric (`SplayPoisson`),
* strongly filtered (`hπwt`, `hπ`, as in `PBWFilteredData.lean`),
* strongly multiplicative for the splay coproduct (`hΔ`, Def. 1.11),

and whose image the splay counit kills (`hε`). Then `formalGroup_of_splay` gives a formal
group law `G` in `|I|` variables whose formal-group-law convolution is the product of `U`,
in the PBW basis `δ^J = ∏_{i increasing} bᵢ(Jᵢ)`.

Assembly: the PBW basis (`splay_integrationBasis`) is re-indexed from normal words to
multi-indices (`wordEquiv`), `U` gets the descended bialgebra (`quotBialgebra`), and the
Cartier reconstruction (`formalGroupLaw_of_pbw`) produces `G`.

No `sorry`, no axiom beyond Lean's three.
-/

set_option linter.unusedSectionVars false

namespace QOU.FormalGroups.PBW

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond UGB.GrobnerShirshov.BlockSplay
  LinearAlgebra TensorProduct

noncomputable section

/-- `0 ↦ none`, `n ↦ some n`: the divided-power index as an `Option ℕ+`. -/
def optOf (n : ℕ) : Option ℕ+ := if h : n = 0 then none else some ⟨n, Nat.pos_of_ne_zero h⟩

theorem optOf_zero : optOf 0 = none := rfl

theorem optOf_pnat (n : ℕ+) : optOf n = some n := by
  simp [optOf, n.ne_zero]; rfl

variable {R : Type*} [CommRing R] {I : Type*} [DecidableEq I]
  {A : I → Type*} [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
  {L : I → Type*} [∀ i, DecidableEq (L i)]

theorem qT_ofW (b : ∀ i, Module.Basis (Option (L i)) R (A i)) (w : List (Σ i, L i)) :
    qT b (ofW w) = (w.map (letter b)).prod := by
  induction w with
  | nil => simp [ofW, qT]
  | cons g w ih =>
    rw [show g :: w = [g] ++ w from rfl, ofW_append, map_mul, qT_ofW_single, ih]
    rfl

end

noncomputable section Assembly

variable {R : Type*} [CommRing R] {I : Type*} [DecidableEq I] [LinearOrder I] [Fintype I]
  [Nonempty I]
  {A : I → Type*} [∀ i, CommRing (A i)] [∀ i, Bialgebra R (A i)]
  (b : ∀ i, Module.Basis (Option ℕ+) R (A i))
  (wtL : ∀ _ : I, ℕ+ → ℕ)
  {β : Type*} [LinearOrder β] [WellFoundedLT β] (rank : (Σ _ : I, ℕ+) → β)
  (rank_inj : Function.Injective rank)
  (π : (Σ _ : I, ℕ+) → (Σ _ : I, ℕ+) → MA (Σ _ : I, ℕ+) R)
  (hshort : ∀ i (x y o : ℕ+), (b i).repr (b i (some x) * b i (some y)) (some o) ≠ 0 →
    wtL i o ≤ wtL i x + wtL i y)
  (hmono : ∀ a c : Σ _ : I, ℕ+, c.1 < a.1 → rank c < rank a)
  (hπwt : ∀ a c : Σ _ : I, ℕ+, c.1 < a.1 → ∀ p ∈ (π a c).support,
    wsum (splayWt wtL) (FreeMonoid.toList p) < splayWt wtL a + splayWt wtL c)
  (hb1 : ∀ i, b i none = 1)
  (hcomul : ∀ i n, Coalgebra.comul (R := R) (b i (optOf n)) =
    ∑ p ∈ Finset.antidiagonal n, b i (optOf p.1) ⊗ₜ[R] b i (optOf p.2))
  [Nontrivial R] (ρ : SplayPoisson R A)
  (hπ : ∀ a c : Σ _ : I, ℕ+, c.1 < a.1 →
    qT b (π a c) = ρ.toPoissonStructure.bracket (letter b a) (letter b c))
  (hΔ : IsStronglyMultiplicative (opMul R _) (splayComul R A).toLinearMap
    ρ.toPoissonStructure.bracket)
  (hε : ∀ f g, splayCounit R A (ρ.toPoissonStructure.bracket f g) = 0)

/-- The divided powers of `U`: `e i n = [ιᵢ bᵢ(n)]`. -/
def divPow (i : I) (n : ℕ) : IntegrationQuotient ρ.toPoissonStructure :=
  integrationMk _ (FreeProduct.ι R A i (b i (optOf n)))

include hb1 in
theorem divPow_zero (i : I) : divPow b ρ i 0 = 1 := by
  rw [divPow, optOf_zero, hb1, map_one, map_one]

include hcomul in
theorem divPow_comul (i : I) (n : ℕ) :
    quotComul ρ.toPoissonStructure hΔ (divPow b ρ i n) =
      ∑ p ∈ Finset.antidiagonal n, divPow b ρ i p.1 ⊗ₜ[R] divPow b ρ i p.2 := by
  rw [divPow, quotComul, descendedComul_mk, splayComul_ι, hcomul, map_sum, map_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  simp [divPow]

/-- The ordered list of all indices. -/
def allIdx : List I := Finset.univ.sort (· ≤ ·)

include hb1 in
theorem orderedMono_eq (J : I →₀ ℕ) :
    integrationMk ρ.toPoissonStructure (qT b (ofW (toWord J))) =
      FormalGroups.orderedMono (divPow b ρ) allIdx J := by
  rw [qT_ofW, map_list_prod, List.map_map, FormalGroups.orderedMono, allIdx,
    ← prod_toWord (divPow b ρ) (divPow_zero b hb1 ρ) J]
  congr 1
  refine List.map_congr_left fun g _ => ?_
  simp only [Function.comp_apply, letter, divPow, optOf_pnat]

include rank_inj hshort hmono hπwt hb1 hcomul hπ in
/-- **Thm. 3.7 of arXiv:math/0602138.** Under the hypotheses of the module docstring, there
is a formal group law `G` in the variables `I` such that, in the PBW basis
`δ^J = ∏_{i increasing} [ιᵢ bᵢ(Jᵢ)]` of `U = T / J`, the coproduct of `U` is the one of
`Dist(G)` (`G.F` is the Cartier series of the basis) and the product of `U` is the
convolution of `G`. In words: `U` is the distribution algebra of the formal group `G`. -/
theorem formalGroup_of_splay [DecidableEq R] :
    ∃ (B : Module.Basis (I →₀ ℕ) R (IntegrationQuotient ρ.toPoissonStructure)),
      (∀ J, B J = FormalGroups.orderedMono (divPow b ρ) allIdx J) ∧
      letI := quotBialgebra ρ.toPoissonStructure hΔ hε
      ∃ G : FormalGroupLaw R I, G.F = cartierF B ∧
        (∀ u v, B.repr (u * v) = conv G (B.repr u) (B.repr v)) ∧ B.repr 1 = one := by
  obtain ⟨B₀, hB₀⟩ := splay_integrationBasis (L := fun _ => ℕ+) b wtL rank rank_inj π hshort
    hmono hπwt hb1 ρ hπ
  let eqv := (Equiv.subtypeEquivRight fun m =>
    BlockData.normalFormMonomial_iff_isChain
      (splayFD b wtL rank rank_inj π hshort hmono hπwt hb1).toBlockData m).trans wordEquiv
  have hB : ∀ J, B₀.reindex eqv J = FormalGroups.orderedMono (divPow b ρ) allIdx J := by
    intro J
    rw [Module.Basis.reindex_apply, hB₀]
    exact orderedMono_eq b hb1 ρ J
  refine ⟨B₀.reindex eqv, hB, ?_⟩
  letI := quotBialgebra ρ.toPoissonStructure hΔ hε
  exact formalGroupLaw_of_pbw (divPow b ρ) (divPow_zero b hb1 ρ)
    (divPow_comul b hcomul ρ hΔ) allIdx (Finset.sort_nodup _ _)
    (fun j => (Finset.mem_sort _).2 (Finset.mem_univ j)) _ hB

end Assembly

end QOU.FormalGroups.PBW
