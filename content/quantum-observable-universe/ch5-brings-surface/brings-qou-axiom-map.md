We record how each axiom of a quantum observable universe
([Definition](#def:quantum-observable-universe)) is realised on Bring's
surface.

**(i) Non-degeneracy.**
The Frobenius form $\lambda = h_q$ is the Haar state on
$A = \mathcal{O}_q(\mathrm{SU}(2))$.  Faithfulness of $h_q$ for compact
quantum groups gives the isomorphism
$A \xrightarrow{\;\sim\;} A^{\vee}$.  The antipode $S$ and $h_q$
together define the dagger $f^{\dagger} = h_q \circ \mu(S(f) \otimes -)$,
which is positive-definite
([Definition](#def:positive-definite-dagger)) because the Haar state
satisfies $h_q(a^* a) > 0$ for $a \neq 0$.

**(ii) Observability.**
The adjoint representation decomposes as
$\mathrm{Ad}(A) \cong V_1 \oplus V_2 \oplus \cdots$ with no spin-$0$
summand, so $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$ by the
quantum Schur lemma.  Geometrically, this is the statement that
Bring's surface has no global holomorphic vector field
(it has genus $g = 4 > 1$).

**(iii) Categorical volume constraint.**
The fundamental object $V$ of
$\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ has categorical
dimension $2$.  In the archimedean realisation, $V$ is the rank-$2$
defining representation carried by the state bundle fibre
$E_p \cong \mathbb{C}^2$ ([Remark](#rem:brings-qou-4tuple), item 3).
The non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$
is instantiated by the Levi form
$L_\theta = -i\,d\theta|_{H \times H}$
([Remark](#rem:archimedean-realisations)): because $L_\theta$ is
alternating and non-degenerate on the rank-$4$ real distribution
$H = \ker\theta$, it furnishes the symplectic pairing that makes $V$
self-dual and forces $\det(g_V) = 1$, selecting $\mathrm{SU}(2)$ over
$\mathrm{GL}(2)$.  In the spectral coordinates
([Remark](#rem:lagrange-resolvents)), this constraint appears as the
Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$, which is the $\mathrm{SL}(2)$
Plucker relation for $\Lambda^2 V$.  The top-degree extension to the
full chiral fibre is the spectral volume
constraint; see
[Remark](#rem:seiberg-witten) for the explicit symplectic
form and its relation to $\epsilon$.
