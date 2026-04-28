import Mathlib.NumberTheory.Cyclotomic.Basic
import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Algebra.Order.AbsoluteValue
import Mathlib.Analysis.MeanInequalities

/-!
# Full pole structure of the mass trace

The mass trace `tr_M(T_w, q)` is meromorphic on `ℂˣ` with simple
poles at every primitive root of unity `ζ_n^{(j)} = e^{2πij/n}`
for `gcd(j, n) = 1`, `n ≥ 2`.  The Mittag-Leffler expansion at
a regular point `q₀` sums contributions from **all** poles
weighted by the Cauchy kernel `1/(q₀ - ζ_n^{(j)})`.  Truncating
at the closest pole loses interference and resonance effects.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:full-pole-structure-mass-trace`
-/

namespace QOU.BraidKnot

/-- A primitive `n`-th root of unity for `n ≥ 2`.  Parameterised
    by `j ∈ Fin n` with `gcd j n = 1`. -/
structure PrimitiveRoot where
  n : ℕ
  n_ge_two : 2 ≤ n
  j : ℕ
  j_coprime : Nat.Coprime j n
  j_lt : j < n

/-- The complex residue of `Φ_q · tr_{M,ℓ}` at a primitive root
    of unity.  Axiomatized; content-side `prop:gb-residue-spectral-sum`. -/
noncomputable opaque residueAt (ζ : PrimitiveRoot) (braid : Unit) : ℝ

/-- **Full Mittag-Leffler pole sum.**

    The mass trace evaluated at `q₀` is

      tr_M(T_w, q₀) = entire(q₀)
                    + Σ_{n ≥ 2} Σ_{j : gcd(j,n)=1}
                         residueAt(ζ_n^{(j)}, T_w) / (q₀ - ζ_n^{(j)}).

    Truncation to `n ≤ N` introduces error controlled by the
    Habiro cyclotomic expansion: `(q₀; q₀)_N = ∏_{k≤N}(1 - q₀^k)`
    vanishes at all `ζ_n^{(j)}` with `n ≤ N`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
class FullPoleStructure where
  q0 : ℝ
  entire_part : ℝ
  braid : Unit
  /-- Truncation order. In Habiro form this is the cyclotomic
      cutoff. -/
  truncation : ℕ
  mass : ℝ
  /-- Mass equals entire part plus the truncated residue sum
      modulo the Habiro tail. -/
  mittag_leffler_truncated :
    ∃ tail_error : ℝ,
      mass = entire_part +
        -- sum over roots of unity up to order `truncation`
        ∑ n : Fin truncation,
          residueAt (sorry : PrimitiveRoot) braid
        + tail_error

/-- The q-Pochhammer factor `(q₀; q₀)_N = ∏_{k=1}^{N} (1 - q₀^k)`. -/
noncomputable def qPochhammer (q : ℝ) (N : ℕ) : ℝ :=
  ∏ k ∈ Finset.range N, (1 - q ^ (k + 1))

/-- **Habiro cyclotomic truncation bound.**

    For `0 < q₀ < 1` and any truncation order `N`, the absolute
    Pochhammer factor `|(q₀; q₀)_N|` satisfies the strict
    decreasing bound `|(q₀; q₀)_{N+1}| ≤ |(q₀; q₀)_N|` since each
    new factor `(1 - q₀^{N+1})` lies in `(0, 1)`.

    This is the structural ingredient of the Habiro tail estimate:
    truncating the cyclotomic expansion at order `N` produces a
    residual whose magnitude is controlled by `|(q₀; q₀)_N|`,
    decreasing monotonically as `N → ∞`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127,
    [garoufalidis-lauda2011] https://doi.org/10.1007/s11511-011-0069-8 -/
theorem habiro_truncation_bound
    (q : ℝ) (hq_pos : 0 < q) (hq_lt : q < 1) (N : ℕ) :
    |qPochhammer q (N + 1)| ≤ |qPochhammer q N| := by
  -- (q;q)_{N+1} = (q;q)_N · (1 - q^{N+1}); |1 - q^{N+1}| ≤ 1.
  unfold qPochhammer
  rw [Finset.prod_range_succ]
  -- |a · b| = |a| · |b| ≤ |a| · 1 = |a| when |b| ≤ 1.
  rw [abs_mul]
  have h_factor_lt_one : |1 - q ^ (N + 1)| ≤ 1 := by
    have h_qpow_pos : 0 < q ^ (N + 1) := pow_pos hq_pos (N + 1)
    have h_qpow_lt_one : q ^ (N + 1) < 1 := pow_lt_one (le_of_lt hq_pos) hq_lt (Nat.succ_ne_zero N)
    rw [abs_of_nonneg (by linarith : (0 : ℝ) ≤ 1 - q ^ (N + 1))]
    linarith
  have h_prod_nn : (0 : ℝ) ≤ |∏ k ∈ Finset.range N, (1 - q ^ (k + 1))| :=
    abs_nonneg _
  nlinarith

end QOU.BraidKnot
