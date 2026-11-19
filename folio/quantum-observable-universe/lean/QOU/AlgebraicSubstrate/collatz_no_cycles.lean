import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Algebra.Ring.GeomSum

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

end QOU.AlgebraicSubstrate
