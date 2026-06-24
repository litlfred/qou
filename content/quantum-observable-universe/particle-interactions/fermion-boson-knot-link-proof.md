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
**boson**.
$\qquad\blacksquare$
