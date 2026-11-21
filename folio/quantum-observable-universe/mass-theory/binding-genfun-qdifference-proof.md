Write $G(x;q)=\sum_{n\geq 0}B_n x^n$ and, for polynomial $R$,
$R(q,x)=\sum_{j=0}^{d} r_j(q)\,x^{j}$. The coefficient of $x^{n}$ in $G(qx;q)$ is
$q^{n}B_{n}$, and in $R(q,x)G(x;q)$ it is $\sum_{j=0}^{d} r_j B_{n-j}$. Hence

$$
  (q^{n} - r_0)\,B_{n} \;=\; \sum_{j=1}^{d} r_j\,B_{n-j},
$$

and for $q^n \neq r_0$ this solves for $B_n$ in terms of $B_{n-1},\dots,B_{n-d}$
with coefficients $r_j/(q^n - r_0)$, rational in $q$ and $q^n$. A Laurent $R$
shifts the indices but leaves the factor $q^n$ on the $B_n$ coefficient. This is
the standard fact that a $q$-holonomic series has $q$-recursive coefficients; it
fixes every term from $R$ and the first $d$ terms. (An earlier version of this
proof wrote the recurrence with coefficients independent of $n$; the factor
$q^n$ makes them depend on $n$.)

For the Archimedean image, apply $\tau$ at $q=q_0$ and let $q\to q_0$ act on the
shift operator $x\mapsto qx$: the multiplicative $q$-shift degenerates to the
infinitesimal generator $x\,\partial_x$ (the confluent limit of a $q$-difference
operator), so $G(qx;q)=R(q,x)G(x;q)$ passes to a linear differential equation
$x\,\partial_x \widehat{G} = \rho(x)\,\widehat{G}$ on the realised
$\widehat{G}=\tau G$ — the Dirac-type equation. Given the depth-$d$
recurrence, with position-dependent coefficients, the term identity follows;
the existence of $R$ for the binding $G$ is the conjectural input
(carried as a hypothesis). $\qquad\blacksquare$
