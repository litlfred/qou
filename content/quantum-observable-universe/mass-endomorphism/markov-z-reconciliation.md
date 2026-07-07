Two conventions for the Markov parameter $z$ appear in the literature and in this paper. They differ by a factor of $q - 1$ and arise from different normalisation choices for the trace.

**Convention 1 (Jones, 1987).** The Jones–Markov trace ([Jones–Markov trace](#thm:jones-markov-trace)) satisfies $\mathrm{tr}_M(x\,\sigma_n^{\pm 1}) = z_{\mathrm{J}}^{\pm 1}\,\mathrm{tr}_M(x)$ with
$$
  z_{\mathrm{J}}
  \;=\;
  \frac{q - 1}{(q^{1/2} + q^{-1/2})^2}.
$$
At $q_0 \approx 1.110$, this gives $z_{\mathrm{J}} \approx 0.027$. This parameter makes the trace a link invariant via the Markov closure $\hat{\beta}$.

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

**Origin of the two conventions.** Convention 1 normalises the Jones polynomial as a link invariant. The factor $(q-1)$ absorbs the writhe correction and makes $J_L(q)$ independent of the braid representative. Convention 2 arises when we evaluate the trace on a single generator $\sigma_i$ without the writhe prefactor. We have $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{m}}$ in Convention 2, whereas $\mathrm{tr}_M(\sigma_i) = z_{\mathrm{J}}$ in Convention 1.

All mass tables, vertex volumes, and nuclear binding computations in this paper use $z = z_{\mathrm{m}} = 1/(q^{1/2} + q^{-1/2})$. The Jones–Markov trace theorem statement retains $z_{\mathrm{J}}$ to match the original reference.
