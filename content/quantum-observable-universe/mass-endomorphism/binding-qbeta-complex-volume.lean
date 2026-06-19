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

/-! ## Bar-parity + descent over a CommRing with involution (§7c — NOT `ℂ`)

The *proofs* live over a commutative ring `R` with a ring **involution**
`σ` (the bar-involution `q ↦ q⁻¹`), **not** `ℂ`. `σ`-even `x + σx` is the
binding (bar-even / `cosh`) channel; `σ`-odd `x − σx` is the `𝔔_β`
(bar-odd / `sinh`) channel. `ℂ` with complex conjugation is just the
*archimedean realisation* (below). The `/2` (`cosh`/`sinh`) normalisation
is narrative; we use the division-free `x ± σx` forms, so everything
holds over any `CommRing`. -/
section BarParityInvolution
variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- `σ`-even + `σ`-odd reconstructs `2x` (`(x+σx) + (x−σx) = 2x`). -/
theorem barParity_sum (x : R) : (x + σ x) + (x - σ x) = 2 * x := by ring

/-- `σ`-even − `σ`-odd reconstructs `2·σx`. -/
theorem barParity_diff (x : R) : (x + σ x) - (x - σ x) = 2 * σ x := by ring

/-- **Involution descent.** One ring identity `x = w` yields BOTH the
    bar-even (binding) and bar-odd (`𝔔_β`) identities at once — the
    `[CommRing R]`-generic form of "prove on `𝔙` once, read off both
    channels" (no `ℂ`, no `/2`). -/
theorem invol_descent {x w : R} (h : x = w) :
    (x + σ x = w + σ w) ∧ (x - σ x = w - σ w) :=
  ⟨by rw [h], by rw [h]⟩

/-- **Recurrence descent — the `c_k`-ladder mechanism, generic.** A
    three-term recurrence `𝔙ₚ = c·𝔙ₖ − 𝔙ₘ` with a **bar-even** multiplier
    `c` (`σ c = c`, the `2cosh η` analogue) yields the binding (`σ`-even)
    AND `𝔔_β` (`σ`-odd) recurrences from the *single* ring proof. -/
theorem recurrence_invol_descent {Vp Vk Vm c : R} (hc : σ c = c)
    (h : Vp = c * Vk - Vm) :
    ((Vp + σ Vp) = c * (Vk + σ Vk) - (Vm + σ Vm)) ∧
    ((Vp - σ Vp) = c * (Vk - σ Vk) - (Vm - σ Vm)) := by
  have key : σ Vp = c * σ Vk - σ Vm := by
    simp only [h, map_sub, map_mul, hc]
  exact ⟨by rw [key, h]; ring, by rw [key, h]; ring⟩

end BarParityInvolution

/-! ## Archimedean realisation (`ℂ`, `σ =` complex conjugation) -/

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

/-- **The definitional unification imposes NO cross-constraint between the
    channels.** Every pair `(a, b)` of real values is realised as `(Re 𝔙, Im 𝔙)`
    for some `𝔙`, so knowing the unification `𝔙 = 𝔈_bind + i·𝔔_β`
    (`complex_volume_unification`, i.e. `Complex.re_add_im`) constrains binding
    given `𝔔_β` — or vice versa — **not at all**.

    This is the formal core of the holomorphy-closure audit
    (`docs/audits/2026-06-19-qbeta-complex-volume-holomorphy-no-cr-cross-constraint.md`):
    `re_add_im` is a **real-linear reconstruction**, not a Cauchy–Riemann
    constraint. `Re` and `Im` are independent real degrees of freedom of one
    complex number. A *holomorphic* `𝔙(q)` would tie them via CR — but the audit
    shows no such holomorphy is available where the cross-constraint was hoped
    for: the `i` is the bar-involution / target `ℂ` (the proofs above live over a
    `CommRing` with involution, not over a holomorphic source), the two channels
    are read at different archimedean loci (real-`q` vs root-of-unity), and at
    the observable level `Im(q₀) = 0` (`lusztig_q_0_imaginary_part_zero`) so
    there is no holomorphic disk at all. Hence the keystone-tower separation
    (Q_β `c_k` argument-ladder vs binding `Δ_λ` order-tower) survives: `𝔙`
    unifies the two legs as one fibre object with two real shadows, NOT as a
    holomorphic cross-constraint. -/
theorem re_im_independent (a b : ℝ) : ∃ z : ℂ, z.re = a ∧ z.im = b :=
  ⟨⟨a, b⟩, rfl, rfl⟩

/-! ## Descent — one proof on `𝔙` covers binding AND `𝔔_β`

The "prove once, read off both channels" payoff is the **generic**
`invol_descent` / `recurrence_invol_descent` above (over `[CommRing R]`
with the bar-involution `σ`). The `ℂ` Re/Im descent is simply their
**archimedean instance** with `σ =` complex conjugation: `Re z = (z+σz)/2`
(bar-even / binding) and `Im z` carried by `(z−σz)/2` (bar-odd / `𝔔_β`).
No separate `ℂ`-only lemma is needed — the proofs live over the ring with
involution, per CLAUDE.md §7c. -/

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
