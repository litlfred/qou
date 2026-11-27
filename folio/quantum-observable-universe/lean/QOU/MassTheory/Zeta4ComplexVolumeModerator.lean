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
import Mathlib.Data.Complex.Basic
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

/-! ## The moderator on `G_m` — `ζ₄` acts by multiplication

Following the owner ruling of 2026-11-27 (roots of unity), the rotation
`η ↦ η + iπ/2` is written on the multiplicative coordinate `x = e^η ∈ G_m`,
where it is multiplication by the root of unity `ζ` with `ζ² = −1`, defined
algebraically.  `cosh` and `sinh` are the bar-even and bar-odd parts
`(x ± x⁻¹)/2`.  The identification `ζ = e^{iπ/2}` is the non-analytic `exp`
label; the `Complex.cosh` forms are in
`QOU.Transcendental.MassTheory.Zeta4ComplexVolumeModeratorReal`. -/

section GmModerator

variable {K : Type*} [Field K]

/-- Bar-even part of `x ∈ G_m`: `(x + x⁻¹)/2`, the cosh channel. -/
def barEvenPart (x : K) : K := (x + x⁻¹) / 2

/-- Bar-odd part of `x ∈ G_m`: `(x − x⁻¹)/2`, the sinh channel. -/
def barOddPart (x : K) : K := (x - x⁻¹) / 2

/-- **`Re 𝔙 ↦ i·Im-channel`, on `G_m`.**  Multiplying by `ζ` with `ζ² = −1`
sends the bar-even part to `ζ ×` the bar-odd part. -/
theorem barEvenPart_zeta4_mul {ζ x : K} (hζ : ζ ^ 2 = -1) :
    barEvenPart (ζ * x) = ζ * barOddPart x := by
  have hinv : ζ⁻¹ = -ζ :=
    inv_eq_of_mul_eq_one_right (by linear_combination -hζ)
  unfold barEvenPart barOddPart
  rw [mul_inv, hinv]
  ring

/-- **`Im 𝔙 ↦ i·Re-channel`, on `G_m`.**  The same multiplication sends the
bar-odd part to `ζ ×` the bar-even part. -/
theorem barOddPart_zeta4_mul {ζ x : K} (hζ : ζ ^ 2 = -1) :
    barOddPart (ζ * x) = ζ * barEvenPart x := by
  have hinv : ζ⁻¹ = -ζ :=
    inv_eq_of_mul_eq_one_right (by linear_combination -hζ)
  unfold barEvenPart barOddPart
  rw [mul_inv, hinv]
  ring

end GmModerator

end QOU.Mass.Zeta4ComplexVolumeModerator
