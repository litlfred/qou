import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.AbsoluteValue
import Mathlib.Algebra.GroupPower.Order
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Tactic.Linarith

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
    `(q; q)_m = ∏_{k=1}^{m} (1 - q^k)`, used in the
    `0 < q < 1` truncation bound below. -/
noncomputable def qPochhammer (q : ℝ) (m : ℕ) : ℝ :=
  ∏ k ∈ Finset.range m, (1 - q ^ (k + 1))

/-- **Polynomial q-Pochhammer** `(u; u)_m = Π_{k=1}^{m} (1 - u^k) ∈ ℤ[u]`.

    This is the polynomial-ring companion of `qPochhammer` above.
    Polynomial divisibility by `qPochhammerPoly N` is non-trivial:
    `qPochhammerPoly N` has degree `N(N+1)/2` and is a non-unit in
    `ℤ[u]`, so divisibility encodes the Habiro-ideal property
    genuinely (unlike real divisibility, which is trivially solvable
    whenever the divisor is non-zero).

    The generic ring-valued analogue
    `QOU.BraidKnot.qPochhammer (u : R) : ℕ → R` over an arbitrary
    `[CommRing R]` lives in the sibling file
    `habiro-expansion-atomic.lean`; this is the specialisation
    `qPochhammer (Polynomial.X : Polynomial ℤ)`.  The two
    definitions are duplicated only because each sibling `.lean`
    file is read standalone (not yet part of a shared Lake
    module); a future `QOU.BraidKnot.HabiroBasic` module would let
    both files import a single source. -/
noncomputable def qPochhammerPoly (m : ℕ) : Polynomial ℤ :=
  ∏ k ∈ Finset.range m, (1 - (Polynomial.X : Polynomial ℤ) ^ (k + 1))

/-- **Habiro completion of the Markov trace** (polynomial-ring form).

    The mass trace of a closed braid `T_w` lies in the Habiro
    ring `Ẑ[q]` and admits a unique cyclotomic expansion

      tr_M(T_w, u) = Σ_{m ≥ 0} a_m(T_w) · (u; u)_m,
      a_m(T_w) ∈ ℤ[u].

    (After Markov normalisation by `D(u)` — see field `trace`
    below — the prefactor leaves the cyclotomic coefficients
    `a_m` in the regular polynomial ring `ℤ[u]` rather than in
    the Laurent ring `ℤ[u^±1]`.)

    This class records the trace as a polynomial `trace : ℤ[u]`,
    the cyclotomic coefficients `coeff : ℕ → ℤ[u]`, and the
    substantive axiom `tail_in_ideal`: at every truncation order
    `N`, the residual `trace - Σ_{m<N} a_m · (u;u)_m` lies in the
    Habiro ideal `((u;u)_N) ⊂ ℤ[u]`.

    **Why polynomial-typed.**  Polynomial divisibility by
    `qPochhammerPoly N` is non-trivial: the divisor has degree
    `N(N+1)/2` and is a non-unit, so the divisibility constraint
    cuts out a proper subset of polynomials.  An earlier
    ℝ-evaluation-only formulation was vacuous (real divisibility by
    a non-zero divisor is always solvable); the polynomial form
    above repairs that and is what Gemini and Copilot reviews
    requested as the "honest Habiro-ideal" statement.

    **ℝ-evaluation shadow.**  The earlier ℝ-evaluation observable
    ("at any `q` annihilating `(q;q)_n`, the trace equals the
    cyclotomic partial sum up to order `n`") follows by evaluating
    both sides of `tail_in_ideal` at the relevant `q` (mapping
    `ℤ[u] → ℝ` via `Polynomial.eval₂ (Int.castRingHom ℝ) q`): if
    `(u;u)_N` divides the tail in `ℤ[u]`, then at any `q` where
    `(q;q)_N = 0` the tail evaluates to `0`.

    The class is axiomatised: existence of the cyclotomic expansion
    follows from Markov–Jones integrality plus sequential cyclotomic
    division, formalised in `cor:habiro-expansion-atomic`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
class HabiroCompletion where
  /-- The Markov trace as a polynomial in `ℤ[u]` (Markov-normalised
      so that the result is integer-coefficient; the Laurent prefactor
      `D(u)` is folded into `trace`). -/
  trace : Polynomial ℤ
  /-- Cyclotomic coefficients `a_m(T_w) ∈ ℤ[u]`. -/
  coeff : ℕ → Polynomial ℤ
  /-- **Habiro-ideal property.**

      At every truncation order `N`, the residual
      `trace - Σ_{m<N} a_m · (u;u)_m` lies in the principal ideal
      `((u;u)_N) ⊂ ℤ[u]`.

      Non-vacuous: `qPochhammerPoly N` has degree `N(N+1)/2` and is
      a non-unit, so this divisibility genuinely constrains the
      coefficient sequence.  In particular, evaluating both sides
      at any `q` with `qPochhammer q N = 0` forces the trace to
      equal the cyclotomic partial sum up to order `N` (the
      ℝ-evaluation shadow). -/
  tail_in_ideal :
    ∀ (N : ℕ),
      qPochhammerPoly N ∣
        (trace - ∑ m ∈ Finset.range N, coeff m * qPochhammerPoly m)

/-- **Habiro cyclotomic monotone bound** (purely structural).

    For `0 < q < 1` and any truncation order `N`, the absolute
    Pochhammer factor `|(q; q)_N|` is monotonically decreasing in
    `N`, since each new factor `(1 - q^{N+1})` lies in `(0, 1)`.

    Scope: this lemma is stated for `q ∈ (0, 1)`. The QOU substrate
    sits at `q₀ ≈ 1.110 > 1`, so this bound does **not** apply
    directly at the substrate value: for `q > 1` the factor
    `|1 - q^{N+1}|` grows with `N` and `|(q;q)_N|` is monotone
    *increasing*. Truncation control at the substrate uses the
    `q ↔ q⁻¹` duality of the Hecke algebra (so that `q₀⁻¹ ≈ 0.901`
    falls in the `(0, 1)` regime where this lemma applies); the
    duality bridge itself is left to `prop:full-pole-structure-mass-trace`
    in the narrative.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
theorem habiro_truncation_bound
    (q : ℝ) (hq_pos : 0 < q) (hq_lt : q < 1) (N : ℕ) :
    |qPochhammer q (N + 1)| ≤ |qPochhammer q N| := by
  unfold qPochhammer
  rw [Finset.prod_range_succ, abs_mul]
  have h_factor_lt_one : |1 - q ^ (N + 1)| ≤ 1 := by
    have h_qpow_pos : 0 < q ^ (N + 1) := pow_pos hq_pos (N + 1)
    have h_qpow_lt_one : q ^ (N + 1) < 1 :=
      pow_lt_one (le_of_lt hq_pos) hq_lt (Nat.succ_ne_zero N)
    rw [abs_of_nonneg (by linarith : (0 : ℝ) ≤ 1 - q ^ (N + 1))]
    linarith
  exact mul_le_of_le_one_right (abs_nonneg _) h_factor_lt_one

/-- **Supercritical truncation bound** (q > 1, the QOU substrate
    regime).  At `q₀ ≈ 1.110 > 1` the original `habiro_truncation_bound`
    does not apply directly — each new factor `|1 - q^{N+1}|` exceeds
    1.  Bridges via the Habiro `q ↔ q⁻¹` involution: `q > 1` implies
    `0 < q⁻¹ < 1`, so the original bound applies to `qPochhammer q⁻¹`.

    Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127. -/
theorem habiro_truncation_bound_supercrit
    (q : ℝ) (hq : 1 < q) (N : ℕ) :
    |qPochhammer (q⁻¹) (N + 1)| ≤ |qPochhammer (q⁻¹) N| := by
  have hqpos : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hinvpos : (0 : ℝ) < q⁻¹ := inv_pos.mpr hqpos
  have hinvlt : q⁻¹ < 1 := by
    have hne : q ≠ 0 := ne_of_gt hqpos
    have hmul : q⁻¹ * q = 1 := inv_mul_cancel₀ hne
    nlinarith
  exact habiro_truncation_bound (q⁻¹) hinvpos hinvlt N

end QOU.BraidKnot
