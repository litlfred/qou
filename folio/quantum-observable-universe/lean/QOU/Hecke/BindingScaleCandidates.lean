/-
# The binding scale: the candidate class, what a fitted "best scale" measures,
# and why the bond-level factors are not scale candidates

The adopted binding law (owner ruling 2026-09-04, Option B; arc synthesis
2026-09-05) is

```
B(Z,N) = E · S(Z,N),     S = log( tr_M(β_free) / tr_M(β_atom) )
                           = (Z−1)(−ln b_pp) + (−ln b_pn) + (N−1)(−ln b_nn)
```

with the derived scale `E₀ = m_e / (q₀(q₀−1))` (`rem:energy-scale-planck`) and,
after the 2026-09-05 tower ruling, `E₀^full = E₀ / (1 − ℏ_q²)`. Against the 2548
measured AME2020 nuclides the *best single scale* is `11.119 MeV`, a factor
`2.656` above `E₀` (`qbeta_binding_law_options_probe.py`). Bean `qou-v8ct` asks
whether that factor is a **scale** defect or belongs to the **bond factors**.

This file proves the structural facts that frame that question, so that no
number has to be chosen. Nothing here selects a candidate; every statement is
an identity or an inequality over an arbitrary field / ordered field.

## What is proved

**§1 — the scale candidates are identities in the substrate constants.**
`E₀ = m_e·c_q²·ℏ_q` (`E0_eq_planck`), `1 − ℏ_q² = (2q−1)/q²`
(`one_sub_hbarQ_sq`), so the tower-summed scale has the closed form
`E₀^full = m_e·q / ((q−1)(2q−1))` (`E0full_closed`) and the ratio of the two
derived forms is `q²/(2q−1)` (`E0full_div_E0`), independent of the anchor `m_e`.
Over `ℝ` the tower sum is literally the geometric series
`Σ_N ℏ_q^{2N} = 1/(1 − ℏ_q²)` (`E0full_eq_E0_mul_tsum`), which is what
"brane-tower summed" means.

**§2 — the bond-level factors already live inside `S`.** The two pure-crossing
bonds satisfy `b_pp · b_nn = 1/[2]_q²` identically (`fPP_mul_fNN`), with
`b_pp = q²/[2]_q` and `b_nn = q⁻²/[2]_q` (`fPP_eq_sq_div_quantumTwo`,
`fNN_eq_inv_sq_div_quantumTwo`), so over `ℝ` the per-strand coefficient of `S`
is exactly `ln [2]_q` (`neg_log_fPP_add_neg_log_fNN`). Hence `[2]_q`, `z_D` and
`1/(q²+1)` are **bond-factor content, not scale candidates**: multiplying `E` by
any of them would count the same factor twice. This is `qou-xf14`'s pinning
identity in Lean; the probe there was symbolic, this is the proof.

**§3 — what a fitted "best scale" is.** For any sample of nuclides with
`B_i, S_i > 0`, the log-least-squares scale is the **geometric mean of the
per-nuclide residuals** `B_i / S_i` (`sum_sq_sub_decomp`, `mean_minimises`,
`bestLogScale_eq_mean`). So the 11.119 MeV target *is* `E₀ × exp(mean ln r_i)`
— an average of a residual that ranges from 1.27 (²H) to 3.26 (⁴He). A scale
that "lands on 11.119" lands on a sample average of the shape defect, which is
why the target is sample-dependent (measured: 2.61 → 2.41 across the mass
bands). On a single-nuclide sample the best scale is that nuclide's own
residual (`bestLogScale_singleton`).

**§4 — rescaling cannot touch the residual's (Z,N)-dependence.** The ratio of
the residuals at two nuclides is the same at every scale
(`residual_ratio_scale_invariant`). Whatever part of `B_exp / (E·S)` varies
across the chart is therefore *not* a scale defect at any `E`; only the
constant part could be. This is the separation the bean asks for, and it is an
identity rather than a measurement.

## What is NOT proved here

That any candidate is the right scale. In particular nothing here derives
`11.119 MeV`, and the Lean would be exactly as true if the measured factor were
`1.000`. The `q ≠ 0`, `q ≠ 1`, `q² + 1 ≠ 0`, `1 < q` hypotheses are all
satisfied at the proton pin `q₀ ≈ 1.10998` and are established there by the
probe, not here.

Base ring per AGENTS.md §7c: §1–§2 and §4 are over a generic `Field`; §3 and the
tower sum need `Real.log` / `tsum` and are stated over `ℝ` after the wall.

Producer / measurement: `computations/qbeta/qbeta_e0_scale_candidates_probe.py`.
Bean `qou-v8ct` (parent `qou-vyvt`).
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

namespace QOU.Hecke.BindingScaleCandidates

open Finset

/-! ## §1. The scale candidates as identities in the substrate constants -/

section Generic

variable {R : Type*} [Field R]

/-- `c_q = 1/(q−1)`, the substrate speed of information (`rem:energy-scale-planck`). -/
def cQ (q : R) : R := 1 / (q - 1)

/-- `ℏ_q = (q−1)/q = 1 − q⁻¹`, the substrate Planck parameter. -/
def hbarQ (q : R) : R := (q - 1) / q

/-- Quantum integer `[2]_q = q + q⁻¹`. -/
def quantumTwo (q : R) : R := q + q⁻¹

/-- Markov parameter, convention D: `z_D = q³/(q²+1)`. -/
def markovZ (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- Hecke skein parameter `h = q − q⁻¹`. -/
def heckeH (q : R) : R := q - q⁻¹

/-- p–p interface factor `b_pp = z_D` (a positive crossing is one Markov reduction). -/
def fPP (q : R) : R := markovZ q

/-- n–n interface factor `b_nn = 1/(q³+q)` (the closed form of
`qbeta_bond_factors_derived_probe.py`). -/
def fNN (q : R) : R := 1 / (q ^ 3 + q)

/-- The single-tick scale `E₀ = m / (q(q−1))`. -/
def E0 (m q : R) : R := m / (q * (q - 1))

/-- The tower-summed scale `E₀^full = E₀ / (1 − ℏ_q²)` (owner ruling 2026-09-05). -/
def E0full (m q : R) : R := E0 m q / (1 - hbarQ q ^ 2)

/-- `E₀ = m·c_q²·ℏ_q`: the closed form of `rem:energy-scale-planck` is the
Planck-unit product, identically in `q`. -/
theorem E0_eq_planck (m q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0 m q = m * cQ q ^ 2 * hbarQ q := by
  unfold E0 cQ hbarQ
  field_simp

/-- `1 − ℏ_q² = (2q − 1)/q²`. -/
theorem one_sub_hbarQ_sq (q : R) (hq : q ≠ 0) :
    1 - hbarQ q ^ 2 = (2 * q - 1) / q ^ 2 := by
  unfold hbarQ
  field_simp
  ring

/-- The tower-summed scale in closed form: `E₀^full = m·q / ((q−1)(2q−1))`. -/
theorem E0full_closed (m q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0full m q = m * q / ((q - 1) * (2 * q - 1)) := by
  unfold E0full E0
  rw [one_sub_hbarQ_sq q hq]
  field_simp

/-- The ratio of the two derived forms is `q²/(2q−1)` — it does not see the
anchor `m` at all. At the proton pin this is the `1.00991` of `qou-qkbp`. -/
theorem E0full_div_E0 (m q : R) (hm : m ≠ 0) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0full m q / E0 m q = q ^ 2 / (2 * q - 1) := by
  rw [E0full_closed m q hq hq1]
  unfold E0
  field_simp

/-- The n–n factor is the Markov parameter minus the skein parameter, `z_D − h`
— the form `QOU.Hecke.ClosedFormInterfaceFactors.fNN` carries in the
square-root variable. Same object, `q`-variable. -/
theorem fNN_eq_markovZ_sub_heckeH (q : R) (hq : q ≠ 0) (h21 : q ^ 2 + 1 ≠ 0) :
    fNN q = markovZ q - heckeH q := by
  unfold fNN markovZ heckeH
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h21
  field_simp
  ring

end Generic

section Tower

/-- For `1 < q`, `0 ≤ ℏ_q² < 1`. -/
theorem hbarQ_sq_lt_one (q : ℝ) (hq : 1 < q) : hbarQ q ^ 2 < 1 := by
  unfold hbarQ
  have h0 : 0 < q := by linarith
  have h1 : 0 ≤ (q - 1) / q := div_nonneg (by linarith) h0.le
  have h2 : (q - 1) / q < 1 := by rw [div_lt_one h0]; linarith
  nlinarith

/-- **The tower-summed scale is the geometric series.** For `1 < q`,
`E₀^full = E₀ · Σ_{N≥0} ℏ_q^{2N}`: "brane-tower summed" means exactly the sum
of the `ℏ_q^{2N}` ladder, and the ruled `1/(1 − ℏ_q²)` is its value. -/
theorem E0full_eq_E0_mul_tsum (m q : ℝ) (hq : 1 < q) :
    E0full m q = E0 m q * ∑' n : ℕ, (hbarQ q ^ 2) ^ n := by
  rw [tsum_geometric_of_lt_one (sq_nonneg _) (hbarQ_sq_lt_one q hq)]
  unfold E0full
  rw [div_eq_mul_inv]

end Tower

/-! ## §2. The bond-level factors are inside `S`, not candidates for `E` -/

section BondLevel

variable {R : Type*} [Field R]

/-- `b_pp · b_nn = 1/[2]_q²`, identically in `q`. The geometric mean of the two
pure-crossing bonds is the inverse loop value (`qou-xf14`). -/
theorem fPP_mul_fNN (q : R) (hq : q ≠ 0) (h21 : q ^ 2 + 1 ≠ 0) :
    fPP q * fNN q = (quantumTwo q)⁻¹ ^ 2 := by
  unfold fPP fNN markovZ quantumTwo
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h21
  field_simp

/-- `b_pp = q² / [2]_q`. -/
theorem fPP_eq_sq_div_quantumTwo (q : R) (hq : q ≠ 0) (h21 : q ^ 2 + 1 ≠ 0) :
    fPP q = q ^ 2 / quantumTwo q := by
  unfold fPP markovZ quantumTwo
  field_simp

/-- `b_nn = q⁻² / [2]_q`. -/
theorem fNN_eq_inv_sq_div_quantumTwo (q : R) (hq : q ≠ 0) (h21 : q ^ 2 + 1 ≠ 0) :
    fNN q = q⁻¹ ^ 2 / quantumTwo q := by
  unfold fNN quantumTwo
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h21
  field_simp

end BondLevel

section BondLevelReal

/-- Over `ℝ` with `0 < q`: the two pure-crossing bond energies sum to
`2 ln [2]_q`, so `ln [2]_q` is the per-strand coefficient **inside** `S`.
Multiplying the scale by `[2]_q` (or by `z_D`, or by `1/(q²+1)`) would count a
factor the law already carries. -/
theorem neg_log_fPP_add_neg_log_fNN (q : ℝ) (hq : 0 < q) :
    -Real.log (fPP q) + -Real.log (fNN q) = 2 * Real.log (quantumTwo q) := by
  have hq0 : q ≠ 0 := hq.ne'
  have h21 : q ^ 2 + 1 ≠ 0 := by positivity
  have hpp : 0 < fPP q := by unfold fPP markovZ; positivity
  have hnn : 0 < fNN q := by unfold fNN; positivity
  have h2 : 0 < quantumTwo q := by unfold quantumTwo; positivity
  have key : Real.log (fPP q) + Real.log (fNN q) = -(2 * Real.log (quantumTwo q)) := by
    rw [← Real.log_mul hpp.ne' hnn.ne', fPP_mul_fNN q hq0 h21, Real.log_pow,
      Real.log_inv]
    push_cast
    ring
  linarith [key]

end BondLevelReal

/-! ## §3. A fitted "best scale" is the geometric mean of the residuals -/

section BestScale

variable {ι : Type*}

/-- Sample mean of `a` over `s`. -/
noncomputable def mean (s : Finset ι) (a : ι → ℝ) : ℝ := (∑ i ∈ s, a i) / s.card

/-- **Sum-of-squares decomposition.** For any `x`,
`Σ (a_i − x)² = Σ (a_i − μ)² + n·(x − μ)²` with `μ` the sample mean. -/
theorem sum_sq_sub_decomp (s : Finset ι) (hs : s.Nonempty) (a : ι → ℝ) (x : ℝ) :
    ∑ i ∈ s, (a i - x) ^ 2
      = ∑ i ∈ s, (a i - mean s a) ^ 2 + s.card * (x - mean s a) ^ 2 := by
  have hn : (s.card : ℝ) ≠ 0 := by
    exact_mod_cast (Finset.card_pos.mpr hs).ne'
  have hsum : ∑ i ∈ s, a i = s.card * mean s a := by
    unfold mean; field_simp
  -- expand both sides and compare
  have e1 : ∀ i, (a i - x) ^ 2 = (a i - mean s a) ^ 2
      + 2 * (mean s a - x) * a i + (x ^ 2 - (mean s a) ^ 2) := by
    intro i; ring
  simp_rw [e1]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum,
    Finset.sum_const, nsmul_eq_mul, hsum]
  ring

/-- The sample mean minimises the sum of squared deviations. -/
theorem mean_minimises (s : Finset ι) (hs : s.Nonempty) (a : ι → ℝ) (x : ℝ) :
    ∑ i ∈ s, (a i - mean s a) ^ 2 ≤ ∑ i ∈ s, (a i - x) ^ 2 := by
  rw [sum_sq_sub_decomp s hs a x]
  have : (0 : ℝ) ≤ s.card * (x - mean s a) ^ 2 := by positivity
  linarith

/-- **Constant-plus-shape split of the log-residual.** With `a_i = ln r_i`,
`Σ a_i² = n·μ² + Σ (a_i − μ)²`: the first term is everything a scale can absorb,
the second is what it cannot. This is what the probe's "shape share" measures. -/
theorem sum_sq_eq_const_add_shape (s : Finset ι) (hs : s.Nonempty) (a : ι → ℝ) :
    ∑ i ∈ s, (a i) ^ 2 = s.card * (mean s a) ^ 2 + ∑ i ∈ s, (a i - mean s a) ^ 2 := by
  have h := sum_sq_sub_decomp s hs a 0
  simp only [sub_zero, zero_sub, neg_sq] at h
  linarith

/-- The log-least-squares residual of the additive law `B = E·S` at scale
`E > 0`, over a sample with `B_i, S_i > 0`. -/
noncomputable def logResidual (s : Finset ι) (B S : ι → ℝ) (E : ℝ) : ℝ :=
  ∑ i ∈ s, (Real.log (B i) - Real.log (E * S i)) ^ 2

/-- The best log-scale is the sample geometric mean of `B_i/S_i`:
`logResidual` at `E* = exp(mean ln(B_i/S_i))` is at most its value at any
`E > 0`. This is exactly the `_geo` the probe uses, so `11.119 MeV` is
`exp(mean ln(B_i/S_i))` over the 2548 measured nuclides and nothing else. -/
theorem bestLogScale_eq_mean (s : Finset ι) (hs : s.Nonempty) (B S : ι → ℝ)
    (hB : ∀ i ∈ s, 0 < B i) (hS : ∀ i ∈ s, 0 < S i) (E : ℝ) (hE : 0 < E) :
    logResidual s B S (Real.exp (mean s (fun i => Real.log (B i / S i))))
      ≤ logResidual s B S E := by
  unfold logResidual
  -- rewrite each summand as (a_i − log E')² with a_i = log(B_i/S_i)
  have rw1 : ∀ E' : ℝ, 0 < E' → ∀ i ∈ s,
      (Real.log (B i) - Real.log (E' * S i)) ^ 2
        = (Real.log (B i / S i) - Real.log E') ^ 2 := by
    intro E' hE' i hi
    rw [Real.log_mul hE'.ne' (hS i hi).ne', Real.log_div (hB i hi).ne' (hS i hi).ne']
    ring
  rw [Finset.sum_congr rfl (rw1 E hE),
    Finset.sum_congr rfl (rw1 _ (Real.exp_pos _)), Real.log_exp]
  exact mean_minimises s hs _ _

/-- On a one-nuclide sample the best scale is that nuclide's own residual
`B_i / S_i`: the fitted target ranges over the residual, so it inherits the
residual's shape. -/
theorem bestLogScale_singleton (i : ι) (B S : ι → ℝ) (hB : 0 < B i) (hS : 0 < S i) :
    Real.exp (mean {i} (fun j => Real.log (B j / S j))) = B i / S i := by
  unfold mean
  simp [Real.exp_log (div_pos hB hS)]

end BestScale

/-! ## §4. Rescaling cannot touch the residual's `(Z,N)`-dependence -/

section Separation

variable {R : Type*} [Field R]

/-- The ratio of the residuals `B/(E·S)` at two nuclides is the same at every
scale `E`. Whatever varies across the chart is not a scale defect. -/
theorem residual_ratio_scale_invariant (Bx By Sx Sy E E' : R)
    (hE : E ≠ 0) (hE' : E' ≠ 0) (hSx : Sx ≠ 0) (hSy : Sy ≠ 0) (hBy : By ≠ 0) :
    (Bx / (E * Sx)) / (By / (E * Sy)) = (Bx / (E' * Sx)) / (By / (E' * Sy)) := by
  field_simp

/-- Every candidate scale has the shape `m · f(q)` with one dimensionful anchor
`m`, so the ratio of two candidates is a pure function of `q`. A measurement of
`m` alone cannot separate them. -/
theorem candidate_ratio_indep_of_anchor (m f g : R) (hm : m ≠ 0) (hg : g ≠ 0) :
    (m * f) / (m * g) = f / g := by
  field_simp

/-- **Pure-crossing bond ratio `b_pp / b_nn = q⁴` (`qou-v8ct`).**
Since `b_pp = q³/(q²+1)` and `b_nn = 1/(q³+q)`, their ratio is `q⁴` over any field `R`. -/
theorem fPP_div_fNN_eq_pow_four (q : R) (hq : q ≠ 0) (h21 : q ^ 2 + 1 ≠ 0) :
    fPP q / fNN q = q ^ 4 := by
  unfold fPP fNN markovZ
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h21
  field_simp
  ring

end Separation

end QOU.Hecke.BindingScaleCandidates
