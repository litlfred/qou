We record how each axiom of a
([quantum observable universe](#def:quantum-observable-universe)) is realised on Bring's
surface.

**(i) Non-degeneracy.**
The Frobenius form $\int_A = h_q$ is the Haar state on
$A = \mathcal{O}_q(\mathrm{SU}(2))$.  Faithfulness of $h_q$ for compact
quantum groups gives the isomorphism
$A \xrightarrow{ \sim } A^{\vee}$.  The antipode $S$ and $h_q$
together define the dagger $f^{\dagger} = h_q \circ \mu(S(f) \otimes -)$,
which is positive-definite
([positive definite dagger](#prop:positive-definite-dagger)) because the Haar state
satisfies $h_q(a^* a) > 0$ for $a \neq 0$.

**(ii) Observability.**
The adjoint representation decomposes as
$\mathrm{Ad}(A) \cong V_1 \oplus V_2 \oplus \cdots$ with no spin-$0$
summand, so $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by the
quantum Schur lemma.  Geometrically, this is the statement that
Bring's surface has no global holomorphic vector field
(it has genus $g = 4 > 1$).

**(iii) Categorical volume constraint.**
The fundamental object $V$ of
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ has categorical
dimension $2$.  In the archimedean realisation, $V$ is the rank-$2$
defining representation carried by the state bundle fibre
$\mathcal{S}_p \cong \mathbb{C}^2$ ([Bring's QOU 4-tuple](#rem:brings-qou-4tuple), item 3).
The non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$
is instantiated by the Levi form
$L_\varTheta = -id\varTheta|_{H \times H}$
([archimedean realisations](#rem:archimedean-realisations)): because $L_\varTheta$ is
alternating and non-degenerate on the rank-$4$ real distribution
$H = \ker\varTheta$, it furnishes the symplectic pairing that makes $V$
self-dual and forces $\det(g_V) = 1$, selecting $\mathrm{SU}(2)$ over
$\mathrm{GL}(2)$.  In the spectral coordinates
([Lagrange resolvents](#rem:lagrange-resolvents)), this constraint appears as the
Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$, which is the $\mathrm{SL}(2)$
Plucker relation for $\Lambda^2 V$.  The top-degree extension to the
full color fibre is the spectral volume
constraint; see
[Seiberg--Witten](#rem:seiberg-witten) for the explicit symplectic
form and its relation to $\epsilon$.
