import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic

/-!
# Separated groups of rows do not interact

`HookSumElasticity` put the hook sum in β-coordinates and showed it is a **separable quadratic**
there: the one-body, linear and quadratic parts of the `REV_n` objective split over any partition
of the rows by inspection.  The whole objective does not, because it also carries a **pair** term

    − Σ_{i<j} ε(β_i − β_j) ,    ε(m) = −log(1 − q₀^{−2m}) ,

and that is the only thing that can tie two groups of displaced rows together.  This file is
about that one term.

Two results, and they are deliberately of different kinds.

`sum_pairs_split` is **pure algebra** — a double sum splits into the two within-class sums plus
the cross sums, over any decidable predicate, in any `AddCommMonoid`.  It carries no order, no
metric and no analysis, and it is what makes "restrict the displacement to one group" a
well-defined summand rather than a heuristic.

`cross_sum_le` is the **estimate**: if the kernel is antitone and the two groups are at least `R`
apart, the cross sum is at most `|A| · |B| · g R`.  Its geometric corollary
`cross_sum_le_geom` is the archimedean specialisation (§7c), stated over `ℝ` because a
geometric bound needs one.

## Why the `REV_n` arc wanted this

The maximiser of `REV_n` at triangular `n` is a positive block at the free top edge, a contiguous
run of `−1`, and a positive block against the bottom wall, with the run's **position free**
(PR #7323).  A free position is a position that can go to infinity, and these two results say
what that buys: the excess is *exactly* the three pieces plus a cross term, and the cross term is
bounded by the kernel at the separation.  Since `ε(m) ≤ q₀^{−2m}`, a separation growing with `k`
drives it to zero geometrically — so the three pieces stop interacting and each becomes a
`k`-free quantity.

That is the structural content behind `rev_e_infinity_edge_limit_probe.py`, which measures the
cross term directly and finds it identically zero in 1e-40 arithmetic once the separation clears
`223`.  Nothing here fixes a value of `e_inf`; what it fixes is that the value *decomposes*.

| | |
|---|---|
| `sum_pairs_split` | a pair sum splits into within-class and cross parts, exactly |
| `cross_sum_nonneg` | a non-negative kernel gives a non-negative cross term |
| `cross_sum_le` | separated groups contribute at most `|A| · |B| · g R` |
| `cross_sum_le_geom` | with `g m ≤ C rᵐ` the cross term is `O(rᴿ)` — the decoupling |

-- Ref: [leitner2026] `computations/deltalambda/rev_e_infinity_edge_limit_probe.py`
-/

namespace QOU.BraidKnot.EdgeDecoupling

open Finset

/-- A double sum over one index set splits, over any decidable predicate `P`, into the two
within-class sums and the two cross sums.

This is the exact statement that "restrict the displacement to one group" is a summand: no
order, no metric, no decay — it holds in any `AddCommMonoid`. -/
theorem sum_pairs_split {M : Type*} [AddCommMonoid M] {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (P : ι → Prop) [DecidablePred P] (f : ι → ι → M) :
    ∑ i ∈ s, ∑ j ∈ s, f i j
      = ((∑ i ∈ s.filter P, ∑ j ∈ s.filter P, f i j)
          + ∑ i ∈ s.filter (fun x => ¬ P x), ∑ j ∈ s.filter (fun x => ¬ P x), f i j)
        + ((∑ i ∈ s.filter P, ∑ j ∈ s.filter (fun x => ¬ P x), f i j)
          + ∑ i ∈ s.filter (fun x => ¬ P x), ∑ j ∈ s.filter P, f i j) := by
  have hinner : ∀ i : ι, ∑ j ∈ s, f i j
      = (∑ j ∈ s.filter P, f i j) + ∑ j ∈ s.filter (fun x => ¬ P x), f i j := fun i =>
    (Finset.sum_filter_add_sum_filter_not s P (f i)).symm
  rw [← Finset.sum_filter_add_sum_filter_not s P (fun i => ∑ j ∈ s, f i j)]
  simp only [hinner, Finset.sum_add_distrib]
  simp only [add_left_comm, add_comm]

/-- A non-negative kernel gives a non-negative cross term. -/
theorem cross_sum_nonneg {M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {ι : Type*}
    {A B : Finset ι} {d : ι → ι → ℕ} {g : ℕ → M} (hg0 : ∀ m, 0 ≤ g m) :
    0 ≤ ∑ i ∈ A, ∑ j ∈ B, g (d i j) :=
  Finset.sum_nonneg fun _ _ => Finset.sum_nonneg fun _ _ => hg0 _

/-- **The decoupling estimate.** If the kernel `g` is antitone and every member of `A` is at
least `R` away from every member of `B`, then the cross term is at most `|A| · |B| · g R`.

Stated with `•` rather than `*` so it needs only an ordered `AddCommMonoid`: the multiplication
by two cardinalities is repeated addition, not ring multiplication. -/
theorem cross_sum_le {M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {ι : Type*}
    {A B : Finset ι} {d : ι → ι → ℕ} {g : ℕ → M} {R : ℕ}
    (hg : Antitone g) (hsep : ∀ i ∈ A, ∀ j ∈ B, R ≤ d i j) :
    ∑ i ∈ A, ∑ j ∈ B, g (d i j) ≤ (A.card * B.card) • g R := by
  have hstep : ∑ i ∈ A, ∑ j ∈ B, g (d i j) ≤ ∑ _i ∈ A, ∑ _j ∈ B, g R :=
    Finset.sum_le_sum fun i hi =>
      Finset.sum_le_sum fun j hj => hg (hsep i hi j hj)
  calc ∑ i ∈ A, ∑ j ∈ B, g (d i j)
      ≤ ∑ _i ∈ A, ∑ _j ∈ B, g R := hstep
    _ = (A.card * B.card) • g R := by
        rw [Finset.sum_const, Finset.sum_const, mul_nsmul']

/-- **The decoupling, in the form the `REV_n` arc uses it.** A kernel dominated by a geometric
`C rᴹ` makes the cross term `O(rᴿ)` in the separation `R`, so two groups of rows that move apart
stop interacting geometrically fast.

`ε(m) = −log(1 − q₀^{−2m}) ≤ q₀^{−2m} / (1 − q₀^{−2})` is such a kernel with `r = q₀^{−2} < 1`,
which is why the three pieces of the maximiser separate at all. -/
theorem cross_sum_le_geom {ι : Type*} {A B : Finset ι} {d : ι → ι → ℕ} {g : ℕ → ℝ} {R : ℕ}
    {C r : ℝ} (hg : Antitone g) (hgle : g R ≤ C * r ^ R)
    (hsep : ∀ i ∈ A, ∀ j ∈ B, R ≤ d i j) :
    ∑ i ∈ A, ∑ j ∈ B, g (d i j) ≤ (A.card * B.card : ℕ) * (C * r ^ R) := by
  have h1 : ∑ i ∈ A, ∑ j ∈ B, g (d i j) ≤ (A.card * B.card) • g R := cross_sum_le hg hsep
  have h2 : (A.card * B.card) • g R ≤ (A.card * B.card : ℕ) * (C * r ^ R) := by
    rw [nsmul_eq_mul]
    exact mul_le_mul_of_nonneg_left hgle (Nat.cast_nonneg _)
  exact h1.trans h2

/-! ### The run's straddling pairs collect by distance

A contiguous run of `ell` displaced rows inside an arithmetic progression leaves every gap
*inside* the run alone and moves only the pairs that straddle it.  Gathering those pairs by
distance is the identity below: the `j`-th row of the run contributes every distance `> j`, so a
distance `d` is contributed by exactly `min d ell` of them.

This is what turns the run's pair sum into a single sum over distances,

    Xrun(ell)  =  ∑_d min(d, ell) · T(d)  −  (ln q₀ / 2) · ell ,

which `rev_e_infinity_closed_form_probe.py` evaluates and checks against the direct pair sum.

Like `sum_pairs_split` it is **pure algebra** — no order, no metric, no decay — so it holds in any
`AddCommMonoid` and says nothing on its own about which kernel `f` is.  In particular it does not
establish that the sum over `d` converges: that is the `ε` decay, and it lives on the analytic
side.  What it does establish is the *shape* — that the run's contribution depends on `ell` only
through the weights `min d ell`, which is why `Xrun` is a function of the run length alone and
carries no `k`. -/

/-- The rows of the run whose *upward* reach at distance `d` clears the run: `min d ell`.

The `min` is the whole content — a distance shorter than the run is contributed by only the
first `d` rows, a distance longer than it by all `ell`. -/
theorem card_filter_lt (d ell : ℕ) :
    ((range ell).filter (fun j => j < d)).card = min d ell := by
  have hset : (range ell).filter (fun j => j < d) = range (min d ell) := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_range, lt_min_iff]
    omega
  rw [hset, Finset.card_range]

/-- The rows whose *downward* reach at distance `d` clears the run: also `min d ell`.

This is the reflection `j ↦ ell - 1 - j` of `card_filter_lt`, and it is not a restatement — the
downward half of the run's pair sum is generated by a different condition (`ell ≤ j + d`, the
row plus the distance leaving the run at the bottom) and only *lands* on the same count. -/
theorem card_filter_ge (d ell : ℕ) :
    ((range ell).filter (fun j => ell ≤ j + d)).card = min d ell := by
  have hnot : (range ell).filter (fun j => ¬ (ell ≤ j + d)) = range (ell - d) := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_range, not_le]
    omega
  have hsum := Finset.filter_card_add_filter_neg_card_eq_card
    (s := range ell) (p := fun j => ell ≤ j + d)
  rw [hnot, Finset.card_range, Finset.card_range] at hsum
  omega

/-- **Collecting the run's upward straddling pairs by distance.**

The left side is how the pair sum is generated — row by row of the run, each contributing every
distance beyond it.  The right side is how it is evaluated — distance by distance, each with the
multiplicity `min d ell`.  They are equal by exchanging the order of summation and counting. -/
theorem sum_tails_eq_sum_min {M : Type*} [AddCommMonoid M] (ell N : ℕ) (f : ℕ → M) :
    ∑ j ∈ range ell, ∑ d ∈ range N, (if j < d then f d else 0)
      = ∑ d ∈ range N, (min d ell) • f d := by
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun d _ => ?_
  rw [← Finset.sum_filter, Finset.sum_const, card_filter_lt]

/-- **Collecting the run's downward straddling pairs by distance.** -/
theorem sum_heads_eq_sum_min {M : Type*} [AddCommMonoid M] (ell N : ℕ) (f : ℕ → M) :
    ∑ j ∈ range ell, ∑ d ∈ range N, (if ell ≤ j + d then f d else 0)
      = ∑ d ∈ range N, (min d ell) • f d := by
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun d _ => ?_
  rw [← Finset.sum_filter, Finset.sum_const, card_filter_ge]

/-- **The run's pair sum, both halves, as one sum over distances.**

This is the shape `rev_e_infinity_closed_form_probe.py::run_direct` actually computes: each row
of the run contributes upward to every row above it that lies outside the run, and downward to
every row below it that does.  The two conditions are different (`j < d` and `ell ≤ j + d`) and
carry different kernels, and the identity is that both collect with the same multiplicity, so
the run's whole contribution is a single sum over `d` against the combined kernel

    T d  =  fUp d + fDown d .

At `fUp d = ε(2d) − ε(2d+1)` and `fDown d = ε(2d) − ε(2d−1)` that combined kernel is exactly the
probe's `T(d) = 2ε(2d) − ε(2d−1) − ε(2d+1)`.  Nothing here says that series converges, or what
its value is; it says the run depends on `ell` only through the weights `min d ell` — which is
why `Xrun` is a function of the run length alone and carries no `k`. -/
theorem run_pair_sum_eq_sum_min {M : Type*} [AddCommMonoid M] (ell N : ℕ) (fUp fDown : ℕ → M) :
    (∑ j ∈ range ell, ∑ d ∈ range N, (if j < d then fUp d else 0))
        + ∑ j ∈ range ell, ∑ d ∈ range N, (if ell ≤ j + d then fDown d else 0)
      = ∑ d ∈ range N, (min d ell) • (fUp d + fDown d) := by
  rw [sum_tails_eq_sum_min, sum_heads_eq_sum_min, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun d _ => (nsmul_add _ _ _).symm

/-- Subtracting the minimum-weighted distance sum from the double sum of downward straddling pairs yields zero (`qou-k54t`). -/
theorem sum_heads_sub_sum_min_eq_zero {M : Type*} [AddCommGroup M] (ell N : ℕ) (f : ℕ → M) :
    (∑ j ∈ range ell, ∑ d ∈ range N, (if ell ≤ j + d then f d else 0))
      - ∑ d ∈ range N, (min d ell) • f d = 0 := by
  rw [sum_heads_eq_sum_min ell N f, sub_self]

end QOU.BraidKnot.EdgeDecoupling
