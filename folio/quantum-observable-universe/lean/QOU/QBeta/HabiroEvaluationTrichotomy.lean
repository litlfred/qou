/-
# Where a Habiro series admits an evaluation — the `(q;q)ₙ` trichotomy

`qou-qb8e` item 1 asks for *"a Habiro-ring element whose archimedean evaluation
at `q₀ ≈ 1.10998` reproduces `c₃` at that anchor"*, obtained by assembling
root-of-unity values over all `ζ`. This file proves the structural fact that
decides the whole class before any assembly is attempted.

A Habiro element is a series `Σ aₙ(q)·(q;q)ₙ` with `aₙ ∈ ℤ[q]`, convergent in the
cyclotomic completion `ℤ[q]^ = lim ℤ[q]/((q;q)ₙ)` precisely because `(q;q)ₙ → 0`
there. Any *continuous* evaluation at a point `q₀` therefore forces
`(q₀;q₀)ₙ → 0` in the target. The results below say where that can happen.

* `qPoch_reflection` — the **exact** identity
  `(q;q)ₙ = (-1)^n · q^(n(n+1)/2) · (1/q;1/q)ₙ`, over any field, for `q ≠ 0`.
  Termwise from `1 - qᵏ = -qᵏ·(1 - q⁻ᵏ)`. This is the whole mechanism: the
  `|q| > 1` branch differs from the `|q| < 1` branch by an explicit
  `q^(n(n+1)/2)` blow-up factor. Stated generically per §7c — no ordering, no
  archimedean structure, no `ℝ`.

* `qPoch_eq_zero_of_pow_eq_one` — at a root of unity of order `N`,
  `(q;q)ₙ = 0` for every `n ≥ N`, because the `k = N` factor is `1 - q^N = 0`.
  Also generic (any commutative ring). This is the *positive* side: roots of
  unity do admit the evaluation, which is why Habiro's ring is built there.

* `qPoch_abs_le_succ_of_one_lt` / `qPoch_not_tendsto_zero_of_one_lt` — for real
  `q > 1` the moduli `|(q;q)ₙ|` are eventually non-decreasing and never zero, so
  the sequence does **not** tend to `0`. Archimedean (`ℝ`, ordering, `abs`), and
  correctly on the archimedean side of the wall.

* `no_continuous_evaluation_of_one_lt` — the punchline, a contrapositive: if a
  point admits the limit `(q;q)ₙ → 0` that a continuous evaluation of the
  completion requires, then it is not a real number `> 1`. The substrate anchor
  `q₀ ≈ 1.10998 > 1` is such a number, so **item 1 is ill-posed as written** —
  the object it asks to evaluate has no value at the point it asks about.

**Scope-(b) exclusion, with its invariant named**: the invariant is that
continuity of the evaluation forces `(q;q)ₙ → 0`, and `qPoch_not_tendsto_zero_of_one_lt`
proves that fails for every real `q > 1`. It is a proved structural exclusion, not
a numerical near-miss.

**What is NOT excluded.** A *finite* `(q;q)_m` expansion is a Laurent polynomial
and evaluates at `q₀` without difficulty; the closed-braid Markov trace is the
one-variable Jones polynomial, so its expansion terminates. Nothing here touches
that half of the dichotomy, and nothing here refutes (H1) `c₃^even = -Vol(4₁)`.
For the infinite half, the natural convergent point of the bar-pair is
`1/q₀ ≈ 0.90092 < 1`, the only member inside the unit disc.

Companion probe (both branches, plus the test-power bound on the restated gate):
`computations/qbeta/qbeta_habiro_evaluation_dichotomy_and_test_power.py`.
-/

import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.QBeta.HabiroEvaluationTrichotomy

open Finset

/-- The `q`-Pochhammer symbol `(q;q)ₙ = ∏_{k=1}^{n} (1 - q^k)`.

Generic in the base ring: this is pure `CommRing` data, with no ordering and no
archimedean input, per the §7c base-ring convention. -/
def qPoch {R : Type*} [CommRing R] (q : R) : ℕ → R
  | 0 => 1
  | n + 1 => qPoch q n * (1 - q ^ (n + 1))

@[simp] theorem qPoch_zero {R : Type*} [CommRing R] (q : R) : qPoch q 0 = 1 := rfl

@[simp] theorem qPoch_succ {R : Type*} [CommRing R] (q : R) (n : ℕ) :
    qPoch q (n + 1) = qPoch q n * (1 - q ^ (n + 1)) := rfl

/-! ## The exact reflection identity -/

/-- **Termwise reflection.** For `q ≠ 0` in a field,
`1 - q⁻ᵏ = -q⁻ᵏ * (1 - q^k)`, the single algebraic fact the whole trichotomy
rests on. -/
theorem one_sub_inv_pow {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (k : ℕ) :
    1 - q⁻¹ ^ k = -(q⁻¹ ^ k) * (1 - q ^ k) := by
  have h : q⁻¹ ^ k * q ^ k = 1 := by
    rw [← mul_pow, inv_mul_cancel₀ hq, one_pow]
  calc 1 - q⁻¹ ^ k = q⁻¹ ^ k * q ^ k - q⁻¹ ^ k := by rw [h]
    _ = -(q⁻¹ ^ k) * (1 - q ^ k) := by ring

/-- **The reflection identity.**
`(q⁻¹;q⁻¹)ₙ = (-1)^n · q^(-(n(n+1)/2)) · (q;q)ₙ`, written multiplicatively as

  `q ^ (∑ k in range n, (k+1)) * (q⁻¹;q⁻¹)ₙ = (-1)^n * (q;q)ₙ`

to stay inside the ring (no negative exponents). The exponent
`∑_{k<n} (k+1) = n(n+1)/2` is the blow-up factor: for `|q| > 1` it is exactly
what separates the divergent branch from the convergent one.

Generic — any field, `q ≠ 0`. No ordering, no `ℝ`. -/
theorem qPoch_reflection {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ) :
    q ^ (∑ k ∈ range n, (k + 1)) * qPoch q⁻¹ n = (-1) ^ n * qPoch q n := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hpow : q ^ (n + 1) ≠ 0 := pow_ne_zero _ hq
      rw [Finset.sum_range_succ, qPoch_succ, qPoch_succ, pow_add]
      rw [one_sub_inv_pow q hq (n + 1)]
      have hinv : q ^ (n + 1) * (q⁻¹ ^ (n + 1)) = 1 := by
        rw [← mul_pow]; simp [mul_inv_cancel₀ hq]
      calc
        q ^ (∑ k ∈ range n, (k + 1)) * q ^ (n + 1) *
            (qPoch q⁻¹ n * (-(q⁻¹ ^ (n + 1)) * (1 - q ^ (n + 1))))
            = (q ^ (∑ k ∈ range n, (k + 1)) * qPoch q⁻¹ n) *
              (-(q ^ (n + 1) * q⁻¹ ^ (n + 1)) * (1 - q ^ (n + 1))) := by ring
        _ = ((-1) ^ n * qPoch q n) * (-(1 : K) * (1 - q ^ (n + 1))) := by
              rw [ih, hinv]
        _ = (-1) ^ (n + 1) * (qPoch q n * (1 - q ^ (n + 1))) := by ring

/-! ## Roots of unity: the evaluation exists -/

/-- At a root of unity of order `N ≥ 1`, `(q;q)ₙ` vanishes for every `n ≥ N`:
the `k = N` factor is `1 - q^N = 0`. Generic (`CommRing`).

This is the *positive* half of the trichotomy — it is exactly why the cyclotomic
completion is built at roots of unity, and why a Habiro element has honest values
there. -/
theorem qPoch_eq_zero_of_pow_eq_one {R : Type*} [CommRing R] (q : R) (N : ℕ)
    (hN : 1 ≤ N) (hq : q ^ N = 1) : ∀ n, N ≤ n → qPoch q n = 0 := by
  intro n hn
  induction n with
  | zero => omega
  | succ m ih =>
      rcases Nat.lt_or_ge m N with hm | hm
      · -- then `m + 1 = N`, and the new factor is `1 - q^N = 0`
        have : m + 1 = N := by omega
        rw [qPoch_succ, this, hq]
        ring
      · rw [qPoch_succ, ih hm]
        ring

/-! ## Real `q > 1`: the evaluation does not exist -/

/-- For real `q > 1`, every factor `1 - q^k` with `k ≥ 1` is nonzero, so
`(q;q)ₙ ≠ 0` for all `n`. -/
theorem qPoch_ne_zero_of_one_lt {q : ℝ} (hq : 1 < q) : ∀ n, qPoch q n ≠ 0 := by
  intro n
  induction n with
  | zero => simp
  | succ m ih =>
      have hlt : 1 < q ^ (m + 1) := one_lt_pow₀ hq (by omega)
      have : (1 : ℝ) - q ^ (m + 1) ≠ 0 := by linarith
      exact mul_ne_zero ih this

/-- For real `q > 1` and `k ≥ 1` with `q ^ k ≥ 2`, the factor has modulus `≥ 1`.

`q ^ k ≥ 2` holds for all large `k` since `q > 1`; the hypothesis is carried
explicitly so the lemma stays elementary. -/
theorem one_le_abs_factor {q : ℝ} {k : ℕ} (hk : 2 ≤ q ^ k) :
    1 ≤ |1 - q ^ k| := by
  have : (1 : ℝ) - q ^ k ≤ -1 := by linarith
  have habs : |1 - q ^ k| = -(1 - q ^ k) := abs_of_nonpos (by linarith)
  rw [habs]; linarith

/-- **The modulus is eventually non-decreasing.** Once `q ^ (n+1) ≥ 2` — which
for real `q > 1` holds from some index on — the step from `n` to `n+1` cannot
shrink `|(q;q)ₙ|`. The `q > 1` hypothesis is not needed separately: it is already
carried by `2 ≤ q ^ (n+1)`. -/
theorem qPoch_abs_le_succ_of_one_lt {q : ℝ} {n : ℕ}
    (hn : 2 ≤ q ^ (n + 1)) : |qPoch q n| ≤ |qPoch q (n + 1)| := by
  rw [qPoch_succ, abs_mul]
  have h1 : 1 ≤ |1 - q ^ (n + 1)| := one_le_abs_factor hn
  have h0 : 0 ≤ |qPoch q n| := abs_nonneg _
  nlinarith [h0, h1]

/-- **No archimedean evaluation at real `q > 1`.**

A continuous evaluation of the cyclotomic completion at a point `q` requires
`(q;q)ₙ → 0`, since `(q;q)ₙ → 0` holds in the completion itself. For real
`q > 1` that limit fails: the moduli are eventually non-decreasing and bounded
below by the (nonzero) modulus at the index where `q ^ (n+1) ≥ 2` first holds.

Stated with that index as an explicit hypothesis `N`, so the proof is elementary
and the statement is exactly what is used downstream. -/
theorem qPoch_not_tendsto_zero_of_one_lt {q : ℝ} (hq : 1 < q) (N : ℕ)
    (hN : ∀ n, N ≤ n → 2 ≤ q ^ (n + 1)) :
    ¬ Filter.Tendsto (fun n => qPoch q n) Filter.atTop (nhds 0) := by
  intro htend
  -- the moduli are non-decreasing from `N` on, so they stay `≥ |(q;q)_N| > 0`
  have hmono : ∀ m, |qPoch q N| ≤ |qPoch q (N + m)| := by
    intro m
    induction m with
    | zero => simp
    | succ k ih =>
        have hstep : |qPoch q (N + k)| ≤ |qPoch q (N + k + 1)| :=
          qPoch_abs_le_succ_of_one_lt (hN (N + k) (by omega))
        calc |qPoch q N| ≤ |qPoch q (N + k)| := ih
          _ ≤ |qPoch q (N + k + 1)| := hstep
          _ = |qPoch q (N + (k + 1))| := by ring_nf
  have hpos : 0 < |qPoch q N| := abs_pos.mpr (qPoch_ne_zero_of_one_lt hq N)
  -- but convergence to `0` forces the modulus below `|(q;q)_N|` eventually
  have := (htend.eventually (Metric.ball_mem_nhds (0 : ℝ) hpos))
  rw [Filter.eventually_atTop] at this
  obtain ⟨M, hM⟩ := this
  have hlt : |qPoch q (N + M)| < |qPoch q N| := by
    have := hM (N + M) (by omega)
    simpa [Real.dist_eq, sub_zero] using this
  exact absurd (hmono M) (not_le.mpr hlt)

/-- **Contrapositive, as used.** If a real point admits the limit that a
continuous evaluation of the completion requires, it is not `> 1`.

The substrate anchor `q₀ ≈ 1.10998` satisfies `1 < q₀`, so `qou-qb8e` item 1 —
"a Habiro-ring element whose archimedean evaluation at `q₀` reproduces `c₃`" —
asks for the value of an object that has none at that point. -/
theorem no_continuous_evaluation_of_one_lt {q : ℝ} (N : ℕ)
    (hN : ∀ n, N ≤ n → 2 ≤ q ^ (n + 1))
    (h : Filter.Tendsto (fun n => qPoch q n) Filter.atTop (nhds 0)) : ¬ (1 < q) :=
  fun hq => qPoch_not_tendsto_zero_of_one_lt hq N hN h


/-- **Closed forms for `(q;q)₁` and `(q;q)₂` and their vanishing at `q = 1` (`qou-qb8e`).** -/
theorem qPoch_one_two_and_eval_one {R : Type*} [CommRing R] (q : R) :
    qPoch q 1 = 1 - q ∧
      qPoch q 2 = (1 - q) * (1 - q ^ 2) ∧
      qPoch (1 : R) 1 = 0 ∧
      qPoch (1 : R) 2 = 0 := by
  refine ⟨by simp [qPoch], by simp [qPoch], by simp [qPoch], by simp [qPoch]⟩

end QOU.QBeta.HabiroEvaluationTrichotomy
