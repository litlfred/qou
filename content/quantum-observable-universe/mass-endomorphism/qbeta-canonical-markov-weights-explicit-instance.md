# Explicit instance of canonical Markov weights

The Lean class `CanonicalMarkovWeightsH3` (declared in [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) §Extension #4) is inhabited. We construct an explicit $\sqrt q$-bearing instance:

$$
  y_{(3)}(q) = z(q), \qquad
  y_{(2,1)}(q) = \tfrac{1}{2} - z(q), \qquad
  y_{(1,1,1)}(q) = z(q),
$$

where $z(q) = \sqrt q / (1 + q)$ is the Markov parameter.

## Cross-references

- Class declaration: [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) §Extension #4.
- Conditional theorems consuming this class: [`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md).
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
