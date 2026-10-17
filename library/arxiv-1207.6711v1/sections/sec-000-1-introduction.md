---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.786
---
\subsection{Thurston's gluing equations}
\label{sub.ge}


Thurston's gluing equations are a system of polynomial equations defined for 
a compact $3$-manifold $M$ together with a topological ideal triangulation 
$\T$ of the interior of $M$. The gluing equations were introduced to concretely construct a complete hyperbolic structure on $M$ from a (suitable) solution to the gluing equations. 

Although Thurston only considered manifolds whose boundary components are tori (a necessary condition for the existence of a solution yielding a hyperbolic structure), the gluing equations are defined for manifolds with arbitrary (possibly empty) boundary. The existence of hyperbolic structures is of no concern to us here.

The gluing equations consist of an \emph{edge equation} for each $1$ cell of $\T$ and a \emph{cusp equation} for each generator of the fundamental group of each boundary component of $M$. The system may be written in the form
\begin{equation}\label{eq:GluingEqIntro}
\prod_j z_j^{A_{ij}} \prod_j (1-z_j)^{B_{ij}}=\e_i,
\end{equation}
where $A$ and $B$ are matrices whose columns are parametrized by the simplices of $\T$ and $\e_i$ is a sign (which is $1$ for the edge equations). Each variable $z_j$ may be thought of as an assignment of an ideal simplex shape to a simplex of $\T$. If the shapes $z_j\in\C\setminus\{0,1\}$ satisfy~\eqref{eq:GluingEqIntro}, as well as some extra conditions on the arguments of $z_i$, the ideal simplices glue together to form a complete hyperbolic structure on $M$. Ignoring the cusp equations gives structures that are incomplete. This gives rise to an efficient algorithm for constructing hyperbolic structures, which has been effectively implemented in software packages such as SnapPea~\cite{SnapPea}, Snap~\cite{snapprogram}, and SnapPy~\cite{SnapPy}. 


Among the numerous important features of the gluing equations we will focus
on two:
\begin{itemize}
\item[(a)] The symplectic property of the exponent matrix $(A \vert B)$
of the gluing equations due to Neumann and Zagier~\cite{NeumannZagier}.
\item[(b)] The link to $\PGL(2,\BC)$ representations via a 
\emph{developing map}
\begin{equation}\label{eq.dev2}
V_2(\CT) \to \{\rho\colon\pi_1(M)\to\PGL(n,\C)\}\big/\Conj
\end{equation}
where  $V_2(\T)$ denotes the affine variety of solutions in 
$\C\setminus\{0,1\}$ to the \emph{edge} equations, and the right hand side denotes the set of conjugacy classes of representations of $\pi_1(M)$ in $\PGL(2,\C)$. 

\end{itemize}
We may thus think of $V_2(\T)$ as a parametrization of representations. Note, however, that $V_2(\T)$ depends on the triangulation, and that the developing map need neither be onto nor finite to one. However, if the triangulation is sufficiently fine (a single barycentric subdivision suffices) the developing map is onto, i.e.~every representation is detected (including reducible ones). A solution satisfying the cusp equations as well gives rise to a representation that is boundary-unipotent, i.e.~takes peripheral curves to unipotent elements. Our goal is to
\begin{itemize}
\item
Extend Thurston's gluing equations to $\PGL(n,\BC)$ preserving the above
features for $n=2$, using suitable shape parameters.
\item
Relate the Ptolemy parameters of~\cite{GaroufalidisThurstonZickert}
to the shape parameters via a monomial map.
\end{itemize}

The Ptolemy and shape coordinates were inspired by the $\mathcal A$-coordinates
and $\mathcal X$-coordinates on higher Teichm\"{u}ller spaces due to Fock and 
Goncharov~\cite{FockGoncharov}. Note, however, that Fock and 
Goncharov study surfaces, whereas we study 3-manifolds. Shape coordinates for $n=3$ have been studied independently by Bergeron, Falbel and Guilloux~\cite{FrenchPeople}.

There is a very interesting interplay between the shape coordinates and the Ptolemy coordinates. The groups $\PGL(n,\C)$ and $\SL(n,\C)$ are Langlands dual, and we believe that this interplay is a 3-dimensional aspect of the duality discussed for surfaces by Fock and Goncharov~\cite[p.~33]{FockGoncharov}. The duality is particularly explicit when all the boundary components of $M$ are tori, see Proposition~\ref{prop:DualityTori}.








While the Ptolemy variety naturally parametrizes boundary-unipotent representations, the gluing equations also parametrize representations that are not necessarily boundary-unipotent. The boundary-unipotent ones can be determined by adding additional equations, which are generalizations of Thurston's cusp equations. This is studied in Section~\ref{sec:CuspEquations}.
