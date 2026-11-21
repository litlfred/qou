---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-008-18-the-relation-with-perturbative-chernsimons-th
section_title: "The relation with perturbative Chern–Simons theory"
section_number: 1.8
pages: 15-17
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.955
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.CS}

Theorem~\ref{thm.2} involves a symmetric matrix with integer entries and a
non-degenerate solution $z$ of the Nahm equations. As such, it looks removed from
perturbative Chern--Simons theory with complex gauge group.
In this subsection, we briefly explain the relation betwee Theorem~\ref{thm.2} and
perturbative complex Chern--Simons theory.

To begin with, Chern--Simons theory
with a complex gauge group (such as $\SL_2(\BC)$) was formulated as a path integral
by Witten~\cite{Witten:complexCS}, following his earlier work on a path integral
with compact gauge group (such as $\mathrm{SU}(2)$)~\cite{Witten:jones}.

However,
there is a crucial difference between complex versus compact Lie groups. The path
integral with compact gauge group satisfies cut-and-paste properties that lead to
its effective computation, and to a combinatorial definition developed by
Reshetikhin--Turaev~\cite{RT:ribbon,Tu:book}.
On the other hand, the path integral with complex
gauge group is lacking cut and paste properties and, to the best of our knowledge,
it is unknown for instance how to compute it for closed 3-manifolds. 

For reasons that are not entirely understood, the partition function of 
Chern--Simons theory with complex gauge group $\SL_2(\BC)$ for manifolds with torus
boundary components conjecturally reduces to a finite-dimensional integral (the so called-state
integral) whose integrand is a product of Faddeev's quantum dilogarithm
functions~\cite{Faddeev}, assembled out of an ideal triangulation of
the manifold. This was the approach taken by
Andersen-Kashaev~\cite{AK, AK-review} and Dimofte~\cite{dimofte-rev}
following prior ideas of~\cite{Hikami,DGLZ}. Focusing for simplicity
on the case of a 3-manifold with a single torus boundary component
(such as the complement of a hyperbolic knot in $S^3$), the
state-integral is a holomorphic function of
$\tau \in \BC'=\BC\setminus (-\infty,0]$.

We now turn to perturbative Chern--Simons theory with complex gauge group
$\SL_2(\BC)$. Using the above mentioned (state-integral) partition function, in
a series of papers the perturbation theory was defined first at $q$ near
$1$~\cite{DG} and then for $q$ near an arbitrary complex root of unity~\cite{DG2}.
This perturbation theory depends on the combinatorics of an ideal triangulation
of a cusped hyperbolic 3-manifold, a solution $z$ of its Neumann--Zagier equations,
as well as some auxillary choices (of a quad of the tetrahedra and of an edge of the
triangulation). These choices lead to a so-called Neumann--Zagier datum, which
is a the upper part $(\boldsymbol{A}|\boldsymbol{B})$ of a symplectic $N \times N$
matrix with integer entries, a vector $\nu \in \BZ^N$, and a solution $z$ of the
Neumann--Zagier equations
\be
\label{NZeqn}
\prod_{j=1}^N z_j^{\boldsymbol{A}_{ij}} (1-\tfrac{1}{z_j})^{\boldsymbol{B}_{ij}}
\= (-1)^{\nu_i}, \qquad i=1,\dots N\,.
\ee
The solution $z$ in turn defines a representation $\pi_1(M) \to \PSL_2(\BC)$ up to
conjugation, which under mild hypotheses can be lifted to a representation $\rho_z$
to $\SL_2(\BC)$. 
Fixing such a Neumann--Zagier datum, the complex Chern--Simons perturbative series
around $\rho_z$ are defined in~\cite{DG,DG2} by formal Gaussian integration, 
and these are none other than the series $\Phi(h)$ of Equation~\eqref{as41} for
the case of the $4_1$ knot, where $\rho_z$ is an $\SL_2(\BC)$ lift of the discrete
faithful $\PSL_2(\BC)$-representation of the $4_1$ knot. 

The symplectic property of $(\boldsymbol{A}|\boldsymbol{B})$ the Neumann--Zagier
matrix implies that when $\boldsymbol{B}$ is invertible over $\BZ$, then
$A=I-\boldsymbol{B}^{-1}\boldsymbol{A}$ is a symmetric $N \times N$ matrix with
integer entries. Moreover, the Neumann--Zagier equations~\eqref{NZeqn} are equivalent
to the Nahm equations~\eqref{zjt=0}, and what's more the perturbative series at
roots of unity defined by formal Gaussian integration \emph{syntactically matches} that
of the corresponding Nahm sum (when $A$ is positive definite) and of the admissible
series for general $A$. This matching is discussed in detail in~\cite{GZ:nahm} and is generalised in Theorem~\ref{thm.1}.

Putting everything together, it follows that Theorem~\ref{thm.2} contains the
asymptotics of complex Chern--Simons theory when a 3-manifold with torus boundary
has an (essential) ideal triangulation and a choice of quad with unimodular matrix
$\boldsymbol{B}$. While such a choice is not known to exist in general, it has
been found for all knots with at most 14 crossings using their
default \texttt{SnapPy} triangulation.
