import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Marginal-ratio criteria for extensivity — and why "ratios rising to 1" proves nothing

**What this file is for.** A chain binding total `B(A)` is a sum over `A-1`
bonds. Its *marginal* `m(A) = B(A) - B(A-1)` is what the `A`-th nucleon adds,
and **extensivity is exactly the statement that `m` has a nonzero limit**: if
`m(A) → c > 0` then `B(A) ~ cA`, and if `m(A) → 0` fast enough to be summable
then `B` is *bounded* and not extensive at all. So the behaviour of the marginal
sequence is not a side observation — it *is* the extensivity question, which
`docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md` and the
`qou-brng` channel taxonomy both identify as the live blocker.

Measured on the pure single-species chains (PRs #6336, #6365, and the A=5
continuation), the ratios `r(A) = m(A+1)/m(A)` are:

    pp   0.847753, 0.898991, 0.953066     rising toward 1
    nn   0.386424, 0.367352, 0.314444     falling

## The claim this file was written to CHECK, and refutes

I wrote, in a merged PR body and in a probe, that a ratio sequence *rising
monotonically toward 1 from below* is "the signature of a marginal bond
converging to a NONZERO limit -- saturation rather than collapse."

**That is false**, and `ratio_rising_to_one_insufficient` below exhibits the
counterexample: `r k = (k+1)/(k+2)` is strictly increasing, lies strictly in
`(0,1)`, tends to `1`, and its partial products are *exactly* `1/(n+1)`, which
tends to `0`. Rising-to-1 is **necessary but not sufficient**; the correct
criterion is summability of `1 - r`, which `one_sub_sum_le_prod_one_sub`
supplies in the usable direction.

## What survives, and what it costs

* The **nn** reading survives and is now a scope-(b) structural exclusion with a
  named invariant: `prod_le_pow_of_le` shows a ratio sequence bounded above by
  `c < 1` forces the partial products below `c^n`. The measured nn ratios are
  all `≤ 0.387`, so that collapse is geometric and unconditional.
* The **pp** reading does **not** survive as stated. Worse for it, the corpus
  already proved the total is bounded — `|tr_M|` is a bounded trace and its
  free-atom difference saturates — and `B_tot = E₀·(S_off - S_on)` *is* that
  difference. `card_large_marginals_le` turns a bounded total into the finite
  statement that only boundedly many marginals can exceed any `ε > 0`, so a
  nonzero limit is excluded outright.

The corrected picture is therefore **not** "pp saturates, nn collapses" but
**both collapse, at wildly different rates** — pp so slowly that four points
cannot see it, which is exactly what a `1 - r ~ c/k` tail looks like.

## Scope

Everything here is a statement about real sequences: no substrate, no `q`, no
anchor. `ℝ` rather than a generic `CommRing` is correct under §7c because every
statement uses the ordering. Nothing is wired; the file's role is to say which
readings of a measured ratio sequence are licensed and which are not.
-/

namespace QOU.MassTheory.MarginalRatio

open Finset

/-- Partial product of a ratio sequence: `∏_{i<n} r i`. Applied to
`r i = m(i+1)/m(i)` this is `m(n)/m(0)`, so its limit is the marginal's. -/
noncomputable def prodUpTo (r : ℕ → ℝ) (n : ℕ) : ℝ := ∏ i ∈ range n, r i

@[simp] lemma prodUpTo_zero (r : ℕ → ℝ) : prodUpTo r 0 = 1 := by
  simp [prodUpTo]

lemma prodUpTo_succ (r : ℕ → ℝ) (n : ℕ) :
    prodUpTo r (n + 1) = prodUpTo r n * r n := by
  simp [prodUpTo, Finset.prod_range_succ]

/-! ### 1. Ratios bounded away from 1 force geometric collapse

This is the sound half, and it is what licenses the `nn` reading. -/

/-- If every ratio is nonnegative and at most `c`, the partial products are at
most `c ^ n`. With `c < 1` this is geometric decay to zero: a **scope-(b)**
exclusion whose invariant is the uniform bound `c`. -/
theorem prod_le_pow_of_le {r : ℕ → ℝ} {c : ℝ}
    (h0 : ∀ i, 0 ≤ r i) (hc : ∀ i, r i ≤ c) (n : ℕ) :
    prodUpTo r n ≤ c ^ n := by
  unfold prodUpTo
  calc ∏ i ∈ range n, r i
      ≤ ∏ _i ∈ range n, c :=
        Finset.prod_le_prod (fun i _ => h0 i) (fun i _ => hc i)
    _ = c ^ n := by simp

/-! ### 2. The counterexample: rising to 1 is NOT sufficient

`cex k = (k+1)/(k+2)`. Strictly increasing, strictly inside `(0,1)`, tends to
`1` — and its partial product is exactly `1/(n+1)`. -/

/-- The counterexample ratio sequence `r k = (k+1)/(k+2) = 1 - 1/(k+2)`. -/
noncomputable def cex (k : ℕ) : ℝ := (k + 1) / (k + 2)

lemma cex_pos (k : ℕ) : 0 < cex k := by
  unfold cex
  have h : (0:ℝ) < (k : ℝ) + 2 := by positivity
  have h1 : (0:ℝ) < (k : ℝ) + 1 := by positivity
  exact div_pos h1 h

lemma cex_lt_one (k : ℕ) : cex k < 1 := by
  unfold cex
  rw [div_lt_one (by positivity)]
  linarith

/-- `1 - cex k = 1/(k+2)`, so the gaps to 1 are the harmonic tail — **not
summable**, which is precisely why the product still dies. -/
lemma one_sub_cex (k : ℕ) : 1 - cex k = 1 / ((k : ℝ) + 2) := by
  unfold cex
  have h : ((k : ℝ) + 2) ≠ 0 := by positivity
  field_simp
  ring

/-- Strictly increasing, proved through the `1 - 1/(k+2)` form rather than by a
cross-multiplication lemma, whose name has moved between Mathlib versions. -/
lemma cex_strictMono : StrictMono cex := by
  intro a b hab
  have ha : (0:ℝ) < (a : ℝ) + 2 := by positivity
  have hab' : ((a : ℝ) + 2) < ((b : ℝ) + 2) := by
    have : (a : ℝ) < (b : ℝ) := by exact_mod_cast hab
    linarith
  have hrec : 1 / ((b : ℝ) + 2) < 1 / ((a : ℝ) + 2) :=
    one_div_lt_one_div_of_lt ha hab'
  have ea := one_sub_cex a
  have eb := one_sub_cex b
  linarith

/-- The partial products telescope exactly: `∏_{i<n} (i+1)/(i+2) = 1/(n+1)`. -/
theorem cex_prodUpTo (n : ℕ) : prodUpTo cex n = 1 / ((n : ℝ) + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [prodUpTo_succ, ih, cex]
      have h1 : ((n : ℝ) + 1) ≠ 0 := by positivity
      have h2 : ((n : ℝ) + 2) ≠ 0 := by positivity
      push_cast
      field_simp
      ring

/-- **The refutation.** There is a ratio sequence that is strictly increasing,
lies strictly in `(0,1)`, has `1 - r k → 0`, and whose partial products are
`1/(n+1)` — hence tend to `0`. So "the ratios rise monotonically toward 1"
does **not** license "the marginal converges to a nonzero limit".

This is stated as an explicit existential so it can be cited as the reason that
inference is unavailable, rather than re-derived each time. -/
theorem ratio_rising_to_one_insufficient :
    ∃ r : ℕ → ℝ,
      StrictMono r ∧
      (∀ k, 0 < r k) ∧
      (∀ k, r k < 1) ∧
      (∀ k, 1 - r k = 1 / ((k : ℝ) + 2)) ∧
      (∀ n, prodUpTo r n = 1 / ((n : ℝ) + 1)) := by
  refine ⟨cex, cex_strictMono, cex_pos, cex_lt_one, one_sub_cex, cex_prodUpTo⟩

/-! ### 3. The correct criterion, in the usable direction

Weierstrass: `∏ (1 - a i) ≥ 1 - ∑ a i`. So a *finite* measurement plus a tail
bound on `∑ (1 - r)` gives a genuine positive lower bound on the product —
which is what a claim of extensivity actually needs. -/

/-- `1 - ∑_{i<n} a i ≤ ∏_{i<n} (1 - a i)` for `a i ∈ [0,1]`.

Read with `a i = 1 - r i`: if the gaps to 1 sum to less than 1, the product is
bounded below by a positive constant, so the marginal cannot collapse. This is
the sufficient condition the counterexample above shows is missing — and note
it is checkable from finitely many measured terms *plus* a bound on the tail,
never from the measured terms alone. -/
theorem one_sub_sum_le_prod_one_sub {a : ℕ → ℝ}
    (h0 : ∀ i, 0 ≤ a i) (h1 : ∀ i, a i ≤ 1) (n : ℕ) :
    1 - ∑ i ∈ range n, a i ≤ ∏ i ∈ range n, (1 - a i) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.prod_range_succ, Finset.sum_range_succ]
      have hS : 0 ≤ ∑ i ∈ range n, a i :=
        Finset.sum_nonneg (fun i _ => h0 i)
      have hb : 0 ≤ 1 - a n := by linarith [h1 n]
      have hstep : (1 - ∑ i ∈ range n, a i) * (1 - a n)
          ≤ (∏ i ∈ range n, (1 - a i)) * (1 - a n) :=
        mul_le_mul_of_nonneg_right ih hb
      nlinarith [h0 n, hS, hstep]

/-! ### 4. A bounded total excludes a nonzero marginal limit

This is the one that settles the `pp` case, given the corpus result that the
trace binding is intensive (bounded). Stated finitely — no filters — so it can
be applied to a measured, finite sequence directly. -/

/-- If the marginals are nonnegative and every partial sum is at most `M`, then
for any `ε > 0` the number of marginals reaching `ε` is bounded: their count
times `ε` is at most `M`.

Consequence for the binding: a **bounded** total (which is what "the binding is
intensive" says) permits only boundedly many marginals above any threshold, so
`m(A) → c > 0` is impossible. Both chains' marginals therefore go to zero, and
the measured question is only *how fast*. -/
theorem card_large_marginals_mul_le {m : ℕ → ℝ} {M ε : ℝ}
    (h0 : ∀ i, 0 ≤ m i)
    (hM : ∀ n, ∑ i ∈ range n, m i ≤ M) (n : ℕ) :
    ((range n).filter (fun i => ε ≤ m i)).card * ε ≤ M := by
  have hsub : (range n).filter (fun i => ε ≤ m i) ⊆ range n :=
    Finset.filter_subset _ _
  have h1 : (((range n).filter (fun i => ε ≤ m i)).card : ℝ) * ε
      = ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε := by
    rw [Finset.sum_const, nsmul_eq_mul]
  have h2 : ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε
      ≤ ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i := by
    refine Finset.sum_le_sum ?_
    intro i hi
    exact (Finset.mem_filter.mp hi).2
  have h3 : ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i
      ≤ ∑ i ∈ range n, m i :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => h0 i)
  calc (((range n).filter (fun i => ε ≤ m i)).card : ℝ) * ε
      = ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε := h1
    _ ≤ ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i := h2
    _ ≤ ∑ i ∈ range n, m i := h3
    _ ≤ M := hM n

/-- The usable form: at most `M / ε` of the first `n` marginals reach `ε`.

This is the bound that actually excludes a nonzero limit — if `m(A) → c > 0`
then *every* sufficiently large `A` has `m(A) ≥ c/2`, i.e. unboundedly many,
contradicting the fixed ceiling `M / (c/2)`. Unlike the multiplicative form
above it genuinely needs `0 < ε`, which is why both are stated. -/
theorem card_large_marginals_le {m : ℕ → ℝ} {M ε : ℝ}
    (hε : 0 < ε) (h0 : ∀ i, 0 ≤ m i)
    (hM : ∀ n, ∑ i ∈ range n, m i ≤ M) (n : ℕ) :
    (((range n).filter (fun i => ε ≤ m i)).card : ℝ) ≤ M / ε := by
  rw [le_div_iff₀ hε]
  exact card_large_marginals_mul_le h0 hM n

/-! ### 5. Average understates the marginal

Formalises why reporting `B(A)/(A-1)` (as #6336 did) hides how fast the
underlying quantity moves: the average of an antitone sequence is at least its
last term. -/

/-- For an antitone marginal sequence, the running average dominates the last
marginal. So an average that has fallen by `x %` sits on a marginal that has
fallen by *at least* `x %` — the average is a lagging indicator, never a
leading one. -/
theorem sum_ge_card_mul_last {m : ℕ → ℝ} (hanti : Antitone m) (n : ℕ) :
    (n : ℝ) * m n ≤ ∑ i ∈ range n, m i := by
  have h : ∀ i ∈ range n, m n ≤ m i := by
    intro i hi
    exact hanti (le_of_lt (Finset.mem_range.mp hi))
  calc (n : ℝ) * m n = ∑ _i ∈ range n, m n := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    _ ≤ ∑ i ∈ range n, m i := Finset.sum_le_sum h

end QOU.MassTheory.MarginalRatio
