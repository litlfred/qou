Two conventions for the Markov parameter $z$ appear in the literature and in this paper. They arise from different normalisation choices for the trace.

**Convention 1 (Jones link normalisation).** Producing a link invariant from the trace requires a writhe-dependent prefactor outside the trace ([Jones–Markov trace](#thm:jones-markov-trace)); the normalisation parameter absorbed into that prefactor is
$$
  z_{\mathrm{J}}
  \;=\;
  \frac{q - 1}{(q^{1/2} + q^{-1/2})^2}.
$$
At $q_0 \approx 1.110$, this gives $z_{\mathrm{J}} \approx 0.027$. The trace itself does **not** satisfy a two-sided rule $\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = c^{\pm 1}\,\mathrm{tr}_M(x)$ for any parameter $c$: the Hecke quadratic relation forces the negative stabilisation to the affine value $z_{-} = z_{\mathrm{m}} - (q - q^{-1})$ (see below), and requiring $c\,\bigl(c - (q - q^{-1})\bigr) = 1$ forces $c \in \{q, -q^{-1}\}$, the two degenerate one-dimensional characters.

**Convention 2 (Hecke tower Markov parameter).** The categorical mass formula ([categorical mass as Markov trace](#prop:categorical-mass-markov)) and all mass and binding evaluations use
$$
  z_{\mathrm{m}}
  \;=\;
  \frac{q^3}{q^2+1}
  \;=\;
  \frac{q^2}{[2]_q},
$$
giving $z_{\mathrm{m}} \approx 0.6127$ at the proton-anchored $q_0$.

**Relation to the half-argument loop reciprocal.** Writing $z_{1/2} := 1/(q^{1/2} + q^{-1/2}) = 1/[2]_{\sqrt q}$, the writhe-prefactor scalar $z_{\mathrm{J}}$ satisfies
$$
  z_{\mathrm{J}}
  \;=\;
  (q - 1)\,z_{1/2}^{\,2},
$$
whereas the Hecke Markov parameter satisfies $z_{\mathrm{m}}(q) = q^2\,z_{1/2}(q^2)$. Convention 1 normalises the Jones polynomial as a link invariant by absorbing the writhe correction into $(q-1)$; Convention 2 evaluates the trace directly on a single Hecke generator without a writhe prefactor, $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{m}}$.

**The negative-crossing loop value.** The stabilisation rule is one-sided. For $\mathrm{tr}_M(x\,\sigma_n) = z_{\mathrm{m}}\,\mathrm{tr}_M(x)$, the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ forces
$$
  \mathrm{tr}_M(x\,\sigma_n^{-1})
  \;=\;
  z_{-}\,\mathrm{tr}_M(x),
  \qquad
  z_{-} \;:=\; z_{\mathrm{m}} - (q - q^{-1})
  \;=\; \frac{1}{q(q^2+1)}
  \;\approx\; 0.4036
$$
at $q_0$ ([Markov axioms](#rem:markov-axioms-primitive)). This is the value that Hecke normal-form reduction yields for $\mathrm{tr}_M(\sigma_i^{-1})$; it is neither $z_{\mathrm{m}}$ nor $z_{\mathrm{m}}^{-1}$.

**Block weights.** For any stabilisation parameter $z$ with $z_- = z - (q - q^{-1})$, the Wedderburn block weights are given in closed form by the Ocneanu product

$$
  w_\lambda
  \;=\;
  \mathrm{tr}_M(p_\lambda)
  \;=\;
  \prod_{x \in \lambda}
  \frac{z\,q^{c(x)} - z_{-}\,q^{-c(x)}}{q^{h(x)} - q^{-h(x)}},
$$

with $c(x)$ the content and $h(x)$ the hook length of the cell $x$ — the Ocneanu weight formula at framing ratio $a^2 = z/z_{-}$, verified for every $\lambda \vdash n \leq 5$. The single-cell case recovers $\mathrm{tr}_M(1) = (z - z_{-})/(q - q^{-1}) = 1$.

**Monomial framing ratio and the $U_q(\mathfrak{sl}_N)$ Ocneanu family.** Using $\hbar_\times = q - q^{-1}$ and $[2]_q^2 - \hbar_\times^2 = 4$, the loop pair $(z_{\mathrm{m}}, z_-)$ at $z_{\mathrm{m}} = q^3/(q^2+1)$ satisfies

$$
  z_{-} \;=\; \frac{1}{q(q^2+1)} , \qquad
  z_{\mathrm{m}}\,z_{-} \;=\; \frac{1}{[2]_q^{2}} , \qquad
  a^2 \;=\; \frac{z_{\mathrm{m}}}{z_{-}} \;=\; q^4 .
$$

Thus the two crossing loop values multiply to the inverse square of the quantum dimension ($z_{\mathrm{m}}\,z_{-} = w_{(2,1)}$), and the Ocneanu framing parameter is the **monomial** $a = q^2$. When $a = q^N$ — that is, $z = q^{2N}z_-$ — every numerator of the Ocneanu product collapses,

$$
  z\,q^{c} - z_{-}q^{-c} \;=\; z_{-}\bigl(q^{2N+c} - q^{-c}\bigr) \;=\; z_{-}q^{N}\bigl(q^{N+c} - q^{-(N+c)}\bigr),
$$

so with $z_{-}q^{N} = 1/[N]_q$ the product reduces to the hook-content formula for the $U_q(\mathfrak{sl}_N)$ quantum dimension:

$$
  w_\lambda \;=\; \frac{\dim_q\bigl(V_\lambda^{\mathfrak{sl}_N}\bigr)}{[N]_q^{\,n}} .
$$

Solving $a = q^N$ for $z$ yields the one-parameter family $z_N = q^N/[N]_q$, whose $N = 2$ member is $z_2 = q^2/[2]_q = q^3/(q^2+1) = z_{\mathrm{m}}$ (Wenzl level $r = 2$). For every $N \in \mathbb{Z}_{\geq 1}$, the framing ratio is $q^{2N}$, the weights are $\dim_q/[N]_q^{\,n}$, and $w_\lambda = 0$ precisely when $\lambda$ has more than $N$ rows: a partition with more than $N$ rows contains a cell of content $-N$, whose numerator factor carries $[0]_q = 0$. In particular, at $N = 2$ one obtains $w_{(3)} = [4]_q/[2]_q^3$, $w_{(2,1)} = 1/[2]_q^2$, and the exact $\mathfrak{sl}_2$ row bound $w_{(1^3)} = 0$.

By contrast, setting $z = z_{1/2} = 1/(q^{1/2}+q^{-1/2})$ gives $z_- = (q^{3/2} - q^3 - q^2 + q + 1)/\bigl(q(q+1)\bigr)$ and a non-monomial framing ratio $a^2$ whose logarithmic derivative $q\,(a^2)'/a^2 = -(3s^6+s^4+s^2+3)/\bigl(2(s^6+s^4-s^3-s^2-1)\bigr)$ ($s = \sqrt q$) is non-constant, so $z_{1/2}$ belongs to $z_N$ for no value of $N$ and imposes no row bound.

> **Notation warning.** The $w_\lambda$ of this block is the **Ocneanu/Markov** weight $y_\lambda$. It is *not* the $w_\lambda(q) = \dim_q(\lambda)^2/[n]_q!$ of the [canonical $q$-deformed Wedderburn-block weight](../mass-theory/wedderburn-weight-canonical.md), which is built from the Frame–Robinson–Thrall hook-*length* dimension rather than the hook-*content* one. At $n = 3$ the two differ already at $q = 1$ — $(1/6, 2/3, 1/6)$ against $(1/2, 1/4, 0)$.

Fed $z_{\mathrm{m}} = q^3/(q^2+1)$, the general Ocneanu formula reproduces $w_{(3)} = [4]_q/[2]_q^3$, $w_{(2,1)} = 1/[2]_q^2$, and $w_{(1^3)} = 0$, with $\sum_{\lambda} (\dim V_\lambda)\, w_\lambda = 1$ holding identically.
