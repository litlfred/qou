---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-008-221-log-weights-and-boundary-weights
section_title: "Log weights and boundary weights"
section_number: 2.2.1
pages: 13-16
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.967
---
\label{sec:landbweights} As usual denote by $\bar M$ the compact manifold with interior $M$; so $\partial \bar M$ is a disjoint union of $c$ tori. Recall the holonomy map \eqref{defholmapSept24}. 
\smallskip

It is well-known that, besides the holonomy $\rho_w$, a point $w\in G(T,b)$ determines a group homomorphism 
\begin{equation}\label{dilationdef}
\fonc{\delta_w}{H_1(\partial \bar M; \mz)}{\mc^*}{\gamma}{\delta_{w}(\gamma).}
\end{equation}
Thus we have a map $\delta\colon G(T,b)\ra H^1(\partial \bar M; \mc^*)$, $w\mapsto \delta_w$. We  call $\delta$ the {\it dilation factor}. The scalar $\delta_w(\gamma)$ is the square of one among the two (reciprocally inverse) eigenvalues of $\rho_w(\gamma)$, and can be computed as a signed monomial in the classical shape parameters $w^i_k$ (see \cite{NZ}, or the formulas in \cite[Lemma E.6.8]{BP}; these formulas immediately follow from \eqref{formulekappa} below). If $T$ is a geometric triangulation, as defined in Section \ref{sec:tri_GV}, and $w$ is close enough to the point $w_{hyp}\in G(T,b)$, then $\delta_w$ is the holonomy of a similarity structure on $\partial \bar M$ (see, e.g., \cite[Proposition E.6.5]{BP}, \cite[Proposition 2.3]{PP}).
\smallskip

Similarly, by adjoining to $w\in G(T,b)$ a compatible system of edge colors $d$, one can define two  classes $h_2\in H^1(M;\mz/2\mz)$ and $l\kappa\in H^1(\partial \bar M; \mc)$, such that for all $\gamma \in H_1(\partial \bar M; \Z)$ we have (where $j^*\colon H^1(\bar{M},\mz/2)\ra H^1(\partial \bar{M},\mz/2)$ is induced by the inclusion $j\colon \partial \bar{M} \ra \bar{M}$):
\begin{align}
l\kappa(\gamma) & = \Log(\delta_{w}(\gamma)) \quad {\rm mod}(i\pi\mz) \label{lkconstraint0}\\
j^*(h_2)(\gamma) & = (l\kappa(\gamma)-\Log(\delta_{w}(\gamma)))/i\pi\quad{\rm mod} (2\mz).\label{h2class}
\end{align}
Let us explain this. To define the classes $l\kappa$ and $h_2$, first we stipulate that $l\kappa(0):=0$ and $h_2(0):=0$, for the $0$ classes in $H_1(\partial \bar M;\mz)$ or $H_1(M;\mz/2)$ respectively. Given a non-zero class $\gamma\in H_1(\partial \bar M;\mz)$, we represent it by a union of oriented simple closed curves in $\partial \bar M$ which are essential ({\it i.e.}, do not bound a disk) and transverse to the $1$-skeleton of $\partial T$, the triangulation of $\partial \bar M$ induced by $T$. We can assume that these curves have no ``back-tracking'', {\it i.e.}, they intersect each triangle of $\partial T$ in a disjoint union of segments. Call such curves {\it normal curves} in $\partial T$. If a triangle $F$ of $\partial T$ is a section of the tetrahedron $\Delta$ of $T$ near one of its vertices, for every vertex $v$ of $F$ denote by $E_v$ the abstract edge of $\Delta$ containing $v$, by $w(E_v)$ the classical shape parameter of $E_v$, by $d(E_v)$ its color, and by $*_v$ the branching sign of $\Delta$. Given a union of normal curves $C$, we write $F\colon C \rightarrow E_v$ to mean that $C$ intersects the triangle $F$ in subsegments joining the two edges of $F$ having $v$ has endpoint. We count these subsegments algebraically, by using the orientation of $C$: if there are $s_+$ (resp. $s_-$) such segments whose orientation is compatible with (resp. opposite to) the orientation of $\partial \bar M$ as viewed from $v$, then we set $ind(C,v) :=s_+-s_-$. Then, for any non zero class $\gamma\in H_1(\partial \bar M;\mz)$ represented by a union of normal curves $C$ in $\partial T$, we set (the sum is over all the triangles of $\partial T$)
\begin{equation}
  l\kappa(\gamma)  := \sum_{F\colon C \ra E_v} *_v \ ind(C,v)\left(\Log(w(E_v)) +\pi \sqrt{-1}d(E_v)\right) \label{formulelkappa}.
  \end{equation}
Similarly, we define the non oriented normal curves in $T$ as transverse to the $2$-skeleton and intersecting each tetrahedron in a disjoint union of segments. For any normal curve in $T$, we write $\Delta\colon C \rightarrow E$ to mean that $C$ intersects the tetrahedron $\Delta$ in subsegments joining the faces of $\Delta$ adjacent to an abstract edge $E$ of $\Delta$. For any such a tetrahedron, we denote by $ind(C,E)$ the number of these segments, and by $d(E)$ the color of $E$. Then, for any non-zero class $\gamma \in H_1(M;\mz/2)$ represented by a union of normal curves $C$ in $T$ we have (the sum is over all the tetrahedra of $T$)
  \begin{equation}
  h_2(\gamma) =\sum_{\Delta\colon C \ra E} \ ind(C,E)d(E) \quad{\rm mod} (2\mz). \label{formulebulkw}
\end{equation}
We call $l\kappa$ the {\it log weight} of $(w,d)$, and $h_2$ the {\it bulk weight}. In the particular case where $M$ is the complement of a knot $K$ in $S^3$, $H^1(\bar M; \mz/2)\cong \mz/2$ is generated by the meridian of $K$ and therefore $h_2$ is determined by $l\kappa$ (and it vanishes on the canonical longitude).
\begin{remark}\label{cfweight}{\rm One can associate classes $k_f\in H^1(\partial\bar{M};\mc)$ and $k_c\in H^1(\partial\bar{M};\mz)$ (and similarly classes $h_{2,f}$, $h_{2,c} \in H_1(M;\mz/2)$), respectively called {\it flattening weight} and {\it charge weight}, to flattenings $f$ and charge $c$ as in Remark \ref{defflatcharge}. Namely, $k_f$ is defined by the formula obtained from \eqref{formulelkappa} by replacing the color $d(E_v)$ with the flattening $f(E_v)$, and $k_c$ by the formula obtained from \eqref{formulelkappa} by replacing $*_v(\Log(w(E_v))+\pi \sqrt{-1}d(E_v))$ with the charge $c(E_v)$. Note that
\begin{equation}\label{fconstraint0}
k_f(\gamma)  = \Log(\delta_{w}(\gamma)) \quad {\rm mod}(i\pi\mz).
\end{equation}
Clearly
\begin{equation}\label{deflkappa}
	l\kappa= k_f-\pi ik_c.
\end{equation}
}\end{remark}

The following statement follows from results in  \cite{N0,N}. In the present notations, the first claim is Propositions 4.8 (2) and 4.9 (2) of \cite{AGT}, formulated for $l\kappa= k_f-\pi ik_c$. The generators in the second claim follow from the last claim of Lemma 6.1 in \cite{N0}, and the rank is a standard computation in the Neumann-Zagier combinatorics (\cite{NZ}). 
\begin{teo}\label{spaced} Let $w\in G(T,b)$. For any classes $h_2\in H^1(M;\mz/2\mz)$ and $l\kappa\in H^1(\partial \bar M; \mc)$ satisfying \eqref{lkconstraint0} and \eqref{h2class} there is a system of edge colors $d$ satisfying \eqref{formulelkappa} and \eqref{formulebulkw}. Moreover, the set formed by these systems of edge colors is an affine space over a $\mz$-lattice of rank $n-p$ (where $p$ is the number of cusps) generated by vectors in one-to-one correspondence with the edges of $T$.
\end{teo}
In such a situation we say that $(h_2, l\kappa)$ and $(w,d)$, or $(h_2, l\kappa)$ and the corresponding tuple of quantum shape parameters $\bw\in G_N(T,b)$ defined by the formula \eqref{coldef}, are {\it compatible}. For simplicity we will often omit $d$ from the notations, and say that $l\kappa$ and $w$, or $l\kappa$ and $\bw$, or $l\kappa$ and the $PSL(2,\mc)$-character $\rho_w = hol(w)$, are compatible.  For a link complement $M$ the map $j^*\colon H^1(\bar{M},\mz/2)\ra H^1(\partial \bar{M},\mz/2)$ is an isomorphism, so $h_2$ is given by $l\kappa$ and $\delta_w$ via the relation \eqref{h2class}.  
\smallskip

Similarly to \eqref{formulelkappa}, denoting by $\bw(E_v)$ the quantum shape parameter of an abstract edge $E_v$, we can associate to any point $\bw\in G_N(T,b)$ a class $\kappa_\bw\in H^1(\partial \bar M; \mc^*)$ defined by
\begin{equation}
 \kappa_\bw(\gamma)  := \prod_{F\colon C \ra E_v} \bw(E_v)^{*_v ind(C,v)} \label{formulekappa}.
\end{equation}
We call $\kappa_\bw$ the {\it boundary weight} of $\bw$. Clearly $\kappa_\bw(\gamma)^{N}= \delta_{w}(\gamma)$, and if $d\in \mz^{3n}$ is a compatible tuple of edge colors with bulk and log weights $h_2$ and $l\kappa$, for every $\gamma\in H_1(\partial \bar M; \Z)$ we have
\begin{equation}\kappa_\bw(\gamma)  = \exp\left(\frac{l\kappa(\gamma)}{N}+(\pi i) j^*(h_2)(\gamma)\right). \label{kappaborddef}
\end{equation}
Consider the covering map
\begin{equation}\label{coverGN}
\fonc{\pi_N}{G_N(T,b)}{G(T,b)}{\bw = (\bw_k^i)}{w = ((\bw_k^i)^N).}
\end{equation}
Theorem \ref{spaced} (or its proof, using systems of $N$-colors) implies:
\begin{teo}\label{teocoverGN} The map $\pi_N$ has degree $N^{n+p}$. 
\end{teo}
Note that the exponent decomposes as $n+p=n-p+2p$, where $n-p$ follows from Theorem  \ref{spaced}, and $2p$ comes from the degree of freedom in the choice of $\kappa_\bw$. 


\subsubsection{The spaces $G_{hyp,N}(T,b)$ and ${}_NX_{hyp}(M)$}\label{GhypN}{\rm (See \cite[Section 4]{AGT}.) Let $T$ be a geometric triangulation of $M$. We saw in Section \ref{sec:tri_GV} that $w_{hyp}$ is a smooth point of $G(T,b)$. Denote its irreducible component by $G_{hyp}(T,b)$. In this section we discuss some of its remarkable properties, and explain how the map \eqref{coverGN} can be given an intrinsic definition over $G_{hyp}(T,b)$.
\smallskip

We need to recall the following results:
\smallskip

(a) The character $\rho_{hyp}$ of the discrete faithful representations of $\pi_1(M)$ into $PSL(2,\mc)$ is a smooth point of $X(M)$, and thus is contained in a unique irreducible component $X_{hyp}(M)$ of $X(M)$; moreover ${\rm dim}_\mc(X_{hyp}(M)) = p$, the number of cusps of $M$ (see \cite[Chapter 4.5]{Shalen}, \cite[Theorem 8.44]{Kapo}). We call $X_{hyp}(M)$ the {\it geometric component} of $X(M)$.
\smallskip

(b) Dunfield \cite{Dun} showed that the (regular) restriction map $r\colon X_{hyp}(M) \ra X(\partial \bar M)$ is a birational isomorphism onto its image, in the case when $M$ has a single cusp.  This result has been extended by Klaff-Tillmann \cite{KT} to an arbitrary number of cusps. 
\smallskip

(c) The $PSL(2,\mc)$-characters of $M$ can be ``augmented'' (\cite{Champ,BD}): an augmented character $\tilde{\rho}$ consists of a character $\rho\in X(M)$ together with a conjugation invariant choice of a fixed point of $\rho(\pi_1(\partial \bar{M}))$, for each peripheral subgroup $\pi_1(\partial \bar{M})$ of $\pi_1(M)$. Such a choice is equivalent to selecting the square of one among the two (reciprocally inverse) eigenvalues of $\rho(\gamma)$, for each peripheral element $\gamma$ of $\pi_1(M)$; hence it defines a class $\delta_{\tilde \rho}\in H^1(\partial \bar M;\mc^*)$. The set of augmented characters $\tilde{X}(M)$ is algebraic, and has a canonical irreducible component $\tilde{X}_{hyp}(M)$ containing the augmentation of $\rho_{hyp}$ (it is unique, since $\rho_{hyp}$ maps elements of $\pi_1(\partial \bar M)$ to parabolic transformations). 
\smallskip

Now, identify $H^1(\partial \bar M;\mc^*)$ with $(\mc^*\times \mc^*)^p$ by fixing a basis $(\mu_1,\lambda_1,\ldots, \mu_p,\lambda_p)$ of $H_1(\partial \bar M;\mz)$. The map $\tilde{X}_{hyp}(M) \rightarrow X_{hyp}(M)$, $\tilde{\rho}= (\rho,\delta_{\tilde \rho}) \mapsto \rho$, is regular, generically $2^p\colon 1$, and the map
$$\fonc{\delta^X}{\tilde{X}_{hyp}(M)}{H^1(\partial \bar M;\mc^*)\cong (\mc^*\times \mc^*)^p}{\tilde{\rho}}{\delta_{\tilde \rho}}$$ is regular. The map $(\mc^*\times \mc^*)^p\ra X(\partial \bar M)=X(T^2)^p$, which sends the $i$-th entry $(m_i^2,\ell_i^2)$, $i=1,\ldots, p$, to the coset in $X(T^2)$ of the pair
$$\left( \pm \begin{pmatrix} m_i & 0 \\ 0 & m_i^{-1}\end{pmatrix}, \pm \begin{pmatrix} \ell_i & 0 \\ 0 & \ell_i^{-1}\end{pmatrix}\right) \in PSL(2,\mc)^2,$$ is generically $2^p\colon 1$. Since $r\colon X_{hyp}(M) \ra X(\partial \bar M)$ has degree one, it follows that $\delta^X$ has degree one, and is therefore a birational isomorphism onto its image. We thus get the bottom right square of the following commutative diagram, whose description we complete below.
$$\xymatrix{ &  {}_NX_{hyp}(M) \ar[d]^{\pi_N^X} \ar[r]^{\kappa^X} & (\mc^* \times \mc^*)^p \ar[d]^{((.)^N \times (.)^N)^p} \\ G_{hyp,N}(T,b)  \ar[d]_{\pi_N} \ar[r] \ar[ru]^{\widetilde{hol}} & \tilde{X}_{hyp}(M) \ar[r]^{\delta^X} \ar[d]^{2^p:1} & (\mc^* \times \mc^*)^p \ar[d]^{2^p:1}\\G_{hyp}(T,b) \ar[r]^{hol_{\vert}}\ar[ru]^{\tilde{hol}_{\vert}} & X_{hyp}(M) \ar[r]^{r} & X(\partial \bar M)}$$

Let $T$ be a geometric triangulation of $M$, and $G_{hyp}(T,b)\subset G(T,b)$ the irreducible component of $w_{hyp}$. Using the dilation factor \eqref{dilationdef}, the holonomy map $hol$ in \eqref{defholmapSept24} lifts to a regular map $\tilde{hol}\colon G(T,b)\rightarrow \tilde{X}(M)$, $w\mapsto (\rho_w,\delta_w)$, such that that $\delta_w = \delta^X \circ \tilde{hol}(w)$. We have:
\begin{prop} {\rm (\cite[Proposition 4.6]{AGT} and \cite[Remark 1.4]{NA}) The restriction  
\begin{equation}\label{tildeholresmars25}
\tilde{hol}_{\vert}\colon G_{hyp}(T,b)\rightarrow \tilde{X}_{hyp}(M)
\end{equation}
is a birational isomorphism, and the dilation factor $\delta\colon G_{hyp}(T,b)\rightarrow H^1(\partial \bar M;\mc^*)\cong (\mc^*\times \mc^*)^p$ is a birational isomorphism onto its image.}
\end{prop}
The proof combines Thurston's hyperbolic Dehn filling theorem in the form of \cite{PP, Martelli} with Dunfield's arguments showing that $r$ has degree one.

Set
\begin{equation}\label{GhypNdef}
G_{hyp,N}(T,b):= \pi_N^{-1}(G_{hyp}(T,b)),
\end{equation} with $\pi_N$ the map \eqref{coverGN}. Define ${}_NX_{hyp}(M)$ as the set of pairs $(\rho,\kappa)$ where $\rho \in X_{hyp}(M)$, $\kappa\in H^1(\partial \bar M;\mc^*)$, and $\kappa^{N}(\gamma)$ is a squared eigenvalue of $\rho(\gamma)$ for all $\gamma\in H_1(\partial \bar M;\mz)$. Thus ${}_NX_{hyp}(M)$ has the structure of a fibered product $X_{hyp}(M) \times_{X(\partial \bar M)} H^1(\partial \bar M;\mc^*)$. Clearly, the map $\pi_N^X\colon {}_NX_{hyp}(M)\ra \tilde X_{hyp}(M)$, $(\rho,\kappa)\mapsto (\rho, \kappa^N)$, has degree $N^{2p}$. Consider the ``boundary weight map'' (see \eqref{kappaborddef})
\begin{equation}\label{defweightSept24}
\fonc{\kappa}{G_{hyp,N}(T,b)}{H^1(\partial \bar M;\mc^*)}{\bw}{\kappa_\bw.}
\end{equation}
Since $\kappa_\bw(\gamma)^{N}= \delta_w(\gamma)$, we can lift $\tilde{hol}_{\vert}$ to a regular map
\begin{equation}\label{grostildeholmars25}
\fonc{\widetilde{hol}}{G_{hyp,N}(T,b)}{{}_NX_{hyp}(M)}{\bw}{(\rho_w,\kappa_\bw).}
\end{equation}
It has degree $N^{n-p}$ (see Theorem \ref{teocoverGN} and the comment thereafter), and by construction $$\pi_N = (\tilde{hol}_{\vert})^*\pi_N^X.$$ Finally $\kappa^X\colon {}_NX_{hyp}(M) \ra \mc^* \times \mc^*$ is defined by $\kappa^X(\rho,\kappa) = (\kappa(\mu_K), \kappa(\lambda_K))$; so $\kappa = \kappa^X \circ \widetilde{hol}$.

\begin{remark}\label{mostrho}{\rm (see \cite[Proposition 4.6 and pages 2017-2019]{AGT} and \cite[Remark 1.4]{NA}). Denote by EP the set of triangulations obtained by subdividing the Epstein-Penner polyhedral decomposition  of $M$. For every $T\in EP$, fix a branchings $b_T$ of $T$ as at the beginning of Section \ref{sec:tri_GV}, and set $Z_T:=G_{hyp}(T,b_T)\subset G(T,b_T)$. There is a maximal Zariski open subset $\Omega_{Z_T}$ in $Z_T$ containing $w_{hyp}$, such that $hol(\Omega_{Z_T})$ is Zariski open in $X_{hyp}(M)$ and $hol\colon \Omega_{Z_T} \ra hol(\Omega_{Z_T})$ is a homeomorphism. Then $$\Omega := \bigcap_{T\in {\rm EP}} hol(\Omega_{Z_T})$$
is a canonical Zariski open subset $\Omega$ of $X_{hyp}(M)$ which contains $\rho_{hyp}$ and whose points can be (uniquely) encoded by points in the components $G_{hyp}(T,b)$, for every $T\in EP$.}
\end{remark}
