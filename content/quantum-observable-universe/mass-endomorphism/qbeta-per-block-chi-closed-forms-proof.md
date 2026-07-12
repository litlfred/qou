# Proof of per-block character closed forms

Each closed form is a rational expression in $q$. The vanishing at $q = 1$ follows directly from the $(q^2 - 1)$ factor present in all three forms. The antipode pairing reduces to the rational identity $-(q^2-1)(q^2+1)^2/(4q^5) = q^{-4} [-(q^2-1)(q^2+1)^2/(4q)]$, which simplifies to $1/q^5 = q^{-4} (1/q)$. The Lean proof discharges all three parts via `field_simp; ring` after providing positivity witnesses for the denominators ($q > 0$). $\square$

## Scope and structural insight

This proposition establishes the exact rational, pre-archimedean source data for the Q$_\beta$ precision-ladder derivation. All three blocks share a $(q^2 - 1)$ factor, forcing each to contribute at order $w$ or higher in the Taylor expansion around $q = 1$ (where $w = q - 1$).

The leading-order coefficients at $O(w)$ are $-2$ for the $(3)$ block, $-1$ for the $(2,1)$ block, and $-2$ for the $(1,1,1)$ block. The shared $-2$ between the $(3)$ and $(1,1,1)$ blocks is the algebraic signature of the antipode pairing. Under $q \mapsto 1/q$, the order-$w$ expansion preserves the leading coefficient up to the $q^{-4}$ framing weight.

## Lean extensions

The accompanying Lean file builds the structural infrastructure for any future $\Delta\mathrm{tr}_M$ closure attack.

**Extension 1: Surrogate closed form.** We define the non-canonical rational surrogate weights $y_\lambda^{\text{surr}}(q)$ matching the per-block dimension structure $\{q^2, q, 1\}/((1+q)(1+q+q^2))$. The resulting trace difference closed form is:

$$
  \Delta\mathrm{tr}_M^{\text{surr}}(q) =
  \frac{-q^{11}+q^{10}-2q^9+q^8+q^6-q^5-q^3+2q^2-q+1}{4q^5(q^2+q+1)}.
$$

The theorem `delta_tau_M_surrogate_eq_sum` discharges this identity sorry-free via `field_simp; ring`. This surrogate is not the canonical Markov trace, as canonical weights require $\sqrt q$.

**Extension 2: Taylor coefficients at $q = 1$.** We lock the order-0 coefficient as a sorry-free vanishing theorem ($\Delta\mathrm{tr}_M^{\text{surr}}(1) = 0$). We establish the order-1 coefficient via a sorry-free `HasDerivAt` theorem ($D \Delta\mathrm{tr}_M^{\text{surr}}(1) = -5/6$), proven by explicit quotient-rule chaining ($N'(1) = -10, D(1) = 12, N(1) = 0 \Rightarrow -10/12$). Higher orders ($5/6, -41/9, \dots$) require bulky $n$-th derivative computations and are recorded via witness JSON.

**Extension 3.** The invariant that $\Delta\mathrm{tr}_M$ lacks $\sqrt q$ atoms is vacuous at the Lean type level. Once $\Delta\mathrm{tr}_M^{\text{surr}} : \mathbb{R} \to \mathbb{R}$ is built from polynomial inputs, Lean's type system enforces rationality by construction.

**Extension 4: Canonical $\sqrt q$-bearing trace (conditional class).** We define the archimedean Markov parameter $z(q) = \sqrt q / (1+q)$ and prove the symmetric identity $z(q) = 1 / (\sqrt q + 1/\sqrt q)$ sorry-free via `Real.mul_self_sqrt`. We axiomatise the canonical Wenzl–Markov weights via `class CanonicalMarkovWeightsH3` using a single dimension-normalisation axiom. A conditional `def delta_tau_M_canonical` consumes the class. The conditional vanishing theorem `delta_tau_M_canonical_vanish_at_one` is sorry-free, reducing to `chi_blocks_vanish_at_one`.

**Extension 5: $z$-recursion class.** We axiomatise the three-term recursion $4(n+1)a_{n+1} + 6na_n + (2n-1)a_{n-1} = 0$ on the Taylor coefficients of $z(q)$ at $q = 1$, with seeds $a_0 = 1/2$ and $a_1 = 0$. The `ZRecursionCoeffs.unique` theorem uses strong induction with a linear-solve step to prove uniqueness sorry-free. This auxiliary recursion supports the general $c_k$ ladder recursion ([`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).

## Theorem status

All theorems are sorry-free and locally verified. The three originally deferred sorries (derivative at $q=1$, Markov-parameter symmetric form, and $z$-recursion uniqueness) were discharged during local Lean verification.
