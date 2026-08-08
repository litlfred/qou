Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property, for $x \in H_n(\mathbb{C}, q)$:
$$
  \mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x), \qquad
  z = \frac{1}{q^{1/2} + q^{-1/2}} = \mathrm{tr}_M(\sigma_i)
$$
the Markov-trace loop value.

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is a non-zero scalar multiple of the character $\chi_\lambda$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes, up to framing, the link invariant of the closure $\hat{\beta}$ attached to the member of the Ocneanu family selected by $z$.

That invariant is the Jones polynomial for one member only: the one whose three-row weight vanishes, $y_{(1^3)} = 0$, equivalently $z = q^3/(q^2+1)$ — convention D of the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md), the trace carried by the two-dimensional $\mathrm{SU}_q(2)$ fibre. The value stipulated in axiom 3 above is the full-Hecke member, convention C, for which $y_{(1^3)}(q) \neq 0$ whenever $q \neq 1$; the two functionals differ on explicit braids, so the name of the theorem does not identify which one is meant. Every $\mathrm{tr}_M$ value quoted below $0.1\%$ precision must therefore name its convention.
