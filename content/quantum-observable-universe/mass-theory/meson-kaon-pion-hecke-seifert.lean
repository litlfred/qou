/-
  Kaon-to-pion mass ratio from Hecke characters and Seifert volumes.

  m_K/m_π = χ^{(2,1)}(σ₁⁵) × (V_S(T(2,5))/V_S(T(2,3)))²
          = (q⁵ − q⁻⁵) × (9/5)²

  Base ring (§7c): the file splits at the two very different inverses it uses.

  * The **Hecke character** is a Laurent identity in `q` — the only inverse it
    forms is `q⁻¹`, and `q` is the substrate parameter, invertible by fiat.
    It is therefore stated over `[CommRing R]` with `q : Rˣ` carried as a unit:
    no field, no `q ≠ 0` side condition.
  * The **Seifert–Euler** side genuinely needs a field. `e(T(2,n)) = 1 − 1/2 −
    1/n` divides by the *variable* index `n : ℕ`, which is not a unit of a
    general ring (and is literally `0` for `n = 0`); it is the field's totality
    convention that makes `seifertEuler` a total function of `n`. It keeps its
    explicit `2, 3, 5 ≠ 0` hypotheses — the invertibility the ratio identity
    genuinely needs, vacuous in any characteristic-0 specialisation.

  A relational restatement of the Euler number (`2·n·e = n − 2`) would be
  division-free, but it turns the definition into a predicate and needs `6`
  invertible to recover the ratio — a different modelling decision, not a
  de-specialisation of this one.

  The substrate evaluation (q at q₀) lives downstream.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass

section HeckeCharacter

variable {R : Type*} [CommRing R]

/-- Hecke character χ^{(2,1)}(σ₁ⁿ) = qⁿ + (-q⁻¹)ⁿ for the standard
    representation of H₃(q), with `q` carried as a unit so `q⁻¹` is the
    `Units` inverse rather than a field division. For odd n, this equals
    qⁿ - q⁻ⁿ. -/
def chi_21 (q : Rˣ) (n : ℕ) : R := (q : R) ^ n + (-((q⁻¹ : Rˣ) : R)) ^ n

/-- For odd n, χ^{(2,1)}(σ₁ⁿ) = qⁿ - q⁻ⁿ. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem chi_21_odd (q : Rˣ) (n : ℕ) (hn : Odd n) :
    chi_21 q n = (q : R) ^ n - ((q⁻¹ : Rˣ) : R) ^ n := by
  unfold chi_21
  rw [hn.neg_pow]
  ring

end HeckeCharacter

/-- The number of quark constituents of a meson, which is the squaring
    exponent appearing in `mesonMassRatio`.  A **named constant**, not a
    theorem.

    Replaced `theorem meson_squaring_exponent : (2 : ℕ) = 2 := rfl`
    (2026-08-21; vacuity ledger, `reflexive-tautology-ascribed-literal`).
    The docstring named an equality of two defined quantities — the
    squaring exponent and the constituent count — but the Lean proved
    `2 = 2`, dropping both sides; it held whatever either quantity was.
    Per Strict Lean Discipline §8 that is notation, not a theorem.

    The identification is now carried **structurally** instead of being
    asserted: `mesonMassRatio` raises `(9/5)` to this constant, so the
    exponent *is* the constituent count by construction rather than by a
    tautology claiming so. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §proof
def quarkConstituentCount : ℕ := 2

section SeifertEuler

variable {R : Type*} [Field R]

/-- Seifert Euler number of T(2,n): e = 1 - 1/2 - 1/n = (n-2)/(2n). -/
noncomputable def seifertEuler (n : ℕ) : R :=
  1 - (1 : R) / 2 - 1 / (n : R)

/-- Seifert volume ratio V_S(T(2,5)) / V_S(T(2,3)) = 9/5, over any field
    in which 2, 3, 5 are invertible. -/
-- Ref: [manuscript] prop:meson-kaon-pion-hecke-seifert §2
theorem seifert_ratio_T25_T23
    (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (h5 : (5 : R) ≠ 0) :
    (seifertEuler 5 : R) / seifertEuler 3 = 9 / 5 := by
  unfold seifertEuler
  have h35 : ((5 : ℕ) : R) ≠ 0 := by exact_mod_cast h5
  have h33 : ((3 : ℕ) : R) ≠ 0 := by exact_mod_cast h3
  push_cast
  field_simp
  ring

/-- The meson mass ratio formula:
    m_K/m_π = χ^{(2,1)}(σ₁⁵) × (9/5)². -/
noncomputable def mesonMassRatio (q : Rˣ) : R :=
  chi_21 q 5 * (9 / 5) ^ quarkConstituentCount

end SeifertEuler


end QOU.Mass
