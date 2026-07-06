**Proposition (a fixed-depth recurrence for the prolonged periods exists).**

The prolonged Seiberg--Witten periods $a_D^{(n)} = \varphi(M^n v_0)$ are orbits of
the jet-prolongation operator $M$
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)) acting on the
Gauss--Manin period space $V$ of the SW family over Bring's surface. Since $V$
is **finite-rank** — it is the de Rham cohomology of the family, $\dim V \leq 2g
= 8$ for the genus-$4$ Bring curve — the operator $M$ satisfies its
characteristic polynomial (Cayley--Hamilton):
$M^d = \sum_{j<d} c_j\,M^j$ with $d \leq \operatorname{rank} V$ and $c_j$ the
characteristic-polynomial coefficients. Therefore the operator powers — and
hence the periods — satisfy the depth-$d$ linear recurrence

$$
M^{\,n+d} = \sum_{j<d} c_j\,M^{\,n+j},
\qquad
a_D^{(n+d)} = \sum_{j<d} c_j\,a_D^{(n+j)},
$$

with **$n$-independent** kernel $c$, for every $n$.

This **proves the existence half** of
[`conj:qdifference-kernel-prolongation-symbol`](#conj:qdifference-kernel-prolongation-symbol):
a fixed-depth recurrence on the prolonged periods *necessarily* exists, with
depth bounded by the rank of the Gauss--Manin local system. What remains is the
**identification half** — that $d$ and the kernel $c$ are *exactly* the Bring
Picard--Fuchs operator (so the kernel is the prolongation symbol, not a generic recurrence). That is fixed by computing the SW connection's local monodromy
at the branch points and matching it against the residue weights $a_D^{(n)}$
(the consistency test of the keystone workplan, gated on the per-knot weights at
$n = 2, 3$).

The operator recurrence is verified sorry-free
([`QOU.Mass.prolongation_fixed_depth_recurrence`](#prop:prolonged-periods-fixed-depth));
the finite-rank premise (Gauss--Manin / Cayley--Hamilton) is the cited
structural input, and the scalar period recurrence follows by applying the
linear functional $\varphi(\,\cdot\,v_0)$ to both sides.
