/-!
# QOU.Organic.EvenNBarrierSpectrum — Linear trend of even-N barriers

The barriers `ΔE_closure(N)` for even N follow a linear-in-N trend
with slope `½ · |q+q⁻¹|_mol`, derived from the half-weight property
of the threading link.

## References

- [manuscript] Ch. 10, Proposition `prop:even-N-barrier-spectrum`
- [manuscript] Ch. 10, Proposition `prop:threading-half-weight`
- [manuscript] Ch. 10, Proposition `prop:ring-closure-barrier-quantitative`
-/

namespace QOU.Organic

/-- The predicted slope of `ΔE_closure(N)` vs. N in the classical
    limit q → 1: half of the molecular crossing-energy quantum. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:even-N-barrier-spectrum
def evenNBarrierSlope (e_mol : ℝ) : ℝ := e_mol / 2

/-- The predicted intercept of `ΔE_closure(N)` vs. N in the classical
    limit: `−|q+q⁻¹|_mol`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:even-N-barrier-spectrum
def evenNBarrierIntercept (e_mol : ℝ) : ℝ := -e_mol

/-- Linear model: `ΔE_closure(2m) = (m − 1) · |q+q⁻¹|_mol` in the
    classical limit. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:even-N-barrier-spectrum
def evenNBarrierModel (m : ℕ) (e_mol : ℝ) : ℝ :=
  evenNBarrierIntercept e_mol + evenNBarrierSlope e_mol * (2 * m : ℝ)

/-- Closed form: `ΔE_closure(2m) = (m − 1) · |q+q⁻¹|_mol`. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:even-N-barrier-spectrum
theorem evenNBarrierModel_closed (m : ℕ) (e_mol : ℝ) :
    evenNBarrierModel m e_mol = ((m : ℝ) - 1) * e_mol := by
  unfold evenNBarrierModel evenNBarrierIntercept evenNBarrierSlope
  ring

/-- Slope is positive when the crossing quantum is positive. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:even-N-barrier-spectrum
theorem evenNBarrierSlope_pos (e_mol : ℝ) (h : 0 < e_mol) :
    0 < evenNBarrierSlope e_mol := by
  unfold evenNBarrierSlope
  positivity

end QOU.Organic
