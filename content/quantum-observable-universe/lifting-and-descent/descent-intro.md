The :refterm[descent]{#descent} machinery connects the infinite brane tower to finite-dimensional
geometry.  Given a quantum observable universe $(\mathbf{C}, A, \tau)$ with
brane tower $\{A_n\}_{n \geq 0}$
([recursive brane tower](#def\:recursive-brane-tower)), the :refterm[descent]{#descent} lemma
([:refterm[descent]{#descent} lemma](#lem\:descent)) shows that each level $A_n$ inherits the
full QOU structure from $A$.  The :refterm[descent]{#descent} involution
([:refterm[descent]{#descent} involution](#def\:descent-involution)) then splits each $A_n$ into
eigenspaces whose direct limit recovers the physical algebra.  This section
develops the :refterm[descent]{#descent} involution, its eigenspace decomposition, and the
mass-decomposition formula that results.

The arc proceeds in three movements.  We first record the existence
and uniqueness of the descent involution at each tower level — the
involutive splitting is forced by the fixed point of the brane
recursion.  We then exhibit the eigenspace decomposition
$A_n = A_n^+ \oplus A_n^-$ and identify the $+$-eigenspace as the
*physical* part of the algebra: the part that survives the
classical limit and feeds the mass observables.  The closing blocks
of the section assemble these per-level decompositions into the
mass-decomposition formula, which the next section's cosimplicial
machinery promotes into a genuine higher-categorical structure.
