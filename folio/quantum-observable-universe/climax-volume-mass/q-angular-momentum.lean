import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic


/-!
# QOU.Archimedean.QAngularMomentum — q-Angular momentum from SU_q(2) Casimir

The q-angular momentum is the q-Casimir eigenvalue `[j]_q [j+1]_q` of the
SU_q(2) representation carried by the particle knot. At `q = 1` this reduces
to the standard `j(j+1)`.

LaTeX label: `def:q-angular-momentum`

## References
- [leitner2026] §6/q-angular-momentum
- Kassel, "Quantum Groups" (1995)

**Ground ring (AGENTS.md §7c).** The Casimir is a product of two q-numbers
and nothing more, so it is stated over a generic `{R : Type*} [CommRing R]`
and the carrier `QAngularMomentum R` takes the q-number as *data*. Only the
specific real-exponent q-number `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)` needs `ℝ`,
because `q ^ n` at a real `n` is `Real.rpow`; that lives below the
substrate→archimedean wall as `qNumberReal` and is one instantiation of the
generic development, not its ground.

This file previously opened with `abbrev R_q := ℝ` and
`def q_param : R_q := 1.1097`, both inside `namespace QOU.Archimedean`,
where `R_q` canonically means `LaurentPolynomial ℤ` and `q_param` the
indeterminate `T 1` (`QOU/Archimedean/GroundRing.lean`,
`QOU/Archimedean/ParticleKnots.lean`). One name meant two different rings.
Both are gone: the generic layer carries no ground ring at all, and the
archimedean layer writes `ℝ` where it means `ℝ` (bean `qou-u87j`).
-/

namespace QOU.Archimedean

/-- **q-Angular momentum.** The q-deformed commutation relation
`[J₊, J₋] = [2J_z]_q` (not `2J_z`), carried by a particle knot.

The q-number is a *field* rather than a fixed function, which is what keeps
the structure generic: the Casimir below is `[j]_q · [j+1]_q` for whichever
bracket the instance supplies. `PartialOrder R` is required only to state
`m_bound`. -/
structure QAngularMomentum (R : Type*) [CommRing R] [PartialOrder R] where
  /-- The q-number `[·]_q` this instance is built over. -/
  qNumber : R → R → R
  /-- Substrate parameter `q`. -/
  q : R
  /-- Spin quantum number `j`. -/
  j : R
  /-- The magnetic quantum number `m`, ranging from `-j` to `+j`. -/
  m : R
  /-- The magnetic quantum number is bounded by `±j`. -/
  m_bound : -j ≤ m ∧ m ≤ j

namespace QAngularMomentum

variable {R : Type*} [CommRing R]

/-- The q-Casimir eigenvalue `J_q²(j) = [j]_q · [j+1]_q`, over any commutative
ring, for any q-number `qn`. -/
-- Ref: [leitner2026] §6/q-angular-momentum
def qCasimir (qn : R → R → R) (q j : R) : R := qn q j * qn q (j + 1)

/-- A q-number vanishing at `0` forces the Casimir to vanish at `j = 0`.

This is the ring-generic content of the classical limit `[n]_q → n` as
`q → 1`: it needs no ordering, no exponentiation and no archimedean
structure, only that the bracket kills `0`. -/
-- Ref: [leitner2026] §6/q-angular-momentum
-- Ref: [kassel1995] Kassel, "Quantum Groups" (1995)
theorem qCasimir_zero_of_qNumber_zero (qn : R → R → R) (q : R)
    (h : qn q 0 = 0) : qCasimir qn q 0 = 0 := by
  unfold qCasimir
  rw [h, zero_mul]

/-- The Casimir eigenvalue carried by an instance. -/
-- Ref: [leitner2026] §6/q-angular-momentum
def casimir [PartialOrder R] (A : QAngularMomentum R) : R :=
  qCasimir A.qNumber A.q A.j

/-! ### Archimedean specialisation

Below the substrate→archimedean wall: `q ^ n` at a real exponent is
`Real.rpow`, so these declarations are `ℝ` and say so. -/

/-- The q-number `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)` at **real** exponents.

**Deliberately not consolidated onto `QOU.QInteger.qIntBal`** (`qou-qint`
census). The index `n` is a real, not a `ℕ` or a `ℤ`, and that is
load-bearing: `qCasimir` is evaluated at `j` and `j + 1` for a *spin* `j`,
which takes half-integer values. The canonical bracket and its `ℤ`-indexed
sibling `qIntBalZ` are both discretely indexed, so neither can express this;
there is no equation to state, not merely none convenient. -/
-- Ref: [leitner2026] §6/q-angular-momentum
noncomputable def qNumberReal (q n : ℝ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : ℝ)))

/-- `[0]_q = 0`: the numerator is `q⁰ - q⁰`. -/
-- Ref: [leitner2026] §6/q-angular-momentum
theorem qNumberReal_zero (q : ℝ) : qNumberReal q 0 = 0 := by
  unfold qNumberReal
  simp

/-- For spin-½ at `q ≈ 1.1097`: `[1/2]_q · [3/2]_q ≈ 0.818` (classical 0.75).

The literal is a rounded illustration, not the substrate anchor — the live
pin is `q_at()` in `qou_substrate.constants`, currently
`1.1099785827513808`. -/
-- Ref: [leitner2026] §6/q-angular-momentum
noncomputable def spinHalfCasimirIllustration : ℝ :=
  qCasimir qNumberReal 1.1097 (1 / 2 : ℝ)

end QAngularMomentum

end QOU.Archimedean
