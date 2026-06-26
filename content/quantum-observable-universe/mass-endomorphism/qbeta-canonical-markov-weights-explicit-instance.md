**Proposition (explicit instance).** *The Lean class
`CanonicalMarkovWeightsH3` (from
[`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
§Extension #4) is inhabited. An explicit $\sqrt q$-bearing instance
is*

$$
  y_{(3)}(q) = z(q), \qquad
  y_{(2,1)}(q) = \tfrac{1}{2} - z(q), \qquad
  y_{(1,1,1)}(q) = z(q),
$$

*where $z(q) = \sqrt q / (1 + q)$ is the Markov parameter
(`markov_parameter`).*

**Proof of the normalisation axiom.** $y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q)
= z(q) + 2 \left( \tfrac{1}{2} - z(q) \right) + z(q)
= z(q) + 1 - 2 z(q) + z(q) = 1$, valid for every $q > 0$. The Lean
discharge is `ring`. $\square$

## Honest scope — what this instance does and does NOT establish

**Establishes (rigorously):**

- The class `CanonicalMarkovWeightsH3` has at least one inhabitant.
- All §3b-cond conditional theorems stated under
  `[CanonicalMarkovWeightsH3]` (in particular
  [`delta_tau_M_canonical_has_q2_minus_1_factor`](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md)
  and its corollary `delta_tau_M_canonical_vanish_at_one_via_factor`)
  are NOT vacuous — they hold for at least this concrete instance.
- The $\sqrt q$-bearing form of the instance demonstrates that the
  class formalism naturally accommodates the archimedean
  $\sqrt q$ structure expected from the canonical Wenzl–Markov
  construction.

**Does NOT establish:**

- That this instance IS the canonical Wenzl–Markov weights. The
  canonical weights from $H_3(q)$ have a specific closed form
  derived from the Bratteli-diagram / quantum-dimension structure
  of the Hecke algebra; they are tied to the Markov property
  $\tau_M(x \cdot \sigma_{n-1}) = z \cdot \tau_M(x)$ for
  $x \in H_{n-1}(q)$. Identifying which inhabitant of the class is
  THE canonical one remains open (the residue-A categorical ID
  question — see 1ppQ-Q$_\beta$ ledger).
- A formula for $\Delta\tau_M^{\text{can}}(q)$ at this instance
  (although it is now computable via
  `delta_tau_M_canonical_has_q2_minus_1_factor` modulo straight
  algebra).
- Any bearing on the $c_k$ ladder closure — the f-map remains open.

## Numerical sanity check

At $q = q_0 \approx 1.10998$ (substrate parameter):

- $z(q_0) = \sqrt{q_0} / (1 + q_0) \approx 0.499$ — close to $1/2$
  by accident (since $\sqrt{q_0} \approx 1.054$ and
  $(1 + q_0)/2 \approx 1.055$).
- This instance gives $y_{(3)}(q_0) \approx 0.499$,
  $y_{(2,1)}(q_0) \approx 0.001$, $y_{(1,1,1)}(q_0) \approx 0.499$,
  with sum $0.499 + 2(0.001) + 0.499 = 1.000$ (normalisation).

The CANONICAL Wenzl weights (computed by
`markov_weights_symbolic.solve_y_lambda(3)` at $q_0$) give
$y_{(3)}^{\text{canon}} \approx 0.4154$,
$y_{(2,1)}^{\text{canon}} \approx 0.2809$,
$y_{(1,1,1)}^{\text{canon}} \approx 0.0227$,
with sum $0.4154 + 2(0.2809) + 0.0227 = 0.9999$ (canonical
normalisation, off by $10^{-4}$ from 1 due to truncation precision).

The numerical mismatch between this instance ($y_{(3)} \approx 0.499$)
and canonical ($y_{(3)} \approx 0.4154$) confirms this is NOT the
canonical instance — the class admits infinitely many inhabitants,
and we are identifying ONE.

## Cross-references

- Class declaration:
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  §Extension #4.
- Conditional theorems consuming this class:
  [`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor`](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
