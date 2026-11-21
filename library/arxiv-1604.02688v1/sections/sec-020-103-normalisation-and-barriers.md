---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-020-103-normalisation-and-barriers
section_title: "Normalisation and barriers"
section_number: 10.3
pages: 30-35
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.97
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{barriers}

There is a well-known procedure going back to Kneser \cite{Kn} for 
`normalisation' of an embedded closed surface $S$ in a triangulation $\T$ 
of a manifold $M$. We can assume initially that the surface $S$ is 
transverse to the triangulation.There are five basic moves: 

\begin{enumerate}
\item 
Compress $S$ along an embedded disk $D$ in the interior of a tetrahedron 
$\D$, which meets $S$ in $C=\partial D$, where  either $C$ is essential in 
$S$ or a disk bounded by $C$ in $S$ meets $\partial \D$. 
\item 
Isotope a disk $D^\prime$ of intersection of $S$ with a tetrahedron across a 
face of the tetrahedron, where $\partial D^\prime$ lies in a face and is an 
innermost curve in that face. 
\item 
Isotope an innermost arc of intersection of $S$ with a face of the 
triangulation across an edge. Here the arc has both ends on the edge and 
there are no intersections of $S$ with the bigon cut off by the arc in 
the face. 
\item 
Boundary compress the intersection of $S$ with a tetrahedron. This occurs 
along a bigon which intersects $S$ in one arc of its boundary with the 
other arc contained in an edge of the tetrahedron. 
\item
Finally, any component which is a sphere contained in the interior of a 
tetrahedron is removed.
\end{enumerate}

Kneser \cite{Kn} and Haken \cite{Ha1} show that any surface can either be 
{\em normalised}, i.e. either converted to a non-empty normal surface 
by a sequence of such moves,  or else converted to the empty surface.

\begin{rmk}
If an embedded sphere $S$ or an embedded torus $T$ is converted to the 
empty surface when normalised in one of its complementary regions,
then that region is a 3-ball or solid torus in $M$ bounded by $S$ or $T$ 
respectively. 

In fact, if $S$ or $T$ did not bound a 3-ball or solid torus respectively 
then there is no isotopy or a disk compression followed by an isotopy, 
shrinking $S$ or $T$ respectively to a point. 
\end{rmk}

\begin{defn}
An embedded surface $S^\prime$ is a {\it barrier} for the normalisation of 
$S$ if it satisfies the following conditions. Firstly, 
$S^\prime \cap S = \emptyset$. Secondly, $S$ can be normalised by moves 
in the complement of $S^\prime$. 
\end{defn}

\begin{thm} 
Let $\T$ be an ideal triangulation  of compact manifold with boundary 
consisting of tori. Suppose that $S^\prime$ is a ``simple'' embedded 
generalised normal surface in $\T$, i.e. has at most one generalised 
normal disk in each tetrahedron. Then $S^\prime$ is a barrier for 
normalisation of any surface in its complement. 
\end{thm}

\begin{proof}
Consider the two regions $R, R^\prime$ obtained by splitting a tetrahedron 
$\D$ open along a generalised normal disk $D$ in $S'$. 
The faces of these regions consist of a copy of $D$ and the result of 
splitting the faces of $\D$ open along $\partial D$. 
The latter produce faces which are either triangles, quadrilaterals or 
pentagons. (Hexagons cannot arise since a generalised normal disk has at 
most two different arc types in any triangular face of $\D$.)

Choose a maximal family of disjoint non parallel properly embedded bigon 
compressing disks for each of the regions $R,R'$, as in the fourth 
normalisation move.  Thus, a quadrilateral face  of $R$ or  $R^\prime$ 
has two associated bigon disks, one along each edge of $\D$ in its 
boundary, whereas a pentagon has one such bigon. (Figure \ref{fig:12gon} 
exhibits the case where $D$ is a 12-gon, with $\bd \D$ stereographically 
projected to the plane.)

\begin{center}
\begin{figure}
\includegraphics[width=0.3\textwidth]{figures/12gon} \qquad\qquad
\includegraphics[width=0.3\textwidth]{figures/12gon_in_tet}


\caption{\label{fig:12gon} (left) A schematic diagram of the 12-gon 
determined by coordinates $(2,1,0)$. (right) An embedding of this 12-gon. 
The region $R$ faces the dark (red) shaded side, while $R'$ faces the 
lighter side.}
\end{figure}
\end{center}

If either region is compressed along all these disks, each of the 
resulting components is either a tetrahedron, where the compression of $D$ 
gives a face of the tetrahedron, or a 3-ball with boundary a pair of disks, 
where one disk is the result of compressing $D$ and the other disk is in 
a face of $\D$. 

Suppose that $S$ is a surface disjoint from $S^\prime$. If $S$ meets either 
region $R, R^\prime$, then notice that the intersection of $S$ with the 
above families of bigon disks can be used to perform normalisation moves 
on $S$ in the complement of $S^\prime$. For if there is a loop $C$ in 
$S \cap  D_i$ where $D_i$ is one of the bigon disks and either $C$ is 
essential on $S$ or a disk bounded by $C$ in $S$ meets $\partial \D$, 
then this gives a first normalisation move.  On the other hand, if there 
are arcs in $S \cap  D_i$, these give third or fourth normalisation moves. 

After performing all such normalisation moves, the resulting surface 
again denoted by $S$ is still disjoint from $S^\prime$ 
but also from all the bigon disks in  $R, R^\prime$. It is easy to see that 
we can perform additional first or second normalisation 
moves  so that $S \cap  \D$ consists entirely of triangular normal disks 
and spheres in interior $\D$ and after discarding any 
sphere components  we have normalised $S$ in $\D$. 

This argument can clearly be performed in all tetrahedra containing a 
generalised normal disk, and in tetrahedra containing only normal disks, 
the argument in \cite{JR} applies. This completes the proof. 
\end{proof}

\begin{cor}
\label{barrier}
If $S^*$ is a two-sided embedded ``simple'' generalised normal surface 
(i.e. has at most one generalised normal disk in each tetrahedron), then 
it can be pushed off itself to either side and normalised in its complement.
\end{cor}

\begin{rmk}
\label{surface_dies}
If we consider an arbitrary generalised normal surface $S^*$ which is not 
necessarily simple, the same idea shows that any surface $S$ in the 
complement of $S^*$ can be transformed into a {\em generalised} normal 
surface, by moves similar to the ones above for normalisation. 
The difference in this case is that if $S^*$ has parallel generalised 
normal disks bounding a product region $R$ in a tetrahedron and $S$ meets 
$R$,  then $S$ might be transformed to intersect $R$ in 
parallel copies of these generalised normal disks. 
\end{rmk}

\begin{thm}
\label{euler_for_gen_norm_surf}
Let $\T$ be a 1-efficient ideal triangulation of a cusped, orientable 
3-manifold $M$, and assume that $M$ is not a solid torus or $T^2 \times I$.
Then $\T$ contains no closed embedded simple generalised normal surface 
$\tilde S$ with $\chi(\tilde S) \ge 0$.
\end{thm} 

\begin{proof} 
Recall that $\T$ 1-efficient implies that $M$ is irreducible and atoroidal. 
Suppose first that $\tilde S$ is two-sided in $M$. Now by the barrier 
argument in Corollary \ref{barrier}, we can push the simple generalised 
surface $\tilde S$ off itself on either side, and normalise it. The result 
is either (i) a normal sphere, or (ii) a normal torus, or else
(iii) the surface becomes empty. 
 
The first case clearly contradicts the assumption of 1-efficiency. 

In the second case, note that the surface may normalise to a peripheral 
torus at a cusp when it is pushed off itself to a side containing a cusp. 
Since we are assuming that $M$ is not $T^2 \times I$, it follows that 
normalisation to a peripheral torus cannot occur on both sides of a 
generalised normal torus. But then, pushing off to at least one side, we 
would get a normal torus which is topologically but not normally parallel 
into a cusp, again contradicting 1-efficiency.  

So we are left with the case that the surface becomes empty. If $\tilde S$ 
is a sphere, it cannot bound a ball on both sides 
and hence yields a normal sphere on one side or the other by 
Remark \ref{surface_dies}, contrary to assumption. 

If $\tilde S$ is a torus, it could be compressible. In this case, the 
torus bounds a solid torus or cube-with-knotted-hole. 
In the latter case, the sphere resulting from compressing $\tilde S$ 
does not bound a ball in the complement of $\tilde S$ 
so can be normalised giving a normal sphere, contrary to assumption. 
So we are left with the final case, where $\tilde S$  is a torus bounding 
a solid torus. The other side of $\tilde S$ must contain a cusp of $M$. 
But then if $\tilde S$ is compressible on this side, 
the result is a sphere which can be normalised, contradicting the 
assumption of 1-efficiency.  On the other hand, if $\tilde S$ is 
incompressible on the side containing a cusp, either $\tilde S$ normalises 
to give a non-peripheral normal torus, contrary to 1-efficiency, 
or $M$ is a solid torus, which is excluded by our hypothesis. So the case 
where $\tilde S$ is two-sided is complete. 

If the generalised normal surface $\tilde S$ is one-sided it is a 
projective plane or Klein bottle. The first case contradicts 
irreducibility. If  $\tilde S$ is a Klein bottle, the boundary of a small 
regular neighbourhood of $\tilde S$ is either an  incompressible torus, 
contradicting the atoroidal assumption, or compressible and $M$ is a 
closed prism manifold, contradicting the hypothesis that $M$ has a cusp. 
This completes the proof. 
\end{proof}

\begin{lemma} 
\label{solid_torus_gen_norm}
Let $\T$ be a 1-efficient ideal triangulation of $M$, which is either a 
solid torus or $T^2 \times I$. Then $\T$ contains no closed embedded 
simple generalised normal surface $\tilde S$ with $\chi(\tilde S) > 0$,
and no closed embedded normal surface $\tilde S$ with $\chi(\tilde S) = 0$ 
which is non-peripheral. However, $\T$ always contains a closed embedded 
generalised normal $\tilde S$ with $\chi(\tilde S) = 0$.
In fact, there is an almost normal torus $\tilde S$ containing one 
octagonal disk.
\end{lemma}

\begin{proof} 
If there was a simple generalised normal surface $\tilde S$ with 
$\chi(\tilde S) > 0$, then $\tilde S$ would be a sphere or projective 
plane. A projective plane can be normalised and in the case of a sphere, 
$\tilde S$ could be normalised to the side which was not a ball. Both cases 
contradict 1-efficiency. Similarly there cannot be a non-peripheral normal 
surface $\tilde S$ with $\chi(\tilde S) = 0$ for the same reason. 

By a standard sweepout argument, starting with a peripheral normal torus 
at a cusp and sweeping to a core circle or the other cusp, there must be 
an intermediate almost normal torus $\tilde S$ - see Rubinstein \cite{Ru} 
or Stocking \cite{St}. If $\tilde S$ was obtained by attaching a tube to 
a normal sphere, this would contradict 1-efficiency. Hence $\tilde S$ must 
have one octagonal disk as claimed. 
\end{proof}

\begin{rmk} 
The proof of Theorem \ref{euler_for_gen_norm_surf} shows that a 1-efficient 
triangulation $\T$ of a closed orientable 3-manifold $M$ 
{\em other than $S^3$ or a lens space} contains no closed embedded simple 
generalised normal surface $\tilde S$ with $\chi(\tilde S) \ge 0$. 
(Here 1-efficient means there are no embedded normal spheres, projective 
planes, Klein bottles or tori, except for vertex linking spheres and 
edge linking tori. The former are boundaries of a small regular 
neighbourhood of a vertex, and the latter are obtained similarly from an 
edge which is a loop.) 
\end{rmk}

\begin{cor}
\label{1-efficient_degrees}
Let $\T$ be a 1-efficient ideal triangulation of a manifold $M$ other 
than the solid torus or $T^2 \times I$, and let $0\ne S \in N(\T;\Z)$ be 
an irreducible closed normal class. Then the contribution of $S$ to the 
3D-index sum has $q^{1/2}$-degree $d(S) \ge 1$.
\end{cor}

\begin{proof} 
Since $S$ is irreducible, it contains no tetrahedral solution summand, 
so $S=S^*$ is  the minimal non-negative coset representative of $[S]=S+\TT$. 
Then $S^*$  contains at most two quad types in each tetrahedron,
so can be replaced by an embedded generalised normal surface $\tilde S$ 
by Lemma \ref{gen_closed_class}. Now $\tilde S$ is connected since $S$ 
is irreducible, and $d(S) \ge - \chi(\tilde S)$ by 
Lemma \ref{deg_for_gen_norm_surf}.
Assume first that $\tilde S$ is not simple, so there are at least two of 
two different quadrilateral types in some tetrahedron for $S^*$. 
But then Lemma \ref{deg_for_gen_norm_surf} implies that $d(S) \ge 2$.
On the other hand,  if $\tilde S$ is simple and $M$ is not a solid torus, 
then $\chi(\tilde S)<0$ by Theorem \ref{euler_for_gen_norm_surf}, hence 
$d(S) \ge 1$. This completes the proof. 
\end{proof}

\begin{rmk}
\label{solid_torus_T2xI_degrees}
This result fails for 1-efficient triangulations of the solid torus and 
$T^2 \times I$. Here every normal class $S$ contributing to the index sum 
has degree $d(S)\ge 0$, but an almost normal torus $S$ gives a 
contribution $d(S)=0$. (Compare Example \ref{solid_torus_ex} below.)
\end{rmk}

One consequence of Corollary \ref{1-efficient_degrees} and 
Remark \ref{solid_torus_T2xI_degrees} is the following basic fact about 
the 3D-index.

\begin{cor}
If $\T$ is a 1-efficient ideal triangulation then the 3D-index $I_\T^0(0)$
is a formal power series in $q^{1/2}$, not just a formal Laurent series 
in $q^{1/2}$.
\end{cor}

In general, we expect that the minimum $q^{1/2}$-degree $d_{min}$ of 
$I^0_\T(kb)$ grows quadratically as $k \to +\infty$. However this is 
no longer true if $b$ is the boundary of an embedded spun normal surface.

\begin{lemma}
\label{linear_growth}
Assume $\T$ is a 1-efficient triangulation of a 3-manifold other than 
the solid torus or $T^2 \times I$. Assume that $\T$  contains an embedded 
spun normal surface $S$ with $\bd S=b \ne 0$, and 
that $S$ is the only irreducible spun normal class in $Q(\T;\Z_+)$ whose 
boundary is a positive integer multiple of $b$.
Then the minimum $q^{1/2}$-degree $d_{min}$ of $I^0_\T(kb)$ grows at 
mostly linearly as $k \to +\infty$.
In fact, $d_{min} I^0_\T(kb) \le -\chi(S)k$ for all even $k \ge 0$.   
\end{lemma}

\begin{proof} 
For each even $k\ge 0$, $k S$ has $\bd(k S) = k b$ and $[k S]=0$ so 
contributes a term to  $I^0_\T(kb)$
with $d(kS)^*)= d(kS) = -\chi(S)k+\delta(S)k^2 = -\chi(S)k.$ 
Now, by our assumption, any $S'$ with $\bd S'=b$ can be written as 
$S'=kS + S_0$ where $\bd S_0=0$. Hence $d(S') \ge d(kS) + d(S_0) > d(kS)$ 
unless $S_0=0$ by Corollary \ref{1-efficient_degrees}. 
\end{proof}

\begin{ex}
For the figure eight knot complement, with its canonical triangulation 
$\T$ given in Example \ref{ex:fig8}, there are embedded, essential, 
spun normal once-punctured Klein bottles with boundary
$b = \pm 4 \mu \pm \lambda$ and Euler characteristic $\chi= -1$ giving 
a term in $I^0_\T(k b)$ of degree $-\chi k =k$ for each $k \ge 0$. Further 
this is the {\em only} irreducible spun  normal class
with boundary a positive multiple of $b$, so by Lemma \ref{linear_growth}
this is the minimum $q^{1/2}$-degree of $I^0_\T(k b)$.
(Compare the calculations for 
$I_\T^0(8\mu+2\lambda) = I_{\CT}(4\mu+\lambda )$ and 
$I_\T^0(4\mu+\lambda )= I_{\CT}(2\mu+\frac{1}{2} \lambda)$
given in Example \ref{ex:fig8}.)

For the trefoil knot complement, with its 2 tetrahedra triangulation $\T$ 
given in Example \ref{trefoil_ex}, 
we have $I^0_\T((x \mu + y \lambda)) =  \delta_{0,x+6y}$.
Here there is an embedded, essential, spun normal M\"obius strip $S$ with 
boundary $b= \pm(6 \mu - \lambda)$
giving a contribution to  $I^0_\T(k b)$ of degree $0 = -\chi(S)k$ for all 
$k \in \Z_+$. Further, this is the {\em only} irreducible spun  normal class
with boundary a positive multiple of $b$, so  Lemma \ref{linear_growth} 
again applies.
\end{ex}
