import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.TransferMatrixOperator

The transfer matrix T_{K₁,K₂}(q) is the universal operator encoding
particle interactions.  Its entries are polynomials in q, determined
by the knot types K₁, K₂ of the two interacting strands.

Every interaction (beta decay, photon absorption, pair creation) is
an instance of this operator.

LaTeX label: `def:transfer-matrix-operator`

## References
- [leitner2026] §6/transfer-matrix-operator
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Archimedean

/-- Crossing coefficients (c, d) determined by knot types. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
structure CrossingCoeffs where
  c : ℝ  -- σ coefficient
  d : ℝ  -- identity coefficient

/-- The transfer matrix from crossing coefficients.
    T(c,d) = ( c·(q-q⁻¹)+d,  c )
             (     c,         d ) -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
structure TransferMatrixOp where
  q : ℝ
  coeffs : CrossingCoeffs
  /-- (1,1) entry: c·(q-q⁻¹) + d -/
  m₁₁ : ℝ := coeffs.c * (q - 1/q) + coeffs.d
  /-- (1,2) entry: c -/
  m₁₂ : ℝ := coeffs.c
  /-- (2,1) entry: c -/
  m₂₁ : ℝ := coeffs.c
  /-- (2,2) entry: d -/
  m₂₂ : ℝ := coeffs.d

/-- The three nuclear crossing types. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def ppCoeffs : CrossingCoeffs := ⟨1, 0⟩

noncomputable def nnCoeffs (q : ℝ) : CrossingCoeffs :=
  let q_half := Real.sqrt q
  ⟨q^2, -q * (q_half - 1 / q_half)⟩

noncomputable def mixCoeffs (q : ℝ) : CrossingCoeffs :=
  let q_half := Real.sqrt q
  ⟨(1 + q^2) / 2, -q * (q_half - 1 / q_half) / 2⟩

/-- The photon-electron crossing has the same coefficients as pp.
    This is because the photon (empty knot) has J(q) = 1,
    contributing no deformation. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def photonElectronCoeffs : CrossingCoeffs := ppCoeffs

/-- Proof: photon-electron = proton-proton crossing coefficients. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
theorem photon_electron_eq_pp :
    photonElectronCoeffs = ppCoeffs := rfl

/-- The Hecke chain step: (aσ + b) × (cσ + d) → a'σ + b'
    via σ² = (q-q⁻¹)σ + 1. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def heckeStep (q a b c d : ℝ) : ℝ × ℝ :=
  (a * c * (q - 1/q) + a * d + b * c,  -- a'
   a * c + b * d)                        -- b'

/-- The interaction operator: Δ = T_after - T_before. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
structure InteractionOp where
  q : ℝ
  /-- Transfer matrix before interaction. -/
  before : CrossingCoeffs
  /-- Transfer matrix after interaction. -/
  after : CrossingCoeffs
  /-- Δc = c_after - c_before. -/
  delta_c : ℝ := after.c - before.c
  /-- Δd = d_after - d_before. -/
  delta_d : ℝ := after.d - before.d

/-- Beta decay operator (universal). -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def betaDecayOp (q : ℝ) : InteractionOp where
  q := q
  before := nnCoeffs q
  after := mixCoeffs q

/-- Photon absorption operator (R-I extension). -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def photonAbsorptionOp (q : ℝ) : InteractionOp where
  q := q
  before := ⟨0, 1⟩  -- identity (no crossing before)
  after := ppCoeffs   -- T_{γe} appended

/-- The eigenvalues of T_pp (= T_{γe}) determine hydrogen energy levels.
    λ± = ½[(q-q⁻¹) ± √((q-q⁻¹)² + 4)] -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
noncomputable def T_pp_eigenvalue_plus (q : ℝ) : ℝ :=
  let disc_sqrt := Real.sqrt ((q - 1/q)^2 + 4)
  ((q - 1/q) + disc_sqrt) / 2

noncomputable def T_pp_eigenvalue_minus (q : ℝ) : ℝ :=
  let disc_sqrt := Real.sqrt ((q - 1/q)^2 + 4)
  ((q - 1/q) - disc_sqrt) / 2

/-- The eigenvalues of T_pp are real and distinct for q > 0. -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
theorem T_pp_eigenvalues_real (q : ℝ) (hq : 0 < q) :
    0 < (q - 1/q)^2 + 4 := by
  positivity

/-- det(T_pp) = -1 (the product of eigenvalues). -/
-- Ref: [leitner2026] §6/transfer-matrix-operator
-- det = (q-q⁻¹)·0 - 1·1 = -1
theorem T_pp_det (q : ℝ) :
    let t : TransferMatrixOp := { q := q, coeffs := ppCoeffs }
    t.m₁₁ * t.m₂₂ - t.m₁₂ * t.m₂₁ = -1 := by
  intro t
  show t.m₁₁ * t.m₂₂ - t.m₁₂ * t.m₂₁ = -1
  simp only [t, ppCoeffs]
  ring

end QOU.Archimedean
