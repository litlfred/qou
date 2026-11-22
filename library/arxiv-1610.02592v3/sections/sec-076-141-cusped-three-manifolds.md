---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-076-141-cusped-three-manifolds
section_title: "Cusped three-manifolds"
section_number: 14.1
pages: 429-441
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.998
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{cusped:section}
We know that every cusped finite-volume complete hyperbolic surface is constructed by gluing isometrically finitely many ideal triangles along their edges (see Proposition \ref{straightens:prop}). Likewise, we now construct plenty of cusped hyperbolic three-manifolds by gluing isometrically finitely many ideal tetrahedra along their faces.


\subsection{Ideal tetrahedra}
Ideal triangles are all isometric, but ideal tetrahedra are not! We now show that they can be described up to isometry by a single complex parameter $z$ with $\Im z >0$.\index{ideal tetrahedron}

\begin{figure}
\begin{center}
\includegraphics[width = 7cm] {\iftoggle{BW}{tetrahedron-BW}{tetrahedron}} 
\nota{An ideal tetrahedron with three vertices in $0,1,\infty$ in the half-space mode is determined by the position $z\in \matC\cup\{\infty\}$ of the fourth vertex. A small horosphere centred at the ideal vertex intersects the tetrahedron in a Euclidean triangle uniquely determined up to similarities.}
\label{tetrahedron:fig}
\end{center}
\end{figure}

An ideal tetrahedron is determined by its four ideal vertices $v_1, v_2, v_3, v_4\in\partial \matH^3$. 
We use the half-space model $H^3$ and recall that $\partial H^3 = \matC \cup \{\infty\}$ and $\Iso^+(H^3) = \PSLC$, hence there is a unique orientation-preserving isometry of $H^3$ that sends the vertices $v_1, v_2, v_3, v_4$ respectively to $0, 1, \infty, z$ for some $z$. Up to mirroring with the orientation-reversing reflection $z\mapsto \bar z$ we can suppose that $\Im z > 0$. 

\begin{oss}
By definition the number $z$ is the \emph{cross-ratio} of the four complex numbers $v_1, v_2, v_3, v_4$.\index{cross-ratio}
\end{oss}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{tetraedro2-BW}{tetraedro2}} 
\nota{At each ideal vertex we have a Euclidean triangle defined up to similarities: each vertex of the triangle has a well-defined complex angle (left). We can assign the complex angles directly to the edges of the tetrahedron. The argument is the dihedral angle of the edge (right).}
\label{tetraedro2:fig}
\end{center}
\end{figure}

A horosphere centred at the vertex $v_3=\infty$ is a horizontal Euclidean plane that intersects the ideal tetrahedron in a Euclidean triangle as in Figure \ref{tetrahedron:fig}. The oriented similarity class of the triangle depends only on the vertex $v_3$, because a horosphere change results in a dilation: we can represent it as a triangle in $\matC=\matR^2$ with vertices at $0$, $1$, and $z$ as in Figure \ref{tetraedro2:fig}-(left). The \emph{complex angle} of a vertex of the triangle is the ratio of the two adjacent sides, taken with clockwise order and seen as complex numbers. The three complex angles are shown in Figure \ref{tetraedro2:fig}-(left) and are:
$$z,\ \frac 1{1-z},\ \frac{z-1}z.$$
The argument is the usual angle, and the modulus is the ratio of the two lengths of the adjacent sides.

Proposition \ref{symmetries:ideal:tetrahedron:prop} shows that some symmetries of an ideal tetrahedron act on its vertices like the alternating group $A_4$ and hence transitively. Therefore every vertex has the same triangular section as in Figure \ref{tetraedro2:fig}-(left), and all the sections can be encoded by assigning the complex numbers directly to the edges of $\Delta$ as shown in Figure \ref{tetraedro2:fig}-(right). These labels on the edges are called \emph{moduli} and determine the ideal tetrahedron up to orientation-preserving isometries of $\matH^3$. The argument of a modulus is the dihedral angle of the edge.

On a regular ideal tetrahedron the triangular sections are equilateral and hence all edges have the same modulus $z = e^{\frac{\pi i}3}$.


\subsection{Ideal triangulations} \label{ideal:subsection}
Let $\Delta_1,\ldots, \Delta_n$ be identical copies of the standard oriented 3-simplex. As in the two-dimensional case, a \emph{triangulation} $\calT$ is a partition of the $4n$ faces of the tetrahedra into $2n$ pairs, and for each pair a simplicial isometry between the two faces. The triangulation is \emph{oriented} if the simplicial isometries are orientation-reversing. If we glue the tetrahedra along the simplicial isometries we get a topological space $X$, which is not necessarily a topological manifold. Let $M$ be $X$ minus the vertices of the triangulation: we say that $\calT$ is an \emph{ideal triangulation} for $M$.

\begin{figure}
\begin{center}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Truncatedtetrahedron-BW}{269px-Truncatedtetrahedron}}
\nota{A truncated tetrahedron.}
\label{truncated:fig}
\end{center}
\end{figure}

\begin{prop} If $\calT$ is oriented then $M$ is a topological 3-manifold, homeomorphic to the interior of a compact oriented manifold with boundary.
\end{prop}
\begin{proof}
To prove that $M$ is a manifold we only need to check that a point $x\in e$ in an edge $e$ has a neighbourhood homeomorphic to an open ball. A cycle of tetrahedra is attached to $e$, and since $\calT$ is oriented we are certain that a neighbourhood of $x$ is a cone over a 2-sphere and not over a projective plane.

If we truncate the tetrahedra as in Figure \ref{truncated:fig} before gluing them, we get a compact manifold $N\subset M$ with boundary such that $M\setminus N \isom \partial N \times [0,1)$. Therefore $M$ is homeomorphic to $\interior N$.
\end{proof}

We will always suppose that $\calT$ is oriented and $M$ is connected, so $M=\interior N$ for some compact $N$ with boundary. Every ideal vertex $v$ in $\calT$ is locally a cone over a small triangulated closed surface $\Sigma\subset M$ obtained by truncating the tetrahedra incident to $v$. We call such a $\Sigma$ the \emph{link} of $v$. 


\subsection{Hyperbolic ideal triangulations}
Let $\calT$ be an oriented ideal triangulation with tetrahedra $\Delta_1,\ldots, \Delta_n$ of a 3-manifold $M$. We now substitute every $\Delta_i$ with an ideal hyperbolic tetrahedron and pair their faces with orientation-reversing isometries. As opposite to the two-dimensional case, the ideal hyperbolic tetrahedra are not unique (they depend on a complex modulus $z_i$) but the isometric pairing of their faces is uniquely determined in virtue of the following.

\begin{prop} Given two ideal triangles $\Delta$ and $\Delta'$, every bijection between the ideal vertices of $\Delta$ and of $\Delta'$ is realised by a unique isometry. 
\end{prop}
\begin{proof}
We see the ideal triangles in $\matH^2$ and recall that for any two triples of points in $\partial \matH^2$ there is a unique isometry sending pointwise the first triple to the second. Alternatively, we may use the barycentric decomposition shown in Figure \ref{triangoli_ideali:fig}-(left).
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{tetrahedron3-BW}{tetrahedron3}} 
\nota{If we manage to glue all the tetrahedra incident to an edge $e$ inside $\matH^3$ as shown, the hyperbolic structure is defined also in $e$ (left). Let $z_1,\ldots, z_h$ be the complex moduli assigned to the sides of the $h$ incident tetrahedra (here $h=5$). We can glue everything in $\matH^3$ if and only if $z_1\cdots z_h=1$ and the arguments sum to $2\pi$ (right).}
\label{tetrahedron3:fig}
\end{center}
\end{figure}

If we substitute each $\Delta_i$ with an ideal hyperbolic tetrahedron, we immediately get a well-defined hyperbolic structure on $M$ minus the edges of $\calT$.
We now try to extend this hyperbolic structure to the edges: we can do this if we are able to glue all the $h$ tetrahedra around each edge $e$ inside $\matH^3$ as in Figure \ref{tetrahedron3:fig}. Let $z_1,\ldots, z_h$ be the complex moduli associated to the edges of the $h$ tetrahedra incident to $e$. As shown in the figure, if $z_1\cdots z_h = 1$ and the sum of their argument is $2\pi$ (and not some higher multiple of $2\pi$) then all tetrahedra can be glued simultaneously inside $\matH^3$ and the hyperbolic structure extends naturally to $e$. If this holds at every edge $e$ of $\calT$ then  $M$ inherits a hyperbolic structure and $\calT$ is said to be a \emph{hyperbolic} (or \emph{geometric}) \emph{ideal triangulation} for $M$.\index{hyperbolic ideal triangulation}


\subsection{Consistency equations}
We want to parametrize the hyperbolic structures on $M$ that may be constructed in this way from a fixed ideal triangulation $\calT$. We pick an arbitrary edge for every tetrahedron $\Delta_i$ and assign to it a complex variable $z_i$ with $\Im z_i>0$, and the other edges of $\Delta_i$ are automatically labeled by one of the variables $z_i$, $\frac{z_i-1}{z_i}$, or $\frac 1{1-z_i}$ as indicated in Figure \ref{tetraedro2:fig} (recall that the tetrahedra are oriented). As we have seen, for every edge $e$ in $\calT$ we obtain an equation of type 
$$w_1\cdots w_h = 1$$ 
(to which we must add the condition that the sum of the arguments is $2\pi$), where each $w_j$ equals $z_i$, $\frac{z_i-1}{z_i}$, or $\frac 1{1-z_i}$ for some $i$.

We have thus obtained a system of \emph{consistency equations}, with a variable $z_i$ for each tetrahedron and an equation $w_1\cdots w_h = 1$ for each edge. A solution $z = (z_1,\ldots, z_n)$ to these equations produces a hyperbolic ideal triangulation and hence a hyperbolic structure on $M$. Recall that we assume $\Im z_i>0$ $\ \forall i$.

As in the two-dimensional case, the resulting hyperbolic structure is not necessarily complete, and to get a complete hyperbolic manifold we must add more equations.


\subsection{Completeness equations} \label{complete:solutions:subsection}
Our aim is to construct a complete finite-volume hyperbolic metric on $M$. By Corollary \ref{tame:cor} if $M$ has such a metric the link of every ideal vertex of $\calT$ is a triangulated torus and identifies a cusp of $M$, so we will henceforth suppose that the links of all vertices are tori. In other words $M$ is the interior of a compact 3-manifold $N$ bounded by some $c>0$ tori.

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{complete_equations-BW}{complete_equations}} 
\nota{Every boundary torus $T\subset \partial N$ is triangulated, and each triangle has a Euclidean structure well-defined up to similarities and inherits three complex moduli $w_1, w_2, w_3$ at its vertices (left). At every vertex of the triangulation, the product of the adjacent moduli is $1$, for instance here $w_{12}w_{15}w_{16}w_{19}w_{23} = 1$. The \iftoggle{BW}{grey}{red} path contributes to $\mu(\gamma)$ with the factor $-w_{30}w_{29}w_{25}w_{24}w_{23}w_{19}w_{20}$ (right).}
\label{complete_equations:fig}
\end{center}
\end{figure}

Let $z=(z_1,\ldots, z_n)$ be a solution to the consistency equations, providing a hyperbolic structure to $M$. Every boundary torus $T\subset \partial N$ is triangulated by $\calT$: every triangle in $T$ is the truncation triangle of some $\Delta_i$ and hence inherits the complex moduli of the three adjacent edges of $\Delta_i$ as in Figure \ref{complete_equations:fig}-(left), thus it has a Euclidean structure well-defined up to similarities. We want to study the following problem: do these Euclidean structures on the triangles glue to form a Euclidean structure on $T$? We will see that $M$ is complete if and only if the answer is ``yes'' at each boundary torus $T$.

Pick $\gamma \in \pi_1(T)=H_1(T,\matZ) \isom \matZ^2$. We represent $\gamma$ as a simplicial path in the triangulation of $T$ and then define $\mu(\gamma)\in \matC^*$ to be $(-1)^{|\gamma|}$ times the product of all the complex moduli that $\gamma$ encounters at its right side, with $|\gamma|$ being the number of edges of $\gamma$, see Figure \ref{complete_equations:fig}-(right). 

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{complete_move-BW}{complete_move}} 
\nota{This move for $\gamma$ does not affect $\mu(\gamma)$.}
\label{complete_move:fig}
\end{center}
\end{figure}

\begin{prop} \label{mu:prop}
The element $\mu(\gamma)$ is well-defined and $\mu\colon\pi_1(T) \to \matC^*$ is a homomorphism.
\end{prop}
\begin{proof}
Two different paths for $\gamma$ are related by moves as in Figure \ref{complete_move:fig}. This move does not affect $\mu(\gamma)$ since $w_1w_2w_3=-1$ and the product of the moduli around a vertex is $+1$. The map $\mu$ is clearly a homomorphism.
\end{proof}

Let $C(T)\subset M$ be a closed collar of the torus $T$ in $N$, intersected with $M$. It is diffeomorphic to $T\times [0,+\infty)$.

\begin{prop} \label{mu:equivalent:prop}
The following facts are equivalent:
\begin{enumerate}
\item the homomorphism $\mu$ is trivial,
\item there is a Euclidean structure on $T$ that induces all the moduli,
\item the manifold $C(T)$ is complete and contains a truncated cusp.
\end{enumerate}
\end{prop}
\begin{proof}
The equivalence (1)$\Leftrightarrow$(2) is a simple exercise.
If (2) holds we may choose small horosections of all the hyperbolic tetrahedra incident to $v$ that match to give a Euclidean torus $T_*\subset C(T)$. The non-compact part of $C(T)$ bounded by $T_*$ is a truncated cusp with base $T_*$ and is thus complete.
On the other hand, if (1) does not hold, there is a path of horosections from a tetrahedron to itself which ends at a bigger height and we conclude that $C(T)$ is not complete as in the two-dimensional case, see the proof of Proposition \ref{completion:surface:prop}.
\end{proof}

\begin{cor} The hyperbolic manifold $M$ is complete $\Longleftrightarrow$ $\mu$ is trivial for every torus $T\subset \partial N$.
\end{cor}

Fix for every boundary torus $T$ two generators $m,l$ for $H_1(T, \matZ)$. The homomorphism $\mu$ is trivial $\Longleftrightarrow$ the following two equations are satisfied:
$$\mu(m) = 1, \quad \mu(l)=1.$$ 
Each equation is of some type $w_1\cdots w_k = 1$.
We get two equations for each of the $c$ boundary tori and hence $2c$ equations in total, called the \emph{completeness equations} for the triangulation $\calT$. We summarise our discussion:\index{Thurson's hyperbolicity equations}

\begin{prop}
Let $\calT$ be an ideal triangulation of $M=\interior N$ with $n$ tetrahedra and $\partial N$ consisting of $c$ tori. If a point $z = (z_1,\ldots, z_n)$ with $\Im z_i >0$ satisfies the $n$ consistency equations and the $2c$ completeness equations, then $M$ admits a finite-volume complete hyperbolic metric.
\end{prop}


\subsection{Examples}
On a triangulation $\calT$, the \emph{valence} of an edge $e$ is the number of tetrahedra incident to it, counted with multiplicity. The simplest kinds of solutions arise in the following construction. 

\begin{prop} \label{valence:6:prop}
Let $\calT$ be a triangulation where all edges have valence six. The point $(e^{\frac{\pi i}3}, \ldots, e^{\frac{\pi i}3})$ is a solution of both the consistency and completeness equations and defines a hyperbolic structure where all the ideal tetrahedra are regular.
\end{prop}
\begin{proof}
Note that when $z= e^{\frac{\pi i}3}$ the tetrahedron is regular and we get 
$$z = \frac{z-1}z = \frac 1{1-z} = e^{\frac{\pi i}3}.$$
Therefore the moduli are $e^{\frac{\pi i}3}$ everywhere. The consistency equations are satisfied since $(e^{\frac{\pi i}3})^6 = 1$ and also the completeness equations are, because by assigning length 1 to each edge of the triangulation of a torus $T$ we get a global Euclidean structure on $T$ tessellated into isometric equilateral triangles.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{triangulation_figure8-BW}{triangulation_figure8}} 
\nota{An oriented triangulation with $2$ tetrahedra: faces with the same letter $F, J, P, R$ are paired with a simplicial map that matches the letters. We get two edges with valence six (the \iftoggle{BW}{grey}{red} and white dots). }
\label{triangulation_figure8:fig}
\end{center}
\end{figure}

Figure \ref{triangulation_figure8:fig} shows an ideal triangulation with two tetrahedra and two edges, each with valence six: this defines a cusped finite-volume complete hyperbolic three-manifold $M$ that decomposes into two regular ideal tetrahedra. 

Every finite covering $\tilde M$ of $M$ is another example: the ideal triangulation $\calT$ lifts to an ideal triangulation $\tilde \calT$ where all the edges have valence six. Since the fundamental group $\pi_1(M)$ is residually finite (see Proposition \ref{RF:hyperbolic:prop}) there are plenty of such coverings.

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{octa-BW}{octa}} 
\nota{By pairing the faces of two ideal regular octahedra as shown we get a cusped complete hyperbolic three-manifold. Faces with the same letter are paired with the unique isometry that matches the letters. We get six edges with valence four (marked with coloured dots). }
\label{octa:fig}
\end{center}
\end{figure}

\begin{ex} Construct a triangulation $\calT$ with one tetrahedron and one edge. The edge has valence six and hence the construction of Proposition \ref{valence:6:prop} produces a cusped hyperbolic manifold. Note however that the triangulation is not orientable and a cusp section is a Klein bottle! This non-orientable hyperbolic manifold is called the \emph{Gieseking manifold}.\index{Gieseking manifold}
\end{ex}


Similar kinds of ``regular'' examples may be constructed using some other platonic solids.
The ideal regular octahedron is particularly interesting and useful because it is right-angled, see Section \ref{platonici:subsection}. If we pick finitely many oriented regular ideal octahedra $O_1, \ldots, O_h$ and pair orientation-reversingly their triangular faces in a way that every resulting edge has valence four, we construct a finite-volume cusped hyperbolic manifold $M$ because $4\times \frac \pi 2 = 2 \pi$. An example with two octahedra is shown in Figure \ref{octa:fig}.

We can further decompose each regular ideal octahedron into four non-regular ideal tetrahedra (there are three ways to do this: you must choose a diagonal connecting two opposite vertices) to get an ideal triangulation $\calT$ for $M$. The moduli of each such tetrahedron are 
$$i, \ \frac 1{1-i} = \frac{1+i}2, \ \frac{i-1}i = 1+i$$
and they satisfy the consistency and completeness equations in a less trivial way than before. The edges of the resulting triangulation have varying valences 4, 6, and 8.


\subsection{SnapPea}
It is of course hard to construct ideal triangulations by hand, except in some very symmetric and simple cases like the one just described. And it is even more difficult to solve the consistency and completeness equations.

There is a beautiful computer program that does all this for you! This is \emph{SnapPea}, written by Jeff Weeks in the 1980s. Using SnapPea you can draw any link diagram $L$ and the program immediately constructs an ideal triangulation for the complement of $L$ in $S^3$. Then it uses the Newton method to find a numerical solution to the consistency and completeness equations: the solution is only numerical, but then one can use some \emph{a posteriori} argument to confirm it rigorously.

For instance, if we draw the trefoil knot, SnapPea triangulates its complement and finds no solution to the equations: this is not surprising since its complement is Seifert and hence not hyperbolic, see Proposition \ref{torus:knot:complement:prop}. 

If we draw the figure-eight knot in Figure \ref{figure8:fig}-(left), SnapPea constructs precisely the ideal triangulation of Figure \ref{triangulation_figure8:fig}, and we have hence discovered that the complement of the figure-eight knot is hyperbolic and decomposes into two ideal regular tetrahedra. 

We may draw links with many components, and discover for instance that the complement of the Borromean rings from Figure \ref{figure8:fig}-(right) is hyperbolic and decomposes into two right-angled ideal regular octahedra. We can also Dehn-fill some boundary components to obtain more cusped manifolds that are not link complements in $S^3$.

\begin{figure}
\begin{center}
\includegraphics[width = 4.5 cm] {\iftoggle{BW}{Blue_Figure-Eight_Knot-BW}{422px-Blue_Figure-Eight_Knot}} 
\includegraphics[width = 5 cm] {\iftoggle{BW}{Borromean_Rings_Illusion-BW}{484px-Borromean_Rings_Illusion}}
\nota{The figure-eight knot and the Borromean rings are \emph{hyperbolic}, that is  their complements admit complete hyperbolic metrics.}
\label{figure8:fig}
\end{center}
\end{figure}

SnapPea can calculate numerically a wealth of geometrical invariants with some precision, including the volume and the first segment of the geodesic spectrum. It can  manipulate manifolds (Dehn-filling, drilling along short simple closed geodesics, finite covers) and change triangulations. It provides beautiful pictures of the Dirichlet domain and of the cusp shapes. 

Is SnapPea guaranteed to find a hyperbolic structure on $M$ if there is one? No, it is not, although in practice it succeeds most of the time. The fact that $M$ is hyperbolic does not guarantee that there is a solution to Thurston's equations on a given triangulation $\calT$, and the existence of a solution does not guarantee that SnapPea will be able to find it. 

We note that for most ideal triangulations $\calT$ of a hyperbolic $M$ there is no solution to Thurston's equations, and SnapPea is clever enough to modify $\calT$ to increase the probability to find one. In all known examples, a cusped hyperbolic $M$ admits at least \emph{one} geometric ideal triangulation, but whether this holds true for all cusped hyperbolic 3-manifolds $M$ is still an open question.


\subsection{Cusped census}
As with knots tabulations, topologists have used computers to list the cusped hyperbolic manifolds that can be triangulated with few ideal tetrahedra.

\begin{table}
\begin{center}
\begin{tabular}{c||ccccccc}
tetrahedra        & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
 \hline \hline
1 cusp &  & 2 & 9 & 52 & 223 & 913 & 3388 \\
2 cusps & & & & 4 & 11 & 48 & 162  \\
3 cusps & & & & & & 1 & 2
\end{tabular}
\vspace{.2 cm}
\nota{The number of cusped orientable hyperbolic three-manifolds that can be triangulated with at most 7 ideal tetrahedra.}
\label{cusped:census:table}
\end{center}
\end{table}

\begin{table}
\begin{center}
\begin{tabular}{c||ccccccc}
Name        & Volume & Homology & Symmetry & SG & C \\
 \hline \hline
$M2_1$ & $2.0298832128$ & $\matZ$ & $D_4$ & $1.09$ & a \\
$M2_2$ & $2.0298832128$ & $\matZ+\matZ_5$ & $\matZ_2+\matZ_4$ & $0.86$ & a \\
$M3_1$ & $2.5689706009$ & $\matZ+\matZ_5$ & $D_4$ & $0.65$ & c \\
$M3_2$ & $2.5689706009$ & $\matZ+\matZ_3$ & $D_4$ & $0.65$ & c \\
$M3_3$ & $2.6667447834$ & $\matZ+\matZ_2$ & $D_4$ & $0.63$ & c \\
$M3_4$ & $2.6667447834$ & $\matZ+\matZ_6$ & $D_4$ & $0.63$ & c \\
$M3_5$ & $2.7818339124$ & $\matZ$ & $\matZ_2$ & $0.51$ & c \\
$M3_6$ & $2.8281220883$ & $\matZ$ & $D_4$ & $0.56$ & c \\
$M3_7$ & $2.8281220883$ & $\matZ$ & $\matZ_2$ & $0.58$ & c \\
$M3_8$ & $2.8281220883$ & $\matZ+\matZ_7$ & $D_4$ & $0.56$ & c \\
$M3_9$ & $2.9441064867$ & $\matZ$ & $\matZ_2$ & $0.43$ & c 
\end{tabular}
\vspace{.2 cm}
\nota{The 1-cusped orientable hyperbolic manifolds that can be triangulated with at most 3 ideal tetrahedra. The name $Mi_j$ indicates that the manifold is the one with $j$-th smallest volume among those that can be triangulated with $i$ tetrahedra. The column SG shows the length of the shortest closed geodesic (volume and SG values are truncated after few digits). The column C indicates whether the manifold is achiral (a) or chiral (c), that is if it admits an orientation-reversing isometry or not.}
\label{cusped:census:2:table}
\end{center}
\end{table}

\begin{table}
\begin{center}
\begin{tabular}{c||ccccccc}
Name        & Volume & Homology & Symmetry & SG & C \\
 \hline \hline
$M4_1^2$ & $3.6638623767$ & $\matZ+\matZ$ & $D_8$ & $1.06$ & c \\
$M4_2^2$ & $3.6638623767$ & $\matZ+\matZ$ & $D_8$ & $0.96$ & c \\
$M4_3^2$ & $4.0597664256$ & $\matZ+\matZ$ & $D_{12}$ & $0.86$ & c \\
$M4_4^2$ & $4.0597664256$ & $\matZ+\matZ$ & $D_8$ & $0.86$ & a \\
\end{tabular}
\vspace{.2 cm}
\nota{The 2-cusped orientable hyperbolic manifolds that can be triangulated with 4 ideal tetrahedra. The name $Mi_j^k$ indicates that the manifold is the $k$-cusped one with $j$-th smallest volume among those that triangulate with $i$ tetrahedra.}
\label{cusped:census:3:table}
\end{center}
\end{table}

The number of cusped hyperbolic orientable manifolds that can be ideally triangulated with $n$ tetrahedra (and not less than $n$) is written in Table \ref{cusped:census:table} for all $n\leqslant 7$. The 1-cusped manifolds with $n=2,3$ are listed with more detail in Table \ref{cusped:census:2:table} and the 2-cusped ones with $n=4$ are in Table \ref{cusped:census:3:table}. These tables were produced by Callahan -- Hildebrand -- Weeks \cite{CaHiWe} in 1999 via a computer enumeration.

The figure-eight knot complement is $M2_1$, while $M2_2$ is another hyperbolic manifold that decomposes into two regular ideal tetrahedra: it is not a knot complement in $S^3$ since its homology is not $\matZ$, but it is  the complement of a knot $K$ in the lens space $L(5,1)$, called the \emph{figure-eight knot sibling}. This knot is obtained by performing a $(-5)$-surgery on one component of the \emph{Whitehead link} shown in Figure \ref{sequence:fig}: since this component is trivial, the surgered manifold is $L(5,1)$ and the other unsurgered component is our knot $K$. Both manifolds $M2_1$ and $M2_2$ have volume $2.0298832128\ldots$ since the volume of the ideal regular tetrahedron is $3\Lambda\big(\frac \pi 3\big) = 1.0149416064\ldots$

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {sequence_thick.pdf}
\nota{A remarkable sequence of hyperbolic links. These are the \emph{figure eight knot}, the \emph{Whitehead link}, and some particular \emph{chain links} with 3,4,5 components. }
\label{sequence:fig}
\end{center}
\end{figure}

The manifold $M4_1^2$ is the Whitehead link complement, that can be obtained by pairing the faces of a single ideal regular octahedron $O$. Indeed the volume of $O$ is $8\Lambda\big(\frac {\pi} 4\big) = 3.6638623767\ldots $

After the figure eight knot and the Whitehead link, a notable sequence of hyperbolic links in $S^3$ with increasing number of components is shown in Figure \ref{sequence:fig}. Their complements are conjectured to be the smallest hyperbolic manifolds with $i=1,\ldots, 5$ cusps (see the references at the end of the chapter).


\subsection{Hyperbolic knots}
How many hyperbolic knots in $S^3$ are there? There are infinitely many hyperbolic knots, and infinitely many non-hyperbolic knots. Geometrisation translates hyperbolicity into an appealing topological condition:

\begin{teo}
A knot $K\subset S^3$ is either a torus knot, a satellite knot, of a hyperbolic knot.
\end{teo}
\begin{proof}[Proof using geometrisation]
Proposition \ref{trichotomy:knots:prop} says that $K$ is either a torus knot, a satellite knot, or has simple complement $M$. In the latter case $M$ is hyperbolic by Corollary \ref{simple:bounded:hyperbolic}.
\end{proof}

Note that the three cases are mutually exclusive. The number of prime knots with $c\leqslant 14$ crossings in each of the three classes is shown in Table \ref{torus:satellite:hyperbolic:knots:table}, taken from Hoste -- Thistlethwaite -- Weeks \cite{HTW}: the table shows a strong predominance of hyperbolic knots, but it is unknown whether it persists also when $c$ tends to infinity.

\begin{table}
\begin{center}
\begin{tabular}{c||cccccccccccc}
 $c$       &  
 $3$ & $4$ & $5$ & $6$ & $7$ & $8$
 & $9$ & $10$ & $11$ & $12$ & $13$ & $14$ \\
 \hline \hline
torus & 
1 & 0 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 1 \\
satellite & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 2 \\
hyperbolic & 
0 & 1 & 1 & 3 & 6 & 20 & 48 & 164 & 551 & 2176 & 9985 & 46969 
 \end{tabular}
\vspace{.2 cm}
\nota{The number of torus, satellite, and hyperbolic prime knots with $c$ crossings, for all $c\leqslant 14$.}
\label{torus:satellite:hyperbolic:knots:table}
\end{center}
\end{table}
