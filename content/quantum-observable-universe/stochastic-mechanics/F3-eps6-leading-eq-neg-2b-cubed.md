**Lean exact-arithmetic lemma**: The leading $\varepsilon^6$ coefficient of $(F_3 - 1)$ at $q = 1 + \varepsilon$ equals $-2 \cdot b^3(q=1) = -3\sqrt{3}/4$.

## Statement

The factor $F_3 = 1 - 2 b^3 \hbar_q^6$ appears in the [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder) precision ladder. The leading $\varepsilon^6$ contribution of $(F_3 - 1)$ at $q = 1+\varepsilon$ attains the **exact algebraic value**:

$$
\boxed{
  -2 \cdot b^3(q=1) \;=\; -2 \cdot \frac{3\sqrt{3}}{8} \;=\; -\frac{3\sqrt{3}}{4}
   \;\approx\; -1.29904 .
}
$$

We verify this at sympy precision in [`probe_q_beta_cat_per_factor_decomposition.py`](../../computations/probe_q_beta_cat_per_factor_decomposition.py) via algebraic equality (no numerical rounding) and in Lean via [`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean).

## Proof

The Hoefsmit off-diagonal coupling requires $b = \sqrt{q^4+q^2+1}/(q^2+1)$. At $q = 1$:

- $q^4 + q^2 + 1 = 3$
- $(q^2+1)^2 = 4$
- $b^2 = 3/4$, hence $b = \sqrt{3}/2$
- $b^3 = (\sqrt{3}/2)^3 = 3\sqrt{3}/8$
- $-2 \cdot b^3 = -3\sqrt{3}/4$

The Lean stub proves all four arithmetic steps directly via `Real.sqrt_sq`, `field_simp`, and `ring`. The proof closes with no `sorry`s.

## Significance

This lemma forms the **purely-arithmetic component** of the $c_3 = -2$ identification in [`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov). The categorical content states that the order-$\hbar_q^6$ contribution to $\tau_M$ factors through Hopf-link Jones values. This remains class-axiomatic via `ThreeFoldMarkovHopfExtraction`. Its **arithmetic discharge** at the $\varepsilon^6$ level is now fully Lean-proved.

Combined with [`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive), two previously-axiomatic class hypotheses reduce to purely algebraic or arithmetic theorems:

1. `MarkovDisjointStabilisation` $\to$ discharged by `MarkovTraceAxioms` (M1 + M3 primitive axioms; iterated stabilisation theorem).
2. `ThreeFoldMarkovHopfExtraction` (leading order) $\to$ discharged by `F3_eps6_leading_eq_neg_2b_cubed` (exact $-2 \cdot b(1)^3$ identity).

The substantive open content of `ThreeFoldMarkovHopfExtraction` reduces to the **categorical identification**. The perturbative $\hbar_q^6$ piece of the $\tau_M$-expansion must factor through Hopf-link Jones values. This is now the only remaining axiomatic input.
