# Explicit instance of canonical Markov weights

The Lean class `CanonicalMarkovWeightsH3` (declared in [Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, antipode pairing, and vanishing at $q = 1$](qbeta-per-block-chi-closed-forms.md) §Extension #4) is inhabited. We construct an explicit $\sqrt q$-bearing instance:

$$
  y_{(3)}(q) = z(q), \qquad
  y_{(2,1)}(q) = \tfrac{1}{2} - z(q), \qquad
  y_{(1,1,1)}(q) = z(q),
$$

where $z(q) = \sqrt q / (1 + q) = 1/(q^{1/2}+q^{-1/2})$ is the parameter *this instance* is built on. It is the **excised convention C** value, not the framework's production Markov parameter $z = q^3/(q^2+1)$; the instance is a formal inhabitant of the class, constructed to show the class is non-empty, and nothing downstream reads its $z$ as the paper's.

## Cross-references

- Class declaration: [Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, antipode pairing, and vanishing at $q = 1$](qbeta-per-block-chi-closed-forms.md) §Extension #4.
- Conditional theorems consuming this class: [Conditional on canonical Markov weights](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md).
