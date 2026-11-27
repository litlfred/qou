$$
y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q)
= z(q) + 2 \left( \tfrac{1}{2} - z(q) \right) + z(q)
= 1
$$

This holds for every $q > 0$. $\square$

## Scope of the explicit choice

This explicitly constructs weights satisfying the canonical Markov-weight hypothesis. It establishes that:

- The hypothesis is satisfiable.
- The conditional results stated under it (specifically the [canonical $(q^2-1)$ factor of the Markov trace difference](qbeta-delta-tau-canonical-conditional-q2-minus-1-factor.md) and its corollary, vanishing at $q = 1$) are not vacuous.
- The hypothesis accommodates the archimedean $\sqrt q$ parametrization of this auxiliary choice alongside the rational Wenzl–Markov weights at $z = q^3/(q^2+1)$.

It does not establish:

- That this instance is the canonical Wenzl–Markov weights. The canonical weights from $H_3(q)$ have a specific closed form derived from the Hecke algebra's Bratteli diagram and quantum dimensions. They are tied to the Markov property $\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_{n-1}(q)$. The canonical inhabitant is identified in the next section.
- A formula for $\Delta\mathrm{tr}_M^{\text{can}}(q)$ at this instance, though it is computable from the canonical $(q^2 - 1)$ factorisation.
- Any bearing on the $c_k$ ladder closure.

## The canonical inhabitant, identified

The canonical choice carries the production trace's own weights:

$$
  y_{(3)} = \frac{[4]_q}{[2]_q^{3}} = \frac{q^4+1}{(q^2+1)^2},
  \qquad
  y_{(2,1)} = \frac{1}{[2]_q^{2}} = \frac{q^2}{(q^2+1)^2},
  \qquad
  y_{(1^3)} = 0 .
$$

**Why these weights are canonical.** The Markov parameter $z = q^3/(q^2+1)$ is the $N=2$ member of the Ocneanu family $z_N = q^N/[N]_q$ — its framing ratio $a^2 = z/z_-$ is the *monomial* $q^4$, which collapses every Ocneanu numerator into quantum integers and turns the weight product into the hook-content formula $w_\lambda = \dim_q(V_\lambda^{\mathfrak{sl}_N})/[N]_q^{\,n}$ (see [Reconciliation of the Markov parameter $z$](markov-z-reconciliation.md)). Thus the three values are **derived from the trace rather than chosen to satisfy the normalisation**, and the vanishing $y_{(1^3)} = 0$ is the $\mathfrak{sl}_2$ **row bound** ($[0]_q = 0$ at content $-2$).

**Derived from the Markov axioms.** The three values equal the unique $n = 3$ Markov weights solved from $\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma_1) = q^3/(q^2+1)$, and the Markov relation, matching the $n = 3$ slice of the general-$n$ Ocneanu formula ([Reconciliation of the Markov parameter $z$](markov-z-reconciliation.md)).

**The normalisation is an identity, not a constraint that had to be arranged.** The normalisation $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$ reduces to $(q^4+1) + 2q^2 = (q^2+1)^2$, which holds for every $q$ with no positivity hypothesis — equivalently $[4]_q = ([2]_q^2 - 2)[2]_q$, so $[4]_q/[2]_q^3 = 1 - 2/[2]_q^2$.

**The explicit $\sqrt q$-bearing choice is not wrong.** It satisfies the normalisation because $z + 2(\tfrac12 - z) + z = 1$ for *any* $z$ — which is precisely why it satisfies the hypothesis without being the production weights. It differs from the canonical set on all three blocks.

## Numerical sanity check

At the substrate parameter $q = q_0 \approx 1.10998$, the auxiliary function evaluates to $\sqrt{q_0} / (1 + q_0) \approx 0.499$ (distinct from the Markov parameter $q_0^3/(q_0^2+1) \approx 0.6127$), yielding $y_{(3)}(q_0) \approx 0.499$, $y_{(2,1)}(q_0) \approx 0.001$, and $y_{(1,1,1)}(q_0) \approx 0.499$, with $0.499 + 2(0.001) + 0.499 = 1.000$.

By contrast, the canonical Wenzl–Markov weights at $q_0$ (for $z = q^3/(q^2+1)$) are $y_{(3)} = [4]_q/[2]_q^3 \approx 0.5054042$, $y_{(2,1)} = 1/[2]_q^2 \approx 0.2472979$, and $y_{(1^3)} = 0$, satisfying $\sum_\lambda y_\lambda d_\lambda = 1$ with $d = (1, 2, 1)$ and zero truncation residue.

The difference between the auxiliary witness and the canonical Wenzl–Markov weights is concentrated on the mixed and alternating blocks: while on the symmetric block $(3)$ the auxiliary value $y_{(3)} = z(q_0) \approx 0.4993$ differs from the canonical $\approx 0.5054$ by $\approx 1.2\,\%$, on the remaining blocks the explicit choice gives $y_{(2,1)} \approx 0.0007$ against the canonical $\approx 0.2473$, and $y_{(1,1,1)} \approx 0.4993$ where the canonical weight vanishes identically. The hypothesis admits infinitely many algebraic solutions; the explicit choice witnesses its non-vacuity over $\mathbb{R}$, whereas the canonical choice supplies the unique Wenzl–Ocneanu weights of the production trace.
