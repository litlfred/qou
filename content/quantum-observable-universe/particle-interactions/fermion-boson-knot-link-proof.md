*Proof.*
The torus knot $T(2,n)$ on the Bring's surface wraps $2$ times
around the meridian and $n$ times around the longitude.  The
number of connected components is $\gcd(2, n)$.

**Case $n$ odd** ($\gcd(2,n) = 1$): $T(2,n)$ is a knot with
one connected component.  This single component winds around
the Reeb direction ([categorical Reeb](#def:categorical-reeb))
with nonzero winding number.  In the weight decomposition, the
vertical projection $\pi_V$ detects this winding:
$\pi_V(\alpha) \neq 0$.  The particle is a **fermion**.

**Case $n$ even** ($\gcd(2,n) = 2$): $T(2,n)$ is a link with
two connected components, each winding $1$ time around the
meridian and $n/2$ times around the longitude.  The two
components have **opposite vertical winding**: one winds $+1$
and the other $-1$ around the Reeb direction (they are related
by the fiber adjoint involution).  Their vertical projections
cancel: $\pi_V(\alpha^{(1)}) + \pi_V(\alpha^{(2)}) = 0$, so
the total vertical component vanishes.  The particle is a
**boson**. $\square$

**The T(2,n) particle table.**

See [Table](#tbl:fermion-boson-knot-link-table-data).

**Spin--statistics from topology.**
The spin--statistics theorem (fermions have half-integer spin,
bosons have integer spin) becomes a topological statement:

- **Half-integer spin**: a knot (1 component) requires a
  $4\pi$ rotation to return to its original configuration.
  The single strand winds through the Reeb flow with an
  odd winding number, and the monodromy of the fiber
  adjoint involution has order $2$ (not $1$).

- **Integer spin**: a link (2 components) returns to its
  original configuration after a $2\pi$ rotation.  The two
  strands can be exchanged by the fiber adjoint involution
  without changing the link type.

**Quarks in this framework.**
Quarks are **not** knots or links in the $T(2,n)$ family.
They are unknots Borromean-linked in the exceptional divisor
([Borromean quark](#conj:borromean-quark)).  The Borromean
link $\mathcal{B}_3$ has **three** components — neither a
knot (1) nor a standard link (2).  Its statistics are
determined by the overall baryon: the proton
$\mathcal{B}_3(u,u,d) \oplus \mathcal{L}_H$ is a composite
fermion because the Borromean structure, when resolved via
the Skein relation, reduces to an odd number of knot
components.
