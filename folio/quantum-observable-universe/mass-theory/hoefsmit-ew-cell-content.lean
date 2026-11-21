/-
  Disjoint carrier strand pairs and the eight pure-pattern idempotents
  of the far-commuting triple (σ₁, σ₃, σ₅) in H₆(q).

  Companion: hoefsmit-ew-cell-content.md
  Path: folio/quantum-observable-universe/mass-theory/

  What this file PROVES (sorry-free, over a generic commutative ring R
  with q invertible and [2]_q = q + q⁻¹ invertible, §7c):

  * the strand pairs {1,2}, {3,4}, {5,6} of σ₁, σ₃, σ₅ are pairwise
    disjoint and cover {1,…,6}, and the indices 1, 3, 5 pairwise
    far-commute (`carrier_strand_pairs_disjoint`,
    `WZH_indices_far_commute`);
  * in any commutative R-algebra containing three Hecke generators
    (the commutative subalgebra H_2(q)^{⊗3} the far-commuting σ_1, σ_3,
    σ_5 generate), the eight pure-pattern projectors
    E(a,b,c) = e^a(σ_1) e^b(σ_3) e^c(σ_5) are idempotent, pairwise
    orthogonal, and sum to 1 (`patternsPairwiseOrthogonal_of_hecke`);
  * the six patterns other than (sym,sym,sym) and (alt,alt,alt) sum to
    1 − E(sss) − E(aaa) (`ewPhysicalProjectors_decompose_of_hecke`);
  * on its own strand pair, σ^{2k} is a word in B₂ whose closure
    permutation is the identity, so its closure has two components, and
    whose writhe is 2k (`components_sigmaOnePow_even`,
    `writhe_sigmaOnePow`). These are two invariants of the torus link
    T(2,2k).

  What it does NOT prove:
  * that the closure of σ^{2k} in B₂ IS the torus link T(2,2k). The
    tree has no link-isotopy type carrying an independent torus-link
    construction: `QOU.BraidKnot.closure2` assigns the label
    `torusLink2 |k|` to σ^k by definition, and
    `QOU.Archimedean.RossoJonesGeneral` takes T(r,s) to be the closure of
    (s₀⋯s_{r−2})^s. Against either, the identification is the definition,
    so it is not stated here as a theorem;
  * that the six patterns are the W±, Z±, H± carriers. That is a naming,
    recorded in `rem:hoefsmit-ew-cell-content-context`; its physical
    content is `conj:electroweak-higgs-torus-link-triplet`.

  The pattern multiplicities (4,2,1,3,3,1,2,4), 20 in total, are recorded
  from an enumeration of the 76 standard tableaux of size 6, not derived.

  The idempotent algebra is imported from
  `QOU.Conjectures.WeakSpectralCompleteness` (`joint_*` lemmas).

  Refs:
    [hoefsmit1974] Hoefsmit, "Representations of Hecke Algebras
       of Finite Groups with BN-pairs of Classical Type," UBC
       PhD thesis, 1974.
    computations/probes/ew_interface_knot_probe.py (tableau enumeration)
-/

import Mathlib.Algebra.Algebra.Basic
import QOU.Conjectures.WeakSpectralCompleteness
import QOU.Knot.BraidClosure

namespace QOU.BraidsAndKnots

open QOU.Conjectures

/-- Eigenvalue class of a Hecke generator on a Hoefsmit
    seminormal-basis vector: sym (eigenvalue +q), alt
    (eigenvalue -q⁻¹), or mixed (off-diagonal). -/
inductive HoefsmitClass where
  | sym
  | alt
  | mixed

/-- An eight-pattern label for the simultaneous Hoefsmit class
    of (σ_1, σ_3, σ_5) on a basis vector (only the pure cases —
    mixed combinations are tracked separately). -/
inductive PurePattern where
  | sss  -- (sym, sym, sym): unbroken vacuum, multiplicity 4
  | ass  -- (alt, sym, sym): W- excited, multiplicity 2
  | sas  -- (sym, alt, sym): Z- excited, multiplicity 1
  | ssa  -- (sym, sym, alt): H- excited, multiplicity 3
  | aas  -- (alt, alt, sym): W- + Z-, multiplicity 3
  | asa  -- (alt, sym, alt): W- + H-, multiplicity 1
  | saa  -- (sym, alt, alt): Z- + H-, multiplicity 2
  | aaa  -- (alt, alt, alt): fully broken, multiplicity 4
  deriving DecidableEq

/-- Tableau-multiplicity per pure pattern, RECORDED from an enumeration
    of the 76 standard tableaux of size 6 (the tableau and eigenvalue-class
    routines in `computations/probes/ew_interface_knot_probe.py`). Not
    derived here; the generating function is open. -/
def purePatternMultiplicity : PurePattern → ℕ
  | .sss => 4
  | .ass => 2
  | .sas => 1
  | .ssa => 3
  | .aas => 3
  | .asa => 1
  | .saa => 2
  | .aaa => 4

/-- The recorded multiplicities sum to the 20 pure tableaux. -/
theorem totalPureMultiplicity :
    purePatternMultiplicity .sss
    + purePatternMultiplicity .ass
    + purePatternMultiplicity .sas
    + purePatternMultiplicity .ssa
    + purePatternMultiplicity .aas
    + purePatternMultiplicity .asa
    + purePatternMultiplicity .saa
    + purePatternMultiplicity .aaa
    = 20 := by
  -- Ref: [leitner2026] computations/probes/ew_interface_knot_probe.py
  decide

/-- The six "physical" EW patterns (single-flip + double-flip),
    excluding the unbroken-vacuum and fully-broken patterns. -/
def isEWPhysical : PurePattern → Bool
  | .sss => false  -- unbroken vacuum (photon-like)
  | .aaa => false  -- fully broken
  | _ => true

/-- Coordinates of a pure pattern on the three carriers
    `(σ₁, σ₃, σ₅)`; `true` = sym (`+q`), `false` = alt (`-q⁻¹`). -/
def PurePattern.toTriple : PurePattern → Bool × Bool × Bool
  | .sss => (true, true, true)
  | .ass => (false, true, true)
  | .sas => (true, false, true)
  | .ssa => (true, true, false)
  | .aas => (false, false, true)
  | .asa => (false, true, false)
  | .saa => (true, false, false)
  | .aaa => (false, false, false)

/-- The eight pure patterns are exactly the eight sym/alt triples. -/
theorem PurePattern.toTriple_injective : Function.Injective PurePattern.toTriple := by
  intro a b h
  cases a <;> cases b <;> first | rfl | (simp [PurePattern.toTriple] at h)

theorem PurePattern.toTriple_surjective : Function.Surjective PurePattern.toTriple := by
  rintro ⟨a, b, c⟩
  cases a <;> cases b <;> cases c <;>
    first
    | exact ⟨.sss, rfl⟩ | exact ⟨.ass, rfl⟩ | exact ⟨.sas, rfl⟩
    | exact ⟨.ssa, rfl⟩ | exact ⟨.aas, rfl⟩ | exact ⟨.asa, rfl⟩
    | exact ⟨.saa, rfl⟩ | exact ⟨.aaa, rfl⟩

/-! ### Disjoint strand pairs -/

/--
  Far-commutativity at the index level: braid-generator indices `i`
  and `j` far-commute in `B_n` iff `i + 2 ≤ j ∨ j + 2 ≤ i`, which is
  the hypothesis of the braid relation `σ_i σ_j = σ_j σ_i`.
-/
-- Ref: [kassel1995] §VII (braid-group presentation)
def FarCommutes (i j : ℕ) : Prop := i + 2 ≤ j ∨ j + 2 ≤ i

/-- The strand pair on which generator `σ_i` acts. -/
def strandPair (i : ℕ) : Finset ℕ := {i, i + 1}

/-- Far-commuting generators act on disjoint strand pairs. -/
theorem strandPair_disjoint_of_farCommutes {i j : ℕ} (h : FarCommutes i j) :
    Disjoint (strandPair i) (strandPair j) := by
  unfold strandPair
  rw [Finset.disjoint_left]
  intro x hx hy
  simp only [Finset.mem_insert, Finset.mem_singleton] at hx hy
  unfold FarCommutes at h
  omega

/-- The W/Z/H carrier triple `(1, 3, 5)` in `B_6` is pairwise
    far-commuting. -/
theorem WZH_indices_far_commute :
    FarCommutes 1 3 ∧ FarCommutes 3 5 ∧ FarCommutes 1 5 := by
  refine ⟨?_, ?_, ?_⟩ <;> unfold FarCommutes <;> decide

/-- The carrier strand pairs `{1,2}`, `{3,4}`, `{5,6}` are pairwise
    disjoint and all lie in `{1,…,6}`, so `n = 6` strands suffice. -/
theorem carrier_strand_pairs_disjoint :
    Disjoint (strandPair 1) (strandPair 3) ∧
    Disjoint (strandPair 3) (strandPair 5) ∧
    Disjoint (strandPair 1) (strandPair 5) ∧
    strandPair 1 ∪ strandPair 3 ∪ strandPair 5 = Finset.Icc 1 6 := by
  obtain ⟨h13, h35, h15⟩ := WZH_indices_far_commute
  refine ⟨strandPair_disjoint_of_farCommutes h13,
    strandPair_disjoint_of_farCommutes h35,
    strandPair_disjoint_of_farCommutes h15, ?_⟩
  decide

/-! ### The carrier powers on their own strand pair -/

section Closure

open QOU.BraidKnot QOU.Knot.BraidClosure

/-- The positive generator `σ₁` of `B₂`. -/
def sigmaOne : BraidCrossing 2 := ⟨⟨0, by decide⟩, true⟩

/-- The braid word `σ₁^m` in `B₂`. -/
def sigmaOnePow (m : ℕ) : BraidWord 2 := List.replicate m sigmaOne

/-- An even power of `σ₁` induces the identity permutation of the two
    strand endpoints. -/
theorem closurePerm_sigmaOnePow_even (k : ℕ) :
    closurePerm (sigmaOnePow (2 * k)) = 1 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    have h : sigmaOnePow (2 * (k + 1)) = sigmaOne :: sigmaOne :: sigmaOnePow (2 * k) := by
      simp [sigmaOnePow, Nat.mul_succ, List.replicate_succ]
    rw [h, closurePerm_cons, closurePerm_cons, ih, mul_one]
    simp [crossingSwap, Equiv.swap_mul_self]

/-- The closure of `σ₁^{2k}` has two components. -/
theorem components_sigmaOnePow_even (k : ℕ) :
    components (sigmaOnePow (2 * k)) = 2 := by
  simp [components, closurePerm_sigmaOnePow_even]

/-- The writhe of `σ₁^m` is `m`. -/
theorem writhe_sigmaOnePow (m : ℕ) :
    BraidWord.writhe (sigmaOnePow m) = m := by
  induction m with
  | zero => rfl
  | succ m ih =>
    simp only [sigmaOnePow, List.replicate_succ, BraidWord.writhe_cons] at ih ⊢
    rw [ih]; simp [sigmaOne]; ring

/-- The carrier powers `σ⁴, σ⁶, σ⁸` on a single strand pair: two closure
    components and writhe `2k`, for `k = 2, 3, 4`. -/
theorem carrier_powers_closure_invariants :
    ∀ k ∈ ({2, 3, 4} : Finset ℕ),
      components (sigmaOnePow (2 * k)) = 2 ∧
        BraidWord.writhe (sigmaOnePow (2 * k)) = 2 * k := by
  intro k _
  exact ⟨components_sigmaOnePow_even k, by rw [writhe_sigmaOnePow]; push_cast; ring⟩

end Closure

/-! ### The eight pure-pattern projectors -/

section Projectors

variable {R : Type*} [CommRing R] {A : Type*} [CommRing A] [Algebra R A]

/-- The projector of a pure pattern: `E(a,b,c) = e^a(s₁) e^b(s₃) e^c(s₅)`. -/
def patternProjector (h : HeckeScalars R) (s₁ s₃ s₅ : A) (p : PurePattern) : A :=
  joint h s₁ s₃ s₅ p.toTriple

/-- The eight pure-pattern projectors are idempotent, pairwise orthogonal,
    and sum to `1`. -/
def PatternsPairwiseOrthogonal (h : HeckeScalars R) (s₁ s₃ s₅ : A) : Prop :=
  (∀ p, patternProjector h s₁ s₃ s₅ p * patternProjector h s₁ s₃ s₅ p =
      patternProjector h s₁ s₃ s₅ p) ∧
  (∀ p p', p ≠ p' →
      patternProjector h s₁ s₃ s₅ p * patternProjector h s₁ s₃ s₅ p' = 0) ∧
  (patternProjector h s₁ s₃ s₅ .sss + patternProjector h s₁ s₃ s₅ .ass
    + patternProjector h s₁ s₃ s₅ .sas + patternProjector h s₁ s₃ s₅ .ssa
    + patternProjector h s₁ s₃ s₅ .aas + patternProjector h s₁ s₃ s₅ .asa
    + patternProjector h s₁ s₃ s₅ .saa + patternProjector h s₁ s₃ s₅ .aaa = 1)

theorem eight_sum_eq_joint_sum (h : HeckeScalars R) (s₁ s₃ s₅ : A) :
    patternProjector h s₁ s₃ s₅ .sss + patternProjector h s₁ s₃ s₅ .ass
      + patternProjector h s₁ s₃ s₅ .sas + patternProjector h s₁ s₃ s₅ .ssa
      + patternProjector h s₁ s₃ s₅ .aas + patternProjector h s₁ s₃ s₅ .asa
      + patternProjector h s₁ s₃ s₅ .saa + patternProjector h s₁ s₃ s₅ .aaa
      = ∑ p : Bool × Bool × Bool, joint h s₁ s₃ s₅ p := by
  simp only [Fintype.sum_prod_type, Fintype.sum_bool, patternProjector,
    PurePattern.toTriple]
  ring

/-- **Pairwise orthogonality, proved.** For three Hecke generators in a
    commutative `R`-algebra (the subalgebra generated by the far-commuting
    `σ₁, σ₃, σ₅`), the eight pure-pattern projectors form a complete
    family of orthogonal idempotents. -/
theorem patternsPairwiseOrthogonal_of_hecke (h : HeckeScalars R) {s₁ s₃ s₅ : A}
    (h₁ : IsHeckeGen h s₁) (h₃ : IsHeckeGen h s₃) (h₅ : IsHeckeGen h s₅) :
    PatternsPairwiseOrthogonal h s₁ s₃ s₅ := by
  refine ⟨fun p => joint_idempotent h h₁ h₃ h₅ _, fun p p' hne => ?_, ?_⟩
  · exact joint_orthogonal h h₁ h₃ h₅
      (fun e => hne (PurePattern.toTriple_injective e))
  · rw [eight_sum_eq_joint_sum]; exact joint_sum_eq_one h s₁ s₃ s₅

/-- The six "physical" pattern projectors (all but `sss`, `aaa`) sum to
    `1 − E(sss) − E(aaa)`. The naming of these six as W±, Z±, H± is a
    labelling of constructions, not part of this statement. -/
def EWPhysicalProjectorsDecompose (h : HeckeScalars R) (s₁ s₃ s₅ : A) : Prop :=
  patternProjector h s₁ s₃ s₅ .ass + patternProjector h s₁ s₃ s₅ .sas
    + patternProjector h s₁ s₃ s₅ .ssa + patternProjector h s₁ s₃ s₅ .aas
    + patternProjector h s₁ s₃ s₅ .asa + patternProjector h s₁ s₃ s₅ .saa
    = 1 - patternProjector h s₁ s₃ s₅ .sss - patternProjector h s₁ s₃ s₅ .aaa

theorem ewPhysicalProjectors_decompose_of_hecke (h : HeckeScalars R)
    {s₁ s₃ s₅ : A} (h₁ : IsHeckeGen h s₁) (h₃ : IsHeckeGen h s₃)
    (h₅ : IsHeckeGen h s₅) :
    EWPhysicalProjectorsDecompose h s₁ s₃ s₅ := by
  have hsum := (patternsPairwiseOrthogonal_of_hecke h h₁ h₃ h₅).2.2
  unfold EWPhysicalProjectorsDecompose
  linear_combination hsum

/-- **Hoefsmit cell content of `(σ₁, σ₃, σ₅)` in `H₆(q)`.** Disjoint
    strand pairs covering `{1,…,6}`, a complete orthogonal family of eight
    pure-pattern idempotents, the six-pattern decomposition, and the closure
    invariants of `σ⁴, σ⁶, σ⁸` on one strand pair. -/
theorem hoefsmit_ew_cell_content (h : HeckeScalars R) {s₁ s₃ s₅ : A}
    (h₁ : IsHeckeGen h s₁) (h₃ : IsHeckeGen h s₃) (h₅ : IsHeckeGen h s₅) :
    (Disjoint (strandPair 1) (strandPair 3) ∧
      Disjoint (strandPair 3) (strandPair 5) ∧
      Disjoint (strandPair 1) (strandPair 5) ∧
      strandPair 1 ∪ strandPair 3 ∪ strandPair 5 = Finset.Icc 1 6) ∧
    PatternsPairwiseOrthogonal h s₁ s₃ s₅ ∧
    EWPhysicalProjectorsDecompose h s₁ s₃ s₅ ∧
    (∀ k ∈ ({2, 3, 4} : Finset ℕ),
      QOU.Knot.BraidClosure.components (sigmaOnePow (2 * k)) = 2 ∧
        QOU.BraidKnot.BraidWord.writhe (sigmaOnePow (2 * k)) = 2 * k) :=
  ⟨carrier_strand_pairs_disjoint, patternsPairwiseOrthogonal_of_hecke h h₁ h₃ h₅,
    ewPhysicalProjectors_decompose_of_hecke h h₁ h₃ h₅,
    carrier_powers_closure_invariants⟩

end Projectors

end QOU.BraidsAndKnots
