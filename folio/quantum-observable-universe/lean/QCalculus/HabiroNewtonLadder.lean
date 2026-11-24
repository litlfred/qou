import Mathlib.Tactic

/-!
# QOU.BraidKnot.HabiroNewtonLadder

**Habiro–Newton ladder of the figure-eight colored Jones — Lean proof and
generalization of the cp4i probe identity.**

Formalizes, sorry-free, the structural identity verified exactly by
`computations/aj_operator_aw_shape_probe.py` (bean `cp4i`; audit:
`docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md` §"Probe result"):

  `J_N(4₁; q) = ∑_{k=0}^{N-1} ∏_{j=1}^{k} (Λ_N − λ_j)`,
  `Λ_N = q^N + q^{−N}`, `λ_j = q^j + q^{−j}`,

i.e. the Habiro–Lê double-Pochhammer form of the figure-eight colored Jones
is a **Newton-interpolation ladder on the bar-even variable** `Λ` with all
cyclotomic coefficients equal to 1 (the 4₁ signature of Habiro's cyclotomic
expansion — Ref: [habiro2004cyclotomic]; strong AJ proved for 4₁ —
Ref: [nguyen-tran-2021]).  The identity is TERMWISE
(`habiroTerm_eq_newtonLadder`), which is strictly stronger than the summed
statement the probe checked per-`N`.

## What this file proves (all sorry-free)

* `newtonLadder_succ` — the ladder is **two-term / first-order**
  (`g_{k+1} = (x − a_{k+1}) · g_k`, lower coefficient `B_k ≡ 0`): the
  degenerate boundary of the Askey–Wilson three-term shape.
* `casoratian_eq_zero` — **generalized**: over any commutative ring, any two
  solutions of a first-order ladder have identically vanishing Casoratian
  (discrete Wronskian) — the reason the proved knot side supplies no
  Casoratian sign for the 1jrh test
  (`docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`).
* `lam_bar_even` / `multiplier_bar_even` — the ladder nodes and multiplier
  are **bar-even** (`q ↦ q⁻¹` invariant), consistent with the bar-even
  multiplier the 1jrh one-recurrence hypothesis requires.
* `newtonLadder_eq_zero` / `newtonLadder_sum_stable` — **generalized
  termination**: the sum truncates at any node hit (`x = a m`), the 4₁
  mechanism `Λ_N = λ_N`.
* `habiroTerm_eq_newtonLadder` — the termwise Habiro↔Newton identity.
* `coloredJones41_eq_newton_sum` / `coloredJones41_sum_stable` /
  `coloredJones41_bar_symmetric` — the probe's checks (0), termination, and
  bar symmetry, now structural theorems for ALL `N` (the probe verified
  `N ≤ 9`).
* `coloredJones41_two` — anchor: `J_2` is the Jones polynomial of 4₁.

## Base ring (§7c)

The Newton-ladder section is generic `{R : Type*} [CommRing R]` (no
inverses).  Nodes `λ_j`, the Habiro term, and the colored Jones need `q⁻¹`,
hence `{K : Type*} [Field K]` — still fully algebraic, no `ℝ`, no ordering,
no archimedean construct.  Bar involution is the literal map `q ↦ q⁻¹`.

## What this file does NOT prove

That `coloredJones41` agrees with the quantum-group / skein-theoretic
colored Jones of 4₁ — the Habiro–Lê formula is taken as the definition here
(it is the form the corpus's compute uses and the literature proves;
Ref: [habiro2000] §3, the 4₁ formula, also due to Lê; [nguyen-tran-2021]).  No claim about the AJ conjecture
itself is made or needed.
-/

namespace QOU.BraidKnot.HabiroNewtonLadder

open Finset

/-! ## Generalized Newton ladder — any commutative ring, any node sequence -/

section NewtonLadder
variable {R : Type*} [CommRing R]

/-- Newton-interpolation ladder on the nodes `a 1, a 2, …`:
    `g_k(x) = ∏_{j=1}^{k} (x − a j)`. -/
def newtonLadder (a : ℕ → R) (x : R) (k : ℕ) : R :=
  ∏ j ∈ Finset.range k, (x - a (j + 1))

@[simp] theorem newtonLadder_zero (a : ℕ → R) (x : R) :
    newtonLadder a x 0 = 1 := by
  simp [newtonLadder]

/-- **The ladder is two-term (first-order): `B_k ≡ 0`.**  In the normal form
    `g_{k+1} = A_k g_k + B_k g_{k−1}` the multiplier is `A_k = x − a (k+1)`
    and the lower coefficient vanishes identically — the degenerate
    Newton-interpolation boundary of the Askey–Wilson three-term shape. -/
theorem newtonLadder_succ (a : ℕ → R) (x : R) (k : ℕ) :
    newtonLadder a x (k + 1) = (x - a (k + 1)) * newtonLadder a x k := by
  unfold newtonLadder
  rw [Finset.prod_range_succ]
  ring

/-- **Generalized Casoratian collapse.**  Over any commutative ring, any two
    solutions of a first-order (two-term) ladder `u_{k+1} = A_k u_k` have
    identically vanishing Casoratian (discrete Wronskian).  This is the
    structural reason a `B_k ≡ 0` ladder carries no Casoratian sign
    information for the 1jrh Askey–Wilson test. -/
theorem casoratian_eq_zero (A u v : ℕ → R)
    (hu : ∀ k, u (k + 1) = A k * u k) (hv : ∀ k, v (k + 1) = A k * v k)
    (k : ℕ) :
    u k * v (k + 1) - u (k + 1) * v k = 0 := by
  rw [hu, hv]; ring

/-- The Newton ladder is itself such a first-order ladder, so its Casoratian
    against any other solution of the same ladder vanishes. -/
theorem newtonLadder_casoratian_eq_zero (a : ℕ → R) (x : R) (v : ℕ → R)
    (hv : ∀ k, v (k + 1) = (x - a (k + 1)) * v k) (k : ℕ) :
    newtonLadder a x k * v (k + 1) - newtonLadder a x (k + 1) * v k = 0 :=
  casoratian_eq_zero (fun k => x - a (k + 1)) _ v
    (newtonLadder_succ a x) hv k

/-- **Generalized termination**: once the evaluation point hits a node
    (`x = a m`, `1 ≤ m`), every ladder element of index `≥ m` vanishes. -/
theorem newtonLadder_eq_zero (a : ℕ → R) {x : R} {m : ℕ}
    (hm : 1 ≤ m) (hx : x = a m) {k : ℕ} (hk : m ≤ k) :
    newtonLadder a x k = 0 := by
  refine Finset.prod_eq_zero (i := m - 1) (Finset.mem_range.mpr (by omega)) ?_
  have h1 : m - 1 + 1 = m := by omega
  rw [h1, hx, sub_self]

/-- **Generalized sum truncation**: the ladder sum is stable under extending
    the range past the hit node — the 4₁ mechanism `Λ_N = λ_N` in general
    form. -/
theorem newtonLadder_sum_stable (a : ℕ → R) {x : R} {m : ℕ}
    (hm : 1 ≤ m) (hx : x = a m) {k : ℕ} (hK : m ≤ k) :
    ∑ i ∈ Finset.range k, newtonLadder a x i
      = ∑ i ∈ Finset.range m, newtonLadder a x i := by
  refine (Finset.sum_subset
    (fun i hi => Finset.mem_range.mpr
      (lt_of_lt_of_le (Finset.mem_range.mp hi) hK)) ?_).symm
  intro i _ hi
  exact newtonLadder_eq_zero a hm hx
    (le_of_not_gt fun h => hi (Finset.mem_range.mpr h))

end NewtonLadder

/-! ## The figure-eight instance — bar-even nodes over a field -/

section FigureEight
variable {K : Type*} [Field K]

/-- The bar-even node `λ_j = q^j + q^{−j}` (written inverse-explicitly). -/
def lam (q : K) (j : ℕ) : K := q ^ j + (q ^ j)⁻¹

/-- **Nodes are bar-even**: `λ_j(q⁻¹) = λ_j(q)`.  Holds unconditionally over
    a field (`0⁻¹ = 0` covers `q = 0`). -/
@[simp] theorem lam_bar_even (q : K) (j : ℕ) : lam q⁻¹ j = lam q j := by
  simp [lam, inv_pow, add_comm]

/-- **The ladder multiplier `A_k = x − λ_{k+1}` is bar-even** (for any
    bar-fixed `x`) — the shape requirement of the 1jrh one-recurrence
    hypothesis, satisfied on the proved knot side. -/
theorem multiplier_bar_even (q x : K) (k : ℕ) :
    x - lam q⁻¹ (k + 1) = x - lam q (k + 1) := by
  rw [lam_bar_even]

/-- The Habiro–Lê summand of the figure-eight colored Jones:
    `q^{Nk} · (q^{−N−1}; q^{−1})_k · (q^{−N+1}; q)_k`, with the two
    q-Pochhammer products written inverse-explicitly. -/
def habiroTerm (q : K) (N k : ℕ) : K :=
  q ^ (N * k) * (∏ j ∈ Finset.range k, (1 - (q ^ (N + 1 + j))⁻¹))
    * ∏ j ∈ Finset.range k, (1 - q ^ (j + 1) * (q ^ N)⁻¹)

/-- Per-factor identity:
    `q^N (1 − q^{−N−1−j})(1 − q^{j+1−N}) = λ_N − λ_{j+1}`. -/
theorem habiro_factor {q : K} (hq : q ≠ 0) (N j : ℕ) :
    q ^ N * ((1 - (q ^ (N + 1 + j))⁻¹) * (1 - q ^ (j + 1) * (q ^ N)⁻¹))
      = lam q N - lam q (j + 1) := by
  have hN : q ^ N ≠ 0 := pow_ne_zero _ hq
  have hj : q ^ (j + 1) ≠ 0 := pow_ne_zero _ hq
  have hNj : q ^ (N + 1 + j) ≠ 0 := pow_ne_zero _ hq
  unfold lam
  field_simp
  ring

/-- **Termwise Habiro ↔ Newton identity** (strictly stronger than the summed
    probe check): each Habiro–Lê summand IS the Newton-ladder element on the
    bar-even nodes, evaluated at `x = λ_N`. -/
theorem habiroTerm_eq_newtonLadder {q : K} (hq : q ≠ 0) (N : ℕ) :
    ∀ k, habiroTerm q N k = newtonLadder (lam q) (lam q N) k := by
  intro k
  induction k with
  | zero => simp [habiroTerm]
  | succ k ih =>
      have step : habiroTerm q N (k + 1)
          = q ^ N * ((1 - (q ^ (N + 1 + k))⁻¹) * (1 - q ^ (k + 1) * (q ^ N)⁻¹))
            * habiroTerm q N k := by
        unfold habiroTerm
        rw [Finset.prod_range_succ, Finset.prod_range_succ]
        ring
      rw [step, habiro_factor hq N k, newtonLadder_succ, ih]

/-- The N-colored Jones polynomial of the figure-eight knot `4₁`
    (Habiro–Lê form, normalized `J_1 = 1`), as used by
    `computations/figure_eight_aj_operator.py`. -/
def coloredJones41 (q : K) (N : ℕ) : K :=
  ∑ k ∈ Finset.range N, habiroTerm q N k

/-- **Main identity (Λ-Newton / cyclotomic form), all `N`**:
    `J_N(4₁; q) = ∑_{k<N} ∏_{j=1}^{k} (Λ_N − λ_j)` with `Λ_N = λ_N` — all
    Habiro cyclotomic coefficients equal 1. -/
theorem coloredJones41_eq_newton_sum {q : K} (hq : q ≠ 0) (N : ℕ) :
    coloredJones41 q N
      = ∑ k ∈ Finset.range N, newtonLadder (lam q) (lam q N) k :=
  Finset.sum_congr rfl fun k _ => habiroTerm_eq_newtonLadder hq N k

/-- **Termination, all `N ≥ 1`**: extending the Newton sum past `k = N − 1`
    changes nothing — the `j = N` factor is `λ_N − λ_N = 0` (the probe's
    check for `N ≤ 6`, now structural). -/
theorem coloredJones41_sum_stable {q : K} (hq : q ≠ 0) {N k : ℕ}
    (hN : 1 ≤ N) (hK : N ≤ k) :
    coloredJones41 q N
      = ∑ i ∈ Finset.range k, newtonLadder (lam q) (lam q N) i := by
  rw [coloredJones41_eq_newton_sum hq,
      newtonLadder_sum_stable (lam q) hN rfl hK]

/-- **Bar symmetry / amphichirality, all `N`**: `J_N(4₁; q⁻¹) = J_N(4₁; q)`
    — manifest from the Λ-Newton form since every node is bar-even (the
    probe's empirical check for `N ≤ 9`, now structural). -/
theorem coloredJones41_bar_symmetric {q : K} (hq : q ≠ 0) (N : ℕ) :
    coloredJones41 q⁻¹ N = coloredJones41 q N := by
  rw [coloredJones41_eq_newton_sum (inv_ne_zero hq),
      coloredJones41_eq_newton_sum hq]
  refine Finset.sum_congr rfl fun k _ => ?_
  simp [newtonLadder]

/-- **Anchor**: `J_2` is the Jones polynomial of the figure-eight,
    `V(4₁) = q² + q⁻² − q − q⁻¹ + 1` (the same anchor the compute uses). -/
theorem coloredJones41_two {q : K} (hq : q ≠ 0) :
    coloredJones41 q 2 = q ^ 2 + (q ^ 2)⁻¹ - q - q⁻¹ + 1 := by
  have h2 : q ^ 2 ≠ 0 := pow_ne_zero _ hq
  have h3 : q ^ 3 ≠ 0 := pow_ne_zero _ hq
  simp only [coloredJones41, habiroTerm, Finset.sum_range_succ,
    Finset.sum_range_zero, Finset.prod_range_succ, Finset.prod_range_zero]
  field_simp
  ring

end FigureEight

end QOU.BraidKnot.HabiroNewtonLadder
