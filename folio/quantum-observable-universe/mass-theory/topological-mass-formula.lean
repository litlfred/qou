import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith


/-!
# QOU.Torsion.ArchimedeanMassFormula — Topological mass formula (Archimedean)

In the archimedean realisation, the categorical mass decomposition
specialises to:

  m(K) = Vol(K) / ℏ_q²

where Vol(K) is the hyperbolic volume of S³ \ K and
ℏ_q = 1 - 1/q is the quantum Planck constant.

LaTeX label: `conj:topological-mass-formula`

## References

- [leitner2026] §4/topological-mass-formula
- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [thurston1978] https://doi.org/10.1007/978-1-4612-9903-6

**Ground ring**: this is the *archimedean* (post-fibre-functor)
realisation, so every quantity is a real number. The substrate ground
ring `R_q = ℤ[q, q⁻¹]` carries no ordering or division and cannot host
`ℏ_q = (q-1)/q`, `div_pos`, or the positivity statements below; the
specialisation `ι : R_q → ℝ, q ↦ q₀` is taken *before* these
statements, per AGENTS.md §7c (archimedean constructs ⇒ `ℝ`).
-/

namespace QOU.Torsion

/-- The quantum Planck constant ℏ_q = (q - 1)/q = 1 - 1/q. -/
noncomputable def quantumPlanck (q : ℝ) : ℝ := (q - 1) / q

/-- ℏ_q is positive for q > 1. -/
theorem quantumPlanck_pos (q : ℝ) (hq : 1 < q) : 0 < quantumPlanck q := by
  unfold quantumPlanck
  apply div_pos (by linarith) (by linarith)

/-- The archimedean mass formula: m(K) = Vol(K) / ℏ_q². -/
noncomputable def archimedeanMass (q : ℝ) (vol : ℝ) : ℝ :=
  vol / (quantumPlanck q) ^ 2

/-- **Archimedean Mass Formula, Step 3** (for `conj:topological-mass-formula`):

    Let (C, A, τ) be the C-quantum observable universe and let K be a
    hyperbolic knot. The descent involution induces the idempotent
    splitting End_C(A_{n+1}) = A^desc ⊕ A^trans. Under the archimedean
    fibre functor:
    - The descended trace evaluates to Hol_{∇_A} (the holonomy)
    - Each transient trace evaluates to Φ_q(z_i) (quantum dilogarithm)

    Summing: m(K) = Vol(K) + Vol(K)(1/ℏ_q² - 1) = Vol(K)/ℏ_q².

    This theorem proves only Step 3: given the two evaluations as the
    hypotheses `h_baseline` and `h_exceptional`, the sum is Vol(K)/ℏ_q².
    The conjecture rests on the categorical decomposition
    (`conj:topological-mass`, open) and on the two evaluations:
    1. Baseline holonomy → Vol(K) via Chern-Simons/volume correspondence
    2. Exceptional divisor contributions → Vol(K) · (1/ℏ_q² - 1)
    3. Total: m = Vol(K)/ℏ_q² -/
-- Ref: [leitner2026] §4/topological-mass-formula
-- Ref: [thurston1978] The Geometry and Topology of Three-Manifolds — see folio/schema/references.ts
theorem ArchimedeanMassFormula
    (q : ℝ) (hq : 1 < q)
    (vol : ℝ)
    (baseline : ℝ) (exceptional : ℝ)
    (h_baseline : baseline = vol)
    (h_exceptional : exceptional = vol * (1 / (quantumPlanck q) ^ 2 - 1))
    : baseline + exceptional = archimedeanMass q vol := by
  unfold archimedeanMass
  rw [h_baseline, h_exceptional]
  -- Vol + Vol · (1/ℏ² - 1) = Vol · (1 + 1/ℏ² - 1) = Vol/ℏ²
  -- Ref: [leitner2026] §4/topological-mass-formula
  have hℏ : (quantumPlanck q) ^ 2 ≠ 0 :=
    pow_ne_zero 2 (ne_of_gt (quantumPlanck_pos q hq))
  field_simp
  ring

/-- The archimedean mass is positive for hyperbolic knots (Vol > 0). -/
-- Ref: [leitner2026] §4/topological-mass-formula
theorem archimedeanMass_pos (q : ℝ) (hq : 1 < q)
    (vol : ℝ) (hvol : 0 < vol) :
    0 < archimedeanMass q vol := by
  unfold archimedeanMass
  exact div_pos hvol (pow_pos (quantumPlanck_pos q hq) 2)

end QOU.Torsion
