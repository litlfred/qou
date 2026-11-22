import QOU.Archimedean.DilogPartBBoundarySeed

/-!
# Dilog Part-B W-P1 — the a.e. route, deterministic bricks (Borel–Cantelli programme)

The scope-(b) refutation (`DilogPartBWP1Refutation`) shows the unconditional *pointwise*
branch-index limit is false; the only attainable *positive* over all `x` is the
**measure-theoretic** one — for a.e. `x ∈ (0,1)`, the branch-index boundary term `→ 0` — via a
Borel–Cantelli argument on resonance windows (ledger `docs/coordination/dilog-part-b-cusp-attack.md`,
bean `qou-jplv`/`qou-zuuz`; Mathlib has `measure_limsup_eq_zero`, lacks Weyl equidistribution).

This file lands the **deterministic** heart of that programme — the two `x`-pointwise bricks
that reduce a.e. convergence to a pure *measure* estimate (the one genuine research residual):

* `branch_endpoint_eq` — the branch-index endpoint identity `x·q^{⌊s⌋} = exp((⌊s⌋−s)·log q)`
  with `s := log(1/x)/log q` (so the gap is governed by the resonance `frac s = s − ⌊s⌋`).
* `branch_gap_lower_of_fract` — the **no-resonance ⇒ gap** bound: if `frac s ≥ θ` (`θ>0`) and
  `q ∈ (1,2]`, then `1 − x·q^{⌊s⌋} ≥ (θ/4)(q−1)`.  This is exactly the hypothesis
  `boundary_term_vanishes` (#4270) consumes, so `frac s` bounded below ⇒ the boundary term
  `→ 0`.  The remaining open brick is: **the set `{x : frac s_m < ε_m}` has summable measure**
  (the resonance-window Lebesgue estimate), then Borel–Cantelli gives a.e. `frac` bounded below.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `Real.exp`, `Real.log`, `Nat.floor`, ordering `1 < q`.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md; bean qou-jplv, qou-zuuz
-/

namespace QOU.Archimedean

open Filter Topology

variable {x q : ℝ}

/-- The resonance parameter `s := log(1/x)/log q` (`> 0` for `x ∈ (0,1)`, `q > 1`).  The
    branch index is `⌊s⌋`; the endpoint gap is governed by the fractional part `s − ⌊s⌋`. -/
noncomputable def brS (x q : ℝ) : ℝ := Real.log (1 / x) / Real.log q

theorem brS_nonneg (hx0 : 0 < x) (hx1 : x < 1) (hq1 : 1 < q) : 0 ≤ brS x q := by
  have h1x : (1 : ℝ) < 1 / x := by rw [lt_div_iff₀ hx0]; linarith
  exact le_of_lt (div_pos (Real.log_pos h1x) (Real.log_pos hq1))

/-- **Branch-index endpoint identity** `x·q^{⌊s⌋} = exp((⌊s⌋ − s)·log q)`.  Since
    `s·log q = log(1/x) = −log x`, we get `x·q^{⌊s⌋} = exp(−s·log q + ⌊s⌋·log q)`. -/
theorem branch_endpoint_eq (hx0 : 0 < x) (hq1 : 1 < q) :
    x * q ^ (Nat.floor (brS x q))
      = Real.exp (((Nat.floor (brS x q) : ℝ) - brS x q) * Real.log q) := by
  have hlogq : 0 < Real.log q := Real.log_pos hq1
  have hlq : Real.log q ≠ 0 := ne_of_gt hlogq
  have hqpos : (0 : ℝ) < q := by linarith
  have hcancel : brS x q * Real.log q = Real.log (1 / x) := by
    unfold brS; field_simp
  have hlogx : Real.log x = - (brS x q * Real.log q) := by
    rw [hcancel, one_div, Real.log_inv, neg_neg]
  calc x * q ^ (Nat.floor (brS x q))
      = Real.exp (Real.log x) * Real.exp (Real.log q) ^ (Nat.floor (brS x q)) := by
        rw [Real.exp_log hx0, Real.exp_log hqpos]
    _ = Real.exp (Real.log x) * Real.exp ((Nat.floor (brS x q) : ℝ) * Real.log q) := by
        rw [← Real.exp_nat_mul]
    _ = Real.exp (Real.log x + (Nat.floor (brS x q) : ℝ) * Real.log q) := by rw [← Real.exp_add]
    _ = Real.exp (((Nat.floor (brS x q) : ℝ) - brS x q) * Real.log q) := by
        rw [hlogx]; congr 1; ring

/-- **No-resonance ⇒ gap lower bound.**  If the resonance `frac s = s − ⌊s⌋ ≥ θ` (`θ > 0`)
    and `q ∈ (1,2]`, then `1 − x·q^{⌊s⌋} ≥ (θ/4)(q−1)`.  Feeds `boundary_term_vanishes`
    (#4270) with `c = θ/4`, closing the boundary term `→ 0` on the no-resonance set.

    Proof: `1 − x·q^{⌊s⌋} = 1 − e^{−a}` with `a = (s−⌊s⌋)·log q ≥ 0`; `1 − e^{−a} ≥ a·e^{−a}`
    (`add_one_le_exp`); `a ≥ θ·log q ≥ θ(q−1)/2` (`log q ≥ (q−1)/q ≥ (q−1)/2` on `q≤2`); and
    `e^{−a} = q^{−frac} ≥ q^{−1} ≥ 1/2`.  Product `≥ (θ(q−1)/2)(1/2) = (θ/4)(q−1)`. -/
theorem branch_gap_lower_of_fract (hx0 : 0 < x)
    (hq1 : 1 < q) (hq2 : q ≤ 2) {θ : ℝ} (hθ0 : 0 < θ)
    (hfract : θ ≤ brS x q - (Nat.floor (brS x q) : ℝ)) :
    θ / 4 * (q - 1) ≤ 1 - x * q ^ (Nat.floor (brS x q)) := by
  have hlogq : 0 < Real.log q := Real.log_pos hq1
  set a : ℝ := (brS x q - (Nat.floor (brS x q) : ℝ)) * Real.log q with ha_def
  have ha0 : 0 ≤ a := mul_nonneg (by linarith [hfract]) hlogq.le
  -- endpoint = exp(-a)
  have hend : x * q ^ (Nat.floor (brS x q)) = Real.exp (-a) := by
    rw [branch_endpoint_eq hx0 hq1]; rw [ha_def]; congr 1; ring
  rw [hend]
  -- 1 - e^{-a} ≥ a e^{-a}
  have hea : (0 : ℝ) < Real.exp (-a) := Real.exp_pos _
  have hlb : a * Real.exp (-a) ≤ 1 - Real.exp (-a) := by
    have h := Real.add_one_le_exp a
    have hmul : (a + 1) * Real.exp (-a) ≤ Real.exp a * Real.exp (-a) :=
      mul_le_mul_of_nonneg_right h hea.le
    rw [← Real.exp_add, add_neg_cancel, Real.exp_zero] at hmul
    nlinarith [hmul]
  -- a ≥ θ log q ≥ θ (q-1)/2
  have hqpos : (0 : ℝ) < q := by linarith
  have hlogq_half : (q - 1) / 2 ≤ Real.log q := by
    have hlb : (q - 1) / q ≤ Real.log q := by
      have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < 1 / q by positivity)
      rw [one_div, Real.log_inv] at h
      rw [sub_div, div_self (ne_of_gt hqpos), one_div]
      linarith [h]
    have hqle : (q - 1) / 2 ≤ (q - 1) / q := by
      apply div_le_div_of_nonneg_left (by linarith) (by linarith) hq2
    linarith
  have ha_lb : θ * ((q - 1) / 2) ≤ a := by
    rw [ha_def]
    have hfl : θ ≤ brS x q - (Nat.floor (brS x q) : ℝ) := hfract
    have : θ * Real.log q ≤ (brS x q - (Nat.floor (brS x q) : ℝ)) * Real.log q :=
      mul_le_mul_of_nonneg_right hfl hlogq.le
    nlinarith [mul_le_mul_of_nonneg_left hlogq_half hθ0.le, this]
  -- e^{-a} ≥ 1/2 :  a ≤ log q · 1 < log 2 < 1 ... use e^{-a} ≥ q^{-1} ≥ 1/2
  have hfrac_lt1 : brS x q - (Nat.floor (brS x q) : ℝ) < 1 := by
    have := Nat.lt_floor_add_one (brS x q); linarith
  have ha_ub : a ≤ Real.log q := by
    rw [ha_def]
    have h1 : brS x q - (Nat.floor (brS x q) : ℝ) ≤ 1 := le_of_lt hfrac_lt1
    nlinarith [mul_le_mul_of_nonneg_right h1 hlogq.le]
  have hea_lb : (1 : ℝ) / 2 ≤ Real.exp (-a) := by
    have hstep : Real.exp (- Real.log q) ≤ Real.exp (-a) :=
      Real.exp_le_exp.mpr (by linarith [ha_ub])
    rw [Real.exp_neg, Real.exp_log hqpos] at hstep
    have hq_inv : (1 : ℝ) / 2 ≤ q⁻¹ := by
      have hqinv_pos : 0 < q⁻¹ := inv_pos.mpr hqpos
      have hcancel : q⁻¹ * q = 1 := inv_mul_cancel₀ (ne_of_gt hqpos)
      nlinarith [hcancel, hqinv_pos, mul_nonneg hqinv_pos.le (by linarith : (0:ℝ) ≤ 2 - q)]
    calc (1:ℝ)/2 ≤ q⁻¹ := hq_inv
      _ ≤ Real.exp (-a) := hstep
  -- combine
  have hfinal : θ / 4 * (q - 1) ≤ a * Real.exp (-a) := by
    have h1 : θ * ((q - 1) / 2) * (1 / 2) ≤ a * Real.exp (-a) := by
      apply mul_le_mul ha_lb hea_lb (by norm_num) ha0
    nlinarith [h1]
  linarith [hlb, hfinal]

end QOU.Archimedean
