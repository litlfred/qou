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
- The class formalism accommodates the archimedean $\sqrt q$ parametrization of the auxiliary test inhabitant alongside the rational Convention-D production weights.

It does not establish:

- That this instance is the canonical Wenzl–Markov weights. The canonical weights from $H_3(q)$ have a specific closed form derived from the Hecke algebra's Bratteli diagram and quantum dimensions. They are tied to the Markov property $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}(q)$. The canonical inhabitant is identified in the next section.
- A formula for $\Delta\mathrm{tr}_M^{\text{can}}(q)$ at this instance, though it is computable via `delta_tau_M_canonical_has_q2_minus_1_factor`.
- Any bearing on the $c_k$ ladder closure.

## The canonical inhabitant, identified

**`QOU.BraidKnot.CanonicalMarkovWeightsH3.canonicalInstance`**, carries the production trace's own weights:

$$
  y_{(3)} = \frac{[4]_q}{[2]_q^{3}} = \frac{q^4+1}{(q^2+1)^2},
  \qquad
  y_{(2,1)} = \frac{1}{[2]_q^{2}} = \frac{q^2}{(q^2+1)^2},
  \qquad
  y_{(1^3)} = 0 .
$$

These are exactly the convention-D values this block already quotes below; what was missing was the Lean instance, not the mathematics.

**Why they are the canonical ones, rather than merely another inhabitant.** Convention D is the $N=2$ member of the Ocneanu family $z_N = q^N/[N]_q$ — its framing ratio $a^2 = z/z_-$ is the *monomial* $q^4$, which collapses every Ocneanu numerator into quantum integers and turns the weight product into the hook-content formula $w_\lambda = \dim_q(V_\lambda^{\mathfrak{sl}_N})/[N]_q^{\,n}$ (see [Reconciliation of the Markov parameter $z$](markov-z-reconciliation.md)). So the three values are **derived from the trace, not chosen to satisfy the class axiom** — and the vanishing $y_{(1^3)} = 0$ is the $\mathfrak{sl}_2$ **row bound**, since a partition with more than $N$ rows has a cell of content $-N$ whose numerator factor carries $[0]_q = 0$.

**Derived, not merely checked.** The three values are proved equal to the `n = 3` Markov weights that `QOU.SchurWeyl.HeckeMarkov3` *solves* from `tr_M(1) = 1`, `tr_M(\sigma_1) = z` and the Markov relation — `canonical_y3_eq_markovWeight0`, `canonical_y21_eq_markovWeight2`, `markovWeight1_at_markovZD` in `QOU.BraidKnot.QBetaCanonicalMarkovWeightsDerived` — and hence to the `n = 3` slice of the general-`n` `ocneanuWeight` at `z_D`. The family and the hook-content identification invoked in the previous paragraph are prior results in Lean (`WenzlWeightVanishing`, `SchurWeyl/OcneanuWeight*`, `WenzlWeightLevelR`); see [Reconciliation of the Markov parameter $z$](markov-z-reconciliation.md).

**The normalisation is an identity, not a constraint that had to be arranged.** The class axiom $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$ reduces to $(q^4+1) + 2q^2 = (q^2+1)^2$, which holds for every $q$ with no positivity hypothesis — equivalently $[4]_q = ([2]_q^2 - 2)[2]_q$, so $[4]_q/[2]_q^3 = 1 - 2/[2]_q^2$.

**The pre-existing `explicitInstance` is untouched and was never wrong.** It satisfies the class axiom because $z + 2(\tfrac12 - z) + z = 1$ for *any* $z$ — which is precisely why it inhabits the class without being the production weights. It differs from the canonical set on all three blocks.

**It is now the class's default instance**, so a bare `delta_tau_M_canonical q` means the production trace's $\Delta\tau_M$ rather than the $\sqrt q$-bearing toy.

The promotion was made as a **pair** with demoting `explicitInstance` from `instance` to `def`, and the pairing is the point: two global instances of one class is a silent hazard, since resolution takes the later declaration and nothing in the source says so. With one registered instance, what a bare use means is *stated* rather than inferred. `explicitInstance` remains a first-class inhabitant and every use of it is unchanged — they all name it explicitly with `@` — it is no longer a candidate for implicit resolution.

The change is machine-guarded, not asserted: `delta_tau_M_canonical_resolves_to_canonical` is `rfl`-provable only because resolution picks the canonical weights, so declaring a second instance or promoting `explicitInstance` back would stop it typechecking rather than silently changing what every bare use means. The guard was verified to have teeth — the same statement written against `explicitInstance` does not typecheck. All five files that mention the class are `lean`-direct exit 0, against a green baseline taken *before* the change.

Measurement: [`canonical_markov_weights_h3_are_sl2_dimensions.py`](https://github.com/litlfred/qou/blob/main/computations/probes/canonical_markov_weights_h3_are_sl2_dimensions.py) (11/11).

## Numerical sanity check

At the substrate parameter $q = q_0 \approx 1.10998$, this instance's own parameter is $z(q_0) = \sqrt{q_0} / (1 + q_0) \approx 0.499$. Note that this is $1/(q^{1/2}+q^{-1/2})$, the **excised convention C** value, not the framework's production $z = q^3/(q^2+1) \approx 0.6127$; the instance is a formal inhabitant of the class and is free to carry it, but the symbol $z$ here does not mean what it means elsewhere in the paper. The value is close to $1/2$ by accident, since $\sqrt{q_0} \approx 1.054$ and $(1 + q_0)/2 \approx 1.055$. This instance gives $y_{(3)}(q_0) \approx 0.499$, $y_{(2,1)}(q_0) \approx 0.001$, and $y_{(1,1,1)}(q_0) \approx 0.499$. The sum is $0.499 + 2(0.001) + 0.499 = 1.000$, satisfying normalisation.

The canonical Wenzl weights at $q_0$ are $y_{(3)} = [4]_q/[2]_q^3 \approx 0.5054042$, $y_{(2,1)} = 1/[2]_q^2 \approx 0.2472979$, and $y_{(1^3)} = 0$ — **convention D**, the production trace. They satisfy the normalisation $\sum_\lambda y_\lambda d_\lambda = 1$ with $d = (1, 2, 1)$ and no truncation residue. By contrast, the triple $(0.4154,\ 0.2809,\ 0.0227)$ produced by `markov_weights_symbolic.solve_y_lambda(3)` belongs to the excised **convention C** ([trace-convention registry](../../../docs/coordination/trace-convention-registry.md)).

The discrepancy between `explicitInstance` and the canonical Convention-D weights is concentrated on the mixed and alternating blocks: while on the symmetric block $(3)$ the auxiliary value $y_{(3)} = z(q_0) \approx 0.4993$ differs from the canonical $\approx 0.5054$ by $\approx 1.2\,\%$, on the remaining blocks `explicitInstance` gives $y_{(2,1)} \approx 0.0007$ against the canonical $\approx 0.2473$, and $y_{(1,1,1)} \approx 0.4993$ where the canonical weight vanishes identically. The class `CanonicalMarkovWeightsH3` admits infinitely many algebraic inhabitants; `explicitInstance` witnesses non-vacuity of the class axioms over $\mathbb{R}$, whereas `canonicalInstance` supplies the unique Wenzl–Ocneanu weights of the production trace.
