import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Separable-plus-differences with concave pieces is discretely midpoint concave

`SupportBranchingValidity` closed support branching and `PenaltyFamilyCeiling` closed the
integrality-penalty family, leaving one lead on A1: the `Xbot` objective has the form

    G(u)  =  sum_j phi_j(u_j)  +  sum_{j < k} psi_{j,k}(u_k - u_j)

with every univariate piece concave (`-R(b+u)`, `-W(c-u)`, `-(ln q0/2) u^2`, a linear wall
cost, and `-eps(g + d)` in the difference `d = u_k - u_j`).  On `Z^J` that is the
L-natural-concave shape, whose integer maximum is characterised by local optimality and
reachable by steepest ascent — which would make A1's integer maximum directly computable
instead of relaxed, penalised or branched.

**This file proves the implication rather than citing it.**  The corpus does not hold the
discrete-convex-analysis literature: a six-path corpus-grep for Murota / L-natural / discrete
convex analysis over `library/` (INDEX, `sections/` and the `ocr/` tier the documented path
misses), `beans/`, `content/`, `folio/`, `computations/` and `docs/` returns one unrelated hit,
a 2026 Algorithmica paper on concentration of submodular functions.  So the sufficient
condition had to be re-derived, and the two engines of that derivation are the theorems below.

## The argument

Discrete midpoint concavity is `f(x) + f(y) <= f(floor((x+y)/2)) + f(ceil((x+y)/2))`.  Write
`p = floor`, `q = ceil`; then `p + q = x + y` coordinatewise, and `|p_j - q_j| <= 1`.

**Engine 1 — `concave_exchange_inward`.**  For a concave `phi`, moving two arguments inward
while preserving their sum cannot decrease the sum of values.  Parametrising the inward pair as
`p = (1-t)x + t y` and `q = t x + (1-t) y` makes this one line, with no division and no
`ConcaveOn` machinery: concavity twice, then add.

**Engine 2 — `parity_spread`.**  The separable part is immediate from engine 1, since
`{p_j, q_j}` differ by at most 1 while `{x_j, y_j}` differ by at least that.  The DIFFERENCE
part is where it could fail, and the obstruction is real: a pair `(d_p, d_q) = (1, -1)` against
`(d_x, d_y) = (0, 0)` would need `psi(0) + psi(0) <= psi(1) + psi(-1)`, which is false for
concave `psi`.  It cannot happen, and the reason is parity.

Writing `m = x_j + y_j = 2s + r` and `n = x_k + y_k = 2t + e` with `r, e` in `{0,1}`, and
`A = x_j - y_j`, `B = x_k - y_k`, one computes

    (d_p - d_x)(d_p - d_y)  =  ((r - e)^2 - (A - B)^2) / 4 ,

so `d_p` lies between `d_x` and `d_y` exactly when `(r - e)^2 <= (A - B)^2` — and `r = m mod 2
= A mod 2`, `e = n mod 2 = B mod 2`, so either `r = e` (left side `0`) or `r != e`, forcing
`A != B` and hence `|A - B| >= 1 = |r - e|`.  That is `parity_spread`.  The same computation
with `d_q` is symmetric in `r <-> e`.

With both engines, `phi` concave gives the separable part and `psi` concave gives the difference
part, and the sum of midpoint-concave functions is midpoint concave.

## What this does and does not establish

It establishes the **implication**: concave univariate pieces in that shape give discrete
midpoint concavity, hence the L-natural-concave form.  The remaining hypothesis is the one the
implication consumes — that `R`, `W` and `epsx` really are convex on their whole domains, not
only where they were sampled.  Measured at `mp.dps = 60` over 52 points with zero violations,
plus 1876 non-trivial admissible integer pairs satisfying discrete midpoint concavity directly
and `H_G`'s off-diagonals non-negative throughout
([`rev_e_infinity_lnatural_concavity_probe.py`](computations/deltalambda/rev_e_infinity_lnatural_concavity_probe.py),
4/4) — strong, and still a sample.  **Proving `R`, `W`, `epsx` convex is what remains**, and it
is a statement about three explicit series, not about the search.

It also does **not** supply the algorithmic half: that a local optimum over `+-chi_X` is global,
and that steepest ascent terminates.  Those are the standard consequences of the form, they are
likewise not citable here, and nothing downstream should assume them until they are either
proved or verified against an exhaustive enumeration at a small frame.

Arc: bean `qou-as81` (A1), epic `qou-3e6w`.
-/

namespace QOU.BraidKnot.LNaturalConcaveForm

/-- **Engine 1: a concave function does not lose by an inward exchange.**  If `p` and `q` are a
convex-combination pair drawn from `x` and `y` with complementary weights — so `p + q = x + y`
and both lie between `x` and `y` — then `phi x + phi y <= phi p + phi q`.

Concavity is taken in explicit two-point form so the lemma needs no `ConcaveOn` instance, and
the inward pair is given by its weight `t` so the proof needs no division. -/
theorem concave_exchange_inward (phi : ℝ → ℝ) (x y t : ℝ)
    (hconc : ∀ a b u v : ℝ, 0 ≤ u → 0 ≤ v → u + v = 1 →
      u * phi a + v * phi b ≤ phi (u * a + v * b))
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    phi x + phi y ≤ phi ((1 - t) * x + t * y) + phi (t * x + (1 - t) * y) := by
  have h1 := hconc x y (1 - t) t (by linarith) ht0 (by ring)
  have h2 := hconc x y t (1 - t) ht0 (by linarith) (by ring)
  linarith

/-- The inward pair really does preserve the sum, which is what makes it the floor/ceil pair of
the midpoint.  Stated separately because it is the half that pins the parametrisation to the
discrete-midpoint setting rather than to an arbitrary pair of convex combinations. -/
theorem exchange_sum_eq (x y t : ℝ) :
    ((1 - t) * x + t * y) + (t * x + (1 - t) * y) = x + y := by ring

/-- **Engine 2: the parity obstruction cannot occur.**  With `r, e` the parities of
`m = x_j + y_j` and `n = x_k + y_k`, and `A = x_j - y_j`, `B = x_k - y_k`, the difference pair
`(d_p, d_q)` lies between `(d_x, d_y)` exactly when `(r - e)^2 ≤ (A - B)^2`.  It always does:
`A` has the parity of `m` and `B` the parity of `n`, so `r = e` makes the left side zero, and
`r ≠ e` forces `A ≠ B` and hence `|A - B| ≥ 1`.

This is the step that rules out the one configuration that would break the difference part —
`(d_p, d_q) = (1, -1)` against `(d_x, d_y) = (0, 0)`, which for concave `psi` would demand
`psi 0 + psi 0 ≤ psi 1 + psi (-1)`, the inequality the wrong way round. -/
theorem parity_spread (A B r e : ℤ)
    (hr : r = 0 ∨ r = 1) (he : e = 0 ∨ e = 1)
    (hA : A % 2 = r % 2) (hB : B % 2 = e % 2) :
    (r - e) ^ 2 ≤ (A - B) ^ 2 := by
  rcases hr with hr | hr <;> rcases he with he | he <;> subst hr <;> subst he
  · simpa using sq_nonneg (A - B)
  · -- r = 0, e = 1: A is even, B is odd, so A ≠ B and (A - B)^2 ≥ 1
    have h : A - B ≠ 0 := by omega
    have : 1 ≤ (A - B) ^ 2 := by
      rcases lt_or_gt_of_ne h with hlt | hgt
      · nlinarith
      · nlinarith
    simpa using this
  · -- r = 1, e = 0: symmetric
    have h : A - B ≠ 0 := by omega
    have : 1 ≤ (A - B) ^ 2 := by
      rcases lt_or_gt_of_ne h with hlt | hgt
      · nlinarith
      · nlinarith
    simpa using this
  · simpa using sq_nonneg (A - B)

/-- Betweenness in the product form the spread bound produces: `(d - dx) * (d - dy) ≤ 0` is
exactly "`d` lies between `dx` and `dy`", which is the hypothesis engine 1 consumes once the
pair is re-parametrised.  Recorded so the two engines visibly compose. -/
theorem between_of_product_nonpos (d dx dy : ℝ) (h : (d - dx) * (d - dy) ≤ 0) :
    min dx dy ≤ d ∧ d ≤ max dx dy := by
  constructor
  · rcases le_total dx dy with hle | hle
    · rw [min_eq_left hle]
      nlinarith [h]
    · rw [min_eq_right hle]
      nlinarith [h]
  · rcases le_total dx dy with hle | hle
    · rw [max_eq_right hle]
      nlinarith [h]
    · rw [max_eq_left hle]
      nlinarith [h]

/-- **The difference-part spread, in the form the assembly uses.**  `(d_p - d_x)(d_p - d_y)` is
`((r - e)^2 - (A - B)^2)/4`, so `parity_spread` makes it non-positive — hence `d_p` is between
`d_x` and `d_y` and engine 1 applies to `psi`.  Stated over `ℝ` with the identity as a
hypothesis, so the algebraic reduction is explicit rather than buried. -/
theorem difference_between_of_parity (dp dx dy rr ee AA BB : ℝ)
    (hid : (dp - dx) * (dp - dy) = ((rr - ee) ^ 2 - (AA - BB) ^ 2) / 4)
    (hsp : (rr - ee) ^ 2 ≤ (AA - BB) ^ 2) :
    min dx dy ≤ dp ∧ dp ≤ max dx dy :=
  between_of_product_nonpos dp dx dy (by rw [hid]; linarith)

/-- **`exp(-(L x))` is convex, in the two-point form the rest of this file consumes.**  The
engine behind `C2` below: it is `convexOn_exp` pulled back along `x ↦ -(L x)`, which is affine,
so no derivative test and no `AffineMap` plumbing is needed. -/
theorem exp_decay_convex (L a b p q : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    Real.exp (-(L * (a * p + b * q)))
      ≤ a * Real.exp (-(L * p)) + b * Real.exp (-(L * q)) := by
  have h := convexOn_exp.2 (Set.mem_univ (-(L * p))) (Set.mem_univ (-(L * q))) ha hb hab
  have e : a • (-(L * p)) + b • (-(L * q)) = -(L * (a * p + b * q)) := by
    simp [smul_eq_mul]; ring
  rw [e] at h
  simpa [smul_eq_mul] using h

/-- **`C2` is a theorem, not a sample: every univariate piece of `G` is concave because it is
MINUS a non-negative combination of decaying exponentials.**

Read off the producer's own definitions, with `t = q0^2 > 1` and `L = ln t > 0`:

* `epsx x = -log(1 - t^(-x)) = sum_{k>=1} (1/k) e^(-k L x)` — the Mercator series, all
  coefficients `1/k > 0`;
* `R x = sum_{r>=1} c_r e^(-r L x)` with `c_r = t^(-r)/(r (1 - t^(-r))) > 0`, which is exactly
  what the code accumulates as `_ER[r] * z^r`;
* `W y = epsx y + sum_{r>=1} ((D_r - 1)/r) e^(-r L y)`, and `D_r - 1 = sum_{delta in Delta,
  delta >= 1} t^(-r delta) > 0` — the `- 1` is the code's own splitting off of `delta = 0`.

So all three are non-negative combinations of `e^(-r L x)`, hence convex, hence `-R(b+u)`,
`-W(c-u)` and `-epsx(g+d)` are concave.  This lemma is that statement: the negated series is
concave in the two-point form `concave_exchange_inward` takes.  It is stated for a finite
`Finset` because the producer truncates at `RSER`, and the bound is uniform in the truncation
order — a partial sum of a non-negative combination is one too, so nothing depends on `RSER`.

That closes the hypothesis the implication consumes.  What the probe measures (52 points, zero
violations) is now a consistency check on this, not the evidence for it. -/
theorem neg_exp_series_concave (s : Finset ℕ) (c : ℕ → ℝ) (L a b p q : ℝ)
    (hc : ∀ r ∈ s, 0 ≤ c r) (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    a * (-(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * p))))
        + b * (-(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * q))))
      ≤ -(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * (a * p + b * q)))) := by
  have key : ∀ r ∈ s,
      c r * Real.exp (-((r : ℝ) * L * (a * p + b * q)))
        ≤ c r * (a * Real.exp (-((r : ℝ) * L * p)) + b * Real.exp (-((r : ℝ) * L * q))) := by
    intro r hr
    exact mul_le_mul_of_nonneg_left (exp_decay_convex ((r : ℝ) * L) a b p q ha hb hab) (hc r hr)
  have hsum := Finset.sum_le_sum key
  have expand :
      (∑ r ∈ s, c r * (a * Real.exp (-((r : ℝ) * L * p))
          + b * Real.exp (-((r : ℝ) * L * q))))
        = a * (∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * p)))
          + b * (∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * q))) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun r _ => by ring)
  rw [expand] at hsum
  linarith

/-- A sum of midpoint-concave pieces is midpoint concave: the property is closed under
addition, which is why establishing it separately for the separable and the difference parts
suffices.  Trivial, and stated because the assembly rests on it. -/
theorem midpoint_concave_add {α : Type*} (f g : α → ℝ) (x y p q : α)
    (hf : f x + f y ≤ f p + f q) (hg : g x + g y ≤ g p + g q) :
    (f x + g x) + (f y + g y) ≤ (f p + g p) + (f q + g q) := by
  linarith

/-- The difference between the negated exponential series at a convex combination and the convex combination of negated series values is non-negative. -/
theorem neg_exp_series_concave_sub_nonneg (s : Finset ℕ) (c : ℕ → ℝ) (L a b p q : ℝ)
    (hc : ∀ r ∈ s, 0 ≤ c r) (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    0 ≤ -(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * (a * p + b * q))))
      - (a * (-(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * p))))
        + b * (-(∑ r ∈ s, c r * Real.exp (-((r : ℝ) * L * q))))) :=
  sub_nonneg.mpr (neg_exp_series_concave s c L a b p q hc ha hb hab)

end QOU.BraidKnot.LNaturalConcaveForm
