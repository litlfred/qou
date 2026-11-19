# Proof of the normalisation axiom

$$
y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q)
= z(q) + 2 \left( \tfrac{1}{2} - z(q) \right) + z(q)
= 1
$$

This holds for every $q > 0$ by direct ring simplification. $\square$

## Scope of the instance

This explicitly constructs an inhabitant of the canonical $H_3$ Markov-weights hypothesis. It establishes that:

- The dimension-normalisation hypothesis has at least one inhabitant.
- All conditional statements under that hypothesis (specifically [the canonical $(q^2-1)$ factor](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md) and its vanishing at $q = 1$) are non-vacuous.
- The hypothesis accommodates the archimedean $\sqrt q$ parametrization of the auxiliary test inhabitant alongside the rational convention-D production weights.

It does not establish:

- That this auxiliary inhabitant is the canonical Wenzl–Markov weight triple. The canonical weights from $H_3(q)$ have a specific closed form derived from the Hecke algebra's Bratteli diagram and quantum dimensions. They are tied to the Markov property $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}(q)$. The canonical inhabitant is identified in the next section.
- A formula for $\Delta\mathrm{tr}_M^{\text{can}}(q)$ at this auxiliary inhabitant, though it is computable via [the canonical $(q^2-1)$ factor](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md).
- Any bearing on the $c_k$ ladder closure.

## The canonical inhabitant, identified

The canonical inhabitant carries the production trace's own weights:

$$
  y_{(3)} = \frac{[4]_q}{[2]_q^{3}} = \frac{q^4+1}{(q^2+1)^2},
  \qquad
  y_{(2,1)} = \frac{1}{[2]_q^{2}} = \frac{q^2}{(q^2+1)^2},
  \qquad
  y_{(1^3)} = 0 .
$$

These are the convention-D values quoted below.

**Why they are the canonical ones, rather than merely another inhabitant.** Convention D is the $N=2$ member of the Ocneanu family $z_N = q^N/[N]_q$ — its framing ratio $a^2 = z/z_-$ is the *monomial* $q^4$, which collapses every Ocneanu numerator into quantum integers and turns the weight product into the hook-content formula $w_\lambda = \dim_q(V_\lambda^{\mathfrak{sl}_N})/[N]_q^{\,n}$ (see [reconciliation of the Markov parameter](markov-z-reconciliation.md)). So the three values are **derived from the trace, not chosen to satisfy the normalisation axiom** — and the vanishing $y_{(1^3)} = 0$ is the $\mathfrak{sl}_2$ **row bound**, since a partition with more than $N$ rows has a cell of content $-N$ whose numerator factor carries $[0]_q = 0$.

**Derived, not merely checked.** The three values equal the $n = 3$ Markov weights solved directly from $\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma_1) = z$, and the Markov relation, and hence agree with the $n = 3$ slice of the general-$n$ Ocneanu weight at $z_{\mathrm{D}}$; see [reconciliation of the Markov parameter](markov-z-reconciliation.md).

**The normalisation is an identity, not a constraint that had to be arranged.** The normalisation relation $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$ reduces to $(q^4+1) + 2q^2 = (q^2+1)^2$, which holds for every $q$ with no positivity hypothesis — equivalently $[4]_q = ([2]_q^2 - 2)[2]_q$, so $[4]_q/[2]_q^3 = 1 - 2/[2]_q^2$.

**Comparison with the auxiliary $\sqrt q$ inhabitant.** The auxiliary inhabitant satisfies the normalisation axiom because $z + 2(\tfrac12 - z) + z = 1$ for *any* $z$ — which is precisely why it satisfies the algebraic axiom without coinciding with the production weights. It differs from the canonical set on all three blocks. The canonical convention-D triple serves as the primary weight assignment for $\Delta\mathrm{tr}_M^{\text{can}}(q)$.

## Numerical sanity check

At the substrate parameter $q = q_0 \approx 1.10998$, this auxiliary inhabitant's own parameter is $z(q_0) = \sqrt{q_0} / (1 + q_0) \approx 0.499$. Note that this is $1/(q^{1/2}+q^{-1/2})$, the **excised convention C** value, not the framework's production $z = q^3/(q^2+1) \approx 0.6127$; the auxiliary inhabitant is free to carry it, but the symbol $z$ here does not mean what it means elsewhere in the paper. The value is close to $1/2$ by accident, since $\sqrt{q_0} \approx 1.054$ and $(1 + q_0)/2 \approx 1.055$. This inhabitant gives $y_{(3)}(q_0) \approx 0.499$, $y_{(2,1)}(q_0) \approx 0.001$, and $y_{(1,1,1)}(q_0) \approx 0.499$. The sum is $0.499 + 2(0.001) + 0.499 = 1.000$, satisfying normalisation.

The canonical Wenzl weights at $q_0$ are $y_{(3)} = [4]_q/[2]_q^3 \approx 0.5054042$, $y_{(2,1)} = 1/[2]_q^2 \approx 0.2472979$, and $y_{(1^3)} = 0$ — **convention D**, the production trace. They satisfy the normalisation $\sum_\lambda y_\lambda d_\lambda = 1$ with $d = (1, 2, 1)$ and no truncation residue. By contrast, the triple $(0.4154,\ 0.2809,\ 0.0227)$ belongs to the excised **convention C** ([trace-convention registry](../../../docs/coordination/trace-convention-registry.md)).

The discrepancy between the auxiliary inhabitant and the canonical convention-D weights is concentrated on the mixed and alternating blocks: while on the symmetric block $(3)$ the auxiliary value $y_{(3)} = z(q_0) \approx 0.4993$ differs from the canonical $\approx 0.5054$ by $\approx 1.2\,\%$, on the remaining blocks the auxiliary inhabitant gives $y_{(2,1)} \approx 0.0007$ against the canonical $\approx 0.2473$, and $y_{(1,1,1)} \approx 0.4993$ where the canonical weight vanishes identically. The dimension-normalisation hypothesis admits infinitely many algebraic inhabitants; the auxiliary inhabitant witnesses non-vacuity of the axiom over $\mathbb{R}$, whereas the canonical inhabitant supplies the unique Wenzl–Ocneanu weights of the production trace.
