import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.MassEndomorphism.ComplexVolumeUnification

Complex-volume unification of mass-binding and β-decay
([binding-qbeta-complex-volume.md](binding-qbeta-complex-volume.md)).

Binding `𝔈_bind` and the β-decay `𝔔_β` are the real and imaginary parts of a
single complex fibre observable — the complexified mass-endomorphism
convolution-defect `𝔙 = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ` — the QOU analogue of the
Neumann–Zagier complex volume `Vol(K) + i·CS(K)`.

Per the owner's observation ("in many ways this is definitional"), the
unification is taken **definitionally**: `𝔙 := E₀·tr_M((Π_free−1)∘𝓜)` (𝓜 = mass endomorphism in 𝐂, Π_free = idempotent projector onto the factorized sub-object, tr_M = categorical Markov trace — no braid words),
`𝔈_bind := Re 𝔙`, `𝔔_β := Im 𝔙`.  Then the unification
`𝔈_bind + i·𝔔_β = 𝔙` is a **theorem** (`Complex.re_add_im`), sorry-free.
The only conjectural content is the *physical match*: that the measured
binding and Q_β equal these definitional Re/Im at one normalisation —
axiomatised as the class `ComplexVolumeMatch` (CLAUDE.md §3b-cond).

Fibre-level caveat: `Im(q₀)=0` at the archimedean level
(`lusztig_q_0_imaginary_part_zero`); the complex structure is fibre-level
and `𝔈_bind, 𝔔_β` are real observable shadows under different archimedean
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

/-- The complex fibre observable `𝔙 = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`. -/
noncomputable def fibreDefect (E0 : ℝ) (trDefect : ℂ) : ℂ := (E0 : ℂ) * trDefect

/-- Binding `𝔈_bind := Re 𝔙` — the bar-even / volume channel. -/
noncomputable def binding (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).re
/-- β-decay `𝔔_β := Im 𝔙` — the bar-odd / Chern–Simons channel. -/
noncomputable def Qbeta (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).im

/-- **The complex-volume unification (definitional, PROVED, sorry-free).**
    Binding (Re) and β-decay (Im) reconstruct the one complex fibre
    object `𝔙`: `𝔈_bind + i·𝔔_β = 𝔙`.  Mass and binding are no longer two
    stories — they are the two parities of one complex volume. -/
theorem complex_volume_unification (E0 : ℝ) (trDefect : ℂ) :
    (binding E0 trDefect : ℂ) + (Qbeta E0 trDefect : ℂ) * Complex.I
      = fibreDefect E0 trDefect := by
  unfold binding Qbeta
  exact Complex.re_add_im _

/-! ## Physical-match conjecture (the only open content) -/

/-- The physical-match conjecture (CLAUDE.md §3b-cond class): the
    *measured* complex volume of a composite `K` — the **single** observable
    `𝔙_obs = 𝔈_bind^obs + i·𝔔_β^obs` — equals `𝔙(K)` at a single
    normalisation.  One hypothesis (`volume_match`), not two parallel arms:
    binding and `Q_β` are the Re/Im of *one* measured object, matched to the
    Re/Im of *one* fibre object.  This is the conjectural input; the
    unification theorem above is proved unconditionally. -/
class ComplexVolumeMatch (K : Type*) where
  /-- substrate energy scale `E₀`. -/
  E0 : ℝ
  /-- the complexified convolution-defect `tr_M((Π_free−1)∘𝓜)(K) ∈ ℂ` (fibre-level). -/
  trDefect : ℂ
  /-- the **measured complex volume** `𝔙_obs = 𝔈_bind^obs + i·𝔔_β^obs ∈ ℂ`
      (binding as Re, β-decay Q-value as Im — one observable, two shadows). -/
  measured_volume : ℂ
  /-- the single physical-match hypothesis: `𝔙_obs = E₀·(defect)`. -/
  volume_match : measured_volume = fibreDefect E0 trDefect

namespace ComplexVolumeMatch
variable {K : Type*} [c : ComplexVolumeMatch K]

/-- Measured binding `𝔈_bind^obs := Re 𝔙_obs`. -/
def binding_measured : ℝ := c.measured_volume.re
/-- Measured β-decay Q-value `𝔔_β^obs := Im 𝔙_obs`. -/
def qbeta_measured : ℝ := c.measured_volume.im

/-- Measured binding matches `Re 𝔙` (derived from the single `volume_match`). -/
theorem binding_match : (binding_measured (K := K)) = binding c.E0 c.trDefect := by
  unfold binding_measured binding; rw [c.volume_match]
/-- Measured Q-value matches `Im 𝔙`. -/
theorem qbeta_match : (qbeta_measured (K := K)) = Qbeta c.E0 c.trDefect := by
  unfold qbeta_measured Qbeta; rw [c.volume_match]

end ComplexVolumeMatch

/-- Under the physical-match class, the measured observables reconstruct
    the complex defect: `𝔈_bind^obs + i·𝔔_β^obs = 𝔙`.  Now immediate from the
    single `volume_match` + the definitional unification. -/
theorem measured_complex_volume {K : Type*} [c : ComplexVolumeMatch K] :
    (ComplexVolumeMatch.binding_measured (K := K) : ℂ)
        + (ComplexVolumeMatch.qbeta_measured (K := K) : ℂ) * Complex.I
      = fibreDefect c.E0 c.trDefect := by
  rw [ComplexVolumeMatch.binding_match, ComplexVolumeMatch.qbeta_match]
  exact complex_volume_unification _ _

end QOU.MassEndomorphism
