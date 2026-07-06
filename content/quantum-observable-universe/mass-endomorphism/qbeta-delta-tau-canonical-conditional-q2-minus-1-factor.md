# Canonical $(q^2 - 1)$ factor of the Markov trace difference

Assume a concrete instance of the canonical Wenzl–Markov weights class `CanonicalMarkovWeightsH3` exists. This instance supplies weights $y_{(3)}(q)$, $y_{(2,1)}(q)$, and $y_{(1,1,1)}(q)$ satisfying the dimension-normalisation axiom $y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q) = 1$ for $q > 0$. 

Define the canonical trace difference $\Delta\tau_M^{\text{can}}(q)$ as the weighted sum:

$$
  \Delta\tau_M^{\text{can}}(q) =
  y_{(3)}(q) \chi_{(3)}(q)
  + y_{(2,1)}(q) \chi_{(2,1)}(q)
  + y_{(1,1,1)}(q) \chi_{(1,1,1)}(q).
$$

Then for $q > 0$, the trace difference factors as:

$$
  \Delta\tau_M^{\text{can}}(q) = (q^2 - 1) P^{\text{can}}(q),
$$

where

$$
  P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q) + y_{(1,1,1)}(q) P_{(1,1,1)}(q).
$$

Here $P_\lambda(q)$ are the per-block witnesses from `chi_blocks_have_q2_minus_1_factor`. In particular, $\Delta\tau_M^{\text{can}}(1) = 0$.

## Cross-references

- Parent block: [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md) (establishes the per-block $\chi_\lambda$ closed forms and the `CanonicalMarkovWeightsH3` class).
- Sibling on main: [`prop:q-beta-over-e0-classical-vanishing`](../mass-theory/q-beta-over-e0-classical-vanishing.md) (shows the classical-point vanishing of the upstream object $S(q) = \mathfrak{Q}_\beta/E_0$).
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, and numerical evaluation at the substrate parameter $q_0$. Generic categorical or $q$-deformation identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
