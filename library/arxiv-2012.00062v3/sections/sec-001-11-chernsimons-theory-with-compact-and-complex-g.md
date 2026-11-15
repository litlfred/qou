---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-001-11-chernsimons-theory-with-compact-and-complex-g
section_title: "Chern–Simons theory with compact and complex gauge group"
section_number: 1.1
pages: 1-4
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.846
---
\label{sub.intro}


Chern--Simons gauge theory, introduced by Witten in his seminal
paper~\cite{witten-jones} as a quantum field theory proposal of the
Jones polynomial~\cite{Jones}, remains one of the most fascinating
quantum field theories. It gives a powerful framework to study the
quantum topology of knots and three-manifolds, and at the same time it
provides a rich yet tractable model to explore general aspects of
quantum field theories.

In~\cite{witten-jones}, Witten analyzed in detail Chern--Simons gauge
theory with a compact gauge group (such as $\mathrm{SU}(2)$). Its
partition function on a 3-manifold $M$ with torus boundary components
depends on a quantized version $k \in \BZ$ of Planck's constant (or
equivalently, on a complex root of unity $\re^{2\pi \ri k}$), as well
as a discrete color (a finite dimensional irreducible representation
of $\mathrm{SU}(2)$) per boundary component of $M$. A more powerful
Chern--Simons theory with complex gauge group (such as $\SL(2,\BC)$)
was introduced by Witten~\cite{witten:complexCS} and developed
extensively by Gukov~\cite{gukov}.  A key feature of complex
Chern--Simons theory is that the partition function $Z_M(u;\tau)$ for
a 3-manifold $M$ with torus boundary components depends analytically
on a complex parameter $\tau$ (where $\tau=1/k$ in the Chern--Simons
theory with compact gauge group) as well as on a complex parameter $u$
per each boundary component of $M$ that plays the role of the holonomy
of a peripheral curve.  The analytic dependence of $Z_M(u;\tau)$ on
the parameters $u$ and $\tau$ allows one to formulate questions of
complex analysis and complex geometry which would be difficult, or
impossible, to do in Chern--Simons theory with compact gauge group.

There is a key difference between Chern--Simons theory with compact
versus complex gauge group: the former is an exactly solvable theory,
meaning that the partition function can be computed by a finite
state-sum, a consequence of the fact that it is a TQFT in 3
dimensions.  On the other hand, the situation with complex
Chern--Simons theory is more mysterious. For reasons that are not
entirely understood, the partition function $Z_M(u;\tau)$ for
manifolds with torus boundary components reduces to a
finite-dimensional integral (the so called-state integral) whose
integrand is a product of Faddeev's quantum dilogarithm
functions~\cite{Faddeev}, assembled out of an ideal triangulation of
the manifold. This was the approach taken by
Andersen-Kashaev~\cite{AK, AK-review} and Dimofte~\cite{dimofte-rev}
following prior ideas of~\cite{Hikami,DGLZ}. Focusing for simplicity
on the case of a 3-manifold with a single torus boundary component
(such as the complement of a hyperbolic knot in $S^3$), the
state-integral $Z_M(u;\tau)$ is a holomorphic function of
$\tau \in \BC'=\BC\setminus (-\infty,0]$ and 
$u \in \BC$ that satisfies a pair of linear $q$-difference equations.
The existence of these equations for a state-integral follows from the
closure properties of Zeilberger's theory of $q$-holonomic functions
and the the quasi-periodicity properties of Faddeev's quantum
dilogarithm, in much the same way as the $q$-holonomicity of the
colored Jones polynomial of a knot follows from a state-sum
formula~\cite{GL}. In fact, it is conjectured that the linear
$q$-difference equation satisfied by the colored Jones polynomial of a
knot coincides with the linear $q$-difference equations of
$Z_M(u;\tau)$ (see e.g.~\cite{AM} and Sections~\ref{sec.41}
and~\ref{sec.52} below for examples).


\subsection{Resurgence and the Stokes automorphism}
\label{sub.wall}
  
The global function $Z_M(u;\tau)$ gives rise to a vector
$\Phi(x;\tau)$ of perturbative series in $\tau$ whose coefficients are
meromorphic functions of $u$. These series are typically factorially
divergent and a key question is a description of the analytic
continuation of their Borel transform in Borel plane, their
trans-series and their Stokes automorphisms. This is a typical
question in perturbative quantum field theory where resurgence aims to
reproduce analytic functions from factorially divergent series (for an
introduction to resurgence, see for instance~\cite{msauzin,abs,mmreview,mmbook}),
and where Chern--Simons theory with a compact or complex gauge group is an
excellent case to analyze. Some aspects of resurgence in Chern--Simons
theory were studied
in~\cite{Ga:resurgence,CG,mmreview,gmp,gh-res,GZ:qseries,GZ:kashaev}.  The
multi-valuedness of the complex Chern-Simons action dictates that the
transseries are assembled out of monomials in $\tx$ and $\tq$ where
$\tq=\re^{-2 \pi \ri/\tau}$ and $\tx=\re^{u/\tau}$.

Our discoveries are summarized as follows:
\begin{itemize}
\item The singularities of the series $\Phi(x;\tau)$ in Borel
  plane are arranged in horizontal lines $2\pi \ri$ apart, and within
  these lines in finitely many points $\log x$ apart. This defines a
  collection of Stokes lines in a peacock-like pattern (see
  Figure~\ref{fig:stokes_rays}) whose corresponding Stokes
  automorphisms satisfy a unique factorization property with integer
  Stokes constants.
\item The Stokes automorphism $\sf{S}(x;q)$ along a half-plane is
  a fundamental matrix solution to a (dual) linear q-difference
  equation, hence fully computable.
\item The function $Z_M(u;\tau)$ is one entry of a matrix-valued collection
  of descendant partition functions which are a fundamental solution
  to a $q$-holonomic system in two variables.
\end{itemize}

\begin{figure}[htpb!]
  \centering
  \includegraphics[width=0.3\linewidth]{stokes_rays_refl}
  \caption{A peacock arrangement of Stokes rays in the complex Borel
    plane.}
  \label{fig:stokes_rays}
\end{figure}
  
The arrangement of the singularities in Borel plane
is reminiscent of a ``stability datum'' of
Kontsevich-Soibelman~\cite{KS,KS:stability, KS:wall-crossing} where the
corresponding integers are often called DT-invariants or BPS degeneracies. 
The Stokes automorphisms along half-planes are analogous to the spectrum
generators in
Gaiotto-Moore-Neitzke~\cite{gmn, gmn2, gmn3}. Our integers are locally
constant functions of a complex parameter $x$ and their jumping along
a wall-crossing will be the topic of a subsequent publication.

Our paper gives a concrete realization of these abstract ideas of
perturbative series and their resurgence, Stokes automorphisms and
their wall-crossing formulas for the case of complex Chern--Simons
theory, and illustrate our results with the 3-manifolds of the two
simplest hyperbolic knot complements, the complements of the
$\knot{4}_1$ and the $\knot{5}_2$ knots.
