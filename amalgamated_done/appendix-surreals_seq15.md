<!-- FILE_START: surreal-bounds-graded-mikusinski.md -->
**Remark (the surreal-bound family as graded-Mikusiński std-collapse instances).**

The four millennium-problem surreal bounds ([`rem:bsd-surreal-bound`](#rem:bsd-surreal-bound), [`rem:rh-surreal-bound`](#rem:rh-surreal-bound), [`rem:p-vs-np-surreal-bound`](#rem:p-vs-np-surreal-bound), [`rem:collatz-surreal-bound`](#rem:collatz-surreal-bound)) share a structural mechanism. The standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$ collapses a transfinite cost on the surreal-envelope side to a standard-real cost on the archimedean side, leaving a finite gap. Per [`lem:surreal-squeeze`](#lem:surreal-squeeze), the gap forces the inequality.

The graded-Mikusiński keystone ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) identifies these four remarks as the same construction at different depths of the iterated-integral filtration on $\mathcal{H}_q$:

| Bound | Conjecture interpreted | Depth class | Std-collapsed object |
|---|---|---|---|
| RH | [`thm:quantum-gap-collapse`](#thm:quantum-gap-collapse) | $\mathcal{P}_1$ (logs) | $\zeta$ critical-line vanishing |
| BSD | [`conj:q-birch-swinnerton-dyer`](#conj:q-birch-swinnerton-dyer) | $\mathcal{P}_2$ (regulators) | $L$-function rank match |
| P vs NP | [`conj:p-vs-np-qou`](#conj:p-vs-np-qou) | $\mathcal{P}_{\geq 1}$ (transfinite Reeb period) | budget separation |
| Collatz | [`conj:q-collatz`](#conj:q-collatz) | $\mathcal{P}_2$ (Bloch–Wigner shadow) | contact-boundary deviation |

The depth assignment above is conjectural modulo [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence). The keystone generates all four bounds via the single form:

$$
\mathrm{std}\!\left( \text{depth-}n \text{ infinitesimal cost in } \mathbf{No} \right) > \text{standard archimedean budget},
$$

where $n$ ranges over the four classes and $\mathrm{std}$ serves as the archimedean realization. The inequality direction is enforced by [`lem:surreal-squeeze`](#lem:surreal-squeeze).

Unifying the four bounds provides three concrete consequences. First, we replace problem-specific squeezes with a universal std-collapse at a specified depth, analogous to Mikusiński's (1959) field of fractions unifying operational identities. Second, closing the squeeze at depth $n$ for one millennium problem transports to any other problem at the same depth (e.g., depth-2 techniques for BSD $\leftrightarrow$ Collatz). Third, the keystone predicts a depth-3 surreal bound for any open problem whose archimedean reading involves weight-3 Goncharov periods (multiple zeta values $\zeta(3), \zeta(2,1)$), such as Apéry-style irrationality questions (Zagier 1986).

We relate this to graded Titchmarsh. Mikusiński passes from $C[0,\infty)$ to its field of fractions via Titchmarsh's no-zero-divisor theorem. The graded analog asks at which iterated-integral depth the $*_q$-product on $\mathcal{H}_q$ first acquires zero divisors. Each surreal-bound remark is an obstruction to inverting a depth-$n$ element, representing exactly the obstruction Mikusiński removes by passing to fractions. The four bounds are instances of graded Titchmarsh failure, each occurring at its characteristic depth.

This reframes existing content under a single rubric. The novel mathematical content resides in [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) and its discharge targets.
<!-- FILE_END: surreal-bounds-graded-mikusinski.md -->

<!-- FILE_START: millennium-unification.md -->
Six classical-limit problems tackled by the QOU framework (the Riemann hypothesis, 3D Navier--Stokes regularity, Collatz, P vs NP, Birch--Swinnerton-Dyer, and the Yang--Mills mass gap) reduce to a single surreal inequality between the cost of a standard-real deviation and the mass-gap infinitesimal. The adelic--Tate factorisation provides the local-global refinement.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). From [surreal rate calculus](#prop:surreal-rate-calculus), we recall:

$$
\Delta_q \asymp \varepsilon^3 \qquad (\text{mass-gap dissipation, positive infinitesimal}),
$$

$$
\Omega_q \asymp \varepsilon^{-1} \qquad (\text{Reeb-period budget, positive transfinite}).
$$

Each problem identifies a drift $\delta$ that measures the standard-real deviation from the classical stable configuration. The [surreal squeeze](#lem:surreal-squeeze) delivers the identical inequality:

$$
\delta^2 \cdot \Omega_q > \Delta_q \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Expanding $\Omega_q \asymp \varepsilon^{-1}$ and $\Delta_q \asymp \varepsilon^3$: for every standard real $\delta > 0$, $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$.

See [Table 1](#tbl:millennium-unification-table1-data).

The first three rows are unconditional surreal translations of existing QOU propositions ([collapse of the quantum gap](#thm:quantum-gap-collapse), blowup as Yekutieli lifting obstruction, [$q$-Collatz](#conj:q-collatz)). The fourth row is conditional on [P vs NP in the QOU](#conj:p-vs-np-qou). The fifth row is conditional on [$q$-BSD](#conj:q-birch-swinnerton-dyer); the adelic refinement ([adelic--Tate surreal squeeze](#rem:adelic-tate-squeeze)) localises this row at each prime. The sixth row is unconditional once the QOU substrate is posited: the mass gap is a categorical invariant of $\mathbf{C}$ with $\ordw(\Delta_q) = -3$, and Yang--Mills on $\mathbb{R}^4$ is the standard part of the $q$-deformation.

The mass-gap scaling $\Delta_q \asymp \varepsilon^3$ is a fixed structural invariant of the rigid :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$. It remains constant across problems. The Reeb-period scaling $\Omega_q \asymp \varepsilon^{-1}$ is similarly a fixed structural invariant of the Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb-derivation)). The content of each millennium problem resides in identifying the problem-specific drift $\delta$ and translating the classical statement into the vanishing of this drift. Once $\delta$ is identified, the squeeze $\delta^2 / \varepsilon > \varepsilon^3$ closes the argument uniformly.

The six millennium problems are not independent questions but six instances of a single substrate-stability requirement: the observable universe contains only classical-limit configurations where no standard-real drift absorbs more substrate energy than the mass gap dissipates. The Riemann hypothesis is the spectral instance, Navier--Stokes is the hydrodynamic instance, Collatz is the arithmetic instance, P vs NP is the complexity instance, BSD is the elliptic-curve instance, and Yang--Mills is the gauge-theory instance. The adelic--Tate framework ([adelic--Tate surreal squeeze](#rem:adelic-tate-squeeze)) localises each instance at every prime, rendering the squeeze strictly local-global.

The $\omega$-adic form of each squeeze is registered in the [body asymptotics catalog](#rem:body-asymptotics-catalog) under the $\ordw$-entry of the corresponding body block ([Big-O via $\ordw$](#rem:conway-normal-form)). We can read these remarks in either the "$\delta^2 \cdot \Omega_q > \Delta_q$ in $\mathbb{R}(\varepsilon)$" register or the "$\ordw(\text{cost}) > \ordw(\text{budget})$" register. The two are equivalent by the Big-O bridge.
<!-- FILE_END: millennium-unification.md -->
