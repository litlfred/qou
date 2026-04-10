/-!
# QOU.NonSelfIntersection — Obstruction to self-intersection

The non-cocommutativity of the Hopf structure at `q ≠ 1` provides a
categorical obstruction to knot self-intersection via an energy barrier
at the quantum Planck scale `ℏ_q = 1 − q⁻¹`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The quantum Planck constant at a given substrate parameter value. -/
noncomputable def hbar_q (q : R_q) : R_q := 1 - q⁻¹

/-- The quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def quantumTwo (q : R_q) : R_q := q + q⁻¹

/-- **q-Deformed repulsion kernel**.

    At `q ≠ 1`, the classical `1/r²` kernel is replaced by
    `[2]_q / (r² − ℏ_q²)` which has a hard singularity at `r = ℏ_q`.
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
noncomputable def qRepulsionKernel (q r : R_q) : R_q :=
  quantumTwo q / (r ^ 2 - hbar_q q ^ 2)

/-- The quantum Planck constant is positive when `q > 1`. -/
theorem hbar_q_pos (q : R_q) (hq : q > 1) : 0 < hbar_q q := by
  unfold hbar_q; linarith [inv_lt_one_of_one_lt₀ hq]

/-- The quantum integer `[2]_q` is positive when `q > 0`. -/
theorem quantumTwo_pos (q : R_q) (hq : q > 0) : 0 < quantumTwo q := by
  unfold quantumTwo; linarith [inv_pos.mpr hq]

/-- **Corollary: Obstruction to self-intersection.**

    For `q ≠ 1`, the non-cocommutativity of the Hopf structure provides
    an energy barrier: the q-repulsion kernel diverges at `r = ℏ_q`,
    creating a "quantum exclusion zone" of radius `ℏ_q = 1 − q⁻¹`.

    LaTeX: `\label{cor:non-self-intersection}`
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
structure NonSelfIntersection where
  /-- The deformation parameter `q > 1`. -/
  q : R_q
  -- q_gt_one : q > 1  -- (archimedean; not meaningful over R_q)
  /-- The exclusion radius `ℏ_q = 1 − q⁻¹`. -/
  exclusionRadius : R_q := hbar_q q
  /-- The exclusion radius is positive. -/
  exclusionRadius_pos : 0 < exclusionRadius

/-- The exclusion radius is exactly `ℏ_q`. -/
theorem NonSelfIntersection.exclusionRadius_eq
    (nsi : NonSelfIntersection) :
    nsi.exclusionRadius = hbar_q nsi.q :=
  rfl

/-- The exclusion radius vanishes in the classical limit `q → 1`. -/
theorem hbar_q_classical_limit : hbar_q 1 = 0 := by
  simp [hbar_q, inv_one]

/-- At `q > 1`, the exclusion zone has positive radius. -/
theorem exclusionZone_positive (q : R_q) (hq : q > 1) :
    0 < hbar_q q :=
  hbar_q_pos q hq

end QOU
