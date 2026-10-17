---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-006-21-face-pairing-permutations
section_title: "Face pairing permutations"
section_number: 2.1
pages: 7-8
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.95
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
We canonically identify the symmetry group of an ordered simplex with
$S_4$.
\begin{definition} 
Let $\Delta_0$ and $\Delta_1$ be ordered simplices and let $\psi$ from face $f_0$ of $\Delta_0$ to face $f_1$ of $\Delta_1$ be a face pairing. The \emph{face pairing permutation} corresponding to $\psi$ is the unique permutation $\sigma\in S_4$ such that $\psi$ takes vertex $v$ of $\Delta_0$ to vertex $\sigma(v)$ of $\Delta_1$ whenever $v$ is a vertex in $f_0$. 
\end{definition}
Note that if we identify $\Delta_0$ and $\Delta_1$ via the unique order preserving isomorphism, $\sigma$ is the unique extension of $\psi$ to a symmetry of $\Delta_0$. See Figure~\ref{fig:faceGluing}.











\section{Thurston's gluing equations}\label{sec:ThurstonReview}
In this section we briefly review Thurston's gluing equations. For details we refer to Thurston~\cite{ThurstonNotes} or Neumann-Zagier~\cite{NeumannZagier}.

Let $\T$ be an \emph{oriented} triangulation of $M$. The gluing equations are given in terms of a variable $z_\Delta\in\C\setminus\{0,1\}$, called a \emph{shape coordinate}, for each simplex $\Delta$ of $M$. To define the equations, assign to each edge of each simplex $\Delta$ of $M$ one of three \emph{shape parameters}, see Figure~\ref{fig:TraditionalShapes}. The shape parameters are given in terms of the shape coordinate $z_\Delta$ by
\begin{equation} \label{eqn:shapeParms}
z_\Delta,\qquad z_\Delta^\prime=\frac{1}{1-z_\Delta},\qquad z_\Delta^{\prime\prime}=1-\frac{1}{z_\Delta}=-\frac{1-z_\Delta}{z_\Delta}.
\end{equation}

\begin{figure}[htpb]
\begin{center}
\includegraphics[width=4.5cm]{figures_src/tetrahedronshapes}
\end{center}


\caption{Assigning shape parameters to the edges of a 
simplex.}\label{fig:TraditionalShapes}
\end{figure}

The gluing equations consist of \emph{edge equations} and \emph{cusp equations}. There is an edge equation for each edge cycle $e$ of $\mathcal T$, obtained by setting the product of the shape parameters assigned to each edge in $e$ equal to $1$. 
Each edge equation thus has the form 
\begin{equation}\label{eqn:ThurstonGluing}
\prod_\Delta z_\Delta^{a_\Delta} \prod_\Delta z'^{b_\Delta}_\Delta \prod_\Delta z''^{c_\Delta}_\Delta = 1,
\end{equation}
where $a_\Delta$, $b_\Delta$ and $c_\Delta$ are integers.

The cusp equations consist of an equation for each generator of the fundamental group of each boundary component. If $\gamma$ is a peripheral (normal) curve, we obtain a cusp equation by setting the product of the shape parameters (or their inverses) of edges passed by $\gamma$ equal to $1$ ($\gamma$ \emph{passes} an edge $E$ of a simplex $\Delta$ if it enters and exits $\Delta$ through faces intersecting in $E$). A shape parameter appears with its inverse if and only if $\gamma$ passes $e$ in a clockwise direction viewed from the cusp. The cusp equations have the same form as \eqref{eqn:ThurstonGluing}.

The following result is well known. We will generalize this to representations in $\mathrm{PGL}(n,\C)$ below.
\begin{theorem} A solution to the edge equations with all shape coordinates in $\C\setminus\{0,1\}$ uniquely (up to conjugation) determines a representation $\rho\colon\pi_1(M)\to \PGL(2,\C)$. If the solution also satisfies the cusp equations, $\rho$ is boundary-unipotent, i.e.~takes peripheral curves to a conjugate of $N$.
\end{theorem}
