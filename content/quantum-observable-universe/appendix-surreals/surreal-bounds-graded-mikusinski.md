**Remark (the surreal-bound family as graded-Mikusiński std-collapse instances).**

The four millennium-problem surreal bounds in this chapter ([`rem:bsd-surreal-bound`](#rem:bsd-surreal-bound), [`rem:rh-surreal-bound`](#rem:rh-surreal-bound), [`rem:p-vs-np-surreal-bound`](#rem:p-vs-np-surreal-bound), [`rem:collatz-surreal-bound`](#rem:collatz-surreal-bound)) interpret different conjectures. However, they share a structural mechanism. The standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$ collapses a transfinite cost on the surreal-envelope side to a standard-real cost on the archimedean side. This leaves a finite gap. Per [`lem:surreal-squeeze`](#lem:surreal-squeeze), the gap forces the inequality.

The graded-Mikusiński keystone ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) identifies these four remarks as the same construction at different **depths** of the iterated-integral filtration on $\mathcal{H}_q$:

| Bound | Conjecture interpreted | Depth class | Std-collapsed object |
|---|---|---|---|
| RH | [`thm:quantum-gap-collapse`](#thm:quantum-gap-collapse) | $\mathcal{P}_1$ (logs) | $\zeta$ critical-line vanishing |
| BSD | [`conj:q-birch-swinnerton-dyer`](#conj:q-birch-swinnerton-dyer) | $\mathcal{P}_2$ (regulators) | $L$-function rank match |
| P vs NP | [`conj:p-vs-np-qou`](#conj:p-vs-np-qou) | $\mathcal{P}_{\geq 1}$ (transfinite Reeb period) | budget separation |
| Collatz | [`conj:q-collatz`](#conj:q-collatz) | $\mathcal{P}_2$ (Bloch–Wigner shadow) | contact-boundary deviation |

The depth assignment above is conjectural at each row, modulo [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence). The keystone provides a single framework generating all four bounds. Each bound takes the form:

$$
  \mathrm{std}\!\left( \text{depth-}n \text{ infinitesimal cost in } \mathbf{No} \right)
  \;>\;
  \text{standard archimedean budget},
$$

with $n$ ranging over the four classes and $\mathrm{std}$ serving as the archimedean realization. The inequality direction is enforced by [`lem:surreal-squeeze`](#lem:surreal-squeeze).

### Significance for this paper

Unifying the four bounds has three concrete consequences:

1. **No more one-off arguments.** Each `*-surreal-bound` block currently uses a problem-specific squeeze. With the keystone, each reduces to picking the depth and applying the universal std-collapse. This is analogous to how the Mikusiński (1959) field of fractions unifies disparate operational identities.
2. **Cross-bound transport.** A technique that closes the squeeze at depth $n$ for one millennium problem candidate-transports to any other problem at the same depth. (E.g., depth-2 techniques for BSD $\leftrightarrow$ Collatz.)
3. **Depth-3 prediction.** The keystone predicts a depth-3 surreal bound for any open problem whose archimedean reading involves weight-3 Goncharov periods (multiple zeta values $\zeta(3), \zeta(2,1)$). Apéry-style irrationality questions (Zagier 1986) serve as candidates. A future block can record this as the depth-3 instance.

### Connection to graded Titchmarsh

Mikusiński's construction passes from $C[0,\infty)$ to its field of fractions via Titchmarsh's no-zero-divisor theorem. The graded analog asks: at which iterated-integral depth does the $*_q$-product on $\mathcal{H}_q$ first acquire zero divisors? Each surreal-bound remark is an obstruction to inverting a depth-$n$ element. This is exactly the kind of obstruction Mikusiński's construction removes by passing to fractions. The four bounds are four concrete instances of graded Titchmarsh failure. Each occurs at its characteristic depth.

This reframes existing content under a single rubric. The novel mathematical content resides in [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) and its discharge targets.
