**Exact-arithmetic lemma**: the leading $\varepsilon^6$ coefficient of $(F_3 - 1)$ at $q = 1 + \varepsilon$ equals $-2 \cdot b^3(q=1) = -3\sqrt{3}/4$.

## Statement

For the $F_3 = 1 - 2 b^3 \hbar_q^6$ factor in the [$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder) precision ladder, the leading $\varepsilon^6$ contribution of $(F_3 - 1)$ at $q = 1+\varepsilon$ is the exact algebraic value:

$$
\boxed{
  -2 \cdot b^3(q=1) \;=\; -2 \cdot \frac{3\sqrt{3}}{8} \;=\; -\frac{3\sqrt{3}}{4}
   \;\approx\; -1.29904 .
}
$$

This value is checked by exact symbolic computation and proved below.

## Proof

The Hoefsmit off-diagonal coupling is $b = \sqrt{q^4+q^2+1}/(q^2+1)$. At $q = 1$, $b^2 = 3/4$, hence $b = \sqrt{3}/2$. Thus $b^3 = 3\sqrt{3}/8$, and $-2 \cdot b^3 = -3\sqrt{3}/4$.

## Significance

This lemma is the purely-arithmetic component of the $c_3 = -2$ identification in [Categorical derivation of $c_3 = J_{\mathrm{Hopf}}(q=1) = -2$ via 3-fold Markov closure](#prop:q-beta-c3-hopf-three-fold-markov). The categorical content remains a hypothesis (the three-fold Markov Hopf extraction), but its arithmetic discharge at the $\varepsilon^6$ level is proved.

Combined with [Primitive Markov-trace axioms](#rem:markov-axioms-primitive), two previously assumed hypotheses are replaced by purely algebraic/arithmetic theorems. The substantive open content of the three-fold Markov Hopf extraction reduces to the categorical identification that the perturbative $\hbar_q^6$ piece of the $\mathrm{tr}_M$-expansion factors through Hopf-link Jones values.
