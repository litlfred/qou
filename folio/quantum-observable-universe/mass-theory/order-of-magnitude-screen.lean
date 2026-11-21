/-
  QOU.MassCore.OrderOfMagnitudeScreen — the mathematics underneath the §4(d)
  "direction-sanity gate" (`rem:q-beta-direction-sanity-gate`).

  The gate is a *rule* (an order-of-magnitude screen against a
  CODATA-derived number), not a theorem.  This file isolates what is
  actually provable about it, with the threshold `lam` and the target
  `t` as explicit PARAMETERS (no decimal constants, no fitted values):

  §1  `Screen lam t x`  : the multiplicative window  t ≤ lam·|x| ∧ |x| ≤ lam·t
      (= "max(|x|/t, t/|x|) ≤ lam", stated without division).
      `AdditiveScreen lam t x` : |x − t| ≤ lam·t  (what the corpus Lean uses).
  §2  order structure of the screen: monotone in the threshold,
      reflexive for lam ≥ 1, symmetric, multiplicatively transitive,
      closed under products.
  §3  conditional rejection soundness: IF the true value passes at
      some mu ≤ lam, every candidate rejected at lam differs from it.
      (The premise is a comparison with measurement and is not established here;
      see rem:q-beta-direction-sanity-gate.)
  §4  the finite precision-ladder product ∏(1 + a_k) with |a_k| ≤ 1/2
      lies in the window of width ∏(1 + 2|a_k|) around 1 — the
      algebraic core of proof Step 1 (no logarithms, no limits).
  §5  diagnosis of the additive form: it never rejects any
      x ∈ [0, (lam+1)t] (so never rejects a too-small magnitude), and
      the "operational test" is NOT sufficient for window-failure on
      signed values (explicit counterexample in ℚ).
  §6  the threshold-free direction obstruction: a downward factor
      (0 ≤ z ≤ 1) can never close an upward gap (B < t); plus: failure
      of z^m candidates is upward closed in m, and (Archimedean) every
      geometric-decay family is eventually rejected at EVERY finite
      threshold — the value 10 only moves the first rejected m.

  Generic over a linearly ordered field K; nothing here uses ℝ.
-/
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.MassCore.OrderOfMagnitudeScreen

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-! ## §1 Definitions -/

/-- The multiplicative order-of-magnitude window with threshold `lam`
    around target `t`: `t ≤ lam·|x|` and `|x| ≤ lam·t`. -/
def Screen (lam t x : K) : Prop := t ≤ lam * |x| ∧ |x| ≤ lam * t

/-- The additive band used by the corpus siblings
    (`DirectionSanityGateClass`, `MassDirectionSanityGateClass`,
    `BarEvenKernel.direction_match`). -/
def AdditiveScreen (lam t x : K) : Prop := |x - t| ≤ lam * t

/-! ## §2 Order structure of the screen -/

/-- Monotone in the threshold: passing at `lam` implies passing at
    every `lam' ≥ lam`. -/
theorem screen_mono {lam lam' t x : K} (hl : lam ≤ lam') (ht : 0 ≤ t)
    (h : Screen lam t x) : Screen lam' t x :=
  ⟨h.1.trans (mul_le_mul_of_nonneg_right hl (abs_nonneg x)),
   h.2.trans (mul_le_mul_of_nonneg_right hl ht)⟩

/-- Contrapositive: rejection at `lam'` implies rejection at every
    smaller threshold. -/
theorem not_screen_anti {lam lam' t x : K} (hl : lam ≤ lam') (ht : 0 ≤ t)
    (h : ¬ Screen lam' t x) : ¬ Screen lam t x :=
  fun h' => h (screen_mono hl ht h')

/-- Reflexive for `lam ≥ 1`: the target itself always passes. -/
theorem screen_refl {lam t : K} (hl : 1 ≤ lam) (ht : 0 ≤ t) :
    Screen lam t t := by
  have h1 : t ≤ lam * t := le_mul_of_one_le_left ht hl
  refine ⟨?_, ?_⟩ <;> rw [abs_of_nonneg ht] <;> exact h1

/-- The screen sees only `|x|`. -/
theorem screen_abs_iff {lam t x : K} : Screen lam t |x| ↔ Screen lam t x := by
  simp [Screen, abs_abs]

/-- Symmetric (for a nonnegative target): `x` is within `lam` of `t`
    iff `t` is within `lam` of `|x|`. -/
theorem screen_symm {lam t x : K} (ht : 0 ≤ t) :
    Screen lam t x ↔ Screen lam |x| t := by
  unfold Screen
  simp only [abs_of_nonneg ht]
  exact And.comm

/-- Multiplicative transitivity (nonnegative data): thresholds multiply. -/
theorem screen_trans {lam mu a b c : K} (hlam : 0 ≤ lam) (hmu : 0 ≤ mu)
    (hb : 0 ≤ b) (h1 : Screen lam a b) (h2 : Screen mu b c) :
    Screen (lam * mu) a c := by
  obtain ⟨h1a, h1b⟩ := h1
  obtain ⟨h2a, h2b⟩ := h2
  rw [abs_of_nonneg hb] at h1a h1b
  refine ⟨?_, ?_⟩
  · calc a ≤ lam * b := h1a
      _ ≤ lam * (mu * |c|) := mul_le_mul_of_nonneg_left h2a hlam
      _ = lam * mu * |c| := by ring
  · calc |c| ≤ mu * b := h2b
      _ ≤ mu * (lam * a) := mul_le_mul_of_nonneg_left h1b hmu
      _ = lam * mu * a := by ring

/-- Closed under products (nonnegative data): thresholds multiply.
    No sign hypothesis on `lam` is needed: with `a, b ≥ 0` a negative
    threshold forces `a = b = 0`, and the product screen holds trivially. -/
theorem screen_mul {lam mu a b c d : K}
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (h1 : Screen lam a b) (h2 : Screen mu c d) :
    Screen (lam * mu) (a * c) (b * d) := by
  obtain ⟨h1a, h1b⟩ := h1
  obtain ⟨h2a, h2b⟩ := h2
  rw [abs_of_nonneg hb] at h1a h1b
  rcases le_or_gt 0 lam with hlam | hlam
  swap
  · have ha0 : a = 0 := le_antisymm
      (h1a.trans (mul_nonpos_of_nonpos_of_nonneg hlam.le hb)) ha
    have hb0 : b = 0 := le_antisymm (by
      have := h1b; rw [ha0, mul_zero] at this; exact this) hb
    subst ha0; subst hb0
    unfold Screen; simp
  rw [abs_of_nonneg hd] at h2a h2b
  unfold Screen
  rw [abs_of_nonneg (mul_nonneg hb hd)]
  refine ⟨?_, ?_⟩
  · calc a * c ≤ (lam * b) * (mu * d) :=
          mul_le_mul h1a h2a hc (mul_nonneg hlam hb)
      _ = lam * mu * (b * d) := by ring
  · calc b * d ≤ (lam * a) * (mu * c) :=
          mul_le_mul h1b h2b hd (mul_nonneg hlam ha)
      _ = lam * mu * (a * c) := by ring

/-- Finite products: if each nonnegative factor `f i` is within `r i`
    of `1`, the product is within `∏ r i` of `1`. -/
theorem screen_prod_one {ι : Type*} (s : Finset ι) (r f : ι → K)
    (hr : ∀ i ∈ s, 0 ≤ r i) (hf : ∀ i ∈ s, 0 ≤ f i)
    (h : ∀ i ∈ s, Screen (r i) 1 (f i)) :
    Screen (∏ i ∈ s, r i) 1 (∏ i ∈ s, f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using screen_refl (le_refl (1 : K)) zero_le_one
  | insert j s hj ih =>
    rw [Finset.prod_insert hj, Finset.prod_insert hj]
    have ih' := ih (fun i hi => hr i (Finset.mem_insert_of_mem hi))
      (fun i hi => hf i (Finset.mem_insert_of_mem hi))
      (fun i hi => h i (Finset.mem_insert_of_mem hi))
    have := screen_mul
      zero_le_one (hf j (Finset.mem_insert_self j s)) zero_le_one
      (Finset.prod_nonneg fun i hi => hf i (Finset.mem_insert_of_mem hi))
      (h j (Finset.mem_insert_self j s)) ih'
    simpa using this

/-! ## §3 Conditional rejection soundness -/

/-- **Conditional rejection soundness.**  If the true value `xstar`
    passes at some threshold `mu ≤ lam` (HYPOTHESIS — for the Q_β
    gate this premise is a comparison with a CODATA number and is not
    established by this file), then every candidate value rejected at
    `lam` differs from `xstar`. -/
theorem ne_of_not_screen_of_screen {lam mu t xstar x : K} (hml : mu ≤ lam)
    (ht : 0 ≤ t) (htrue : Screen mu t xstar) (hrej : ¬ Screen lam t x) :
    x ≠ xstar := by
  rintro rfl
  exact hrej (screen_mono hml ht htrue)

/-! ## §4 The finite ladder product (algebraic core of proof Step 1) -/

/-- A single ladder factor `1 + a` with `|a| ≤ 1/2` is within
    `1 + 2|a|` of `1`. -/
theorem screen_one_add {a : K} (ha : |a| ≤ 1 / 2) :
    Screen (1 + 2 * |a|) 1 (1 + a) := by
  have hn : 0 ≤ |a| := abs_nonneg a
  have hlo : -|a| ≤ a := neg_abs_le a
  have hhi : a ≤ |a| := le_abs_self a
  have hpos : 0 ≤ 1 + a := by linarith
  unfold Screen
  rw [abs_of_nonneg hpos]
  refine ⟨?_, by linarith⟩
  -- 1 ≤ (1 + 2|a|)(1 + a): for a ≥ -|a| and |a| ≤ 1/2
  have key : (1 + 2 * |a|) * (1 - |a|) ≤ (1 + 2 * |a|) * (1 + a) :=
    mul_le_mul_of_nonneg_left (by linarith) (by linarith)
  have : 1 ≤ (1 + 2 * |a|) * (1 - |a|) := by nlinarith
  linarith

/-- **Finite precision-ladder bound.**  For any finite family with
    `|a k| ≤ 1/2`, the product `∏ (1 + a k)` passes the screen around
    `1` at threshold `∏ (1 + 2|a k|)`. -/
theorem screen_ladder_prod {ι : Type*} (s : Finset ι) (a : ι → K)
    (ha : ∀ k ∈ s, |a k| ≤ 1 / 2) :
    Screen (∏ k ∈ s, (1 + 2 * |a k|)) 1 (∏ k ∈ s, (1 + a k)) := by
  refine screen_prod_one s _ _ (fun k _ => by positivity) (fun k hk => ?_)
    (fun k hk => screen_one_add (ha k hk))
  have := neg_abs_le (a k)
  have := ha k hk
  linarith

/-! ## §5 Diagnosis of the additive band -/

/-- The additive band admits `0` (no signal) whenever `lam ≥ 1`. -/
theorem additive_admits_zero {lam t : K} (hl : 1 ≤ lam) (ht : 0 ≤ t) :
    AdditiveScreen lam t 0 := by
  unfold AdditiveScreen
  rw [zero_sub, abs_neg, abs_of_nonneg ht]
  exact le_mul_of_one_le_left ht hl

/-- On nonnegative magnitudes the additive band is exactly a one-sided
    upper bound `x ≤ (lam + 1)·t`: it rejects nothing that is too small. -/
theorem additive_iff_le_of_nonneg {lam t x : K} (hl : 1 ≤ lam) (ht : 0 ≤ t)
    (hx : 0 ≤ x) : AdditiveScreen lam t x ↔ x ≤ (lam + 1) * t := by
  unfold AdditiveScreen
  have h1 : t ≤ lam * t := le_mul_of_one_le_left ht hl
  rw [abs_sub_le_iff]
  constructor
  · rintro ⟨h, -⟩; linarith
  · intro h; exact ⟨by linarith, by linarith⟩

/-- On nonnegative magnitudes, window-pass implies additive-pass
    (so additive-rejection is sufficient for window-rejection there). -/
theorem additive_of_screen_of_nonneg {lam t x : K} (hl : 1 ≤ lam)
    (ht : 0 ≤ t) (hx : 0 ≤ x) (h : Screen lam t x) : AdditiveScreen lam t x := by
  rw [additive_iff_le_of_nonneg hl ht hx]
  have h2 := h.2
  rw [abs_of_nonneg hx] at h2
  linarith

/-- **Counterexample** to "the operational test |F − t|/t > 10 is a
    sufficient condition for failure" (proof.md, "The gate") on SIGNED
    values: `F = −19/2`, `t = 1` fails the additive test yet its
    magnitude `19/2` lies inside the decade window. -/
theorem operational_test_not_sufficient :
    Screen (10 : ℚ) 1 (-19 / 2) ∧ ¬ AdditiveScreen (10 : ℚ) 1 (-19 / 2) := by
  have habs : |(-19 / 2 : ℚ)| = 19 / 2 := by norm_num [abs_of_neg]
  have habs2 : |(-19 / 2 : ℚ) - 1| = 21 / 2 := by norm_num [abs_of_neg]
  unfold Screen AdditiveScreen
  rw [habs, habs2]
  norm_num

/-- The additive band admits the entire downward region `[0, t]`, so it
    cannot detect any "too small" (z < 1) direction error. -/
theorem additive_admits_below {lam t x : K} (hl : 1 ≤ lam) (ht : 0 ≤ t)
    (hx0 : 0 ≤ x) (hxt : x ≤ t) : AdditiveScreen lam t x := by
  rw [additive_iff_le_of_nonneg hl ht hx0]
  nlinarith

/-! ## §6 The direction obstruction (threshold-free) -/

/-- **Direction obstruction.**  A base `B > 0` corrected by any number of
    downward factors `0 ≤ z ≤ 1` never reaches a target `t > B`. -/
theorem mul_pow_lt_of_lt {B t z : K} (hz0 : 0 ≤ z) (hz1 : z ≤ 1)
    (hB : 0 ≤ B) (hBt : B < t) (m : ℕ) : B * z ^ m < t := by
  have : z ^ m ≤ 1 := pow_le_one₀ hz0 hz1
  calc B * z ^ m ≤ B * 1 := mul_le_mul_of_nonneg_left this hB
    _ = B := mul_one B
    _ < t := hBt

/-- Same, for an arbitrary finite family of downward factors. -/
theorem mul_prod_lt_of_lt {ι : Type*} (s : Finset ι) (f : ι → K)
    (hf0 : ∀ i ∈ s, 0 ≤ f i) (hf1 : ∀ i ∈ s, f i ≤ 1)
    {B t : K} (hB : 0 ≤ B) (hBt : B < t) : B * ∏ i ∈ s, f i < t := by
  have : ∏ i ∈ s, f i ≤ 1 := Finset.prod_le_one hf0 hf1
  calc B * ∏ i ∈ s, f i ≤ B * 1 := mul_le_mul_of_nonneg_left this hB
    _ = B := mul_one B
    _ < t := hBt

/-- Rejection of the geometric family `B·z^m` is upward closed in `m`:
    once `lam·B·z^n < t`, every `m ≥ n` is rejected. -/
theorem not_screen_pow_of_le {lam t B z : K} (hl : 0 ≤ lam) (hB : 0 ≤ B)
    (hz0 : 0 ≤ z) (hz1 : z ≤ 1) {n m : ℕ} (hnm : n ≤ m)
    (hn : lam * (B * z ^ n) < t) : ¬ Screen lam t (B * z ^ m) := by
  rintro ⟨h, -⟩
  have hzm : z ^ m ≤ z ^ n := pow_le_pow_of_le_one hz0 hz1 hnm
  rw [abs_of_nonneg (mul_nonneg hB (pow_nonneg hz0 m))] at h
  have : lam * (B * z ^ m) ≤ lam * (B * z ^ n) :=
    mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hzm hB) hl
  linarith

/-- **Non-vacuity at every threshold** (Archimedean `K`): for `0 ≤ z < 1`
    and `t > 0`, every geometric-decay family `B·z^m` is rejected for all
    sufficiently large `m`, whatever the finite threshold `lam ≥ 0`.  The
    threshold only moves the first rejected index. -/
theorem eventually_not_screen_pow [Archimedean K] {lam t B z : K}
    (hl : 0 ≤ lam) (ht : 0 < t) (hB : 0 ≤ B) (hz0 : 0 ≤ z) (hz1 : z < 1) :
    ∃ n : ℕ, ∀ m, n ≤ m → ¬ Screen lam t (B * z ^ m) := by
  have hc : 0 < lam * B + 1 := by positivity
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one (div_pos ht hc) hz1
  refine ⟨n, fun m hm => not_screen_pow_of_le hl hB hz0 hz1.le hm ?_⟩
  have hzn : 0 ≤ z ^ n := pow_nonneg hz0 n
  have h1 : (lam * B + 1) * z ^ n < t := by
    have := mul_lt_mul_of_pos_left hn hc
    rwa [mul_div_cancel₀ _ hc.ne'] at this
  nlinarith

end QOU.MassCore.OrderOfMagnitudeScreen

