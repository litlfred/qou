The argument proceeds in three steps.

*Step 1: The volume constraint determines the Lie algebra.*
The categorical volume constraint provides a non-degenerate epimorphism
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$. Under the forgetful functor
$\tau$, this endows the rank-$2$ module $\tau(V)$ with a
$q$-antisymmetric pairing whose invariance algebra is
$\mathfrak{su}_q(2)$. This is the Lie algebra of the reconstructed
group $G_q$, and hence of the crossed module
$\partial \colon G_q \xrightarrow{\mathrm{id}} G_q$ defining
$\mathrm{INN}(G_q)$.

*Step 2: The determinant-one condition descends to the
2-form datum.*
A $2$-connection $(A, B)$ for the principal $2$-bundle of
$\mathrm{INN}(G_q)$ takes values in
$\mathfrak{g}_q = \mathfrak{su}_q(2)$. Quantum
flatness sets $B = F_A$, so $B$ inherits the
tracelessness forced by the determinant constraint
$\det(g_V) = 1$ of [$\mathrm{SU}(2)$ emergence](#thm:su2-emergence): $B$ is
$\mathrm{Ad}(P)$-valued with $\mathrm{tr}B = 0$, i.e.
$\mathfrak{su}_q(2)$-valued rather than $\mathfrak{gl}_q(2)$-valued.

*Step 3: Simplicity plus :refterm[quantum flatness]{#quantum-flatness} gives the instanton
equation.*
Imposing the simplicity constraint
$B \in \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P))$
([self-dual 2-group](#rem:self-dual-2group)) and combining with $F_A = B$
yields $F_A = F_A^+$, hence $F_A^- = 0$. Step 1 guarantees the
structure group is $\mathrm{SU}_q(2)$---not a quotient of
$\mathrm{GL}_q(2)$---so the instanton moduli space carries the
gauge symmetry dictated by the categorical axioms.
