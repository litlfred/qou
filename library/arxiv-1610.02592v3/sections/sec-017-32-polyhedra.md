---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-017-32-polyhedra
section_title: "Polyhedra"
section_number: 3.2
pages: 86-90
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.986
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
A polyhedron in $\matH^n$ is a natural geometric object, that may be used to visualise discrete groups in $\Iso(\matH^n)$ and hence hyperbolic manifolds. 
Polyhedra may sometimes be combined to form some tessellations of the space. 


\subsection{Polyhedra} \label{polyhedra:subsection}
A \emph{half-space} in $\matH^n$ is the closure of one of the two portions of space delimited by a hyperplane. We say that a set of half-spaces is locally finite if their boundary hyperplanes are. \index{polyhedron}

\begin{defn}
A $n$-dimensional \emph{polyhedron} $P$ in $\matH^n$ is the intersection of a locally finite set of half-spaces. We also assume that $P$ has non-empty interior.
\end{defn}

A subset $S\subset \overline{\matH^n}$ is \emph{convex} if $x,y\in S$ implies that the segment connecting $x,y$ is also contained in $S$ (such a segment is a half-line or a line if one or both points lie in $\partial \matH^n$). Every polyhedron $P$ is clearly convex because it is the intersection of convex sets. Its closure $\overline P$ in $\overline{\matH^n}$ is also convex.
\index{convex subset}

Let $H\subset \matH^n$ be a half-space containing the polyhedron $P$. If non-empty, the intersection $F=\partial H\cap P$ is called a \emph{face} of $P$. The \emph{supporting subspace} of $F$ is the smallest subspace of $\matH^n$ containing $F$; the \emph{dimension} of a face is the dimension of its supporting subspace. A face of dimension $0$, $1$, and $n-1$ is called a \emph{vertex}, an \emph{edge}, and a \emph{facet}.

\begin{ex} \label{intersection:faces:ex}
If non-empty, the intersection of faces of $P$ is a face.
\end{ex}

\begin{ex} Every $k$-dimensional face is a polyhedron in its supporting $k$-dimensional space.
\end{ex}

The \emph{convex hull} of a set $S\subset \overline{\matH^n}$ is the intersection of all the convex sets containing $S$. \index{convex hull}

\begin{ex} \label{hull:ex}
The convex hull of finitely many points in $\matH^n$ that are not contained in a hyperplane is a compact polyhedron. Conversely, every compact polyhedron has finitely many vertices and is the convex hull of them.
\end{ex}

Everything we said holds with no modifications for $\matR^n$. On $S^n$ some care should be taken: some definitions need to be modified slightly to take into account the annoying presence of antipodal points. We gloss over this technical point.


\subsection{Finite polyhedra}
We now enlarge slightly the class of compact polyhedra by admitting finitely many vertices at infinity. \index{polyhedron!finite polyhedron}

\begin{defn}
A \emph{finite polyhedron} is the convex hull of finitely many points $x_1,\ldots, x_k \in \overline{\matH^n}$ that are not contained in the closure of a hyperplane.
\end{defn}

The $x_i$'s that lie in $\partial \matH^n$ are called \emph{ideal vertices}, while the usual vertices of $P$ are the \emph{finite} or \emph{actual vertices}. The ideal vertices form the set $\overline P \setminus P$.

\begin{ex}
A finite polyhedron $P$ has finitely many faces and is the convex hull of its ideal and finite vertices.
\end{ex}

We want to estimate the volume of finite polyhedra, and to do this we need a lemma. Given a horosphere $O$ centred at $p\in\partial \matH^n$ and a domain $D\subset O$, the \emph{cone} $C$ of $D$ over $p$ is the union of all the half-lines exiting from $D$ and pointing towards $p$, see Figure \ref{volume:fig}.

\begin{lemma} \label{O:lemma}
Let $O$ be a horosphere centred at $p\in \partial \matH^n$, $D\subset O$ any domain and $C$ the cone over $D$. The following equality holds:
$$\Vol(C) = \frac {\Vol_O (D)}{n-1}$$
where $\Vol_O$ is the $(n-1)$-dimensional volume in the flat $(n-1)$-manifold $O$.
\end{lemma}
\begin{proof}
Let $O$ have some height $x_n=h$ as in Figure \ref{volume:fig}-(left). We obtain
$$\Vol(C) = \int_D dx \int_{h}^\infty \frac 1{t^{n}}dt = \frac 1{n-1}\int_D \frac{dx}{h^{n-1}} = \frac 1{n-1} \cdot \Vol_O(D).$$
The proof is complete.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{volume-BW}{volume}} 
\nota{The cone $C$ over a domain $D\subset O$ has volume proportional to the area of $D$ (left). If the domain is compact, the cone has finite volume: therefore a finite polyhedron has finite volume (right).}
\label{volume:fig}
\end{center}
\end{figure}

We now turn to finite polyhedra.

\begin{prop}
Every finite polyhedron has finite volume.
\end{prop}
\begin{proof}
For every ideal vertex of $P$, a small horoball centred at $p$ intersects $P$ into a cone that has finite volume. The polyhedron $P$ decomposes into finitely many cones and a bounded region, see Figure \ref{volume:fig}-(right).
\end{proof}

A finite polyhedron without finite vertices is called an \emph{ideal polyhedron}.
\index{polyhedron!ideal polyhedron}


\subsection{Polygons}
A polygon is just a polyhedron of dimension two. In contrast with Euclidean geometry, a strikingly simple formula relates the area of a finite polygon with its inner angles. We define the inner angle of an ideal vertex to be zero. 

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{triangle_area-BW}{triangle_area}}
\nota{A triangle with at least an ideal vertex (left). The area of a triangle with finite vertices can be derived as the area difference of triangles with one ideal vertex (right).}
\label{triangle_area:fig}
\end{center}
\end{figure}

\begin{prop} \label{polygon:area:prop}
A polygon $P$ with inner angles $\alpha_1,\ldots, \alpha_n$ has area
$$\Area (P) = (n-2)\pi - \sum_{i=1}^n \alpha_i.$$
\end{prop}
\begin{proof}
Every polygon decomposes into triangles, and it suffices to prove the formula on these. Consider first a triangle $T$ with at least one vertex at infinity. We use the half-plane model and send this vertex to $\infty$ as in Figure \ref{triangle_area:fig}-(left). We suppose that the \iftoggle{BW}{grey}{red} dot is the origin of $\matR^2$, hence 
$$T = \big\{(r\cos\theta, y)\ | \ \beta\leqslant \theta \leqslant \pi-\alpha, \ y\geqslant r\sin\theta\big\}$$
and we get
\begin{align*}
\Area(T) & = \int_T \frac 1{y^2}dxdy = \int_{\pi-\alpha}^{\beta} \int_{r\sin\theta}^\infty \frac{-r\sin \theta}{y^2}dyd\theta \\
 & = \int_{\pi-\alpha}^\beta -r\sin\theta \left[-\frac 1y\right]_{r\sin\theta}^\infty d\theta = 
\int_{\beta}^{\pi-\alpha} \frac{r\sin\theta}{r\sin\theta}d\theta \\
 & = \int_{\beta}^{\pi-\alpha} 1 = \pi-\alpha-\beta.
\end{align*} 
The area of a triangle with finite vertices $ABC$ is deduced as in Figure \ref{triangle_area:fig}-(right) using the formula
$$\Area (ABC) = \Area(AB\infty) + \Area(BC\infty) - \Area (AC\infty).$$
The proof is complete.
\end{proof}

The sum of the inner angles of a hyperbolic polygon is strictly smaller than that of a Euclidean polygon with the same number of sides, and the difference between these two numbers is precisely its area. 

\begin{cor} Every ideal triangle has area $\pi$.
\end{cor}


\subsection{Platonic solids} \label{platonici:subsection}
The theory of three-dimensional polyhedra in $\matH^3$ is very rich: we limit ourselves to the study of the platonic solids.

The five Euclidean platonic solids are the regular tetrahedron, the cube, the regular octahedron, icosahedron, and dodecahedron. We now see that each platonic solid $P\subset \matR^3$ generates a nice continuous family of solids in the three geometries $\matH^3, \matR^3$, and $S^3$.

To construct this family we fix any point $x$ in $\matH^3$ and represent $P$ centred at $x$ with varying size. To do this, we put $P$ inside the Euclidean tangent space $T_x\matH^3$ centred at the origin and with some radius $t>0$. Consider the image of its vertices by the exponential map and take their convex hull. We indicate by $P(-t)$ the resulting polyhedron in $\matH^3$. The polyhedron $P(-t)$ is combinatorially equivalent to $P$ and has the same symmetries of $P$.

We extend this family to the other geometries as follows. The polyhedron $P(0)$ is the Euclidean $P$ (unique up to dilations), and $P(t)$ with $t>0$ is the spherical $P$, constructed as above with $S^3$ instead of $\matH^3$: we fix $x\in S^3$, take a copy of $P$ inside $T_x S^3$ with radius $t$, project its vertices, and take the convex hull. We define the spherical $P(t)$ only for $t \in (0, \frac \pi 2]$: when $t= \frac\pi 2$ it degenerates to a hemisphere. We also define $P(-\infty)$ as the ideal hyperbolic platonic solid obtained by sending all the vertices at infinity.

\begin{figure}
\begin{center}
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{Icosahedron-BW}{256px-Icosahedron}} \qquad
\includegraphics[width = 3.5 cm] {\iftoggle{BW}{Dodecahedron-BW}{245px-Dodecahedron}}
\nota{The regular icosahedron and dodecahedron.}
\label{icosaedro:fig}
\end{center}
\end{figure}

We have defined a polyhedron $P(t)$ for all $t\in [-\infty, \frac \pi 2]$, that lies in $\matH^3, \matR^3, S^3$ depending on whether $t$ is negative, null, or positive. In some sense the polyhedron $P(t)$ depends continuously on $t$ also when it crosses the value $t=0$: when $t\to 0$ the polyhedron in $\matH^3$ or $S^3$ shrinks, and every polyhedron tends to a Euclidean one when shrunk. 

In particular the dihedral angle $\theta(t)$ of $P(t)$ varies continuously with $t\in [-\infty, \frac \pi2]$. The function $\theta(t)$ is strictly monotone and we now determine its image. The \emph{vertex valence} of $P$ is the number of edges incident to each vertex.

\begin{prop} \label{dihedral:platonic:prop}
Let $n\in\{3,4,5\}$ be the vertex valence of $P$. It holds 
$$\theta \left(\left[-\infty, \frac \pi 2\right]\right) = \left[\frac{n-2}n \pi, \pi\right].$$
\end{prop}
\begin{proof}
Since $\theta$ is continuous and monotone increasing, it suffices to show that $\theta(-\infty) = \frac{n-2}n\pi$ and $\theta(\frac \pi 2) = \pi$.

By intersecting the ideal polyhedron $P(-\infty)$ with a small horosphere $O$ centred at an ideal vertex $v$ we get a regular $n$-gon in the Euclidean plane $O$, with interior angles $\frac{n-2}n\pi$. The dihedral angle at an edge $e$ incident to $v$ is measured by intersecting $P(-\infty)$ with any hypersurface orthogonal to $e$: since $O$ is orthogonal to $e$ we get $\theta(-\infty) =  \frac{n-2}n\pi$. 

The polyhedron $P(\frac \pi 2)$ is a hemisphere and hence $\theta(\frac \pi 2) = \pi$.
\end{proof}

For some values of $t$, the platonic solid $P(t)$ may have nice dihedral angles $\theta(t)$, for instance angles that divide $2\pi$. In the Euclidean world, the only platonic solid with such nice dihedral angles is the cube. In the hyperbolic and spherical world we find more.

The platonic solids with dihedral angles that divide $2\pi$ are listed in Table \ref{platonic:table}. The table is just a consequence of Proposition \ref{dihedral:platonic:prop}: it suffices to know the Euclidean dihedral angles for $P$, and all the angles bigger (smaller) than this value are spherical (hyperbolic).

\begin{table} 
\begin{center}
\begin{tabular}{c||cccc}
\phantom{\Big|} polyhedron & $\theta = \frac \pi 3$ & $\theta = \frac{2\pi}5$ & $\theta = \frac \pi 2$ &
$\theta = \frac{2\pi}3$ \\
\hline\hline
\rule{0pt}{3ex}
\phantom{\big|}  tetrahedron & ideal $\matH^3$ & $S^3$ & $S^3$ & $S^3$ \\
\phantom{\big|}  cube & ideal $\matH^3$ & $\matH^3$ & $\matR^3$ & $S^3$ \\
\phantom{\big|}  octahedron & & & ideal $\matH^3$ & $S^3$ \\
\phantom{\big|} icosahedron & & & & $\matH^3$ \\
\phantom{\big|} dodecahedron & ideal $\matH^3$ & $\matH^3$ & $\matH^3$ & $S^3$ \\
\end{tabular}
\end{center}
\nota{The platonic solids with dihedral angle $\theta$ that divide $2\pi$.}
\label{platonic:table}
\end{table}

In particular, there are four right-angled platonic solids: the spherical tetrahedron, the  Euclidean cube, the hyperbolic dodecahedron, and the ideal hyperbolic octahedron.
