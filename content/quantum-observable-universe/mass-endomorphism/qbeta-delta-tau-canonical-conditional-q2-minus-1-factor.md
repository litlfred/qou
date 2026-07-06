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

$$
  P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q)
  + y_{(1,1,1)}(q) P_{(1,1,1)}(q),
$$

*with $P_\lambda(q)$ the per-block witnesses from
`chi_blocks_have_q2_minus_1_factor`. In particular,
$\Delta\tau_M^{\text{can}}(1) = 0$.*
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

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
