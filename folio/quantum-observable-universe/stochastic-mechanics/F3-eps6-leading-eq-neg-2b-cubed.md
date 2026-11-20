**Lean exact-arithmetic lemma**: the leading $\varepsilon^6$ coefficient of $(F_3 - 1)$ at $q = 1 + \varepsilon$ equals $-2 \cdot b^3(q=1) = -3\sqrt{3}/4$.

## Statement

For the $F_3 = 1 - 2 b^3 \hbar_q^6$ factor in the [$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder) precision ladder, the leading $\varepsilon^6$ contribution of $(F_3 - 1)$ at $q = 1+\varepsilon$ is the exact algebraic value:

$$
\boxed{
  -2 \cdot b^3(q=1) \;=\; -2 \cdot \frac{3\sqrt{3}}{8} \;=\; -\frac{3\sqrt{3}}{4}
   \;\approx\; -1.29904 .
}
$$

This is verified at sympy precision in [`probe_q_beta_cat_per_factor_decomposition.py`](../../computations/probe_q_beta_cat_per_factor_decomposition.py) and in Lean [`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean).

## Proof

The Hoefsmit off-diagonal coupling is $b = \sqrt{q^4+q^2+1}/(q^2+1)$. At $q = 1$, $b^2 = 3/4$, hence $b = \sqrt{3}/2$. Thus $b^3 = 3\sqrt{3}/8$, and $-2 \cdot b^3 = -3\sqrt{3}/4$. The Lean stub proves all steps directly.

## Significance

This lemma is the purely-arithmetic component of the $c_3 = -2$ identification in [Categorical derivation of $c_3 = J_{\mathrm{Hopf}}(q=1) = -2$ in the $\mathfrak{Q}_\beta$ precision ladder via 3-fold Markov closure → 2-strand sub-braid Hopf-link substructure → KL classical-limit decategorification](#prop:q-beta-c3-hopf-three-fold-markov). The categorical content remains class-axiomatic via `ThreeFoldMarkovHopfExtraction`, but its arithmetic discharge at the $\varepsilon^6$ level is Lean-proved.

Combined with [Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988)](#rem:markov-axioms-primitive), two previously-axiomatic class hypotheses have been replaced by purely algebraic/arithmetic theorems. The substantive open content of `ThreeFoldMarkovHopfExtraction` reduces to the categorical identification that the perturbative $\hbar_q^6$ piece of the $\mathrm{tr}_M$-expansion factors through Hopf-link Jones values.
