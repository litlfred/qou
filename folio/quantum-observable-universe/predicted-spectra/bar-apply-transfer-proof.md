*Proof.*
(1) Assume $\forall q > a,\, P(q)$. Let $q < a^{-1}$ with $q > 0$. Then $q^{-1} > a$, so $P(q^{-1})$ holds, which implies $P(q)$ by bar-invariance. The reverse implication is dual. 
(3) Negate (1). 
(2) This is false in general. For example, $P(q) = \mathbf{1}_{q \in (a, a^{-1})}$ is bar-invariant on $(a, a^{-1})$ but false outside. Under continuity, every limit point of $\{q : P(q)\}$ is bar-conjugate to a limit point of $\neg P$, forcing the symmetric extension. $\square$

The bar-transfer principle establishes that a one-sided aether bound for a bar-invariant property yields the bar-conjugate bound. Once

$$
  q_0 > 1/\varphi^2 \quad\Rightarrow\quad
  \mathcal{E}_{q_0}\text{ is non-degenerate}
$$

is established, bar-applying yields

$$
  q_0 < \varphi^2 \quad\Rightarrow\quad
  \mathcal{E}_{1/q_0}\text{ is non-degenerate}
$$

The property holds on the super-classical wing $(1, \varphi^2)$ exactly as established on the sub-classical wing $(1/\varphi^2, 1)$. Both derivations fold into a single statement on the bar-self-dual band $\mathcal{B} = (1/\varphi^2, \varphi^2)$.

Every two-sided stability statement of the form

$$
  q \in (a, a^{-1}) \Longleftrightarrow \text{stable}
$$

with a bar-invariant stability condition requires proving only one inequality. The companion inequality is automatic. This principle applies to the following eligible bar-invariant predicates:
- $\Delta(\mathcal{E}_q) < 0$ (single real component), via bar T-duality.
- Slater-strict feasibility of the confinement SDP formulated $\iota$-equivariantly in $q$.
- Markov-trace positivity on the Hecke algebra ($\sigma_i \leftrightarrow \sigma_i^{-1}$).
- $j$-invariant finiteness of the Descartes elliptic curve.
