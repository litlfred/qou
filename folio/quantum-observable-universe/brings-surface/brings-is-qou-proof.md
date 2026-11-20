*Item (1).*
The quantised coordinate ring $A = \mathcal{O}_q(\mathrm{SU}(2))$ is a
Hopf algebra over $R[q, q^{-1}]$ with antipode $S$, counit $\varepsilon$,
and the Haar state $h_q \colon A \to R$ furnishing a non-degenerate
Frobenius form $\int_A = h_q$ (non-degeneracy follows from the
faithfulness of the Haar state for compact quantum groups).  The category
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is $R$-linear, rigid
monoidal (duals given by contragredient representations), and the forgetful
functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ is exact,
faithful, and monoidal.  The Woronowicz left-covariant $3D$ differential
calculus \cite{woronowicz1987-twisted-su2}
$\Omega^1(A) = \ker(\varepsilon) / \ker(\varepsilon)^2$ is a
$3$-dimensional $A$-bimodule in $\mathbf{C}$, providing the differential
calculus axiom; the left-covariant (not bi-covariant) $3D$
calculus of \cite{woronowicz1987-twisted-su2} is used throughout.

*Item (2).*
The adjoint representation $\mathrm{Ad}(A)$ decomposes under
$\mathrm{SU}_q(2)$ into irreducible representations of spin $j \geq 1$
(the spin-$0$ component vanishes because
$\mathrm{Ad} \cong V_1 \oplus V_2 \oplus \cdots$ with no trivial
summand).  Therefore $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by
the quantum Schur lemma.

*Item (3).*
By [jet prolongation](#prop:jet-prolongation), $J^1(A)$ is Frobenius--Hopf, so
the brane tower $\{A_n\}$ is well-defined.  Each transition
$A_n \hookrightarrow A_{n+1}$ gives a central extension of gerbes banded by
the centre $\mathcal{B} = Z(\mathrm{Aut}(A_n))$.  The obstruction class
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ exists by the standard gerbe
classification theorem, verifying the Quantum lifting condition
([quantum lifting](#prop:yekutieli-lifting)).

*Item (4).*
The categorical Euler characteristic equals $-6$ on Bring's surface
by ([Bring Euler-characteristic computation](#lem:brings-euler-characteristic)).

*Item (5).*
The canonical-system covering $\pi \colon \Sigma_4 \to \mathbb{P}(V)$
has degree $4$, genus $4$ source, and total ramification
$R_{\mathrm{tot}} = 14$ over exactly $6$ branch points by
([Riemann--Hurwitz for $\Sigma_4 \to \mathbb{P}(V)$](#lem:brings-riemann-hurwitz)).
$\square$
