# Proof of the normalisation axiom

$$
y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q)
= z(q) + 2 \left( \tfrac{1}{2} - z(q) \right) + z(q)
= 1
$$

This holds for every $q > 0$. The Lean discharge is `ring`. $\square$

## Scope of the instance

This explicitly constructs an instance of `CanonicalMarkovWeightsH3`. It establishes that:

- The class `CanonicalMarkovWeightsH3` has at least one inhabitant.
- All conditional theorems stated under `[CanonicalMarkovWeightsH3]` (specifically [`delta_tau_M_canonical_has_q2_minus_1_factor`](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md) and its corollary `delta_tau_M_canonical_vanish_at_one_via_factor`) are not vacuous.
- The class formalism naturally accommodates the archimedean $\sqrt q$ structure expected from the canonical Wenzl–Markov construction.

It does not establish:

- That this instance is the canonical Wenzl–Markov weights. The canonical weights from $H_3(q)$ have a specific closed form derived from the Hecke algebra's Bratteli diagram and quantum dimensions. They are tied to the Markov property $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}(q)$. Identifying the canonical inhabitant remains open (see the 1ppQ-Q$_\beta$ ledger).
- A formula for $\Delta\mathrm{tr}_M^{\text{can}}(q)$ at this instance, though it is computable via `delta_tau_M_canonical_has_q2_minus_1_factor`.
- Any bearing on the $c_k$ ladder closure.

## Numerical sanity check

At the substrate parameter $q = q_0 \approx 1.10998$, we have $z(q_0) = \sqrt{q_0} / (1 + q_0) \approx 0.499$. This is close to $1/2$ by accident, since $\sqrt{q_0} \approx 1.054$ and $(1 + q_0)/2 \approx 1.055$. This instance gives $y_{(3)}(q_0) \approx 0.499$, $y_{(2,1)}(q_0) \approx 0.001$, and $y_{(1,1,1)}(q_0) \approx 0.499$. The sum is $0.499 + 2(0.001) + 0.499 = 1.000$, satisfying normalisation.

The canonical Wenzl weights (computed by `markov_weights_symbolic.solve_y_lambda(3)` at $q_0$) give $y_{(3)}^{\text{canon}} \approx 0.4154$, $y_{(2,1)}^{\text{canon}} \approx 0.2809$, and $y_{(1,1,1)}^{\text{canon}} \approx 0.0227$. The sum is $0.9999$ (canonical normalisation, subject to truncation precision).

The numerical mismatch between this instance ($y_{(3)} \approx 0.499$) and the canonical values ($y_{(3)} \approx 0.4154$) confirms this is not the canonical instance. The class admits infinitely many inhabitants, and this construction merely identifies one.
