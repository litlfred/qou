/-
  Typed Garside element of the nuclear braid.

  The typed Garside staircase builds all C(A,2) pairwise crossings
  with typed coefficients d(p,p)=0, d(n,n)=-h, d(p,n)=-h/2.
  After Hecke reduction, this gives the normal form of the nuclear
  braid in H_A(q).

  Ref: [manuscript] §6.3c, Definition def:typed-garside-element
-/

import Mathlib.GroupTheory.PresentedGroup
import Mathlib.RingTheory.HeckeAlgebra

namespace QOU.Archimedean

/-- Nucleon type: proton or neutron. -/
inductive NucleonType where
  | proton : NucleonType
  | neutron : NucleonType
  deriving DecidableEq, Repr

/-- Typed crossing coefficient d(f_i, f_j) for the Hecke algebra.
    pp → 0, nn → -h, pn/np → -h/2 where h = q - q⁻¹. -/
noncomputable def typedCrossingCoeff (q : ℝ) (f₁ f₂ : NucleonType) : ℝ :=
  let h := q - q⁻¹
  match f₁, f₂ with
  | .proton, .proton => 0
  | .neutron, .neutron => -h
  | _, _ => -h / 2

/-- A nuclear ordering is a list of nucleon types. -/
abbrev NuclearOrdering := List NucleonType

/-- Number of protons in an ordering. -/
def protonCount (ord : NuclearOrdering) : ℕ :=
  ord.filter (· == .proton) |>.length

/-- Number of neutrons in an ordering. -/
def neutronCount (ord : NuclearOrdering) : ℕ :=
  ord.filter (· == .neutron) |>.length

/-- The total number of pairwise crossings in the Garside staircase
    for A nucleons is C(A, 2) = A(A-1)/2.

    The hypothesis `_hA : 2 ≤ A` is preserved (with leading-
    underscore) for documentation consistency with the minimum-
    arity assumption in `def:typed-garside-element`, even though
    `Nat.choose_two_right` holds for all `A : ℕ`. -/
theorem garside_crossing_count (A : ℕ) (_hA : 2 ≤ A) :
    A * (A - 1) / 2 = Nat.choose A 2 := by
  -- Ref: [manuscript] Definition def:typed-garside-element
  exact (Nat.choose_two_right A).symm

/-- The typed Garside element has the standard Garside element Δ_A
    as its leading term (highest degree-lex word). -/
def typed_garside_leading_term
    (ord : NuclearOrdering) (hlen : 2 ≤ ord.length) :
    True := by  -- placeholder for the statement about leading term
  -- Ref: [manuscript] Definition def:typed-garside-element
  -- The leading term of the typed Garside element is Δ_A,
  -- independent of the typing (the d-shifts only affect lower-order terms).
  trivial

/-- For the pure proton ordering [p, p, ..., p], all crossings are pp type
    with d = 0, so the typed Garside element equals the standard Garside
    element Δ_A. -/
def pure_proton_garside_is_standard
    (A : ℕ) (hA : 2 ≤ A) :
    True := by  -- placeholder; conclusion is the literal `True`,
                 -- pending substantive Garside infrastructure.
  -- Ref: [manuscript] Definition def:typed-garside-element
  trivial

end QOU.Archimedean
