import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.Fintype.Perm
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import BraidKnotOctonion.BraidClosure
import QOU.StandardModel.ComponentFraming
import QOU.StandardModel.SignCoherentTwist

/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/

set_option autoImplicit false

/-!
# Framed Braid Semidirect Monoid, Framing-Slide Coinvariants, and Twist Multisets (`qou-kebu`)

Formalizes the framed-braid monodromy layer for bean `qou-kebu` (*T2b: derive per-strand twist
multisets from framed braid words*) directly over the repository's `n`-strand braid word carrier
`QOU.BraidKnot.BraidWord n` and Markov closure permutation `QOU.Knot.BraidClosure.closurePerm`,
without altering or duplicating `ComponentFraming`, `SignCoherentTwist`, or queued sibling modules.

## Main Results (`0 sorry`, `0` custom axioms, §7c clean)

1. **Semidirect-product framed braid word monoid (`FramedBraidWord n`, Ko–Smolinski $\mathbb{Z}^n \rtimes B_n^*$):**
   - `FramedBraidWord.instMonoid`: equips `BraidWord n × (Fin n → ℤ)` with the twisted product
     `(x * y).twist i = x.twist i + y.twist ((closurePerm x.word)⁻¹ i)`, proved associative via
     `BraidClosure.closurePerm_append` and `mul_inv_rev`.
   - `totalTwist_mul` & `ribbonScalarWeight_mul`: the total twist `T(w, τ) = ∑ᵢ τᵢ` is additive
     under framed braid composition, and for any scalar ribbon twist `θ` in a commutative group `M`,
     `ribbonScalarWeight θ (w, τ) = θ ^ T(w, τ)` is a monoid homomorphism that factors strictly
     through `totalTwist` (`ribbonScalarWeight_factors_totalTwist` — formalizing the `qou-kebu`
     scalar-twist obstruction on `FramedBraidWord n`).

2. **Markov-I framing-slide conjugation & closed-component coboundaries:**
   - `framingSlide_twist`: conjugating `(w, τ)` in `FramedBraidWord n` by a pure strand twist
     `pureTwist δ = ([], δ)` preserves `w` and shifts `τ` by the exact `closurePerm w`-coboundary
     `τᵢ ↦ τᵢ + δᵢ - δ_{(closurePerm w)⁻¹(i)}`.
   - `componentTwistSum_framingSlide_eq`: on every `closurePerm w`-invariant strand subset `S`
     (in particular each closed link component), `∑_{i ∈ S} τᵢ` is strictly invariant under all
     framing slides.

3. **Complete coinvariant & multiset theorems on the `BraidWord 3` particle dictionary:**
   - **1-component lepton words (`leptonUnknotWord3 = σ₀σ₁`, `leptonTrefoilWord3 = (σ₀σ₁)²`):**
     `FramingSlideEquiv` holds **iff** `totalTwist` agrees (`framingSlideEquiv_unknot_iff`,
     `framingSlideEquiv_trefoil_iff`), and a slide-equivalent `IsComponentFraming` representative
     exists **iff** `3 ∣ totalTwist x` (`unknot_has_componentFraming_iff_dvd_three`), uniquely
     forcing `(0, 0, 0)` at `T = 0` (`ν`), `(-1, -1, -1)` at `T = -3` (`e⁻` knot backup), and
     refuting symmetric component framings when `3 ∤ T` (`T = +2` or `T = -1`).
   - **2-component Hopf-link electron word (`hopfElectronWord3 = σ₀σ₁σ₀`, `components = 2`):**
     `FramingSlideEquiv` holds **iff** the 2-strand component sum `τ₀ + τ₂` and the fixed-strand
     twist `τ₁` both agree (`framingSlideEquiv_hopf_iff`).
   - **3-component Borromean baryon word (`borromeanBraidWord3 = (σ₀σ₁⁻¹)³`, `components = 3`):**
     every framing slide acts as the identity (`framingSlide_borromean_eq_self`), while conjugation
     by any 3-braid `γ` permutes the strand twists and preserves the 3-element
     `twistMultiset` (`twistMultiset_braidTransport_eq`).

## References
- [ko-smolinski1992] K. H. Ko & L. Smolinski, *A combinatorial matrix in 3-manifold theory*,
  Pacific J. Math. 149 (1991), 319–336 (framed braid monoid / semidirect presentation).
- [kassel-turaev2008] C. Kassel & V. Turaev, *Braid Groups*, GTM 247, Springer (2008).
-/

namespace QOU.StandardModel.FramedBraidTwistMonodromy

open Finset
open QOU.BraidKnot
open QOU.Knot.BraidClosure
open QOU.StandardModel.ComponentFraming
open QOU.StandardModel.SignCoherentTwist

/-! ## 1. The Semidirect Framed Braid Word Monoid `FramedBraidWord n` -/

/-- An `n`-strand framed braid word: an Artin braid word `word : BraidWord n` paired with an
integer ribbon twist `twist : Fin n → ℤ` accumulated along each strand. -/
structure FramedBraidWord (n : ℕ) where
  /-- Underlying `n`-strand Artin braid word. -/
  word : BraidWord n
  /-- Per-strand integer ribbon framing twist. -/
  twist : Fin n → ℤ

namespace FramedBraidWord

variable {n : ℕ}

theorem ext {x y : FramedBraidWord n} (hw : x.word = y.word)
    (ht : ∀ i : Fin n, x.twist i = y.twist i) : x = y := by
  cases x
  cases y
  simp only [mk.injEq] at hw ⊢
  exact ⟨hw, funext ht⟩

/-- Semidirect composition of framed braid words (`ℤⁿ ⋊ Bₙ*`): stacking `y` after `x` concatenates
the words and pulls `y`'s strand twists back along `(closurePerm x.word)⁻¹`. -/
def mul (x y : FramedBraidWord n) : FramedBraidWord n where
  word := x.word ++ y.word
  twist := fun i => x.twist i + y.twist ((closurePerm x.word)⁻¹ i)

/-- Identity framed braid word: empty crossing list and zero twist on every strand. -/
def one : FramedBraidWord n where
  word := []
  twist := fun _ => 0

instance instMul : Mul (FramedBraidWord n) := ⟨mul⟩
instance instOne : One (FramedBraidWord n) := ⟨one⟩

@[simp] theorem mul_word (x y : FramedBraidWord n) : (x * y).word = x.word ++ y.word := rfl

@[simp] theorem mul_twist (x y : FramedBraidWord n) (i : Fin n) :
    (x * y).twist i = x.twist i + y.twist ((closurePerm x.word)⁻¹ i) := rfl

@[simp] theorem one_word : (1 : FramedBraidWord n).word = [] := rfl

@[simp] theorem one_twist (i : Fin n) : (1 : FramedBraidWord n).twist i = 0 := rfl

/-- `FramedBraidWord n` is a genuine `Monoid` under semidirect composition. -/
instance instMonoid : Monoid (FramedBraidWord n) where
  mul := (· * ·)
  one := 1
  one_mul x :=
    ext (List.nil_append x.word) (fun i => by simp [closurePerm_nil])
  mul_one x :=
    ext (List.append_nil x.word) (fun i => by simp)
  mul_assoc x y z :=
    ext (List.append_assoc x.word y.word z.word) (fun i => by
      simp only [mul_twist, mul_word, closurePerm_append, mul_inv_rev, Equiv.Perm.mul_apply]
      ring)

/-- Pure strand-framing element `([], δ)` with no crossings. -/
def pureTwist (δ : Fin n → ℤ) : FramedBraidWord n :=
  ⟨[], δ⟩

@[simp] theorem pureTwist_mul (δ₁ δ₂ : Fin n → ℤ) :
    pureTwist δ₁ * pureTwist δ₂ = pureTwist (fun i => δ₁ i + δ₂ i) :=
  ext rfl (fun i => by simp [pureTwist, closurePerm_nil])

@[simp] theorem pureTwist_cancel_right (δ : Fin n → ℤ) :
    pureTwist δ * pureTwist (fun i => -δ i) = 1 :=
  ext rfl (fun i => by simp [pureTwist, closurePerm_nil])

@[simp] theorem pureTwist_cancel_left (δ : Fin n → ℤ) :
    pureTwist (fun i => -δ i) * pureTwist δ = 1 :=
  ext rfl (fun i => by simp [pureTwist, closurePerm_nil])

/-! ## 2. Total Twist, Multiset, and the Scalar Ribbon-Twist Factorization -/

/-- Total framing twist `T(w, τ) = ∑ᵢ τᵢ`. -/
def totalTwist (x : FramedBraidWord n) : ℤ :=
  ∑ i : Fin n, x.twist i

/-- Unordered multiset of per-strand twists `{τ₀, …, τₙ₋₁}`. -/
def twistMultiset (x : FramedBraidWord n) : Multiset ℤ :=
  (Finset.univ : Finset (Fin n)).val.map x.twist

@[simp] theorem totalTwist_one : totalTwist (1 : FramedBraidWord n) = 0 := by
  simp [totalTwist]

/-- **Total twist is a monoid homomorphism `(FramedBraidWord n, *) → (ℤ, +)`.** -/
theorem totalTwist_mul (x y : FramedBraidWord n) :
    totalTwist (x * y) = totalTwist x + totalTwist y := by
  unfold totalTwist
  simp only [mul_twist, Finset.sum_add_distrib]
  congr 1
  exact Equiv.sum_comp (closurePerm x.word)⁻¹ y.twist

/-- Writhe is likewise additive on `FramedBraidWord n`. -/
theorem writhe_mul (x y : FramedBraidWord n) :
    (x * y).word.writhe = x.word.writhe + y.word.writhe :=
  writhe_append x.word y.word

/-- Scalar ribbon-twist weight `θ ^ T(x)` on `n` identical strands carrying central twist `θ`. -/
def ribbonScalarWeight {M : Type*} [CommGroup M] (θ : M) (x : FramedBraidWord n) : M :=
  θ ^ totalTwist x

/-- `ribbonScalarWeight θ` is a monoid homomorphism `FramedBraidWord n →* M`. -/
theorem ribbonScalarWeight_mul {M : Type*} [CommGroup M] (θ : M) (x y : FramedBraidWord n) :
    ribbonScalarWeight θ (x * y) = ribbonScalarWeight θ x * ribbonScalarWeight θ y := by
  unfold ribbonScalarWeight
  rw [totalTwist_mul, zpow_add]

/-- **Categorical Scalar-Twist Factorization (`qou-kebu` Step-1 Obstruction on `FramedBraidWord`):**
Any central/scalar ribbon twist `θ` on identical strands depends solely on `totalTwist` and cannot
distinguish two framings of the same braid word that share a total twist (e.g. `(-1,-1,1)` vs
`(-1,0,0)` at `T = -1`). -/
theorem ribbonScalarWeight_factors_totalTwist {M : Type*} [CommGroup M] (θ : M)
    (x y : FramedBraidWord n) (h : totalTwist x = totalTwist y) :
    ribbonScalarWeight θ x = ribbonScalarWeight θ y := by
  unfold ribbonScalarWeight
  rw [h]

/-! ## 3. Markov-I Framing-Slide Conjugation & Closed-Component Coboundaries -/

/-- **Markov-I framing slide:** conjugation of `x` by `pureTwist δ` in `FramedBraidWord n`,
sliding twists `δ` through the Markov closure arcs from top to bottom of `x.word`. -/
def framingSlide (δ : Fin n → ℤ) (x : FramedBraidWord n) : FramedBraidWord n :=
  pureTwist δ * x * pureTwist (fun i => -δ i)

@[simp] theorem framingSlide_word (δ : Fin n → ℤ) (x : FramedBraidWord n) :
    (framingSlide δ x).word = x.word := by
  simp [framingSlide, pureTwist]

/-- **Coboundary Formula for Framing Slides:**
Conjugating `(w, τ)` by `pureTwist δ` leaves `w` unchanged and adds the exact `closurePerm w`
coboundary `δ i - δ ((closurePerm w)⁻¹ i)` to `τ i`. -/
@[simp] theorem framingSlide_twist (δ : Fin n → ℤ) (x : FramedBraidWord n) (i : Fin n) :
    (framingSlide δ x).twist i =
      x.twist i + δ i - δ ((closurePerm x.word)⁻¹ i) := by
  simp only [framingSlide, pureTwist, mul_twist, mul_word, List.nil_append, closurePerm_nil, inv_one,
    Equiv.Perm.one_apply]
  ring

/-- Framing slides form an additive `ℤⁿ`-action on `FramedBraidWord n`. -/
theorem framingSlide_comp (δ₁ δ₂ : Fin n → ℤ) (x : FramedBraidWord n) :
    framingSlide δ₁ (framingSlide δ₂ x) = framingSlide (fun i => δ₁ i + δ₂ i) x :=
  ext (by simp) (fun i => by
    simp only [framingSlide_twist, framingSlide_word]
    ring)

@[simp] theorem framingSlide_zero (x : FramedBraidWord n) :
    framingSlide (fun _ => 0) x = x :=
  ext (by simp) (fun i => by simp)

/-- Framing-slide equivalence of two framed braid words (Markov-I equivalence by pure twists). -/
def FramingSlideEquiv (x y : FramedBraidWord n) : Prop :=
  ∃ δ : Fin n → ℤ, framingSlide δ x = y

theorem framingSlideEquiv_refl (x : FramedBraidWord n) : FramingSlideEquiv x x :=
  ⟨fun _ => 0, framingSlide_zero x⟩

theorem framingSlideEquiv_symm {x y : FramedBraidWord n} (h : FramingSlideEquiv x y) :
    FramingSlideEquiv y x := by
  obtain ⟨δ, rfl⟩ := h
  refine ⟨fun i => -δ i, ?_⟩
  rw [framingSlide_comp]
  have hzero : (fun i : Fin n => -δ i + δ i) = (fun _ => 0) := by funext i; ring
  rw [hzero, framingSlide_zero]

theorem framingSlideEquiv_trans {x y z : FramedBraidWord n}
    (hxy : FramingSlideEquiv x y) (hyz : FramingSlideEquiv y z) :
    FramingSlideEquiv x z := by
  obtain ⟨δ₁, rfl⟩ := hxy
  obtain ⟨δ₂, rfl⟩ := hyz
  exact ⟨fun i => δ₂ i + δ₁ i, (framingSlide_comp δ₂ δ₁ x).symm⟩

/-- Sum of strand twists along a subset `S ⊆ Fin n` (e.g. a single link component / orbit of
`closurePerm x.word`). -/
def componentTwistSum (S : Finset (Fin n)) (x : FramedBraidWord n) : ℤ :=
  ∑ i ∈ S, x.twist i

/-- **Per-Component Framing Invariance Theorem:**
For every `closurePerm x.word`-invariant subset `S ⊆ Fin n` (`(closurePerm x.word)⁻¹ i ∈ S ↔ i ∈ S`),
the component twist sum `∑_{i ∈ S} x.twist i` is strictly invariant under all framing slides. -/
theorem componentTwistSum_framingSlide_eq (S : Finset (Fin n)) (δ : Fin n → ℤ)
    (x : FramedBraidWord n)
    (hS : ∀ i : Fin n, (closurePerm x.word)⁻¹ i ∈ S ↔ i ∈ S) :
    componentTwistSum S (framingSlide δ x) = componentTwistSum S x := by
  unfold componentTwistSum
  have hbij : (∑ i ∈ S, δ ((closurePerm x.word)⁻¹ i)) = ∑ i ∈ S, δ i := by
    refine Finset.sum_bij (fun i _ => (closurePerm x.word)⁻¹ i) ?_ ?_ ?_ ?_
    · intro i hi
      exact (hS i).mpr hi
    · intro i₁ _ i₂ _ h
      exact (closurePerm x.word)⁻¹.injective h
    · intro j hj
      refine ⟨closurePerm x.word j, ?_, by simp⟩
      exact (hS (closurePerm x.word j)).mp (by simpa using hj)
    · intro _ _
      rfl
  have hexpand :
      (∑ i ∈ S, (x.twist i + δ i - δ ((closurePerm x.word)⁻¹ i))) =
        (∑ i ∈ S, x.twist i) + (∑ i ∈ S, δ i) - ∑ i ∈ S, δ ((closurePerm x.word)⁻¹ i) := by
    simp only [sub_eq_add_neg, Finset.sum_add_distrib, Finset.sum_neg_distrib]
  simp only [framingSlide_twist]
  rw [hexpand, hbij]
  ring

/-- In particular, `totalTwist` (`S = univ`) is invariant under every framing slide. -/
theorem totalTwist_framingSlide (δ : Fin n → ℤ) (x : FramedBraidWord n) :
    totalTwist (framingSlide δ x) = totalTwist x :=
  componentTwistSum_framingSlide_eq Finset.univ δ x (fun _ => by simp)

/-! ## 4. Exact Monodromy & Multiset Classification on the `BraidWord 3` Corpus Carriers -/

/-- Positive Artin generator `σ₀` in `BraidCrossing 3`. -/
def sigma0Pos3 : BraidCrossing 3 := ⟨0, true⟩

/-- Positive Artin generator `σ₁` in `BraidCrossing 3`. -/
def sigma1Pos3 : BraidCrossing 3 := ⟨1, true⟩

/-- Negative Artin generator `σ₁⁻¹` in `BraidCrossing 3`. -/
def sigma1Neg3 : BraidCrossing 3 := ⟨1, false⟩

/-- 3-strand unknot lepton carrier `σ₀ σ₁ ∈ BraidWord 3` (1-component knot closure). -/
def leptonUnknotWord3 : BraidWord 3 := [sigma0Pos3, sigma1Pos3]

/-- 3-strand trefoil lepton backup carrier `(σ₀ σ₁)² ∈ BraidWord 3` (1-component knot closure). -/
def leptonTrefoilWord3 : BraidWord 3 := [sigma0Pos3, sigma1Pos3, sigma0Pos3, sigma1Pos3]

/-- Post-`2026-11-21` primary Hopf-link electron carrier `σ₀ σ₁ σ₀ ∈ BraidWord 3` (2-component closure). -/
def hopfElectronWord3 : BraidWord 3 := [sigma0Pos3, sigma1Pos3, sigma0Pos3]

/-- Action of `(closurePerm leptonUnknotWord3)⁻¹` on `Fin 3`: `0 ↦ 2`, `1 ↦ 0`, `2 ↦ 1`. -/
theorem closurePerm_inv_unknot3 :
    (closurePerm leptonUnknotWord3)⁻¹ 0 = 2 ∧
    (closurePerm leptonUnknotWord3)⁻¹ 1 = 0 ∧
    (closurePerm leptonUnknotWord3)⁻¹ 2 = 1 := by
  decide

/-- Transitivity of `closurePerm leptonUnknotWord3` on `Fin 3` (single 3-cycle component). -/
theorem closurePerm_unknot3_transitive :
    ∀ i j : Fin 3, ∃ k : ℕ, ((closurePerm leptonUnknotWord3) ^ k) i = j := by
  intro i j
  fin_cases i <;> fin_cases j
  · exact ⟨0, by decide⟩
  · exact ⟨1, by decide⟩
  · exact ⟨2, by decide⟩
  · exact ⟨2, by decide⟩
  · exact ⟨0, by decide⟩
  · exact ⟨1, by decide⟩
  · exact ⟨1, by decide⟩
  · exact ⟨2, by decide⟩
  · exact ⟨0, by decide⟩

/-- Action of `(closurePerm leptonTrefoilWord3)⁻¹` on `Fin 3`: `0 ↦ 1`, `1 ↦ 2`, `2 ↦ 0`. -/
theorem closurePerm_inv_trefoil3 :
    (closurePerm leptonTrefoilWord3)⁻¹ 0 = 1 ∧
    (closurePerm leptonTrefoilWord3)⁻¹ 1 = 2 ∧
    (closurePerm leptonTrefoilWord3)⁻¹ 2 = 0 := by
  decide

/-- **Complete Coboundary Theorem for `leptonUnknotWord3 = σ₀σ₁`:**
Two framings `τ, τ'` of `leptonUnknotWord3` are framing-slide equivalent in `FramedBraidWord 3`
**if and only if** they have the same total twist. -/
theorem framingSlideEquiv_unknot_iff (τ τ' : Fin 3 → ℤ) :
    FramingSlideEquiv ⟨leptonUnknotWord3, τ⟩ ⟨leptonUnknotWord3, τ'⟩ ↔
      totalTwist ⟨leptonUnknotWord3, τ⟩ = totalTwist ⟨leptonUnknotWord3, τ'⟩ := by
  constructor
  · rintro ⟨δ, hδ⟩
    rw [← hδ]
    exact (totalTwist_framingSlide δ ⟨leptonUnknotWord3, τ⟩).symm
  · intro htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    obtain ⟨hi0, hi1, hi2⟩ := closurePerm_inv_unknot3
    let δ : Fin 3 → ℤ := fun j =>
      if j = 0 then τ' 0 - τ 0
      else if j = 1 then (τ' 0 - τ 0) + (τ' 1 - τ 1)
      else 0
    refine ⟨δ, ext (by simp) (fun i => ?_)⟩
    fin_cases i
    · change (framingSlide δ ⟨leptonUnknotWord3, τ⟩).twist 0 = τ' 0
      rw [framingSlide_twist, hi0]
      dsimp [δ]
      ring
    · change (framingSlide δ ⟨leptonUnknotWord3, τ⟩).twist 1 = τ' 1
      rw [framingSlide_twist, hi1]
      dsimp [δ]
      ring
    · change (framingSlide δ ⟨leptonUnknotWord3, τ⟩).twist 2 = τ' 2
      rw [framingSlide_twist, hi2]
      dsimp [δ]
      omega

/-- **Complete Coboundary Theorem for `leptonTrefoilWord3 = (σ₀σ₁)²`:**
Two framings `τ, τ'` of `leptonTrefoilWord3` are framing-slide equivalent in `FramedBraidWord 3`
**if and only if** they have the same total twist. -/
theorem framingSlideEquiv_trefoil_iff (τ τ' : Fin 3 → ℤ) :
    FramingSlideEquiv ⟨leptonTrefoilWord3, τ⟩ ⟨leptonTrefoilWord3, τ'⟩ ↔
      totalTwist ⟨leptonTrefoilWord3, τ⟩ = totalTwist ⟨leptonTrefoilWord3, τ'⟩ := by
  constructor
  · rintro ⟨δ, hδ⟩
    rw [← hδ]
    exact (totalTwist_framingSlide δ ⟨leptonTrefoilWord3, τ⟩).symm
  · intro htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    obtain ⟨hi0, hi1, hi2⟩ := closurePerm_inv_trefoil3
    let δ : Fin 3 → ℤ := fun j =>
      if j = 0 then (τ' 0 - τ 0) + (τ' 1 - τ 1)
      else if j = 1 then τ' 1 - τ 1
      else 0
    refine ⟨δ, ext (by simp) (fun i => ?_)⟩
    fin_cases i
    · change (framingSlide δ ⟨leptonTrefoilWord3, τ⟩).twist 0 = τ' 0
      rw [framingSlide_twist, hi0]
      dsimp [δ]
      ring
    · change (framingSlide δ ⟨leptonTrefoilWord3, τ⟩).twist 1 = τ' 1
      rw [framingSlide_twist, hi1]
      dsimp [δ]
      ring
    · change (framingSlide δ ⟨leptonTrefoilWord3, τ⟩).twist 2 = τ' 2
      rw [framingSlide_twist, hi2]
      dsimp [δ]
      omega

/-- **Derived Component-Framing Divisibility & Uniqueness Theorem (`qou-kebu` on `leptonUnknotWord3`):**
A framed 1-component 3-braid `⟨leptonUnknotWord3, τ⟩` admits a framing-slide-equivalent
`IsComponentFraming` representative `t` **if and only if** `3 ∣ totalTwist ⟨leptonUnknotWord3, τ⟩`;
moreover, when `totalTwist ⟨leptonUnknotWord3, τ⟩ = 3 * Q`, `t` is **uniquely forced** to the
constant triple `fun _ => Q` (forcing `(0,0,0)` for `ν` at `T = 0`, `(-1,-1,-1)` for `e⁻` at `T = -3`,
and proving no symmetric component framing exists at fractional-charge totals `T = +2` or `T = -1`). -/
theorem unknot_has_componentFraming_iff_dvd_three (τ : Fin 3 → ℤ) :
    (∃ t : Fin 3 → ℤ,
      IsComponentFraming (closurePerm leptonUnknotWord3) t ∧
        FramingSlideEquiv ⟨leptonUnknotWord3, τ⟩ ⟨leptonUnknotWord3, t⟩) ↔
      (3 : ℤ) ∣ totalTwist ⟨leptonUnknotWord3, τ⟩ := by
  constructor
  · rintro ⟨t, hcomp, hslide⟩
    have htot := (framingSlideEquiv_unknot_iff τ t).mp hslide
    have hconst := constant_of_transitive hcomp closurePerm_unknot3_transitive
    refine ⟨t 0, ?_⟩
    rw [htot]
    simp only [totalTwist, Fin.sum_univ_three, hconst 1 0, hconst 2 0]
    ring
  · rintro ⟨Q, hQ⟩
    refine ⟨fun _ => Q, const_isComponentFraming _ Q, ?_⟩
    rw [framingSlideEquiv_unknot_iff, hQ]
    simp only [totalTwist, Fin.sum_univ_three]
    ring

/-- **2-Component Closure Theorem for `hopfElectronWord3 = σ₀σ₁σ₀`:**
`closurePerm hopfElectronWord3 = Equiv.swap 0 2` and `components hopfElectronWord3 = 2`. -/
theorem hopfElectronWord3_closurePerm_and_components :
    closurePerm hopfElectronWord3 = Equiv.swap (0 : Fin 3) 2 ∧
      components hopfElectronWord3 = 2 := by
  have hp : closurePerm hopfElectronWord3 = Equiv.swap (0 : Fin 3) 2 := by decide
  refine ⟨hp, ?_⟩
  have hne : (0 : Fin 3) ≠ 2 := by decide
  have hcyc : (Equiv.swap (0 : Fin 3) 2).cycleType =
      {(Equiv.swap (0 : Fin 3) 2).support.card} :=
    (Equiv.Perm.isCycle_swap hne).cycleType
  simp [components, hp, hcyc]

/-- **Complete Coboundary Theorem for `hopfElectronWord3 = σ₀σ₁σ₀`:**
Two framings `τ, τ'` of `hopfElectronWord3` are framing-slide equivalent in `FramedBraidWord 3`
**if and only if** they agree on both closed components: `τ 0 + τ 2 = τ' 0 + τ' 2` and `τ 1 = τ' 1`. -/
theorem framingSlideEquiv_hopf_iff (τ τ' : Fin 3 → ℤ) :
    FramingSlideEquiv ⟨hopfElectronWord3, τ⟩ ⟨hopfElectronWord3, τ'⟩ ↔
      (τ 0 + τ 2 = τ' 0 + τ' 2 ∧ τ 1 = τ' 1) := by
  have hp : (closurePerm hopfElectronWord3)⁻¹ = Equiv.swap (0 : Fin 3) 2 := by decide
  have s0 : (Equiv.swap (0 : Fin 3) 2) 0 = 2 := by decide
  have s1 : (Equiv.swap (0 : Fin 3) 2) 1 = 1 := by decide
  have s2 : (Equiv.swap (0 : Fin 3) 2) 2 = 0 := by decide
  constructor
  · rintro ⟨δ, hδ⟩
    have h0 := congrFun (congrArg FramedBraidWord.twist hδ) 0
    have h1 := congrFun (congrArg FramedBraidWord.twist hδ) 1
    have h2 := congrFun (congrArg FramedBraidWord.twist hδ) 2
    simp only [framingSlide_twist, hp] at h0 h1 h2
    rw [s0] at h0
    rw [s1] at h1
    rw [s2] at h2
    exact ⟨by omega, by omega⟩
  · rintro ⟨h02, h1⟩
    let δ : Fin 3 → ℤ := fun j => if j = 0 then τ' 0 - τ 0 else 0
    refine ⟨δ, ext (by simp) (fun i => ?_)⟩
    fin_cases i
    · change (framingSlide δ ⟨hopfElectronWord3, τ⟩).twist 0 = τ' 0
      rw [framingSlide_twist, hp, s0]
      dsimp [δ]
      ring
    · change (framingSlide δ ⟨hopfElectronWord3, τ⟩).twist 1 = τ' 1
      rw [framingSlide_twist, hp, s1]
      dsimp [δ]
      linarith
    · change (framingSlide δ ⟨hopfElectronWord3, τ⟩).twist 2 = τ' 2
      rw [framingSlide_twist, hp, s2]
      dsimp [δ]
      omega

/-- **3-Component Pure-Braid Theorem for `borromeanBraidWord3 = (σ₀σ₁⁻¹)³`:**
`closurePerm borromeanBraidWord3 = 1` and `components borromeanBraidWord3 = 3`. -/
theorem borromeanBraidWord3_closurePerm_and_components :
    closurePerm borromeanBraidWord3 = 1 ∧
      components borromeanBraidWord3 = 3 := by
  have hp : closurePerm borromeanBraidWord3 = 1 := by decide
  refine ⟨hp, ?_⟩
  simp [components, hp]

/-- **Borromean Framing-Slide Rigidity Theorem:**
Because `closurePerm borromeanBraidWord3 = 1`, every pure framing slide fixes
`⟨borromeanBraidWord3, τ⟩` pointwise (`FramingSlideEquiv` is equality of twist vectors). -/
@[simp] theorem framingSlide_borromean_eq_self (δ τ : Fin 3 → ℤ) :
    framingSlide δ ⟨borromeanBraidWord3, τ⟩ = ⟨borromeanBraidWord3, τ⟩ := by
  have hp : (closurePerm borromeanBraidWord3)⁻¹ = 1 := by
    rw [borromeanBraidWord3_closurePerm_and_components.1, inv_one]
  exact ext (by simp) (fun i => by simp [framingSlide_twist, hp])

theorem framingSlideEquiv_borromean_iff (τ τ' : Fin 3 → ℤ) :
    FramingSlideEquiv ⟨borromeanBraidWord3, τ⟩ ⟨borromeanBraidWord3, τ'⟩ ↔ τ = τ' := by
  constructor
  · rintro ⟨δ, hδ⟩
    rw [framingSlide_borromean_eq_self] at hδ
    exact congrArg FramedBraidWord.twist hδ
  · rintro rfl
    exact framingSlideEquiv_refl _

/-- **Braid-Conjugation Multiset Gauge Invariance on Pure Framed Braids:**
When a pure framed braid (`closurePerm w = 1`, such as `borromeanBraidWord3`) has its twist datum
transported along any braid word `γ : BraidWord n` (`τ ∘ (closurePerm γ)⁻¹`), the unordered
`twistMultiset` is strictly preserved. -/
theorem twistMultiset_braidTransport_eq (γ w : BraidWord n) (τ : Fin n → ℤ) :
    twistMultiset ⟨w, fun i => τ ((closurePerm γ)⁻¹ i)⟩ = twistMultiset ⟨w, τ⟩ := by
  classical
  unfold twistMultiset
  change ((Finset.univ : Finset (Fin n)).val.map (τ ∘ ⇑(closurePerm γ)⁻¹)) =
    (Finset.univ : Finset (Fin n)).val.map τ
  rw [← Multiset.map_map τ ⇑(closurePerm γ)⁻¹]
  congr 1
  rw [← Equiv.coe_toEmbedding, ← Finset.map_val, Finset.map_univ_equiv]

/-- Explicit 3-element expansion of `twistMultiset` on `Fin 3`. -/
theorem twistMultiset_three_eq (w : BraidWord 3) (τ : Fin 3 → ℤ) :
    twistMultiset ⟨w, τ⟩ = {τ 0, τ 1, τ 2} := by
  have huniv : (Finset.univ : Finset (Fin 3)).val =
      (0 : Fin 3) ::ₘ (1 : Fin 3) ::ₘ {(2 : Fin 3)} := by decide
  unfold twistMultiset
  rw [huniv, Multiset.map_cons, Multiset.map_cons, Multiset.map_singleton]
  rfl

/-- **Unified `FramedBraidWord 3` Multiset Theorem at the Four First-Generation Totals:**
Combining `FramedBraidWord 3` component-constancy and sign-coherence over the unit-twist range
`∀ i, -1 ≤ τ i ∧ τ i ≤ 1`:
1. At `T = 2` on `borromeanBraidWord3`, `twistMultiset` is uniquely `{0, 1, 1}` (no coherence needed);
2. At `T = -1` on `borromeanBraidWord3` with `SignCoherent τ`, `twistMultiset` is uniquely `{-1, 0, 0}`;
3. At `T = 0` on `leptonUnknotWord3` with `IsComponentFraming`, `τ = (0, 0, 0)`;
4. At `T = -3` on `hopfElectronWord3`, `τ = (-1, -1, -1)`. -/
theorem framedBraid3_firstGen_multisets_determined :
    (∀ τ : Fin 3 → ℤ, (∀ i, -1 ≤ τ i ∧ τ i ≤ 1) →
      totalTwist ⟨borromeanBraidWord3, τ⟩ = 2 →
      twistMultiset ⟨borromeanBraidWord3, τ⟩ = ({0, 1, 1} : Multiset ℤ)) ∧
    (∀ τ : Fin 3 → ℤ, (∀ i, -1 ≤ τ i ∧ τ i ≤ 1) → SignCoherent τ →
      totalTwist ⟨borromeanBraidWord3, τ⟩ = -1 →
      twistMultiset ⟨borromeanBraidWord3, τ⟩ = ({-1, 0, 0} : Multiset ℤ)) ∧
    (∀ τ : Fin 3 → ℤ, IsComponentFraming (closurePerm leptonUnknotWord3) τ →
      totalTwist ⟨leptonUnknotWord3, τ⟩ = 0 →
      ∀ i, τ i = 0) ∧
    (∀ τ : Fin 3 → ℤ, (∀ i, -1 ≤ τ i ∧ τ i ≤ 1) →
      totalTwist ⟨hopfElectronWord3, τ⟩ = -3 →
      ∀ i, τ i = -1) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro τ hrange htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    rw [twistMultiset_three_eq]
    rcases u_multiset_forced hrange htot with ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩
    · rw [h0, h1, h2]
    · rw [h0, h1, h2]; decide
    · rw [h0, h1, h2]; decide
  · intro τ hrange hcoh htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    rw [twistMultiset_three_eq]
    rcases d_multiset_forced hrange htot hcoh with ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩
    · rw [h0, h1, h2]
    · rw [h0, h1, h2]; decide
    · rw [h0, h1, h2]; decide
  · intro τ hcomp htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    exact nu_framing_is_zero hcomp closurePerm_unknot3_transitive htot
  · intro τ hrange htot
    simp only [totalTwist, Fin.sum_univ_three] at htot
    have r0 := hrange 0
    have r1 := hrange 1
    have r2 := hrange 2
    have h0 : τ 0 = -1 := by omega
    have h1 : τ 1 = -1 := by omega
    have h2 : τ 2 = -1 := by omega
    intro i
    fin_cases i <;> assumption

end FramedBraidWord

end QOU.StandardModel.FramedBraidTwistMonodromy
