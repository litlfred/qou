import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.MassEndomorphism.ComplexVolumeUnification

Complex-volume unification of mass-binding and β-decay
([binding-qbeta-complex-volume.md](binding-qbeta-complex-volume.md)).

Binding `𝔅` and the β-decay `𝔔_β` are the real and imaginary parts of a
single complex fibre observable — the complexified mass-endomorphism
convolution-defect `𝔚 = E₀(tr_M^free − tr_M^knot) ∈ ℂ` — the QOU analogue of the
Neumann–Zagier complex volume `Vol(K) + i·CS(K)`.

Per the owner's observation ("in many ways this is definitional"), the
unification is taken **definitionally**: `𝔚 := E₀(tr_M^free − tr_M^knot)`,
`𝔅 := Re 𝔚`, `𝔔_β := Im 𝔚`.  Then the unification
`𝔅 + i·𝔔_β = 𝔚` is a **theorem** (`Complex.re_add_im`), sorry-free.
The only conjectural content is the *physical match*: that the measured
binding and Q_β equal these definitional Re/Im at one normalisation —
axiomatised as the class `ComplexVolumeMatch` (CLAUDE.md §3b-cond).

Fibre-level caveat: `Im(q₀)=0` at the archimedean level
(`lusztig_q_0_imaginary_part_zero`); the complex structure is fibre-level
and `𝔅, 𝔔_β` are real observable shadows under different archimedean
evaluations (real-q vs root-of-unity), exactly as `Vol` and `CS` are
separately real.

Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
Ref: [kashaev1997] https://doi.org/10.1007/BF00768318
-/

namespace QOU.MassEndomorphism

open Complex

/-! ## Bar-parity decomposition (generic field, §7c)

The bar-even part is `∝ q + q⁻¹ = 2cosh(log q)` and the bar-odd part is
`∝ q − q⁻¹ = 2sinh(log q)`.  The `/2` normalisation (`cosh`/`sinh`) is
narrative; the structural fact proved here is that the two parities
reconstruct the eigenvalues `q` (`= e^{+λ}`) and `q⁻¹` (`= e^{−λ}`),
holding over any field (`q⁻¹` cancels additively — no `q ≠ 0`). -/
section BarParity
variable {R : Type*} [Field R]

/-- Sum of the bar-parities reconstructs `2q` (`= e^λ + e^{−λ}` doubled
    even part... here `(q+q⁻¹) + (q−q⁻¹) = 2q`). -/
theorem barParity_sum (q : R) : (q + q⁻¹) + (q - q⁻¹) = 2 * q := by ring

/-- Difference of the bar-parities reconstructs `2q⁻¹`. -/
theorem barParity_diff (q : R) : (q + q⁻¹) - (q - q⁻¹) = 2 * q⁻¹ := by ring

end BarParity

/-! ## The complex convolution-defect and the definitional unification -/

/-- The complex fibre observable `𝔚 = E₀(tr_M^free − tr_M^knot) ∈ ℂ`. -/
noncomputable def fibreDefect (E0 : ℝ) (trDefect : ℂ) : ℂ := (E0 : ℂ) * trDefect

/-- Binding `𝔅 := Re 𝔚` — the bar-even / volume channel. -/
noncomputable def binding (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).re
/-- β-decay `𝔔_β := Im 𝔚` — the bar-odd / Chern–Simons channel. -/
noncomputable def Qbeta (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).im

/-- **The complex-volume unification (definitional, PROVED, sorry-free).**
    Binding (Re) and β-decay (Im) reconstruct the one complex fibre
    object `𝔚`: `𝔅 + i·𝔔_β = 𝔚`.  Mass and binding are no longer two
    stories — they are the two parities of one complex volume. -/
theorem complex_volume_unification (E0 : ℝ) (trDefect : ℂ) :
    (binding E0 trDefect : ℂ) + (Qbeta E0 trDefect : ℂ) * Complex.I
      = fibreDefect E0 trDefect := by
  unfold binding Qbeta
  exact Complex.re_add_im _

/-! ## Physical-match conjecture (the only open content) -/

/-- The physical-match conjecture (CLAUDE.md §3b-cond class): the
    *measured* binding and `Q_β` of a composite `K` equal the
    definitional Re/Im of `𝔚(K)` at a single normalisation.
    This is the conjectural input; the unification theorem above is
    proved unconditionally. -/
class ComplexVolumeMatch (K : Type*) where
  /-- substrate energy scale `E₀`. -/
  E0 : ℝ
  /-- the complexified convolution-defect `(tr_M^free − tr_M^knot)(K) ∈ ℂ` (fibre-level). -/
  trDefect : ℂ
  /-- the experimentally measured binding energy. -/
  binding_measured : ℝ
  /-- the experimentally measured β-decay `Q`-value. -/
  qbeta_measured : ℝ
  /-- match hypothesis: measured binding `=` Re `𝔚`. -/
  binding_match : binding_measured = binding E0 trDefect
  /-- match hypothesis: measured `Q_β` `=` Im `𝔚`. -/
  qbeta_match : qbeta_measured = Qbeta E0 trDefect

/-- Under the physical-match class, the measured observables reconstruct
    the complex defect: `𝔅_meas + i·𝔔_β,meas = 𝔚`.  Derived from the two
    match hypotheses and the definitional unification — non-degenerate
    (the class carries the inputs; the theorem composes them). -/
theorem measured_complex_volume {K : Type*} [c : ComplexVolumeMatch K] :
    (c.binding_measured : ℂ) + (c.qbeta_measured : ℂ) * Complex.I
      = fibreDefect c.E0 c.trDefect := by
  rw [c.binding_match, c.qbeta_match]
  exact complex_volume_unification _ _

end QOU.MassEndomorphism
