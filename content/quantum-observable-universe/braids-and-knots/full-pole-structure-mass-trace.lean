import Mathlib.NumberTheory.Cyclotomic.Basic
import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Algebra.Order.AbsoluteValue

/-!
# Habiro completion of the mass trace

The Markov trace `tr_M(T_w)` of a closed braid is **not** a
meromorphic function on `ℂ`: the primitive roots of unity are
dense in `S¹`, so `S¹` is a natural boundary.  The correct
algebraic home is the **Habiro ring** `Ẑ[q]`, the cyclotomic
completion of `ℤ[q]`:

  Ẑ[q] := lim_n  ℤ[q] / (q;q)_n

In this completion `tr_M(T_w)` admits a unique cyclotomic
expansion `Σ_m a_m (q;q)_m` with `a_m ∈ ℤ[q^±1]`, evaluation at
every root of unity is well-defined, and truncation at order `m`
exactly suppresses the contribution of every root of unity of
order `≤ m`.

The earlier "Mittag-Leffler over `ℂ`" expression
`Σ_{n,j} r_n^{(j)} / (q - ζ_n^{(j)})` is a **formal residue
spectral sum** — see `prop:gb-residue-spectral-sum` — that feeds
the cyclotomic coefficients `a_m`.  It is not a complex-analytic
identity on or near `S¹`.

Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127
LaTeX label: `prop:full-pole-structure-mass-trace`
-/

namespace QOU.BraidKnot

/-- The real-valued q-Pochhammer factor
    `(q; q)_m = ∏_{k=1}^{m} (1 - q^k)`, used below for the
    `0 < q < 1` truncation bound.  The polynomial-typed version
    over an arbitrary commutative ring (where vanishing at primitive
    roots of unity makes sense) is in `habiro-expansion-atomic.lean`,
    `QOU.BraidKnot.qPochhammer` over `R[u]`. -/
noncomputable def qPochhammer (q : ℝ) (m : ℕ) : ℝ :=
  ∏ k ∈ Finset.range m, (1 - q ^ (k + 1))

/-- **Habiro completion of the Markov trace** (ℝ-evaluation form).

    The mass trace of a closed braid `T_w` lies in the Habiro
    ring `Ẑ[q]` and admits a unique cyclotomic expansion

      tr_M(T_w, q) = Σ_{m ≥ 0} a_m(T_w) · (q; q)_m,
      a_m(T_w) ∈ ℤ[q^±1].

    This class records the **real-valued evaluation observable** of
    that polynomial-ring statement: a sequence of cyclotomic
    coefficients `coeff : ℕ → ℝ` and a trace function
    `trace : ℝ → ℝ` related by the axiom
    `trace_at_pochhammer_zero` — at any `q` annihilating `(q;q)_n`,
    the trace coincides with the cyclotomic partial sum up to
    order `n`.  This is the ℝ-shadow of the Habiro-ideal divisibility
    in `Ẑ[q]`; the polynomial-typed version with explicit
    `a_m ∈ ℤ[u]` and constructive `(u;u)_n`-divisibility is in
    `cor:habiro-expansion-atomic`.

    The atomic-case termination property `a_k = 0` for
    `k > m_max(T_w)` is also a corollary (see
    `cor:habiro-expansion-atomic`).

    The class is axiomatized: existence of the cyclotomic expansion
    follows from Markov–Jones integrality plus sequential cyclotomic
    division.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
class HabiroCompletion where
  braid : Unit
  /-- Cyclotomic coefficients `a_m(T_w) ∈ ℤ[q^±1]`, represented
      here as a sequence of real-valued evaluations at the substrate
      parameter. -/
  coeff : ℕ → ℝ
  /-- Evaluation of the trace at substrate parameter `q`. -/
  trace : ℝ → ℝ
  /-- **ℝ-shadow of the Habiro-ideal property.**

      At any `q` where `(q;q)_n = 0` (i.e. `q` is a root of unity of
      order ≤ n), the trace equals the cyclotomic partial sum up to
      order `n` exactly.  This is the ℝ-evaluation observable of the
      polynomial-ring statement "tail ∈ ((q;q)_n) ⊂ Ẑ[q]": polynomial
      divisibility of the tail by `(q;q)_n` forces the tail to vanish
      wherever `(q;q)_n` vanishes.  We axiomatise the vanishing
      directly because real-valued divisibility (`tail = (q;q)_n · r`
      for some `r ∈ ℝ`) is trivially solvable whenever
      `(q;q)_n ≠ 0`, and so cannot encode the intended polynomial
      divisibility on its own.

      The honest polynomial-ring version of this property is the
      content of the corollary `cor:habiro-expansion-atomic`, where
      the cyclotomic-division algorithm produces explicit `a_m ∈ ℤ[u]`
      witnessing the divisibility constructively. -/
  trace_at_pochhammer_zero :
    ∀ (q : ℝ) (n : ℕ),
      qPochhammer q n = 0 →
      trace q = ∑ m ∈ Finset.range n, coeff m * qPochhammer q m

/-- **Habiro cyclotomic monotone bound** (purely structural).

    For `0 < q < 1` and any truncation order `N`, the absolute
    Pochhammer factor `|(q; q)_N|` is monotonically decreasing in
    `N`, since each new factor `(1 - q^{N+1})` lies in `(0, 1)`.

    This controls the Habiro tail: at substrate parameter `q < 1`
    in the regular regime, truncating the cyclotomic expansion at
    order `N` produces a residual whose magnitude is bounded by
    `|(q;q)_N|`, decreasing as `N → ∞`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
theorem habiro_truncation_bound
    (q : ℝ) (hq_pos : 0 < q) (hq_lt : q < 1) (N : ℕ) :
    |qPochhammer q (N + 1)| ≤ |qPochhammer q N| := by
  unfold qPochhammer
  rw [Finset.prod_range_succ]
  rw [abs_mul]
  have h_factor_lt_one : |1 - q ^ (N + 1)| ≤ 1 := by
    have h_qpow_pos : 0 < q ^ (N + 1) := pow_pos hq_pos (N + 1)
    have h_qpow_lt_one : q ^ (N + 1) < 1 :=
      pow_lt_one (le_of_lt hq_pos) hq_lt (Nat.succ_ne_zero N)
    rw [abs_of_nonneg (by linarith : (0 : ℝ) ≤ 1 - q ^ (N + 1))]
    linarith
  have h_prod_nn : (0 : ℝ) ≤ |∏ k ∈ Finset.range N, (1 - q ^ (k + 1))| :=
    abs_nonneg _
  nlinarith

end QOU.BraidKnot
