The balanced dimension sum $S^{\mathrm{bal}}(n; q)$ is the fibre-level
numerator of the classical binding period: at $q = 1$ it specialises to the
involution count $I(n)$, and the body-order period is $I(n)/n$
([Seiberg–Witten period residue sum proposition](#prop:sw-period-residue-sum)). The identity of
[binding period involution statistic proposition](#prop:binding-period-involution-statistic)
therefore locates the open recurrence kernel $R(q, x)$ of
[binding generating-function $q$-difference proposition](#prop:binding-genfun-qdifference) at the
level of a *permutation statistic*: the binding period is the generating
function of involutions by $2\,\mathrm{maj} + \mathrm{content} \circ \mathrm{RSK}$
— a different statistic from the crossing statistic of the $q$-Hermite family.

Two structural consequences follow, both verified exactly.

1. **The kernel is an insertion recursion rather than a finite $q$-difference
   operator.** Splitting the involutions by the fate of the largest letter,
   the fixed-point-insertion weight ratio is non-monomial with growing
   polynomial spread, so the statistic is not Markovian under RSK insertion
   on any fixed finite basis.

2. **The exact kernel object is a descent-set transfer operator.** The
   statistic *is* Markovian on the lifted state space of pairs
   (shape, marked corner row): the level-$k$ step factorises as
   $T_k = A_k + q^{2k} B_k$, where the non-descent block $A$ and the descent
   block $B$ carry only the monomial entries $q^{c}$ with $c$ the content of
   the added cell, the sole level dependence being the scalar $q^{2k}$ on
   $B$. The operator reconstructs the right-hand side exactly, while its
   state space grows without bound (like the corner-marked Young lattice), so
   no fixed-depth $q$-difference projection closes.
