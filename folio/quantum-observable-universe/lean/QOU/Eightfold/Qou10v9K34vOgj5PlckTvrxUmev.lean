/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization for Round 108 beans:
- `qou-k34v`: Tangent pairing variation requires prepotential associativity (WDVV residual)
  beyond a single-space bilinear pairing.
- `qou-ogj5`: Spectral prefactor `alpha = 8 * m_e * G` glyph collision between the
  hyperbolic volume constant and the unitless gravitational constant, plus circularity
  of post-hoc ratio definition.
- `qou-plck`: Symbolic q-form identity `G_q * (hbar_q / c_q)^2 = 1` over cleared
  denominators and separation of the three distinct q-length scales.
- `qou-tvrx`: Projective polarization dictionary `[phi1 : lambda * phi0]` leaves the
  complex phase parameter `lambda` unfixed between linear and circular real states.
- `qou-umev`: Unit-determinant 2x2 trace discriminant `t^2 - 4`, refutation of the
  `t = -2` claim for `2 - 3*h^4 - h^6`, and positive discriminant `(q^2 - q^{-2})^2 > 0`
  for the even-length square word.
-/

namespace QOU.Eightfold.Qou10v9K34vOgj5PlckTvrxUmev

/-! ### 1. `qou-k34v`: Tangent Pairing Prepotential Associativity Residual -/

/-- Third-derivative tensor data `(a, b, d)` and diagonal inverse metric `(eta1, eta2)`
for a two-coordinate tangent algebra family. -/
structure TangentPrepotentialDatum where
  eta1 : Int
  eta2 : Int
  a : Int
  b : Int
  d : Int
  deriving DecidableEq, Repr

/-- Associativity commutator residual `(c_{111} eta2 c_{122} + c_{112} eta1 c_{112})
- (c_{112} eta2 c_{112} + c_{122} eta1 c_{112})` for a two-coordinate prepotential. -/
def prepotentialAssociativityResidual (P : TangentPrepotentialDatum) : Int :=
  (P.a * P.eta2 * P.d + P.b * P.eta1 * P.b) - (P.b * P.eta2 * P.b + P.d * P.eta1 * P.b)

/-- Factored form of the prepotential associativity residual:
`eta2 * (a * d - b^2) + eta1 * b * (b - d)`. -/
def prepotentialFactoredResidual (P : TangentPrepotentialDatum) : Int :=
  P.eta2 * (P.a * P.d - P.b * P.b) + P.eta1 * P.b * (P.b - P.d)

/-- Algebraic equivalence between the expanded commutator residual and its factored form
at unit diagonal inverse metric `eta1 = 1, eta2 = 1` with `b = d = 1`. -/
theorem prepotential_residual_unit_slice (a : Int) :
    prepotentialAssociativityResidual ⟨1, 1, a, 1, 1⟩ = a - 1 ∧
    prepotentialFactoredResidual ⟨1, 1, a, 1, 1⟩ = a - 1 := by
  dsimp [prepotentialAssociativityResidual, prepotentialFactoredResidual]
  omega

/-- A constant single-fibre pairing (`a = 1, b = 1, d = 1`) has zero associativity residual,
whereas varying `a = 2` while keeping the same metric `eta1 = eta2 = 1` produces a nonzero
associativity obstruction (`residual = 1`). -/
theorem prepotential_variation_obstruction_witness :
    prepotentialAssociativityResidual ⟨1, 1, 1, 1, 1⟩ = 0 ∧
    prepotentialAssociativityResidual ⟨1, 1, 2, 1, 1⟩ = 1 ∧
    prepotentialAssociativityResidual ⟨1, 1, 1, 1, 1⟩ ≠
      prepotentialAssociativityResidual ⟨1, 1, 2, 1, 1⟩ := by
  decide

/-! ### 2. `qou-ogj5`: Spectral Prefactor Glyph Collision (`8 * m_e * G`) -/

/-- Scaled spectral prefactor `8 * m_e * G` in integer micro-units. -/
def spectralPrefactorScaled (meScaled gScaled : Int) : Int :=
  8 * meScaled * gScaled

/-- Post-hoc quotient definition residual: if `gDef` is defined so that `8 * m_e * gDef = alpha`,
then `spectralPrefactorScaled m_e gDef - alpha = 0` holds tautologically for any target `alpha`. -/
def postHocPrefactorResidual (alpha eightMeG : Int) : Int :=
  eightMeG - alpha

/-- Distinct coupling constants `g1 < g2` at positive electron mass scale `meScaled > 0`
produce strictly distinct spectral prefactors. -/
theorem spectral_prefactor_glyph_collision_distinct (meScaled g1 g2 : Int)
    (hMe : 0 < meScaled) (hG : g1 < g2) :
    spectralPrefactorScaled meScaled g1 < spectralPrefactorScaled meScaled g2 := by
  dsimp [spectralPrefactorScaled]
  have h8 : 0 < 8 * meScaled := by omega
  exact Int.mul_lt_mul_of_pos_left hG h8

/-- Concrete integer-scaled witness at `m_e = 510999` (in eV) and `G_vol = 915966` vs
`G_unit = 1000000` (in `10^-6` units): the hyperbolic-volume prefactor `3744461680272`
and the unit-coupling prefactor `4087992000000` differ by `343530319728`. -/
theorem spectral_prefactor_volume_vs_unit_gap :
    spectralPrefactorScaled 510999 915966 = 3744461680272 ∧
    spectralPrefactorScaled 510999 1000000 = 4087992000000 ∧
    spectralPrefactorScaled 510999 1000000 - spectralPrefactorScaled 510999 915966 =
      343530319728 := by
  decide

/-! ### 3. `qou-plck`: Symbolic q-Rational Unit Identity and Three Length Scales -/

/-- Cleared-denominator numerator of `G_q * (hbar_q / c_q)^2` where
`hbar_q = (q - 1)/q`, `c_q = 1/(q - 1)`, and `G_q = q^2 / (q - 1)^4`. -/
def symbolicCouplingNumer (q : Int) : Int :=
  (q * q) * ((q - 1) * (q - 1)) * ((q - 1) * (q - 1))

/-- Cleared-denominator denominator of `G_q * (hbar_q / c_q)^2`. -/
def symbolicCouplingDenom (q : Int) : Int :=
  ((q - 1) * (q - 1)) * ((q - 1) * (q - 1)) * (q * q)

/-- Cleared-denominator squares of the three inequivalent q-length candidates at scale `q^2`:
(1) normalised step `1` (`q^2`),
(2) per-step share `(q - 1)/q` (`(q - 1)^2`),
(3) derived root `sqrt(q)` (`q^3`). -/
def normalisedStepSqScaled (q : Int) : Int := q * q
def perStepShareSqScaled (q : Int) : Int := (q - 1) * (q - 1)
def derivedRootSqScaled (q : Int) : Int := q * q * q

/-- The symbolic coupling numerator and denominator coincide identically for every integer `q`
by commutativity and associativity of multiplication. -/
theorem symbolic_coupling_numer_eq_denom (q : Int) :
    symbolicCouplingNumer q = symbolicCouplingDenom q := by
  dsimp [symbolicCouplingNumer, symbolicCouplingDenom]
  ac_rfl

/-- For every integer `q ≥ 2`, the three q-length candidates have strictly ordered
cleared-denominator squares: `(q - 1)^2 < q^2 < q^3`. -/
theorem three_q_length_scales_strictly_ordered (q : Int) (hq : 2 ≤ q) :
    perStepShareSqScaled q < normalisedStepSqScaled q ∧
    normalisedStepSqScaled q < derivedRootSqScaled q := by
  dsimp [perStepShareSqScaled, normalisedStepSqScaled, derivedRootSqScaled]
  have hqm1_pos : 0 < q - 1 := by omega
  have hq_pos : 0 < q := by omega
  have hlt1 : q - 1 < q := by omega
  constructor
  · have step1 : (q - 1) * (q - 1) < (q - 1) * q :=
      Int.mul_lt_mul_of_pos_left hlt1 hqm1_pos
    have step2 : (q - 1) * q < q * q :=
      Int.mul_lt_mul_of_pos_right hlt1 hq_pos
    exact Int.lt_trans step1 step2
  · have hpos2 : 0 < q * q := Int.mul_pos hq_pos hq_pos
    have hlt2 : 1 < q := by omega
    have hmul := Int.mul_lt_mul_of_pos_left hlt2 hpos2
    omega

/-! ### 4. `qou-tvrx`: Projective Polarization Dictionary Phase Freedom -/

/-- Complex phase dictionary parameter `lambda = (lamRe, lamIm)` acting on a real photon
mode pair `(phi0, phi1)` via `[phi1 : lambda * phi0]`. -/
structure PolarizationDictionaryDatum where
  lamRe : Int
  lamIm : Int
  phi0 : Int
  phi1 : Int
  deriving DecidableEq, Repr

/-- Unnormalised linear Stokes component `2 * Re(phi1 * conj(lambda * phi0)) = 2 * lamRe * phi0 * phi1`. -/
def linearStokesComponent (D : PolarizationDictionaryDatum) : Int :=
  D.lamRe * (2 * D.phi0 * D.phi1)

/-- Unnormalised circular Stokes component `2 * Im(phi1 * conj(lambda * phi0)) = -2 * lamIm * phi0 * phi1`. -/
def circularStokesComponent (D : PolarizationDictionaryDatum) : Int :=
  -D.lamIm * (2 * D.phi0 * D.phi1)

/-- Under the real dictionary `lambda = (1, 0)`, a mixed real mode `(phi0, phi1)` has
vanishing circular component; under the imaginary dictionary `lambda = (0, 1)`, the
same real mode has vanishing linear component. -/
theorem dictionary_phase_flips_linear_and_circular (phi0 phi1 : Int) :
    circularStokesComponent ⟨1, 0, phi0, phi1⟩ = 0 ∧
    linearStokesComponent ⟨0, 1, phi0, phi1⟩ = 0 ∧
    linearStokesComponent ⟨1, 0, phi0, phi1⟩ + circularStokesComponent ⟨0, 1, phi0, phi1⟩ = 0 := by
  dsimp [linearStokesComponent, circularStokesComponent]
  omega

/-- Concrete non-degenerate mixed mode `(phi0, phi1) = (1, 1)` showing that `lambda = 1`
gives pure linear polarization `(2, 0)` while `lambda = i` gives pure circular polarization `(0, -2)`. -/
theorem dictionary_phase_unfixed_witness :
    linearStokesComponent ⟨1, 0, 1, 1⟩ = 2 ∧
    circularStokesComponent ⟨1, 0, 1, 1⟩ = 0 ∧
    linearStokesComponent ⟨0, 1, 1, 1⟩ = 0 ∧
    circularStokesComponent ⟨0, 1, 1, 1⟩ = -2 := by
  decide

/-! ### 5. `qou-umev`: Unit-Determinant 2x2 Eigenvalue Discriminant and Trace Refutation -/

/-- Characteristic polynomial discriminant `tr^2 - 4 * det` for a 2x2 matrix. -/
def charPolyDiscriminant (tr det : Int) : Int :=
  tr * tr - 4 * det

/-- Six-crossing alternating braid trace `2 - 3 * h^4 - h^6` scaled by `s^6` where `h = n / s`. -/
def alternatingSixTraceScaled (n s : Int) : Int :=
  2 * (s ^ 6) - 3 * (n ^ 4) * (s ^ 2) - (n ^ 6)

/-- Even-length square generator trace `q^2 + q^{-2} = 2 + h^2` scaled by `s^2` where `h = n / s`. -/
def squareWordTraceScaled (n s : Int) : Int :=
  2 * s * s + n * n

/-- Scaled discriminant `(tr_sq)^2 - 4 * s^4` for the even-length square generator word `sigma_1^2`. -/
def squareWordDiscriminantScaled (n s : Int) : Int :=
  (squareWordTraceScaled n s) * (squareWordTraceScaled n s) - 4 * (s ^ 4)

/-- At `h = 0` (`q = 1`), the six-crossing alternating trace equals `+2` (not `-2`),
and at rational benchmark `h = 1/10` (`n = 1, s = 10`), `alternatingSixTraceScaled 1 10 = 1999699 > 0`,
refuting the `-2 * 10^6 = -2000000` degenerate-eigenvalue premise while keeping `|tr| < 2 * s^6`. -/
theorem alternating_six_trace_refutes_neg_two :
    alternatingSixTraceScaled 0 1 = 2 ∧
    alternatingSixTraceScaled 1 10 = 1999699 ∧
    alternatingSixTraceScaled 1 10 ≠ -2000000 ∧
    -2000000 < alternatingSixTraceScaled 1 10 ∧
    alternatingSixTraceScaled 1 10 < 2000000 := by
  decide

/-- For any nonzero parameter `n ≠ 0` and any scale `s`, the even-length word
`sigma_1^2` has trace strictly greater than `2 * s^2`, refuting the unconditional claim
that all even-length words have `|tr| ≤ 2`. -/
theorem square_word_trace_exceeds_two (n s : Int) (hn : n ≠ 0) :
    2 * s * s < squareWordTraceScaled n s := by
  dsimp [squareWordTraceScaled]
  have hsq : 0 < n * n := by
    rcases Int.lt_trichotomy n 0 with hlt | rfl | hgt
    · exact Int.mul_pos_of_neg_of_neg hlt hlt
    · contradiction
    · exact Int.mul_pos hgt hgt
  omega

/-- Concrete witness at `(n, s) = (1, 10)`: the even-length square word has positive
discriminant `squareWordDiscriminantScaled 1 10 = 401 > 0` (real eigenvalues off the unit circle). -/
theorem square_word_positive_discriminant_witness :
    squareWordTraceScaled 1 10 = 201 ∧
    squareWordDiscriminantScaled 1 10 = 401 ∧
    0 < squareWordDiscriminantScaled 1 10 := by
  decide

end QOU.Eightfold.Qou10v9K34vOgj5PlckTvrxUmev
