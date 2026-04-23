**Residual conjecture (shrunk form).**
In a strictly commutative QOU
([def:commutative-qou](#def:commutative-qou)), the base manifold $X$
carrying the commutative-limit observables satisfies

*(i)*  $X$ is hyperelliptic --- there exists a degree-$2$ morphism
$\pi \colon X \to \mathbb{P}^1$ with involution $\iota$;

*(ii)* $X$ admits a faithful $\mathbb{Z}_5$-automorphism $\phi$
commuting with $\iota$, where the $\mathbb{Z}_5$ is identified with
the Sylow-5 subgroup of the $S_5$ automorphism group of
[Bring's surface](#def:brings-surface).

**What follows from this automatically.**  Given (i)+(ii) and the
minimal-genus requirement, the classification theorem
([thm:hyperelliptic-z5-classification](#thm:hyperelliptic-z5-classification))
shows that $X$ is uniquely determined: $g(X) = 2$ and
$X \cong \mathcal{X}_5 \colon y^2 = x^5 - 1$
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)).  Every
quantitative consequence --- the Seifert bound
([conj:torus-knot-seifert-bound](#conj:torus-knot-seifert-bound)),
the single $\mathrm{U}(1)$ phase tube
([rem:u1-phase-tube](#rem:u1-phase-tube)), the weight identification
to Bring
([prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification))
--- is downstream of the theorem and therefore entirely determined
by (i)+(ii).

**Why this stays a conjecture.**  Neither (i) nor (ii) is derivable
from `def:commutative-qou` alone: the Tannakian reconstruction
$\mathrm{Rep}(\mathrm{SU}(2)) \leadsto \mathrm{SU}(2)$ recovers the
classical gauge group but does not pin geometric data on a base
manifold.  Each condition is an additional structural hypothesis,
testable by its consequences rather than a theorem of the QOU axioms.
A probe of each is given in
[rem:residual-conjecture-probe](#rem:residual-conjecture-probe).

**Contrast with the original overreach.**  An earlier draft claimed
that commutativity *forces* the base to $g = 2$ via a cohomological
argument in $H^2(X, \mathcal{T}_X)$.  That argument is vacuous on a
Riemann surface (where $H^2$ of every coherent sheaf vanishes), and
the provable content is what remains after the vacuity is stripped:
given (i)+(ii), minimality picks out $\mathcal{X}_5$.  The forcing
has been replaced with a classification.
