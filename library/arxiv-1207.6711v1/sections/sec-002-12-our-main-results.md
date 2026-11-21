---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-002-12-our-main-results
section_title: "Our main results"
section_number: 1.2
pages: 3-5
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.965
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sub.results}
Given a topological ideal triangulation $\CT$, each simplex of $\T$ is divided into $\binom{n+1}{3}$ overlapping \emph{subsimplices} (see Definition~\ref{def:Subsimplex}) and each edge of each subsimplex is assigned a \emph{shape parameter} (see Definition~\ref{shapeassignment}). These are the variables of the gluing equations. There is an equation for each non-vertex integral point 
point of $\T$ (see Definition \ref{def:IntegralPoint}). These are given in Definition~\ref{def:GluingEquationsOri}.




We can write the gluing equations (without the cusp equations) in the form
\begin{equation}\label{eq:GluinEqSimplified}
\prod_s z_s^{A_{p,s}}\prod_s(1-z_s)^{B_{p,s}}=1,
\end{equation}
where $A$ and $B$ are matrices whose rows are parametrized by the non-vertex integral points $p$ of $\T$ and whose colums are parametrized by the subsimplices $s$ of $\T$.

\begin{theorem}\label{thm:soft} Let $P=(A\vert B)$ be the concatenation of the matrices $A$ and $B$ in~\eqref{eq:GluinEqSimplified}.

\begin{itemize}
\item[(a)]\label{item:Soft1} The rows of $P$ Poisson commute, i.e.~for any two rows $v$ and $w$, $\langle v,w\rangle=0$, where $\langle,\rangle$ is the symplectic form given by $\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$.
\item[(b)]\label{item:soft2} If all boundary components of $M$ are tori, $P$ is an $r\times 2r$ matrix, where $r=t\binom{n+1}{3}$ and $t$ is the number of simplices of $\T$.
\end{itemize}
\end{theorem}

Let $V_n(\CT)$ denote the affine variety of solutions to the 
$\PGL(n,\BC)$ gluing equations and let $P_n(\CT)$ denote the affine variety
of solutions to the Ptolemy equations of~\cite{GaroufalidisThurstonZickert} (see Section~\ref{sec:PtolemyReview} for a review).
The link to representations is given by the result below, which also gives the relationship between the shape coordinates and the Ptolemy coordinates.

\begin{theorem}\label{thm:ShortMainThm} There is a monomial map $\mu\colon P_n(\T)\to V_n(\T)$ which fits in a commutative diagram
\begin{equation}\label{eqn:ShortDiagramIntro}
\cxymatrix{{{P_n(\T)}\ar[r]^-{\mathcal R}\ar[d]^\mu&{\left\{\txt{$\rho\colon\pi_1(M)\to\SL(n,\C)$\\\textnormal{ boundary-unipotent}}\right\}\Big/\Conj}\ar[d]^\pi\\{V_n(\T)}\ar[r]^-{\mathcal R}&{\{\rho\colon\pi_1(M)\to\PGL(n,\C)\}\big/\Conj}}}
\end{equation}
where the map $\pi$ is induced by the canonical map $\SL(n,\C)\to\PGL(n,\C)$. Furthermore, the horizontal maps are surjective if the triangulation $\T$ is sufficiently fine.
\end{theorem}

































Theorem~\ref{thm:ShortMainThm} is an immediate consequence of Theorem~\ref{thm:MainThm} below which displays some more of the underlying structure. Briefly, a \emph{decoration} is an equivariant assignment of a coset to each vertex of each simplex of $\T$ (see Definition~\ref{def:Decoration}) and a \emph{cocycle} is an assignment of matrices to the edges satisfying the standard cocycle condition that the product around each face is $1$ (see Definition~\ref{def:GCocycle}). Generic decorations and natural cocycles are defined in Definition~\ref{def:generic} and Definitions~\ref{def:NaturalSLCocycle} and \ref{def:NaturalPGLCocycle}. 

\begin{theorem}\label{thm:MainThm}
There is a commutative diagram
\begin{equation} \label{eqn:DiagramIntro}
\cxymatrix{{
\left\{\txt{\textnormal{Ptolemy}\\\textnormal{assignments}}\right\} 

\ar[d]^\mu & \ar[d]^\pi \ar_-{\mathcal C}[l] \left\{\txt{\textnormal{Generic} $\SL(n,\C)/N$\\\textnormal{decorations}}\right\} \ar^-{\mathcal L_{\alpha\beta}}[r] & \ar[d]^\tau \left\{\txt{\textnormal{Natural} $(\SL(n,\C),N)$\\\textnormal{cocycles}}\right\}\\
\left\{\txt{\textnormal{Shape}\\\textnormal{assignments}}\right\} 

& \ar_-{\mathcal Z}[l] \left\{\txt{\textnormal{Generic} $\PGL(n,\C)/B$\\\textnormal{decorations}}\right\} \ar^-{\mathcal L_{\alpha\beta\gamma}}[r] & \left\{\txt{\textnormal{Natural} $(\PGL(n,\C),B,H)$\\\textnormal{cocycles}}\right\}
}}
\end{equation}
in which the horizontal maps are $1$-$1$-correspondences. All maps are explicit with explict inverses and respect the symmetries of a simplex.
\end{theorem}
The fact that the top horizontal maps are $1$-$1$-correspondences was proved in Garoufalidis-Thurston-Zickert~\cite{GaroufalidisThurstonZickert}.

To see that Theorem~\ref{thm:MainThm} implies Theorem~\ref{thm:ShortMainThm}, note that a cocycle determines a representation by picking a base point and taking products along edge paths. Furthermore, a decoration also determines a representation using the dual triangulation of $\T$ which is generated by face pairings. The last statement of Theorem~\ref{thm:ShortMainThm} follows from Remark~\ref{rm:FineTriangulation}.
