---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-018-6-a-chain-complex-of-ptolemy-assignments
section_title: "A chain complex of Ptolemy assignments"
section_number: 6
pages: 18-19
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.939
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.ptolemy}

Let $Pt_k^n$ be the free abelian group on Ptolemy assignments on $\Delta^k_n$. 
The usual boundary map induces a boundary map $Pt_k^n\to Pt_{k-1}^n$ and the 
natural map $C_*^{\gen}(G/N)\to Pt_*^n$ taking a tuple $(g_0N,\dots,g_kN)$ to 
its Ptolemy assignment is a chain map. The result below is proved in 
Section~\ref{proofsection}.

\begin{proposition}
\lbl{tupleuniqueuptoGaction}
A generic tuple is determined up to the diagonal $G$-action by its 
Ptolemy coordinates.\qed
\end{proposition} 

\begin{corollary}
\lbl{Ptolemycomputeshomology} 
The natural map induces an isomorphism 
\begin{equation}\lbl{CgenPt}
C_*^{\gen}(G/N)\otimes_{\Z[G]}\Z\cong Pt_*^n.
\end{equation}
In particular, $H_*(G,N)=H_*(Pt^n_*)$.\qed
\end{corollary}

\begin{lemma}
\lbl{inducedPtolemyassignment}
Let $c\in Pt_k^n$ be a Ptolemy assignment, and let $\alpha\in\Delta^k_{n-2}(\Z)$. The 
Ptolemy coordinates $c_{\alpha_{ij}}$, $i\neq j$ are the Ptolemy coordinates 
of a unique Ptolemy assignment $c_\alpha$ on the subsimplex $\Delta^k(\alpha)$.
\end{lemma}

\begin{proof} 
For $1\leq k\leq 3$, this follows from Proposition~\ref{uniquePtolemyassignment}. 
For $k>3$, the result follows by induction, using the fact that $5$ Ptolemy 
coordinates on $\Delta^3_2$ determines the last.
\end{proof}

A Ptolemy assignment $c$ on $\Delta^k_n$ thus induces a Ptolemy assignment $c_\alpha$ on each 
subsimplex. We thus have maps
\begin{equation}
\lbl{Jkn}
J_k^n\colon Pt_k^n\to Pt_k^2, \quad c\mapsto\sum_{\alpha\in \Delta^k_{n-2}(\Z)}c_{\alpha}.
\end{equation}

For a Ptolemy assignment $c\in Pt_k^n$ let $c_{\underline i}\in Pt_{k-1}^n$ be the 
induced Ptolemy assignment on the $i$th face of $\Delta^k_n$, i.e.~we have 
$\partial(c)=\sum_{i=0}^k (-1)^ic_{\underline i}$. Note that
\begin{equation}\lbl{helpfuleq1}
(c_{\underline i})_{(a_0,\dots,a_{k-1})}=c_{(a_0,\dots,a_{i-1},0,a_{i},\dots a_{k-1})_{\underline i}}
\in Pt_{k-1}^2.
\end{equation}

For $\beta\in \Delta^k_{n-3}(\Z)$, let $c_{\beta^i}=c_{(\beta+e_i)_{\underline i}}\in Pt_{k-1}^2$, 
and define $\partial_{\beta}(c)\in Pt_{k-1}^2$ by 
\begin{equation}
\partial_{\beta}(c)=\sum_{i=0}^k (-1)^i c_{\beta^i}\in Pt_{k-1}^2.
\end{equation}  
The geometry is explained in Figure~\ref{cbetafigure}.

\begin{figure}[htpb]
$$
\psdraw{SLrepFigures.4}{1.7in} \qquad
\psdraw{SLrepFigures.5}{1.6in}
$$
\caption{The dotted lines in the left figure indicate $c_{\beta^0}$, 
$c_{\beta^1}$ and $c_{\beta^2}$ for $k=2$. The triangle in the right figure 
indicates $c_{\beta^0}$ for $k=3$. Here, $n=3$ and $\beta=0$.}
\lbl{cbetafigure}
\end{figure}

\begin{proposition}
\lbl{DeltaJ} 
Let $c\in Pt_k^n$. We have
\begin{equation}\partial (J_k^n(c))-J^n_{k-1}(\partial(c))
=\sum_{\beta\in \Delta^k_{n-3}(\Z)}\partial_\beta(c)\in Pt_{k-1}^2.
\end{equation}
\end{proposition}

\begin{proof}
By~\eqref{helpfuleq1}, we have
\begin{equation}
\begin{aligned}
\partial (J_k^n(c))-J_{k-1}^n(\partial(c))=&
\sum_{i=0}^k(-1)^i\sum_{\alpha\in \Delta^k_{n-2}(\Z)}c_{\alpha_{\underline i}}-
\sum_{i=0}^k(-1)^i\sum_{\substack{\alpha\in \Delta^k_{n-2}(\Z)\\a_i=0}}c_{\alpha_{\underline i}}
\\=&\sum_{i=0}^k(-1)^i\sum_{\substack{\alpha\in \Delta^k_{n-2}(\Z)\\a_i>0}}c_{\alpha_{\underline i}}
\\=&\sum_{\beta\in \Delta^k_{n-3}(\Z)}\sum_{i=0}^k(-1)^ic_{(\beta+e_i)_{\underline i}}
\\=&\sum_{\beta\in \Delta^k_{n-3}(\Z)}\partial_\beta(c)
\end{aligned}
\end{equation}
as desired
\end{proof}
