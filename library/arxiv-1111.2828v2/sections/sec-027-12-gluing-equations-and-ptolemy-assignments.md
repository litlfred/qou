---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-027-12-gluing-equations-and-ptolemy-assignments
section_title: "Gluing equations and Ptolemy assignments"
section_number: 12
pages: 41-42
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.978
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.gluingequations}

In this section we discuss the relation between Ptolemy assignments and 
solutions to the gluing equations. The latter were invented by 
Thurston~\cite{ThurstonNotes} to explicitly compute the hyperbolic 
structure (and its deformations) of a triangulated hyperbolic manifold,
and used effectively in \cite{NeumannZagier, snapprogram, SnapPy}.  
The gluing equations make sense for any $3$-cycle. 
They are defined by assigning a \emph{cross-ratio} $z_i\in\Cremove$ to each simplex 
$\Delta_i$ of $K$. Given these, we assign cross-ratio parameters to 
the edges of $\Delta_i$ as in Figure~\ref{Crossratioparameters}.




\begin{figure}[ht]
$$
\psdraw{SLrepFigures.22}{1.7in}
$$
\caption{Assigning cross-ratio parameters to the edges of $\Delta_i$. By definition, $z^\prime=\frac{1}{1-z}$ and $z^{\prime\prime}=1-\frac{1}{z}$.}
\lbl{Crossratioparameters}
\end{figure}
There is a gluing equation for each edge $E$ in $K$ and each generator 
$\gamma$ of the fundamental group of each boundary component of $M$. These 
are given by
\begin{equation}\lbl{gluingequations}
\prod_{e\mapsto E}z(e)^{\epsilon_i(e)}=1,\qquad \prod_{\gamma\textnormal{ passes }e}
z(e)^{\epsilon_i(e)}=1.
\end{equation}
Here $z(e)$ denotes the cross-ratio parameter assigned to $e$, and 
$\epsilon_i(e)=\epsilon_i$ if $e$ is an edge of $\Delta_i$. 

It follows that the set of assignments $\Delta_i\mapsto z_i\in\Cremove$ 
satisfying the gluing equations~\eqref{gluingequations} is an algebraic 
set $V(K)$.
 
\begin{lemma} 
For every point $\{z_i\}\in V(K)$ there is a map $D\colon L^{(0)}\to\Cinfty$ 
such that if $\widetilde\Delta_i$ is a lift of $\Delta_i$ with vertices 
$e_1,\dots,e_3$ in $L$, the cross-ratio of the ideal simplex with vertices 
$D(e_1),\dots,D(e_3)$ is $z_i$. It is unique up to multiplication by an 
element in $\PSL(2,\C)$. Moreover, there is a unique (up to conjugation) 
boundary-unipotent representation $\pi_1(M)\to\PSL(2,\C)$ such that $D$ is 
$\rho$-equivariant.
\end{lemma}

\begin{proof}
Pick a fundamental domain $F$ for $K$ in $L$. Pick a simplex $\Delta$ in 
$F$ and define $D$ by mapping the first $3$ vertices of $\Delta$ to $0$, 
$\infty$ and $1$. The map $D$ is now uniquely determined by the cross-ratios. 
The fundamental group of $M$ has a presentation with a generator for each 
face pairing of $F$. The second statement thus follows from the fact that 
$\PSL(2,\C)$ is $3$-transitive. We leave the details to the reader.
\end{proof}

Given a Ptolemy assignment on $K$, we assign the cross-ratio $z_i=\frac{c^i_{03}c^i_{12}}{c^i_{02}c^i_{13}}$ to $\Delta_i$.
Note that the Ptolemy relations imply that the cross-ratio parameters are given by
\begin{equation}\label{eq:shapeparameterformula}
z_i=\frac{c^i_{03}c^i_{12}}{c^i_{02}c^i_{13}},\qquad z_i^\prime=\frac{c^i_{02}c^i_{13}}{c^i_{01}c^i_{23}}, \qquad z_i^{\prime\prime}=-\frac{c^i_{01}c^i_{23}}{c^i_{03}c^i_{12}}. 
\end{equation}

\begin{theorem} 
There is a surjective regular map
\begin{equation}
\coprod_{\sigma\in H^2(K;\Z/2\Z)} P_2^\sigma(K)\to V(K),
\quad c\mapsto \{z_i=\frac{c^i_{03}c^i_{12}}{c^i_{02}c^i_{13}}\}.
\end{equation}
The fibers are disjoint copies of $(\C^*)^h$, where $h$ is the number of zero-cells of $K$.
\end{theorem}

\begin{proof}
By a simple cancellation argument (as in the proof of Zickert~\cite[Theorem~6.5]{ZickertDuke}), the gluing equations would be satisfied if the formula \eqref{eq:shapeparameterformula} for $z_i^{\prime\prime}$ did not have the minus sign. The minus sign appears whenever the edge is $02$ or $13$. As explained in the proof of Proposition~\ref{independenceoflog}, any curve passes these an even number of times. It thus follows that the cross-ratios satisfy the gluing equations. Surjectivity follows from Lemma~\ref{developingdecoration}, and the fact that fibers are $(\C^*)^h$ follows from the fact that $g_1\infty=g_2\infty$ if and only if $g_1N=g_2dN$ for a unique diagonal matrix $d$.
\end{proof}

\begin{remark}
Gluing equation varieties for $n>2$ are studied in Garoufalidis-Goerner-Zickert~\cite{GaroufalidisGoernerZickert}.
\end{remark}
