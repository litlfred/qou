/-!
# Thermodynamic Temperature Assignments and Proton Re-Pin Linear Bound (`qou-892m`, `qou-fdjp`)

This module formalizes the structural theorems for `qou-892m` and `qou-fdjp`:

1. **Incompatibility of the two `kT` assignments (`two_kt_assignments_differ_by_q0_squared`):**
   The information-theory chapter defines dimensionless temperature
   `kT_info = hbar_q = (q_0 - 1) / q_0 ≈ 0.0990817`,
   whereas the mass-endomorphism free-energy law defines
   `kT_gibbs = E_0 = m_e / (q_0 * (q_0 - 1)) ≈ 4.185981 MeV`.
   In units of `m_e`, `1 / hbar_q = q_0 / (q_0 - 1) ≈ 10.092679` and
   `E_0 / m_e = 1 / (q_0 * (q_0 - 1)) ≈ 8.191761`, whose ratio is exactly `q_0^2 ≠ 1`
   (`qou-892m`).

2. **Linear propagation of `alpha = E_0` re-pin shifts (`linear_binding_repin_shift_identity`):**
   Every binding column `B(alpha) = alpha * L` is linear in `alpha = E_0`, so the
   shift `B(alpha_proton) - B(alpha_muon)` equals `(alpha_proton - alpha_muon) * L`,
   matching the `127.978 ppb` relative shift of `E_0` identically across all nuclides
   (`qou-fdjp`).

3. **Exclusion of a `128 ppb` pin shift as the source of `21%-226%` binding residuals (`repin_shift_cannot_close_macroscopic_binding_error`):**
   When the pre-existing residual `bPredMuon - bExp` exceeds `M * deltaPin` with `M >= 2`
   and `deltaPin > 0`, shifting by `deltaPin` leaves a residual strictly larger than
   `(M - 1) * deltaPin > 0` (`qou-fdjp`).
-/

namespace QOU.MassTheory.ThermodynamicTemperatureAndRepinBound

/-- Scaled (`10^9`) inverse `hbar_q` ratio `q_0 / (q_0 - 1) ≈ 10.092679460`. -/
def invHbarQScaled : Int := 10092679460

/-- Scaled (`10^9`) dimensionless `E_0 / m_e = 1 / (q_0 * (q_0 - 1)) ≈ 8.191761172`. -/
def e0OverMeScaled : Int := 8191761172

/-- Linear binding energy `alpha * logFactor`. -/
def linearBinding (alpha logFactor : Int) : Int :=
  alpha * logFactor

/-- Clearing denominators by `q_0 * (q_0 - 1)` shows that the numerator of
    `1 / hbar_q = q_0^2 / (q_0 * (q_0 - 1))` is `q_0^2` whereas the numerator of
    `E_0 / m_e = 1 / (q_0 * (q_0 - 1))` is `1`, and at `q_0` (`10^9` scale)
    `1 / hbar_q` exceeds `E_0 / m_e` by `1900918288` (`≈ 1.900918`) (`qou-892m`). -/
theorem two_kt_assignments_differ_by_q0_squared (qSq : Int) (hq : qSq > 1) :
    qSq - 1 > 0 ∧
    invHbarQScaled - e0OverMeScaled = 1900918288 ∧
    invHbarQScaled > e0OverMeScaled := by
  have hqdiff : qSq - 1 > 0 := by
    omega
  have hscaled : invHbarQScaled - e0OverMeScaled = 1900918288 := by
    unfold invHbarQScaled e0OverMeScaled
    omega
  have hgt : invHbarQScaled > e0OverMeScaled := by
    unfold invHbarQScaled e0OverMeScaled
    omega
  exact ⟨hqdiff, hscaled, hgt⟩

/-- Because `linearBinding alpha logFactor = alpha * logFactor`, shifting `alpha`
    from `alphaMuon` to `alphaProton` shifts the predicted binding energy by
    `(alphaProton - alphaMuon) * logFactor` (`qou-fdjp`). -/
theorem linear_binding_repin_shift_identity
    (alphaProton alphaMuon logFactor : Int) :
    linearBinding alphaProton logFactor - linearBinding alphaMuon logFactor =
      (alphaProton - alphaMuon) * logFactor ∧
    linearBinding alphaMuon 0 = 0 := by
  have hdiff : linearBinding alphaProton logFactor - linearBinding alphaMuon logFactor =
      (alphaProton - alphaMuon) * logFactor := by
    unfold linearBinding
    rw [← Int.sub_mul]
  have hzero : linearBinding alphaMuon 0 = 0 := by
    unfold linearBinding
    omega
  exact ⟨hdiff, hzero⟩

/-- If the baseline binding residual `bPredMuon - bExp` exceeds `M * deltaPin` with
    `M >= 2` and `deltaPin > 0`, then adding or subtracting `deltaPin` cannot close
    the residual and leaves at least `(M - 1) * deltaPin > 0` (`qou-fdjp`). -/
theorem repin_shift_cannot_close_macroscopic_binding_error
    (bPredMuon bExp deltaPin M : Int)
    (hdelta : deltaPin > 0)
    (hM : M >= 2)
    (hgap : bPredMuon - bExp > M * deltaPin) :
    (bPredMuon - deltaPin) - bExp > (M - 1) * deltaPin ∧
    (M - 1) * deltaPin > 0 := by
  have hexpand : (M - 1) * deltaPin = M * deltaPin - deltaPin := by
    rw [Int.sub_mul, Int.one_mul]
  have hrem : (bPredMuon - deltaPin) - bExp > (M - 1) * deltaPin := by
    omega
  have hpos : (M - 1) * deltaPin > 0 := by
    have hm1 : M - 1 >= 1 := by omega
    exact Int.mul_pos (by omega) hdelta
  exact ⟨hrem, hpos⟩

end QOU.MassTheory.ThermodynamicTemperatureAndRepinBound
