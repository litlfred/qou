/-
# The three-scale gauge law of the α_EM B2 Schur scalar — Lean core of K1

Machine-verified K1 core of the merged canonical-scale-ratio probe
(`computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py`, 8/8;
audit `docs/audits/2026-07-25-alpha-em-b2-canonical-scale-ratio.md`).
The Schur scalar `c` of the τ-identification's proportionality
`Pᵀ * G_M * P = c • G_H`
(`TauS5EquivarianceReduction.tauImage_proportional_hodge`, scalar commutant
via `SchurInvariantFormProportional` / `MatrixSchurCommutant`) transforms
under the **three**-scale gauge group

    G_M ↦ λ • G_M,    G_H ↦ μ • G_H,    P ↦ s • P

by `c ↦ (λ·s²/μ)·c` in the transported-form orientation proved here
(`three_scale_gauge_law`), equivalently `c ↦ (λ/(μ·s²))·c` in the probe's
orientation where the intertwiner pulls the *Hodge* Gram back
(`three_scale_gauge_law_probe_orientation` — the literal K1 assertion, the
probe's transform check passing at deviation 5e-60). The three legs:

* `invariantForm_markov_rescale` — **Markov leg**: rescaling the Markov Gram
  `M ↦ λ • M` rescales `c` by `λ`.
* `invariantForm_hodge_rescale` — **Hodge leg**: rescaling the Hodge Gram
  `G ↦ μ • G` (μ ≠ 0) rescales `c` by `μ⁻¹`.
* `three_scale_gauge_law` — the composite with the proved `s²` intertwiner
  covariance (`InvariantFormTransport.invariantForm_pullback_smul`).
* `gauge_ratio_invariant` (over `ℝ`) — the degree-0 corollary the probe's
  route-C I1 rests on: the **ratio** of two Schur scalars under the *same*
  gauge action is gauge-invariant — only ratio-spectrum shapes are intrinsic.

**Honest scope** (STRICT, 2026-07-19 owner ruling respected): the gauge law
*constrains conventions* — two canonical Gram pins can never make the
magnitude of `c` convention-free, because the intertwiner gauge `s²` is a
third independent scale (the audit's O2). It does **not** fix the τ-scale:
that third scale *is* the τ-scale gate, which remains OPEN. Nothing here
constructs the intertwiner, evaluates `c`, or registers a `TauRhoHodgeLift`
instance for physical weights; `1/(8π)` stays a phase-4 identification;
nothing is wired.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur's lemma)
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Real.Basic
import QOU.Archimedean.InvariantFormTransport

namespace QOU.Archimedean.GaugeGroupThreeScale

open Matrix

variable {n : Type*} [Fintype n]

section MarkovLeg

variable {k : Type*} [CommRing k]

/-- **Markov leg of the three-scale gauge law.** If the transported Markov
Gram is proportional to the Hodge Gram, `Pᵀ * M * P = c • G`, then rescaling
the Markov Gram `M ↦ λ • M` rescales the Schur scalar by `λ`:
`Pᵀ * (λ • M) * P = (λ * c) • G`. Purely algebraic — stated over a generic
commutative ring per the base-ring convention (§7c). -/
theorem invariantForm_markov_rescale {P M G : Matrix n n k} {c : k}
    (lam : k) (h : Pᵀ * M * P = c • G) :
    Pᵀ * (lam • M) * P = (lam * c) • G := by
  rw [Matrix.mul_smul, Matrix.smul_mul, h, smul_smul]

end MarkovLeg

section FieldLegs

variable {k : Type*} [Field k]

/-- **Hodge leg of the three-scale gauge law.** If `Pᵀ * M * P = c • G` and
`μ ≠ 0`, then relative to the rescaled Hodge Gram `μ • G` the same
transported form has Schur scalar `c / μ`:
`Pᵀ * M * P = (c / μ) • (μ • G)`. Rescaling the Hodge side rescales `c` by
`μ⁻¹`. -/
theorem invariantForm_hodge_rescale {P M G : Matrix n n k} {c : k}
    (mu : k) (hmu : mu ≠ 0) (h : Pᵀ * M * P = c • G) :
    Pᵀ * M * P = (c / mu) • (mu • G) := by
  rw [smul_smul, div_mul_cancel₀ c hmu]
  exact h

/-- **The composite three-scale gauge law (K1, transported-form
orientation).** Combining the Markov leg, the Hodge leg, and the proved
intertwiner covariance `invariantForm_pullback_smul`: under the full gauge
action `(M, G, P) ↦ (λ • M, μ • G, s • P)` with `μ ≠ 0`,

    (s • P)ᵀ * (λ • M) * (s • P) = (λ * s² / μ * c) • (μ • G),

i.e. the Schur scalar transforms as `c ↦ (λ·s²/μ)·c`. This is the audit's
K1 law: the gauge group has THREE scales, so two canonical Gram pins still
leave the intertwiner gauge `s²` — a fully normalization-free magnitude is
impossible with two pins. The gauge law constrains conventions only; it
does not fix the τ-scale (that third scale is the open τ-scale gate). -/
theorem three_scale_gauge_law {P M G : Matrix n n k} {c : k}
    (lam mu s : k) (hmu : mu ≠ 0) (h : Pᵀ * M * P = c • G) :
    (s • P)ᵀ * (lam • M) * (s • P) = (lam * s ^ 2 / mu * c) • (mu • G) := by
  rw [InvariantFormTransport.invariantForm_pullback_smul,
    invariantForm_markov_rescale lam h, smul_smul, smul_smul]
  congr 1
  -- scalar identity: s² * (λ * c) = λ * s² / μ * c * μ
  rw [mul_right_comm (lam * s ^ 2 / mu) c mu, div_mul_cancel₀ (lam * s ^ 2) hmu,
    mul_left_comm, mul_assoc]

/-- **The composite three-scale gauge law in the probe's orientation
(K1, literal form).** The probe defines `c` with the intertwiner on the
Hodge side, `G_M = c • (Pᵀ * G_H * P)`; there the gauge action
`(G_M, G_H, P) ↦ (λ • G_M, μ • G_H, s • P)` transforms the scalar as
`c ↦ (λ/(μ·s²))·c` — the exact factor asserted (and machine-verified to
5e-60) by `K1_three_scale_gauge_group` in
`alpha_em_b2_canonical_scale_ratio_probe.py`. The two orientations are the
same gauge law: the `s`-exponent flips sign with the side of the pullback. -/
theorem three_scale_gauge_law_probe_orientation {P GH GM : Matrix n n k}
    {c : k} (lam mu s : k) (hmu : mu ≠ 0) (hs : s ≠ 0)
    (h : GM = c • (Pᵀ * GH * P)) :
    lam • GM
      = (lam / (mu * s ^ 2) * c) • ((s • P)ᵀ * (mu • GH) * (s • P)) := by
  have hmus : mu * s ^ 2 ≠ 0 := mul_ne_zero hmu (pow_ne_zero 2 hs)
  rw [InvariantFormTransport.invariantForm_pullback_smul, Matrix.mul_smul,
    Matrix.smul_mul, h]
  simp only [smul_smul]
  congr 1
  -- scalar identity: λ * c = λ/(μ·s²) * c * (s² * μ)
  rw [mul_right_comm (lam / (mu * s ^ 2)) c (s ^ 2 * mu), mul_comm (s ^ 2) mu,
    div_mul_cancel₀ lam hmus]

end FieldLegs

/-- **Gauge invariance of Schur-scalar ratios (route C I1, over `ℝ`).**
Two Schur scalars `c₁, c₂` transported under the *same* three-scale gauge
action pick up the same factor `λ/(μ·s²)`, so their ratio is unchanged:
the ratio is a degree-0 (gauge-invariant) observable. This is the Lean
footing for the probe's route-C I1 reading that only ratio-spectrum shapes
are intrinsic — magnitudes of individual scalars are convention-carrying.
(For an admissible gauge — `λ, μ, s` all nonzero — the common factor is
nonzero and cancels; no `c₂ ≠ 0` hypothesis is needed, since with Mathlib's
division convention the identity also holds degenerately. The probe's
route-C instance has `c₂ ≠ 0`.) -/
theorem gauge_ratio_invariant {lam mu s c₁ c₂ : ℝ}
    (hlam : lam ≠ 0) (hmu : mu ≠ 0) (hs : s ≠ 0) :
    (lam / (mu * s ^ 2) * c₁) / (lam / (mu * s ^ 2) * c₂) = c₁ / c₂ := by
  have hg : lam / (mu * s ^ 2) ≠ 0 :=
    div_ne_zero hlam (mul_ne_zero hmu (pow_ne_zero 2 hs))
  rw [mul_div_mul_left c₁ c₂ hg]

end QOU.Archimedean.GaugeGroupThreeScale
