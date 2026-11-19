# Proof of per-block character closed forms

Each closed form is a rational expression in $q$. The vanishing at $q = 1$ follows directly from the $(q^2 - 1)$ factor present in all three forms. The antipode pairing reduces to the rational identity $-(q^2-1)(q^2+1)^2/(4q^5) = q^{-4} [-(q^2-1)(q^2+1)^2/(4q)]$, which simplifies to $1/q^5 = q^{-4} (1/q)$ for $q > 0$. $\square$

## Scope and structural insight

This proposition establishes the exact rational, pre-archimedean source data for the Q$_\beta$ precision-ladder derivation. All three blocks share a $(q^2 - 1)$ factor, forcing each to contribute at order $w$ or higher in the Taylor expansion around $q = 1$ (where $w = q - 1$).

The leading-order coefficients at $O(w)$ are $-2$ for the $(3)$ block, $-1$ for the $(2,1)$ block, and $-2$ for the $(1,1,1)$ block. The shared $-2$ between the $(3)$ and $(1,1,1)$ blocks is the algebraic signature of the antipode pairing. Under $q \mapsto 1/q$, the order-$w$ expansion preserves the leading coefficient up to the $q^{-4}$ framing weight.

## Companion identities and extensions

The per-block closed forms support five structural extensions for the $\Delta\mathrm{tr}_M$ analysis.

**Extension 1: Surrogate closed form.** Non-canonical rational surrogate weights $y_\lambda^{\text{surr}}(q)$ matching the per-block dimension structure $\{q^2, q, 1\}/((1+q)(1+q+q^2))$ yield the trace-difference closed form:

$$
  \Delta\mathrm{tr}_M^{\text{surr}}(q) =
  \frac{-q^{11}+q^{10}-2q^9+q^8+q^6-q^5-q^3+2q^2-q+1}{4q^5(q^2+q+1)}.
$$

This identity holds by rational simplification. The surrogate is not the canonical Markov trace: its weights are chosen for the rational dimension identity, not derived from the Markov parameter (see Extension 4).

**Extension 2: Taylor coefficients at $q = 1$.** The order-0 coefficient vanishes ($\Delta\mathrm{tr}_M^{\text{surr}}(1) = 0$), and the order-1 derivative at $q = 1$ equals $D \Delta\mathrm{tr}_M^{\text{surr}}(1) = -5/6$, obtained by explicit quotient-rule differentiation ($N'(1) = -10, D(1) = 12, N(1) = 0 \Rightarrow -10/12$). Higher orders ($5/6, -41/9, \dots$) follow from higher-order derivative towers and are catalogued separately.

**Extension 3: Rationality.** Because $\Delta\mathrm{tr}_M^{\text{surr}}$ is constructed from polynomial numerators and denominators in $q$, it is manifestly rational in $q$ and free of $\sqrt q$ radicals.

**Extension 4: Canonical trace weights.** The Wenzl–Markov weights satisfy the single dimension-normalisation relation $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$. Under this relation, the vanishing of $\Delta\mathrm{tr}_M^{\text{can}}(1)$ reduces directly to the classical-point vanishing of the three per-block characters. The convention-D weights at the Markov parameter $z = q^3/(q^2+1)$ are:

$$
y_{(3)}(q) = \frac{q^4+1}{(q^2+1)^2}, \qquad y_{(2,1)}(q) = \frac{q^2}{(q^2+1)^2}, \qquad y_{(1^3)}(q) = 0.
$$

These weights are rational in $q$, so no $\sqrt q$ appears, and their normalisation reduces to the polynomial identity $(q^4+1) + 2q^2 = (q^2+1)^2$. By contrast, the parameter $z_{\mathrm{C}}(q) = \sqrt q/(1+q) = 1/(\sqrt q + 1/\sqrt q)$ belongs to the excised convention C and does not enter the canonical convention-D trace.

**Extension 5: $z$-recursion.** The three-term recursion $4(n+1)a_{n+1} + 6na_n + (2n-1)a_{n-1} = 0$ on the Taylor coefficients of $z_{\mathrm{C}}(q)$ at $q = 1$, with seeds $a_0 = 1/2$ and $a_1 = 0$, uniquely determines all higher coefficients $a_n$ by strong induction. This auxiliary recursion supports the general $c_k$ ladder recursion ([Habiro $q$-difference recursion for $c_k$](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).
