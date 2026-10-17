---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.813
latex_coverage_ratio: 0.934
---
\label{sec.intro}

This paper concerns the topological invariance of a formal power series associated
to an ideally triangulated 3-manifold $M$ with a torus boundary component~\cite{DG}. 
The series is defined by formal Gaussian integration of a finite dimensional integral
(a so-called ``state-integral'')
and it is expected to coincide to all orders with the asymptotic expansion of
three important topological invariants of 3-manifolds.

The first is the Kashaev invariant of a hyperbolic
knot~\cite{K95}, where Kashaev's famous volume conjecture is refined to an
asymptotic statement to all orders in perturbation theory using the above formal
power series. This was studied in detail in~\cite{GZ:kashaev} based on extensive
numerical computations, but it is only proven for a handful of hyperbolic knots.

The second invariant is the Andersen--Kashaev state integral~\cite{AK}, whose
asymptotic expansion for the simplest hyperbolic $4_1$ knot was shown to agree with
the above series in~\cite[Sec.12]{AK}, and also observed numerically for the
first three simplest hyperbolic knots in~\cite{GZ:qseries}.
The state-integrals of~\cite{AK} are finite-dimensional integrals whose integrand
is a product of Faddeev quantum dilogarithms times an exponential of a quadratic
form, assembled from an ideal triangulation of a 3-manifold with torus boundary
components. Andersen--Kashaev proved that these are topological invariants that
are the partition function of the Teichm\"uller TQFT~\cite{AK,AK:teichmuller},
which is a 3-dimensional version of a quantization of Teichm\"uller
space~\cite{Kashaev:quantization, Fock-Chekhov}. 

A third invariant is the Chern--Simons theory with complex gauge group $\SL_2(\BC)$ .
This theory was introduced by Witten~\cite{Witten:complexCS} and studied
extensively by Gukov~\cite{Gukov:Apoly}. Although Chern--Simons theory with compact
gauge group $\mathrm{SU}(2)$ has an exact nonperturbative definition given by the
so-called Witten--Reshetikhin--Turaev invariant~\cite{Witten:Jones,RT} and a
well--defined perturbation theory involving Feynman diagrams with uni-trivalent
vertices~\cite{AS,AarhusII}, the same is not known for Chern--Simons theory with
complex gauge group $\SL_2(\BC)$. For reasons that are not entirely
understood, the partition function of complex Chern--Simons theory for 3-manifolds
with torus boundary reduces to a finite-dimensional state-integral, as if some
unknown localization principle holds. The corresponding state-integrals were
introduced and studied by Hikami~\cite{Hikami}, Dimofte~\cite{Dimofte:complexCS}
and others~\cite{DGLZ}. Unfortunately, in those works the integration contour
was not pinned down, and this problem was finally dealt with in~\cite{AK}
and, among other things, implied topological invariance of the state-integrals,
which were coined to be the partition function of Teichm\"uller TQFT.
But ignoring the contour of integration, and focusing on a critical point of the
action, which is a solution to a system of polynomial equations, allowed~\cite{DG}
to give a definition of the formal power series that are the main focus of our paper.  
Note, however, that the Feynman diagrams of~\cite{DG} involve stable graphs of
arbitrary valency, a perturbative definition of Chern--Simons theory with complex
gauge groups would involve uni-trivalent graphs. 

The above discussion points out several aspects of these formal power series
and conjectural relations to perturbation theory of complex Chern--Simons
and of Teich\"uller TQFT. Aside from conjectures, this paper concerns
a theorem, the topological invariance of the above formal power series.
  
Let us briefly recall the key ingredients that go into the definition of the
series, and discuss those in detail in later sections. The first ingredient is  
an ideal triangulation $\calT$ with $N$ ideal tetrahedra of a 3-manifold $M$ with
torus boundary. Each tetrahedron has shapes $z \in \BC\setminus\{0,1\}$, $z'=1/(1-z)$
and $z''=1-1/z$ attached to its three pairs of opposite edges, and the shapes
satisfy a system of polynomial equations (so-called ``gluing equations''~\cite{Th} or
Neumann-Zagier equations~\cite{NZ}) determined by the combinatorics
of the triangulation, one for each edge and peripheral curve. After some choices
are made (such as an ordering of the tetrahedra and their edges, a choice of shape
for each tetrahedron, a choice of an edge to remove from the gluing equations, and
a choice of peripheral curve to include), one obtains two matrices $A$ and $B$
with integer entries such that $(A\,|\,B)$ is the upper-half of a symplectic $2N \times
2N$ matrix, as well as a vector $\nu \in \BZ^N$. In addition, we choose a solution
$z=(z_1,\dots,z_N)$ of the gluing equations as well as a flattening $(f,f'')$, i.e.,
an integer solution to the equation $\nu = A f + B f''$. The power series
$\Phi^\Xi(\hbar)$ depends on the tuple $\Xi=(A,B,\nu,z,f,f'')$, which we collectively
call a NZ-datum. 

The next ingredient that goes in the definition of $\Phi^\Xi(\hbar)$ is an
auxiliary formal power series







\be
\label{psih}
  \psi_{\hbar}(x,z)
  \;:=\;
  \exp\bigg(\!-\!\!\sum_{\underset{k+\frac{\ell}{2}>1}{k,\ell\in\BZ_{\geq0}}}
  \frac{B_{k}\,x^{\ell}\,\hbar^{k+\frac{\ell}{2}-1}}{\ell!\,k!}\Li_{2-k-\ell}(z)\bigg)
  \in1+\hbar^{\frac{1}{2}}\BQ[z,(1-z)^{-1}][x]\llbracket\hbar^{\frac{1}{2}}
  \rrbracket\,.
\ee
This series, which differs from the one given in~\cite[Eq. 1.9]{DG} by a factor of
$\exp\big(\frac{1}{12}\hbar-\frac{1}{2}x\hbar^{\frac{1}{2}}\big)$, comes from
the asymptotics of the infinite Pochhammer symbol (also known as the
quantum dilogarithm)
\be
\label{poch}
(x;q)_\infty = \prod_{k=0}^\infty (1-q^k x) = \exp\Big(
-\sum_{n=1}^\infty \frac{x^n}{n(1-q^n)} \Big) \,.
\ee
Explicitly, for complex numbers $x$ and $z$ with $|z|<1$ and
$\Re(\hbar)<0$ we have (see~\cite{Zagier:dilog} and
also~\cite[Lem.2.1]{GZ:asymptotics})
\be
\label{eq.qpoch.asy.psi}
  (ze^{x\hbar^{1/2}};e^{\hbar})_{\infty}^{-1}
  \;\sim\;
  \frac{1}{\sqrt{1-z}}\exp\Big(-\frac{\Li_{2}(z)}{\hbar}
  -\frac{\Li_{1}(z)x}{\hbar^{\frac{1}{2}}}
  -\frac{\Li_{0}(z)x^2}{2}\Big)
  \psi_{\hbar}(x,z)\,, \qquad (\hbar\rightarrow 0) \,.
\ee
Assuming that the matrix $B$ is invertible, (i.e., that $\det(B) \neq 0$),
we introduce the function
\be
\label{integrand}
f^\Xi_{\hb}(x,z) \=
\exp \bigg(\frac{\hbar^{\frac12}}{2} x^t1-\frac{\hbar^{\frac12}}{2} x^t  B^{-1} \nu
+\frac\hbar8 f^t B^{-1} A f \bigg) 
\prod_{i=1}^N \psi_{\hb}(x_i,z_i) \in \BQ(z)[x]\llbracket \hbar^{\frac12} \rrbracket\,,
\ee
which is the product of one quantum dilogarithm per tetrahedron (each
with its own integration variable), 
with some additional terms coming from the NZ-datum
where $x=(x_1,...,x_N)^t$ and $z=(z_1,...,z_N)$.

The last ingredient is the formal Gaussian integration~\cite{BIZ}  
\begin{small}
\bea
\label{FGI}
\left\langle
f_\hbar(x,z)
\right\rangle_{x,\Lambda}
\;:=\; \exp\left(
{\frac 1 2 \sum_{i,j=1}^N (\Lambda^{-1})_{i,j}
\frac{\partial}{\partial x_i}
\frac{\partial}{\partial x_j}}\right)
f_\hbar(x,z) \Big|_{x=0} =
\frac{\int e^{-\frac12x^t \Lambda \,x}f_{\hb,z}(x) \, dx}{
  \int e^{-\frac12x^t \Lambda \,x} \, dx}
\in \BQ(z)\llbracket \hbar \rrbracket
\eea
\end{small}
of a power series $f_\hbar(x,z) \in \BQ(z)[x]\llbracket\hroot \rrbracket$, with
respect to an invertible matrix $\Lambda$. Assuming further that the symmetric
matrix
\be
\label{lambda}
\Lambda \= - B^{-1} A + \diag(1/(1-z_j))
\ee
is invertible, we define 

\be
\label{Phidef}
\Phi^\Xi(\hbar) \= \langle f^\Xi_{\hbar}(x,z) \rangle_{x, \Lambda}
\in \BQ(z)\llbracket \hbar \rrbracket\,.
\ee

Using a solution $z$ of the Neumann--Zagier equations that corresponds to
the discrete faithful representation $\rho^\geom: \pi_1(M) \to \PSL_2(\BC)$
of a cusped hyperbolic 3-manifold $M$, one obtains a series $\Phi^\Xi(\hbar)$
with coefficients in the invariant trace field of $M$.
Our main theorem is the following.

\begin{theorem}
\label{thm.1}
$\Phi^\Xi(\hbar)$ is a topological invariant of a cusped hyperbolic 3-manifold.
\end{theorem}

A corollary of the above theorem is that every coefficient of the above
series is a topological invariant of a cusped hyperbolic 3-manifold. These
topological invariants have a geometric origin, since they take values in
the invariant trace field of the manifold, and hence they are algebraic, but
not (in general) rational, numbers. This series seems to come from 
hyperbolic geometry (though a definition of these invariants in terms of the
hyperbolic geometry of the 3-manifold is not known), and perhaps not from enumerative
quantum field theory (such as the Gromov--Witten or any of the 4-dimensional
known theories). The behavior of these series under finite cyclic coverings of
cusped hyperbolic 3-manifolds is given in~\cite{GY:1loop.torsion}, and the
formulas presented there (e.g., for the coefficient of $\hbar^2$) point to
unknown connections with the spectral theory of hyperbolic 3-manifolds.

The proof of our theorem combines the ideas of the topological invariance of the
Andersen--Kashaev state-integrals~\cite{AK} with those of the Aarhus
integral~\cite{AarhusII}. We briefly recall that the building block for the
state-integral is the Faddeev quantum
dilogarithm, the state-integral is a finite-dimensional integral of a product of
Faddeev quantum dilogarithm~\cite{Faddeev}, one for each tetrahedron of an (ordered)
ideal triangulation. Aside from elementary choices, two important parts
in the proof of topological invariance of the state-integral is
invariance under (a) the choice of a nondegenerate quad, and
(b) 2--3 ordered Pachner moves, the latter connecting one ideal triangulation
with another. In~\cite{AK}, (a) and (b) are dealt with a Fourier transform and
a pentagon identity for the Faddeev quantum dilogarithm.

The power series $\Phi^\Xi(\hbar)$ is given instead by a formal Gaussian integral
(as opposed to an integral over Euclidean space), where the building block is
the formal power series $\psi_\hbar$ instead of the Faddeev
quantum dilogarithm. The topological invariance of the $\Phi^\Xi(\hbar)$ under
the choice of quad and under the 2--3 Pachner moves follows from a Fourier tranform
identity and a pentagon identity for $\psi_\hbar$; see Theorems~\ref{thm.fourier}
and~\ref{thm.pentagon} below. Although these identities are, in a sense, limits of
the corresponding identities for the Faddeev quantum dilogarithm (just as
$\psi_\hbar$ is a limit of the Faddeev quantum dilogarithm), it would requires
additional analytic work to do so, and instead we give algebraic proofs of
theorems~\ref{thm.fourier} and~\ref{thm.pentagon} using properties of the
formal Gaussian integration, together with holonomic properties of the involved
formal power series.

Having discussed the similarities between the proof of Theorem~\ref{thm.1} and
the corresponding theorem for the state-integral of~\cite{AK}, we now point out
some differences. In~\cite{AK}, Andersen--Kashaev use ordered triangulations,
and the state-integral is
obtained by the push-forward of a distribution with variables at the faces and
the tetrahedra of the ordered triangulation. Part of the distribution is a product
of delta functions in linear forms of the face-variables. In our Theorem~\ref{thm.1},
and in the formal Gaussian integration, we carefully avoided the need to use
delta functions, although such a reformulation of our results are possible, with
additional effort.

We end this section by pointing out a wider context for the asymptotic series
$\Phi^\Xi(\hbar)$ and Theorem~\ref{thm.1}. It was clear from~\cite{DG} that
a NZ-datum $\Xi=(A,B,\nu,z,f,f'')$ depends on two square matrices $A$ and $B$
such that $AB^t$ is symmetric that may or may not come from topology, and that
the series $\Phi^\Xi(\hbar)$ is defined under the assumption that $\det(B) \neq 0$
and $\det(\Lambda) \neq 0$. Doing so, the proof of Theorem~\ref{thm.1} shows that
the series $\Phi^\Xi(\hbar)$ is invariant under the moves that appear
in~\cite[Sec.6]{GZ:kashaev}; see also Section~\ref{sec.elementary}.
