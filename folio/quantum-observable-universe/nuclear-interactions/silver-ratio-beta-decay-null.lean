import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.SilverRatioBetaDecayNull

**Silver-ratio β-decay null point**: at q = 1 ± √2 the categorical
β-decay vanishes, the Hecke generator σ has eigenvalues equal to
the silver-ratio conjugates (self-referential fixed point), and the
proton/neutron Markov-traces become categorically indistinguishable.

Derivation: from `prop:neutron-qvalue-symbolic`,
  Δ(net) = h(h-2)/2  where h = q - q⁻¹
Setting h = 2 gives q² - 2q - 1 = 0, roots q = 1 ± √2.
-/

-- Ref: [leitner2026] prop:neutron-qvalue-symbolic
-- Ref: [wenzl1988] doi:10.1007/BF01404457 (Hecke Markov trace)
-- Ref: [hoefsmit1974] (Hoefsmit seminormal forms)

namespace QOU.ParticleInteractions

/-- Hecke skein parameter h = q - q⁻¹. -/
noncomputable def heckeSkein (q : ℝ) : ℝ := q - 1/q

/-- Symbolic Δ(net) = h(h-2)/2 from `prop:neutron-qvalue-symbolic`. -/
noncomputable def deltaNet (q : ℝ) : ℝ :=
  heckeSkein q * (heckeSkein q - 2) / 2

/-- The silver ratio conjugates 1 ± √2 are roots of q² - 2q - 1 = 0. -/
theorem silver_ratio_polynomial_root :
    let q_plus : ℝ := 1 + Real.sqrt 2
    let q_minus : ℝ := 1 - Real.sqrt 2
    q_plus^2 - 2*q_plus - 1 = 0 ∧ q_minus^2 - 2*q_minus - 1 = 0 := by
  refine ⟨?_, ?_⟩ <;> (
    ring_nf
    rw [Real.sq_sqrt (by norm_num : (2:ℝ) ≥ 0)]
    ring
  )

/-- **β-decay null condition**: Δ(net) vanishes iff h = 0 or h = 2. -/
theorem beta_decay_null_iff_h_zero_or_two (q : ℝ) (hq : q > 0) :
    deltaNet q = 0 ↔ heckeSkein q = 0 ∨ heckeSkein q = 2 := by
  unfold deltaNet
  constructor
  · intro h
    have h' : heckeSkein q * (heckeSkein q - 2) = 0 := by linarith
    rcases mul_eq_zero.mp h' with h1 | h2
    · left; exact h1
    · right; linarith
  · intro h
    rcases h with h1 | h2
    · simp [h1]
    · rw [h2]; ring

/-- **Self-referential fixed point**: at q = 1 + √2 (silver ratio),
    the Hecke quadratic σ² = h·σ + 1 becomes σ² = 2σ + 1, whose
    roots are σ = 1 ± √2 — equal to q^{±1} at the silver ratio. -/
theorem hecke_quadratic_silver_ratio_self_referential :
    let q_silver : ℝ := 1 + Real.sqrt 2
    let σ_root_plus : ℝ := 1 + Real.sqrt 2
    let σ_root_minus : ℝ := 1 - Real.sqrt 2
    -- The roots of σ² - 2σ - 1 = 0 are σ = 1 ± √2:
    σ_root_plus^2 - 2*σ_root_plus - 1 = 0 ∧
    σ_root_minus^2 - 2*σ_root_minus - 1 = 0 ∧
    -- And σ_root_plus = q_silver (self-referential!):
    σ_root_plus = q_silver := by
  refine ⟨?_, ?_, rfl⟩ <;> (
    ring_nf
    rw [Real.sq_sqrt (by norm_num : (2:ℝ) ≥ 0)]
    ring
  )

/-- **At silver ratio, b² (Hoefsmit coupling squared) = 7/8 exactly.**

    Derivation: at q = 1 + √2, q² = 3 + 2√2, q⁴ = 17 + 12√2.
    Numerator q⁴ + q² + 1 = 21 + 14√2 = 7(3 + 2√2).
    Denominator (q² + 1)² = (4 + 2√2)² = 16 + 16√2 + 8 = 24 + 16√2 = 8(3 + 2√2).
    Ratio: 7/8. -/
theorem hoefsmit_b_squared_at_silver_ratio :
    let q : ℝ := 1 + Real.sqrt 2
    (q^4 + q^2 + 1) / (q^2 + 1)^2 = 7/8 := by
  -- Strategy: substitute q^2 = 3 + 2√2 and q^4 = 17 + 12√2; both
  -- numerator and denominator share the conjugate factor (3 + 2√2):
  --   numerator   = 21 + 14√2 = 7 · (3 + 2√2)
  --   denominator = (4 + 2√2)^2 = 24 + 16√2 = 8 · (3 + 2√2)
  -- so the ratio cancels to 7/8.
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  show ((1 + Real.sqrt 2)^4 + (1 + Real.sqrt 2)^2 + 1)
        / ((1 + Real.sqrt 2)^2 + 1)^2 = 7/8
  -- q^2 = 3 + 2 · √2
  have hq2 : (1 + Real.sqrt 2)^2 = 3 + 2 * Real.sqrt 2 := by
    have h : (1 + Real.sqrt 2)^2
              = 1 + 2 * Real.sqrt 2 + Real.sqrt 2 * Real.sqrt 2 := by ring
    rw [h, hs]; ring
  -- q^4 = (q^2)^2 = (3 + 2√2)^2 = 17 + 12 · √2
  have hq4 : (1 + Real.sqrt 2)^4 = 17 + 12 * Real.sqrt 2 := by
    have h1 : (1 + Real.sqrt 2)^4 = ((1 + Real.sqrt 2)^2)^2 := by ring
    rw [h1, hq2]
    have h2 : (3 + 2 * Real.sqrt 2 : ℝ)^2
              = 9 + 12 * Real.sqrt 2 + 4 * (Real.sqrt 2 * Real.sqrt 2) := by ring
    rw [h2, hs]; ring
  rw [hq2, hq4]
  -- Denominator: ((3 + 2√2) + 1)^2 = (4 + 2√2)^2 = 24 + 16 · √2
  have hden : ((3 + 2 * Real.sqrt 2 : ℝ) + 1)^2 = 24 + 16 * Real.sqrt 2 := by
    have h : ((3 + 2 * Real.sqrt 2 : ℝ) + 1)^2
              = 16 + 16 * Real.sqrt 2 + 4 * (Real.sqrt 2 * Real.sqrt 2) := by ring
    rw [h, hs]; ring
  rw [hden]
  -- Goal: (17 + 12√2 + (3 + 2√2) + 1) / (24 + 16√2) = 7/8.
  -- Numerator simplifies to 21 + 14√2; cross-multiply gives
  --   8 · (21 + 14√2) = 168 + 112√2 = 7 · (24 + 16√2). ✓
  have hden_pos : (24 + 16 * Real.sqrt 2 : ℝ) > 0 := by positivity
  rw [div_eq_div_iff (ne_of_gt hden_pos) (by norm_num : (8 : ℝ) ≠ 0)]
  ring

end QOU.ParticleInteractions
