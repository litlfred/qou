/-
  Watson-uniqueness brick 4b-ii (assembly) — the shifted uniqueness lemma
  (bean el8w tranche 5).

  Final assembly of the Watson boundary argument: apply brick 3's
  `watson_uniqueness_rhp` to the SHIFTED functions `w ↦ f(w + ε)` on `{re > 0}`
  to obtain uniqueness on the shifted half-plane `{re ≥ ε}`, then feed the
  family `(EqOn f g {re ≥ ε})_{ε>0}` to the ε-reduction
  `eqOn_rhp_of_eqOn_shifted` (brick 4b-ii boundary) to conclude on the open
  half-plane `{re > 0}` — dodging the `w = 0` puncture that blocked a direct
  application.

  Building blocks proved here, sorry-free:
    * `tendsto_addRight_cobounded` — translation preserves coboundedness
      (`‖w+ε‖ ≥ ‖w‖ − ‖ε‖ → ∞`);
    * `tendsto_addRight_shifted` — translation maps the filter of brick 3's
      growth hypothesis, `cobounded ⊓ 𝓟{re>0}`, to `cobounded ⊓ 𝓟{re>ε}`.

  With the merged `diffContOnCl_comp_add_const` (DiffContOnCl transport) and the
  growth transport below, the six hypotheses of `watson_uniqueness_rhp` all move
  across the shift. Archimedean (ℂ).

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4b-ii assembly
-/

import QOU.Mathlib.BorelWatsonUniqueness
import QOU.Mathlib.BorelWatsonBoundary
import QOU.Mathlib.BorelWatsonShift

namespace QOU.Mathlib.Borel

open Filter Bornology Topology Complex Set Asymptotics
open scoped Topology

/-- Translation `w ↦ w + ε` preserves coboundedness: `Tendsto (·+ε) cobounded
    cobounded`. Via `‖w + ε‖ ≥ ‖w‖ − ‖ε‖ → ∞` on `cobounded`. -/
theorem tendsto_addRight_cobounded (ε : ℂ) :
    Tendsto (fun w : ℂ => w + ε) (cobounded ℂ) (cobounded ℂ) := by
  rw [← comap_norm_atTop (E := ℂ), tendsto_comap_iff, comap_norm_atTop (E := ℂ)]
  refine tendsto_atTop_mono (fun w => ?_)
    (tendsto_norm_cobounded_atTop.atTop_add (tendsto_const_nhds (x := -‖ε‖)))
  have h := norm_sub_norm_le w (-ε)
  simp only [sub_neg_eq_add, norm_neg] at h
  simpa [Function.comp] using h

/-- The filter of brick 3's growth hypothesis, `cobounded ⊓ 𝓟 {re > 0}`, is
    carried by `w ↦ w + ε` to `cobounded ⊓ 𝓟 {re > ε}`: coboundedness is
    preserved and the open half-plane `{re > 0}` maps into `{re > ε}`. -/
theorem tendsto_addRight_shifted (ε : ℝ) :
    Tendsto (fun w : ℂ => w + (ε : ℂ))
      (cobounded ℂ ⊓ 𝓟 {z : ℂ | 0 < z.re})
      (cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}) := by
  refine (tendsto_addRight_cobounded _).inf ?_
  rw [tendsto_principal_principal]
  intro w hw
  simp only [mem_setOf_eq, Complex.add_re, Complex.ofReal_re] at hw ⊢
  linarith

/-- **Growth-bound transport.** The brick-3 growth hypothesis
    `∃ c < 2, ∃ B, f =O exp(B‖z‖^c)` on `{re > ε}` moves to the same shape for
    `w ↦ f(w+ε)` on `{re > 0}`. After `comp_tendsto` (giving
    `f' =O exp(B‖w+ε‖^c)`), the exponent/coefficient are normalized to
    `c' = max c 0 ∈ [0,2)`, `B' = max B 0 · 2^{c'}`, using `‖w+ε‖ ≤ 2‖w‖` and
    rpow monotonicity — all valid eventually since `‖w‖ → ∞` on `cobounded`. -/
theorem isBigO_exp_shift {E : Type*} [NormedAddCommGroup E] {f : ℂ → E} {ε : ℝ}
    (hf : ∃ c < (2 : ℝ), ∃ B, f =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}]
      fun z => Real.exp (B * ‖z‖ ^ c)) :
    ∃ c < (2 : ℝ), ∃ B, (fun w => f (w + (ε : ℂ)))
      =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | 0 < z.re}] fun z => Real.exp (B * ‖z‖ ^ c) := by
  obtain ⟨c, hc, B, hO⟩ := hf
  set S : Set ℂ := {z : ℂ | 0 < z.re}
  set c' : ℝ := max c 0 with hc'
  have hc'0 : 0 ≤ c' := le_max_right _ _
  have hcc' : c ≤ c' := le_max_left _ _
  -- eventually ‖w‖ is large on the working filter
  have hnorm : Tendsto (fun w : ℂ => ‖w‖) (cobounded ℂ ⊓ 𝓟 S) atTop :=
    tendsto_norm_cobounded_atTop.mono_left inf_le_left
  -- f' =O exp(B‖w+ε‖^c)
  have h1 : (fun w => f (w + (ε : ℂ))) =O[cobounded ℂ ⊓ 𝓟 S]
      fun w => Real.exp (B * ‖w + (ε : ℂ)‖ ^ c) := by
    have := hO.comp_tendsto (tendsto_addRight_shifted ε)
    simpa [Function.comp] using this
  refine ⟨c', max_lt hc (by norm_num), max B 0 * 2 ^ c', h1.trans (IsBigO.of_bound 1 ?_)⟩
  -- ∀ᶠ w, ‖exp(B‖w+ε‖^c)‖ ≤ 1 * ‖exp(B'‖w‖^c')‖
  filter_upwards [hnorm.eventually_ge_atTop (max 1 (‖(ε : ℂ)‖ + 1))] with w hw
  have hwε : ‖(ε : ℂ)‖ + 1 ≤ ‖w‖ := le_trans (le_max_right _ _) hw
  have hw1 : (1 : ℝ) ≤ ‖w‖ := le_trans (le_max_left _ _) hw
  have hw0 : (0 : ℝ) < ‖w‖ := lt_of_lt_of_le one_pos hw1
  have htri : ‖w + (ε : ℂ)‖ ≤ 2 * ‖w‖ := by
    calc ‖w + (ε : ℂ)‖ ≤ ‖w‖ + ‖(ε : ℂ)‖ := norm_add_le _ _
      _ ≤ ‖w‖ + ‖w‖ := by linarith
      _ = 2 * ‖w‖ := by ring
  have hwε1 : (1 : ℝ) ≤ ‖w + (ε : ℂ)‖ := by
    have := norm_sub_norm_le w (-(ε : ℂ))
    simp only [sub_neg_eq_add, norm_neg] at this
    linarith
  -- the core exponent inequality: B‖w+ε‖^c ≤ (max B 0 · 2^c')‖w‖^c'
  have key : B * ‖w + (ε : ℂ)‖ ^ c ≤ (max B 0 * 2 ^ c') * ‖w‖ ^ c' := by
    have e1 : ‖w + (ε : ℂ)‖ ^ c ≤ ‖w + (ε : ℂ)‖ ^ c' :=
      Real.rpow_le_rpow_of_exponent_le hwε1 hcc'
    have e2 : ‖w + (ε : ℂ)‖ ^ c' ≤ (2 * ‖w‖) ^ c' :=
      Real.rpow_le_rpow (norm_nonneg _) htri hc'0
    have e3 : (2 * ‖w‖) ^ c' = 2 ^ c' * ‖w‖ ^ c' :=
      Real.mul_rpow (by norm_num) (norm_nonneg _)
    have hbnd : ‖w + (ε : ℂ)‖ ^ c ≤ 2 ^ c' * ‖w‖ ^ c' := le_trans e1 (e3 ▸ e2)
    calc B * ‖w + (ε : ℂ)‖ ^ c
        ≤ max B 0 * ‖w + (ε : ℂ)‖ ^ c :=
          mul_le_mul_of_nonneg_right (le_max_left B 0)
            (Real.rpow_nonneg (norm_nonneg _) _)
      _ ≤ max B 0 * (2 ^ c' * ‖w‖ ^ c') :=
          mul_le_mul_of_nonneg_left hbnd (le_max_right B 0)
      _ = (max B 0 * 2 ^ c') * ‖w‖ ^ c' := by ring
  rw [one_mul, Real.norm_of_nonneg (Real.exp_nonneg _),
    Real.norm_of_nonneg (Real.exp_nonneg _)]
  exact Real.exp_le_exp.mpr key

/-- **Shifted Watson uniqueness.** Brick 3's `watson_uniqueness_rhp`, transported
    to the shifted half-plane `{re ≥ ε}` by applying it to `w ↦ f(w+ε)`,
    `w ↦ g(w+ε)` on `{re > 0}`. All six hypotheses move across the shift: the
    `DiffContOnCl` regularity via `diffContOnCl_comp_add_const`, the growth
    bounds via `isBigO_exp_shift`, and (directly, matching the shifted
    evaluation points) the imaginary-axis→vertical-line `{re = ε}` boundedness
    and the shifted positive-real-axis stretched-exp decay. The conclusion is
    pulled back from `{re ≥ 0}` to `{re ≥ ε}` by `w = z − ε`. -/
theorem watson_uniqueness_shifted {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] {f g : ℂ → E} {C b s ε : ℝ} (hb : 0 < b) (hs : 1 < s)
    (hfd : DiffContOnCl ℂ f {z : ℂ | ε < z.re})
    (hgd : DiffContOnCl ℂ g {z : ℂ | ε < z.re})
    (hfexp : ∃ c < (2 : ℝ), ∃ B, f =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}]
      fun z => Real.exp (B * ‖z‖ ^ c))
    (hgexp : ∃ c < (2 : ℝ), ∃ B, g =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}]
      fun z => Real.exp (B * ‖z‖ ^ c))
    (hfim : ∃ C, ∀ x : ℝ, ‖f ((x : ℂ) * Complex.I + (ε : ℂ))‖ ≤ C)
    (hgim : ∃ C, ∀ x : ℝ, ‖g ((x : ℂ) * Complex.I + (ε : ℂ))‖ ≤ C)
    (hre : ∀ᶠ x : ℝ in atTop,
      ‖f ((x : ℂ) + (ε : ℂ)) - g ((x : ℂ) + (ε : ℂ))‖ ≤ C * Real.exp (-b * x ^ s)) :
    Set.EqOn f g {z : ℂ | ε ≤ z.re} := by
  have key : Set.EqOn (fun w => f (w + (ε : ℂ))) (fun w => g (w + (ε : ℂ)))
      {z : ℂ | 0 ≤ z.re} :=
    watson_uniqueness_rhp hb hs (diffContOnCl_comp_add_const hfd)
      (diffContOnCl_comp_add_const hgd) (isBigO_exp_shift hfexp)
      (isBigO_exp_shift hgexp) hfim hgim hre
  intro z hz
  have hw : (z - (ε : ℂ)) ∈ {w : ℂ | 0 ≤ w.re} := by
    simp only [mem_setOf_eq, Complex.sub_re, Complex.ofReal_re]
    simp only [mem_setOf_eq] at hz; linarith
  have := key hw
  simpa using this

/-- **Watson uniqueness on the open right half-plane — COMPLETE.** The capstone:
    if the shifted Watson hypotheses hold on every strictly-interior half-plane
    `{re > ε}` (ε > 0), then `f = g` on the whole open half-plane `{re > 0}`.
    Composes `watson_uniqueness_shifted` (each `{re ≥ ε}` instance) with the
    ε-reduction `eqOn_rhp_of_eqOn_shifted` (brick 4b-ii boundary), which lets
    `ε → 0` while never touching the boundary puncture at `0`. This closes the
    Watson / Nevanlinna–Sokal uniqueness gap on the half-plane. -/
theorem watson_uniqueness_rhp_open {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] {f g : ℂ → E} {b s : ℝ} (hb : 0 < b) (hs : 1 < s)
    (hshift : ∀ ε : ℝ, 0 < ε → ∃ C : ℝ,
      DiffContOnCl ℂ f {z : ℂ | ε < z.re} ∧
      DiffContOnCl ℂ g {z : ℂ | ε < z.re} ∧
      (∃ c < (2 : ℝ), ∃ B, f =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}]
        fun z => Real.exp (B * ‖z‖ ^ c)) ∧
      (∃ c < (2 : ℝ), ∃ B, g =O[cobounded ℂ ⊓ 𝓟 {z : ℂ | ε < z.re}]
        fun z => Real.exp (B * ‖z‖ ^ c)) ∧
      (∃ Cf, ∀ x : ℝ, ‖f ((x : ℂ) * Complex.I + (ε : ℂ))‖ ≤ Cf) ∧
      (∃ Cg, ∀ x : ℝ, ‖g ((x : ℂ) * Complex.I + (ε : ℂ))‖ ≤ Cg) ∧
      (∀ᶠ x : ℝ in atTop,
        ‖f ((x : ℂ) + (ε : ℂ)) - g ((x : ℂ) + (ε : ℂ))‖ ≤ C * Real.exp (-b * x ^ s))) :
    Set.EqOn f g {z : ℂ | 0 < z.re} := by
  refine eqOn_rhp_of_eqOn_shifted (fun ε hε => ?_)
  obtain ⟨C, hfd, hgd, hfexp, hgexp, hfim, hgim, hre⟩ := hshift ε hε
  exact watson_uniqueness_shifted hb hs hfd hgd hfexp hgexp hfim hgim hre

end QOU.Mathlib.Borel
