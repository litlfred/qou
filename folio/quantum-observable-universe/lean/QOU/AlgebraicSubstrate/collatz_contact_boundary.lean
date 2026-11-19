import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic
import QOU.AlgebraicSubstrate.qou_obstruction_reduction

/-!
# QOU.AlgebraicSubstrate.collatz_contact_boundary

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts`](quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts).

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

**C10 (2026-07-31).** The Kummer-removability content is no longer a standalone
context-class axiom. `CollatzContactBoundaryContext` now **extends** the universal
`QouObstructionReductionContext`, `kummer_obstruction_removable` is *defined* as
the vanishing of the level-2 Kummer obstruction, and
`obstruction_removable_of_even_chi` is **derived** (theorem, not field) from
`kappa_vanishes_iff_chi`. So "`2 ∣ χ(A)` ⟹ the `[2]_q`-divisor is removable" now
reduces to the universal χ(A) obstruction-reduction, not an independent assumption.
-/

namespace QOU.AlgebraicSubstrate


/-- QOU-furnished context for the `collatz_contact_boundary` claim. **Extends** the
    universal Kummer obstruction-reduction context (`QouObstructionReductionContext`,
    supplying `χ(A)`, `κ₀`, the level-`n` vanishing predicate and its definitional
    reduction), together with the Skein/Reeb data of a quantum observable universe
    `(𝐂, A, τ)` — `q` its substrate parameter, `[2]_q = q + 1` — and the Descartes
    specialisation `χ(A) = -6`. Kummer removability is no longer a field: it is
    *defined* below as level-2 obstruction vanishing and *derived* from parity. -/
class CollatzContactBoundaryContext (R : Type*) [CommRing R]
    extends QouObstructionReductionContext where
  /-- Substrate parameter `q` of the QOU, over the coefficient ring `R`.

      **Base ring (§7c).** This was `ℝ`, and that was a gratuitous
      specialisation: the manuscript's ambient object is the Skein module
      `𝒮(q) ≅ ℤ[q^{±1}]` — a Laurent ring — and the only thing done with `q`
      here is the ring identity `[2]_q = q + 1` and the hypothesis
      `[2]_q = 0` (i.e. `q = -1`, the residue-ring specialisation the prose
      describes). No ordering, no radical, no `Real.*` construct appears, so
      per AGENTS.md §7c this belongs over a generic commutative ring. -/
  q : R
  /-- The q-integer `[2]_q = q + 1`. -/
  q_int_2 : R
  q_int_2_eq : q_int_2 = q + 1
  /-- Descartes specialisation: `χ(A) = -6` (Bring's surface). -/
  chi_A_eq : chi_A = -6

/-- **Kummer-level-2 obstruction removable** := the level-2 Kummer obstruction
    *vanishes*. This is the manuscript's own identity — *"the obstruction vanishes;
    this means the `[2]_q`-divisor is removable"* — i.e. in Kummer theory the
    obstruction class **is** the removability criterion. -/
def kummer_obstruction_removable (R : Type*) [CommRing R]
    [CollatzContactBoundaryContext R] : Prop :=
  QouObstructionReductionContext.kappa_vanishes 2

/-- **`2 ∣ χ(A)` ⟹ the `[2]_q`-divisor is Kummer-removable — DERIVED** (formerly a
    raw context-class axiom `obstruction_removable_of_even_chi`). Removability is
    the vanishing of the level-2 obstruction (`kummer_obstruction_removable`), and
    `kappa_vanishes_iff_chi` reduces that vanishing to `2 ∣ χ(A)`. So the parity
    condition now discharges removability through the universal obstruction, with
    no independent assumption. -/
theorem obstruction_removable_of_even_chi {R : Type*} [CommRing R]
    [ctx : CollatzContactBoundaryContext R] (h : (2 : ℤ) ∣ ctx.chi_A) :
    kummer_obstruction_removable R := by
  unfold kummer_obstruction_removable
  exact (kappa_vanishes_iff_chi 2).mpr (by simpa using h)

/-! ## Unconditional Algebraic & Contractive Identities of the `[2]_q`-Contact Boundary

The following definitions and theorems formalize the unconditional algebraic
and analytic content of `appendix-surreals/collatz-contact-boundary.md`:
1. Over any `[CommRing R]`, the unbalanced quantum integers `[2]_q = 1 + q`
   and `[3]_q = 1 + q + q²` satisfy the contact margin identity
   `[2]_q² - [3]_q = q`.
2. Over any `[Field K]`, the per-cycle contraction ratio decomposes as
   `[3]_q / [2]_q³ = 1 / [2]_q - q / [2]_q³`.
3. Over `ℝ` for every `q > 0`:
   - `1 < [2]_q < [3]_q < [2]_q² < [2]_q³`,
   - `0 < [3]_q / [2]_q³ < 1 / [2]_q < 1`,
   - the sharp threshold `v*(q) = log [3]_q / log [2]_q` satisfies
     `1 < v*(q) < 2`, avoiding transcendental bounds via the integer
     contact threshold `v ≥ 2`,
   - any non-negative sequence `P : ℕ → ℝ` satisfying the per-cycle contact
     bound `P (m + 1) ≤ ([3]_q / [2]_q^v) * P m` with `v ≥ 2` and `q > 0`
     converges geometrically to `0` (`Filter.Tendsto P Filter.atTop (nhds 0)`). -/

/-- Unbalanced quantum integer `[2]_q = 1 + q` over any commutative ring `R`. -/
def qInt2Unbal {R : Type*} [CommRing R] (q : R) : R := 1 + q

/-- Unbalanced quantum integer `[3]_q = 1 + q + q²` over any commutative ring `R`. -/
def qInt3Unbal {R : Type*} [CommRing R] (q : R) : R := 1 + q + q ^ 2

/-- **Contact margin identity (`[2]_q² - [3]_q = q`)** over any `[CommRing R]`. -/
theorem qInt2Unbal_sq_sub_qInt3Unbal {R : Type*} [CommRing R] (q : R) :
    (qInt2Unbal q) ^ 2 - qInt3Unbal q = q := by
  unfold qInt2Unbal qInt3Unbal
  ring

/-- **Contraction ratio decomposition (`[3]_q / [2]_q³ = 1 / [2]_q - q / [2]_q³`)**
    over any `[Field K]` whenever `[2]_q ≠ 0`. -/
theorem collatz_contraction_ratio_decomp {K : Type*} [Field K] (q : K)
    (hq : qInt2Unbal q ≠ 0) :
    qInt3Unbal q / (qInt2Unbal q) ^ 3 =
      1 / qInt2Unbal q - q / (qInt2Unbal q) ^ 3 := by
  have hmargin : qInt3Unbal q = (qInt2Unbal q) ^ 2 - q := by
    linear_combination -qInt2Unbal_sq_sub_qInt3Unbal q
  rw [hmargin]
  field_simp [hq]

/-- Over `ℝ`, for `q > 0`, `1 < [2]_q`. -/
theorem one_lt_qInt2Unbal {q : ℝ} (hq : 0 < q) : 1 < qInt2Unbal q := by
  unfold qInt2Unbal; linarith

/-- Over `ℝ`, for `q > 0`, `[2]_q < [3]_q`. -/
theorem qInt2Unbal_lt_qInt3Unbal {q : ℝ} (hq : 0 < q) :
    qInt2Unbal q < qInt3Unbal q := by
  unfold qInt2Unbal qInt3Unbal
  have : 0 < q ^ 2 := sq_pos_of_pos hq
  linarith

/-- Over `ℝ`, for `q > 0`, `[3]_q < [2]_q²`. -/
theorem qInt3Unbal_lt_qInt2Unbal_sq {q : ℝ} (hq : 0 < q) :
    qInt3Unbal q < (qInt2Unbal q) ^ 2 := by
  have h := qInt2Unbal_sq_sub_qInt3Unbal q
  linarith

/-- Over `ℝ`, for `q > 0`, the two-halving per-cycle factor `[3]_q / [2]_q³` is
    strictly positive, strictly less than `1 / [2]_q`, and `1 / [2]_q < 1`. -/
theorem collatz_contraction_ratio_bounds {q : ℝ} (hq : 0 < q) :
    0 < qInt3Unbal q / (qInt2Unbal q) ^ 3 ∧
    qInt3Unbal q / (qInt2Unbal q) ^ 3 < 1 / qInt2Unbal q ∧
    1 / qInt2Unbal q < 1 := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have h3_gt2 : qInt2Unbal q < qInt3Unbal q := qInt2Unbal_lt_qInt3Unbal hq
  have h3_pos : 0 < qInt3Unbal q := by linarith
  have h3_lt_sq : qInt3Unbal q < (qInt2Unbal q) ^ 2 := qInt3Unbal_lt_qInt2Unbal_sq hq
  have h2_cube_pos : 0 < (qInt2Unbal q) ^ 3 := pow_pos h2_pos 3
  refine ⟨div_pos h3_pos h2_cube_pos, ?_, ?_⟩
  · rw [collatz_contraction_ratio_decomp q (ne_of_gt h2_pos)]
    have hq_div_pos : 0 < q / (qInt2Unbal q) ^ 3 := div_pos hq h2_cube_pos
    linarith
  · rw [div_lt_iff₀ h2_pos]
    linarith

/-- **Sharp logarithmic threshold (`1 < log [3]_q / log [2]_q < 2`)** for every `q > 0`. -/
theorem collatz_sharp_threshold_in_unit_interval {q : ℝ} (hq : 0 < q) :
    1 < Real.log (qInt3Unbal q) / Real.log (qInt2Unbal q) ∧
    Real.log (qInt3Unbal q) / Real.log (qInt2Unbal q) < 2 := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have h3_gt2 : qInt2Unbal q < qInt3Unbal q := qInt2Unbal_lt_qInt3Unbal hq
  have h3_pos : 0 < qInt3Unbal q := by linarith
  have h3_lt_sq : qInt3Unbal q < (qInt2Unbal q) ^ 2 := qInt3Unbal_lt_qInt2Unbal_sq hq
  have hlog2_pos : 0 < Real.log (qInt2Unbal q) := Real.log_pos h2_gt1
  constructor
  · rw [one_lt_div hlog2_pos]
    exact Real.log_lt_log h2_pos h3_gt2
  · rw [div_lt_iff₀ hlog2_pos]
    have hlog_sq : Real.log ((qInt2Unbal q) ^ 2) = 2 * Real.log (qInt2Unbal q) := by
      rw [Real.log_pow]; norm_num
    rw [← hlog_sq]
    exact Real.log_lt_log h3_pos h3_lt_sq

/-- For any `q > 0` and integer valuation `v ≥ 2`, the per-cycle contraction factor
    `r = [3]_q / [2]_q^v` satisfies `0 ≤ r < 1`. -/
theorem collatz_step_factor_in_unit_interval {q : ℝ} (hq : 0 < q) {v : ℕ} (hv : 2 ≤ v) :
    0 ≤ qInt3Unbal q / (qInt2Unbal q) ^ v ∧
    qInt3Unbal q / (qInt2Unbal q) ^ v < 1 := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have h3_gt2 : qInt2Unbal q < qInt3Unbal q := qInt2Unbal_lt_qInt3Unbal hq
  have h3_pos : 0 < qInt3Unbal q := by linarith
  have h3_lt_sq : qInt3Unbal q < (qInt2Unbal q) ^ 2 := qInt3Unbal_lt_qInt2Unbal_sq hq
  have hpow_pos : 0 < (qInt2Unbal q) ^ v := pow_pos h2_pos v
  have hpow_mono : (qInt2Unbal q) ^ 2 ≤ (qInt2Unbal q) ^ v :=
    pow_le_pow_right₀ (le_of_lt h2_gt1) hv
  refine ⟨le_of_lt (div_pos h3_pos hpow_pos), ?_⟩
  rw [div_lt_iff₀ hpow_pos]
  linarith

/-- Inductive bound on `P m` under per-cycle contraction `P (m + 1) ≤ r * P m`. -/
theorem collatz_orbit_geometric_bound {P : ℕ → ℝ} {r : ℝ} (hr0 : 0 ≤ r)
    (hstep : ∀ m : ℕ, P (m + 1) ≤ r * P m) :
    ∀ m : ℕ, P m ≤ r ^ m * P 0
  | 0 => by simp
  | m + 1 => by
    have ih := collatz_orbit_geometric_bound hr0 hstep m
    calc P (m + 1) ≤ r * P m := hstep m
      _ ≤ r * (r ^ m * P 0) := mul_le_mul_of_nonneg_left ih hr0
      _ = r ^ (m + 1) * P 0 := by ring

/-- **Geometric orbit convergence under the `[2]_q`-contact condition `v ≥ 2`.**
    If `P : ℕ → ℝ` is non-negative and satisfies the per-cycle contraction
    `P (m + 1) ≤ ([3]_q / [2]_q^v) * P m` for some integer contact valuation
    `v ≥ 2` and `q > 0`, then `Filter.Tendsto P Filter.atTop (nhds 0)`. -/
theorem collatz_orbit_tendsto_zero {P : ℕ → ℝ} {q : ℝ} (hq : 0 < q) {v : ℕ} (hv : 2 ≤ v)
    (hP_nonneg : ∀ m : ℕ, 0 ≤ P m)
    (hstep : ∀ m : ℕ, P (m + 1) ≤ (qInt3Unbal q / (qInt2Unbal q) ^ v) * P m) :
    Filter.Tendsto P Filter.atTop (nhds 0) := by
  set r := qInt3Unbal q / (qInt2Unbal q) ^ v
  obtain ⟨hr0, hr1⟩ := collatz_step_factor_in_unit_interval hq hv
  have hbound : ∀ m : ℕ, P m ≤ r ^ m * P 0 := collatz_orbit_geometric_bound hr0 hstep
  have htend_pow : Filter.Tendsto (fun m : ℕ => r ^ m) Filter.atTop (nhds 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one hr0 hr1
  have htend_mul : Filter.Tendsto (fun m : ℕ => r ^ m * P 0) Filter.atTop (nhds 0) := by
    simpa using htend_pow.mul_const (P 0)
  exact squeeze_zero hP_nonneg hbound htend_mul

/-- **`[2]_q`-Contact Boundary Theorem** (`prop:collatz-contact-boundary`):
    Combines Kummer-divisor removability at `2 ∣ χ(A)` with the contact margin
    identity `[2]_q² - [3]_q = q` (paired with `collatz_contraction_ratio_bounds`,
    `collatz_sharp_threshold_in_unit_interval`, and `collatz_orbit_tendsto_zero` above). -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts
theorem collatz_contact_boundary {R : Type*} [CommRing R]
    [ctx : CollatzContactBoundaryContext R] :
    (ctx.q_int_2 = 0 → kummer_obstruction_removable R) ∧
    ((2 : ℤ) ∣ ctx.chi_A) ∧
    (qInt2Unbal ctx.q) ^ 2 - qInt3Unbal ctx.q = ctx.q := by
  have h1 : (2 : ℤ) ∣ ctx.chi_A := by
    rw [ctx.chi_A_eq]; exact ⟨-3, rfl⟩
  exact ⟨fun _ => obstruction_removable_of_even_chi (R := R) h1, h1,
    qInt2Unbal_sq_sub_qInt3Unbal ctx.q⟩

end QOU.AlgebraicSubstrate
