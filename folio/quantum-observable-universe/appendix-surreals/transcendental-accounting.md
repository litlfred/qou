**Remark (transcendental-accounting ledger — every period in the paper, indexed by Goncharov depth).**

This is the dual ledger to [The algebraic core of QOU lifts to any real-closed field](#rem:algebraic-core-survives). That ledger enumerates the algebra that survives the archimedean wall; this one enumerates the transcendentals that appear on the other side. This section records which periods appear, where, how they relate, and whether their post-archimedean relations are forced by pre-archimedean $q$-rational structure or are archimedean accidents.

A relation $R(\alpha_1, \ldots, \alpha_m) = 0$ in $\mathbb{Z}[q^{\pm 1}]$ on the algebraic side survives under the archimedean realization functor $\tau_{\mathrm{arch}}$ if and only if it is a $q$-polynomial identity. A relation that holds only among the archimedean values $\tau_{\mathrm{arch}}(\alpha_i) \in \mathbb{R}$ but not among the $\alpha_i \in \mathbb{Z}[q^{\pm 1}]$ is an archimedean accident. The 5-term Bloch–Wigner relation among hyperbolic volumes is a typical example.

The graded-Mikusiński correspondence ([GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence)) predicts the origin of each relation by depth. The table below operationalises this for every period in the QOU paper.

See [Table](#tbl:transcendental-accounting-table-data).

The table makes two structural facts visible:

**Fact 1: depth-2 ceiling for hyperbolic 3-mfd volumes.**
Every hyperbolic 3-manifold volume in the paper occurs at depth 2 (one $\mathrm{Li}_2$ factor). The Bloch–Wigner formula $\mathrm{Vol}(M) = \sum_i D(z_i)$ over an ideal-tetrahedron triangulation forces this. Escaping depth 2 requires a different invariant: $\mathrm{CS}$, hyperbolic 4-manifolds, or the trilogarithm at algebraic points (the `bring-trilog-zeta5` route).

**Fact 2: pre-archimedean $q$-rational relations imply post-archimedean equalities.**
For any two Bring-embeddable knots $K, K'$, if $J_K(q) = J_{K'}(q)$ in $\mathbb{Z}[q^{\pm 1}]$, then $\mathrm{Vol}(K) = \mathrm{Vol}(K')$. The volume $\mathrm{Vol}$ is computed from $J_K^{(N)}$ via a limit depending only on the polynomial. Whether this implication is vacuous (whether there are no Jones-coincident pairs among Bring-embeddable knots) remains open ([Exhaustiveness of the QOU knots in the Descartes space (open)](#rem:knot-exhaustiveness) Question 3). A single Jones-coincident pair yields a non-trivial post-archimedean equality forced by $q$-rational structure—exactly the wall-crossing prediction the correspondence makes explicit.

**Non-surviving relations: archimedean accidents.**
The 5-term Bloch–Wigner relation

$$
D(x) + D(y) + D\!\left(\tfrac{1-x}{1-xy}\right) + D(1 - xy) + D\!\left(\tfrac{1-y}{1-xy}\right) = 0
$$

holds among hyperbolic volumes after $\tau_{\mathrm{arch}}$ but is not a $\mathbb{Q}(q)$-polynomial identity on the pre-archimedean side. It is an archimedean accident at depth 2: a relation in $\mathcal{P}_2 / \mathcal{P}_1$ with no $q$-polynomial witness.

Similar wall-crossing accidents occur at depth 3:
- Goncharov's 22-term relation for $\mathrm{Li}_3$ at 5th roots.
- Euler's 1775 identity $\zeta(2,1) = \zeta(3)$ (an accident from the algebraic side, since the multiple zeta value $\zeta(2,1)$ is a separate iterated integral that evaluates to the single zeta).

**Open question: post-archimedean structure forced by Bring's $S_5$.**
Because Bring's curve has $S_5$ symmetry, the cyclotomic field $\mathbb{Q}(\zeta_5)$ acts on the Bring-natural depth-3 grouplikes. The Galois action $\sigma_a \colon \zeta_5 \mapsto \zeta_5^a$ for $\gcd(a, 5) = 1$ permutes:

$$
\{\mathrm{Li}_3(\zeta_5),\, \mathrm{Li}_3(\zeta_5^2),\, \mathrm{Li}_3(\zeta_5^3),\, \mathrm{Li}_3(\zeta_5^4)\}.
$$

The orbit-sum identity for the trilogarithm over the fifth roots of unity, verified numerically, is the Galois-invariant trace of this $S_5$-action. The Galois-non-invariant components—individual $\mathrm{Li}_3(\zeta_5^k)$ values—give a 4-dimensional $\mathbb{Q}$-vector space of depth-3 periods on which $S_5$ acts irreducibly. These are the depth-3 Bring-natural transcendentals. Their post-archimedean structure (linear relations over $\overline{\mathbb{Q}}$) is governed by the motivic Galois group, not by the $q$-rational pre-image. This gives a concrete instance of post-archimedean structure not visible at the $q$-polynomial level.
