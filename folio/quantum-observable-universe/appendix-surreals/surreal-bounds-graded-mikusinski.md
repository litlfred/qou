**Remark (the surreal-bound family as graded-Mikusiński std-collapse instances).**

The four millennium-problem surreal bounds ([BSD surreal bound](#rem:bsd-surreal-bound), [RH surreal bound](#rem:rh-surreal-bound), [P vs NP surreal bound](#rem:p-vs-np-surreal-bound), [Collatz surreal bound](#rem:collatz-surreal-bound)) share a structural mechanism. The standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$ collapses a transfinite cost on the surreal-envelope side to a standard-real cost on the archimedean side, leaving a finite gap. Per [surreal squeeze](#lem:surreal-squeeze), the gap forces the inequality.

The graded-Mikusiński correspondence ([depth–period correspondence](#conj:gb-depth-period-correspondence)) identifies these four remarks as the same construction at different depths of the iterated-integral filtration on $\mathcal{H}_q$:

| Bound | Conjecture interpreted | Depth class | Std-collapsed object |
|---|---|---|---|
| RH | [collapse of the quantum gap](#thm:quantum-gap-collapse) | $\mathcal{P}_1$ (logs) | $\zeta$ critical-line vanishing |
| BSD | [$q$-Birch–Swinnerton-Dyer](#conj:q-birch-swinnerton-dyer) | $\mathcal{P}_2$ (regulators) | $L$-function rank match |
| P vs NP | [P vs NP in the QOU](#conj:p-vs-np-qou) | $\mathcal{P}_{\geq 1}$ (transfinite Reeb period) | budget separation |
| Collatz | [$q$-Collatz](#conj:q-collatz) | $\mathcal{P}_2$ (Bloch–Wigner shadow) | contact-boundary deviation |

The depth assignment above is conjectural modulo [the depth–period correspondence](#conj:gb-depth-period-correspondence). The correspondence generates all four bounds via the single form:

$$
\mathrm{std}\!\left( \text{depth-}n \text{ infinitesimal cost in } \mathbf{No} \right) > \text{standard archimedean budget},
$$

where $n$ ranges over the four classes and $\mathrm{std}$ serves as the archimedean realization. The inequality direction is enforced by [surreal squeeze](#lem:surreal-squeeze).

Unifying the four bounds provides three concrete consequences. First, problem-specific squeezes give way to a universal std-collapse at a specified depth, analogous to Mikusiński's (1959) field of fractions unifying operational identities. Second, closing the squeeze at depth $n$ for one millennium problem transports to any other problem at the same depth (e.g., depth-2 techniques for BSD $\leftrightarrow$ Collatz). Third, the correspondence predicts a depth-3 surreal bound for any arithmetic conjecture whose archimedean reading involves weight-3 Goncharov periods (multiple zeta values $\zeta(3), \zeta(2,1)$), such as Apéry-style irrationality questions (Zagier 1986). For orientation on that programme: for every odd $a \geq 3$, $\dim_{\mathbb{Q}} \mathrm{span}\{1, \zeta(3), \zeta(5), \ldots, \zeta(a)\} > 0.395 \log a$ \cite[Thm.~4]{zudilin2001}. This bounds a dimension; it does not decide the irrationality of any single $\zeta(2k+1)$ with $k \geq 2$.

This structure connects directly to a graded Titchmarsh problem. Mikusiński passes from $C[0,\infty)$ to its field of fractions via Titchmarsh's no-zero-divisor theorem. The graded analog asks at which iterated-integral depth the $*_q$-product on $\mathcal{H}_q$ first acquires zero divisors. Each surreal-bound remark is an obstruction to inverting a depth-$n$ element, representing exactly the obstruction Mikusiński removes by passing to fractions. The four bounds are instances of graded Titchmarsh failure, each occurring at its characteristic depth.

The novel mathematical content resides in [the depth–period correspondence](#conj:gb-depth-period-correspondence) and its discharge targets.
