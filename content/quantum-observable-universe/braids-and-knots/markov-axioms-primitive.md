**Primitive Markov-trace axioms** (helper for the categorical chain).

This remark records the four Markov-trace axioms (Jones 1985, Wenzl 1988) as
Lean-level primitives, allowing **previously-axiomatic class hypotheses to be
discharged** from a smaller axiomatic base.

## Axioms

The Markov trace $\tau_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the
unique linear functional satisfying:

- **M1 (normalisation)**: $\tau_M(1) = 1$.
- **M2 (cyclicity)**: $\tau_M(xy) = \tau_M(yx)$ for all $x, y \in H_n(R, q)$.
- **M3 (stabilisation by $\sigma_n$)**: $\tau_M(x \sigma_n) = z \cdot \tau_M(x)$
  for $x \in H_n(R, q)$, where $z = 1/(\sqrt q + 1/\sqrt q)$ is the
  Markov-Jones parameter and $\sigma_n$ is the new generator from
  stabilising to $H_{n+1}(R, q)$.
- **M4 (stabilisation by $\sigma_n^{-1}$)**: $\tau_M(x \sigma_n^{-1}) = z \cdot \tau_M(x)$.

These together force $\tau_M$ to be the Jones-Markov (non-degenerate) trace
per [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection).

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

## Status

The Lean stub [`markov-axioms-primitive.lean`](markov-axioms-primitive.lean):

- Defines `class MarkovTraceAxioms` with fields for M1 and M3 (the two
  needed for the factorisation; M2 is implicit in the cyclic-trace
  construction; M4 follows from M3 via the Hecke quadratic).
- Proves `markov_iterated_stab`: k applications of M3 give $\tau \cdot z^k$.
- Proves `disjoint_product_factorisation`: from M3 alone, the disjoint
  factorisation holds.
- Discharges `MarkovDisjointStabilisation` from `MarkovTraceAxioms`.

Status: **closed**, no `sorry`s. The two class fields (`tau_one`,
`tau_stab`) carry the unavoidable axiomatic content (M1 and M3 are
Jones-1985 axioms, not derivable from more primitive Lean content
in this scope).
