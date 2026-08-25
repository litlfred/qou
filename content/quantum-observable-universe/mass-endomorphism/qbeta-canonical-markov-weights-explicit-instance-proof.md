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

- That this instance is the canonical Wenzl–Markov weights. The canonical weights from $H_3(q)$ have a specific closed form derived from the Hecke algebra's Bratteli diagram and quantum dimensions. They are tied to the Markov property $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}(q)$. Identifying the canonical inhabitant remains open.
- A formula for $\Delta\mathrm{tr}_M^{\text{can}}(q)$ at this instance, though it is computable via `delta_tau_M_canonical_has_q2_minus_1_factor`.
- Any bearing on the $c_k$ ladder closure.

## Numerical sanity check

At the substrate parameter $q = q_0 \approx 1.10998$, this instance's own parameter is $z(q_0) = \sqrt{q_0} / (1 + q_0) \approx 0.499$. Note that this is $1/(q^{1/2}+q^{-1/2})$, the **excised convention C** value, not the framework's production $z = q^3/(q^2+1) \approx 0.6127$; the instance is a formal inhabitant of the class and is free to carry it, but the symbol $z$ here does not mean what it means elsewhere in the paper. The value is close to $1/2$ by accident, since $\sqrt{q_0} \approx 1.054$ and $(1 + q_0)/2 \approx 1.055$. This instance gives $y_{(3)}(q_0) \approx 0.499$, $y_{(2,1)}(q_0) \approx 0.001$, and $y_{(1,1,1)}(q_0) \approx 0.499$. The sum is $0.499 + 2(0.001) + 0.499 = 1.000$, satisfying normalisation.

The canonical Wenzl weights at $q_0$ are $y_{(3)} = [4]_q/[2]_q^3 \approx 0.5054042$, $y_{(2,1)} = 1/[2]_q^2 \approx 0.2472979$, and $y_{(1^3)} = 0$ exactly — **convention D**, the production trace. They satisfy the normalisation $\sum_\lambda y_\lambda d_\lambda = 1$ exactly, with $d = (1, 2, 1)$; there is no truncation residue. The values $(0.4154,\ 0.2809,\ 0.0227)$ previously called canonical here, and attributed to `markov_weights_symbolic.solve_y_lambda(3)`, are **convention C**, excised by the owner ruling of 2026-08-09, and their reported sum $0.9999$ was a truncation artefact of that same excised route. Check the convention of any `markov_weights_symbolic` call against the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md) before quoting it again.

The mismatch between this instance and the canonical weights survives the convention change, but it moves. On the $(3)$ block the gap shrinks: the instance gives $y_{(3)} = z(q_0) \approx 0.4993$ against the canonical $\approx 0.5054$, a $\approx 1.2\,\%$ discrepancy where against the excised C value $0.4154$ it was $\approx 20\,\%$. What now decides it outright is the rest of the vector: the instance has $y_{(2,1)} \approx 0.0007$ against the canonical $\approx 0.2473$, and $y_{(1,1,1)} \approx 0.4993$ where the canonical value is $0$ exactly. So this is still not the canonical instance, but the sharpest evidence is the vanishing of the $(1^3)$ block, not the size of the $(3)$ block. The class admits infinitely many inhabitants, and this construction merely identifies one.
