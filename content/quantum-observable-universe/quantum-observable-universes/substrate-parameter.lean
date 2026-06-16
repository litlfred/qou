import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Tactic


/-!
# QOU.SubstrateParameter

The substrate parameter is the fibre coordinate q ∈ k× on the
one-parameter family of interpolations between the full differential d
and the vertical projection π_V ∘ d.  Categorically, it is the unique
scalar such that d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d acts as q⁻¹ d on
horizontal forms and as d on vertical forms.

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.

## Base-ring discipline (CLAUDE.md §7c)

The categorical substrate parameter lives over the *formal* ground ring
`R_q = LaurentPolynomial ℤ`, which is **not ordered** and is **not a
field**: archimedean predicates (`0 < q`, `q ≥ 1`, "not a root of
unity") and the inverse `q⁻¹` of an arbitrary element are **not
meaningful** there.  Those properties belong to the *archimedean
realisation* `q : M → ℝ`, on the far side of the substrate→archimedean
wall.  We therefore split:

* `SubstrateParameter M` — the **categorical** modulus field
  `field : M → R_q` (formal; no order, no inverse axioms);
* `ArchimedeanSubstrateField M` — the **archimedean** field
  `field : M → ℝ` carrying the classicality bound `q(p) ≥ 1`, on which
  positivity, invertibility and the Planck displacement `ℏ_q = 1 − q⁻¹`
  are genuine theorems.

The specialisation `ι : R_q → ℝ, q ↦ q₀` carries the categorical field
to the archimedean one at the substrate value `q₀ ≈ 1.1097`.
-/

open scoped Topology CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
noncomputable def q_param : R_q := LaurentPolynomial.T 1
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Substrate parameter** (categorical): the fibre coordinate `q ∈ k×`
    on the one-parameter family of operators interpolating between
    the full differential `d` and the vertical differential `π_V ∘ d`.

    When the quantum universe is fibred over a space `M`, the substrate
    parameter becomes a field `q : M → R_q`.  This is the **formal**
    modulus field over the (un-ordered, non-field) ground ring `R_q`;
    the archimedean properties (`q(p) > 0`, `q(p) ≥ 1`, not a root of
    unity) live on `ArchimedeanSubstrateField` below, after the
    substrate→archimedean wall (CLAUDE.md §7c).

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The categorical substrate field `q : M → R_q`.
      Records the local value of the `End(𝟙) ≅ R_q`-element at each
      point `p`. -/
  field : M → R_q

/-- **Archimedean substrate field**: the realisation of the substrate
    parameter as a genuine real field `q : M → ℝ` at and around the
    substrate value `q₀ ≈ 1.1097`, obtained by specialising the
    categorical `R_q`-field through `ι : R_q → ℝ, q ↦ q₀`.

    It carries the single archimedean axiom — the **classicality bound**
    `q(p) ≥ 1` — from which positivity, invertibility, and the
    non-negativity of the quantum Planck displacement are derived.

    * `q(p) = 1` is the classical limit (`ℏ_q = 0`);
    * `q(p) > 1` is the quantum regime (the physical substrate sits here,
      `q₀ ≈ 1.1097`). -/
structure ArchimedeanSubstrateField (M : Type*) where
  /-- The archimedean substrate field `q : M → ℝ`. -/
  field : M → ℝ
  /-- Classicality bound: `q(p) ≥ 1` at every point. -/
  field_ge_one : ∀ p, 1 ≤ field p

namespace ArchimedeanSubstrateField

variable {M : Type*} (qf : ArchimedeanSubstrateField M) (p : M)

/-- The substrate field is strictly positive (from `q(p) ≥ 1 > 0`). -/
theorem field_pos : 0 < qf.field p :=
  zero_lt_one.trans_le (qf.field_ge_one p)

/-- The interpolation coefficient `q(p)⁻¹` is well-defined: `q(p) ≠ 0`. -/
theorem field_ne_zero : qf.field p ≠ 0 :=
  (qf.field_pos p).ne'

/-- The quantum Planck constant `ℏ_q(p) = 1 − q(p)⁻¹` measures
    displacement along the Reeb fibre.  At `q = 1`, `ℏ_q = 0`;
    as `q → ∞`, `ℏ_q → 1`. -/
noncomputable def planck : ℝ := 1 - (qf.field p)⁻¹

/-- The Planck displacement is non-negative when `q(p) ≥ 1`. -/
theorem planck_nonneg : 0 ≤ qf.planck p := by
  unfold planck
  have h := qf.field_ge_one p
  linarith [inv_le_one_of_one_le₀ h]

/-- At `q(p) = 1` the Planck displacement vanishes (classicality). -/
theorem planck_classical (hq : qf.field p = 1) : qf.planck p = 0 := by
  unfold planck
  simp [hq]

/-- In the strict quantum regime `q(p) > 1`, the substrate value is not
    classical (`q(p) ≠ 1`); for real `q ≥ 1` this is exactly the
    "not a root of unity" condition ensuring semisimplicity. -/
theorem field_ne_one_of_one_lt (h : 1 < qf.field p) : qf.field p ≠ 1 :=
  ne_of_gt h

end ArchimedeanSubstrateField

end QOU
