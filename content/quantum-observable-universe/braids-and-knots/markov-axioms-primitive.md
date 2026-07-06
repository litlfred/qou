**Primitive Markov-trace axioms** (helper for the categorical chain).

We record the four Markov-trace axioms (Jones 1985, Wenzl 1988) as Lean-level primitives. This discharges previously-axiomatic class hypotheses from a smaller axiomatic base.

## Axioms

The Markov trace $\tau_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

- **M1 (normalisation)**: $\tau_M(1) = 1$.
- **M2 (cyclicity)**: $\tau_M(xy) = \tau_M(yx)$ for all $x, y \in H_n(R, q)$.
- **M3 (stabilisation by $\sigma_n$)**: $\tau_M(x \sigma_n) = z \cdot \tau_M(x)$ for $x \in H_n(R, q)$. Here $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov-Jones parameter and $\sigma_n$ is the new generator from stabilising to $H_{n+1}(R, q)$.
- **M4 (stabilisation by $\sigma_n^{-1}$)**: $\tau_M(x \sigma_n^{-1}) = z \cdot \tau_M(x)$.

These axioms force $\tau_M$ to be the non-degenerate Jones-Markov trace ([`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection)).

## Consequence: disjoint-product factorisation

From axiom M3 alone, the joint Markov trace of two braids acting on disjoint strand sets factorises:

$$
  \tau_M(K_1 \sqcup K_2) = \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k,
$$

where $k$ is the number of stabilised disjoint strands. We prove this by iterating M3 $k$ times: each new disjoint strand contributes a factor of $z$.

This discharges the class hypothesis `MarkovDisjointStabilisation` used in [`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms) (Mechanism 2 — linking-number locality). The conditional-class inter-knot-decoupling theorem follows from the primitive Markov axioms, requiring no separate axiomatic input.
