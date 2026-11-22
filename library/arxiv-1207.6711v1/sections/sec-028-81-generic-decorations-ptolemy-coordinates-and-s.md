---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-028-81-generic-decorations-ptolemy-coordinates-and-s
section_title: "Generic decorations, Ptolemy coordinates and shapes"
section_number: 8.1
pages: 26-28
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.957
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
For an element $g\in\GL(n,\C)$, let $\{g\}_i$ denote the ordered set consisting of the first $i$ column vectors of $g$.
\begin{definition}\label{def:generic}
A $\GL(n,\C)/N$-decoration $(g_0N,g_1N,g_2N,g_3N)$ on $\Delta^3_n$ is \emph{generic} if for each $(t_0,t_1,t_2,t_3)\in\Delta_n^3(\Z)$
\begin{equation}\label{eqn:PtolemyDets}
\det\big(\{g_0\}_{t_0}\cup\{g_1\}_{t_1}\cup\{g_2\}_{t_2}\cup\{g_3\}_{t_3}\big)\neq 0.
\end{equation}
Genericity of $\PGL(n,\C)/B$-decorations is defined similarly.
\end{definition}
The definition is obviously independent of the choice of coset representatives, and of the ordering of the tuple.

\begin{remark}\label{rm:FineTriangulation}
Although all representations can be decorated, some representations may only have non-generic decorations. However, after a single barycentric subdivision, every representation has a generic decoration. For $\SL(n,\C)/N$-decorations this is proved in \cite[Prop.~5.4]{GaroufalidisThurstonZickert}, and the proof for $\PGL(n,\C)/B$-decorations is similar. This proves the last statement of Theorem~\ref{thm:ShortMainThm}.
\end{remark}

\begin{lemma}[{Fock-Goncharov~\cite[Lemma~10.3]{FockGoncharov}; see also~\cite{GaroufalidisThurstonZickert}}]\label{lemma:DecorationToPtolemy}
A generic $\GL(n,\C)/N$-decoration $(g_0N,g_1N,g_2N,g_3N)$ of $\Delta^3_n$ induces a Ptolemy assignment
\begin{equation}\label{eqn:DecoToPtolemy}
c\colon\dot\Delta_n^3(\Z)\to \C^*,\quad t\mapsto \det\left(\{g_0\}_{t_0}\cup\{g_1\}_{t_1}\cup\{g_2\}_{t_2}\cup\{g_3\}_{t_3}\right).
\end{equation}\qed
\end{lemma}
\begin{corollary} We have a map
\begin{equation}
\mathcal C\colon\text{\{Generic $\GL(n,\C)/N$-decorations on $\Delta^3_n$\}}\to \text{\{Ptolemy assignments on $\Delta^3_n$\}}. 
\end{equation}\qed
\end{corollary}
Note that $\mathcal C$ is invariant under the left action by $\SL(N,\C)$.

\begin{lemma} \label{lemma:DecorationsAndPullbacks}
The map $\mathcal C$ is compatible with pullbacks, i.e., 
\begin{equation}\label{eq:DecorationsAndPullbacks}
\sigma^*(\mathcal C(g_0N,g_1N,g_2N,g_3N)=\mathcal C(g_{\sigma(0)}N,g_{\sigma(1)}N,g_{\sigma(2)}N,g_{\sigma(3)}N).
\end{equation}

\end{lemma}
\begin{proof}


Let $c=\mathcal C(g_0N,g_1N,g_2N,g_3N)$ and $c'=\mathcal C(g_{\sigma(0)}N,g_{\sigma(1)}N,g_{\sigma(2)}N,g_{\sigma(3)}N)$. Then
\begin{equation}
c_{\sigma(t)}=\det\left(\bigcup_{i=0}^3\{g_i\}_{t_{\sigma^{-1}(i)}}\right),\qquad c'_t=\det\left(\bigcup_{i=0}^3\{g_{\sigma(i)}\}_{t_i}\right).
\end{equation}
One easily checks that
\begin{equation}
\left(\bigcup_{i=0}^3\{g_i\}_{t_{\sigma^{-1}(i)}}\right)I_{\sigma,\sigma(t)}=\bigcup_{i=0}^3\{g_{\sigma(i)}\}_{t_i},
\end{equation}
from which it follows that $(\sigma^*c)_t=c_{\sigma(t)}\det(I_{\sigma,\sigma(t)})=c'_t$. This proves the result.
\end{proof}
\begin{corollary}
A generic $\SL(n,\C)/N$-decoration on $(M,\mathcal{T})$ induces a Ptolemy assignment on $(M,\mathcal{T})$.
\end{corollary}

\begin{proof}
We only need to show that Ptolemy coordinates are identified via the pullback. This follows from Lemma~\ref{lemma:DecorationsAndPullbacks}.
\end{proof}

\begin{remark}
A $\GL(N,\C)/N$-decoration does \emph{not} induce a Ptolemy assignment on $(M,\T)$.
\end{remark}

For $g\in\GL(N,\C)$, let $\bar{g}$ denote the image of $g$ in $\PGL(N,\C)$. 

\begin{proposition}\label{prop:DefofZ}
We have a well defined map
\begin{equation}
\begin{gathered}
\mathcal Z\colon\text{\{$\PGL(n,\C)/B$-decorations on $\Delta^3_n$\}}\to\text{\{shape assignments on $\Delta^3_n$\}},\\
(\bar{g}_0B,\bar{g}_1B,\bar{g}_2B,\bar{g}_3B)\mapsto\mu\circ\mathcal C(g_0N,g_1N,g_2N,g_3N),
\end{gathered}
\end{equation}
which is invariant under the left $\PGL(n,\C)$-action and compatible with pullbacks. 
\end{proposition}
\begin{proof}
Let $c=\mathcal C(g_0N,g_1N,g_2N,g_3N)$.
To prove that $\mathcal Z$ is well defined, we must prove that 
\begin{equation}\mu(c)=\mu(c'),\text{ with } c'=\mathcal C(g_0d_0N,\dots,g_3d_3N),
\end{equation}
where $d_i=d(\lambda^i_1,\dots,\lambda^i_n)$ are diagonal matrices. We prove that $\mu(c)_s^{1100}=\mu(c')^{1100}_s$, the other cases being similar.
Using \eqref{eqn:PtolemyDets} we have
\begin{equation}\mu(c')_s^{1100}=\frac{c'_{s+1001}c'_{s+0110}}{c'_{s+1010}c'_{s+0101}},\quad c'_t=\det(\bigcup\{g_id_i\}_{t_i})=\left(\prod_{j=0}^{3}\prod_{i=1}^{t_i} \lambda^j_i\right) c_t.
\end{equation}
Expanding each term, we obtain
\begin{equation}
\begin{gathered}
c'_{s+1001} = \left(\prod_{j=0}^{3}\prod_{i=1}^{s_i} \lambda^j_i\right) \lambda^0_{s_0+1} \lambda^3_{s_3+1} c_{s+1001},\quad
c'_{s+0110} = \left(\prod_{j=0}^{3}\prod_{i=1}^{s_i} \lambda^j_i\right) \lambda^1_{s_1+1} \lambda^2_{s_2+1} c_{s+0110}\\
c'_{s+1010} = \left(\prod_{j=0}^{3}\prod_{i=1}^{s_i} \lambda^j_i\right) \lambda^0_{s_0+1} \lambda^2_{s_2+1} c_{s+1010},\quad
c'_{s+0101} = \left(\prod_{j=0}^{3}\prod_{i=1}^{s_i} \lambda^j_i\right) \lambda^1_{s_1+1} \lambda^3_{s_3+1} c_{s+0101}.
\end{gathered}
\end{equation}
It now easily follows that 
\begin{equation}
\mu(c')_s^{1100}=\frac{c'_{s+1001}c'_{s+0110}}{c'_{s+1010}c'_{s+0101}}=\frac{c_{s+1001}c_{s+0110}}{c_{s+1010}c_{s+0101}}=\mu(c)_s^{1100}
\end{equation}
as desired. Invariance under left multiplication follows from the fact that $\det(\cup\{gg_i\}_{t_i})=\det(g)\det(\cup\{g_i\}_{t_i})$, and compatibility with pullbacks follows from the fact that both $\mu$ and $\mathcal C$ enjoy this property. 
\end{proof}

\begin{corollary}
A generic $\PGL(n,\C)/B$-decoration on $(M,\T)$ induces a shape assignment on $(M,\T)$.
\end{corollary}

\begin{proof}
By Proposition~\ref{prop:DefofZ}, we have a shape assignment on each simplex, and we must prove that these satisfy the generalized gluing equations. We proceed as in the proof of Theorem~\ref{thm:PtolemyYieldsShapes}. Let $K$ be the local model of an edge point as defined in Section~\ref{subsection:ProofForEdgeEqn}. We can pullback the decoration on $\T$ to a decoration on $K$ using the simplical map $\pi$. Since $K$ is simply connected, we can change the decoration of each simplex by left multiplication by an element in $\PGL(n,\C)$ such that vertices of simplices that get identified in $K$ carry the same coset. This does not affect the shapes. For each vertex in $K$ decorated by $gB$ we pick a lift $\tilde{g}N$ and apply $\mathcal C$ to get a Ptolemy assignment on $K$. By Lemma~\ref{lemma:edgelocalmodel} the shapes satisfy the edge equations. The result for the face, and interior gluing equations is similar.
\end{proof}
