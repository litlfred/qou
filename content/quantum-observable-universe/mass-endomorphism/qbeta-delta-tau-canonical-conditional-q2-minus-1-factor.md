**Proposition (conditional on the canonical Wenzl–Markov weights
class, encoded as Lean `class CanonicalMarkovWeightsH3` in
[`qbeta-per-block-chi-closed-forms.lean`](qbeta-per-block-chi-closed-forms.lean)
under §Extension #4 of the parent block).**

*Assume a concrete instance of the canonical Wenzl–Markov weights
class `CanonicalMarkovWeightsH3` exists, supplying weights
$y_{(3)}(q)$, $y_{(2,1)}(q)$, $y_{(1,1,1)}(q)$ that satisfy the
dimension-normalisation axiom*
$y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q) = 1$
*for $q > 0$. Define the canonical $\Delta\tau_M$ as*

$$
  \Delta\tau_M^{\text{can}}(q) =
  y_{(3)}(q) \cdot \chi_{(3)}(q)
  + y_{(2,1)}(q) \cdot \chi_{(2,1)}(q)
  + y_{(1,1,1)}(q) \cdot \chi_{(1,1,1)}(q).
$$

*Then for $q > 0$,*

$$
  \Delta\tau_M^{\text{can}}(q) = (q^2 - 1) \cdot P^{\text{can}}(q)
$$

*where*
$P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q)
+ y_{(1,1,1)}(q) P_{(1,1,1)}(q)$,
*with $P_\lambda(q)$ the per-block witnesses from
`chi_blocks_have_q2_minus_1_factor`. In particular,
$\Delta\tau_M^{\text{can}}(1) = 0$.*

**Proof.** By
[`chi_blocks_have_q2_minus_1_factor`](qbeta-per-block-chi-closed-forms.md),
each per-block character satisfies $\chi_\lambda(q) = (q^2 - 1) \cdot P_\lambda(q)$
for $q > 0$. Substituting and factoring out $(q^2 - 1)$ from the
weighted sum gives the claim. The Lean proof is a direct substitution
plus ring identity. $\square$
## What this block does NOT establish

- **A concrete instance of `CanonicalMarkovWeightsH3`.** The canonical
  $\sqrt q$-bearing Wenzl weights are still open at the formalisation
  level (require Markov-parameter $\sqrt q$ handling beyond `ring`).
  This block is rigorous *conditional* on such an instance existing.
- **The order-1+ Taylor coefficients of $\Delta\tau_M^{\text{can}}$.**
  Vanishing at $q = 1$ (order-0) is the immediate consequence; higher
  orders depend on the specific $y_\lambda(q)$ behaviour at $q = 1$,
  which the dimension-normalisation axiom alone does not pin down.
- **A bridge to the c_k precision ladder.** The f-map keystone (per
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md))
  is still open; this block contributes pre-archimedean structural
  input the f-map would consume, not a closure step.

## Cross-references

- Parent block:
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (lands the per-block $\chi_\lambda$ closed forms +
  `CanonicalMarkovWeightsH3` class).
- Sibling on main:
  [`prop:q-beta-over-e0-classical-vanishing`](../mass-theory/q-beta-over-e0-classical-vanishing.md)
  (different upstream object — $S(q) = \mathfrak{Q}_\beta/E_0$ — but also
  vanishes at $q = 1$).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
