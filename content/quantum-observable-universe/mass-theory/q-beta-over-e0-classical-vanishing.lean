/-
  # S(q) = Q_β(q) / E_0(q) vanishes at the classical point q = 1

  Sibling .lean for the `prop:q-beta-over-e0-classical-vanishing`
  block.  Algebraic content: the simplified ratio
  `S(q) = (2q + 1 − q²)·(q² − 1) / (2q²)` of the substrate closed
  forms for Q_β and E_0 (N=0 variant) inherits a (q − 1) factor in
  its numerator from the (q² − 1) = (q+1)(q−1) substrate expression.
  Hence S(1) = 0, and the audit doc's "c_k from u_ladder Taylor of
  S(q)" recipe is degenerate when S is interpreted as Q_β/E_0.

  Sorry-free.  Two theorems:

  * `qbeta_over_e0_numerator_at_one_eq_zero` — the numerator
    `(2q + 1 − q²)·(q² − 1)` vanishes at q = 1.  One-line `ring`
    proof over any CommRing R.

  * `qbeta_over_e0_at_one_eq_zero` — the full ratio
    `(2q + 1 − q²)(q² − 1) / (2q²)` vanishes at q = 1.  Follows
    from the numerator vanishing via Field R.

  Ref: [pr1769] https://github.com/litlfred/qou/pull/1769
       [pr1752] https://github.com/litlfred/qou/pull/1752
       [jones1987] https://doi.org/10.2307/1971403
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
       docs/audits/2026-06-03-qbeta-sdp-strict-complementarity-partial.md
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.QBeta.OverE0ClassicalVanishing

universe u

/-- **Numerator of $S(q) = Q_\beta(q)/E_0(q)$ vanishes at $q = 1$.**

    The simplified ratio of the substrate closed forms factors as
    `S(q) = (2q + 1 − q²) · (q² − 1) / (2q²)`.  At `q = 1` the second
    factor `q² − 1` is zero, so the whole numerator vanishes — an
    algebraic identity over any commutative ring.  This is the
    diagnostic of PR #1769: Q_β's `(q + 1)` factor meets E_0's
    `1/[q(q − 1)]` pole and their product carries no constant term
    at the classical point. -/
theorem qbeta_over_e0_numerator_at_one_eq_zero {R : Type u} [CommRing R] :
    (2 * (1 : R) + 1 - 1 ^ 2) * (1 ^ 2 - 1) = 0 := by
  ring

/-- The simplified closed form of `S(q) = Q_β(q) / E_0(q)` using the
    `N = 0` form of `E_0`.  The `m_e` mass scale cancels in the ratio,
    consequently the result is a pure rational function of `q`. -/
noncomputable def S_N0 {R : Type u} [Field R] (q : R) : R :=
  (2 * q + 1 - q ^ 2) * (q ^ 2 - 1) / (2 * q ^ 2)

/-- **$S(q) = Q_\beta(q) / E_0(q)$ vanishes at the classical point $q = 1$.**

    Direct consequence of the numerator-vanishing identity: at `q = 1`
    the rational function `S_N0` evaluates to `0 / 2 = 0`.

    *Consequence for the precision ladder.*  The shape-collapse audit
    `2026-06-03-qbeta-markov-trace-shape-collapse.md` states the `c_k`
    Taylor coefficients come from this `S(q)` — but `S(1) = 0` means
    the Taylor expansion of `S/S(1)` is degenerate (`0/0`).  Hence the
    `c_k` ladder normalization is not `Q_β / E_0` (which is the
    *SDP-constraint scalar*, evaluated at `q_0`); the actual ladder
    normalization is `Q_β / [Q_A · cos(α_eff)]` per
    `qbeta_1ppq_achieved.py`, and `Q_A` is the CODATA-free bare scale
    identified by the SDP strict-complementarity route in PR #1752. -/
theorem qbeta_over_e0_at_one_eq_zero {R : Type u} [Field R] :
    S_N0 (1 : R) = 0 := by
  unfold S_N0
  have h : (2 * (1 : R) + 1 - 1 ^ 2) * (1 ^ 2 - 1) = 0 :=
    qbeta_over_e0_numerator_at_one_eq_zero
  rw [h, zero_div]

end QOU.QBeta.OverE0ClassicalVanishing
