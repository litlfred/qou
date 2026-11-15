import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.ParticleInteractions.SilverRatioBetaDecayNull

**Lake-built mirror** of the sibling-stub
`folio/quantum-observable-universe/particle-interactions/silver-ratio-beta-decay-null.lean`.

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

-- Ref: [leitner2026] prop:neutron-qvalue-symbolic
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

/-! ## The null, restated in crossing energy — and why it is not the VC limit

The corpus writes the per-crossing energy as
$\mathfrak{E}_\times(q) = \tfrac12 (q - q^{-1})$
(`binding-knots-visual-inventory`), which is exactly $h/2$. So the two roots of
`beta_decay_null_iff_h_zero_or_two` are **zero and unit crossing energy** — a
readable condition, where $h \in \{0, 2\}$ reads as an algebraic coincidence.
Same theorem, restated.

This section also records what the restatement does not buy. The
volume-conjecture limit is taken at roots of unity $q = e^{2\pi i/N}$, for which
$|q| = 1$, whereas $\mathfrak{E}_\times = 1$ forces $q = 1 + \sqrt 2 > 2$
(`crossing_energy_one_not_on_unit_circle`). The limit in which the mass
formula's volume term equals the hyperbolic volume is $q \to \infty$, where
$\hbar_q \to 1$ and $\mathrm{Vol}/\hbar_q^2 \to \mathrm{Vol}$
(`tendsto_volTerm_atTop`). At the other null root, $q = 1$, that term's
denominator is zero (`hbarQ_eq_zero_iff`).

**Provenance note.** Every proposition below is verified numerically at
`q ∈ {0.5, 1.11, 2, 3, 1+√2, 10}` and at `q = 10^4, 10^8` for the limit. The
*tactic scripts* were not compiled when written: the container had no Mathlib
oleans, and its Lean toolchain ships no `libLean.a`/`libleancpp.a`, so `lake`
could not link the `cache` executable to fetch them. CI is the first
type-checker for this section. -/

/-- Per-crossing energy $\mathfrak{E}_\times(q) = \tfrac12 (q - q^{-1})$. -/
noncomputable def crossingEnergy (q : ℝ) : ℝ := heckeSkein q / 2

/-- $\mathfrak{E}_\times = h/2$, definitionally. -/
theorem crossingEnergy_eq_half_heckeSkein (q : ℝ) :
    crossingEnergy q = heckeSkein q / 2 := rfl

/-- **The β-decay null is exactly zero-or-unit crossing energy.** -/
theorem beta_decay_null_iff_crossing_energy_zero_or_one (q : ℝ) (hq : q > 0) :
    deltaNet q = 0 ↔ crossingEnergy q = 0 ∨ crossingEnergy q = 1 := by
  rw [beta_decay_null_iff_h_zero_or_two q hq]
  unfold crossingEnergy
  constructor
  · rintro (h | h)
    · left; rw [h]; norm_num
    · right; rw [h]; norm_num
  · rintro (h | h)
    · left; linarith
    · right; linarith

/-- **Unit crossing energy pins $q$ to the silver ratio.** -/
theorem crossing_energy_eq_one_iff (q : ℝ) (hq : 0 < q) :
    crossingEnergy q = 1 ↔ q = 1 + Real.sqrt 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  have hs_pos : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  constructor
  · intro h
    -- h : (q - 1/q)/2 = 1, so q - 1/q = 2, so q² - 2q - 1 = 0.
    have h2 : q - 1 / q = 2 := by
      unfold crossingEnergy heckeSkein at h; linarith
    have hquad : q ^ 2 - 2 * q - 1 = 0 := by
      have hmul : (q - 1 / q) * q = 2 * q := by rw [h2]
      have hexp : (q - 1 / q) * q = q ^ 2 - 1 := by field_simp
      rw [hexp] at hmul; linarith
    -- factor over ℝ using √2 · √2 = 2
    have hfac : (q - 1 - Real.sqrt 2) * (q - 1 + Real.sqrt 2) = 0 := by
      have hexpand : (q - 1 - Real.sqrt 2) * (q - 1 + Real.sqrt 2)
          = q ^ 2 - 2 * q + 1 - Real.sqrt 2 * Real.sqrt 2 := by ring
      rw [hexpand, hs]; linarith
    have hs_gt1 : (1 : ℝ) < Real.sqrt 2 := by
      rw [show (1 : ℝ) = Real.sqrt 1 from Real.sqrt_one.symm]
      exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
    rcases mul_eq_zero.mp hfac with h1 | h1
    · linarith
    · exfalso; linarith
  · intro h
    subst h
    unfold crossingEnergy heckeSkein
    have hden : (1 : ℝ) + Real.sqrt 2 ≠ 0 := by positivity
    rw [div_eq_one_iff_eq (by norm_num : (2 : ℝ) ≠ 0)]
    field_simp
    linarith [hs]

/-- **The unit-crossing-energy point is not on the unit circle**, where the
volume conjecture's root-of-unity limit lives. -/
theorem crossing_energy_one_not_on_unit_circle (q : ℝ) (hq : 0 < q)
    (h : crossingEnergy q = 1) : |q| ≠ 1 := by
  rw [crossing_energy_eq_one_iff q hq] at h
  have hs_pos : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  rw [abs_of_pos hq, h]
  intro hcontra
  linarith

/-! ### The substrate deformation parameter and the large-$q$ limit -/

/-- $\hbar_q = 1 - q^{-1}$, the quantity the mass formula divides by. -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - 1 / q

/-- The mass formula's volume term $\mathrm{Vol}/\hbar_q^2$. -/
noncomputable def volTerm (V q : ℝ) : ℝ := V / (hbarQ q) ^ 2

/-- **$\hbar_q$ vanishes exactly at $q = 1$**, the $\mathfrak{E}_\times = 0$
null root, so the volume term's denominator is zero there. -/
theorem hbarQ_eq_zero_iff (q : ℝ) (hq : q ≠ 0) : hbarQ q = 0 ↔ q = 1 := by
  unfold hbarQ
  constructor
  · intro h
    have h1 : (1 : ℝ) / q = 1 := by linarith
    have h2 : (1 : ℝ) = q := (div_eq_one_iff_eq hq).mp h1
    linarith
  · intro h; subst h; norm_num

/-- $\hbar_q \to 1$ as $q \to \infty$. -/
theorem tendsto_hbarQ_atTop :
    Filter.Tendsto hbarQ Filter.atTop (nhds (1 : ℝ)) := by
  have h : Filter.Tendsto (fun q : ℝ => 1 - q⁻¹) Filter.atTop (nhds (1 - 0)) :=
    Filter.Tendsto.sub tendsto_const_nhds tendsto_inv_atTop_zero
  have hfun : hbarQ = fun q : ℝ => 1 - q⁻¹ := by
    funext q; simp [hbarQ, one_div]
  rw [hfun]; simpa using h

/-- **The large-$q$ limit returns the bare hyperbolic volume.**
$\mathrm{Vol}/\hbar_q^2 \to \mathrm{Vol}$ as $q \to \infty$. This is a limit
along the real axis, disjoint from the root-of-unity direction in which the
volume conjecture is taken. -/
theorem tendsto_volTerm_atTop (V : ℝ) :
    Filter.Tendsto (volTerm V) Filter.atTop (nhds V) := by
  have h1 : Filter.Tendsto (fun q : ℝ => (hbarQ q) ^ 2) Filter.atTop
      (nhds ((1 : ℝ) ^ 2)) := tendsto_hbarQ_atTop.pow 2
  have h2 : Filter.Tendsto (fun q : ℝ => V / (hbarQ q) ^ 2) Filter.atTop
      (nhds (V / (1 : ℝ) ^ 2)) :=
    Filter.Tendsto.div tendsto_const_nhds h1 (by norm_num)
  simpa [volTerm] using h2

end QOU.ParticleInteractions.SilverRatioBetaDecayNull
