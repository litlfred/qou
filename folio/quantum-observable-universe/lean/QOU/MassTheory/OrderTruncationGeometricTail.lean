import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# Truncating the multi-bond order expansion: geometric domination from a ratio bound

The binding expansion runs over orders (levels) `k`, and the question is whether
higher orders may be dropped for a target precision. The corpus supplies the
input from the other side: `computations/deltalambda/wlambda_wstd_superexp_lower_bound.py`
proves a **rigorous super-exponential lower bound on the level-selection tower
weight**

    w_std(k) ≥ (1/4)·√(k!) / p(k)^{3/2},

which grows faster than every fixed `C^k` (since `√(k!) = (k/e)^{k/2}·poly` and
`p(k) = exp(O(√k))` is sub-exponential). Contributions enter *inverted* against
that weight, so a super-exponentially growing `w_std` is exactly a
super-exponentially **decaying** per-order contribution. That is the sense in
which higher orders may be ignored — the growth is in the weight, the decay is in
the term.

**Direction matters here.** The corpus result is a growth bound on `w_std(k)`,
not a decay bound on anything. Reading it as "the terms grow" would invert the
conclusion and forbid truncation rather than license it. The consequence the
corpus already records from the same bound — inverting a super-exponentially
growing `w_std` against an extensive target `B ~ A` forces `k(A) = O(log A)`,
excluding `k ~ A` and `k ~ bond-count` — is the same statement in the form the
mass tower uses it.

## What this file proves (sorry-free)

The elementary step that turns a per-order ratio bound into a truncation bound:

* `le_geometric_of_ratio` — if `a (k+1) ≤ r · a k` for all `k ≥ N`, then
  `a (N + j) ≤ r^j · a N`. Every order past `N` is geometrically dominated.
  (Non-negativity of the terms is *not* needed for this one — only `0 ≤ r`.)
* `le_geometric_of_ratio'` — the same indexed by `k ≥ N` directly.
* `tail_lt_of_ratio` — with `0 ≤ r < 1` and `a N > 0`, for any target precision
  `ε > 0` all sufficiently high orders fall below `ε`. The truncation order is
  explicit in `r` and `ε`.

The super-exponential case is the sub-case where the admissible `r` may be taken
arbitrarily small as `N` grows, so the domination is far stronger than geometric.
Stating it geometrically is deliberate: the geometric form is what a truncation
*bound* needs, and it holds under the weakest hypothesis.

## What is hypothesis and what is theorem

The ratio bound `a (k+1) ≤ r · a k` is a **hypothesis** here, supplied by the
caller. Its justification for the binding tower is the `w_std` growth bound
above, which is a separate result with its own status (steps (B),(C) of that
script are described there as Lean-ready, not yet Lean). This file does **not**
prove the physical ratio bound and does not assert that the binding expansion
satisfies it — per AGENTS.md §"Axiomatization is NOT a Proof", carrying it as a
hypothesis buys nothing toward establishing it.

What this file does supply is the missing implication: *given* a ratio bound, the
tail is controlled and the truncation order is explicit. That is the piece that
was being used informally.

## Scope

No exclusion, no refutation — an enabling lemma. It says nothing about the
magnitude of any order, nor about whether the expansion converges to the measured
binding.

## Base ring (§7c)

`ℝ`: the content is an ordering/decay statement (`0 ≤ r < 1`, `<` on terms), i.e.
archimedean by nature. A generic-ring version would be meaningless.

-- Ref: [leitner2026] computations/deltalambda/wlambda_wstd_superexp_lower_bound.py
-/

namespace QOU.MassTheory

/-- **Geometric domination from a ratio bound.** If each order past `N` is at most
`r` times the previous one, then order `N + j` is at most `r^j` times order `N`.

This is the step that licenses dropping high orders: a per-order ratio bound is
usually what one can establish, while a *tail* bound is what truncation needs. -/
theorem le_geometric_of_ratio {a : ℕ → ℝ} {N : ℕ} {r : ℝ}
    (hr0 : 0 ≤ r)
    (hratio : ∀ k, N ≤ k → a (k + 1) ≤ r * a k) :
    ∀ j, a (N + j) ≤ r ^ j * a N := by
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
      have hstep : a (N + j + 1) ≤ r * a (N + j) := hratio (N + j) (Nat.le_add_right N j)
      have : r * a (N + j) ≤ r * (r ^ j * a N) := by
        exact mul_le_mul_of_nonneg_left ih hr0
      calc a (N + (j + 1)) = a (N + j + 1) := by ring_nf
        _ ≤ r * a (N + j) := hstep
        _ ≤ r * (r ^ j * a N) := this
        _ = r ^ (j + 1) * a N := by ring

/-- The same bound indexed by an order `k ≥ N` rather than an offset. -/
theorem le_geometric_of_ratio' {a : ℕ → ℝ} {N : ℕ} {r : ℝ}
    (hr0 : 0 ≤ r)
    (hratio : ∀ k, N ≤ k → a (k + 1) ≤ r * a k)
    {k : ℕ} (hk : N ≤ k) :
    a k ≤ r ^ (k - N) * a N := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
  simpa using le_geometric_of_ratio hr0 hratio j

/-- **Truncation at an explicit order.** With a contraction ratio `r < 1`, every
order beyond some finite point contributes less than any prescribed `ε > 0`. The
order is explicit: any `k` with `r ^ (k - N) * a N < ε`.

The super-exponential case of the `w_std` bound is stronger than this — there the
effective ratio itself tends to `0` — so this is the conservative form. -/
theorem tail_lt_of_ratio {a : ℕ → ℝ} {N : ℕ} {r ε : ℝ}
    (hr0 : 0 ≤ r) (hr1 : r < 1) (hε : 0 < ε) (hpos : ∀ k, 0 ≤ a k)
    (hratio : ∀ k, N ≤ k → a (k + 1) ≤ r * a k) :
    ∃ K : ℕ, N ≤ K ∧ ∀ k, K ≤ k → a k < ε := by
  rcases eq_or_lt_of_le (hpos N) with hzero | hposN
  · -- `a N = 0` collapses the whole tail to `0`.
    refine ⟨N, le_refl N, fun k hk => ?_⟩
    have := le_geometric_of_ratio' hr0 hratio hk
    rw [← hzero] at this
    simpa using lt_of_le_of_lt (by simpa using this) hε
  · obtain ⟨j, hj⟩ := exists_pow_lt_of_lt_one (div_pos hε hposN) hr1
    refine ⟨N + j, Nat.le_add_right N j, fun k hk => ?_⟩
    have hNk : N ≤ k := le_trans (Nat.le_add_right N j) hk
    have hbound := le_geometric_of_ratio' hr0 hratio hNk
    have hmono : r ^ (k - N) ≤ r ^ j :=
      pow_le_pow_of_le_one hr0 hr1.le (by omega)
    calc a k ≤ r ^ (k - N) * a N := hbound
      _ ≤ r ^ j * a N := mul_le_mul_of_nonneg_right hmono (hpos N)
      _ < (ε / a N) * a N := by
          exact mul_lt_mul_of_pos_right hj hposN
      _ = ε := div_mul_cancel₀ ε hposN.ne'

/-- **Non-vacuity.** The hypotheses are satisfiable: `a k = r ^ k` with
`0 ≤ r < 1` meets the ratio bound with equality at every order. -/
example {r : ℝ} : ∀ k, (fun n => r ^ n) (k + 1) ≤ r * (fun n => r ^ n) k := by
  intro k; simp [pow_succ, mul_comm]

end QOU.MassTheory
