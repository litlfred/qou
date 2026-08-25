import Mathlib.Data.Complex.Exponential
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Field
import Mathlib.Topology.Algebra.InfiniteSum.NatInt
import Mathlib.Algebra.Order.GroupWithZero.Unbundled.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import QOU.QBeta.PhiBSArgumentIdentification

/-!
# QOU.QBeta.WindingGFTransform — the winding generating-function transform
of the 4₁ index annihilator (bean qou-3bp8, route 2b of qou-qnnq)

#4433 established that the winding sum `F_m(w) = Σ_e I₄₁(m,e)(q̃)·wᵉ` has
radius of convergence exactly 1, while the corpus sheet `w = q₀²e^{2iϑ}`
lies outside the annulus: the physical effective Stokes coefficient
requires analytic continuation. The continuation vehicle is the DGG
quantum A-polynomial annihilator (eq C.7 of [dimofte-gaiotto-gukov2013],
glyph-decoded and grid-certified in-corpus by
`qbeta_g3_annihilator_certification.py`, re-certified at the substrate
point by the qou-3bp8 W1 probe), whose expanded scalar form is carried
here as the conditional class `FourOneIndexAnnihilated` (§3b-cond: a
cited literature input, NOT proved here — everything downstream is
conditional on it and says so in its hypotheses).

The theorem `gf_three_term` is the load-bearing derived step: given the
annihilator and `HasSum` hypotheses for the three winding rows at their
respective arguments, the generating functions satisfy an exact
three-term functional equation relating `F_{m−1}(w/s)`, `F_m(w)`, and
`F_{m+1}(s·w)` (with `s = √q̃`). Because `|1/s| = q₀^{1/2} > 1`, solving
for the `F_{m−1}(w/s)` term expresses an OUTER-argument value through
values at smaller radius — the exact outward continuation ladder used by
the W2 stepping probe. The numerical A2 certification of the W1 probe
checks the same relation inside the annulus; this file replaces
"numerically certified algebra" with a machine-checked proof.

Also here:
* `pairedWindowSum_unit_sheet_im_zero` — the unit-sheet bar-even lemma of
  #4433: a real winding family in paired form evaluated at `w = e^{iθ}`
  has vanishing imaginary part (amphichirality ⇒ no bar-odd part without
  radial deformation).
* `SDeformedVolumeChannelWinding` — the bean-qou-awpk schema item: the
  Stokes coefficient carried per winding class, tied to the constant
  `A_ω` of the base channel as its `w = 1` total.

-- Ref: [dimofte-gaiotto-gukov2013] https://doi.org/10.1007/s00220-013-1863-2
-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062
-/

namespace QOU.QBeta.WindingGFTransform

open Complex

/-- **The 4₁ index annihilator (DGG eq C.7), expanded scalar form** — a
conditional class carrying the literature input. `s` is `√q̃` (so `q̃ = s²`
and the paper's `q^{k/2}` weights are `s^k`), and `I m e` is the real value
of the 3d-index at charge `(m,e)` (e.g. at a fixed evaluation point of the
q-series). The ten-term identity is the mechanical expansion of

  `L̂₄₁ = (q^{½}M̂ − q^{−½}M̂⁻¹)·ℓ̂⁻¹ − (M̂ − M̂⁻¹)(M̂² + M̂⁻² − M̂ − M̂⁻¹ − q − q⁻¹)
         + (q^{−½}M̂ − q^{½}M̂⁻¹)·ℓ̂`

with the trefoil-calibrated actions `M̂f(m,e) = q^{m/2}f(m,e−1)`,
`ℓ̂f(m,e) = −q^{e/2}f(m+1,e)`; the expansion is cross-checked to 1e−71
against the composed operator on certified engine values (qou-3bp8 W1). -/
class FourOneIndexAnnihilated (s : ℝ) (I : ℤ → ℤ → ℝ) : Prop where
  rel : ∀ m e : ℤ,
    -s ^ (m - e + 2) * I (m - 1) (e - 1) + s ^ (-m - e - 2) * I (m - 1) (e + 1)
      - s ^ (3 * m) * I m (e - 3) + s ^ (2 * m) * I m (e - 2)
      + s ^ (m - 2) * (s ^ (4 : ℤ) + s ^ (2 : ℤ) + 1) * I m (e - 1)
      - s ^ (-m - 2) * (s ^ (4 : ℤ) + s ^ (2 : ℤ) + 1) * I m (e + 1)
      - s ^ (-(2 * m)) * I m (e + 2) + s ^ (-(3 * m)) * I m (e + 3)
      - s ^ (e + m - 2) * I (m + 1) (e - 1) + s ^ (e - m + 2) * I (m + 1) (e + 1) = 0

/-- Reindex-and-scale helper: from a winding `HasSum` at argument `v`, the
`d`-shifted family scaled by a constant sums to the scaled total. -/
private theorem reindexed {I' : ℤ → ℝ} {v : ℂ} {T : ℂ}
    (h : HasSum (fun e : ℤ => (I' e : ℂ) * v ^ e) T) (d : ℤ) (C : ℂ) :
    HasSum (fun e : ℤ => C * ((I' (e + d) : ℂ) * v ^ (e + d))) (C * T) := by
  have h1 : HasSum (fun e : ℤ => (I' (e + d) : ℂ) * v ^ (e + d)) T := by
    have h2 := ((Equiv.addRight d).hasSum_iff
      (f := fun e : ℤ => (I' e : ℂ) * v ^ e) (a := T)).mpr h
    simpa [Function.comp_def, Equiv.coe_addRight] using h2
  exact h1.mul_left C

/-- **The winding generating-function three-term functional equation**
(conditional on the annihilator class). For `s > 0`, `w ≠ 0`, and `HasSum`
hypotheses for the three rows at their arguments — row `m` at `w`, row
`m−1` at `w/s`, row `m+1` at `s·w` — the sums satisfy

  `c₋ · F_{m−1}(w/s) + P_m(w) · F_m(w) + c₊ · F_{m+1}(s·w) = 0`

with `c₋ = −s^{m+1}w + s^{−m−1}w⁻¹`, `c₊ = −s^{m−1}w + s^{−m+1}w⁻¹`, and
`P_m` the middle Laurent polynomial. Since `|1/s| > 1` at the substrate,
solving for `F_{m−1}(w/s)` is the exact outward continuation step. -/
theorem gf_three_term {s : ℝ} (hs : 0 < s) {I : ℤ → ℤ → ℝ}
    [A : FourOneIndexAnnihilated s I] {m : ℤ} {w : ℂ} (hw : w ≠ 0)
    {Fm Fdn Fup : ℂ}
    (hFm : HasSum (fun e : ℤ => (I m e : ℂ) * w ^ e) Fm)
    (hFdn : HasSum (fun e : ℤ => (I (m - 1) e : ℂ) * (w / (s : ℂ)) ^ e) Fdn)
    (hFup : HasSum (fun e : ℤ => (I (m + 1) e : ℂ) * ((s : ℂ) * w) ^ e) Fup) :
    (-(s : ℂ) ^ (m + 1) * w + (s : ℂ) ^ (-m - 1) * w⁻¹) * Fdn
      + (-(s : ℂ) ^ (3 * m) * w ^ (3 : ℤ) + (s : ℂ) ^ (2 * m) * w ^ (2 : ℤ)
          + (s : ℂ) ^ (m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w
          - (s : ℂ) ^ (-m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w⁻¹
          - (s : ℂ) ^ (-(2 * m)) * w ^ (-2 : ℤ)
          + (s : ℂ) ^ (-(3 * m)) * w ^ (-3 : ℤ)) * Fm
      + (-(s : ℂ) ^ (m - 1) * w + (s : ℂ) ^ (-m + 1) * w⁻¹) * Fup = 0 := by
  have hs0 : (s : ℂ) ≠ 0 := by
    exact_mod_cast (ne_of_gt hs)
  -- the ten reindexed-and-scaled HasSum instances (one per expanded term)
  have h1 := reindexed hFdn (-1) (-(s : ℂ) ^ (m + 1) * w)
  have h2 := reindexed hFdn 1 ((s : ℂ) ^ (-m - 1) * w⁻¹)
  have h3 := reindexed hFm (-3) (-(s : ℂ) ^ (3 * m) * w ^ (3 : ℤ))
  have h4 := reindexed hFm (-2) ((s : ℂ) ^ (2 * m) * w ^ (2 : ℤ))
  have h5 := reindexed hFm (-1)
    ((s : ℂ) ^ (m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w)
  have h6 := reindexed hFm 1
    (-(s : ℂ) ^ (-m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w⁻¹)
  have h7 := reindexed hFm 2 (-(s : ℂ) ^ (-(2 * m)) * w ^ (-2 : ℤ))
  have h8 := reindexed hFm 3 ((s : ℂ) ^ (-(3 * m)) * w ^ (-3 : ℤ))
  have h9 := reindexed hFup (-1) (-(s : ℂ) ^ (m - 1) * w)
  have h10 := reindexed hFup 1 ((s : ℂ) ^ (-m + 1) * w⁻¹)
  -- total: HasSum of the pointwise ten-term family (nested adds)
  have htot := ((((((((h1.add h2).add h3).add h4).add h5).add h6).add
    h7).add h8).add h9).add h10
  -- the family is pointwise zero: each summand collection is w^e times the
  -- (cast) annihilator relation
  have h0 := htot.unique (a₂ := 0) ?_
  · linear_combination h0
  · convert (hasSum_zero : HasSum (fun _ : ℤ => (0 : ℂ)) 0) using 2
    rename_i e
    have hrel := A.rel m e
    have hrelC : ((
        -s ^ (m - e + 2) * I (m - 1) (e - 1) + s ^ (-m - e - 2) * I (m - 1) (e + 1)
        - s ^ (3 * m) * I m (e - 3) + s ^ (2 * m) * I m (e - 2)
        + s ^ (m - 2) * (s ^ (4 : ℤ) + s ^ (2 : ℤ) + 1) * I m (e - 1)
        - s ^ (-m - 2) * (s ^ (4 : ℤ) + s ^ (2 : ℤ) + 1) * I m (e + 1)
        - s ^ (-(2 * m)) * I m (e + 2) + s ^ (-(3 * m)) * I m (e + 3)
        - s ^ (e + m - 2) * I (m + 1) (e - 1) + s ^ (e - m + 2) * I (m + 1) (e + 1) : ℝ) : ℂ)
        = 0 := by
      exact_mod_cast congrArg (fun x : ℝ => (x : ℂ)) hrel
    -- cast to ℂ first, then normalize every variable-exponent power to the
    -- atoms (↑s)^m, (↑s)^e, w^e on BOTH sides (2m/3m exponents commuted so
    -- zpow_mul lands on powers of the s^m atom), clear inverses with the
    -- atom-nonzero facts, and close: the family is exactly w^e · (relation).
    push_cast at hrelC
    have hXne : (s : ℂ) ^ m ≠ 0 := zpow_ne_zero _ hs0
    have hYne : (s : ℂ) ^ e ≠ 0 := zpow_ne_zero _ hs0
    have hWne : w ^ e ≠ 0 := zpow_ne_zero _ hw
    simp only [div_zpow, mul_zpow, sub_eq_add_neg, zpow_add₀ hs0,
      zpow_add₀ hw, zpow_neg, zpow_one,
      show (2 : ℤ) * m = m * 2 from mul_comm _ _,
      show (3 : ℤ) * m = m * 3 from mul_comm _ _,
      zpow_mul] at hrelC ⊢
    field_simp at hrelC ⊢
    linear_combination (w ^ e : ℂ) * hrelC

/-- **Unit-sheet bar-even lemma** (#4433 structural result, formalized): a
real winding family in paired form — `c₀ + Σ_{e=1}^{N} c_e·(wᵉ + w⁻ᵉ)` —
evaluated on the unit sheet `w = e^{iθ}` is real: its imaginary part
vanishes identically. Amphichirality therefore forbids any bar-odd part
of the winding-refined Stokes coefficient without RADIAL deformation
(`|w| ≠ 1`) — the corpus structure `𝔲 = ln q₀ + iϑ` needs both. -/
theorem pairedWindowSum_unit_sheet_im_zero (c : ℕ → ℝ) (N : ℕ) (θ : ℝ) :
    ((c 0 : ℂ) + ∑ e ∈ Finset.Icc 1 N,
        (c e : ℂ) * (Complex.exp (θ * Complex.I) ^ e
          + (Complex.exp (θ * Complex.I))⁻¹ ^ e)).im = 0 := by
  have hconj : (Complex.exp (θ * Complex.I))⁻¹
      = starRingEnd ℂ (Complex.exp (θ * Complex.I)) := by
    rw [← Complex.exp_conj]
    rw [← Complex.exp_neg]
    congr 1
    simp [Complex.conj_I]
  rw [Complex.add_im, Complex.ofReal_im, zero_add, Complex.im_sum]
  refine Finset.sum_eq_zero fun e _ => ?_
  have hz : (Complex.exp (θ * Complex.I) ^ e
      + (Complex.exp (θ * Complex.I))⁻¹ ^ e).im = 0 := by
    have hmp : ((starRingEnd ℂ) (Complex.exp (θ * Complex.I))) ^ e
        = (starRingEnd ℂ) ((Complex.exp (θ * Complex.I)) ^ e) :=
      (map_pow _ _ _).symm
    rw [hconj, hmp, Complex.add_im, Complex.conj_im]
    exact add_neg_cancel _
  rw [Complex.mul_im, hz, mul_zero, Complex.ofReal_im, zero_mul, add_zero]

open QOU.QBeta.PhiBSArgumentIdentification in
/-- **Winding-refined Stokes channel** (bean qou-awpk Lean item): the Stokes
coefficient carried per winding class `e ∈ ℤ` (the GGM peacock lattice; for
4₁ the extracted family is `I(0,e)` of the qou-awpk probe), amphichirally
symmetric, whose total is the base channel's constant `A_ω` — i.e. the
constant-A_ω channel is the `w = 1` (complete-structure) evaluation of the
winding family. -/
class SDeformedVolumeChannelWinding (S : ℝ → ℝ)
    extends SDeformedVolumeChannel S where
  /-- The per-winding-class Stokes coefficient family. -/
  A_family : ℤ → ℝ
  /-- Amphichiral symmetry of the family (4₁: `I(0,e) = I(0,−e)`). -/
  A_family_symm : ∀ e : ℤ, A_family (-e) = A_family e
  /-- The base channel's constant is the `w = 1` total of the family. -/
  A_total : HasSum A_family A_ω

open QOU.QBeta.PhiBSArgumentIdentification in
/-- The constant Stokes coefficient of a winding-refined channel is the
`tsum` of its winding family (derived from the `HasSum` field). -/
theorem A_omega_eq_tsum (S : ℝ → ℝ)
    [ch : SDeformedVolumeChannelWinding S] :
    ch.A_ω = ∑' e : ℤ, ch.A_family e :=
  (ch.A_total.tsum_eq).symm


/-! ## Entirety of square-dominated winding families

The qou-3bp8 decay finding: the leading q̃-power of `I(0,e)` grows
quadratically (`lead(e) = T(⌈e/2⌉) ≈ e²/8`), which forces the substrate
values to decay SUPER-exponentially in `e` once past the pre-asymptotic
hump (measured onset ≈ e ≈ 30–40: `I(0,28) ~ 0.09`, `I(0,40) ~ 2·10⁻⁵`).
The #4433 "radius of convergence exactly 1" diagnostic sampled only
`e ≤ 28` — the pre-asymptotic plateau. Consequence, PROVED here: a
two-sided family dominated by `A·ρ^{e²}` is absolutely summable against
`w^e` for EVERY `w ≠ 0` — the winding generating function is entire on
`ℂ*`, no analytic continuation is needed, and the `gf_three_term`
hypotheses are dischargeable at every point (capstone below). The decay
bound itself enters as a hypothesis (computational/literature input);
the entirety consequence and the discharge are machine-checked. -/

/-- A square-dominated ℕ-sequence `A·ρ^{n²}·R^n` is summable for any
`R` (the `ρ^{n²}` factor beats every geometric growth): elementary
tail-comparison with `(1/2)^n` beyond `N` with `ρ^N·R < 1/2`. -/
private theorem summable_sq_dominated_nat {A ρ R : ℝ} (hA : 0 ≤ A)
    (hρ0 : 0 < ρ) (hρ1 : ρ < 1) (hR : 1 ≤ R) :
    Summable (fun n : ℕ => A * ρ ^ (n ^ 2) * R ^ n) := by
  obtain ⟨N, hN⟩ : ∃ N : ℕ, ρ ^ N * R < 1 / 2 := by
    obtain ⟨N, hN⟩ := exists_pow_lt_of_lt_one
      (show (0 : ℝ) < 1 / (2 * R) by positivity) hρ1
    refine ⟨N, ?_⟩
    have hR0 : (0 : ℝ) < R := lt_of_lt_of_le one_pos hR
    calc ρ ^ N * R < 1 / (2 * R) * R := by
          exact mul_lt_mul_of_pos_right hN hR0
    _ = 1 / 2 := by field_simp
  rw [← summable_nat_add_iff N]
  refine Summable.of_nonneg_of_le (fun n => by positivity) (fun n => ?_)
    (((summable_geometric_of_lt_one (by norm_num) (by norm_num :
        (1 : ℝ) / 2 < 1)).mul_left A))
  have h1 : ρ ^ ((n + N) ^ 2) ≤ (ρ ^ N) ^ (n + N) := by
    rw [← pow_mul]
    exact pow_le_pow_of_le_one hρ0.le hρ1.le (by nlinarith)
  have h2 : A * ρ ^ ((n + N) ^ 2) * R ^ (n + N)
      ≤ A * ((ρ ^ N) ^ (n + N) * R ^ (n + N)) := by
    have := mul_le_mul_of_nonneg_right h1
      (pow_nonneg (le_trans zero_le_one hR) (n + N))
    nlinarith [pow_nonneg hρ0.le ((n + N) ^ 2),
      pow_nonneg (le_trans zero_le_one hR) (n + N)]
  refine le_trans h2 ?_
  rw [← mul_pow]
  have h3 : (ρ ^ N * R) ^ (n + N) ≤ (1 / 2) ^ (n + N) :=
    pow_le_pow_left₀ (by positivity) hN.le _
  have h4 : ((1 : ℝ) / 2) ^ (n + N) ≤ (1 / 2) ^ n :=
    pow_le_pow_of_le_one (by norm_num) (by norm_num) (Nat.le_add_right n N)
  have hA' : 0 ≤ A := hA
  nlinarith [pow_nonneg (show (0:ℝ) ≤ ρ ^ N * R by positivity) (n + N)]

/-- **Entirety of square-dominated winding families.** If
`|c e| ≤ A·ρ^{(natAbs e)²}` with `0 < ρ < 1`, then `Σ_e c e · wᵉ`
converges absolutely for EVERY `w ≠ 0`: the winding generating function
is entire on `ℂ*`. This is the machine-checked consequence of the
quadratic-lead decay; no analytic continuation is ever needed. -/
theorem summable_winding_of_sq_dominated {c : ℤ → ℝ} {A ρ : ℝ}
    (hA : 0 ≤ A) (hρ0 : 0 < ρ) (hρ1 : ρ < 1)
    (hc : ∀ e : ℤ, |c e| ≤ A * ρ ^ e.natAbs ^ 2)
    {w : ℂ} (hw : w ≠ 0) :
    Summable (fun e : ℤ => (c e : ℂ) * w ^ e) := by
  have hw0 : (0 : ℝ) < ‖w‖ := norm_pos_iff.mpr hw
  set R : ℝ := max ‖w‖ ‖w‖⁻¹ with hRdef
  have hR1 : 1 ≤ R := by
    rcases le_total 1 ‖w‖ with h | h
    · exact le_max_of_le_left h
    · exact le_max_of_le_right (one_le_inv_iff₀.mpr ⟨hw0, h⟩)
  refine Summable.of_norm ?_
  have hbound : ∀ e : ℤ, ‖(c e : ℂ) * w ^ e‖ ≤ A * ρ ^ e.natAbs ^ 2 * R ^ e.natAbs := by
    intro e
    rw [norm_mul, norm_zpow, Complex.norm_real]
    have hwR : ‖w‖ ^ e ≤ R ^ e.natAbs := by
      rcases Int.natAbs_eq e with he | he
      · rw [he, zpow_natCast]
        exact pow_le_pow_left₀ hw0.le (le_max_left _ _) _
      · rw [he, zpow_neg, zpow_natCast, ← inv_pow]
        simp only [Int.natAbs_neg, Int.natAbs_natCast]
        exact pow_le_pow_left₀ (inv_nonneg.mpr hw0.le) (le_max_right _ _) _
    have h1 : |c e| * ‖w‖ ^ e ≤ (A * ρ ^ e.natAbs ^ 2) * R ^ e.natAbs := by
      refine mul_le_mul (hc e) hwR (zpow_nonneg hw0.le e) ?_
      have := abs_nonneg (c e)
      nlinarith [hc e]
    simpa [mul_assoc] using h1
  refine Summable.of_nonneg_of_le (fun e => norm_nonneg _) hbound ?_
  have hnat := summable_sq_dominated_nat hA hρ0 hρ1 hR1
  refine Summable.of_nat_of_neg ?_ ?_
  · exact hnat.congr fun n => by simp
  · exact hnat.congr fun n => by simp

open QOU.QBeta.PhiBSArgumentIdentification in
/-- **Capstone: the three-term functional equation holds at EVERY `w ≠ 0`**
for square-dominated winding rows — the `gf_three_term` `HasSum`
hypotheses are discharged by entirety, so the relation among the `tsum`s
holds on all of `ℂ*` with no continuation. -/
theorem gf_three_term_of_sq_dominated {s : ℝ} (hs : 0 < s)
    {I : ℤ → ℤ → ℝ} [A : FourOneIndexAnnihilated s I]
    (hdom : ∀ m' : ℤ, ∃ C ρ, 0 ≤ C ∧ 0 < ρ ∧ ρ < 1 ∧
      ∀ e : ℤ, |I m' e| ≤ C * ρ ^ e.natAbs ^ 2)
    {m : ℤ} {w : ℂ} (hw : w ≠ 0) :
    (-(s : ℂ) ^ (m + 1) * w + (s : ℂ) ^ (-m - 1) * w⁻¹)
        * (∑' e : ℤ, (I (m - 1) e : ℂ) * (w / (s : ℂ)) ^ e)
      + (-(s : ℂ) ^ (3 * m) * w ^ (3 : ℤ) + (s : ℂ) ^ (2 * m) * w ^ (2 : ℤ)
          + (s : ℂ) ^ (m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w
          - (s : ℂ) ^ (-m - 2) * ((s : ℂ) ^ (4 : ℤ) + (s : ℂ) ^ (2 : ℤ) + 1) * w⁻¹
          - (s : ℂ) ^ (-(2 * m)) * w ^ (-2 : ℤ)
          + (s : ℂ) ^ (-(3 * m)) * w ^ (-3 : ℤ))
        * (∑' e : ℤ, (I m e : ℂ) * w ^ e)
      + (-(s : ℂ) ^ (m - 1) * w + (s : ℂ) ^ (-m + 1) * w⁻¹)
        * (∑' e : ℤ, (I (m + 1) e : ℂ) * ((s : ℂ) * w) ^ e) = 0 := by
  have hs0 : (s : ℂ) ≠ 0 := by exact_mod_cast (ne_of_gt hs)
  obtain ⟨C1, ρ1, hC1, hρ10, hρ11, hb1⟩ := hdom (m - 1)
  obtain ⟨C2, ρ2, hC2, hρ20, hρ21, hb2⟩ := hdom m
  obtain ⟨C3, ρ3, hC3, hρ30, hρ31, hb3⟩ := hdom (m + 1)
  have hdn := (summable_winding_of_sq_dominated hC1 hρ10 hρ11 hb1
    (w := w / (s : ℂ)) (div_ne_zero hw hs0)).hasSum
  have hm := (summable_winding_of_sq_dominated hC2 hρ20 hρ21 hb2
    (w := w) hw).hasSum
  have hup := (summable_winding_of_sq_dominated hC3 hρ30 hρ31 hb3
    (w := (s : ℂ) * w) (mul_ne_zero hs0 hw)).hasSum
  exact gf_three_term hs hw hm hdn hup

end QOU.QBeta.WindingGFTransform
