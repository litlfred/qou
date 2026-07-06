For an atomic closed braid the Habiro expansion of the Markov trace
([Habiro completion](#prop:full-pole-structure-mass-trace))
**terminates**: only finitely many cyclotomic coefficients $a_m$
are nonzero. This corollary records the explicit termination bound
and integrality, with a constructive proof by sequential cyclotomic
division.

**Corollary.**
*Let $T_w(Z, N) \in H_{3A}(q)$ be the atomic-braid image for
$A = Z + N$ nucleons
([categorical mass, Markov](#prop:categorical-mass-markov)), and
let $u = q^{1/2}$. Then there exists a denominator $D(u)$ — a
finite product of cyclotomic polynomials — and a Laurent
polynomial $p(u) := D(u) \cdot \mathrm{tr}_M(T_w(Z, N), u^2) \in \mathbb{Z}[u, u^{-1}]$
admitting the finite Habiro expansion*

$$
  p(u) \;=\; \sum_{m=0}^{m_{\max}} a_m(u)\,(u; u)_m,
  \qquad (u; u)_m = \prod_{k=1}^{m}(1 - u^k),
$$

*with*

1. **Integrality.** *$a_m(u) \in \mathbb{Z}[u]$ for every $m$.*
2. **Degree bound.** *$\deg_u a_m(u) \leq m$.*
3. **Termination.** *$a_m = 0$ for $m > m_{\max}$, and
   $m_{\max} \leq \lceil \sqrt{2 \deg_u p(u)} \rceil$.*
4. **Uniqueness.** *Given $\deg a_m \leq m$, the sequence
   $\{a_m\}$ is uniquely determined by $p$.*
