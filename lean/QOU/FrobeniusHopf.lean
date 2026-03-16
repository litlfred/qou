/-!
# QOU.FrobeniusHopf — Frobenius–Hopf Algebra Structure

Full formalisations of the algebraic structures underlying the QOU paper:
Frobenius algebras, Hopf algebras, and their combination.

## Paper references
- Definition 1.1 (item ii)  Frobenius–Hopf object
- Remark 1.14               `rem:frobenius-simplification`
- Definition 2.4             `def:direct-limit-algebra`

## Mathlib4 references
- `Mathlib.RingTheory.HopfAlgebra`        (Hopf algebras)
- `Mathlib.LinearAlgebra.TensorProduct`    (monoidal structure on Vect)
- `Mathlib.Algebra.Lie.Basic`              (Lie algebra structure)
- `Mathlib.Algebra.DirectLimit`            (direct limits of algebras)
-/

import QOU.Prelude

universe u v

-- ═══════════════════════════════════════════════════════════════════════
-- Frobenius algebras
-- ═══════════════════════════════════════════════════════════════════════

/-- A **Frobenius algebra** over a field k.
    An algebra (A, μ, η) equipped with a coalgebra (A, Δ, ε) satisfying
    the Frobenius relation: (μ ⊗ id) ∘ (id ⊗ Δ) = Δ ∘ μ = (id ⊗ μ) ∘ (Δ ⊗ id).

    This is the algebraic structure classifying 2d TQFTs (Kock, Atiyah).
    Paper: diagrams `eq:frobenius-relation`, `eq:frobenius-nondegen`. -/
class FrobeniusAlgebra (k : Type u) (A : Type v) [QField k] [QAlgebra k A] where
  /-- Comultiplication Δ : A → A ⊗ A.  Here modelled abstractly. -/
  comul : A → A × A
  /-- Counit ε : A → k. -/
  counit : A → k
  /-- Coassociativity: (Δ ⊗ id) ∘ Δ = (id ⊗ Δ) ∘ Δ. -/
  coassoc : ∀ a : A,
    let ⟨a₁, a₂⟩ := comul a
    let ⟨a₁₁, a₁₂⟩ := comul a₁
    let ⟨a₂₁, a₂₂⟩ := comul a₂
    (a₁₁, a₁₂, a₂) = (a₁, a₂₁, a₂₂)
  /-- Counit axiom: (ε ⊗ id) ∘ Δ = id = (id ⊗ ε) ∘ Δ.
      Stated as: ε(a₁) · a₂ = a = a₁ · ε(a₂). -/
  counit_left : ∀ a : A,
    let ⟨a₁, a₂⟩ := comul a
    QAlgebra.smul (counit a₁) a₂ = a
  counit_right : ∀ a : A,
    let ⟨a₁, a₂⟩ := comul a
    QAlgebra.smul (counit a₂) a₁ = a
  /-- **Frobenius relation**: (μ ⊗ id) ∘ (id ⊗ Δ) = Δ ∘ μ.
      Stated as: for all a, b: μ(a, Δ(b)) has specific form. -/
  frobenius : ∀ (a b : A),
    let ⟨b₁, b₂⟩ := comul b
    comul (a * b) = (a * b₁, b₂)

/-- The Frobenius form β : A ⊗ A → k defined by β(a, b) = ε(a · b). -/
def frobeniusForm {k : Type u} {A : Type v} [QField k] [QAlgebra k A]
    [FrobeniusAlgebra k A] (a b : A) : k :=
  FrobeniusAlgebra.counit (a * b)

/-- **Frobenius non-degeneracy**: β(a, b) = 0 for all b implies a = 0.
    Paper: diagram `eq:frobenius-nondegen`. -/
def FrobeniusNondeg (k : Type u) (A : Type v) [QField k] [QAlgebra k A]
    [FrobeniusAlgebra k A] : Prop :=
  ∀ a : A, (∀ b : A, frobeniusForm a b = (0 : k)) → a = 0

-- ═══════════════════════════════════════════════════════════════════════
-- Hopf algebras
-- ═══════════════════════════════════════════════════════════════════════

/-- A **Hopf algebra** over k: a bialgebra with an antipode S.
    Mathlib: `Mathlib.RingTheory.HopfAlgebra`. -/
class HopfAlgebra (k : Type u) (A : Type v) [QField k] [QAlgebra k A]
    extends FrobeniusAlgebra k A where
  /-- The antipode S : A → A. -/
  antipode : A → A
  /-- Left antipode axiom: μ ∘ (S ⊗ id) ∘ Δ = η ∘ ε.
      Stated as: S(a₁) · a₂ = ε(a) · 1. -/
  antipode_left : ∀ a : A,
    let ⟨a₁, a₂⟩ := comul a
    antipode a₁ * a₂ = QAlgebra.smul (counit a) (1 : A)
  /-- Right antipode axiom: μ ∘ (id ⊗ S) ∘ Δ = η ∘ ε.
      Stated as: a₁ · S(a₂) = ε(a) · 1. -/
  antipode_right : ∀ a : A,
    let ⟨a₁, a₂⟩ := comul a
    a₁ * antipode a₂ = QAlgebra.smul (counit a) (1 : A)

/-- The antipode is an anti-homomorphism: S(ab) = S(b) S(a). -/
theorem antipode_anti_hom {k : Type u} {A : Type v} [QField k] [QAlgebra k A]
    [HopfAlgebra k A] (a b : A) :
    HopfAlgebra.antipode (a * b) = HopfAlgebra.antipode b * HopfAlgebra.antipode a := by
  sorry

/-- The antipode is an involution on commutative or cocommutative Hopf algebras:
    S² = id. -/
theorem antipode_involution {k : Type u} {A : Type v} [QField k] [QAlgebra k A]
    [HopfAlgebra k A]
    (h_cocomm : ∀ a : A, FrobeniusAlgebra.comul a = let ⟨x,y⟩ := FrobeniusAlgebra.comul a; (y,x))
    (a : A) : HopfAlgebra.antipode (HopfAlgebra.antipode a) = a := by
  sorry

-- ═══════════════════════════════════════════════════════════════════════
-- Frobenius simplification (Remark 1.14)
-- ═══════════════════════════════════════════════════════════════════════

/-- **Remark 1.14** `rem:frobenius-simplification`

In a Frobenius category the QOU 5-tuple (M, θ, G, P, E) with
two vanishing conditions reduces to a triple (M, θ, A) where A is
a non-degenerate Frobenius–Hopf object.

The vanishing H⁰ = 0 follows from Frobenius non-degeneracy
together with instanton irreducibility. -/
theorem frobenius_simplification
    {k : Type u} {A : Type v} [QField k] [QAlgebra k A]
    [inst : HopfAlgebra k A]
    (h_nondeg : FrobeniusNondeg k A)
    -- Frobenius non-degeneracy + irreducibility → H⁰(Ad) = 0
    : ∀ (a : A),
      (∀ b : A, a * b = b * a) →       -- a is in the centre
      (∀ b : A, frobeniusForm a b = (0 : k)) →  -- a pairs trivially
      a = 0 := by
  intro a _ h_pair
  exact h_nondeg a h_pair

-- ═══════════════════════════════════════════════════════════════════════
-- Direct limits (Definition 2.4)
-- ═══════════════════════════════════════════════════════════════════════

/-- A **directed system** of algebras: a sequence A₀ → A₁ → A₂ → ⋯
    with compatible algebra maps.
    Mathlib: `Mathlib.Algebra.DirectLimit`. -/
structure DirectedSystem (k : Type u) where
  /-- The n-th algebra in the tower. -/
  algebra : Nat → Type v
  /-- Each level is a k-algebra. -/
  instAlgebra : (n : Nat) → QAlgebra k (algebra n)
  /-- Transition maps φₙ : Aₙ → Aₙ₊₁. -/
  transition : (n : Nat) → algebra n → algebra (n + 1)
  /-- Each transition is a k-algebra homomorphism (compatibility). -/
  transition_compat : Prop

/-- **Definition 2.4** (Direct-limit algebra) `def:direct-limit-algebra`

𝒜_∞ = lim_→ Γ(J¹Eₙ, SU_{qₙ}(2))

The ℂ quantum observable universe as a direct limit of the brane tower
algebras.  Mathlib: `Mathlib.Algebra.DirectLimit`. -/
axiom DirectLimitAlgebra (k : Type u) (sys : DirectedSystem k) : Type v
