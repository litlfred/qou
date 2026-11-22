import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Which gl₆ label order keeps the ruled isospin charge (issue #8833)

A quark strand is `C² ⊗ C³` (isospin `t ∈ {0,1}`, colour `c ∈ {0,1,2}`), embedded in `C⁶` by a
lexicographic order. The gl₆ quantum-trace element `q^{2ρ}` gives label of rank `r` the
exponent `5 − 2r`.

* isospin-major (`r = 3t + c`): exponent `3(1 − 2t) + 2(1 − c)`;
* colour-major (`r = 2c + t`): exponent `(1 − 2t) + 4(1 − c)`.

The ruled D1 rule weighs proton/neutron sectors by the isospin charge exponent `±1` per
quark. Generalising to `C² ⊗ C^b`, the isospin-major isospin exponent is `b(1 − 2t)`, which
equals `1 − 2t` for both `t` iff `b = 1` (`isospinMajor_agrees_iff`). The colour-major isospin
exponent is `1 − 2t` for every `b` (`colourMajor_isospin_exponent`).
-/

namespace QOU.QBeta.GlSixOrderCharge

/-- gl_N `q^{2ρ}` exponent of the label of rank `r`. -/
def rhoExp (N r : ℤ) : ℤ := (N - 1) - 2 * r

theorem isospinMajor_exponent (t c : ℤ) :
    rhoExp 6 (3 * t + c) = 3 * (1 - 2 * t) + 2 * (1 - c) := by
  simp only [rhoExp]; ring

theorem colourMajor_exponent (t c : ℤ) :
    rhoExp 6 (2 * c + t) = (1 - 2 * t) + 4 * (1 - c) := by
  simp only [rhoExp]; ring

/-- On `C² ⊗ C^b`, isospin-major: the isospin part of `rhoExp (2b) (b t + c)` is `b(1 − 2t)`. -/
theorem isospinMajor_general (b t c : ℤ) :
    rhoExp (2 * b) (b * t + c) = b * (1 - 2 * t) + ((b - 1) - 2 * c) := by
  simp only [rhoExp]; ring

/-- On `C² ⊗ C^b`, colour-major: the isospin part of `rhoExp (2b) (2c + t)` is `1 − 2t`. -/
theorem colourMajor_isospin_exponent (b t c : ℤ) :
    rhoExp (2 * b) (2 * c + t) = (1 - 2 * t) + 2 * ((b - 1) - 2 * c) := by
  simp only [rhoExp]; ring

/-- The isospin-major isospin exponent agrees with the ruled charge `1 − 2t` at `t = 0`
iff `b = 1`, i.e. only with no colour. -/
theorem isospinMajor_agrees_iff (b : ℤ) : b * (1 - 2 * 0) = 1 - 2 * 0 ↔ b = 1 := by
  constructor <;> intro h <;> linarith

end QOU.QBeta.GlSixOrderCharge
