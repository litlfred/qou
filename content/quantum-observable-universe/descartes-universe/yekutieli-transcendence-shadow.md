The [quantum characteristic classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ obstruct lifting at every
level of the [cosimplicial crossed
groupoid](#prop:cosimplicial-crossed-groupoid).  The non-vanishing
$\kappa_n \neq 0$ for all $n$ means the brane tower never collapses to
finite height ([Yekutieli lifting](#prop:yekutieli-lifting)).

Each hyperbolic volume $\mathrm{Vol}(K)$ arises as the classical
($q \to 1$) limit of the quantum dilogarithm sum across the brane
tower.  A polynomial relation
$P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)) = 0$ over $\mathbb{Q}[q, q^{-1}]$ would
impose an algebraic constraint on the Chern--Simons invariants of the
three complements $S^3 \setminus 4_1$, $S^3 \setminus 5_2$, and
$S^3 \setminus \mathcal{B}_3$.  Via the Chern--Simons/volume
correspondence (the baseline-equals-volume identity in the
Archimedean mass formula), this would force the holonomy contributions
at different tower levels to satisfy a compatible system of constraints
that "close up" after finitely many levels.

But the cosimplicial structure theorem guarantees that the tower is
genuinely infinite: the obstruction classes $\kappa_n$ never
simultaneously vanish, and the crossed groupoid does not degenerate.
This is precisely
[motivic perpetual obstruction](#conj:motivic-perpetual-obstruction):
the motivic Galois character of the substrate is non-trivial at
every finite place $p \nmid \chi(A)$, so $\kappa_n$ — which is the
HKR image of that character at level $n$
([Hochschild–Kummer connection](#rem:hochschild-kummer-connection)) —
cannot vanish at the corresponding cyclotomic levels. Thus the
algebraic independence of the volumes is the *transcendence shadow*
of the non-vanishing motivic Galois character — the tower never
terminates, so no polynomial envelope can hold among the volumes
it produces.

Making this heuristic rigorous requires controlling the arithmetic of
the quantum dilogarithm at every tower level.  This would likely need
new results in the spirit of Nesterenko's theorem on algebraic
independence of values of $E$-functions, adapted to quantum
dilogarithm series and the cosimplicial filtration of
$\mathrm{SU}_q(2)$-gerbes.
