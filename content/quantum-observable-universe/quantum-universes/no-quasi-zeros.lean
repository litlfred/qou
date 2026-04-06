/-!
# QOU.NoQuasiZeros — Algebra without quasi-zeros

An element a in an R-algebra A is a quasi-zero if bac = 0 for all
b, c in A not both the identity.  We require R to have no quasi-zeros
so that leading-term arguments are well-defined.

LaTeX label: `def:no-quasi-zeros`

## References
- [leitnerpawloski2004] Leitner–Pawloski, Unital Gröbner bases
- [manuscript] §1/no-quasi-zeros
-/

import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Algebra.Basic

namespace QOU

universe u

/-- An element `a` of an `R`-algebra `A` is a **quasi-zero** if
    `b * a * c = 0` for all `b, c` in `A` that are not both `1`. -/
-- Ref: [manuscript] §1/no-quasi-zeros
def IsQuasiZero {R : Type u} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
    (a : A) : Prop :=
  ∀ b c : A, ¬(b = 1 ∧ c = 1) → b * a * c = 0

/-- An `R`-algebra `A` is an **algebra without quasi-zeros** if no
    element satisfies the quasi-zero condition. -/
-- Ref: [leitnerpawloski2004] https://doi.org/10.1016/j.jalgebra.2004.01.006
-- Ref: [manuscript] §1/no-quasi-zeros
def NoQuasiZeros (R : Type u) [CommRing R] (A : Type u) [Ring A] [Algebra R A] : Prop :=
  ∀ a : A, ¬IsQuasiZero a

end QOU
