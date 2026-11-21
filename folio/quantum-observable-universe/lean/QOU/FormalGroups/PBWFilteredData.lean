/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.FormalGroups.PBWIntegration

/-!
# Thm. 3.7 of arXiv:math/0602138 from the paper's hypotheses

`PBWIntegration.lean` proves the PBW basis of `U = T / J` for any filtered block-splay
data `F` compatible with the bases. This file builds that `F` from the paper's input:

* `wordLin`: an element of `Aᵢ` as a combination of words, through the basis `bᵢ`.
* `splayμ`: the block product, the structure constants of `Aᵢ`.
* `splayBD`, `splayFD`: the block-splay data. Blocks are the indices `i`, the order
  is `weightedOrderWF` (weight first, then deg-lex in a rank), and associativity and
  commutativity of the block products come from those of `Aᵢ`.
* `splay_integrationBasis`: the PBW basis of `U`.

The hypotheses are the paper's: the product of two basis elements of `Aᵢ` has no
heavier terms (`hshort`), and the bracket of two letters of different blocks has a
preimage lighter than their product (`hπwt`, `hπ`, the strong filtration).

No `sorry`, no axiom beyond Lean's three.
-/

set_option linter.unusedSectionVars false

namespace QOU.FormalGroups.PBW

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond UGB.GrobnerShirshov.BlockSplay

noncomputable section

variable {R : Type*} [CommRing R] {I : Type*} [DecidableEq I]
  {A : I → Type*} [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
  {L : I → Type*} [∀ i, DecidableEq (L i)]
  (b : ∀ i, Module.Basis (Option (L i)) R (A i))

/-- An element of `Aᵢ` as a combination of words: `bᵢ o ↦ wordOf i o`. -/
def wordLin (i : I) : A i →ₗ[R] MA (Σ i, L i) R := (b i).constr R (wordOf i)

/-- The word list of a basis index. -/
def wordList (i : I) : Option (L i) → List (Σ i, L i)
  | none => []
  | some x => [⟨i, x⟩]

theorem wordOf_eq_ofW (i : I) (o : Option (L i)) : wordOf i o = (ofW (wordList i o) : MA (Σ i, L i) R) := by
  cases o <;> rfl

theorem termSum_eq_lc (F : MA (Σ i, L i) R) (Ψ : List (Σ i, L i) → MA (Σ i, L i) R) :
    termSum F Ψ = Finsupp.linearCombination R (fun p => Ψ (FreeMonoid.toList p)) F := by
  rw [Finsupp.linearCombination_apply]; rfl

/-- `termSum` of an element of `Aᵢ`, computed on the basis. -/
theorem termSum_wordLin (i : I) (z : A i) (Ψ : List (Σ i, L i) → MA (Σ i, L i) R) :
    termSum (wordLin b i z) Ψ = (b i).constr R (fun o => Ψ (wordList i o)) z := by
  rw [termSum_eq_lc]
  change ((Finsupp.linearCombination R fun p => Ψ (FreeMonoid.toList p)) ∘ₗ wordLin b i) z = _
  congr 1
  refine (b i).ext fun o => ?_
  rw [LinearMap.comp_apply, wordLin, Module.Basis.constr_basis]
  erw [Module.Basis.constr_basis, wordOf_eq_ofW, ofW, Finsupp.linearCombination_single, one_smul]
  rfl

variable [Nonempty (Σ i, L i)] (wtL : ∀ i, L i → ℕ)
  {β : Type*} [LinearOrder β] [WellFoundedLT β] (rank : (Σ i, L i) → β)
  (rank_inj : Function.Injective rank)

/-- The block product: the structure constants of `Aᵢ` in `bᵢ`. -/
def splayμ (a c : Σ i, L i) : MA (Σ i, L i) R :=
  if h : c.1 = a.1 then wordLin b a.1 (b a.1 (some a.2) * b a.1 (some (h ▸ c.2))) else 0

theorem splayμ_same (i : I) (x y : L i) :
    splayμ b ⟨i, x⟩ ⟨i, y⟩ = wordLin b i (b i (some x) * b i (some y)) := by
  simp [splayμ]

variable {b} in
theorem mem_support_wordLin {i : I} {z : A i} {p : FreeMonoid (Σ i, L i)}
    (hp : p ∈ (wordLin b i z).support) :
    ∃ o, (b i).repr z o ≠ 0 ∧ FreeMonoid.toList p = wordList i o := by
  classical
  by_contra H
  push_neg at H
  apply (Finsupp.mem_support_iff.1 hp)
  rw [wordLin, Module.Basis.constr_apply, Finsupp.sum, Finsupp.finset_sum_apply]
  refine Finset.sum_eq_zero fun o ho => ?_
  rw [Finsupp.smul_apply, wordOf_eq_ofW, ofW]
  erw [MonoidAlgebra.single_apply]
  split_ifs with h
  · exact absurd (by rw [← h]; rfl) (H o (Finsupp.mem_support_iff.1 ho))
  · simp

/-- The weight of a letter. -/
def splayWt (g : Σ i, L i) : ℕ := wtL g.1 g.2

variable [LinearOrder I] (π : (Σ i, L i) → (Σ i, L i) → MA (Σ i, L i) R)
  (hshort : ∀ i (x y o : L i), (b i).repr (b i (some x) * b i (some y)) (some o) ≠ 0 →
    wtL i o ≤ wtL i x + wtL i y)
  (hmono : ∀ a c : Σ i, L i, c.1 < a.1 → rank c < rank a)
  (hπwt : ∀ a c : Σ i, L i, c.1 < a.1 → ∀ p ∈ (π a c).support,
    wsum (splayWt wtL) (FreeMonoid.toList p) < splayWt wtL a + splayWt wtL c)

include hshort hmono hπwt in
/-- The block-splay data of the splay of the `Aᵢ`: blocks the indices, block product
    the structure constants, weight-then-deg-lex order. -/
def splayBD : BlockData (Σ i, L i) R (weightedOrderWF (splayWt wtL) rank rank_inj) I where
  blk g := g.1
  μ := splayμ b
  π := π
  inhabited := inferInstance
  wt := splayWt wtL
  μ_short a c h p hp := by
    obtain ⟨i, x⟩ := a
    obtain ⟨j, y⟩ := c
    dsimp only at h
    subst h
    rw [splayμ_same] at hp
    obtain ⟨o, ho, hpo⟩ := mem_support_wordLin hp
    rcases o with _ | o
    · exact Or.inl hpo
    · exact Or.inr ⟨⟨i, o⟩, hpo, rfl, hshort i x y o ho⟩
  lt_of_wt := weightedOrderWF_lt_of_wt _ rank rank_inj
  swap_lt a c h := weightedOrderWF_swap_lt _ rank rank_inj (hmono a c h)
  π_lt a c h p hp := weightedOrderWF_lt_of_wsum_lt _ rank rank_inj _ _ (by
    have := hπwt a c h p hp
    simpa [wsum] using this)

variable (hb1 : ∀ i, b i none = 1)

include hb1 in
theorem wordLin_basis_some (i : I) (x : L i) :
    wordLin b i (b i (some x)) = ofW [⟨i, x⟩] := by
  rw [wordLin, Module.Basis.constr_basis]; rfl

include hb1 in
theorem splayBD_leftMul (i : I) (x : L i) (z : A i) :
    (splayBD b wtL rank rank_inj π hshort hmono hπwt).leftMul ⟨i, x⟩ (wordLin b i z) =
      wordLin b i (b i (some x) * z) := by
  rw [BlockData.leftMul, termSum_wordLin]
  change _ = (wordLin b i ∘ₗ LinearMap.mulLeft R (b i (some x))) z
  congr 1
  refine (b i).ext fun o => ?_
  rw [Module.Basis.constr_basis, LinearMap.comp_apply, LinearMap.mulLeft_apply]
  rcases o with _ | y
  · rw [hb1, mul_one, wordLin_basis_some b hb1]; rfl
  · exact splayμ_same b i x y

include hb1 in
theorem splayBD_rightMul (i : I) (y : L i) (z : A i) :
    (splayBD b wtL rank rank_inj π hshort hmono hπwt).rightMul ⟨i, y⟩ (wordLin b i z) =
      wordLin b i (z * b i (some y)) := by
  rw [BlockData.rightMul, termSum_wordLin]
  change _ = (wordLin b i ∘ₗ LinearMap.mulRight R (b i (some y))) z
  congr 1
  refine (b i).ext fun o => ?_
  rw [Module.Basis.constr_basis, LinearMap.comp_apply, LinearMap.mulRight_apply]
  rcases o with _ | x
  · rw [hb1, one_mul, wordLin_basis_some b hb1]; rfl
  · exact splayμ_same b i x y


include hb1 in
/-- **The filtered block-splay data** of the splay of the `Aᵢ`. -/
def splayFD : FilteredData (Σ i, L i) R (weightedOrderWF (splayWt wtL) rank rank_inj) I where
  toBlockData := splayBD b wtL rank rank_inj π hshort hmono hπwt
  lt_of_wsum_lt := weightedOrderWF_lt_of_wsum_lt _ rank rank_inj
  π_wt := hπwt
  assoc a c d h1 h2 := by
    obtain ⟨i, x⟩ := a
    obtain ⟨j, y⟩ := c
    obtain ⟨l, w⟩ := d
    change i = j at h1
    change j = l at h2
    subst h1; subst h2
    change (splayBD b wtL rank rank_inj π hshort hmono hπwt).leftMul _ (splayμ b _ _) =
      (splayBD b wtL rank rank_inj π hshort hmono hπwt).rightMul _ (splayμ b _ _)
    rw [splayμ_same, splayμ_same, splayBD_leftMul b wtL rank rank_inj π hshort hmono hπwt hb1,
      splayBD_rightMul b wtL rank rank_inj π hshort hmono hπwt hb1, mul_assoc]
  comm a c h := by
    obtain ⟨i, x⟩ := a
    obtain ⟨j, y⟩ := c
    change i = j at h
    subst h
    change splayμ b _ _ = splayμ b _ _
    rw [splayμ_same, splayμ_same, mul_comm]

variable [Nontrivial R] (ρ : SplayPoisson R A)
  (hπ : ∀ a c : Σ i, L i, c.1 < a.1 →
    qT b (π a c) = ρ.toPoissonStructure.bracket (letter b a) (letter b c))

include hb1 hπ in
/-- **Thm. 3.7 of arXiv:math/0602138 (PBW basis), from the paper's hypotheses.**
    Let each `Aᵢ` be a commutative `R`-algebra with a basis `bᵢ` indexed by
    `Option Lᵢ`, `bᵢ none = 1`, and weights `wtL` on the `Lᵢ` such that a product of
    two basis elements involves only basis elements of no larger weight
    (`hshort`). Let `ρ` be a Poisson structure on the splay algebra `T = ∐ Aᵢ` that
    restricts to zero on each `Aᵢ`, and suppose it is **strongly filtered**: for
    letters `a, c` of blocks `c.1 < a.1` the bracket of their images has a preimage
    `π a c` all of whose monomials are lighter than `a c` (`hπwt`, `hπ`). Then the
    ordered monomials of the weight-then-deg-lex order are an `R`-basis of
    `U = T / (fg − gf − ρ(f, g))`. The rank `rank` only fixes the order; any
    injective rank into a well-founded linear order increasing with the block will do. -/
theorem splay_integrationBasis [DecidableEq R] :
    ∃ B : Module.Basis {m : Monomial (Σ i, L i) //
        NormalFormMonomial (weightedOrderWF (splayWt wtL) rank rank_inj)
          (splayFD b wtL rank rank_inj π hshort hmono hπwt hb1).quad.sys m} R
        (IntegrationQuotient ρ.toPoissonStructure),
      ∀ m, B m = integrationMk _ (qT b (ofW m.val)) :=
  integrationBasis (F := splayFD b wtL rank rank_inj π hshort hmono hπwt hb1) hb1
    (fun _ => rfl)
    (fun i x y => by
      change splayμ b _ _ = _
      rw [splayμ_same, wordLin, Module.Basis.constr_apply])
    ρ hπ

end

end QOU.FormalGroups.PBW
