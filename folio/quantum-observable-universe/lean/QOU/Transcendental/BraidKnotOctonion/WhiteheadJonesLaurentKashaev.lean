import BraidKnotOctonion.WhiteheadJonesLaurent
import QOU.Transcendental.BraidKnotOctonion.WhiteheadBraidVolumeConjecture
import QOU.Transcendental.BraidKnotOctonion.WhiteheadLemma1RootOfUnityKashaev

/-!
# The Whitehead-braid Laurent polynomial at the Kashaev point

Transcendental companion of `BraidKnotOctonion/WhiteheadJonesLaurent.lean` (strangler split,
bean `qou-dk7p`). The braid-closure identity `braidJonesRT_eq_laurent` depends on the
generic-point data `BraidGeneric` of `WhiteheadBraidVolumeConjecture`; the Kashaev-point value
and the volume limit use the exponential.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-/

namespace QOU.Knot.FigureEightVolume

open Polynomial Finset
open QOU.Mass.QuantumSl2
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.IwahoriHecke.BraidGroup (BraidGroupN)
open QOU.Torsion.MassTraceMarkovClass (artinTower)
open QOU.MathlibExt.MarkovMoves

/-! ### The braid invariant and the Kashaev point -/

/-- At a generic `σ`, `s = σ²` avoids the clasp denominators. -/
theorem braidGeneric_root {m : ℕ} {σ : ℂ} (h : BraidGeneric m σ) :
    ∀ i : ℕ, 1 ≤ i → i < m + 1 → 1 - (σ ^ 2) ^ (2 * (i : ℤ)) ≠ 0 := by
  intro i hi1 hi2 h0
  have hq := h.2.2 i (by omega) (by omega)
  have hq0 : σ ^ 2 ≠ 0 := pow_ne_zero 2 h.1
  apply hq
  have h1 : (σ ^ 2) ^ (2 * i) = 1 := by
    have := (sub_eq_zero.mp h0).symm
    rwa [show (2 * (i : ℤ)) = ((2 * i : ℕ) : ℤ) by push_cast; ring, zpow_natCast] at this
  have hi0 : (σ ^ 2) ^ i ≠ 0 := pow_ne_zero i hq0
  rw [qint, div_eq_zero_iff]
  left
  rw [sub_eq_zero, inv_pow]
  have : (σ ^ 2) ^ i * (σ ^ 2) ^ i = 1 := by rw [← pow_add, ← two_mul, h1]
  exact (eq_inv_of_mul_eq_one_left this)

/-- **The normalised coloured Jones of the Markov class of `whiteheadWord` is a Laurent polynomial
in `q`.** For every braid `p` Markov-equivalent to `whiteheadWord` and every `σ` where the
construction is defined, `[N]⁻¹ J_N(p)(σ) = P_N(σ²)` with `P_N = whiteheadLaurent N ∈ ℤ[q, q⁻¹]`. -/
theorem braidJonesRT_eq_laurent {m : ℕ} {p : Tot BraidGroupN}
    (hp : QOU.MathlibExt.MarkovMoves.MarkovEquiv
      QOU.Torsion.MassTraceMarkovClass.artinTower ⟨2, whiteheadWord⟩ p)
    {σ : ℂ} (h : BraidGeneric m σ) :
    braidJonesRT m p σ = evalL (σ ^ 2) (pow_ne_zero 2 h.1) (whiteheadLaurent (m + 1)) := by
  rw [braidJonesRT_eq_vdv hp h, vdvWhiteheadLinkJones_eq_laurent _ (braidGeneric_root h)]

/-- **At the Kashaev point the Laurent polynomial takes the Kashaev value.** -/
theorem laurent_at_kashaev_point {N : ℕ} (hN : 1 ≤ N) :
    evalL (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) (Complex.exp_ne_zero _)
        (whiteheadLaurent N) = whiteheadLinkKashaev N := by
  rw [← vdvWhiteheadLinkJones_eq_laurent _ fun i h1 h2 => kashaev_pow_ne_one h1 h2,
    vdvWhiteheadLinkJones_at_kashaev_point hN]

/-- **The volume conjecture for the Markov class of `whiteheadWord`, with the Kashaev value as an
evaluation.** `(2π/N) log ‖P_N(e^{πi/N})‖ → Vol_Borromean / 2`, where
`P_N ∈ ℤ[q, q⁻¹]` is the Laurent polynomial that equals `[N]⁻¹ J_N` of that braid class at every generic `q`. -/
theorem whiteheadLaurent_volume_conjecture :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖evalL
        (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) (Complex.exp_ne_zero _)
        (whiteheadLaurent N)‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  refine whiteheadLink_volume_conjecture.congr' ?_
  filter_upwards [Filter.eventually_ge_atTop 1] with N hN
  rw [laurent_at_kashaev_point hN]

end QOU.Knot.FigureEightVolume
