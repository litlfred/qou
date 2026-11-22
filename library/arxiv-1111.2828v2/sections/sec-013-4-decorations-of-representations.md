---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-013-4-decorations-of-representations
section_title: "Decorations of representations"
section_number: 4
pages: 13-14
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.966
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sec.decorations}

In this section we review the notion of decorated representations 
introduced in Zickert~\cite{ZickertDuke}. Throughout the section, $G$ 
denotes an arbitrary group, not necessarily a Lie group. Let $H$ be subgroup 
of $G$. An \emph{ordered simplex} is a simplex with a fixed vertex ordering.

\begin{definition}
\lbl{cycledefn} 
A \emph{closed $3$-cycle} is a cell complex $K$ obtained from a finite 
collection of ordered $3$-simplices $\Delta_i$ by gluing together pairs 
of faces using order preserving simplicial attaching maps. We assume that 
all faces have been glued, and that the space $M(K)$, obtained by truncating 
the $\Delta_i$'s before gluing, is an oriented $3$-manifold with boundary. 
Let $\epsilon_i$ be a sign indicating whether or not the orientation of 
$\Delta_i$ given by the vertex ordering agrees with the orientation of $M(K)$.
\end{definition}

Note that up to removing disjoint balls (which does not effect the 
fundamental group), the manifold $M(K)$ only depends on the underlying 
topological space of $K$, and not on the choice of $3$-cycle structure. 
Also note that for any compact, oriented $3$-manifold $M$ with 
(possibly empty) boundary, the space $\widehat M$ obtained from $M$ by 
collapsing each boundary component to a point has a structure of a closed 
$3$-cycle $K$ such that $M=M(K)$. 

Let $K$ be a closed $3$-cycle, and let $M=M(K)$. Let $L$ denote the space 
obtained from the universal cover $\widetilde M$ of $M$ by collapsing each 
boundary component to a point. The $3$-cycle structure of $K$ induces a 
triangulation of $L$, and also a triangulation of $M$ by truncated simplices. 
The covering map extends to a map $L\to K$, and the action of $\pi_1(M)$ on 
$\widetilde M$ by deck transformations extends to an action on $L$, which is 
determined by fixing, once and for all, a base point in $M$ together with 
one of its lifts. 
Note that the stabilizer of each zero cell is a \emph{peripheral} subgroup 
of $\pi_1(M)$, i.e.~a subgroup induced by inclusion of a boundary component. 

\begin{definition} 
Let $H$ be a subgroup of $G$. A representation $\rho\colon\pi_1(M)\to G$ is a 
$(G,H)$-\emph{representation} if the image of each peripheral subgroup is a 
conjugate of $H$. 
\end{definition}

\begin{definition}
\lbl{decorationdefn} 
Let $\rho$ be a $(G,H)$-representation. A \emph{decoration} (on $K$) of 
$\rho$ is a $\rho$-equivariant assignment of a left $H$-coset to each vertex 
of $L$, i.e.~if $\alpha\in\pi_1(M)$ and the coset $g_eH$ is assigned to $e$, 
the coset assigned to $\alpha e$ must be $\rho(\alpha)g_eH$.
\end{definition}

Note that $g_e^{-1}\rho(\Stab(e))g_e\subset H$, where $\Stab(e)$ is the 
stabilizer of $e$. 

\begin{definition} 
Two decorations $\{g_eH\}$ and $\{g^\prime_eH\}$ of $\rho$ are 
\emph{equivalent} if the corresponding subgroups $g_e^{-1}\rho(\Stab(e))g_e$ and 
$g^{\prime-1}_e\rho(\Stab(e))g^\prime_e$ of $H$ are conjugate (in $H$).
\end{definition}
 
Note that if $\{g_eH\}$ is a decoration of $\rho$, then $\{gg_eH\}$ is a 
decoration of $g\rho g^{-1}$. Since we are only interested in representations 
up to conjugation, we consider such two decorations to be equal.

\begin{remark}
\lbl{normalizerremark} 
Letting $N_G(H)$ denote the normalizer of $H$ in $G$, and $h$ the number of 
boundary components of $M$, right multiplication induces an action of $(N_G(H)/H)^h$ on the set of equivalence classes of 
decorations. If $G=\SL(n,\C)$ and $H=N$, $N_G(H)/H$, is the group of diagonal matrices, and since two subgroups of $N$ are conjugate if and only if they are conjugate by an element in the Borel subgroup $B$ of upper diagonal matrices, this action is transitive.
\end{remark}

\begin{proposition}
\lbl{decorationeqreduction} 
Let $E$ be a flat $G$-bundle over $M$ whose holonomy representation is a 
$(G,H)$-representation $\rho$. There is a $1$-$1$ correspondence between 
decorations of $\rho$ up to equivalence, and reductions of $E_{\partial M}$ to 
an $H$-bundle over $\partial M$.
\end{proposition}

\begin{proof} 
For each boundary component $S_i$ of $M$, choose a base point in $S_i$ and 
a path to the base point of $M$. This determines a lift $e_i$ in $L$ of the 
vertex of $K$ corresponding to $S_i$, and an identification of $\pi_1(S_i)$ 
with $\Stab(e_i)\subset\pi_1(M)$. If $F$ is a reduction of $E_{\partial M}$, the 
holonomy representations $\rho_i\colon\pi_1(S_i)\to H$ of $F_{S_i}$ are 
conjugate to $\rho$, so there exist $g_i\in G$ such that 
$g_i^{-1}\rho g_i=\rho_i$. Assigning the coset $g_iH$ to $e_i$ yields a 
decoration, which up to equivalence is independent of the choice of $g_i$'s. 
On the other hand, a decoration assigns cosets $g_iH$ to $e_i$ such that 
$g_i^{-1}\rho(\Stab(e_i))g_i\subset H$. Hence, $g_i$ defines an isomorphism 
of $E_{S_i}$ with an $H$-bundle, which up to isomorphism only depends on the 
equivalence class of the decoration.
\end{proof}
