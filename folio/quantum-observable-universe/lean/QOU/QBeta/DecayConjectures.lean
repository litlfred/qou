import QOU.QBeta.FlavourWeightSplit

/-!
# Q_β on the γγ base: the three inputs that are not derived, stated as conjectures

Owner directive 2026-11-20 (Carl): *"Rulings are only temporary conjectures. We need to formalize
first always and then try to Lean prove and derive."* Bean `qou-99qc`.

The scored formula `Q_β = |ε(Δ)|·E₀` has three factors, and none of them is derived
(`docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md`, PR #8594):

| factor | was | here |
|---|---|---|
| the decay functional `ε` | owner ruling 2026-09-08 (Markov trace at `z_D`) and 2026-11-20 (its `T³` split) | `DecayFunctionalIsWeightTrace` |
| the nucleon elements | owner ruling 2026-09-08 (γγ + confinement SDP); `V³` for both nucleons is PR #8564's selection result on `H₃` | `NucleonElementsAreGammaGammaBase` |
| the energy scale `E₀` | posited (`m_e/(q(q−1))`, tower-summed by the 2026-09-03 ruling; bean `qou-y3bm`) | `DecayEnergyScale` |

Each is a **primary conjecture** (§3b-tax): a content-bearing `Prop` class with no instance.
`qbeta_eq_of_conjectures` then DERIVES the value from them, using the proved closed form
`FlavourWeightSplit.epsFlavour_V3_eq`. Nothing here asserts that any of the three holds.

## What each conjecture would need, to become a theorem

* `DecayFunctionalIsWeightTrace`: show that the β-decay amplitude functional — the weak vertex
  acting between the two weight spaces (`docs/audits/2026-11-15-one-sided-weak-vertex.md`:
  `q^{∓1}J`, placement open) — reduces to `ε_n − ε_p` with `ε_N` the `U_q(sl₂)` quantum trace on
  `W_N` normalised by `[2]³`. The normalisation itself is proved (the whole-space trace is the
  `z_D` Markov trace); the identification of the decay functional with it is the open step.
* `NucleonElementsAreGammaGammaBase`: transport PR #8564's `frobeniusSelected_ten_unique`
  (stated on the Hoefsmit `H₃` representation, `V^k`, `k ≤ 10`) to the weight-space matrices of
  `NucleonWeightSpaceTwoTerm`, and remove its bound `k ≤ 10`. With the four-term chiral photon,
  `V³` is the two-photon product only at the eigenvalue colour weights `(0,0,qh)`, `(0,0,−q⁻¹h)`.
  Varying the photon weights does NOT produce a proton/neutron difference in the plain trace:
  `photonPair_trace_n_eq_p` below proves `tr_n = tr_p` for every pair of photons, with all six
  weights free. (Corrected 2026-11-21: this note previously said nucleon-dependent `φ₀, φ₁` were
  the missing input; that was wrong.) The symmetry breakers are the Cartan `K`-weighting (the
  first term of the two-term Lagrangian trace, `CategoricalLagrangianTwoTermBridge`) and the
  quark-charge insertion `Q_iQ_j` (its matter term). This file's `ε` carries only the first.
* `DecayEnergyScale`: derive `E₀` from the mass channel by energy conservation. The audit
  (§3) records that the mass channel's scale per unit trace is `945.76 MeV`, not `E₀ ≈ 4.2 MeV`,
  so the decay `Δ` is not yet the difference of the mass-channel objects.

-- Ref: [leitner2026] docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md
-- Ref: [leitner2026] docs/audits/2026-11-20-qbeta-flavour-weight-split.md
-/

namespace QOU.QBeta.DecayConjectures

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.QBeta.FlavourWeightSplit

section Generic

variable {R : Type*} [Field R]

/-- **The plain trace cannot tell the proton from the neutron, whatever the photon.**
For the four-term photon `γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` and any second photon
`γ(ψ₀,ψ₁,ψ₀₁)`, the trace of the photon pair on the neutron weight space `W_n` equals the trace
on the proton weight space `W_p`, for all six weights. The neutron representation is the proton
one with `σ₀ ↔ σ₁`, which is an inner automorphism of `H₃`, so no photon weight separates them. -/
theorem photonPair_trace_n_eq_p (q : R) (hq : q ≠ 0) (φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R) :
    trace ((1 + φ₀ • B₁ q + φ₁ • B₂ q + φ₀₁ • (B₁ q * B₂Inv q)) *
        (1 + ψ₀ • B₁ q + ψ₁ • B₂ q + ψ₀₁ • (B₁ q * B₂Inv q))) =
      trace ((1 + φ₀ • A₁ q + φ₁ • A₂ q + φ₀₁ • (A₁ q * A₂Inv q)) *
        (1 + ψ₀ • A₁ q + ψ₁ • A₂ q + ψ₀₁ • (A₁ q * A₂Inv q))) := by
  simp only [B₁, B₂, A₁, A₂, B₂Inv, A₂Inv]
  simp [Matrix.trace, Fin.sum_univ_three, Matrix.mul_apply, Matrix.add_apply,
    Matrix.one_apply]
  field_simp
  ring

/-- **Conjecture C1 (was a ruling).** The decay functional, evaluated on a proton element `Mp`
(acting on `W_p`) and a neutron element `Mn` (acting on `W_n`), is the difference of the two
`T³` components of the `U_q(sl₂)` quantum trace normalised by `[2]³`. -/
class DecayFunctionalIsWeightTrace (q : R)
    (ε : Matrix (Fin 3) (Fin 3) R → Matrix (Fin 3) (Fin 3) R → R) : Prop where
  eq_weight_trace : ∀ Mp Mn, ε Mp Mn = epsN q Mn - epsP q Mp

/-- **Conjecture C2 (was a ruling).** The proton and neutron elements are the γγ base `V³` on
their weight spaces. -/
class NucleonElementsAreGammaGammaBase (q : R) (Mp Mn : Matrix (Fin 3) (Fin 3) R) : Prop where
  proton_eq : Mp = borromeanV3A q
  neutron_eq : Mn = borromeanV3B q

/-- Under C1 and C2 the decay functional takes the proved closed form. -/
theorem decayFunctional_eq_fV3 (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (ε : Matrix (Fin 3) (Fin 3) R → Matrix (Fin 3) (Fin 3) R → R)
    (Mp Mn : Matrix (Fin 3) (Fin 3) R)
    [DecayFunctionalIsWeightTrace q ε] [NucleonElementsAreGammaGammaBase q Mp Mn] :
    ε Mp Mn = fV3 q := by
  rw [DecayFunctionalIsWeightTrace.eq_weight_trace (q := q) (ε := ε) Mp Mn,
    NucleonElementsAreGammaGammaBase.proton_eq (q := q) (Mp := Mp) (Mn := Mn),
    NucleonElementsAreGammaGammaBase.neutron_eq (q := q) (Mp := Mp) (Mn := Mn)]
  exact epsFlavour_V3_eq q hq hq2

end Generic

section Archimedean

/-- **Conjecture C3 (posited scale).** The β-decay Q-value is the absolute value of the decay
functional times a positive energy scale `E₀`. -/
class DecayEnergyScale (E₀ Qβ ε : ℝ) : Prop where
  scale_pos : 0 < E₀
  qbeta_eq : Qβ = |ε| * E₀

/-- **`Q_β` derived from the three conjectures.** Given C1–C3, `Q_β = |f(q)|·E₀` with
`f(q) = (q²−1)P(q)/(q⁴(q²+1)³)` the proved closed form of the flavour split on `V³`. -/
theorem qbeta_eq_of_conjectures (q : ℝ) (hq : q ≠ 0)
    (ε : Matrix (Fin 3) (Fin 3) ℝ → Matrix (Fin 3) (Fin 3) ℝ → ℝ)
    (Mp Mn : Matrix (Fin 3) (Fin 3) ℝ) (E₀ Qβ : ℝ)
    [DecayFunctionalIsWeightTrace q ε] [NucleonElementsAreGammaGammaBase q Mp Mn]
    [DecayEnergyScale E₀ Qβ (ε Mp Mn)] :
    Qβ = |fV3 q| * E₀ := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [DecayEnergyScale.qbeta_eq (E₀ := E₀) (Qβ := Qβ) (ε := ε Mp Mn),
    decayFunctional_eq_fV3 q hq hq2 ε Mp Mn]

/-- Under C1–C3, on the selection range `1 < q ≤ 23/20`, the decay is not forbidden:
`Q_β > 0`. (Contrast PR #8564: with the same element for both nucleons and no `T³` split,
`Q_β = 0`.) -/
theorem qbeta_pos_of_conjectures {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (ε : Matrix (Fin 3) (Fin 3) ℝ → Matrix (Fin 3) (Fin 3) ℝ → ℝ)
    (Mp Mn : Matrix (Fin 3) (Fin 3) ℝ) (E₀ Qβ : ℝ)
    [DecayFunctionalIsWeightTrace q ε] [NucleonElementsAreGammaGammaBase q Mp Mn]
    [h3 : DecayEnergyScale E₀ Qβ (ε Mp Mn)] :
    0 < Qβ := by
  have hq0 : q ≠ 0 := by positivity
  have hsq : q ^ 2 + 1 ≠ 0 := by positivity
  rw [qbeta_eq_of_conjectures q hq0 ε Mp Mn E₀ Qβ]
  have hf : fV3 q ≠ 0 := by
    rw [← epsFlavour_V3_eq q hq0 hsq]
    exact epsFlavour_V3_ne_zero hq1 hq2
  exact mul_pos (abs_pos.mpr hf) h3.scale_pos

end Archimedean

end QOU.QBeta.DecayConjectures
