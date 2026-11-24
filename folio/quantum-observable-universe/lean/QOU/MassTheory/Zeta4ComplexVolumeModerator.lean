/-
# ζ₄ = i moderates Re 𝔙 (binding) and Im 𝔙 (Q_β) — the complex-volume coupling

The complex-volume observable `𝔙 = Vol + i·CS` (Neumann–Zagier analogue;
`conj:binding-qbeta-complex-volume`) splits by the bar involution `q ↔ q⁻¹` (`q = e^η`,
`η ↦ −η`) into

  * `Re 𝔙 = 𝔈_bind` — binding, **bar-even** (`cosh`-type), the q-Hermite moment side (PR #2899);
  * `Im 𝔙 = 𝔔_β` — β-decay Q-value, **bar-odd** (`sinh`-type), the `c_k` Habiro side.

A projector only *splits* the two channels; what *moderates* (couples) them is the `i` of
`𝔙 = Vol + i·CS`, which in the q-Askey / root-of-unity world is `ζ₄ = i`. This file pins that:

* the `ζ₄ = i` rotation `η ↦ η + iπ/2` sends `cosh ↦ i·sinh` and `sinh ↦ i·cosh` — i.e. it rotates
  `Re 𝔙 ↔ i·Im 𝔙`, exactly the complex-volume coupling (`cosh_zeta4_rotation` /
  `sinh_zeta4_rotation`);
* `Φ₄ = q²+1` — the cyclotomic factor that appears as the **shared residue** of the binding side
  (`L₂`'s denominator `2·Φ₄`, PR #2929) and the Q_β `c_k` kernel (`a₁`'s ζ₄ residue) — is exactly
  the locus `q = ζ₄ = i`, where the bar-even generator `[2]_q = q+q⁻¹` **vanishes** and the bar-odd
  generator `h = q−q⁻¹` becomes **pure imaginary** `2i` (`phi4_root_zeta4`, `barEven_zeta4`,
  `barOdd_zeta4`).

So the `Φ₄` shared between the two sides is not a coincidence of common cyclotomic factors: it is
the algebraic locus of the `i = ζ₄` rotation that interchanges the binding (`Re`) and Q_β (`Im`)
channels of the single complex-volume object `𝔙`.

> **Scope (a).** This pins the moderator at the *generator* level (cosh ↔ i·sinh; the Φ₄ = ζ₄
> locus). That the *full* binding and Q_β observables are exact ζ₄-rotates of one another is the
> stronger claim, gated on the wired values — not asserted here.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-28-wlambda-identity-i-rescope-no-hlf.md §"Finding 3"
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

namespace QOU.Mass.Zeta4ComplexVolumeModerator

/-! ## Algebraic ζ₄ locus — the shared `Φ₄` residue is `q = i` -/

/-- `Φ₄(ζ₄) = 0`: `ζ₄ = i` is the root of the shared cyclotomic residue `Φ₄ = q²+1`. -/
theorem phi4_root_zeta4 : Complex.I ^ 2 + 1 = 0 := by
  rw [Complex.I_sq]; ring

/-- At `q = ζ₄ = i` the **bar-even** generator `[2]_q = q + q⁻¹` (binding / `Re 𝔙`, cosh-type)
**vanishes**. -/
theorem barEven_zeta4 : Complex.I + Complex.I⁻¹ = 0 := by
  rw [Complex.inv_I]; ring

/-- At `q = ζ₄ = i` the **bar-odd** generator `h = q − q⁻¹` (Q_β / `Im 𝔙`, sinh-type) becomes
**pure imaginary** `2i`. -/
theorem barOdd_zeta4 : Complex.I - Complex.I⁻¹ = 2 * Complex.I := by
  rw [Complex.inv_I]; ring

/-! ## The smooth moderator — the `ζ₄` rotation `η ↦ η + iπ/2` exchanges cosh ↔ i·sinh -/

/-- **`Re 𝔙 ↦ i·Im-channel`.** The `ζ₄ = i` rotation `η ↦ η + iπ/2` sends `cosh η` to `i·sinh η`:
the bar-even (binding) channel rotates into `i ×` the bar-odd (Q_β) channel — the
`Re 𝔙 ↔ i·Im 𝔙` coupling of the complex volume `𝔙 = Vol + i·CS`. -/
theorem cosh_zeta4_rotation (z : ℂ) :
    Complex.cosh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.sinh z := by
  rw [Complex.cosh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- **`Im 𝔙 ↦ i·Re-channel`.** The companion: the same rotation sends `sinh η` to `i·cosh η`. -/
theorem sinh_zeta4_rotation (z : ℂ) :
    Complex.sinh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.cosh z := by
  rw [Complex.sinh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- Subtracting the rotated hyperbolic sine term from the shifted hyperbolic cosine cancels to zero (`qou-f8rr`). -/
theorem cosh_zeta4_rotation_sub_eq_zero (z : ℂ) :
    Complex.cosh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) - Complex.I * Complex.sinh z = 0 := by
  rw [cosh_zeta4_rotation z, sub_self]

end QOU.Mass.Zeta4ComplexVolumeModerator
