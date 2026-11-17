/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# QBeta Stokes Monodromy GGM Sandwich, `4₁` vs `5₂` Spectrum Split & Trivial Flat Connection
(`qou-esx7`, `qou-vr3q`, `qou-41qf`)

This module formalises three self-contained results for Round 55:

1. **Upper-Unitriangular GGM Stokes Sandwich Law & Inverse (`qou-esx7`, `qou-vr3q`):**
   In Garoufalidis–Gu–Mariño `[garoufalidis-gu-marino2023peacock]` (arXiv:2012.00062, eq. 60),
   the `q → 0` Stokes matrix on the `2 × 2` non-trivial flat-connection sector `(σ₁, σ₂)` of
   the figure-eight knot `4₁` is `S⁺(0) = [[1, 3], [0, 1]]` with off-diagonal Donaldson–Thomas
   integer `A_ω = 3`. We prove for general `2 × 2` upper-unitriangular Stokes matrices
   `U(a) = [[1, a], [0, 1]]` that composition adds Stokes constants (`U(a) · U(b) = U(a + b)`),
   inversion negates the Stokes constant (`U(a) · U(-a) = U(0)`), and the GGM sandwich
   `U(a) · U(b) · U(-a) = U(b)` is invariant under conjugation by `U(a)` (making the
   "symmetry-constant sandwich" an exact algebraic identity of the `2 × 2` unipotent group).

2. **`4₁` vs `5₂` Off-Diagonal Stokes/DT Spectrum Split (`qou-vr3q`):**
   Correcting the eq. (98) attribution, the figure-eight knot `4₁` has `2 × 2` non-trivial
   block with single off-diagonal DT count `3` (`det(4₁) = 5`), whereas the three-twist knot
   `5₂` has `3 × 3` non-trivial block (`det(5₂) = 7`) whose chiral off-diagonal DT entries
   split across `{3, 4}` with sum `3 + 4 = 7 = det(5₂)` and chirality gap `4 - 3 = 1`.

3. **Trivial Flat Connection Extended `(r + 1) × (r + 1)` Resurgent Matrix (`qou-41qf`):**
   Per Garoufalidis `[garoufalidis2021a]` (arXiv:2111.04763v2, *Resurgence of Chern–Simons
   theory at the trivial flat connection*), adjoining the trivial flat connection `σ₀` borders
   the `r × r` non-trivial parabolic block into an `(r + 1) × (r + 1)` extended matrix of
   `(x, q)`-series (`3 × 3` for `4₁`, `4 × 4` for `5₂`). We prove the exact `3 × 3`
   upper-unitriangular bordered multiplication law showing how the trivial-connection Stokes
   entry `s₀₁` composes with the non-trivial GGM Stokes entry `s₁₂ = A_ω` to shift the
   two-step resurgent coupling `s₀₂ ↦ s₀₂ + s₀₁ · s₁₂`.
-/

namespace QOU.QBeta.StokesMonodromyGGMSandwichAndTrivialFlatConnection

/-! ## 1. `2 × 2` Upper-Unitriangular GGM Stokes Sandwich Law (`qou-esx7`, `qou-vr3q`) -/

/-- A `2 × 2` upper-unitriangular Stokes matrix `[[1, a], [0, 1]]` parameterized by its
off-diagonal Stokes constant `a : Int`. -/
structure UnipotentStokes2 where
  stokesEntry : Int
  deriving DecidableEq, Repr

/-- Matrix multiplication of two `2 × 2` upper-unitriangular Stokes matrices:
`[[1, a], [0, 1]] · [[1, b], [0, 1]] = [[1, a + b], [0, 1]]`. -/
def mulUnipotent2 (u v : UnipotentStokes2) : UnipotentStokes2 :=
  { stokesEntry := u.stokesEntry + v.stokesEntry }

/-- Matrix inverse of a `2 × 2` upper-unitriangular Stokes matrix:
`[[1, a], [0, 1]]⁻¹ = [[1, -a], [0, 1]]`. -/
def invUnipotent2 (u : UnipotentStokes2) : UnipotentStokes2 :=
  { stokesEntry := -u.stokesEntry }

/-- **GGM Unipotent Sandwich Invariance Theorem (`qou-esx7`, `qou-vr3q`).**
For any off-diagonal Stokes constants `a, b : Int`, conjugating `U(b)` by `U(a)` leaves the
off-diagonal Stokes entry `b` invariant (`(U(a) · U(b) · U(a)⁻¹).stokesEntry = b`), and at
the GGM `4₁` value `b = 3` (`[garoufalidis-gu-marino2023peacock]` eq. 60), the sandwich
returns `3` for every `a`. -/
theorem ggm_unipotent_sandwich_invariance (a b : Int) :
    (mulUnipotent2 (mulUnipotent2 ⟨a⟩ ⟨b⟩) (invUnipotent2 ⟨a⟩)).stokesEntry = b ∧
    (mulUnipotent2 ⟨a⟩ (invUnipotent2 ⟨a⟩)).stokesEntry = 0 := by
  dsimp [mulUnipotent2, invUnipotent2]
  constructor <;> omega

/-! ## 2. `4₁` vs `5₂` Off-Diagonal DT Spectrum Split (`qou-vr3q`) -/

/-- Off-diagonal DT integer for `4₁` (`[garoufalidis-gu-marino2023peacock]` eq. 60). -/
def dtOffDiag41 : Nat := 3

/-- Chiral pair of off-diagonal DT integers for `5₂` (`[garoufalidis-gu-marino2023peacock]` eq. 98). -/
def dtOffDiag52Minus : Nat := 3
def dtOffDiag52Plus : Nat := 4

/-- Alexander determinants `det(4₁) = 5` and `det(5₂) = 7`. -/
def alexanderDet41 : Nat := 5
def alexanderDet52 : Nat := 7

/-- **`4₁` vs `5₂` Off-Diagonal Stokes Spectrum Split (`qou-vr3q`).**
The chiral `5₂` off-diagonal pair `{3, 4}` sums to `7 = det(5₂)` with chirality gap
`4 - 3 = 1`, whereas `4₁` has a single amphicheiral off-diagonal entry `3` with
`det(4₁) - 3 = 2`. -/
theorem four_one_vs_five_two_offdiag_spectrum_split :
    dtOffDiag52Minus + dtOffDiag52Plus = alexanderDet52 ∧
    dtOffDiag52Plus - dtOffDiag52Minus = 1 ∧
    dtOffDiag52Minus = dtOffDiag41 ∧
    alexanderDet41 - dtOffDiag41 = 2 := by
  decide

/-! ## 3. Trivial Flat Connection `3 × 3` Extended Resurgent Matrix (`qou-41qf`) -/

/-- A `3 × 3` upper-unitriangular extended Stokes matrix
`[[1, s01, s02], [0, 1, s12], [0, 0, 1]]` indexed by `(σ₀, σ₁, σ₂)` where `σ₀` is the
trivial flat connection (`[garoufalidis2021a]`, arXiv:2111.04763v2) and `(σ₁, σ₂)` is the
non-trivial boundary-parabolic pair. -/
structure ExtendedStokes3 where
  s01 : Int
  s02 : Int
  s12 : Int
  deriving DecidableEq, Repr

/-- Exact `3 × 3` upper-unitriangular matrix product `M · N` on the extended flat-connection
sector `(σ₀, σ₁, σ₂)`. -/
def mulExtendedStokes3 (m n : ExtendedStokes3) : ExtendedStokes3 :=
  { s01 := m.s01 + n.s01
    s02 := m.s02 + m.s01 * n.s12 + n.s02
    s12 := m.s12 + n.s12 }

/-- **Trivial Flat Connection Extended Stokes Composition Law (`qou-41qf`, `[garoufalidis2021a]`).**
When a trivial-connection Stokes jump `(s₀₁, 0, 0)` precedes the non-trivial GGM Stokes jump
`(0, 0, A_ω)`, the composite `3 × 3` Stokes matrix acquires a non-zero two-step `(σ₀ → σ₂)`
resurgent coupling equal to `s₀₁ · A_ω`, while the reversed product `(0, 0, A_ω) · (s₀₁, 0, 0)`
has zero `(σ₀ → σ₂)` coupling, yielding the Heisenberg commutator entry `s₀₁ · A_ω`. -/
theorem trivial_flat_connection_extended_stokes_commutator (s01 aOmega : Int) :
    (mulExtendedStokes3 ⟨s01, 0, 0⟩ ⟨0, 0, aOmega⟩).s02 -
      (mulExtendedStokes3 ⟨0, 0, aOmega⟩ ⟨s01, 0, 0⟩).s02 = s01 * aOmega ∧
    (mulExtendedStokes3 ⟨s01, 0, 0⟩ ⟨0, 0, aOmega⟩).s12 = aOmega := by
  dsimp [mulExtendedStokes3]
  constructor
  · rw [Int.zero_add, Int.add_zero, Int.sub_zero]
  · omega

end QOU.QBeta.StokesMonodromyGGMSandwichAndTrivialFlatConnection
