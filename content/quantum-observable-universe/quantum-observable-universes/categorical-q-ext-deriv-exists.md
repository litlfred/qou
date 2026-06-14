Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
connection $\nabla$, substrate parameter $q$, and weight
decomposition $(\pi_H, \pi_V)$.  Then the
[$q$-deformed exterior derivative](#def:categorical-q-ext-deriv)

$$
  d_q \;=\; q^{-1} d + (1 - q^{-1})  \pi_V \circ d
  \;\colon\; \Omega^k(A) \to \Omega^{k+1}(A)
$$

exists as a morphism in $\mathbf{C}$ for every $k$.

Uniqueness is
([uniqueness of categorical $q$-exterior derivative](#prop:categorical-q-ext-deriv-unique)).


**Strategy.** We constructively build $d_q$ by taking a scalar-weighted linear combination of the standard categorical de Rham differential $d$ and its vertical projection $\pi_V \circ d$. Substrate parameters supply the necessary weights in the $R$-linear category.
