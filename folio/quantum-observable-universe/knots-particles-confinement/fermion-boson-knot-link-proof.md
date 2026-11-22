*Proof.*
The torus knot $T(2,n)$ on Bring's surface wraps $2$ times around the meridian and $n$ times around the longitude. The number of connected components is $\gcd(2, n)$.

**Case $n$ odd** ($\gcd(2,n) = 1$): $T(2,n)$ is a knot with one connected component. This single component winds around the Reeb direction ([categorical Reeb](#def:categorical-reeb)) with nonzero winding number. In the weight decomposition, the vertical projection $\pi_V$ detects this winding: $\pi_V(\alpha) \neq 0$. The particle is a **fermion**.

**Case $n$ even** ($\gcd(2,n) = 2$): $T(2,n)$ is a link with two connected components. Each component winds $1$ time around the meridian and $n/2$ times around the longitude. The two components possess **opposite vertical winding**: one winds $+1$ and the other $-1$ around the Reeb direction. They are related by the fiber adjoint involution. Their vertical projections cancel: $\pi_V(\alpha^{(1)}) + \pi_V(\alpha^{(2)}) = 0$. The total vertical component vanishes. The particle is a **boson**. $\square$

**The T(2,n) particle table.**
See [Table](#tbl:fermion-boson-knot-link-table-data).

**Spin--statistics from topology.**
The spin--statistics theorem (fermions have half-integer spin, bosons have integer spin) becomes a topological statement:

- **Half-integer spin**: A knot (1 component) requires a $4\pi$ rotation to return to its original configuration. The single strand winds through the Reeb flow with an odd winding number. The monodromy of the fiber adjoint involution has order $2$.
- **Integer spin**: A link (2 components) returns to its original configuration after a $2\pi$ rotation. The two strands can be exchanged by the fiber adjoint involution without altering the link type.
