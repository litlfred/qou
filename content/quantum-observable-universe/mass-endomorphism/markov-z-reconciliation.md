Two conventions for the Markov parameter $z$ appear in the literature and in this paper. They differ by a factor of $q - 1$ and arise from different normalisation choices for the trace.

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
  \frac{1}{q^{1/2} + q^{-1/2}},
$$
giving $z_{\mathrm{m}} \approx 0.499$ at $q_0$.

**Relation.** The two parameters satisfy
$$
  z_{\mathrm{J}}
  \;=\;
  (q - 1)\,z_{\mathrm{m}}^{\,2},
$$
since $z_{\mathrm{m}}^2 = 1/(q^{1/2}+q^{-1/2})^2$ by definition. Equivalently, $z_{\mathrm{m}} = z_{\mathrm{J}}^{1/2}\,(q - 1)^{-1/2}$.

**Origin of the two conventions.** Convention 1 normalises the Jones polynomial as a link invariant: the factor $(q-1)$ absorbs the writhe correction and makes $J_L(q)$ independent of the braid representative. Convention 2 is the trace evaluated on a single generator without the writhe prefactor: $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{m}}$.

**The negative-crossing loop value.** The stabilisation rule is one-sided. For the canonical trace with $\mathrm{tr}_M(x\,\sigma_n) = z_{\mathrm{m}}\,\mathrm{tr}_M(x)$, the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ forces
$$
  \mathrm{tr}_M(x\,\sigma_n^{-1})
  \;=\;
  z_{-}\,\mathrm{tr}_M(x),
  \qquad
  z_{-} \;=\; z_{\mathrm{m}} - (q - q^{-1})
  \;\approx\; 0.290
$$
at $q_0$ ([Markov axioms](#rem:markov-axioms-primitive)). This is the value the pyhecke normal-form reduction computes for $\mathrm{tr}_M(\sigma_i^{-1})$; it is neither $z_{\mathrm{m}}$ nor $z_{\mathrm{m}}^{-1}$.

**Block weights.** The two loop values jointly determine the Wedderburn block weights of the convention-C trace in closed form:

$$
  w_\lambda
  \;=\;
  \mathrm{tr}_M(p_\lambda)
  \;=\;
  \prod_{x \in \lambda}
  \frac{z_{\mathrm{m}}\,q^{c(x)} - z_{-}\,q^{-c(x)}}{q^{h(x)} - q^{-h(x)}},
$$

with $c(x)$ the content and $h(x)$ the hook length of the cell $x$ — the Ocneanu weight formula at framing ratio $a^2 = z_{\mathrm{m}}/z_{-}$, verified exactly for every $\lambda \vdash n \leq 5$ ([witness](computations/markov-trace-weights-wenzl.witness.json)). The single-cell case recovers $\mathrm{tr}_M(1) = (z_{\mathrm{m}} - z_{-})/(q - q^{-1}) = 1$.

**Convention.** The parameter $z_{\mathrm{m}} = 1/(q^{1/2} + q^{-1/2}) = \sqrt{q}/(1+q)$ is **convention C** of the [trace-convention registry](docs/coordination/trace-convention-registry.md), there named the full-Hecke Ocneanu/Wenzl $z$-trace. The **mass** and **binding** channels are registered as **convention D**, $z_{\mathrm{D}} = q^3/(q^2+1)$, in both their definitional and production layers, following the owner ruling of 2026-08-09 that excised convention C for those channels. The two differ by $195.8$ ppm on $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ and $-197$ ppm on $\mathfrak{m}_{\mathfrak{p}}$. The numerical values quoted above ($z_{\mathrm{m}} \approx 0.499$, $z_{-} \approx 0.290$) and the weights evaluated at them are therefore **convention-C values**, and do not describe the parameter the mass tables use.

The weight formula itself is **frame-general** — it is the Ocneanu weight at framing ratio $a^2 = z/z_{-}$ for whatever admissible pair $(z, z_{-})$ is supplied, with $z_{-} = z - (q - q^{-1})$. Fed $z_{\mathrm{D}}$ it reproduces the registered convention-D weights exactly, $w_{(3)} = [4]_q/[2]_q^3$, $w_{(2,1)} = 1/[2]_q^2$ and $w_{(1^3)} = 0$; and the normalisation $\sum_{\lambda} (\dim V_\lambda)\, w_\lambda = 1$ holds identically under both conventions.
