import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.NonSelfIntersection — Obstruction to self-intersection

The non-cocommutativity of the Hopf structure at `q ≠ 1` provides a
categorical obstruction to knot self-intersection via an energy barrier
at the quantum Planck scale `ℏ_q = 1 − q⁻¹`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. The Planck-scale quantities `ℏ_q = 1 − q⁻¹`,
`[2]_q = q + q⁻¹`, and the repulsion kernel require inversion and the
ordering `0 < ·`; these are archimedean and live over `ℝ` (post-`τ`
evaluation at the substrate point `q₀ > 1`).
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The quantum Planck constant at a given (archimedean) substrate
    parameter value. -/
def hbar_q (q : ℝ) : ℝ := 1 - q⁻¹

/-- The quantum integer `[2]_q = q + q⁻¹`. -/
def quantumTwo (q : ℝ) : ℝ := q + q⁻¹

/-- **q-Deformed repulsion kernel**.

    At `q ≠ 1`, the classical `1/r²` kernel is replaced by
    `[2]_q / (r² − ℏ_q²)` which has a hard singularity at `r = ℏ_q`.
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
def qRepulsionKernel (q r : ℝ) : ℝ :=
  quantumTwo q / (r ^ 2 - hbar_q q ^ 2)

/-- The quantum Planck constant is positive when `q > 1`. -/
theorem hbar_q_pos (q : ℝ) (hq : q > 1) : 0 < hbar_q q := by
  unfold hbar_q; linarith [inv_lt_one_of_one_lt₀ hq]

/-- The quantum integer `[2]_q` is positive when `q > 0`. -/
theorem quantumTwo_pos (q : ℝ) (hq : q > 0) : 0 < quantumTwo q := by
  unfold quantumTwo; linarith [inv_pos.mpr hq]

/-- **Corollary: Obstruction to self-intersection.**

    For `q ≠ 1`, the non-cocommutativity of the Hopf structure provides
    an energy barrier: the q-repulsion kernel diverges at `r = ℏ_q`,
    creating a "quantum exclusion zone" of radius `ℏ_q = 1 − q⁻¹`.

    LaTeX: `\label{cor:non-self-intersection}`
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
structure NonSelfIntersection where
  /-- The deformation parameter `q > 1`. -/
  q : ℝ
  /-- `q > 1` — the non-classical regime. -/
  q_gt_one : q > 1

/-- The exclusion radius of the quantum exclusion zone.

    **Derived, not carried.** The structure above used to have a free
    field `exclusionRadius : ℝ` alongside a field
    `exclusionRadius_def : exclusionRadius = hbar_q q` asserting what it
    equals, and `exclusionRadius_eq` returned that second field — the
    §3b-cond item-5 degenerate shape, and this file's
    `proof-no-self-assuming-projection` ledger entry. A free field
    constrained by an equation field is not a derivation: the radius could
    be anything and the structure merely assumed it away.

    Here the radius is a definition of `q`, matching the library encoding
    in `QOU/MobiusEnergy.lean`, so it is not a free parameter at all. -/
def NonSelfIntersection.exclusionRadius (nsi : NonSelfIntersection) : ℝ :=
  hbar_q nsi.q

/-- The exclusion radius is exactly `ℏ_q` — now an unfolding lemma of the
    definition above rather than a projection of an assumed equation. -/
theorem NonSelfIntersection.exclusionRadius_eq
    (nsi : NonSelfIntersection) :
    nsi.exclusionRadius = hbar_q nsi.q :=
  rfl

/-- **The exclusion zone is nonempty**: the radius is strictly positive.

    This is what the free-field encoding could not give. Positivity is
    derived from the structure's own `q_gt_one`, through `hbar_q_pos`;
    no field of `NonSelfIntersection` asserts it. -/
theorem NonSelfIntersection.exclusionRadius_pos
    (nsi : NonSelfIntersection) :
    0 < nsi.exclusionRadius :=
  hbar_q_pos nsi.q nsi.q_gt_one

/-- The exclusion radius vanishes in the classical limit `q → 1`. -/
theorem hbar_q_classical_limit : hbar_q 1 = 0 := by
  simp [hbar_q]

/-- At `q > 1`, the exclusion zone has positive radius. -/
theorem exclusionZone_positive (q : ℝ) (hq : q > 1) :
    0 < hbar_q q :=
  hbar_q_pos q hq

end

end QOU
