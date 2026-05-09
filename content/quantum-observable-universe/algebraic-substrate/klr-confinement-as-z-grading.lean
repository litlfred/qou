import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# Confinement levels as KLR $\mathbb{Z}$-grading shifts

Theorem: the substrate's heuristic confinement-level function
corresponds (up to the constant 2) to the rigid $\mathbb{Z}$-grading
shift of KLR modules.  This rigidly types the confinement bound
that previously was a heuristic.

Ref: [khovanov-lauda-2009] https://doi.org/10.4171/rt/01

LaTeX label: `prop:confinement-as-z-grading`.

## Status

Per CLAUDE.md §3b-cond: the KLR $\mathbb{Z}$-grading is axiomatized
via a class hypothesis `KLRZGrading`.  The proposition's proof uses
the class fields directly.
-/

namespace QOU.AlgebraicSubstrate.KLRConfinementGrading

universe u

/-- **§3b-cond conditional-class hypothesis.**  Axiomatizes the KLR
$\mathbb{Z}$-grading and the relation to the substrate's confinement
function.

Ref: [khovanov-lauda-2009] §2.
-/
class KLRZGrading (n : ℕ) where
  /-- The categorified module category type. -/
  Carrier : Type u
  /-- Grading shift of an indecomposable graded projective KLR module. -/
  grading_shift : Carrier → ℤ
  /-- The substrate confinement-level function (heuristic). -/
  confinement_level : Carrier → ℕ
  /-- The CENTRAL CLAIM: the confinement level is exactly half the
      KLR grading shift (up to the constant 2 from `deg σ_i = 2`).
      In any concrete instance this is verified by tracing through
      Khovanov-Lauda's grading prescription on the relevant module. -/
  confinement_eq_half_grading :
      ∀ (M : Carrier),
        (2 : ℤ) * (confinement_level M : ℤ) = grading_shift M

/-- **Confinement = ℤ-grading bound.**

    The substrate's confinement-level bound `confinement_level M ≤ ℓ`
    is equivalent (modulo factor 2) to the KLR ℤ-grading bound
    `grading_shift M ≤ 2ℓ`.  This rigidly types the confinement bound.

    Ref: [manuscript] `prop:confinement-as-z-grading`. -/
theorem confinement_eq_grading_bound
    (n : ℕ) [klr : KLRZGrading.{u} n]
    (M : klr.Carrier) (ℓ : ℕ) :
    klr.confinement_level M ≤ ℓ ↔ klr.grading_shift M ≤ (2 * ℓ : ℤ) := by
  constructor
  · intro h
    rw [← klr.confinement_eq_half_grading]
    have : (klr.confinement_level M : ℤ) ≤ (ℓ : ℤ) := by exact_mod_cast h
    linarith
  · intro h
    rw [← klr.confinement_eq_half_grading] at h
    have : (klr.confinement_level M : ℤ) ≤ (ℓ : ℤ) := by linarith
    exact_mod_cast this

/-- **Geometric disallowance: traversal cannot exceed the grading bound.**

    If a crystal-operator step would push the grading above the bound,
    the resulting module lies outside the allowed sub-category.  The
    engine refuses such a step.  Captured here as a definitional
    statement on the class fields.  -/
theorem disallowed_above_bound
    (n : ℕ) [klr : KLRZGrading.{u} n]
    (M : klr.Carrier) (ℓ : ℕ)
    (h : klr.grading_shift M > (2 * ℓ : ℤ)) :
    ¬ (klr.confinement_level M ≤ ℓ) := by
  intro h_conf
  rw [confinement_eq_grading_bound] at h_conf
  linarith

/-- A trivial-True instance demonstrating the §3b-cond pattern. -/
def trivialKLRZGradingInstance (n : ℕ) : KLRZGrading.{0} n where
  Carrier := Unit
  grading_shift := fun _ => 0
  confinement_level := fun _ => 0
  confinement_eq_half_grading := fun _ => by ring

end QOU.AlgebraicSubstrate.KLRConfinementGrading
