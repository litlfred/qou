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

/-! ### General Parity Removability, `v = 2` Contraction, & Affine Syracuse Iff Characterization -/

/-- **General QOU Kummer removability without hardcoding `χ(A) = -6`:**
    in ANY `QouObstructionReductionContext` whose Euler characteristic equals `chi : ℤ`,
    the level-2 Kummer obstruction vanishes if and only if `(2 : ℤ) ∣ chi`. -/
theorem general_even_chi_kummer_removable [ctx : QouObstructionReductionContext]
    (chi : ℤ) (hchi : ctx.chi_A = chi) :
    ((2 : ℤ) ∣ chi) ↔ QouObstructionReductionContext.kappa_vanishes 2 := by
  rw [kappa_vanishes_iff_chi 2, hchi]
  norm_num

/-- Concrete witness `QouObstructionReductionContext` parameterized by ANY integer
    `chi : ℤ` (not merely `chi = -6`), confirming `general_even_chi_kummer_removable`
    is non-vacuous across all even and odd Euler characteristics. -/
def qouObstructionOfChi (chi : ℤ) : QouObstructionReductionContext where
  hhCohDim i := if i = 2 then 1 else 0
  hhHomDim i := if i = 1 then 1 else 0
  vdb_duality i hi := by interval_cases i <;> rfl
  drinfeld_rigidity := rfl
  chi_A := chi
  phi_1_image := (chi : ℝ)
  kappa0 := chi
  kappa_vanishes n := (n : ℤ) ∣ chi
  kappa_vanishes_def _ := Iff.rfl
  trace_pairing z := (z : ℝ)
  hattori_stallings := rfl
  trace_pairing_cast _ := rfl
  chern_character := rfl

theorem general_even_chi_kummer_removable_witnessed (chi : ℤ) :
    letI := qouObstructionOfChi chi
    (qouObstructionOfChi chi).chi_A = chi ∧
    (((2 : ℤ) ∣ chi) ↔ @QouObstructionReductionContext.kappa_vanishes (qouObstructionOfChi chi) 2) := by
  letI := qouObstructionOfChi chi
  exact ⟨rfl, general_even_chi_kummer_removable chi rfl⟩

/-- **Exact `v = 2` two-halving contraction identity and bounds** (`[3]_q / [2]_q² = 1 - q / [2]_q² ∈ (0, 1)`)
    for every `q > 0`, matching the prose threshold `v = 2`. -/
theorem collatz_two_halving_contraction_bounds {q : ℝ} (hq : 0 < q) :
    0 < qInt3Unbal q / (qInt2Unbal q) ^ 2 ∧
    qInt3Unbal q / (qInt2Unbal q) ^ 2 = 1 - q / (qInt2Unbal q) ^ 2 ∧
    qInt3Unbal q / (qInt2Unbal q) ^ 2 < 1 := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have h3_gt2 : qInt2Unbal q < qInt3Unbal q := qInt2Unbal_lt_qInt3Unbal hq
  have h3_pos : 0 < qInt3Unbal q := by linarith
  have hsq_pos : 0 < (qInt2Unbal q) ^ 2 := sq_pos_of_pos h2_pos
  have hmargin : qInt3Unbal q = (qInt2Unbal q) ^ 2 - q := by
    linear_combination -qInt2Unbal_sq_sub_qInt3Unbal q
  have hdecomp : qInt3Unbal q / (qInt2Unbal q) ^ 2 = 1 - q / (qInt2Unbal q) ^ 2 := by
    rw [hmargin]
    field_simp [ne_of_gt h2_pos]
  refine ⟨div_pos h3_pos hsq_pos, hdecomp, ?_⟩
  rw [hdecomp]
  have hq_div_pos : 0 < q / (qInt2Unbal q) ^ 2 := div_pos hq hsq_pos
  linarith

/-- Compressed affine Syracuse step `x ↦ ([3]_q x + 1) / [2]_q^v`. -/
noncomputable def syracuseStep (q : ℝ) (v : ℕ) (x : ℝ) : ℝ :=
  (qInt3Unbal q * x + 1) / (qInt2Unbal q) ^ v

/-- Unique affine Syracuse fixed point `P_* = 1 / ([2]_q^v - [3]_q)`. -/
noncomputable def syracuseFixedPoint (q : ℝ) (v : ℕ) : ℝ :=
  1 / ((qInt2Unbal q) ^ v - qInt3Unbal q)

/-- For `q > 0` and `v ≥ 2`, the denominator `[2]_q^v - [3]_q` is `≥ q > 0`, so
    `0 < P_* ≤ 1 / q` (and `P_* = 1 / q` at the boundary `v = 2`). -/
theorem syracuseFixedPoint_pos_and_le_inv_q {q : ℝ} (hq : 0 < q) {v : ℕ} (hv : 2 ≤ v) :
    0 < syracuseFixedPoint q v ∧ syracuseFixedPoint q v ≤ 1 / q ∧
      syracuseFixedPoint q 2 = 1 / q := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have hpow_ge : (qInt2Unbal q) ^ 2 ≤ (qInt2Unbal q) ^ v :=
    pow_le_pow_right₀ h2_gt1.le hv
  have hmargin := qInt2Unbal_sq_sub_qInt3Unbal q
  have hdenom_ge : q ≤ (qInt2Unbal q) ^ v - qInt3Unbal q := by linarith
  have hdenom_pos : 0 < (qInt2Unbal q) ^ v - qInt3Unbal q := lt_of_lt_of_le hq hdenom_ge
  refine ⟨div_pos one_pos hdenom_pos, ?_, ?_⟩
  · exact one_div_le_one_div_of_le hq hdenom_ge
  · unfold syracuseFixedPoint
    rw [hmargin]

/-- For `q > 0` and `v ≥ 2`, `syracuseFixedPoint q v` is the **unique** fixed point of
    `syracuseStep q v`. -/
theorem syracuseStep_fixedPoint_iff {q : ℝ} (hq : 0 < q) {v : ℕ} (hv : 2 ≤ v) (x : ℝ) :
    syracuseStep q v x = x ↔ x = syracuseFixedPoint q v := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have hpow_pos : 0 < (qInt2Unbal q) ^ v := pow_pos h2_pos v
  have hpow_ge : (qInt2Unbal q) ^ 2 ≤ (qInt2Unbal q) ^ v :=
    pow_le_pow_right₀ h2_gt1.le hv
  have hmargin := qInt2Unbal_sq_sub_qInt3Unbal q
  have hdenom_pos : 0 < (qInt2Unbal q) ^ v - qInt3Unbal q := by linarith
  have hdenom_ne : (qInt2Unbal q) ^ v - qInt3Unbal q ≠ 0 := ne_of_gt hdenom_pos
  unfold syracuseStep syracuseFixedPoint
  rw [div_eq_iff (ne_of_gt hpow_pos)]
  constructor
  · intro hx
    have hlin : ((qInt2Unbal q) ^ v - qInt3Unbal q) * x = 1 := by linarith
    exact (eq_div_iff_mul_eq hdenom_ne).mpr (by linarith)
  · intro hx
    rw [hx]
    field_simp [hdenom_ne]
    ring

/-- Exact geometric contraction of the affine error `P m - P_*` around `syracuseFixedPoint q v`. -/
theorem syracuse_affine_error_pow {P : ℕ → ℝ} {q : ℝ} (hq : 0 < q) {v : ℕ} (hv : 2 ≤ v)
    (hstep : ∀ m : ℕ, P (m + 1) = (qInt3Unbal q * P m + 1) / (qInt2Unbal q) ^ v) :
    ∀ m : ℕ, P m - syracuseFixedPoint q v =
      (qInt3Unbal q / (qInt2Unbal q) ^ v) ^ m * (P 0 - syracuseFixedPoint q v)
  | 0 => by simp
  | m + 1 => by
    have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
    have h2_pos : 0 < qInt2Unbal q := by linarith
    have hpow_ne : (qInt2Unbal q) ^ v ≠ 0 := ne_of_gt (pow_pos h2_pos v)
    have hfp : (qInt3Unbal q * syracuseFixedPoint q v + 1) / (qInt2Unbal q) ^ v =
        syracuseFixedPoint q v :=
      (syracuseStep_fixedPoint_iff hq hv (syracuseFixedPoint q v)).mpr rfl
    have hdiff : P (m + 1) - syracuseFixedPoint q v =
        (qInt3Unbal q / (qInt2Unbal q) ^ v) * (P m - syracuseFixedPoint q v) := by
      conv_lhs => rw [hstep m, ← hfp]
      field_simp [hpow_ne]
      ring
    rw [hdiff, syracuse_affine_error_pow hq hv hstep m]
    ring

/-- **Strict divergence for `v ≤ 1`:** when `q > 0`, `v ≤ 1`, and `0 < P 0`, the affine
    Syracuse orbit `P (m + 1) = ([3]_q P m + 1) / [2]_q^v` is strictly increasing and
    diverges strictly to `+∞` (`Filter.Tendsto P Filter.atTop Filter.atTop`). -/
theorem syracuse_affine_diverges_of_le_one {P : ℕ → ℝ} {q : ℝ} (hq : 0 < q)
    {v : ℕ} (hv : v ≤ 1) (hP0 : 0 < P 0)
    (hstep : ∀ m : ℕ, P (m + 1) = (qInt3Unbal q * P m + 1) / (qInt2Unbal q) ^ v) :
    (∀ m : ℕ, P m < P (m + 1)) ∧ Filter.Tendsto P Filter.atTop Filter.atTop := by
  have h2_gt1 : 1 < qInt2Unbal q := one_lt_qInt2Unbal hq
  have h2_pos : 0 < qInt2Unbal q := by linarith
  have h3_gt2 : qInt2Unbal q < qInt3Unbal q := qInt2Unbal_lt_qInt3Unbal hq
  have h3_pos : 0 < qInt3Unbal q := by linarith
  have hpow_pos : 0 < (qInt2Unbal q) ^ v := pow_pos h2_pos v
  have hpow_lt3 : (qInt2Unbal q) ^ v < qInt3Unbal q := by
    interval_cases v
    · simp; linarith
    · simpa using h3_gt2
  have hP_pos : ∀ m : ℕ, 0 < P m := by
    intro m
    induction m with
    | zero => exact hP0
    | succ m ih =>
      rw [hstep m]
      exact div_pos (by nlinarith) hpow_pos
  set c : ℝ := 1 / (qInt2Unbal q) ^ v
  have hc_pos : 0 < c := div_pos one_pos hpow_pos
  have hinc : ∀ m : ℕ, P m + c < P (m + 1) := by
    intro m
    rw [hstep m]
    have hnum : (qInt2Unbal q) ^ v * P m + 1 < qInt3Unbal q * P m + 1 := by
      nlinarith [hP_pos m]
    have hdiv : ((qInt2Unbal q) ^ v * P m + 1) / (qInt2Unbal q) ^ v <
        (qInt3Unbal q * P m + 1) / (qInt2Unbal q) ^ v :=
      div_lt_div_of_pos_right hnum hpow_pos
    have hlhs : ((qInt2Unbal q) ^ v * P m + 1) / (qInt2Unbal q) ^ v = P m + c := by
      unfold c
      field_simp [ne_of_gt hpow_pos]
    linarith
  have hlin_bound : ∀ m : ℕ, P 0 + (m : ℝ) * c ≤ P m := by
    intro m
    induction m with
    | zero => simp
    | succ m ih =>
      have hm := hinc m
      push_cast
      linarith
  refine ⟨fun m => by linarith [hinc m], Filter.tendsto_atTop.mpr ?_⟩
  intro B
  rw [Filter.eventually_atTop]
  obtain ⟨N, hN⟩ := exists_nat_gt ((B - P 0) / c)
  refine ⟨N, fun m hm => ?_⟩
  have hNm : (N : ℝ) ≤ (m : ℝ) := Nat.cast_le.mpr hm
  have hgt : B - P 0 < (m : ℝ) * c := by
    have h1 : B - P 0 < (N : ℝ) * c := (div_lt_iff₀ hc_pos).mp hN
    have h2 : (N : ℝ) * c ≤ (m : ℝ) * c := mul_le_mul_of_nonneg_right hNm hc_pos.le
    linarith
  linarith [hlin_bound m]

/-- **Complete two-way `iff` characterization of affine Syracuse convergence and boundedness:**
    for every `q > 0`, constant valuation `v : ℕ`, and orbit `P : ℕ → ℝ` with `0 < P 0` and
    `P (m + 1) = ([3]_q P m + 1) / [2]_q^v`:
    1. When `2 ≤ v`, `syracuseFixedPoint q v > 0` is the unique fixed point and
       `|P m - syracuseFixedPoint q v| → 0`;
    2. `(∃ P_star > 0, |P m - P_star| → 0) ↔ 2 ≤ v` (**both** directions of `iff`);
    3. `(∃ B : ℝ, ∀ m : ℕ, P m ≤ B) ↔ 2 ≤ v` (**both** directions of `iff`). -/
theorem syracuse_affine_converges_and_bounded_iff {P : ℕ → ℝ} {q : ℝ} (hq : 0 < q)
    (v : ℕ) (hP0 : 0 < P 0)
    (hstep : ∀ m : ℕ, P (m + 1) = (qInt3Unbal q * P m + 1) / (qInt2Unbal q) ^ v) :
    ((∃ P_star : ℝ, 0 < P_star ∧
        Filter.Tendsto (fun m : ℕ => |P m - P_star|) Filter.atTop (nhds 0)) ↔ 2 ≤ v) ∧
    ((∃ B : ℝ, ∀ m : ℕ, P m ≤ B) ↔ 2 ≤ v) := by
  have hconv_of_ge : 2 ≤ v →
      (0 < syracuseFixedPoint q v ∧
        Filter.Tendsto (fun m : ℕ => |P m - syracuseFixedPoint q v|) Filter.atTop (nhds 0)) ∧
      (∃ B : ℝ, ∀ m : ℕ, P m ≤ B) := by
    intro hv
    obtain ⟨hfp_pos, _, _⟩ := syracuseFixedPoint_pos_and_le_inv_q hq hv
    obtain ⟨hr0, hr1⟩ := collatz_step_factor_in_unit_interval hq hv
    set r := qInt3Unbal q / (qInt2Unbal q) ^ v
    have herr : ∀ m : ℕ, |P m - syracuseFixedPoint q v| =
        r ^ m * |P 0 - syracuseFixedPoint q v| := by
      intro m
      rw [syracuse_affine_error_pow hq hv hstep m, abs_mul, abs_of_nonneg (pow_nonneg hr0 m)]
    have htend_pow : Filter.Tendsto (fun m : ℕ => r ^ m) Filter.atTop (nhds 0) :=
      tendsto_pow_atTop_nhds_zero_of_lt_one hr0 hr1
    have htend_err : Filter.Tendsto (fun m : ℕ => |P m - syracuseFixedPoint q v|)
        Filter.atTop (nhds 0) := by
      have hfun : (fun m : ℕ => |P m - syracuseFixedPoint q v|) =
          (fun m : ℕ => r ^ m * |P 0 - syracuseFixedPoint q v|) := funext herr
      rw [hfun]
      simpa using htend_pow.mul_const |P 0 - syracuseFixedPoint q v|
    have hbd : ∃ B : ℝ, ∀ m : ℕ, P m ≤ B := by
      refine ⟨syracuseFixedPoint q v + |P 0 - syracuseFixedPoint q v|, fun m => ?_⟩
      have hrm_le : r ^ m ≤ 1 := pow_le_one₀ hr0 hr1.le
      have habs_le : |P m - syracuseFixedPoint q v| ≤ |P 0 - syracuseFixedPoint q v| := by
        rw [herr]
        exact mul_le_of_le_one_left (abs_nonneg _) hrm_le
      have hle_abs : P m - syracuseFixedPoint q v ≤ |P m - syracuseFixedPoint q v| :=
        le_abs_self _
      linarith
    exact ⟨⟨hfp_pos, htend_err⟩, hbd⟩
  have hnot_bd_of_le_one : v ≤ 1 → ¬ ∃ B : ℝ, ∀ m : ℕ, P m ≤ B := by
    intro hv ⟨B, hB⟩
    have hdiv := (syracuse_affine_diverges_of_le_one hq hv hP0 hstep).2
    rw [Filter.tendsto_atTop] at hdiv
    have hev := hdiv (B + 1)
    rw [Filter.eventually_atTop] at hev
    obtain ⟨N, hN⟩ := hev
    linarith [hN N le_rfl, hB N]
  refine ⟨⟨?_, fun hv => ?_⟩, ⟨?_, fun hv => (hconv_of_ge hv).2⟩⟩
  · rintro ⟨P_star, _, htend⟩
    by_contra hlt
    have hv1 : v ≤ 1 := by omega
    have hdiv := (syracuse_affine_diverges_of_le_one hq hv1 hP0 hstep).2
    rw [Filter.tendsto_atTop] at hdiv
    have hev1 := hdiv (P_star + 2)
    have hev2 := (tendsto_order.mp htend).2 1 zero_lt_one
    rw [Filter.eventually_atTop] at hev1 hev2
    obtain ⟨N₁, hN₁⟩ := hev1
    obtain ⟨N₂, hN₂⟩ := hev2
    set M := max N₁ N₂
    have h1 : P_star + 2 ≤ P M := hN₁ M (le_max_left _ _)
    have h2 : |P M - P_star| < 1 := hN₂ M (le_max_right _ _)
    have h3 : P M - P_star ≤ |P M - P_star| := le_abs_self _
    linarith
  · obtain ⟨⟨hfp_pos, htend⟩, _⟩ := hconv_of_ge hv
    exact ⟨syracuseFixedPoint q v, hfp_pos, htend⟩
  · intro hbd
    by_contra hlt
    exact hnot_bd_of_le_one (by omega) hbd

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

/-- Archimedean `(R := ℝ)` specialisation of `collatz_contact_boundary` (§7c `_real` pair). -/
theorem collatz_contact_boundary_real [ctx : CollatzContactBoundaryContext ℝ] :
    (ctx.q_int_2 = 0 → kummer_obstruction_removable ℝ) ∧
    ((2 : ℤ) ∣ ctx.chi_A) ∧
    (qInt2Unbal ctx.q) ^ 2 - qInt3Unbal ctx.q = ctx.q :=
  collatz_contact_boundary (R := ℝ)

end QOU.AlgebraicSubstrate
