import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.ParticleInteractions.SilverRatioBetaDecayNull

**Lake-built mirror** of the sibling-stub
`content/quantum-observable-universe/particle-interactions/silver-ratio-beta-decay-null.lean`.

**Silver-ratio β-decay null point**: at $q = 1 \pm \sqrt{2}$ the
categorical β-decay vanishes, the Hecke generator $\sigma$ has
eigenvalues equal to the silver-ratio conjugates (self-referential
fixed point), and the proton/neutron Markov-traces become
categorically indistinguishable.

Derivation: from `prop:neutron-qvalue-symbolic`,
$\Delta(\text{net}) = h(h-2)/2$ where $h = q - q^{-1}$.
Setting $h = 2$ gives $q^2 - 2q - 1 = 0$, roots $q = 1 \pm \sqrt 2$.

The key algebraic identity at $q = 1 + \sqrt 2$:

```
  (q^4 + q^2 + 1) / (q^2 + 1)^2 = 7/8.
```

This file provides the kernel-verified proof.
-/

-- Ref: [manuscript] prop:neutron-qvalue-symbolic
-- Ref: [wenzl1988] doi:10.1007/BF01404457 (Hecke Markov trace)
-- Ref: [hoefsmit1974] (Hoefsmit seminormal forms)

namespace QOU.ParticleInteractions.SilverRatioBetaDecayNull

/-- Hecke skein parameter $h = q - q^{-1}$. -/
noncomputable def heckeSkein (q : ℝ) : ℝ := q - 1/q

/-- Symbolic $\Delta(\text{net}) = h(h-2)/2$ from
`prop:neutron-qvalue-symbolic`. -/
noncomputable def deltaNet (q : ℝ) : ℝ :=
  heckeSkein q * (heckeSkein q - 2) / 2

/-- The silver ratio conjugates $1 \pm \sqrt 2$ are roots of
$q^2 - 2q - 1 = 0$. -/
theorem silver_ratio_polynomial_root :
    let q_plus : ℝ := 1 + Real.sqrt 2
    let q_minus : ℝ := 1 - Real.sqrt 2
    q_plus^2 - 2*q_plus - 1 = 0 ∧ q_minus^2 - 2*q_minus - 1 = 0 := by
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  refine ⟨?_, ?_⟩
  · -- q_plus = 1 + √2 case
    show (1 + Real.sqrt 2)^2 - 2 * (1 + Real.sqrt 2) - 1 = 0
    have h : (1 + Real.sqrt 2)^2 - 2 * (1 + Real.sqrt 2) - 1
              = Real.sqrt 2 * Real.sqrt 2 - 2 := by ring
    rw [hs] at h; linarith
  · -- q_minus = 1 - √2 case
    show (1 - Real.sqrt 2)^2 - 2 * (1 - Real.sqrt 2) - 1 = 0
    have h : (1 - Real.sqrt 2)^2 - 2 * (1 - Real.sqrt 2) - 1
              = Real.sqrt 2 * Real.sqrt 2 - 2 := by ring
    rw [hs] at h; linarith

/-- **β-decay null condition**: $\Delta(\text{net})$ vanishes iff
$h = 0$ or $h = 2$. -/
theorem beta_decay_null_iff_h_zero_or_two (q : ℝ) (_ : q > 0) :
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

/-- **At silver ratio, $b^2$ (Hoefsmit coupling squared) = $7/8$
exactly.**

Derivation: at $q = 1 + \sqrt 2$, $q^2 = 3 + 2\sqrt 2$,
$q^4 = 17 + 12\sqrt 2$.

  - Numerator: $q^4 + q^2 + 1 = 21 + 14\sqrt 2 = 7 (3 + 2\sqrt 2)$.
  - Denominator: $(q^2 + 1)^2 = (4 + 2\sqrt 2)^2 = 24 + 16\sqrt 2 = 8 (3 + 2\sqrt 2)$.
  - Ratio: $7/8$.
-/
theorem hoefsmit_b_squared_at_silver_ratio :
    let q : ℝ := 1 + Real.sqrt 2
    (q^4 + q^2 + 1) / (q^2 + 1)^2 = 7/8 := by
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  show ((1 + Real.sqrt 2)^4 + (1 + Real.sqrt 2)^2 + 1)
        / ((1 + Real.sqrt 2)^2 + 1)^2 = 7/8
  have hq2 : (1 + Real.sqrt 2)^2 = 3 + 2 * Real.sqrt 2 := by
    have h : (1 + Real.sqrt 2)^2
              = 1 + 2 * Real.sqrt 2 + Real.sqrt 2 * Real.sqrt 2 := by ring
    rw [h, hs]; ring
  have hq4 : (1 + Real.sqrt 2)^4 = 17 + 12 * Real.sqrt 2 := by
    have h1 : (1 + Real.sqrt 2)^4 = ((1 + Real.sqrt 2)^2)^2 := by ring
    rw [h1, hq2]
    have h2 : (3 + 2 * Real.sqrt 2 : ℝ)^2
              = 9 + 12 * Real.sqrt 2 + 4 * (Real.sqrt 2 * Real.sqrt 2) := by ring
    rw [h2, hs]; ring
  rw [hq2, hq4]
  have hden : ((3 + 2 * Real.sqrt 2 : ℝ) + 1)^2 = 24 + 16 * Real.sqrt 2 := by
    have h : ((3 + 2 * Real.sqrt 2 : ℝ) + 1)^2
              = 16 + 16 * Real.sqrt 2 + 4 * (Real.sqrt 2 * Real.sqrt 2) := by ring
    rw [h, hs]; ring
  rw [hden]
  have hden_pos : (24 + 16 * Real.sqrt 2 : ℝ) > 0 := by positivity
  rw [div_eq_div_iff (ne_of_gt hden_pos) (by norm_num : (8 : ℝ) ≠ 0)]
  ring

end QOU.ParticleInteractions.SilverRatioBetaDecayNull
