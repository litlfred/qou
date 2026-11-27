import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The squeeze theorem as an error estimate, and where it needs Archimedes

The volume-conjecture proofs for `4₁` and the Borromean rings in this repository
(`BraidKnotOctonion/FigureEightVolumeSqueeze.lean`, `BorromeanVolume.lean`) are
squeezes: a positive sum `S` lies between its largest term `T` and `N · T`, so after
taking `(2π/N)·log` the sum and the term differ by at most `2π · log N / N`.

This file isolates the logical content of that step, to answer the owner's
2026-11-27 question (thread "Formalize knot volume conjecture"): *is the squeeze
theorem essentially an error estimate that works in any Archimedean ordered field,
and does it fail with infinitesimals?*

* `abs_sub_le_of_squeeze` — the squeeze with an explicit error bound. It holds in
  **every** linearly ordered additive group: no Archimedean property, no topology,
  no completeness. Its `η`-relaxed form `abs_sub_le_of_squeeze_relaxed` covers a
  target known only to within `η`.
* `abs_log_sub_log_le_log_of_le_mul` — the log form used by the Kashaev squeeze:
  `T ≤ S ≤ N·T` implies `|log S − log T| ≤ log N`. Real-valued (it uses `Real.log`).
* `exists_halo_of_not_archimedean` and `archimedean_iff_modulus_limit_unique` —
  where the Archimedean property enters. A sequence controlled by the modulus
  `1/(n+1)` has **at most one** limit point exactly when the field is Archimedean.
  In a non-Archimedean field (hyperreals, surreals) the same estimate is satisfied
  by a whole halo of points around the intended limit. So the error estimate
  survives, and only the step from "error ≤ 1/(n+1) for every standard `n`" to "equal"
  fails.

Everything here is sorry-free and uses only Mathlib.

-- Ref: [mathlib] `archimedean_iff_nat_lt` (Mathlib.Algebra.Order.Archimedean.Basic)
-/

namespace QOU.MathlibExt.SqueezeModulus

/-! ## 1. The squeeze as an error estimate (no Archimedean hypothesis) -/

/-- **Squeeze with an explicit error bound.** If `a ≤ x ≤ b` and both `a` and `b` lie
within `e` of `L`, then so does `x`. This holds in any linearly ordered additive
commutative group. -/
theorem abs_sub_le_of_squeeze {α : Type*} [AddCommGroup α] [LinearOrder α]
    [IsOrderedAddMonoid α] {a b x L e : α}
    (hax : a ≤ x) (hxb : x ≤ b) (ha : |a - L| ≤ e) (hb : |b - L| ≤ e) :
    |x - L| ≤ e := by
  rw [abs_sub_le_iff] at ha hb ⊢
  exact ⟨(sub_le_sub_right hxb L).trans hb.1, (sub_le_sub_left hax L).trans ha.2⟩

/-- **`η`-relaxed squeeze.** If the target is known only to within `η`
(`|L - L₀| ≤ η`, e.g. a constant fixed by a measurement of finite precision), the
squeeze still bounds the error, by `e + η`. -/
theorem abs_sub_le_of_squeeze_relaxed {α : Type*} [AddCommGroup α] [LinearOrder α]
    [IsOrderedAddMonoid α] {a b x L L₀ e η : α}
    (hax : a ≤ x) (hxb : x ≤ b) (ha : |a - L| ≤ e) (hb : |b - L| ≤ e)
    (hL : |L - L₀| ≤ η) :
    |x - L₀| ≤ e + η := by
  have hx := abs_sub_le_of_squeeze hax hxb ha hb
  calc |x - L₀| = |(x - L) + (L - L₀)| := by rw [sub_add_sub_cancel]
    _ ≤ |x - L| + |L - L₀| := abs_add_le _ _
    _ ≤ e + η := add_le_add hx hL

/-! ## 2. The log form used by the Kashaev max-term squeeze -/

/-- **Max-term squeeze, log form.** If `0 < T ≤ S ≤ N·T`, then
`|log S − log T| ≤ log N`. This is the step that turns "the sum of a positive
Kashaev state sum lies between its largest term and `N` times it" into the
error `log N` (and, after scaling by `2π/N`, into `2π·log N / N`). -/
theorem abs_log_sub_log_le_log_of_le_mul {T S N : ℝ} (hT : 0 < T) (hTS : T ≤ S)
    (hSN : S ≤ N * T) : |Real.log S - Real.log T| ≤ Real.log N := by
  have hS : 0 < S := lt_of_lt_of_le hT hTS
  have hN : 0 < N := by
    by_contra h
    push_neg at h
    have : N * T ≤ 0 := mul_nonpos_of_nonpos_of_nonneg h hT.le
    linarith
  have hlow : Real.log T ≤ Real.log S := Real.log_le_log hT hTS
  have hup : Real.log S ≤ Real.log N + Real.log T := by
    rw [← Real.log_mul hN.ne' hT.ne']
    exact Real.log_le_log hS hSN
  rw [abs_le]
  constructor <;> linarith

/-- Scaled form: with the Kashaev normalisation `c / N` (`c = 2π` in the volume
conjecture), the scaled logs of the sum and of the largest term differ by at most
`c · log N / N`. -/
theorem abs_scaled_log_sub_le {T S N c : ℝ} (hT : 0 < T) (hTS : T ≤ S)
    (hSN : S ≤ N * T) (hN : 0 < N) (hc : 0 ≤ c) :
    |c / N * Real.log S - c / N * Real.log T| ≤ c / N * Real.log N := by
  rw [← mul_sub, abs_mul, abs_of_nonneg (div_nonneg hc hN.le)]
  exact mul_le_mul_of_nonneg_left (abs_log_sub_log_le_log_of_le_mul hT hTS hSN)
    (div_nonneg hc hN.le)

/-! ## 3. Where the Archimedean property enters: the halo -/

/-- **The halo.** In a linearly ordered field that is not Archimedean there is a
nonzero element smaller in absolute value than every `1/(n+1)`: a nonzero
infinitesimal. -/
theorem exists_halo_of_not_archimedean {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (h : ¬ Archimedean K) :
    ∃ L : K, L ≠ 0 ∧ ∀ n : ℕ, |L| ≤ 1 / ((n : K) + 1) := by
  rw [archimedean_iff_nat_lt] at h
  push_neg at h
  obtain ⟨x, hx⟩ := h
  have hx1 : (1 : K) ≤ x := by exact_mod_cast hx 1
  have hxpos : 0 < x := lt_of_lt_of_le one_pos hx1
  refine ⟨1 / x, by positivity, fun n => ?_⟩
  rw [abs_of_pos (by positivity)]
  have hn : (n : K) + 1 ≤ x := by exact_mod_cast hx (n + 1)
  exact one_div_le_one_div_of_le (by positivity) hn

/-- In a non-Archimedean field the explicit-modulus squeeze does not pin a point: the
constant sequence `0` satisfies the modulus `1/(n+1)` towards both `0` and a nonzero
infinitesimal `L`. -/
theorem modulus_limit_not_unique_of_not_archimedean {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (h : ¬ Archimedean K) :
    ∃ L L' : K, L ≠ L' ∧ ∀ n : ℕ,
      |(0 : K) - L| ≤ 1 / ((n : K) + 1) ∧ |(0 : K) - L'| ≤ 1 / ((n : K) + 1) := by
  obtain ⟨L, hL0, hL⟩ := exists_halo_of_not_archimedean h
  refine ⟨0, L, fun h0 => hL0 h0.symm, fun n => ⟨?_, ?_⟩⟩
  · simp only [sub_self, abs_zero]; positivity
  · rw [zero_sub, abs_neg]; exact hL n

/-- In an Archimedean field a sequence has at most one limit with modulus
`1/(n+1)`: if `a n` is within `1/(n+1)` of both `L` and `L'` for every `n`, then
`L = L'`. -/
theorem modulus_limit_unique_of_archimedean {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] [Archimedean K] {a : ℕ → K} {L L' : K}
    (h : ∀ n : ℕ, |a n - L| ≤ 1 / ((n : K) + 1) ∧ |a n - L'| ≤ 1 / ((n : K) + 1)) :
    L = L' := by
  by_contra hne
  have hd : 0 < |L - L'| := abs_pos.mpr (sub_ne_zero.mpr hne)
  obtain ⟨n, hn⟩ := exists_nat_gt (2 / |L - L'|)
  have hn1 : (0 : K) < (n : K) + 1 := by positivity
  have htri : |L - L'| ≤ 2 / ((n : K) + 1) := by
    obtain ⟨h1, h2⟩ := h n
    calc |L - L'| = |(a n - L') - (a n - L)| := by congr 1; ring
      _ ≤ |a n - L'| + |a n - L| := abs_sub _ _
      _ ≤ 1 / ((n : K) + 1) + 1 / ((n : K) + 1) := add_le_add h2 h1
      _ = 2 / ((n : K) + 1) := by ring
  have : 2 / |L - L'| < (n : K) + 1 := by linarith
  rw [div_lt_iff₀ hd] at this
  rw [le_div_iff₀ hn1] at htri
  linarith

/-- **The squeeze pins a point exactly in Archimedean fields.** For a linearly ordered
field `K`, the following are equivalent: `K` is Archimedean; every sequence has at
most one limit with explicit modulus `1/(n+1)`. -/
theorem archimedean_iff_modulus_limit_unique {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] :
    Archimedean K ↔ ∀ (a : ℕ → K) (L L' : K),
      (∀ n : ℕ, |a n - L| ≤ 1 / ((n : K) + 1) ∧ |a n - L'| ≤ 1 / ((n : K) + 1)) →
      L = L' := by
  constructor
  · intro _ a L L' h
    exact modulus_limit_unique_of_archimedean h
  · intro H
    by_contra hna
    obtain ⟨L, L', hne, h⟩ := modulus_limit_not_unique_of_not_archimedean hna
    exact hne (H (fun _ => 0) L L' h)

end QOU.MathlibExt.SqueezeModulus
