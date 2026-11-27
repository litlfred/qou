/-
# The `3` in the electron's ring reading is `3·lk`: two-strand torus links

Thread "Derive the electron's categorical weight", fourth part (2026-11-27, owner card: "Prove
the 3 is 3·lk in Lean"). Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §10.

`QOU.Observations.ElectronRingMassReading` found that the electron (Hopf link) has ring energy
reading `U_e(1) = 3`. There were two candidates for the `3`: `3·lk` (`lk(Hopf) = 1`) and the
constant `N² − 1 = 3`. This file reads the whole family of two-strand closures `σ₁ⁿ`, the torus
links and knots `T(2, n)`, on the same ring mass. For even `n = 2k` the closure is a two-component
link with `lk = k`, and for odd `n` it is a knot.

* `ocneanu_weights_forced`: on `H₂(q)` (eigenvalues `q`, `−q⁻¹`), a normalised Markov trace with
  the convention-D parameter `z_D = q³/(q²+1)` has weights `[3]/[2]²` and `1/[2]²`. No choice.
* `trace2`: so `tr_D(σ₁ⁿ) = ([3] qⁿ + (−q⁻¹)ⁿ)/[2]²`. `trace2_zero` and `trace2_one` check the
  normalisation and the Markov parameter.
* `ringMass2_eq`: the ring mass `[2]² q^{−2n} tr_D(σ₁ⁿ) = [3] q⁻ⁿ + (−1)ⁿ q^{−3n}`.
* `ringMass2_two`: at `n = 2` it is `[4]/q³`, the electron's ring mass (the three-strand word of
  `ElectronRingMassReading` gives the same value, as stabilisation invariance requires).
* `ringMass2_at_one`: `m(1) = 3 + (−1)ⁿ`, which is `4 = 2²` for links and `2` for knots.

The derivative at `q = 1` is in `QOU.Transcendental.MassTheory.RingMassLinkingNumber`:
`U(1) = 3k = 3·lk` on `T(2, 2k)` and `U(1) = 0` on every knot `T(2, 2k+1)`. At `k = 2`, `U(1) = 6`,
so the constant `N² − 1` is ruled out. No measured value enters.
-/
import QOU.Observations.ElectronRingMassReading

namespace QOU.Observations.RingMassLinkingNumber

open QOU.Observations.ElectronRingMassReading

variable {R : Type*} [Field R]

/-- Balanced `[3] = q² + 1 + q⁻²`. -/
def qInt3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- **The Ocneanu weights on `H₂` are forced by the convention-D parameter.** If `a + b = 1` and
`a q − b q⁻¹ = q³/(q²+1)`, then `a = [3]/[2]²` and `b = 1/[2]²`. -/
theorem ocneanu_weights_forced (q a b : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (hsum : a + b = 1) (hz : a * q - b * q⁻¹ = q ^ 3 / (q ^ 2 + 1)) :
    a = qInt3 q / (q + q⁻¹) ^ 2 ∧ b = 1 / (q + q⁻¹) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero h2 hq
  have hb : b = 1 - a := by linear_combination hsum
  subst hb
  have ha : a * (q ^ 2 + 1) ^ 2 = q ^ 4 + q ^ 2 + 1 := by
    field_simp at hz
    linear_combination hz
  have ha' : a = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
    rw [eq_div_iff (pow_ne_zero 2 h2)]; exact ha
  constructor
  · rw [ha']; unfold qInt3; field_simp
  · rw [ha']; field_simp; ring

/-- The convention-D trace of `σ₁ⁿ` on two strands. -/
def trace2 (q : R) (n : ℕ) : R := (qInt3 q * q ^ n + (-q⁻¹) ^ n) / (q + q⁻¹) ^ 2

theorem trace2_zero (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : trace2 q 0 = 1 := by
  have hs : (q + q⁻¹) ^ 2 ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact pow_ne_zero 2 (div_ne_zero h2 hq)
  unfold trace2 qInt3
  rw [div_eq_one_iff_eq hs]
  field_simp
  ring

/-- `tr_D(σ₁) = z_D = q³/(q²+1)`. -/
theorem trace2_one (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trace2 q 1 = q ^ 3 / (q ^ 2 + 1) := by
  unfold trace2 qInt3
  field_simp
  ring

/-- The framing-corrected ring mass of the closure of `σ₁ⁿ` (`def:mass-identity`, two strands,
writhe `n`). -/
def ringMass2 (q : R) (n : ℕ) : R := (q + q⁻¹) ^ 2 * q⁻¹ ^ (2 * n) * trace2 q n

/-- **`m(σ₁ⁿ) = [3] q⁻ⁿ + (−1)ⁿ q^{−3n}`.** -/
theorem ringMass2_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (n : ℕ) :
    ringMass2 q n = qInt3 q * q⁻¹ ^ n + (-1) ^ n * q⁻¹ ^ (3 * n) := by
  have hs : (q + q⁻¹) ^ 2 ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact pow_ne_zero 2 (div_ne_zero h2 hq)
  unfold ringMass2 trace2
  rw [mul_div_assoc', mul_comm ((q + q⁻¹) ^ 2), mul_assoc, mul_div_assoc, mul_div_cancel_left₀ _ hs]
  rw [neg_pow]
  simp only [inv_pow]
  have e2 : q ^ (2 * n) = q ^ n * q ^ n := by ring
  have e3 : q ^ (3 * n) = q ^ n * q ^ n * q ^ n := by ring
  rw [e2, e3]
  field_simp

/-- **Hopf link (`n = 2`): the two-strand ring mass is the electron's `[4]/q³`.** -/
theorem ringMass2_two (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ringMass2 q 2 = qInt4 q / q ^ 3 := by
  rw [ringMass2_eq q hq h2]
  unfold qInt3 qInt4
  simp only [inv_pow]
  field_simp
  ring

/-- `m(1) = 3 + (−1)ⁿ`. -/
theorem ringMass2_at_one (n : ℕ) :
    qInt3 (1 : R) * 1⁻¹ ^ n + (-1) ^ n * 1⁻¹ ^ (3 * n) = 3 + (-1) ^ n := by
  unfold qInt3; norm_num

end QOU.Observations.RingMassLinkingNumber
