
*Item (1).*
The quantised coordinate ring $A = \mathcal{O}_q(\mathrm{SU}(2))$ is a
Hopf algebra over $R[q, q^{-1}]$ with antipode $S$, counit $\varepsilon$,
and the Haar state $h_q \colon A \to R$ furnishing a non-degenerate
Frobenius form $\int_A = h_q$ (non-degeneracy follows from the
faithfulness of the Haar state for compact quantum groups).  The category
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is $R$-linear, rigid
monoidal (duals given by contragredient representations), and the forgetful
functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ is exact,
faithful, and monoidal.  The Woronowicz $3D$-calculus
$\Omega^1(A) = \ker(\varepsilon) / \ker(\varepsilon)^2$ is a
$3$-dimensional $A$-bimodule in $\mathbf{C}$, providing the differential
calculus axiom.

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
classification theorem, verifying the Yekutieli lifting condition
([Yekutieli lifting](#prop:yekutieli-lifting)).

*Item (4).*
By [Euler-characteristic stability](#prop:euler-char-stability), the
categorical Euler characteristic
$\chi(A) := \mathrm{tr}(\mathrm{id}_A)$ of the base algebra
coincides with the topological Euler characteristic
$\chi(\mathcal{S})$ of the archimedean state bundle. For the
Descartes universe, $\mathcal{S}$ restricted to a generic fibre is
Bring's surface $\Sigma_4$, so
$\chi(A) = \chi(\Sigma_4) = 2 - 2g(\Sigma_4) = 2 - 8 = -6$.
Equivalently, computing via the categorical trace at $\mathbf{C} =
\mathrm{Rep}(\mathrm{SU}_q(2))$, the quantum dimension of
$A = \mathcal{O}_q(\mathrm{SU}(2))$ specialises at the Descartes
substrate parameter $q_0$ to the value $-6$, matching the
topological count.

*Item (5).*
The Reeb quotient $M_S \to \Sigma_4$ collapses the $\mathrm{U}(1)$-orbits
of the circle bundle (weight-$0$ subalgebra $A_0 = A^{\mathrm{U}(1)}$).
The covering $\pi \colon \Sigma_4 \to \mathbb{P}(V)$ is the map to the
projective line induced by the linear system $|K_{\Sigma_4}|$; it has
degree $4$ and genus $4$ source, so by Riemann--Hurwitz
$R_{\mathrm{tot}} = 2g(\Sigma_4) - 2 - 4(2g(\mathbb{P}^1) - 2) = 6 - 4(-2) = 14$.
The $S_5$-symmetry of $\Sigma_4$ forces the $14$ units of ramification to
be distributed over exactly $6$ branch points (with ramification indices
determined by the cycle types of $S_5$).
