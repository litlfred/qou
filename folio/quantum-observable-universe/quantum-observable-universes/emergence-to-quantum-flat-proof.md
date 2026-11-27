The argument proceeds in three steps.

*Step 1: The volume constraint determines the Lie algebra.*
The categorical volume constraint provides a non-degenerate epimorphism
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$. Under the forgetful functor
$\tau$, this endows the rank-$2$ module $\tau(V)$ with a
$q$-antisymmetric pairing whose invariance algebra is
$\mathfrak{su}_q(2)$. This is the Lie algebra of the reconstructed
group $G_q$, and hence of the identity crossed module
$\partial \colon G_q \xrightarrow{\mathrm{id}} G_q$ defining the strict inner-automorphism $2$-group
$\mathrm{INN}(G_q)$ under the crossed-module classification of John C. Baez and Aaron D. Lauda \cite{baez2004}.

*Step 2: The determinant-one condition descends to the
2-form datum.*
For a general crossed module $\partial \colon H \to G_q$, vanishing fake curvature \cite[§4]{baez-schreiber2007} imposes $F_A = \mathrm{d}\partial(B)$; for $\mathrm{INN}(G_q)$ ($\partial = \mathrm{id}_{G_q}$), a $2$-connection $(A, B)$ takes values in
$\mathfrak{g}_q = \mathfrak{su}_q(2)$ and quantum
flatness sets $B = F_A$ directly, so $B$ inherits the
tracelessness forced by the determinant constraint
$\det(g_V) = 1$ of [$\mathrm{SU}(2)$ emergence](#thm:su2-emergence): $B$ is
$\mathrm{Ad}(P)$-valued with $\mathrm{tr}B = 0$, i.e.
$\mathfrak{su}_q(2)$-valued rather than $\mathfrak{gl}_q(2)$-valued.

*Step 3: Simplicity plus :refterm[quantum flatness]{#quantum-flatness} gives the instanton
equation.*
Imposing the simplicity constraint
$B \in \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P))$
([self-dual 2-group](#rem:self-dual-2group)) and combining with $F_A = B$
yields $F_A = F_A^+$, hence $F_A^- = 0$. Infinitesimally, the equivalence between vanishing fake curvature and $F_A^- = 0$ under simplicity holds for any crossed module whose Lie-algebra differential $\mathrm{d}\partial \colon \mathfrak{h} \to \mathfrak{g}_q$ is an isomorphism; selecting $\mathrm{INN}(G_q)$ uniquely among strict $2$-groups over $G_q$ requires in addition group-level faithfulness $\ker(\partial) = 1$ and surjectivity $\mathrm{coker}(\partial) = 1$ so no discrete central kernel or outer quotient remains. Step 1 guarantees the
structure group is $\mathrm{SU}_q(2)$---not a quotient of
$\mathrm{GL}_q(2)$---so the instanton moduli space carries the
gauge symmetry dictated by the categorical axioms.
