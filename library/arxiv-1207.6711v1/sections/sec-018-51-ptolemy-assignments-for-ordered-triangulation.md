---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-018-51-ptolemy-assignments-for-ordered-triangulation
section_title: "Ptolemy assignments for ordered triangulations"
section_number: 5.1
pages: 14-15
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.92
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\begin{definition}\label{def:PtolemyAssignment}
A \emph{Ptolemy assignment} on $\Delta^3_n$ is an assignment
\begin{equation}
\dot{\Delta}^3_n(\Z)\to\C\setminus\{0\},\qquad t\mapsto c_t
\end{equation}
of a non-zero complex number $c_t$ to each non-vertex integral point $t$ of $\Delta^3_n$ such that the \emph{Ptolemy relation}
\begin{equation}
c_{s+1001}c_{s+0110}+c_{s+1100}c_{s+0011}=c_{s+1010}c_{s+0101}\label{eqn:PtolemyRelation}
\end{equation}
is satisfied for each subsimplex $s\in\Delta^3_{n-2}(\Z)$. 
\end{definition}
\begin{definition}\label{def:PtolemyAssignmentOrd}
A Ptolemy assignment on an \emph{ordered} triangulation $\mathcal{T}$ is an assignment
\begin{equation}
\dot{\mathcal{T}}_n(\Z)\to\C\setminus\{0\},\qquad p\mapsto c_p
\end{equation}
of a non-zero complex number to each non-vertex integral point $p$ of $\mathcal{T}$ such that for each simplex in $\mathcal{T}$ the identification with $\Delta^3_n$ induces a Ptolemy assignment on $\Delta^3_n$. If $(t,\Delta)\in p$ is a representative of $p$, we write $c_{t,\Delta}$ for the Ptolemy coordinate $c_p$. The variety of Ptolemy assignments is denoted by $P_n(\T)$.
\end{definition}

\begin{remark}
Whenever convenient, we extend a Ptolemy assignment, so that it takes vertex points to $1$.
\end{remark}




\begin{figure}[htb]
\begin{center}
\scalebox{0.9}{
\includegraphics{figures_gen/PtolemyCoordinatesOnSimplex_included}}\\
$c_{1131}c_{0240}+c_{1230}c_{0141}=c_{1140}c_{0231}$
\end{center}
\caption{Ptolemy relation for the subsimplex $s=0130$.}
\end{figure}

\begin{remark} Note that the Ptolemy relation \eqref{eqn:PtolemyRelation} is local, i.e.~independent of the triangulation $\mathcal{T}$. The triangulation determines whether $(t,\Delta)$ and $(t',\Delta')$ represent the same integral point $p$, and, hence, whether the Ptolemy coordinates $c_{t,\Delta}$ and $c_{t',\Delta'}$ are identified.
\end{remark}
