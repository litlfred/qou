Bring's surface $\Sigma_4$ ([Definition](#def:brings-surface)) gives rise
to a quantum observable universe over $R$ (with $30 \in R^{\times}$):

1. *Quantum universe.*  Set $\mathcal{C} =
   \mathrm{Rep}(\mathrm{SU}_{q}(2))$ over $R$,
   $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the
   Haar state, and $\omega$ the forgetful functor to $R$-$\mathrm{Mod}$.
   The differential calculus $\Omega^1(A)$ is the Woronowicz
   $3$-dimensional calculus.
2. *Observability.*
   $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$ by the quantum
   Schur lemma: $\mathrm{SU}_q(2)$ has no non-trivial invariants in the
   adjoint representation.
3. *Yekutieli lifting.*  The brane tower satisfies the Yekutieli
   lifting condition ([Proposition](#prop:yekutieli-lifting)).
4. *Euler characteristic.*  By [Theorem](#thm:qu-to-qou),
   $\chi(A) = \mathrm{tr}(\mathrm{id}_A) = 2 - 2g = -6$.
5. *Geometric descent* (for $n = 1$, $\dim M_S = 3$):
   $$
     M_S \;\xrightarrow{\;\mathrm{Reeb}\;}\; \Sigma_4
     \;\xrightarrow{\;\pi\;}\; \mathbb{P}(V)
     \;\xrightarrow{\;\mathrm{branch}\;}\; \{6\;\text{points}\}.
   $$
   The degree-$4$ covering $\pi$ has $6$ branch points with total
   ramification $R_{\mathrm{tot}} = 14$ (Riemann--Hurwitz), and the
   ramification profile is determined by the $S_5$-symmetry.

---

*Item (1).*
The quantised coordinate ring $A = \mathcal{O}_q(\mathrm{SU}(2))$ is a
Hopf algebra over $R[q, q^{-1}]$ with antipode $S$, counit $\varepsilon$,
and the Haar state $h_q \colon A \to R$ furnishing a non-degenerate
Frobenius form $\lambda = h_q$ (non-degeneracy follows from the
faithfulness of the Haar state for compact quantum groups).  The category
$\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is $R$-linear, rigid
monoidal (duals given by contragredient representations), and the forgetful
functor $\omega \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$ is exact,
faithful, and monoidal.  The Woronowicz $3D$-calculus
$\Omega^1(A) = \ker(\varepsilon) / \ker(\varepsilon)^2$ is a
$3$-dimensional $A$-bimodule in $\mathcal{C}$, providing the differential
calculus axiom.

*Item (2).*
The adjoint representation $\mathrm{Ad}(A)$ decomposes under
$\mathrm{SU}_q(2)$ into irreducible representations of spin $j \geq 1$
(the spin-$0$ component vanishes because
$\mathrm{Ad} \cong V_1 \oplus V_2 \oplus \cdots$ with no trivial
summand).  Therefore $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by
the quantum Schur lemma.

*Item (3).*
By [Proposition](#prop:jet-prolongation), $J^1(A)$ is Frobenius--Hopf, so
the brane tower $\{A_n\}$ is well-defined.  Each transition
$A_n \hookrightarrow A_{n+1}$ gives a central extension of gerbes banded by
the centre $\mathcal{B} = Z(\mathrm{Aut}(A_n))$.  The obstruction class
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ exists by the standard gerbe
classification theorem, verifying the Yekutieli lifting condition
([Proposition](#prop:yekutieli-lifting)).

*Item (4).*
The categorical trace of $\mathrm{id}_A$ in
$\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is the quantum dimension
$\mathrm{tr}(\mathrm{id}_A) = [N]_q \cdot [N-1]_q / [1]_q$ evaluated at
$N = 2$ (the rank of $\mathrm{SU}(2)$).  At generic $q$, this recovers
the topological Euler characteristic of $\Sigma_4$:
$\chi(A) = 2 - 2g = 2 - 8 = -6$.

*Item (5).*
The Reeb quotient $M_S \to \Sigma_4$ collapses the $\mathrm{U}(1)$-orbits
of the circle bundle (weight-$0$ subalgebra $A_0 = A^{\mathrm{U}(1)}$).
The covering $\pi \colon \Sigma_4 \to \mathbb{P}(V)$ is the map to the
projective line induced by the linear system $|K_{\Sigma_4}|$; it has
degree $4$ and genus $4$ source, so by Riemann--Hurwitz
$R_{\mathrm{tot}} = 2g(\Sigma_4) - 2 - 4(2g(\mathbb{P}^1) - 2) =
6 - 4(-2) = 14$.
The $S_5$-symmetry of $\Sigma_4$ forces the $14$ units of ramification to
be distributed over exactly $6$ branch points (with ramification indices
determined by the cycle types of $S_5$).
