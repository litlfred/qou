---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-048-92-prime-decomposition
section_title: "Prime decomposition"
section_number: 9.2
pages: 280-295
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.998
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
In this section we study spheres and discs in three-manifolds. We prove that every sphere in $\matR^3$ bounds a disc, and we call \emph{irreducible} a three-manifold that has this property. Then we study the connected sum of three-manifolds, and we show that it behaves like multiplication of natural numbers: every closed oriented three-manifold decomposes uniquely into some \emph{prime} factors.


\subsection{Balls}
In general dimension $n$, we have used the term \emph{disc} to denote the closed Euclidean disc $D^n$, and the term \emph{ball} for its open interior. Speaking about three-dimensional spaces, we will henceforth use a more intuitive terminology and call \emph{disc} and \emph{ball} respectively the closed discs $D^2$ and $D^3$, and we will use the symbols $D$ and $B$ for them.

Let $M$ be a connected 3-manifold. Theorem \ref{dischi:teo} says that all the closed balls $B\subset \interior M$ in $M$ are isotopic and hence the removal of the interior of $B$ from $M$ produces a new manifold $N$ with boundary, which does not depend on $B$. The sphere $\partial B$ is a new boundary component of $N$.

The inverse operation consists of \emph{capping off} a boundary component of $N$ diffeomorphic to $S^2$ by attaching a ball $B$ to it, via some diffeomorphism. This operation depends only on the boundary component that is capped off.

\begin{prop} \label{cap:prop}
The manifold $M$ obtained by capping off a spherical boundary component of $N$ does not depend on the diffeomorphism chosen.
\end{prop}
\begin{proof}
There are only two diffeomorphisms up to isotopy, see Theorem \ref{S2:omotopi:teo}, and they are related by a reflection of $B$, so they produce diffeomorphic manifolds.
\end{proof}

In dimension 3 we can therefore freely remove and add balls without affecting much the topology of the manifold. In particular, by removing the interior of a ball from $S^3$ we get another ball $B$, and by attaching a ball to $B$ we get $S^3$ back. We must thank Smale's Theorem \ref{Smale:teo} for that: the situation in higher dimensions is more complicated.


\subsection{Connected sums}
Connected sums exist in any dimension $n$, but when $n\leqslant 3$ they may be redefined in slightly simpler terms:\index{connected sum} 
\begin{defn}
The \emph{connected sum} $M=M_1\#M_2$ of two oriented connected $3$-manifolds $M_1$, $M_2$ is constructed by removing the interiors of two closed balls from $M_1$ and $M_2$, and then gluing the two resulting spheres via any orientation-reversing diffeomorphism. 
\end{defn}
In dimension $n\leqslant 3$ these diffeomorphisms are all isotopic, see Theorem \ref{S2:omotopi:teo},
 hence this is a good definition (in arbitrary dimension we require the diffeomorphism to extend to the removed discs). We usually work with oriented 3-manifolds to have a uniquely defined connected sum, but in some cases this is not necessary. An orientable manifold $M$ is \emph{mirrorable} if it admits an orientation-reversing self-diffeomorphism.\index{manifold!mirrorable manifold}

\begin{ex} If $M_1$ is mirrorable, the manifold $M = M_1\# M_2$ does not depend (up to diffeomorphisms) on the orientations of $M_1$ and $M_2$.
\end{ex}

If both $M_1$ and $M_2$ are oriented and not mirrorable, it may happen that $M_1\# M_2$ and $M_1 \# \overline{M_2}$ are not diffeomorphic (here $\overline{M_2}$ is $M_2$ with the reverse orientation).
There is also a boundary-version of connected sum:

\begin{defn}
The \emph{$\partial$-connected sum} $M=M_1\#_\partial M_2$ of two oriented $3$-manifolds with boundary is constructed by gluing two discs $D_1\subset \partial M_1$ and $D_2\subset \partial M_2$ via an orientation-reversing diffeomorphism.
\end{defn}

The operation depends only on the components of $\partial M_1, \partial M_2$ containing $D_1, D_2$, because of Theorem \ref{dischi:teo}. The following holds:
$$M\# S^3 = M, \qquad M\#_\partial B = M, \qquad \partial (M_1\#_\partial M_2) = (\partial M_1)\#(\partial M_2).$$
In the latter equality we suppose that $\partial M_1$ and $\partial M_2$ are connected.

\begin{ex} Let $M = M_1\# M_2$ or $M=M_1\#_\partial M_2$. We have
$$\pi_1(M) = \pi_1(M_1) * \pi_2(M_2).$$
\end{ex}
\begin{proof}[Hint]
Use Van Kampen. 
\end{proof}
\begin{cor}
We have $H_1(M,\matZ) = H_1(M_1,\matZ) \oplus H_1(M_2,\matZ)$.
\end{cor}


\subsection{Irreducible 3-manifolds}
We introduce an important definition. Let $M$ be a connected, oriented 3-manifold with (possibly empty) boundary.\index{three-manifold!irreducible three-manifold}
\begin{defn}
The manifold $M$ is \emph{irreducible} if every sphere $S\subset \interior M$ bounds a ball.
\end{defn}
It is important to recall here that the sphere must be a smooth surface. If we admitted also topological spheres, no 3-manifold would be irreducible: there are ``wild'' topological spheres inside every ball, as shown in Figure \ref{Alexander:fig}. 

\begin{figure}
\begin{center}
\includegraphics[width = 7 cm] {\iftoggle{BW}{Morse-BW}{Morse}}
\nota{Non-degenerate points of index 0, 1, and 2.}
\label{Morse:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{3D-Leveltorus-BW}{240px-3D-Leveltorus}}
\nota{The height function on this torus is a Morse function. It has four critical points of index (from bottom to top) 0, 1, 1, 2. }
\label{Morse_torus:fig}
\end{center}
\end{figure}


\subsection{Alexander theorem} The first 3-manifold to look at is of course $\matR^3$. We prove here that $\matR^3$ is irreducible. 

We need some Morse theory. Let $S\subset \matR^3$ be a closed surface and $f(x,y,z)=z$ be the height function. The function $f$ is a \emph{Morse function} for $S$ if $f|_S$ has finitely many critical points, and at each critical point the Hessian of $f|_S$ is non-singular (the Hessian is read on a chart for $S$, but this definition is chart-independent). The critical point is a local minimum, a saddle, or a local maximum, according to the signature of the Hessian, see Figure \ref{Morse:fig}. These critical points have \emph{index} 0, 1, and 2, respectively.\index{Morse function}

\begin{ex}
A critical point $p$ for $f|_S$ is non-degenerate if and only if $p$ is a regular (\emph{i.e.}~non-critical) point for the Gauss map $S \to S^2$.
\end{ex}

\begin{lemma} Let $S\subset \matR^3$ be a closed surface. After rotating $S$ of an arbitrarily small angle, the height function $f$ is a Morse function for $S$. 
\end{lemma}
\begin{proof}
Consider the Gauss map $\psi\colon S\to S^2$. By Sard lemma there are regular values arbitrarily close to $v=(0,0,1)$. Rotate $S$ so that $v$ is a regular value. Now $\psi^{-1}(v)$ is the set of critical points for $f$ and they are all non-degenerate.
\end{proof}

We are now ready to prove the following.\index{Alexander theorem}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{Morse_cap-BW}{Morse_cap}}
\nota{The plane $P$ intersects $S$ into circles. Starting from the innermost ones, we cut $S$ along the circles and cap them off by adding pairs of discs. The resulting surface does not intersect $P$ anymore.}
\label{Morse_cap:fig}
\end{center}
\end{figure}

\begin{teo}[Alexander's Theorem] \label{Alexander:teo}
The space $\matR^3$ is irreducible.
\end{teo}
\begin{proof}
Let $S\subset \matR^3$ be a 2-sphere. Up to a small rotation we suppose that the height function $f|_S$ is a Morse function, and after a further small rotation we may suppose that the $k$ critical points of $f|_S$ stay at distinct heights $z_1< \ldots <z_k$. Pick a regular value $u_i \in (z_i, z_{i+1})$ for every $i=1,\ldots, k-1$. The horizontal plane $P$ at height $u_i$ intersects $S$ transversely into circles. Starting from the innermost ones, we cut $S$ along these circles and cap them off by adding pairs of discs as in Figure \ref{Morse_cap:fig}. The resulting surface is disjoint from $P$.

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{Morse2-BW}{Morse2}}
\nota{After capping off at each $u_i$ we end up with many spheres of these basic types, which clearly bound balls.}
\label{Morse2:fig}
\end{center}
\end{figure}

At every cut a sphere decomposes into two spheres. If we do this for every $i=1,\ldots, k-1$ we end up with many spheres of the types shown in Figure \ref{Morse2:fig}, that clearly bound balls in $\matR^3$.

Now we reverse the process and undo all the cuts: we prove inductively that at each backward step we have a set of spheres bounding balls (note that the balls are not disjoint!). At each backward step we replace two spheres $S_1, S_2$ bounding balls $B_1, B_2$ with one sphere $S$. Isotope $S_1$ and $S_2$, so that they intersect in a disc $D$. If the interiors of $B_1$ and $B_2$ are disjoint, then $S$ bounds the ball $B_1\cup B_2$. If they are not disjoint, then one is contained in the other, say $B_1 \subset B_2$ and $S$ bounds the ball $B_2\setminus \interior{B_1}$.
\end{proof}

\begin{cor}
Every sphere contained in a sub-ball $B\subset M$ of a 3-manifold $M$ bounds a ball $B'\subset B$.
\end{cor}
\begin{cor} \label{both:cor}
Every sphere in $S^3$ bounds a ball on both sides.
\end{cor}
\begin{proof}
Choose two points $p, q \not \in S$ on opposite sides with respect to $S$. We have $S^3 \setminus p = S^3 \setminus q = \matR^3$ hence $S$ is contained in $\matR^3$ in two ways and bounds a ball in each.
\end{proof}

Alexander's Theorem generalises the smooth Jordan curve Theorem to dimension $3$. The situation in higher dimensions is much more problematic: it is still unknown whether every smooth 3-sphere in $\matR^4$ bounds a smooth 4-disc (this is usually called the \emph{Sch\"onflies problem}).\index{Sch\"onflies problem}


\subsection{Prime manifolds}
A connected sum $M_1\# M_2$ is \emph{trivial} if either $M_1$ or $M_2$ is a sphere. \index{three-manifold!prime three-manifold}

\begin{defn}
A connected, oriented 3-manifold $M$ is \emph{prime} if every connected sum $M=M_1\# M_2$ is trivial.
\end{defn}

Being prime is equivalent to be irreducible, with a single exception.

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{prime-BW}{prime}}
\nota{If $S\subset M$ is non-separating, there is a simple closed curve $\alpha$ intersecting $S$ transversely in one point: here $S$ is drawn as a disc whose boundary should be collapsed to a point, and $\alpha$ is a line whose endpoints should be identified (left). Pick two tubular neighbourhoods of $S$ and $\alpha$ and consider their union $N$ (right).}
\label{prime:fig}
\end{center}
\end{figure}

\begin{prop} \label{S2S1:prop}
Every oriented 3-manifold $M\neq S^2 \times S^1$ is prime if and only if it is irreducible.
\end{prop}
\begin{proof}
The inverse operation of a connected sum $M=M_1\# M_2$ consists of cutting along a separating sphere $S\subset M$ and then capping off the two resulting manifolds $N_1, N_2$ with balls. The capped $N_i$ is $S^3$ if and only if $N_i$ is a ball. Therefore the connected sum is trivial if and only if $S$ bounds a ball on one side. Therefore $M$ is prime if and only if every separating sphere $S\subset M$ bounds a ball.

If $M$ is irreducible, then it is clearly prime. If $M$ is prime and not irreducible, there is a non-separating sphere $S\subset M$. There is a simple closed curve $\alpha\subset M$ intersecting $S$ transversely in one point as in Figure \ref{prime:fig}-(left). Pick two tubular neighbourhoods of $S$ and $\alpha$ as in Figure \ref{prime:fig}-(right): their union is a manifold $N$ with a boundary sphere $\partial N = S'$. The sphere $S'$ is separating and $M$ is prime, hence $S'$ bounds a ball $B$ on the other side and $M=N\cup B$. 

We now prove that $M=S^2\times S^1$. We embed $S\cup \alpha$ naturally in $S^2\times S^1$ as $S = S^2\times y$ and $\alpha = x \times S^1$. Decompose $S^2= D\cup D'$ in two discs and $S^1 = I\cup I'$ in two intervals. The manifold
$N$ also embeds as $S^2\times I \cup D \times S^1$ and its complement $B=D'\times I'$ is a ball. Therefore $M = S^2\times S^1$.
\end{proof}


\subsection{Some irreducible manifolds}
The Alexander theorem generates many more examples of irreducible 3-manifolds.

\begin{prop} \label{connected:boundary:prop}
Every compact three-dimensional submanifold $M\subset S^3$ with connected boundary is irreducible.
\end{prop}
\begin{proof}
Every sphere $S \subset M$ bounds two balls in $S^3$. Since $\partial M$ is connected, it is contained in one of them, so the other is contained in $M$.
\end{proof}

We turn to coverings.

\begin{prop} \label{irreducible:cover:prop}
Let $p\colon  M \to N$ be a covering of 3-manifolds. If $ M$ is irreducible then $N$ also is.
\end{prop}
\begin{proof}
A sphere $S\subset N$ lifts to many spheres in $ M$, each bounding at least one ball. Pick an innermost such ball $B$. We prove that $p(B)$ is a ball with boundary $S$ and we are done.

To do this, note that $p|_{\partial B}$ is a diffeomorphism onto $S$ and $p(\interior B)$ is disjoint from $S$ since $B$ is innermost. This implies that $p|_{B}\colon B \to p(B)$ is a covering and since it has degree one on $S$ it is a diffeomorphism.
\end{proof}

\begin{cor}
Elliptic, flat, hyperbolic 3-manifolds are irreducible.
\end{cor}
\begin{proof}
Their universal covering is diffeomorphic to $S^3$ or $\matR^3$.
\end{proof}

Finally, we consider the exception $S^2\times S^1$. It is not irreducible since it contains a non-separating sphere, but it is prime.

\begin{prop} The manifold $S^2\times S^1$ is prime.
\end{prop}
\begin{proof}
Let $S\subset S^2\times S^1$ be a separating sphere: we must prove that it bounds a ball. It separates $S^2\times S^1$ into two manifolds $M$ and $N$, and on fundamental groups we get $\matZ = \pi_1(M)*\pi_1(N)$. This implies easily that either $\pi_1(M)$ or $\pi_1(N)$ must be trivial: suppose the first. 

Since $M$ is simply connected, a copy $M'$ of $M$ lifts to the universal cover $S^2\times \matR$ of $S^2\times S^1$. We identify $S^2\times\matR = \matR^3\setminus 0$. This copy $M'$ now lies in $\matR^3$, and $\partial M' = S^2$ implies that $M'$ is a ball by Alexander theorem.
\end{proof}


\subsection{Handlebodies and line bundles}
We now introduce some basic, but important, compact 3-manifolds with boundary. A \emph{handlebody} is a connected orientable 3-manifold that decomposes into 0- and 1- handles.\index{handlebody} 

\begin{figure}
\begin{center}
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{Sphere_with_three_handles-BW}{500px-Sphere_with_three_handles}}
\nota{A handlebody of genus $3$.}
\label{handlebody:fig}
\end{center}
\end{figure}

\begin{prop}
The boundary of a handlebody is $S_g$ for some $g\geqslant 0$. Two handlebodies are diffeomorphic if and only if they have the same $g$.
\end{prop}
\begin{proof}
By simplifying handles we may decompose the handlebody into one 0-handle and some $g$ 1-handles, so that the boundary is a genus-$g$ surface, see Figure \ref{handlebody:fig}. Each 1-handle is attached along a pair of discs; the orientability assumption together with Theorem \ref{dischi:teo} easily imply that the result of attaching a 1-handle depends on nothing and the handlebody depends only on $g$ up to diffeomorphisms.
\end{proof}

The \emph{genus} of a handlebody $H_g$ is the genus $g$ of its boundary surface. 
Proposition \ref{connected:boundary:prop} implies the following.

\begin{cor} \label{handle:irr:cor}
Handlebodies are irreducible.
\end{cor}

Some other simple manifolds are irreducible.
\begin{prop} \label{product:irr:prop}
If $g\geqslant 1$ then $S_g\times [0,1]$ is irreducible.
\end{prop}
\begin{proof}
Its universal cover $\matR^2 \times [0,1]$ is irreducible, because its interior is diffeomorphic to $\matR^3$.
\end{proof}

\begin{ex}
If $b\geqslant 1$ the manifold $S_{g,b}\times [0,1]$ is homeomorphic to a handlebody of genus $2g+b-1 = -\chi(S_{g,b}) +1$.
\end{ex}


\subsection{Normal surfaces}
Let $M$ be a compact 3-manifold with (possibly empty) boundary. As every smooth compact manifold, $M$ has a triangulation $T$, made of a certain number $t$ of tetrahedra. We now show that $T$ can be used to treat combinatorially many interesting surfaces in $M$.

A properly embedded surface $S\subset M$ is \emph{transverse} to $T$ if it is transverse to all its simplexes. In particular $S$ does not intersect the vertices of $T$, and it intersects every edge, face, and tetrahedron respectively into a finite number of points, curves, and surfaces. Every properly embedded surface $S\subset M$ can be perturbed to be transverse to $T$.

\begin{figure}
\begin{center}
\includegraphics[width = 7 cm] {\iftoggle{BW}{Normal_surface-BW}{640px-Normal_surface}}
\nota{A normal surface intersects every tetrahedron in triangles or squares.}
\label{normal_surface:fig}
\end{center}
\end{figure}


\begin{defn}
A \emph{normal surface} is a properly embedded surface $S$ transverse to $T$ that intersects every tetrahedron into triangles or squares as in Figure \ref{normal_surface:fig}.\index{normal surface}
\end{defn}

\begin{example}
For every vertex $v$ of $T$ lying in $\interior M$ we may take a small sphere centred at $v$ that intersects every incident tetrahedron in a small triangle: we get a normal sphere. If $v$ lies in $\partial M$ we get similarly a normal disc. A surface of this type is called  \emph{vertex-linking}. Vertex-linking spheres are not very interesting since they bound balls.\index{normal surface!vertex-linking normal surface}  
\end{example}

\begin{ex}
A connected normal surface is vertex-linking if and only if it consists of triangles only (no squares).
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{incompressible-BW}{incompressible}}
\nota{We can \emph{surger} a surface $S$ along a disc $D$ with $\partial D = D\cap S$. The operation consists of removing an annular tubular neighbourhood of $\partial D$ in $S$ and adding two parallel copies of $D$. We get a new surface $S'$.}
\label{incompressible:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{incompressible2-BW}{incompressible2}}
\nota{We can also surger a surface $S$ along a disc $D$ touching the boundary in a segment. The result is a new properly embedded surface $S'$.}
\label{incompressible2:fig}
\end{center}
\end{figure}

Let $S\subset M$ be a properly embedded, possibly disconnected, compact surface.
An \emph{elementary transformation} on $S$ is one of the following moves: 
\begin{itemize}
\item the removal of a connected component of $S$ contained in some ball;
\item let $D\subset \interior M$ be a disc with $\partial D = D \cap S$: we \emph{surger} $S$ along $D$ as shown in Figure \ref{incompressible:fig};
\item let $D\subset M$ be a disc with $D\cap (S\cup \partial M) = \partial D = \alpha \cup \beta$, where $\alpha$ is an arc in $S$ and $\beta$ an arc in $\partial M$ as in Figure \ref{incompressible2:fig}-(left): we \emph{surger} $S$ as shown in the figure.
\end{itemize}
Every elementary transformation is local, \emph{i.e.}~it takes place in a ball. It transforms $S$ into a new surface $S'$. 
We fix a triangulation $T$ for $M$.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{normal2-BW}{normal2}}
\nota{Starting from the innermost curves in $\partial \Delta \cap S$ we surger along discs so that $S\cap \Delta$ consists only of discs and closed components, which we then remove.}
\label{normal2:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {normal}
\nota{The closed curves contained in a triangle are the intersections of small spherical components of $S$ with that triangle. We just remove them.}
\label{normal:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{normal3-BW}{normal3}}
\nota{If the boundary of a (\iftoggle{BW}{light grey}{yellow}) disc $D$ intersects an edge $e$ of $\partial \Delta$ twice, we pick two innermost intersections, that must be in opposite directions. There must be a \iftoggle{BW}{grey}{red} disc as shown here (exercise: use Alexander's theorem), which can be used to push $S$ in the direction indicated by the arrow. The resulting surface is shown in the right. If $e\subset \partial M$, we cannot push $S$ outside $\partial M$: instead, we surger along the \iftoggle{BW}{grey}{red} disc.}
\label{normal3:fig}
\end{center}
\end{figure}

\begin{prop}
Every properly embedded surface $S\subset M$ becomes normal after finitely many isotopies and elementary transformations.
\end{prop}
\begin{proof}
Put $S$ transverse to $T$. It intersects every tetrahedron $\Delta$ into surfaces as in Figure \ref{normal2:fig}-(left). The intersection $S\cap \partial \Delta$ consists of closed curves: the innermost ones bound discs in $\partial \Delta$, which may be pushed a bit inside $\Delta$ and then used to surger $S$. We do this with all curves (starting with the innermost ones) to transform $S$ as in Figure \ref{normal2:fig}, so that at the end $S\cap\Delta$ consists only of discs and closed surfaces. Then we remove the closed surfaces: this is an elementary transformation since $\Delta$ is a ball. We do this for every tetrahedron $\Delta$.

Now $S$ intersects every tetrahedron $\Delta$ in discs. Consider the boundary curve of one such disc: if it is contained in a face as in Figure \ref{normal:fig}-(left), it belongs to one or two discs (depending on whether the face belongs to $\partial M$ or not), which form a component of $S$ contained in a ball that can be removed. 

Suppose the boundary curve crosses twice an edge of $\Delta$: if the edge lies in the interior of $M$, we isotope $S$ as shown in Figure \ref{normal3:fig} to decrease the number of intersections of $S$ with the 1-skeleton of $T$; if the edge lies in $\partial M$ we simplify analogously by surgerying along the \iftoggle{BW}{grey}{red} disc shown in the figure. In all cases then we go back to the first step of the algorithm. 

After finitely many steps we get a surface $S$ intersecting every tetrahedron $\Delta$ in discs, whose boundary curves intersect every edge of $\Delta$ at most once. One such disc is either a triangle or a square.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{normal4-BW}{normal4}}
\nota{If we cut a tetrahedron $\Delta$ along triangles and squares we get arbitrarily many prisms with triangular or quadrilateral basis, and at most $6$ other pieces (here we get $4$ pyramids and two esahedra).}
\label{normal4:fig}
\end{center}
\end{figure}


\subsection{Interesting surfaces cannot have too many components}
We know from Proposition \ref{non:ori:prop} that a compact orientable $M$ cannot contain too many disjoint non-orientable surfaces. It can however contain arbitrarily many orientable surfaces: for instance, small surfaces contained in disjoint balls. A crucial aspect of 3-manifolds theory is that $M$ cannot contain arbitrarily many ``interesting'' surfaces, as we now see.

Two disjoint connected diffeomorphic surfaces $\Sigma,\Sigma'\subset M$ are \emph{parallel} if they cobound a region diffeomorphic to $\Sigma\times [0,1]$ with $\Sigma= \Sigma\times 0$ and $\Sigma'=\Sigma\times 1$. Two parallel surfaces are obviously isotopic. 

Let $T$ be a triangulation of a compact $M$ with (possibly empty) boundary. Let $t$ be the number of tetrahedra in $T$ and set $b_2 = \dim H_2(M,\partial M,\matZ_2)$.

\begin{lemma} \label{non:parallel:lemma}
Let $S$ be an orientable normal surface. If $S$ has more than $10t+b_2$ components, then two components $\Sigma, \Sigma'$ of $S$ are parallel and cobound a $\Sigma \times [0,1]$ which is disjoint from the other components.
\end{lemma}
\begin{proof}
The complement $M\setminus S$ intersects every tetrahedron $\Delta$ into polyhedra: there are many prisms lying between parallel triangles or squares, and at most $6$ other pieces, see Figure \ref{normal4:fig}. These at most 6 pieces are adjacent to at most 1+1+1+1+3+3 = 10 triangles and squares.

This implies that, except at most $10t$ of them, the components of $S$ are only adjacent (on both sides) to prisms. These prisms glue to form $I$-bundles. Therefore at least $b_2+1$ components of $S$ are adjacent to $I$-bundles on both sides. The twisted $I$-bundles are at most $b_2$ by Proposition \ref{non:ori:prop}, and each is adjacent to one surface. Therefore at least one surface is adjacent to a product $I$-bundle $\Sigma \times [0,1]$. \end{proof}

We get a topological corollary. A \emph{ball with holes} is a 3-manifold obtained by removing some $k\geqslant 0$ disjoint small open balls from a ball.
A \emph{sphere system} for a 3-manifold $M$ is a surface $S\subset \interior{M}$ consisting of disjoint spheres, such that no component of $M\setminus S$ is a ball with holes disjoint from $\partial M$. (Balls with holes adjacent to spherical components of $\partial M$ are allowed.) \index{ball with holes}\index{sphere system}

\begin{cor} \label{K:cor}
Let $M$ be a compact orientable 3-manifold that does not contain any non-separating sphere. There is a $K>0$ such that every sphere system in $M$ contains less than $K$ spheres.
\end{cor}
\begin{proof}
Pick a triangulation $T$ of $M$ with some $t$ tetrahedra: we prove that $K=10t + b_2+1$ works, with $b_2 = \dim H_2(M,\partial M;\matZ_2)$. Suppose by contradiction that there is a sphere system $S$ with $\geqslant K$ spheres. Via isotopies and elementary transformations we transform $S$ into a normal surface $S'$.

We now examine the effect of elementary transformations in detail. No component of $S$ is contained in a ball, otherwise by Alexander theorem an innermost component of $M\setminus S$ would be a ball. Therefore an elementary transformation cannot cancel a component of $S$. 

A surgery along a disc splits a sphere $S_0$ into two spheres $S_1, S_2$. 
We now prove that by substituting $S_0$ with either $S_1$ or $S_2$ we still get a sphere system. If we push $S_1$ and $S_2$ away from $S_0$ the surfaces $S_0, S_1, S_2$ altogether bound a ball with two holes $B$. 

By our hypothesis on $M$ the spheres $S_0, S_1$, and $S_2$ are separating. Let $N_i$ be the component of $M\setminus (S_0\cup S_1\cup S_2)$ adjacent to $S_i$ distinct from $B$, for $i=0,1,2$. If both $N_1, N_2$ are balls with holes disjoint from $\partial M$, then $N_1\cup N_2 \cup B$ also is, which is excluded. Therefore one, say $N_1$, is not a ball with holes disjoint from $\partial M$. On the other side, if $N_2 \cup B \cup N_0$ were a ball with holes disjoint from $\partial M$, then $N_0$ would also be (by Alexander's theorem), which is excluded. Therefore by substituting $S_0$ with $S_1$ we still get a sphere system.

This proves that the final normal surface $S'$ contains a sphere system with the same number $\geqslant K$ of components as $S$. Lemma \ref{non:parallel:lemma} gives a contradiction.
\end{proof}


\subsection{Prime decomposition}
We now show that the connected sum operation on oriented three-manifolds behaves like the product of natural numbers: every object decomposes uniquely into prime factors.\index{prime decomposition of three-manifolds} 

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{holes-BW}{holes}}
\nota{A reducing set of spheres (\iftoggle{BW}{grey}{red}) for $M = M_1\# M_2 \# (S^2\times S^1)$. Here $B$ is a ball with four holes and $N_i$ is $M_i$ with one hole.}
\label{holes:fig}
\end{center}
\end{figure}

\begin{teo} \label{prime:teo}
Every compact oriented 3-manifold $M$ with (possibly empty) boundary decomposes into prime manifolds:
$$M = M_1\# \ldots \# M_k$$
This list of prime factors is unique up to permutations and adding/removing copies of $S^3$.
\end{teo}
\begin{proof}
We first show the existence of a decomposition. If $M$ contains a non-separating sphere, then the proof of Proposition \ref{S2S1:prop} shows that $M = M'\# (S^2\times S^1)$. Since $H_1(M) = H_1(M')\oplus \matZ$, up to factoring finitely many copies of $S^2\times S^1$ we may suppose that every sphere in $M$ is separating.

If $M$ is prime we are done. If not, it decomposes as $M=M_1\# M_2$. We keep decomposing each factor until all factors are prime: this process must end, because a decomposition $M=M_1\# \ldots \#M_k$ gives rise to a system of $k-1$ spheres, and $k$ cannot be arbitrarily big by Corollary \ref{K:cor}.

We turn to uniqueness. Let 
$$M = M_1\# \ldots \# M_k \#_h(S^2\times S^1), \qquad M = M_1'\# \ldots \# M_{k'}'\#_{h'}(S^2\times S^1)$$
be two prime decompositions with $M_i, M_j' \neq S^2\times S^1$, so $M_i, M_j'$ are irreducible for all $i,j$. We say that a set $S \subset M$ of disjoint spheres is a \emph{reducing set of spheres} for the decomposition $M=M_1\# \ldots \# M_k\#_h(S^2\times S^1)$ if $M\setminus S$ consists of precisely one $M_i$ with some holes for each $i$, and some balls with holes disjoint from $\partial M$. An example is drawn in Figure \ref{holes:fig}. In general, we may construct $S$ by taking the spheres of the prime decomposition, plus one non-separating sphere inside each $S^2\times S^1$ summand. Similarly, let $S'$ be a reducing set of spheres for the other decomposition.

The first observation we make is that if we add to $S$ any sphere $\Sigma$ disjoint from $S$, then we still get a reducing set of spheres for the same decomposition as before. This is because $\Sigma$ is contained in a holed $M_i$ or $S^3$, and since $M_i$ is irreducible $\Sigma$ bounds a ball $B$ there. Therefore by adding $\Sigma$ we still get the same holed $M_i$, plus a possibly holed (if $B\cap S \neq \emptyset$) ball $B$.

We assume $S$ and $S'$ intersect transversely in circles and pick an innermost circle in a component of $S$ bounding a disc $D\subset S$. We surger $S'$ along $D$, thus substituting a component $S_0'$ of $S'$ with two spheres $S_1' \sqcup S_2'$. We check that the result is another sphere system for the same decomposition. We isotope the spheres $S_0', S_1', S_2'$ so that they are disjoint and cobound a ball with two holes $B_2$: the system $S'\sqcup S'_1 \sqcup S'_2$ is still reducing by the observation above. The removal of $S_0'$ then adds $B_2$ to the outside of $S_0'$, and this is equivalent to making one more hole there. 

After finitely many surgeries we get $S\cap S'=\emptyset$. By the same observation above $S\cup S'$ is a reducing set of spheres for both decompositions: therefore the pieces $M_i$ and $M_j'$ of the decompositions are pairwise diffeomorphic.

Finally we must have $h=h'$ since $M=N\#_h(S^2\times S^1) = N\#_{h'}(S^2\times S^1)$ and $H_1(M) = H_1(N) \oplus \matZ^h = H_1(N) \oplus \matZ^{h'}$.
\end{proof}

This important result is known as the \emph{Prime decomposition Theorem} for 3-manifolds: the existence of a decomposition was proved by Kneser \cite{Kn} in 1929, and its uniqueness by Milnor \cite{Mi} in 1962. In light of this result, topologists have since long restricted their attention to prime 3-manifolds, or almost equivalently to irreducible 3-manifolds.

The strategy of cutting canonically a three-manifold along surfaces has proved successful with spheres, so we now try to do the same with other surfaces. We start by studying properly embedded discs, which of course occur only in manifolds with boundary. It is tempting to guess that discs should behave roughly like spheres, because by doubling a 3-manifold along its boundary we transform properly embedded discs into spheres. We now see that this is indeed the case. As for spheres, we need to distinguish the interesting ones, that we call \emph{essential}, from the others.


\subsection{Essential discs} \label{essential:discs:subsection}
Let $M$ be a compact 3-manifold with (possibly empty) boundary. A properly embedded surface $S\subset M$ is \emph{$\partial$-parallel} if it is obtained by slightly pushing inside $M$ the interior of a compact surface $S'\subset \partial M$, possibly with boundary.\index{surface!$\partial$-parallel surface} 

In what follows $D$ and $S$ are properly embedded. 
We say that:\index{sphere!essential sphere}\index{disc!essential disc}
\begin{itemize}
\item a sphere $S\subset M$ is \emph{essential} if it does not bound a ball, 
\item a disc $D\subset M$ is \emph{essential} if it is not $\partial$-parallel.
\end{itemize}
Now, the manifold $M$ is:\index{three-manifold!$\partial$-irreducible three-manifold}
\begin{itemize}
\item \emph{irreducible} if it does not contain essential spheres, and
\item \emph{$\partial$-irreducible} if it does not contain essential discs.
\end{itemize}

To warm up, we show the following. A \emph{solid torus} is a handlebody of genus 1, that is a three-manifold diffeomorphic to $D\times S^1$.\index{solid torus}

\begin{prop} \label{irreducible:solid:torus:prop}
Let $M$ be a compact, irreducible, orientable 3-manifold with boundary, and let $D\subset M$ be an essential disc. Let $\Sigma \subset \partial M$ be the boundary component containing $\partial D$. Then:
\begin{itemize}
\item the curve $\partial D$ is non-trivial in $\Sigma$;
\item if $\Sigma$ is a torus then $M$ is a solid torus.
\end{itemize}
\end{prop}
\begin{proof}
If $\partial D$ bounds a disc $D'\subset \Sigma$ then $D\cup D'$ is a sphere, which bounds a ball because $M$ is irreducible; this ball furnishes a parallelism between $D$ and $D'$ and hence $D$ is $\partial$-parallel, a contradiction. 

If $\Sigma$ is a torus, by surgerying $\Sigma$ along $D$ we get a sphere which must bound a ball $B$. Therefore $M$ is obtained by adding a one-handle to $B$, that is it is a solid torus.
\end{proof}


\subsection{Decomposition along discs}
We now show that essential discs behave roughly like essential spheres, in the sense that there is a kind of prime decomposition theorem also for discs. After stating and proving this theorem, we will essentially forget about essential spheres and discs and focus on the 3-manifolds that do not contain them.

Let $M$ be a compact 3-manifold with (possibly empty) boundary. A \emph{disc system} in $M$ is a set of pairwise disjoint and non-parallel essential discs. 
 
\begin{prop} \label{K2:prop}
There is a $K>0$ such that every disc system in $M$ cannot contain more than $K$ discs.
\end{prop}
\begin{proof}
The proof is analogous to that of Corollary \ref{K:cor}
\end{proof}

We now want to cut irreducible manifolds along essential discs.

\begin{rem}
The opposite operation of cutting a manifold along a properly embedded disc is a 1-handle addition.
\end{rem}

We now state the analogue of Theorem \ref{prime:teo} in this context. Note that $M$ is irreducible by hypothesis: we have already eliminated the essential spheres, and we now remove the essential discs. 

\begin{teo}
Every compact oriented irreducible 3-manifold $M$ is obtained by adding 1-handles to a finite list
$$M_1,\ldots, M_k$$
of connected irreducible and $\partial$-irreducible 3-manifolds. The list is unique
up to permutations and adding/removing balls.
\end{teo}
\begin{proof}
The proof is similar to Theorem \ref{prime:teo}. 
If we cut $M$ along a maximal disc system we get some connected manifolds $M_1,\ldots, M_k$. Each $M_i$ is $\partial$-irreducible because the disc system is maximal, and it is irreducible because every sphere in $M_i\subset M$ bounds a ball $B$ in $M$, and $B$ is necessarily contained in $M_i$.

We prove uniqueness. Pick two sets of discs $S, S' \subset M$ such that by cutting along each we get irreducible and $\partial$-irreducible components. We prove that these components are the same up to adding/removing balls. We assume that $S$ and $S'$ intersect transversely. 

\begin{figure}
\begin{center}
\includegraphics[width = 7 cm] {irreducible_isotopy.pdf}
\nota{The discs $D$ and $D'$ form a sphere which bounds a ball since $M$ is irreducible. We can use this ball to isotope $S'$ away from $S$.}
\label{irreducible_isotopy:fig}
\end{center}
\end{figure}

A circle $S\cap S'$ which is innermost with respect to $S$ is bounded by two sub-discs $D\subset S$ and $D'\subset S'$, which together form a sphere: this sphere in turn bounds a ball (because $M$ is irreducible) as in Figure \ref{irreducible_isotopy:fig}. We can use the ball to isotope $S'$ away from $S$ and reduce the intersections in $S\cap S'$. After finitely many isotopies there are no circles in $S\cap S'$.

We are left to consider the arcs in $S\cap S'$. We end precisely as in Theorem \ref{prime:teo}. We observe that by adding more discs to $S$ or $S'$ we get a set of discs that $\partial$-reduces $M$ into the same list of $M_i$'s, plus possibly some balls.

Thanks to an innermost argument, we may surger some disc $D_0\subset S$ along an arc in $D_0\cap S'$ and transform it into two discs $D_1 \sqcup D_2$, both disjoint from $S$ and with less intersections with $S'$. The set $S\sqcup D_1 \sqcup D_2$ is still a reducing set for the $M_i$'s. If we remove $D_0$ from this new system, in the complement we only remove a ball: hence we can replace $D_0$ with $D_1\sqcup D_2$. After finitely many steps we get $S\cap S' = \emptyset$ and therefore $S\cup S'$ is a reducing set producing the same $M_i$'s of $S$ and $S'$, up to balls.
\end{proof}


\subsection{Projective planes}
The previous discussions show how to deal with spheres and discs, and we now turn to the only remaining compact surface with $\chi>0$: the projective plane. There is not much to say about it.

\begin{prop}
The only compact irreducible orientable 3-manifold $M$ containing $\matRP^2$ is $\matRP^3$.
\end{prop}
\begin{proof}
The orientable $M$ contains the orientable tubular neighbourhood $N=\matRP^2 \timtil I$ of $\matRP^2$. The boundary $\partial N$ is the orientable cover $S^2$ or $\matRP^2$. Since $M$ is irreducible, the sphere $\partial N$ bounds a ball $B$. Therefore $M$ is uniquely determined as the manifold obtained by capping off the boundary sphere of $N$. 

The manifold $\matRP^3$ is irreducible (because its cover $S^3$ is) and contains $\matRP^2$, hence we must have $M=\matRP^3$.
\end{proof}

This proposition does not hold for non-orientable three-manifolds, which might contain $\matRP^2$ with a product neighbourhood $\matRP^2\times I$. These 
cases are difficult to deal with, so one typically excludes them \emph{a priori} by requiring the manifold to be \emph{$\matRP^2$-irreducible}, which means that it does not contain two-sided projective planes.\index{three-manifold!$\matRP^2$-irreducible three-manifold}
