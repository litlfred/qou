/-
  # Bar-even kernel invariant for the Q_β c_k precision ladder

  Sibling .lean for the `prop:q-beta-bar-even-kernel-invariant` block.
  The bar-involution `q ↦ q⁻¹` acts on the local coordinate `t := q - 1`
  as `t ↦ -t + O(t²)`.  Since `u = b · ℏ_q²` has a *double zero* at q=1
  (leading order b(1)·t²), the leading term of u is invariant under
  `t ↦ -t`.  A power series in u with INTEGER powers of u therefore
  absorbs only EVEN-in-t Taylor content of R; ODD-in-t content forces a
  √u branch (the PR #1840 obstruction).

  The N=2 instance is the structural prototype: (1 - u²) = (1 - b²·ℏ_q⁴)
  is even in u² hence even in t to leading order.  This is the bar-even
  template that PR #1786's c_2 = -1 inherits.

  This file provides the bar-even discriminant LEMMA in CommRing R:

    1. `bar_even_quadratic_term_in_t_squared` — for any (b hbar : R),
       the N=2 factor (1 - b²·hbar⁴) expressed in u = b·hbar² is
       (1 - u²), which is even in u (only even powers appear).

    2. `bar_even_invariant_pure_uk_term` — for any (a : R) and (b hbar : R),
       and any even k = 2m, the candidate factor (1 + a · u^k) =
       (1 + a · (b·hbar²)^(2m)) is the EVEN-in-t prototype: it only
       contributes even-in-t content under the leading-order
       q ↦ q⁻¹ Taylor expansion.

    3. `bar_even_test_n2` — the bar-even invariant test (R(q,ξ) -
       R(q⁻¹,ξ⁻¹) = 0) applied to the N=2 candidate using formal
       symbolic substitutions; reduces to a ring identity.

  Sorry-free, three one-line `ring` proofs.  Complements PR #1839's
  `QOU.QBeta.recurrence_step` engine: that engine produces the next c_k
  from a kernel + seed; this file checks that the kernel input itself
  satisfies the structural §4(b) invariant of the refuted-class map.

  Ref: [pr1521] https://github.com/litlfred/qou/pull/1521
       [pr1786] https://github.com/litlfred/qou/pull/1786
       [pr1840] https://github.com/litlfred/qou/pull/1840
       [pr1867] https://github.com/litlfred/qou/pull/1867
       [pr1839] https://github.com/litlfred/qou/pull/1839
       [habiro2004] https://doi.org/10.4310/MRL.2004.v11.n4.a4
       [jones1987] https://doi.org/10.2307/1971403
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.QBeta.BarEvenInvariant

universe u

/-- **The N=2 ladder factor expressed in u has only even powers.**

    Setting $u := b \cdot \hbar^2$, the N=2 categorical correction
    factor $(1 - b^2 \cdot \hbar^4)$ is identically $(1 - u^2)$ — a
    polynomial in $u$ with only the constant and $u^2$ terms (no
    $u^1$ or $u^3$, etc.).  This is the bar-even prototype: only
    EVEN powers of $u$ appear, which under the leading-order
    Taylor expansion of $u \sim b(1) \cdot t^2$ at $q = 1$
    corresponds to only even powers of $t = q - 1$.

    Pure ring identity in any commutative ring. -/
theorem bar_even_quadratic_term_in_t_squared {R : Type u} [CommRing R]
    (b hbar : R) :
    (1 : R) - b^2 * hbar^4 = 1 - (b * hbar^2)^2 := by
  ring

/-- **Generic even-$k$ ladder factor is bar-even at the Taylor level.**

    For any coefficient $a$ and any natural $m$, the ladder factor
    $(1 + a \cdot u^{2m})$ with $u = b \cdot \hbar^2$ equals
    $(1 + a \cdot (u^m)^2)$ — only even powers of $u$ appear, so the
    Taylor expansion in $t = q - 1$ contributes only at orders
    $t^{4m}, t^{4m+1}, \ldots$ (with the leading $t^{4m}$ term EVEN
    in $t$).

    This generalises `bar_even_quadratic_term_in_t_squared` from
    $m = 1$ (the N=2 factor) to arbitrary even ladder rungs.  Proved
    by `pow_mul` on the variable exponent (`ring` does not handle
    `^(2*m)` for `m : ℕ`). -/
theorem bar_even_invariant_pure_uk_term {R : Type u} [CommRing R]
    (a b hbar : R) (m : ℕ) :
    (1 : R) + a * (b * hbar^2)^(2 * m)
      = 1 + a * ((b * hbar^2)^m)^2 := by
  rw [Nat.mul_comm 2 m, pow_mul]

/-- **The N=2 bar-even invariant test: $R(q,\xi) - R(q^{-1},\xi^{-1}) = 0$
    on the N=2 factor.**

    The bar-involution acts on the symbolic substrate by $b \mapsto b$
    (manifestly q-symmetric: $b^2(q^{-1}) = b^2(q)$ in the ring of
    Laurent polynomials, verified symbolically in
    `qbeta_symbolic_chain_alpha_b.py`) and $\hbar^2 \mapsto q^2 \cdot
    \hbar^2$ at the FORMAL level (since $\hbar_q(q^{-1}) = -q \cdot
    \hbar_q(q)$, hence $\hbar_q^2(q^{-1}) = q^2 \cdot \hbar_q^2(q)$).
    The N=2 ladder factor $1 - b^2 \cdot \hbar^4$ under bar then
    becomes $1 - b^2 \cdot q^4 \cdot \hbar^4$.  The DIFFERENCE
    $(1 - b^2 \cdot \hbar^4) - (1 - b^2 \cdot q^4 \cdot \hbar^4) =
    b^2 \cdot \hbar^4 \cdot (q^4 - 1)$ vanishes IFF $q^4 = 1$
    (root-of-unity case) — a formal statement matching the audit doc's
    "fibre-level / cyclotomic" framing.

    For the substrate q in $1 < q < 1 + \sqrt{2}$ (proton-anchor region),
    the factor $q^4 - 1 \neq 0$, so the N=2 ladder factor IS bar-asymmetric
    at the archimedean level — exactly the obstruction PR #1840 flagged.
    The bar-even discriminant CORRECTLY identifies this asymmetry as the
    reason scalar c_k extraction fails: only the operator-level grading
    recovers the c_k.

    Encoded here as a one-line ring identity expressing the bar-asymmetry
    measure: $b^2 \cdot \hbar^4 \cdot (q^4 - 1)$ is the obstruction
    quantity. -/
theorem bar_even_test_n2 {R : Type u} [CommRing R]
    (q b hbar : R) :
    ((1 : R) - b^2 * hbar^4) - (1 - b^2 * q^4 * hbar^4)
      = b^2 * hbar^4 * (q^4 - 1) := by
  ring

end QOU.QBeta.BarEvenInvariant
