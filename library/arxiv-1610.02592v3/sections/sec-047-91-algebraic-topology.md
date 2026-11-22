---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-047-91-algebraic-topology
section_title: "Algebraic topology"
section_number: 9.1
pages: 277-280
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.943
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
The algebraic topology of compact three-manifolds is not very complicate. 


\subsection{Integral homology}
In this section all the homology groups are considered over $\matZ$. We first note that, for closed orientable 3-manifolds, the fundamental group determines everything.

\begin{prop}
The homology $H_*(M)$ of a closed orientable 3-manifold $M$ is determined by $\pi_1(M)$. 
\end{prop} 
\begin{proof}
As in every path connected space, the group $H_1(M)$ is the abelianisation of $\pi_1(M)$ and $H^1(M) = \Hom(H_1(M),\matZ)$, which is hence isomorphic to $H_1(M)$ modulo its torsion. By Poincar\'e duality $H_2(M) = H^1(M)$ and $H^2(M) = H_1(M)$. Finally $H_3(M) = \matZ$.
\end{proof}


\subsection{Homology spheres}
A \emph{homology $n$-sphere} is a closed orientable $n$-manifold $M$ whose homology is the same as that of $S^n$. That is, we have $H_0(M) = H_n(M) = \matZ$ and $H_i(M)$ vanishes for all $0<i<n$.\index{homology sphere} 

By Poincar\'e duality, a closed 3-manifold $M$ is a homology sphere if and only if $H_1(M)$ vanishes. Since $H_1(M)$ is the abelianization of $\pi_1(M)$, this happens precisely when $\pi_1(M)$ is a \emph{perfect group}, that is a group with trivial abelianization.\index{group!perfect group} 

In 1900 Poincar\'e conjectured that every homology 3-sphere should be homeomorphic to $S^3$. Four years later, he found himself a counterexample by constructing what is known today as \emph{Poincar\'e's homology sphere}, a closed 3-manifold with a perfect fundamental group of order 120. He then modified his original conjecture by asking whether every simply connected closed 3-manifold should be homeomorphic to $S^3$. This fact, widely known as \emph{Poincar\'e's Conjecture}, was proved only in 2002 by Perelman.

We will construct Poincar\'e's homology sphere (and many more homology spheres) in Chapter \ref{Seifert:chapter}, and we will discuss the Poincar\'e Conjecture in Section \ref{geometrisation:section}, as a part of Thurston's wider \emph{Geometrisation Conjecture}, also proved by Perelman in 2002.


\subsection{The boundary}
The Euler characteristic $\chi(M)$ of a closed odd-dimensional manifold vanishes, and on manifolds with boundary we have the following.

\begin{prop}
If $M$ is a compact 3-manifold with boundary, then 
$$\chi(M) = \frac {\chi(\partial M)}2.$$
\end{prop}
\begin{proof}
We only use that $M$ has odd dimension $n$. If $M$ is closed and orientable, we have $\chi(M) = \sum_{i=0}^n (-1)^i b_i$ and the Betti numbers $b_i$ and $b_{n-i}$ are equal by Poincar\'e duality, hence $\chi(M)=0$. If $M$ is non-orientable then it has an orientable double-cover $N$ and $\chi(N) = d\chi(M)$ on degree-$d$ covers, hence $\chi(N)=0$ implies $\chi(M)=0$.
If $M$ has boundary then 
$$0 = \chi(DM)=2\chi (M) - \chi(\partial M)$$
where $DM$ is the \emph{double} of $M$, constructed by taking two identical copies of $M$ and identifying their boundaries in the obvious way.
\end{proof}

The manifold $M$ has half the Euler characteristic of $\partial M$, and is also responsible for half of the first homology group of $\partial M$. More precisely, we are interested in the boundary map
$$\partial\colon H_2(M,\partial M) \longrightarrow H_1(\partial M)$$
and we want to prove that its image is a particular half-dimensional subgroup.
Recall from Proposition \ref{homology:prop} that every class in $H_2(M,\partial M)$ is represented by an oriented properly embedded surface $\Sigma$, and $\partial$ sends $[\Sigma]$ to $[\partial \Sigma]$.

Let $M$ be oriented. The boundary $\partial M$ may be disconnected and inherits an orientation. Recall that $H_1(\partial M)\isom \matZ^{2n}$ for some $n$ and $H_1(\partial M)$ is equipped with a symplectic intersection form $\omega$, see Section \ref{homolgy:surface:subsection}. A subgroup $L<H_1(\partial M)$ is \emph{lagrangian} if $\omega|_L\equiv 0$.\index{lagrangian subgroup} 

\begin{ex}
If $L$ is lagrangian then $\rk L \leqslant n$.
\end{ex}
When $\rk L = n$ we say that $L$ has maximal rank.

\begin{prop}  \label{lagrangian:prop}
Let $M$ be an oriented compact 3-manifold with boundary. The image of the map 
$$\partial \colon H_2(M,\partial M, \matZ) \longrightarrow H_1(\partial M,\matZ)$$
is a lagrangian subgroup of $H_1(\partial M, \matZ)$ of maximal rank.
\end{prop}
\begin{proof}
Consider the long exact sequence
$$\ldots \longrightarrow H_2(M,\partial M) \stackrel{\partial}\longrightarrow H_1(\partial M) \stackrel{i_*}\longrightarrow H_1(M) \longrightarrow \ldots$$
We have two pairings
\begin{align*}
\omega \colon H_1(\partial M) \times H_1(\partial M) & \longrightarrow  \matZ, \\
\eta \colon H_2(M,\partial M) \times H_1(M) & \longrightarrow \matZ.
\end{align*}
The latter is provided by Lefschetz duality and is non-degenerate after quotienting the torsion subgroups. We have
$$\omega (\partial \alpha, \beta) = \eta (\alpha, i_*\beta)$$
for all $\alpha \in H_2(M,\partial M)$ and $\beta \in H_1(M)$: this equality can be proved easily by representing the elements of $H_2(M,\partial M)$ as surfaces (which we can do thanks to Proposition \ref{homology:prop}). Now if $\beta = \partial\alpha'$ we get 
$$\omega(\partial \alpha, \partial \alpha') = \eta(\alpha, i_*\partial \alpha') = \eta(\alpha,0) = 0$$
and hence $\Img \partial$ is lagrangian. It has maximal rank since $H_2(M,\partial M)=H^1(M)$ and $H_1(M)$ have the same rank: if $\rk\, \Img \partial < \frac 12 b_1(\partial M)$, then we get $\rk \,\Img i_* > \frac 12 b_1(\partial M)$ and $\rk \ker\partial > b_1(M) - \frac 12 b_1(\partial M)$, a contradiction since $\Img i_*$ and $\ker\partial$ are $\eta$-orthogonal.
\end{proof}

\begin{cor} \label{rank:cor}
Let $M$ be an oriented compact 3-manifold. We have 
$$b_1(M)\geqslant \frac {b_1(\partial M)}2.$$
\end{cor}
\begin{proof}
The rank of $H_1(M)$ equals that of $H^1(M) = H_2(M,\partial M)$.
\end{proof}

\begin{cor}
The boundary of a simply connected compact 3-manifold consists of spheres.
\end{cor}


\subsection{Non-orientable surfaces}
Let $M$ be an orientable 3-manifold and $S\subset M$ be a connected surface. If $S$ is orientable, then by Proposition \ref{unique:line:bundle:prop} every tubular neighbourhood for $S$ is diffeomorphic to the product $S \times \matR$.

The orientable manifold $M$ may also contain a \emph{non}-orientable surface $S$: for instance the orientable projective space $\matRP^3$ contains the non-orientable projective plane $\matRP^2$. In that case a tubular neighbourhood of $S$ is diffeomorphic to the unique orientable interval bundle $S\timtil \matR$ over $S$, see Proposition \ref{unique:line:bundle:prop} again. A compact tubular neighbourhood of $S$ is an interval bundle $S\timtil I$, whose boundary is the orientable double cover of $S$. For instance, the boundary of $\matRP^2 \timtil I$ is a sphere.

A non-orientable properly embedded surface $S\subset M$ does not define a homology class in $\matZ$, but it defines one in $\matZ_2$, that is  $[S] \in H_2(M,\partial M;\matZ_2)$. As opposite to orientable surfaces, this class $[S]$ is always non-trivial.

\begin{prop} \label{non:ori:prop}
Let $M$ be orientable. Every non-orientable surface $S$ determines a non-trivial class $[S] \in H_2(M,\partial M;\matZ_2)$. The manifold $M$ cannot contain more than $\dim H_2(M,\partial M;\matZ_2)$ disjoint non-orientable surfaces.
\end{prop}
\begin{proof}
A tubular neighbourhood $S\timtil I$ of $S$ contains a simple closed loop $\alpha$ intersecting $S$ transversely in one point. The class $[S] \in  H_2(M,\partial M;\matZ_2) = H^1(M;\matZ_2) $ sends $\alpha$ to $1\in\matZ_2$ and is hence non-trivial. If $S=S_1\sqcup\ldots \sqcup S_k$ are all non-orientable, each $S_i$ has its own $\alpha_i$ and therefore the elements $[S_1], \ldots, [S_k] \in H_2(M,\partial M;\matZ_2)$ are linearly independent.
\end{proof}

\begin{cor} A simply-connected three-manifold does not contain any closed non-orientable surface.
\end{cor}
