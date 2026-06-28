Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = 1/(q^{1/2} + q^{-1/2})$ ([Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).
## Operator interpretation

The value $z^2$ is the **Jones polynomial of the Hopf link**
(unknotted two-component linking) evaluated at the substrate
parameter:
$J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
= -(q + q^{-1})/(q^{1/2} + q^{-1/2})$. Multiplying by the
Markov normalization recovers the pair contribution to the
categorical mass — the pair blow-up centre at coordinate
$\hat V_i\hat V_j$ carries the same weight $z^2$ regardless
of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$
(cf. `adjacent-vs-full-probe.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)).
