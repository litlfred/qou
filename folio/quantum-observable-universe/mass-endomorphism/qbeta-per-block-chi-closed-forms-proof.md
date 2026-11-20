# Proof of per-block character closed forms

Each closed form is a rational expression in $q$. The vanishing at $q = 1$ follows directly from the $(q^2 - 1)$ factor present in all three forms. The antipode pairing reduces to the rational identity $-(q^2-1)(q^2+1)^2/(4q^5) = q^{-4} [-(q^2-1)(q^2+1)^2/(4q)]$, which simplifies to $1/q^5 = q^{-4} (1/q)$. All three parts are identities of rational functions on $q > 0$, where every denominator is nonzero. $\square$

## Scope and structural insight

This proposition establishes the exact rational, pre-archimedean source data for the Q$_\beta$ precision-ladder derivation. All three blocks share a $(q^2 - 1)$ factor, forcing each to contribute at order $w$ or higher in the Taylor expansion around $q = 1$ (where $w = q - 1$).

The leading-order coefficients at $O(w)$ are $-2$ for the $(3)$ block, $-1$ for the $(2,1)$ block, and $-2$ for the $(1,1,1)$ block. The shared $-2$ between the $(3)$ and $(1,1,1)$ blocks is the algebraic signature of the antipode pairing. Under $q \mapsto 1/q$, the order-$w$ expansion preserves the leading coefficient up to the $q^{-4}$ framing weight.

## Extensions

The following extensions build the structural infrastructure for any future $\Delta\mathrm{tr}_M$ closure attack.

**Extension 1: Surrogate closed form.** We define the non-canonical rational surrogate weights $y_\lambda^{\text{surr}}(q)$ matching the per-block dimension structure $\{q^2, q, 1\}/((1+q)(1+q+q^2))$. The resulting trace difference closed form is:

$$
  \Delta\mathrm{tr}_M^{\text{surr}}(q) =
  \frac{-q^{11}+q^{10}-2q^9+q^8+q^6-q^5-q^3+2q^2-q+1}{4q^5(q^2+q+1)}.
$$

This identity is an equality of rational functions. This surrogate is not the canonical Markov trace: its weights are chosen for the identity, not derived from the Markov parameter (see Extension 4).

**Extension 2: Taylor coefficients at $q = 1$.** The order-0 coefficient vanishes ($\Delta\mathrm{tr}_M^{\text{surr}}(1) = 0$). The order-1 coefficient is the derivative $D \Delta\mathrm{tr}_M^{\text{surr}}(1) = -5/6$, obtained by the quotient rule ($N'(1) = -10, D(1) = 12, N(1) = 0 \Rightarrow -10/12$). Higher orders ($5/6, -41/9, \dots$) require bulky $n$-th derivative computations and are obtained by computation rather than by a proved derivative identity.

**Extension 3.** The invariant that $\Delta\mathrm{tr}_M$ lacks $\sqrt q$ terms holds automatically here: once $\Delta\mathrm{tr}_M^{\text{surr}} : \mathbb{R} \to \mathbb{R}$ is built from polynomial inputs, it is rational by construction.

**Extension 4: Canonical trace (conditional class and its canonical instance).** The Wenzl–Markov weights are taken as a hypothesis, subject to the single dimension-normalisation condition $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$. The canonical trace difference is defined conditionally on these weights, and its vanishing at $q = 1$ reduces to the vanishing of the block characters at $q = 1$. The hypothesis is satisfied by the convention-D weights, at the Markov parameter $z = q^3/(q^2+1)$:

$$
y_{(3)}(q) = \frac{q^4+1}{(q^2+1)^2}, \qquad y_{(2,1)}(q) = \frac{q^2}{(q^2+1)^2}, \qquad y_{(1^3)}(q) = 0.
$$

These weights are rational in $q$, so no $\sqrt q$ appears. The normalisation is the identity $(q^4+1) + 2q^2 = (q^2+1)^2$. These weights are exactly the solved Markov weights at $z_D$. The earlier archimedean parameter $z(q) = \sqrt q/(1+q) = 1/(\sqrt q + 1/\sqrt q)$ is the convention-C value; it is retained only as a historical identity and does not enter the canonical weights.

**Extension 5: $z$-recursion class.** Consider the three-term recursion $4(n+1)a_{n+1} + 6na_n + (2n-1)a_{n-1} = 0$ on the Taylor coefficients of $z(q)$ at $q = 1$, with seeds $a_0 = 1/2$ and $a_1 = 0$. Strong induction with a linear-solve step proves that its solution is unique. This auxiliary recursion supports the general $c_k$ ladder recursion ([$c_k$ precision-ladder recursion induced by the fibre-level Habiro $q$-difference equation](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).
