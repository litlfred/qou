---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-026-111-essential-edges
section_title: "Essential edges"
section_number: 11.1
pages: 40-41
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.973
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.essential}

\begin{definition}
\lbl{def.essential}
An edge of $K$ is \emph{essential} if the lifts to $L$ have distinct end 
points.
\end{definition}

Note that an edge may be essential even though it is homotopically trivial 
in $K$. Let $L^{(0)}$ denote the zero skeleton of $L$.

\begin{lemma}
\lbl{developingdecoration}
Let $\rho$ be a representation in $\SL(2,\C)$ or $\PSL(2,\C)$. A decoration 
of $\rho$ determines a $\rho$-equivariant map
\begin{equation}
\lbl{developingCinfty}
D\colon L^{(0)}\to \partial\overline\H^3=\C\cup\{\infty\},
\quad e_i\mapsto g_i\infty.
\end{equation} 
Every such map comes from a decoration, and the decoration is generic 
if and only if the vertices of each simplex of $L$ map to distinct points 
in $\C\cup\{\infty\}$.
\end{lemma}

\begin{proof}
Equivariance of \eqref{developingCinfty} follows from the definition of a 
decoration. A $\rho$-equivariant map $D\colon L^{(0)}\to\Cinfty$ is uniquely 
determined by its image of lifts $\widetilde e_i\in L$ of the zero cells 
$e_i$ of $K$. Picking $g_i$ such that $g_i\infty=D(\widetilde e_i)$, we 
define a decoration by assigning the coset $g_iN$ to $\widetilde e_i$. 
The last statement follows from the fact that $\det(g_1e_1,g_2e_1)=0$ if 
and only if $g_1\infty=g_2\infty$.
\end{proof}

In the following we assume that the interior of $M$ is a cusped hyperbolic $3$-manifold $\H^3/\Gamma$ with finite volume.
\begin{proposition}\label{detectsgeometric}
If all edges of $K$ are essential, 
the geometric representation has a generic decoration.
\end{proposition}

\begin{proof}
We identify $\pi_1(M)$ with $\Gamma\subset\PSL(2,\C)$. Each vertex of $L$ 
corresponds to either a cusp of $M$ or an interior point of $M$. Accordingly, 
we have $L^{(0)}=L^{(0)}_{\cusp}\cup L^{(0)}_{\textnormal{int}}$. 
Each point in $L^{(0)}_{\cusp}$ determines a parabolic subgroup of $\PSL(2,\C)$ 
stabilizing a unique point in $\C\cup\{\infty\}$. We thus have an equivariant 
map $D\colon L^{(0)}_{\cusp}\to \C\cup\{\infty\}$ taking a point to its 
stabilizer. Let $e_1$ and $e_2$ be points in $L^{(0)}_{\cusp}$ connected by an 
edge. Since all edges of $K$ are essential, $e_1\neq e_2$. It is well known 
that the point stabilizers of different cusps are distinct. Hence, 
$D(e_1)\neq D(e_2)$ if $e_1$ and $e_2$ correspond to different cusps. If 
$e_1$ and $e_2$ correspond to the same cusp, there exists an element in 
$\Gamma$ taking $e_1$ to $e_2$. Since only peripheral elements (i.e.~cusp 
stabilizers) have fixed points in $\Cinfty$, it follows that 
$D(e_1)\neq D(e_2)$. We extend $D$ to $L^{(0)}$ by choosing any equivariant 
map $L^{(0)}_{\textnormal{int}}\to\C\cup\{\infty\}$. Since such map is uniquely 
determined by finitely many values (which may be chosen freely), we can 
pick the extension so that the vertices of each simplex map to distinct 
points. This proves the result. 
\end{proof}

\begin{theorem}\label{Ptolemydetectsrhogeoproof} Suppose all edges of $K$ are essential. The representation $\phi_n\circ\rho_{\geo}$ is detected by $P_n(K)$ if $n$ is odd, and by $P_n^{\sigma_{\geo}}(K)$ if $n$ is even.
\end{theorem} 
\begin{proof}
By Proposition~\ref{detectsgeometric}, $P_2^{\sigma_{\geo}}(K)$ detects $\rho_{\geo}$. The result now follows from Corollary~\ref{adjointPtolemycor}.
\end{proof}

\begin{remark}
The census triangulations all have essential edges.
\end{remark}
