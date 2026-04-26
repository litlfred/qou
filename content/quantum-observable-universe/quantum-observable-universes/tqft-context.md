The axioms of
[quantum universe](#def:quantum-universe)
and [quantum observable universe](#def:quantum-observable-universe) are grounded in the algebraic
framework of topological quantum field theory (TQFT).

*Frobenius--Hopf objects and 2d TQFT.*
A commutative Frobenius algebra over $R$ is equivalent to a
$2$-dimensional TQFT
$Z \colon \mathbf{2Cob} \to R\text{-}\mathrm{Mod}$
\cite{kock2004, atiyah1988}. The Frobenius--Hopf object $A$ in
[quantum universe](#def:quantum-universe) carries both the Frobenius structure
(encoding the $2$d cobordism data: the product $\mu$ corresponds to a
pair-of-pants cobordism, the Frobenius form $\int_A$ to a cap) and a
Hopf structure (encoding the quantum-group symmetry that extends the theory
to three dimensions). Concretely, a $2$d TQFT assigns to
the circle $S^1$ a Frobenius algebra $A$ and to each cobordism
$\Sigma \colon S^1 \sqcup \cdots \to S^1 \sqcup \cdots$ a linear map
built from $\mu$, $\Delta_\mu$, $\eta$, and $\int_A$. The Hopf
structure $(\Delta, \varepsilon, S)$ equips $A$ with the additional data
needed for three-dimensional and extended TQFTs
\cite{turaev2010, witten1988}.

*The observability condition as a categorical contact condition.*
In the TQFT setting, the condition
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def:quantum-observable-universe)) is the categorical
analogue of the *contact condition* (maximal non-integrability).
A non-zero morphism $\mathbf{1} \to \mathrm{Ad}(A)$ would give a
global invariant section of the adjoint object --- the categorical
counterpart of a nowhere-vanishing section of the adjoint bundle --- and
would force the TQFT to decompose into a direct sum of
lower-dimensional theories. Requiring
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ therefore ensures:

1. *irreducibility*: the associated $3$-dimensional TQFT
   (Chern--Simons type, with gauge datum $A$ and quantum
   parameter $q$) does not split as a direct sum;
2. *non-degeneracy across cobordisms*: the TQFT pairing on
   state spaces assigned to surfaces is non-degenerate
   \cite{freed2010};
3. *full dualisability*: in the sense of the cobordism
   hypothesis \cite{baez1995, lurie2009}, the object $A$ is
   fully dualisable in the relevant Morita higher category, so the
   TQFT extends to a fully local (extended) field theory.

In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), this categorical
condition reduces to
$H^0(M, \mathrm{Ad}(P)) = 0$ --- the classical requirement that the
instanton connection admits no infinitesimal automorphisms, which is the
gauge-theoretic manifestation of the contact (maximally non-integrable)
geometry of $(M, \varTheta)$.
