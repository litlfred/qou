Write $G(x;q)=\sum_{n\geq 0}B_n x^n$ and $R(q,x)=\sum_{j} r_j(q)\,x^{j}$ with
$j$ ranging over a window of width $d$. Comparing the coefficient of $x^{n+d}$
on both sides of $G(qx;q)=R(q,x)G(x;q)$, the left side contributes
$q^{n+d}B_{n+d}$ and the right side a finite $\mathbb{Q}(q)$-linear combination
of $B_{n},\dots,B_{n+d}$. Solving for $B_{n+d}$ (the coefficient $r$ of the top
power is a unit in $\mathbb{Q}(q)$) yields the depth-$d$ recurrence
$B_{n+d}=\sum_{j=0}^{d-1}a_j(q)\,B_{n+j}$ with $a_j$ rational in $q$ and the
$r_j$. This is the standard fact that a $q$-holonomic series has $P$-recursive
coefficients; it fixes every term — and hence the growth law $\rho\cdot A$ —
from the first $d$ terms and $R$.

For the Archimedean image, apply $\tau$ at $q=q_0$ and let $q\to q_0$ act on the
shift operator $x\mapsto qx$: the multiplicative $q$-shift degenerates to the
infinitesimal generator $x\,\partial_x$ (the confluent limit of a $q$-difference
operator), so $G(qx;q)=R(q,x)G(x;q)$ passes to a linear differential equation
$x\,\partial_x \widehat{G} = \rho(x)\,\widehat{G}$ on the realised
$\widehat{G}=\tau G$ — the Dirac-type equation. The Lean witness
[`QOU.Mass.binding_qdifference_recurrence`](#prop:binding-genfun-qdifference)
packages the depth-$d$ recurrence as a structure and extracts the term
identity; the existence of $R$ for the binding $G$ is the conjectural input
(carried as the structure hypothesis). $\qquad\blacksquare$
