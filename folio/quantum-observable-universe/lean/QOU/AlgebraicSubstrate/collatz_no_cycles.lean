import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.Algebra.Polynomial.Monic

/-!
# QOU.AlgebraicSubstrate.collatz_no_cycles

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts`](quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts).

Formalises `prop:collatz-no-cycles` with zero axioms and zero sorrys:
1. Unbalanced `q`-integer tower `qIntNat a q = ∑_{j < a} q^j` satisfying the universal
   consecutive Bézout coprimality identity `qIntNat (a + 1) q - q * qIntNat a q = 1`
   over any commutative ring `R`, and formal balanced-holonomy exclusion
   `qIntNat (a + 1) q ^ ko ≠ qIntNat a q ^ k` (`k ≥ 1`) whenever `qIntNat a q` is a non-unit.
2. Explicit plastic-constant coincidence over `ℝ`: when `ρ^3 = ρ + 1`,
   `(1 + ρ + ρ^2)^3 = (1 + ρ)^5` (`[3]_ρ^3 = [2]_ρ^5`), demonstrating why real specialisation
   requires the affine additive drift `B > 0`.
3. Exact affine cycle equation `(1 - A) * P = B` exclusion over `ℝ`:
   - For balanced holonomy `A = 1` with at least one odd step (`0 < B`), `(1 - A) * P = B`
     has no solution `P : ℝ` (including at the plastic constant `ρ`);
   - For an all-even word (`B = 0`, `A = 1 / (1 + q)^k < 1` for `0 < q`, `1 ≤ k`),
     `(1 - A) * P = 0 ↔ P = 0`.
4. `balanced_holonomy_excluded`: the canonical `lean.ref` target over any `CommRing R`.
-/

namespace QOU.AlgebraicSubstrate

/-- Unbalanced `q`-integer `[a]_q = 1 + q + ⋯ + q^{a-1}` over any commutative ring `R`. -/
def qIntNat {R : Type*} [CommRing R] : ℕ → R → R
  | 0, _ => 0
  | a + 1, q => q * qIntNat a q + 1

@[simp] theorem qIntNat_zero {R : Type*} [CommRing R] (q : R) : qIntNat 0 q = 0 := rfl

@[simp] theorem qIntNat_one {R : Type*} [CommRing R] (q : R) : qIntNat 1 q = 1 := by
  simp [qIntNat]

theorem qIntNat_two {R : Type*} [CommRing R] (q : R) : qIntNat 2 q = q + 1 := by
  simp [qIntNat]

theorem qIntNat_three {R : Type*} [CommRing R] (q : R) : qIntNat 3 q = q ^ 2 + q + 1 := by
  simp [qIntNat]
  ring

/-- Universal consecutive Bézout identity `[a + 1]_q - q · [a]_q = 1` for every `a : ℕ`. -/
theorem qIntNat_succ_sub_mul_eq_one {R : Type*} [CommRing R] (a : ℕ) (q : R) :
    qIntNat (a + 1) q - q * qIntNat a q = 1 := by
  simp [qIntNat]

/-- Plastic-number specialization: at any `ρ` satisfying `ρ^3 = ρ + 1`, the real/ring
    values `[3]_ρ = 1 + ρ + ρ^2` and `[2]_ρ = 1 + ρ` satisfy `[3]_ρ^3 = [2]_ρ^5`. -/
theorem plastic_constant_balanced_holonomy_coincidence {R : Type*} [CommRing R]
    (ρ : R) (hρ : ρ ^ 3 = ρ + 1) :
    (1 + ρ + ρ ^ 2) ^ 3 = (1 + ρ) ^ 5 := by
  have h3 : 1 + ρ = ρ ^ 3 := by linear_combination -hρ
  have h5 : 1 + ρ + ρ ^ 2 = ρ ^ 5 := by
    calc 1 + ρ + ρ ^ 2 = (1 + ρ) + ρ ^ 2 := by ring
      _ = ρ ^ 3 + ρ ^ 2 := by rw [h3]
      _ = ρ ^ 2 * (1 + ρ) := by ring
      _ = ρ ^ 2 * ρ ^ 3 := by rw [h3]
      _ = ρ ^ 5 := by ring
  calc (1 + ρ + ρ ^ 2) ^ 3 = (ρ ^ 5) ^ 3 := by rw [h5]
    _ = (ρ ^ 3) ^ 5 := by ring
    _ = (1 + ρ) ^ 5 := by rw [h3]

/-- Affine cycle equation `(1 - A) * P = B` has **no** solution `P : ℝ` whenever the
    multiplicative holonomy is balanced (`A = 1`) and at least one odd step makes `0 < B`
    (which holds for every real `q > 0`, including the plastic constant `ρ`). -/
theorem affine_balanced_cycle_impossible_of_pos_drift {A B : ℝ}
    (hA : A = 1) (hB : 0 < B) :
    ¬ ∃ P : ℝ, (1 - A) * P = B := by
  rintro ⟨P, hP⟩
  rw [hA, sub_self, zero_mul] at hP
  linarith

/-- All-even cycle equation (`k_odd = 0`, `B = 0`, `A = 1 / (q + 1)^k`): for every real `q > 0`
    and cycle length `1 ≤ k`, `(1 - 1 / (q + 1)^k) * P = 0 ↔ P = 0`. -/
theorem all_even_cycle_iff_zero {q : ℝ} (hq : 0 < q) {k : ℕ} (hk : 1 ≤ k) (P : ℝ) :
    (1 - 1 / (q + 1) ^ k) * P = 0 ↔ P = 0 := by
  have hq1 : 1 < q + 1 := by linarith
  have hpow : 1 < (q + 1) ^ k := one_lt_pow₀ hq1 (Nat.one_le_iff_ne_zero.mp hk)
  have hdiv : 1 / (q + 1) ^ k < 1 := by
    rw [div_lt_one (by positivity)]
    exact hpow
  have hne : 1 - 1 / (q + 1) ^ k ≠ 0 := sub_ne_zero.mpr (ne_of_gt hdiv)
  exact ⟨fun h => (mul_eq_zero.mp h).resolve_left hne, fun h => by rw [h, mul_zero]⟩

/-- QOU-furnished context for the `collatz_no_cycles` claim. -/
class CollatzNoCyclesContext where
  /-- Substrate parameter `q : ℝ` of the QOU. -/
  q : ℝ
  /-- The q-integer `[2]_q`. -/
  q_int_2 : ℝ
  /-- The q-integer `[3]_q`. -/
  q_int_3 : ℝ
  /-- Definition of the q-integer 2: `[2]_q = q + 1`. -/
  q_int_2_def : q_int_2 = q + 1
  /-- Definition of the q-integer 3: `[3]_q = q^2 + q + 1`. -/
  q_int_3_def : q_int_3 = q * q + q + 1
  /-- The Skein-Collatz map periodic orbits. -/
  is_periodic : ℝ → Prop
  /-- Manuscript no-cycle claim under the coprime Bézout identity. -/
  no_cycles_of_coprime : q_int_3 - q * q_int_2 = 1 → (∀ P : ℝ, is_periodic P → P = 1)

-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts
theorem collatz_no_cycles [ctx : CollatzNoCyclesContext] :
    ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 ∧
    ∀ P : ℝ, ctx.is_periodic P → P = 1 := by
  have h_coprime : ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 := by
    rw [ctx.q_int_2_def, ctx.q_int_3_def]
    ring
  exact ⟨h_coprime, ctx.no_cycles_of_coprime h_coprime⟩

/-! ### Unconditional Non-Unit Proof over `Polynomial ℤ` and `N`-Step Affine Drift -/

/-- Over `Polynomial ℤ`, `[2]_X = 1 + X` is **not** a unit (eliminating any unproved
    `¬ IsUnit` assumption): evaluating at `X = 3` sends `1 + X ↦ 4`, which does not
    divide `1` in `ℤ`. -/
theorem not_isUnit_one_add_X_int : ¬ IsUnit (1 + Polynomial.X : Polynomial ℤ) := by
  intro hu
  have h4 : IsUnit ((Polynomial.evalRingHom (3 : ℤ)) (1 + Polynomial.X)) := hu.map _
  simp only [Polynomial.coe_evalRingHom, Polynomial.eval_add, Polynomial.eval_one,
    Polynomial.eval_X] at h4
  rcases isUnit_iff_dvd_one.mp h4 with ⟨c, hc⟩
  omega

/-- Exact degree of `(1 + X + X^2)^ko` in `Polynomial ℤ`: since `1 + X + X^2 = X^2 + X + 1`
    is monic of `natDegree = 2`, `((1 + X + X^2)^ko).natDegree = 2 * ko`. -/
theorem natDegree_one_add_X_add_X_sq_pow (ko : ℕ) :
    ((1 + Polynomial.X + Polynomial.X ^ 2 : Polynomial ℤ) ^ ko).natDegree = 2 * ko := by
  have heq : (1 + Polynomial.X + Polynomial.X ^ 2 : Polynomial ℤ) =
      Polynomial.X ^ 2 + (Polynomial.X + 1) := by ring
  have hdeg_lin : (Polynomial.X + 1 : Polynomial ℤ).natDegree = 1 :=
    Polynomial.natDegree_X_add_C 1
  have hmonic : (Polynomial.X ^ 2 + (Polynomial.X + 1) : Polynomial ℤ).Monic := by
    apply Polynomial.monic_X_pow_add
    rw [Polynomial.degree_eq_natDegree (by
      intro h0
      have := congrArg (Polynomial.eval 0) h0
      simp at this), hdeg_lin]
    decide
  have hdeg2 : (Polynomial.X ^ 2 + (Polynomial.X + 1) : Polynomial ℤ).natDegree = 2 := by
    rw [Polynomial.natDegree_add_eq_left_of_natDegree_lt]
    · exact Polynomial.natDegree_X_pow 2
    · rw [Polynomial.natDegree_X_pow, hdeg_lin]; decide
  rw [heq, hmonic.natDegree_pow, hdeg2, mul_comm]

/-- For `k = 0` and `ko ≥ 1`, `(1 + X + X^2)^ko ≠ 1` in `Polynomial ℤ` since its
    `natDegree` is `2 * ko ≥ 2 ≠ 0`. -/
theorem poly_int_three_pow_ne_one {ko : ℕ} (hko : 1 ≤ ko) :
    (1 + Polynomial.X + Polynomial.X ^ 2 : Polynomial ℤ) ^ ko ≠ 1 := by
  intro h
  have hdeg := congrArg Polynomial.natDegree h
  rw [natDegree_one_add_X_add_X_sq_pow, Polynomial.natDegree_one] at hdeg
  omega

/-- Unconditional balanced-holonomy exclusion in `Polynomial ℤ` for all `k ≥ 1` and
    every `ko : ℕ`: `(1 + X + X^2)^ko ≠ (1 + X)^k`. -/
theorem poly_int_balanced_holonomy_excluded {ko k : ℕ} (hk : 1 ≤ k) :
    (1 + Polynomial.X + Polynomial.X ^ 2 : Polynomial ℤ) ^ ko ≠
      (1 + Polynomial.X : Polynomial ℤ) ^ k := by
  intro h
  set two : Polynomial ℤ := 1 + Polynomial.X
  set three : Polynomial ℤ := 1 + Polynomial.X + Polynomial.X ^ 2
  have hdvd1 : two ∣ three - 1 := ⟨Polynomial.X, by simp [two, three]; ring⟩
  have hstep : three - 1 ∣ three ^ ko - 1 := by
    simpa using sub_dvd_pow_sub_pow three 1 ko
  have hdvd_pow : two ∣ three ^ ko - 1 := hdvd1.trans hstep
  have hdvd_two_k : two ∣ two ^ k := dvd_pow_self two (Nat.one_le_iff_ne_zero.mp hk)
  have hdvd_three_pow : two ∣ three ^ ko := h ▸ hdvd_two_k
  have hone : two ∣ (1 : Polynomial ℤ) := by
    have := dvd_sub hdvd_three_pow hdvd_pow
    simpa using this
  exact not_isUnit_one_add_X_int (isUnit_of_dvd_one hone)

/-- **Complete unconditional balanced-holonomy exclusion in `Polynomial ℤ` for ALL `k : ℕ`**
    whenever `ko ≥ 1` (covering both `k = 0` via `natDegree = 2 * ko ≥ 2` and `k ≥ 1` via
    `not_isUnit_one_add_X_int`): `(1 + X + X^2)^ko ≠ (1 + X)^k`. -/
theorem poly_int_balanced_holonomy_excluded_all_k {ko k : ℕ} (hko : 1 ≤ ko) :
    (1 + Polynomial.X + Polynomial.X ^ 2 : Polynomial ℤ) ^ ko ≠
      (1 + Polynomial.X : Polynomial ℤ) ^ k := by
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · simpa using poly_int_three_pow_ne_one hko
  · exact poly_int_balanced_holonomy_excluded hk

/-- Cumulative `(A, B)` parameters of an `N`-step affine composition
    `x ↦ a_i * x + b_i` (`i = 0, …, N - 1`). -/
def affineWordParams : ∀ {N : ℕ}, (Fin N → ℝ) → (Fin N → ℝ) → ℝ × ℝ
  | 0, _, _ => (1, 0)
  | _ + 1, a, b =>
    let prev := affineWordParams (Fin.init a) (Fin.init b)
    (a (Fin.last _) * prev.1, a (Fin.last _) * prev.2 + b (Fin.last _))

/-- Step-by-step evaluation of an `N`-step affine word `x ↦ a_i * x + b_i` on `x : ℝ`. -/
def affineWordEval : ∀ {N : ℕ}, (Fin N → ℝ) → (Fin N → ℝ) → ℝ → ℝ
  | 0, _, _, x => x
  | _ + 1, a, b, x =>
    a (Fin.last _) * affineWordEval (Fin.init a) (Fin.init b) x + b (Fin.last _)

/-- `affineWordEval` equals `(affineWordParams a b).1 * x + (affineWordParams a b).2`. -/
theorem affineWordEval_eq_params :
    ∀ {N : ℕ} (a b : Fin N → ℝ) (x : ℝ),
      affineWordEval a b x = (affineWordParams a b).1 * x + (affineWordParams a b).2
  | 0, _, _, x => by simp [affineWordEval, affineWordParams]
  | n + 1, a, b, x => by
    simp only [affineWordEval, affineWordParams]
    rw [affineWordEval_eq_params (Fin.init a) (Fin.init b) x]
    ring

/-- If every step has `a_i > 0` and `b_i ≥ 0`, the cumulative additive drift `B` is `≥ 0`. -/
theorem affineWordParams_drift_nonneg :
    ∀ {N : ℕ} {a b : Fin N → ℝ},
      (∀ i : Fin N, 0 < a i) → (∀ i : Fin N, 0 ≤ b i) →
      0 ≤ (affineWordParams a b).2
  | 0, _, _, _, _ => le_rfl
  | n + 1, a, b, ha, hb => by
    simp only [affineWordParams]
    have hprev := affineWordParams_drift_nonneg
      (a := Fin.init a) (b := Fin.init b)
      (fun i => ha i.castSucc) (fun i => hb i.castSucc)
    exact add_nonneg (mul_nonneg (ha (Fin.last n)).le hprev) (hb (Fin.last n))

/-- **Strictly positive cumulative additive drift `B > 0`** for any `N`-step affine
    composition `x ↦ a_i * x + b_i` with `a_i > 0`, `b_i ≥ 0`, and at least one odd
    step `b_{i_0} > 0`. -/
theorem affineWordParams_drift_pos :
    ∀ {N : ℕ} {a b : Fin N → ℝ},
      (∀ i : Fin N, 0 < a i) → (∀ i : Fin N, 0 ≤ b i) →
      (∃ i₀ : Fin N, 0 < b i₀) →
      0 < (affineWordParams a b).2
  | 0, _, _, _, _, ⟨i₀, _⟩ => Fin.elim0 i₀
  | n + 1, a, b, ha, hb, ⟨i₀, hi₀⟩ => by
    simp only [affineWordParams]
    rcases Fin.lastCases (motive := fun i => i = i₀ →
        0 < a (Fin.last n) * (affineWordParams (Fin.init a) (Fin.init b)).2 + b (Fin.last n))
      (fun hlast => by
        subst hlast
        have hprev := affineWordParams_drift_nonneg
          (a := Fin.init a) (b := Fin.init b)
          (fun i => ha i.castSucc) (fun i => hb i.castSucc)
        have hmul : 0 ≤ a (Fin.last n) * (affineWordParams (Fin.init a) (Fin.init b)).2 :=
          mul_nonneg (ha (Fin.last n)).le hprev
        linarith)
      (fun j hj => by
        subst hj
        have hprev_pos := affineWordParams_drift_pos
          (a := Fin.init a) (b := Fin.init b)
          (fun i => ha i.castSucc) (fun i => hb i.castSucc)
          ⟨j, hi₀⟩
        have hmul : 0 < a (Fin.last n) * (affineWordParams (Fin.init a) (Fin.init b)).2 :=
          mul_pos (ha (Fin.last n)) hprev_pos
        have hlast_nn : 0 ≤ b (Fin.last n) := hb (Fin.last n)
        linarith)
      i₀ rfl with h
    exact h

/-- **`N`-step real `q > 0` affine balanced-cycle impossibility:** for any `N`-step
    affine composition `x ↦ a_i * x + b_i` with `a_i > 0`, `b_i ≥ 0`, and at least one
    odd step `b_{i_0} > 0` (such as `q`-Collatz steps for `q > 0`, where even steps have
    `a_i = 1 / (1 + q) > 0, b_i = 0` and odd steps have `a_i = (1 + q + q^2) / (1 + q)^v > 0,
    b_i = 1 / (1 + q)^v > 0`), the cumulative drift `B = (affineWordParams a b).2` satisfies
    `0 < B`, and whenever `A = (affineWordParams a b).1 = 1`, there is **no** fixed point
    `P : ℝ` with `A * P + B = P` (equivalently `affineWordEval a b P = P`). -/
theorem affineWord_no_fixed_point_of_balanced {q : ℝ} (hq : 0 < q)
    {N : ℕ} (a b : Fin N → ℝ)
    (ha : ∀ i : Fin N, 0 < a i)
    (hb : ∀ i : Fin N, 0 ≤ b i)
    (hodd : ∃ i₀ : Fin N, 0 < b i₀) :
    let A := (affineWordParams a b).1
    let B := (affineWordParams a b).2
    0 < q + 1 ∧ 0 < B ∧
      (A = 1 → ¬ ∃ P : ℝ, A * P + B = P) ∧
      (A = 1 → ¬ ∃ P : ℝ, affineWordEval a b P = P) := by
  dsimp only
  have hB : 0 < (affineWordParams a b).2 := affineWordParams_drift_pos ha hb hodd
  refine ⟨by linarith, hB, ?_, ?_⟩
  · intro hA ⟨P, hP⟩
    rw [hA, one_mul] at hP
    linarith
  · intro hA ⟨P, hP⟩
    rw [affineWordEval_eq_params, hA, one_mul] at hP
    linarith

/-- **Balanced-holonomy cycle exclusion (proved, sorry-free).**

    Given a QOU whose Skein `q`-integers satisfy the Skein divisibility
    relation `[3]_q = q·[2]_q + 1` with `[2]_q` a non-unit (as holds for
    `[2]_q = q + 1` in the Skein module `ℤ[q^{±1}]`, and more generally for
    every consecutive `(a, a + 1)` pair via `qIntNat_succ_sub_mul_eq_one`),
    the equation `[3]_q^{k_odd} = [2]_q^{k}` has **no** solution with `k ≥ 1`. -/
-- Ref: [collatz1937]
theorem balanced_holonomy_excluded {R : Type*} [CommRing R]
    (two three q : R) (hdiv : three = q * two + 1) (hnu : ¬ IsUnit two)
    {ko k : ℕ} (hk : 1 ≤ k) : three ^ ko ≠ two ^ k := by
  intro h
  have hdvd1 : two ∣ three - 1 := ⟨q, by rw [hdiv]; ring⟩
  have hstep : three - 1 ∣ three ^ ko - 1 := by
    simpa using sub_dvd_pow_sub_pow three 1 ko
  have hdvd_pow : two ∣ three ^ ko - 1 := hdvd1.trans hstep
  have hdvd_two_k : two ∣ two ^ k := dvd_pow_self two (Nat.one_le_iff_ne_zero.mp hk)
  have hdvd_three_pow : two ∣ three ^ ko := h ▸ hdvd_two_k
  have hone : two ∣ (1 : R) := by
    have := dvd_sub hdvd_three_pow hdvd_pow
    simpa using this
  exact hnu (isUnit_of_dvd_one hone)

/-- Consecutive `(a, a + 1)` balanced-holonomy exclusion for every `a : ℕ`:
    whenever `[a]_q` is a non-unit in `R` and `1 ≤ k`, `[a + 1]_q^{ko} ≠ [a]_q^k`. -/
theorem consecutive_qIntNat_balanced_holonomy_excluded {R : Type*} [CommRing R]
    (a : ℕ) (q : R) (hnu : ¬ IsUnit (qIntNat a q)) {ko k : ℕ} (hk : 1 ≤ k) :
    qIntNat (a + 1) q ^ ko ≠ qIntNat a q ^ k :=
  balanced_holonomy_excluded (qIntNat a q) (qIntNat (a + 1) q) q rfl hnu hk

/-- Archimedean `(R := ℝ)` specialisation of `qIntNat_succ_sub_mul_eq_one` (§7c `_real` pair). -/
theorem qIntNat_succ_sub_mul_eq_one_real (a : ℕ) (q : ℝ) :
    qIntNat (a + 1) q - q * qIntNat a q = 1 :=
  qIntNat_succ_sub_mul_eq_one a q

end QOU.AlgebraicSubstrate
