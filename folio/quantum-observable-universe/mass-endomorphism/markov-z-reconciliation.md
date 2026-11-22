Two conventions for the Markov parameter $z$ appear in the literature and in this paper. They arise from different normalisation choices for the trace.

**Convention 1 (Jones link normalisation).** Producing a link invariant from the trace requires a writhe-dependent prefactor outside the trace ([Jones–Markov trace](#thm:jones-markov-trace)); the normalisation parameter absorbed into that prefactor is
$$
  z_{\mathrm{J}}
  \;=\;
  \frac{q - 1}{(q^{1/2} + q^{-1/2})^2}.
$$
At $q_0 \approx 1.110$, this gives $z_{\mathrm{J}} \approx 0.027$. The trace itself does **not** satisfy a two-sided rule $\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = c^{\pm 1}\,\mathrm{tr}_M(x)$ for any parameter $c$: the Hecke quadratic relation forces the negative stabilisation to the affine value $z_{-} = z_{\mathrm{m}} - (q - q^{-1})$ (see below), and requiring $c\,\bigl(c - (q - q^{-1})\bigr) = 1$ forces $c \in \{q, -q^{-1}\}$, the two degenerate one-dimensional characters.

**Convention 2 (mass computations).** The categorical mass formula ([categorical mass as Markov trace](#prop:categorical-mass-markov)) and all subsequent mass and volume computations use
$$
  z_{\mathrm{m}}
  \;=\;
  \frac{q^3}{q^2+1},
$$
giving $z_{\mathrm{m}} \approx 0.6127$ at the proton-pinned $q_0$. This is convention D of the trace-convention registry, replacing the excised convention-C parameter $z_{\mathrm{C}} = 1/(q^{1/2} + q^{-1/2}) \approx 0.499$ across all mass and binding channels; $z_{\mathrm{C}}$ is retained below solely for explicit comparison.

**Relation.** The Jones normalisation is tied to the convention-C parameter, not to $z_{\mathrm{m}}$:
$$
  z_{\mathrm{J}}
  \;=\;
  (q - 1)\,z_{\mathrm{C}}^{\,2},
$$
since $z_{\mathrm{C}}^2 = 1/(q^{1/2}+q^{-1/2})^2$ by definition. Equivalently, $z_{\mathrm{C}} = z_{\mathrm{J}}^{1/2}\,(q - 1)^{-1/2}$.

**Origin of the two conventions.** Convention 1 normalises the Jones polynomial as a link invariant: the factor $(q-1)$ absorbs the writhe correction and makes $J_L(q)$ independent of the braid representative. Convention 2 is the trace evaluated on a single generator without the writhe prefactor: $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{m}}$.

**The negative-crossing loop value.** The stabilisation rule is one-sided. For the canonical trace with $\mathrm{tr}_M(x\,\sigma_n) = z_{\mathrm{m}}\,\mathrm{tr}_M(x)$, the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ forces
$$
  \mathrm{tr}_M(x\,\sigma_n^{-1})
  \;=\;
  z_{-}\,\mathrm{tr}_M(x),
  \qquad
  z_{-} \;=\; z_{\mathrm{m}} - (q - q^{-1})
  \;=\; \frac{1}{q(q^2+1)}
  \;\approx\; 0.4036
$$
at $q_0$ ($0.290$ under the excised convention C) ([Markov axioms](#rem:markov-axioms-primitive)). This is the value the pyhecke normal-form reduction computes for $\mathrm{tr}_M(\sigma_i^{-1})$; it is neither $z_{\mathrm{m}}$ nor $z_{\mathrm{m}}^{-1}$.

**Block weights.** The two loop values jointly determine the Wedderburn block weights of the trace in closed form:

$$
  w_\lambda
  \;=\;
  \mathrm{tr}_M(p_\lambda)
  \;=\;
  \prod_{x \in \lambda}
  \frac{z_{\mathrm{m}}\,q^{c(x)} - z_{-}\,q^{-c(x)}}{q^{h(x)} - q^{-h(x)}},
$$

with $c(x)$ the content and $h(x)$ the hook length of the cell $x$ — the Ocneanu weight formula at framing ratio $a^2 = z_{\mathrm{m}}/z_{-}$, verified exactly for every $\lambda \vdash n \leq 5$ ([witness](../../../computations/markov-trace-weights-wenzl.witness.json)). The single-cell case recovers $\mathrm{tr}_M(1) = (z_{\mathrm{m}} - z_{-})/(q - q^{-1}) = 1$.

**Convention.** The parameter $z_{\mathrm{m}} = q^3/(q^2+1)$ is **convention D** of the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md), registered for the **mass** and **binding** channels in both their definitional and production layers, whereas convention C ($z_{\mathrm{C}} = \sqrt{q}/(1+q)$, the full-Hecke Ocneanu/Wenzl $z$-trace) is excised for those channels. The two differ by $195.8$ ppm on $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ and $-197$ ppm on $\mathfrak{m}_{\mathfrak{p}}$.

**A structural separation between the two conventions.** The justification on record for the convention-D ruling is empirical — the $195.8$ ppm and $-197$ ppm figures above. There is also a structural one, and it involves no anchor, no measurement and no ppm figure. Using $\hbar_\times = q - q^{-1}$ and $[2]_q^2 - \hbar_\times^2 = 4$, the two loop values of convention D satisfy

$$
  z_{-} \;=\; \frac{1}{q(q^2+1)} , \qquad
  z\,z_{-} \;=\; \frac{1}{[2]_q^{2}} , \qquad
  a^2 \;=\; \frac{z}{z_{-}} \;=\; q^4 .
$$

So in convention D the two crossing loop values multiply to the inverse square of the quantum dimension, and the Ocneanu framing parameter is the **monomial** $a = q^2$. Note also $z\,z_{-} = w_{(2,1)}$: the product of the loop values is exactly the registered standard-block weight.

Convention C satisfies neither. There

$$
  z_{-} \;=\; \frac{q^{3/2} - q^3 - q^2 + q + 1}{q(q+1)} , \qquad
  a^2 \;=\; \frac{q^{3/2}}{q^{3/2} - q^3 - q^2 + q + 1} ,
$$

mixing half-integer and integer powers of $q$ in one numerator, with no factorisation and no monomial framing ratio. Both conventions are admissible — $\mathrm{tr}_M(1) = (z - z_{-})/(q - q^{-1}) = 1$ holds in each — so this is not convention C being invalid; it is convention C being structureless.

Two further forms, recorded because they make the pair comparable at a glance. Convention D admits the exact analogue of the $z_{\mathrm{C}} = 1/[2]_{\sqrt q}$ above,

$$
  z_{\mathrm{D}} \;=\; \frac{q^2}{[2]_q} ,
$$

and the two are bridged by $z_{\mathrm{D}}(q) = q^2\,z_{\mathrm{C}}(q^2)$.

All of the above is proved, and independently confirmed by exact symbolic computation. It was found while chasing the algebraic relation between $z$ and $\hbar_\times$ out of the Toffoli LP arc, where it first appeared only as an obstruction.

**The framing ratio classifies the convention: D is the $\mathfrak{sl}_2$ point.** The monomial above is doing real work in the weight formula below. When $a = q^N$ — that is, $z = q^{2N}z_-$ — every numerator of that product collapses,

$$
  z\,q^{c} - z_{-}q^{-c} \;=\; z_{-}\bigl(q^{2N+c} - q^{-c}\bigr) \;=\; z_{-}q^{N}\bigl(q^{N+c} - q^{-(N+c)}\bigr),
$$

so with $z_{-}q^{N} = 1/[N]_q$ the whole product becomes the hook-content formula for the $U_q(\mathfrak{sl}_N)$ quantum dimension:

$$
  w_\lambda \;=\; \frac{\dim_q\bigl(V_\lambda^{\mathfrak{sl}_N}\bigr)}{[N]_q^{\,n}} .
$$

Solving $a = q^N$ for $z$ gives a one-parameter family $z_N = q^N/[N]_q$, and $z_2 = q^3/(q^2+1)$ is convention D on the nose. Verified for $N = 1,2,3,4$ and every partition of $n \leq 5$: the framing ratio is $q^{2N}$, the weights are $\dim_q/[N]_q^{\,n}$, and $w_\lambda = 0$ exactly when $\lambda$ has more than $N$ rows.

Two consequences. First, the registered $w_{(3)} = [4]_q/[2]_q^3$ and $w_{(2,1)} = 1/[2]_q^2$ are the quantum dimensions of the $4$- and $2$-dimensional $U_q(\mathfrak{sl}_2)$ irreps over $[2]_q^3$. Second, the exact vanishing $w_{(1^3)} = 0$ is the $\mathfrak{sl}_2$ **row bound**, not a coincidence of the trace: a partition with more than $N$ rows has a cell of content $-N$, whose numerator factor carries $[0]_q = 0$.

**Convention C lies in no member of the family, for any $N$** — not merely for no integer $N$. Its framing ratio has logarithmic derivative $q\,(a^2)'/a^2 = -(3s^6+s^4+s^2+3)/\bigl(2(s^6+s^4-s^3-s^2-1)\bigr)$ with $s = \sqrt q$, which is not constant; $a^2 = q^t$ would force it to equal the constant $t$. Consistently, C's weights vanish on no partition at all — checked at $(1^3)$, $(2,1,1)$ and $(1^4)$ — so C has no row bound.

So the convention-D ruling has a classification behind it, not only the empirical figures above: D is the $\mathfrak{sl}_2$ point of the Ocneanu family, C is off the family entirely, and no anchor or measurement enters the argument.

> **Notation warning.** The $w_\lambda$ of this block is the **Ocneanu/Markov** weight — the $y_\lambda$ of the production trace. It is *not* the $w_\lambda(q) = \dim_q(\lambda)^2/[n]_q!$ of the [canonical $q$-deformed Wedderburn-block weight](../mass-theory/wedderburn-weight-canonical.md), which is built from the Frame–Robinson–Thrall hook-*length* dimension rather than the hook-*content* one. At $n = 3$ the two differ on every partition and differ already at $q = 1$ — $(1/6, 2/3, 1/6)$ against $(1/2, 1/4, 0)$ — so the notation register's rule that the partition-weight families are distinct at $q \neq 1$ applies here at $q = 1$ as well.

This classification is proved. It is also proved independently that D is Wenzl level $r = 2$, and that the $z_D$ row cap follows from the general-$n$ cell product.

The weight formula itself is **frame-general** — it is the Ocneanu weight at framing ratio $a^2 = z/z_{-}$ for whatever admissible pair $(z, z_{-})$ is supplied, with $z_{-} = z - (q - q^{-1})$. Fed $z_{\mathrm{D}}$ it reproduces the registered convention-D weights exactly, $w_{(3)} = [4]_q/[2]_q^3$, $w_{(2,1)} = 1/[2]_q^2$ and $w_{(1^3)} = 0$; and the normalisation $\sum_{\lambda} (\dim V_\lambda)\, w_\lambda = 1$ holds identically under both conventions.
