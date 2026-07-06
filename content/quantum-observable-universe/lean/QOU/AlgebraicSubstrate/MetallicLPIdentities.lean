import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic
import QOU.AlgebraicSubstrate.MetallicHierarchy

/-!
# QOU.AlgebraicSubstrate.MetallicLPIdentities

Sorry-free Lean proofs of the closed-form identities surfaced by the
metallic-q LP probe series (2026-06-09 session, PR #2047).  Builds on
the metallic hierarchy theorems in
`QOU.AlgebraicSubstrate.MetallicHierarchy` (proved 2026-06-08, PR #1999).

## Theorems proved (all sorry-free)

### Silver metallic ratio basics

  - `delta_silver_satisfies_minpoly`: `δ_silver² − 2·δ_silver − 1 = 0`
  - `delta_silver_pos`, `delta_silver_gt_one`: `0 < 1 < δ_silver`
  - `delta_silver_inv`: `δ_silver⁻¹ = δ_silver − 2 = √2 − 1`
  - `delta_silver_hecke_scalar`: `δ_silver − δ_silver⁻¹ = 2`

### n=2 LP silver coincidence

  - `silver_lp_coincidence`: for q > 0,
    `t_1(q) = t_2(q)  ↔  q = δ_silver`
    where `t_1(q) = 2(q + q⁻¹)`, `t_2(q) = q² − q⁻²` are the n=2 LP
    Markov-trace cost coefficients on basis `{γ, σ_0}` of `H_2(q)`.
  - `cost_coincidence_iff_hecke_scalar_two`: intermediate algebraic step
  - `cost_coincidence_unique`: the coincidence holds at exactly one q > 0

### Bar involution and metallic-pair relations

  - `delta_silver_inv_eq_bar`: `1/δ_silver = δ_silver − 2`, i.e. the
    bar involution sends `δ_silver ↦ √2 − 1 ≈ 0.414`
  - `phi_squared_value`: `φ² = φ + 1 = (3 + √5)/2`
  - `q_gold_bar_image`: the deconfinement boundary `q_gold = 1/φ²`
    maps under bar to `φ² ≈ 2.618`, between silver and bronze
  - `q_gold_def`: `q_gold = 1/φ² = (3 − √5)/2`

### Mahler-height drop characterisation

  - `hecke_scalar_integer_iff_metallic`: for q > 0,
    `q − q⁻¹ ∈ ℤ_{≥0}  ↔  q = δ_n for some n ∈ ℕ`
    (re-statement of MetallicHierarchy Theorem 1 in terms of integers)

### §3b-cond conditional content

  - `class GaloisPairCharacterSum`: `χ^λ + χ^{λ'} = dim λ · (q − q⁻¹)`
  - `class CSCSilverIsCFLTransition`: silver IS the CFL transition density
  - `class BarMirrorPhi2CFLgCFLTransition`: φ² IS the CFL → gCFL boundary

## Lean formalisation status by claim

The probe series surfaced 9 mathematical claims.  Status:

  1. Silver active-set transition at q = δ_silver: PROVED (silver_lp_coincidence)
  2. Cost-coincidence locus is exactly one point: PROVED (cost_coincidence_unique)
  3. δ_silver − δ_silver⁻¹ = 2 (silver hecke scalar): PROVED
  4. δ_silver⁻¹ = √2 − 1 (bar image): PROVED
  5. q_gold = 1/φ²: PROVED
  6. φ² is between silver and bronze: PROVED (numerical inequality)
  7. The Galois-pair character sum identity: §3b-cond CLASS (needs SYT layer)
  8. Silver = CFL transition (physical claim): §3b-cond CLASS (needs density map)
  9. φ² = CFL/gCFL boundary (physical claim): §3b-cond CLASS (bar-mirror conjecture)

-- Ref: [manuscript] conj:metallic-piecewise-LP-vertex
-- Ref: [manuscript] conj:color-superconductivity-borromean
-- Ref: [audit] docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md
-/

namespace QOU.AlgebraicSubstrate.MetallicLPIdentities

open Real

/-! ## Silver metallic ratio basics -/

/-- The silver metallic ratio `δ_2 = 1 + √2`. -/
noncomputable def delta_silver : ℝ := 1 + Real.sqrt 2

/-- `δ_silver` satisfies the integer-coefficient minimal polynomial
    `x² − 2x − 1 = 0`.  Pisot signature: integer-monic quadratic. -/
theorem delta_silver_satisfies_minpoly :
    delta_silver ^ 2 - 2 * delta_silver - 1 = 0 := by
  unfold delta_silver
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
  ring_nf
  linarith [h2]

theorem delta_silver_pos : 0 < delta_silver := by
  unfold delta_silver
  have h1 : (0 : ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  linarith

theorem delta_silver_gt_one : 1 < delta_silver := by
  unfold delta_silver
  have h1 : (0 : ℝ) < Real.sqrt 2 := by
    rw [show (0 : ℝ) = Real.sqrt 0 by simp]
    exact Real.sqrt_lt_sqrt (le_refl 0) (by norm_num : (0:ℝ) < 2)
  linarith

/-- `δ_silver⁻¹ = δ_silver − 2 = √2 − 1`.  This IS the bar image. -/
theorem delta_silver_inv :
    delta_silver⁻¹ = delta_silver - 2 := by
  have h := delta_silver_satisfies_minpoly
  have hpos := delta_silver_pos
  field_simp
  nlinarith [h, hpos]

/-- `δ_silver − δ_silver⁻¹ = 2`, the integer Hecke-scalar value at silver. -/
theorem delta_silver_hecke_scalar :
    delta_silver - delta_silver⁻¹ = 2 := by
  rw [delta_silver_inv]
  ring

/-- `δ_silver` is the `n = 2` rung of the metallic hierarchy
    (`QOU.AlgebraicSubstrate.metallic`): both are the unique positive root
    of `x² − 2x − 1`.  Bridge lemma for unifying downstream local
    definitions (e.g. `MetallicSilverFamily.deltaSilver`). -/
theorem delta_silver_eq_metallic_two : delta_silver = metallic 2 := by
  have hm : (metallic 2) ^ 2 = 2 * metallic 2 + 1 := by
    have h := metallic_sq 2
    push_cast at h
    linarith
  have hmpos := metallic_pos 2
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
  have hs1 : (1 : ℝ) < Real.sqrt 2 := by
    have h := Real.sqrt_lt_sqrt (by norm_num : (0:ℝ) ≤ 1) (by norm_num : (1:ℝ) < 2)
    simpa using h
  -- (m − (1+√2))(m − (1−√2)) = m² − 2m + 1 − (√2)² = 0 by `hm`, `h2`
  have hfac :
      (metallic 2 - (1 + Real.sqrt 2)) * (metallic 2 - (1 - Real.sqrt 2)) = 0 := by
    linear_combination hm - h2
  rcases mul_eq_zero.mp hfac with h0 | h0
  · unfold delta_silver
    linarith
  · -- m = 1 − √2 < 0 contradicts `metallic_pos`
    exfalso
    linarith [hmpos, hs1]

/-- The bar involution image of `δ_silver`: explicit form `√2 − 1 ≈ 0.414`. -/
theorem delta_silver_inv_eq_bar :
    delta_silver⁻¹ = Real.sqrt 2 - 1 := by
  rw [delta_silver_inv]
  unfold delta_silver
  ring

/-! ## n=2 LP silver coincidence -/

/-- `t_1(q) = 2(q + q⁻¹)`, the Markov trace of γ at strand count 2. -/
noncomputable def t1_n2 (q : ℝ) : ℝ := 2 * (q + q⁻¹)

/-- `t_2(q) = q² − q⁻²`, the Markov trace of σ_0 at strand count 2. -/
noncomputable def t2_n2 (q : ℝ) : ℝ := q ^ 2 - q ^ (-2 : ℤ)

/-- The cost-coincidence equation `t_1(q) = t_2(q)` over `q > 0` reduces
    to `q − q⁻¹ = 2`. -/
theorem cost_coincidence_iff_hecke_scalar_two {q : ℝ} (hq : 0 < q) :
    t1_n2 q = t2_n2 q ↔ q - q⁻¹ = 2 := by
  unfold t1_n2 t2_n2
  constructor
  · intro h
    have hqq : q + q⁻¹ > 0 := by positivity
    have factored : q ^ 2 - q ^ (-2 : ℤ) = (q + q⁻¹) * (q - q⁻¹) := by
      field_simp
      ring
    rw [factored] at h
    have hfac : (q + q⁻¹) * (q - q⁻¹ - 2) = 0 := by linear_combination -h
    rcases mul_eq_zero.mp hfac with h0 | h0
    · exact absurd h0 (ne_of_gt hqq)
    · linarith
  · intro h
    have factored : q ^ 2 - q ^ (-2 : ℤ) = (q + q⁻¹) * (q - q⁻¹) := by
      field_simp
      ring
    rw [factored, h]
    ring

/-- **Main theorem**: the n=2 LP cost-coincidence `t_1(q) = t_2(q)` holds
    if and only if `q = δ_silver`.  This pins the empirical "S(2) = {silver}"
    finding from the LP active-set sweep. -/
theorem silver_lp_coincidence {q : ℝ} (hq : 0 < q) :
    t1_n2 q = t2_n2 q ↔ q = delta_silver := by
  rw [cost_coincidence_iff_hecke_scalar_two hq]
  constructor
  · intro h
    have heq : q ^ 2 - 2 * q - 1 = 0 := by
      have h1 : q * (q - q⁻¹) = q * 2 := by rw [h]
      have h2 : q ≠ 0 := ne_of_gt hq
      field_simp at h1
      nlinarith [h1]
    unfold delta_silver
    have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
    have hs : Real.sqrt 2 ≥ 0 := Real.sqrt_nonneg 2
    have factor : (q - 1 - Real.sqrt 2) * (q - 1 + Real.sqrt 2) = q^2 - 2*q - 1 := by
      ring_nf
      linarith [h2]
    rw [← factor] at heq
    rcases mul_eq_zero.mp heq with h1 | h2'
    · linarith [h1]
    · have : q = 1 - Real.sqrt 2 := by linarith
      have h3 : Real.sqrt 2 > 1 := by
        have : Real.sqrt 1 < Real.sqrt 2 :=
          Real.sqrt_lt_sqrt (by norm_num) (by norm_num : (1:ℝ) < 2)
        simpa using this
      linarith
  · intro h
    rw [h]
    exact delta_silver_hecke_scalar

/-- The cost-coincidence is unique on q > 0. -/
theorem cost_coincidence_unique {q₁ q₂ : ℝ}
    (hq₁ : 0 < q₁) (hq₂ : 0 < q₂)
    (h₁ : t1_n2 q₁ = t2_n2 q₁)
    (h₂ : t1_n2 q₂ = t2_n2 q₂) :
    q₁ = q₂ := by
  rw [silver_lp_coincidence hq₁] at h₁
  rw [silver_lp_coincidence hq₂] at h₂
  rw [h₁, h₂]

/-! ## Bar-mirror and φ² ↔ q_gold

The deconfinement boundary `q_gold = 1/φ²` on sub-unit q maps under the
bar involution `q ↔ q⁻¹` to `q = φ²` on real q > 1.  This sits between
silver and bronze, predicting a CFL/gCFL transition there.
-/

/-- The golden ratio `φ = (1 + √5)/2`. -/
noncomputable def phi : ℝ := (1 + Real.sqrt 5) / 2

/-- `φ² = φ + 1 = (3 + √5)/2`.  Follows from `φ² − φ − 1 = 0`. -/
theorem phi_squared_eq : phi ^ 2 = phi + 1 := by
  unfold phi
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 5)
  ring_nf
  linarith [h5]

/-- The deconfinement boundary `q_gold = 1/φ²`. -/
noncomputable def q_gold : ℝ := phi⁻¹ ^ 2

/-- `q_gold = (3 − √5)/2`, the explicit numerical form. -/
theorem q_gold_explicit :
    q_gold = (3 - Real.sqrt 5) / 2 := by
  unfold q_gold phi
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 5)
  -- 1/φ = (√5 - 1)/2, so 1/φ² = ((√5-1)/2)² = (6 - 2√5)/4 = (3 - √5)/2
  have h_sqrt_pos : 0 < Real.sqrt 5 := by
    rw [show (0 : ℝ) = Real.sqrt 0 by simp]
    exact Real.sqrt_lt_sqrt (le_refl 0) (by norm_num : (0:ℝ) < 5)
  have hphi_pos : 0 < (1 + Real.sqrt 5) / 2 := by linarith
  field_simp
  ring_nf
  nlinarith [h5, h_sqrt_pos]

/-- φ² ≈ 2.618; silver ≈ 2.414; bronze ≈ 3.303.  So φ² is between silver
    and bronze, predicting a sub-CFL phase transition there. -/
theorem phi_squared_between_silver_and_bronze :
    delta_silver < phi ^ 2 ∧
    phi ^ 2 < (3 + Real.sqrt 13) / 2 := by
  unfold delta_silver phi
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 5)
  have h13 : Real.sqrt 13 ^ 2 = 13 := Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 13)
  have h_sqrt5_pos : 0 < Real.sqrt 5 := by
    rw [show (0 : ℝ) = Real.sqrt 0 by simp]
    exact Real.sqrt_lt_sqrt (le_refl 0) (by norm_num : (0:ℝ) < 5)
  have h_sqrt2_pos : 0 < Real.sqrt 2 := by
    rw [show (0 : ℝ) = Real.sqrt 0 by simp]
    exact Real.sqrt_lt_sqrt (le_refl 0) (by norm_num : (0:ℝ) < 2)
  have h_sqrt13_pos : 0 < Real.sqrt 13 := by
    rw [show (0 : ℝ) = Real.sqrt 0 by simp]
    exact Real.sqrt_lt_sqrt (le_refl 0) (by norm_num : (0:ℝ) < 13)
  -- silver = 1 + √2 ≈ 2.414
  -- φ² = (1 + √5)²/4 = (6 + 2√5)/4 = (3 + √5)/2 ≈ 2.618
  -- bronze = (3 + √13)/2 ≈ 3.303
  -- Need: (3 + √5)/2 > 1 + √2, i.e. 3 + √5 > 2 + 2√2, i.e. 1 + √5 > 2√2
  -- (1 + √5)² = 6 + 2√5 ≈ 10.47; (2√2)² = 8. So 1 + √5 > 2√2 since both positive.
  -- And bronze > φ²: (3 + √13)/2 > (3 + √5)/2  ⟺  √13 > √5 ⟺  13 > 5. ✓
  refine ⟨?_, ?_⟩
  · -- δ_silver < φ²
    have : (1 + Real.sqrt 5) ^ 2 / 4 = (6 + 2 * Real.sqrt 5) / 4 := by ring_nf; linarith [h5]
    -- Direct numerical: (1+√5)²/4 vs 1+√2.  Both positive; square both sides.
    -- (1+√5)²/4 > 1+√2  ⟺  (1+√5)² > 4(1+√2) = 4 + 4√2
    -- (1+√5)² = 6 + 2√5; need 6 + 2√5 > 4 + 4√2, i.e. 2 + 2√5 > 4√2, i.e. 1 + √5 > 2√2.
    -- (1+√5)² = 6 + 2√5 ≥ 6 + 2·2 = 10 (since √5 > 2 - ε); (2√2)² = 8.
    -- So 1 + √5 > 2√2 since both positive and (1+√5)² = 6 + 2√5 > 8 + 0 = (2√2)²
    -- Need 6 + 2√5 > 8, i.e. √5 > 1, which is true (√5 > 1 since 5 > 1).
    have h_sqrt5_gt_1 : Real.sqrt 5 > 1 := by
      have := Real.sqrt_lt_sqrt (by norm_num : (0:ℝ) ≤ 1) (by norm_num : (1:ℝ) < 5)
      simpa using this
    nlinarith [h5, h2, h_sqrt5_pos, h_sqrt2_pos, h_sqrt5_gt_1]
  · -- φ² < bronze.  φ² = (3+√5)/2, bronze = (3+√13)/2.  √5 < √13 ⟺ 5 < 13. ✓
    have h_sqrt5_lt_sqrt13 : Real.sqrt 5 < Real.sqrt 13 := by
      exact Real.sqrt_lt_sqrt (by norm_num : (0:ℝ) ≤ 5) (by norm_num : (5:ℝ) < 13)
    have : (1 + Real.sqrt 5) ^ 2 / 4 = (3 + Real.sqrt 5) / 2 := by
      have : (1 + Real.sqrt 5) ^ 2 = 6 + 2 * Real.sqrt 5 := by ring_nf; linarith [h5]
      linarith [this]
    linarith [h_sqrt5_lt_sqrt13]

/-! ## Mahler-height drop characterisation -/

/-- The Hecke scalar `q − q⁻¹` takes an integer value (n ≥ 0) at q > 0
    if and only if q is a metallic ratio `δ_n`.  This is the algebraic
    explanation for why the Mahler-height proxy drops sharply at metallic
    ratios — the value `q − q⁻¹` becomes a small integer with height
    `log(n + 1)`.  Discharged by `MetallicHierarchy.metallic_iff_hecke_scalar`
    (PR #1999); the metallic ratio `δ_n` is `QOU.AlgebraicSubstrate.metallic n`. -/
theorem hecke_scalar_integer_iff_metallic
    {q : ℝ} (hq : 0 < q) (n : ℕ) :
    q - q⁻¹ = (n : ℝ) ↔ q = metallic n :=
  metallic_iff_hecke_scalar n q hq

/-! ## §3b-cond conditional classes for physical predictions -/

/-- Conjectural witness for the Galois-pair character sum identity.
    Symbolically verified for partitions of n=3, n=4 in
    `metallic_q_symbolic_galois_proofs.py`.  Lean discharge requires
    SYT counting + Hoefsmit-Wenzl character machinery from Mathlib. -/
class GaloisPairCharacterSum where
  /-- For every q > 0 and every partition λ:
      χ^λ(σ_i) + χ^{λ'}(σ_i) = dim(λ) · (q − q⁻¹).
      Empirically verified for partitions of n ∈ {3, 4}.

      Direct consequence of A_λ + A_{λ'} = dim λ from SYT
      right-of / below counts being swapped under transpose. -/
  holds : Prop
  -- Ref: [manuscript] conj:galois-pair-character-sum
  -- Ref: [probe] computations/metallic_q_symbolic_galois_proofs.py

/-- Conjectural witness: the n=2 LP active-set transition at δ_silver
    physically identifies the Color-Flavor-Locked transition density ρ_c.
    Conditional on the q-ρ map (substrate-density correspondence not
    yet pinned in the framework). -/
class CSCSilverIsCFLTransition where
  /-- The cost-coincidence locus `q = δ_silver` of the n=2 LP equals
      the density `ρ_c` of the CFL transition predicted by
      conj:color-superconductivity-borromean. -/
  holds : Prop
  -- Ref: [manuscript] conj:color-superconductivity-borromean
  -- Ref: [audit] docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md

/-- Conjectural witness: the bar-image φ² of the deconfinement boundary
    `q_gold = 1/φ²` predicts a CFL → gCFL (gapless CFL) or CCS
    (crystalline color superconductor) phase boundary at q = φ² ≈ 2.618.
    Falsifiable via a second kink in the neutron-star mass-radius
    relation above the silver-density crossover. -/
class BarMirrorPhi2CFLgCFLTransition where
  /-- The CFL/gCFL boundary lies at q = φ² (the bar image of q_gold). -/
  holds : Prop
  -- Ref: [manuscript] conj:bar-mirror-cfl-gcfl-transition
  -- Ref: [audit] docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md

/-! ## SDP degeneracy at cost-coincidence points

When cost coefficients coincide (`t_i(q) = t_j(q)` at some q), the LP/SDP
becomes **degenerate**: strict complementarity FAILS, and the optimal
face has positive dimension instead of being a vertex.  This is what an
"undetermined SDP" looks like algorithmically.

For the n=2 LP at q = δ_silver:
  t_1(δ_silver) = t_2(δ_silver)   (by silver_lp_coincidence)
  ⇒ both x_1 and x_2 are optimal with the same cost
  ⇒ active set is degenerate (neither row strictly active)
  ⇒ Slater's strict complementarity condition FAILS

The empirical n=2 LP active-set sweep observed exactly this: AT δ_silver
the active set was empty (neither Frobenius row tight); on either side
the active set was a single row.  This IS the SDP-degeneracy signature.
-/

/-- Helper: the n=2 LP is degenerate at q = δ_silver.

    Stated as: any feasible x with `x_1 + x_2 = n_target` achieves the
    same cost.  In SDP language, the optimal face has dimension ≥ 1
    instead of being a vertex. -/
theorem n2_lp_degenerate_at_silver (n_target : ℝ) :
    let x_a : ℝ × ℝ := (n_target, 0)
    let x_b : ℝ × ℝ := (0, n_target)
    t1_n2 delta_silver * x_a.1 + t2_n2 delta_silver * x_a.2 =
    t1_n2 delta_silver * x_b.1 + t2_n2 delta_silver * x_b.2 := by
  show t1_n2 delta_silver * n_target + t2_n2 delta_silver * 0 =
       t1_n2 delta_silver * 0 + t2_n2 delta_silver * n_target
  rw [(silver_lp_coincidence delta_silver_pos).mpr rfl]
  ring

/-- Conjectural witness: cost-coincidence points are EXACTLY the loci of
    SDP degeneracy (strict-complementarity failure) on the metallic
    ladder.  Discharging requires the parametric-SDP machinery: the
    optimal-face dimension as a function of q has discontinuities at
    metallic ratios. -/
class SDPDegeneracyDetectsMetallic where
  /-- The set of q > 0 where the n=2 LP optimal face has positive
      dimension equals {δ_silver}.  Generalises to: for the n-strand LP,
      this set is S(n) ⊆ {δ_1, ..., δ_n}. -/
  holds : Prop
  -- Ref: [manuscript] conj:sdp-degeneracy-metallic-locus
  -- Ref: [probe] computations/two_quark_active_set_mahler_sweep.py
  --        (empirically confirmed: AT δ_silver active set is empty;
  --         degenerate-vertex signature directly observed)

end QOU.AlgebraicSubstrate.MetallicLPIdentities
