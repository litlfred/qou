## Consequence: disjoint-product factorisation

From axiom M3 alone, the joint Markov trace of two braids acting on disjoint
strand sets factorises:

$$
  \tau_M(K_1 \sqcup K_2) \;=\; \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k,
$$

where $k$ is the number of disjoint strands stabilised. The proof is by
iterating M3 $k$ times: each new disjoint strand contributes a factor $z$.

This DISCHARGES the previously-axiomatic class hypothesis `MarkovDisjointStabilisation`
used in [`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)
(Mechanism 2 — linking-number locality). The conditional-class
inter-knot-decoupling theorem now follows from the primitive Markov axioms,
not from a separate axiomatic input.
