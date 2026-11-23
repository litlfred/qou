import QOU.Knot.WhiteheadLemma1Derived
import QOU.Mass.QuantumSl2BeltBraid

/-!
# The Whitehead link as a braid closure

The Whitehead link is the closure of the three-strand braid `β = σ₁⁻² σ₂ σ₁⁻¹ σ₂`. On
`V_N^{⊗3}` (`N = m + 1`, `q = σ²`), with `σ₁ = Ř ⊗ 1` and `σ₂ = 1 ⊗ Ř`, this file proves for
every `N`

    vdvWhiteheadLinkJones q N = q^{(N²−1)/2} [N]⁻¹ tr(K^{⊗3} β)      (`vdvWhiteheadLinkJones_eq_braidTrace`).

Here `tr(K^{⊗3} ·)` is the braid-closure quantum trace, `[N] = tr_{V_N}(K)` is its value on the
unknot, and `q^{(N²−1)/2} = σ^{N²−1}` corrects the framing of `β` (writhe `−1`). So van der
Veen's printed formula is the normalised braid-closure trace, with no sign.

**The sign `(−1)^{N−1}`.** The tangle form of the same number,
`tr(Δ(K) · B · q^{N²−1} X)` with the belt `B` and the clasp `X` built from the Kauffman cup
and cap, differs from the braid-closure trace by `(−1)^{N−1}`
(`trace_belt_clasp_eq_braidTrace`). The sign is the flype: turning the hook of the clasp over
costs `(−1)^m s^{m(m+2)} Ř` (`natOp_flype`).

The proof closes the third strand of `β` into the hook of `QuantumSl2LoopLemma`
(`trace_kTri_hook`), identifies the hook of `Ř²` with the belt by the two hexagons
(`hookOp_mono_eq_beltW`), and moves between them by bending and the flype
(`trace_kTri_whitehead`). That `tr(K^{⊗3} ·)` of a braid is an invariant of its closure is
the Markov property of the quantum trace; it is not used here.

Issue #7912.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Knot.FigureEightVolume

open Matrix QOU.Mass.QuantumSl2

section BraidClosure

variable (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ) (hq2 : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0)

/-- The Whitehead braid `σ₁⁻² σ₂ σ₁⁻¹ σ₂` on `V_{m+1}^{⊗3}`. -/
noncomputable def whiteheadBraid : Matrix (Tri m) (Tri m) ℂ :=
  leg12 (rCheckMat σ hσ m m)⁻¹ * leg12 (rCheckMat σ hσ m m)⁻¹ * leg23 (rCheckMat σ hσ m m)
    * leg12 (rCheckMat σ hσ m m)⁻¹ * leg23 (rCheckMat σ hσ m m)

include hq2 hint in
/-- The braid-closure trace of the Whitehead braid in terms of the belt and the clasp. -/
theorem trace_kTri_whiteheadBraid :
    trace (kTri (σ ^ 2) m * whiteheadBraid σ hσ m)
      = ((-1) ^ m * σ ^ (m * (m + 2))) * trace (deltaK (σ ^ 2) m m * beltW σ hσ m * clasp σ hσ m) := by
  have hint' : ∀ i, 0 < i → i ≤ m → qint (σ ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  have hinv : (rCheckMat σ hσ m m)⁻¹ = rotOp (σ ^ 2) m (rCheckMat σ hσ m m) :=
    Matrix.inv_eq_left_inv (rotOp_rCheck_mul_rCheck σ hσ m hq2 hint')
  rw [whiteheadBraid, hinv, trace_kTri_whitehead m σ hσ hq2 fun i h1 h2 => hint i h1 (by omega),
    kk_eq_deltaK m (pow_ne_zero 2 hσ)]

include hq2 hint in
/-- **The sign `(−1)^{N−1}`.** The belt–clasp trace is `(−1)^{N−1} q^{(N²−1)/2}` times the
braid-closure trace of the Whitehead braid. -/
theorem trace_belt_clasp_eq_braidTrace :
    trace (deltaK (σ ^ 2) m m * (beltW σ hσ m * ((σ ^ 2) ^ ((m : ℤ) * (m + 2)) • clasp σ hσ m)))
      = (-1) ^ m * σ ^ (m * (m + 2)) * trace (kTri (σ ^ 2) m * whiteheadBraid σ hσ m) := by
  rw [trace_kTri_whiteheadBraid σ hσ m hq2 hint, Matrix.mul_smul, Matrix.mul_smul, trace_smul,
    smul_eq_mul, ← Matrix.mul_assoc]
  have hz : (σ ^ 2) ^ ((m : ℤ) * (m + 2)) = σ ^ (m * (m + 2)) * σ ^ (m * (m + 2)) := by
    have hk : ((m : ℤ) * (m + 2)) = ((m * (m + 2) : ℕ) : ℤ) := by push_cast; ring
    rw [hk, zpow_natCast]; ring
  have hs : ((-1 : ℂ) ^ m) * (-1) ^ m = 1 := by rw [← mul_pow]; simp
  rw [hz]
  linear_combination (-(σ ^ (m * (m + 2)) * σ ^ (m * (m + 2))
    * trace (deltaK (σ ^ 2) m m * beltW σ hσ m * clasp σ hσ m))) * hs

include hq2 hint in
/-- **The Whitehead link as a braid closure, for every `N`.** van der Veen's formula is the
framing-corrected braid-closure quantum trace of `σ₁⁻² σ₂ σ₁⁻¹ σ₂`, normalised by the unknot:
`vdvWhiteheadLinkJones q N = q^{(N²−1)/2} [N]⁻¹ tr(K^{⊗3} β)`, `N = m + 1`, `q = σ²`. -/
theorem vdvWhiteheadLinkJones_eq_braidTrace :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = σ ^ (m * (m + 2)) * (qint (σ ^ 2) (m + 1))⁻¹
          * trace (kTri (σ ^ 2) m * whiteheadBraid σ hσ m) := by
  rw [vdvWhiteheadLinkJones_eq_trace σ hσ m hq2 hint,
    trace_belt_clasp_eq_braidTrace σ hσ m hq2 hint]
  have hs : ((-1 : ℂ) ^ m) * (-1) ^ m = 1 := by rw [← mul_pow]; simp
  linear_combination ((qint (σ ^ 2) (m + 1))⁻¹ * σ ^ (m * (m + 2))
    * trace (kTri (σ ^ 2) m * whiteheadBraid σ hσ m)) * hs

end BraidClosure

end QOU.Knot.FigureEightVolume
