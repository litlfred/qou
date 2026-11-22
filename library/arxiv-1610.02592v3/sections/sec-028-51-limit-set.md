---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-028-51-limit-set
section_title: "Limit set"
section_number: 5.1
pages: 143-151
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.971
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
How does a discrete group $\Gamma $ of isometries of $\matH^n$ act on the boundary at infinity $\partial \matH^n$? We now prove that $\partial \matH^n$ divides canonically into two $\Gamma$-invariant subsets: an open zone $\Omega(\Gamma)$ where $\Gamma$ acts properly discontinuously, and a closed one $\Lambda(\Gamma)$ where it does not. These regions are called respectively the \emph{domain of discontinuity} and the \emph{limit set} of $\Gamma$. 


\subsection{The limit set}
Throughout this section, we let $\Gamma$ be a non-trivial discrete group of isometries of $\matH^n$. Fix a point $x\in\matH^n$. We now that the orbit $\Gamma(x)$ is a discrete subset of $\matH^n$. The \emph{limit set} $\Lambda (\Gamma)\subset \partial \matH^n$ of $\Gamma$ is the set of all the accumulation points of the orbit $\Gamma(x)$ in $\overline{\matH^n}$.\index{limit set}\index{$\Lambda(\Gamma)$}

\begin{ex}
The limit set does not depend on $x$.
\end{ex}

The limit set is clearly a closed $\Gamma$-invariant subset of $\partial \matH^n$. If $\Gamma' < \Gamma$ we obviously get $\Lambda(\Gamma')\subset \Lambda(\Gamma)$.

\begin{ex} \label{index:lambda:ex}
If $\Gamma'$ has finite index in $\Gamma$ then $\Lambda(\Gamma') = \Lambda(\Gamma)$.
\end{ex}

Recall that $\Gamma$ is elementary if it fixes a finite set of points in $\overline{\matH^n}$.

\begin{example} If $\Gamma$ is elementary and acts freely, that is $M = \matH^n/_\Gamma$ is wither a cusp or a tube (see Proposition \ref{elementary:prop}), then $\Lambda(\Gamma) = \Fix(\Gamma)$ consists of one or two points. 
\end{example}

We now characterise the elementary subgroups of $\Iso(\matH^n)$. Recall that $\Gamma$ is \emph{virtually P} if it has a finite-index subgroup that is P (where P is some property).\index{group!elementary group}

\begin{prop} \label{elementary:4:prop}
The following are equivalent:
\begin{enumerate}
\item $\Gamma$ is elementary,
\item $\Gamma$ fixes either a point $x\in\matH^n$, or a line, or a point $x\in\partial\matH^n$ and all the horospheres centred at $x$,
\item $\Gamma$ is virtually abelian,
\item $\Lambda(\Gamma)$ consists of 0, 1, or 2 points.
\end{enumerate}
\end{prop}
\begin{proof}
(1) $\Rightarrow$ (2). We expand on the proof of Proposition \ref{elementary:prop} by taking elliptic elements into account.

By hypothesis $\Gamma$ fixes a finite set of points in $\overline{\matH^n}$. If some of them lie in $\matH^n$, then $\Gamma$ fixes their barycenter and we are done. If $\Gamma$ fixes more than two points in $\partial \matH^n$, a barycenter is also defined: their convex hull is an ideal polyhedron of dimension at least 2, we can truncate (via horospheres) all the vertices by the same small volume and take the barycenter of the vertices of the resulting compact combinatorial polyhedron. So we are done also in this case. If $\Gamma$ fixes two points, it fixes a line.

We are left with the case where $\Gamma$ fixes a point $x\in \partial \matH^n$, and no other finite set of points. The proof of Lemma \ref{fissi:lemma} extends as is when $\varphi_2$ is elliptic, and shows that if $\Gamma$ contains a hyperbolic element $\varphi_1$ then every other non-trivial element of $\Gamma$ is either hyperbolic or elliptic and fixes the same axis of $\varphi_1$, but this is excluded: so $\Gamma$ contains only parabolics and elliptics, and these must fix all the horospheres centred at $x$, as required.

(2) $\Rightarrow$ (3). The group $\Gamma$ is virtually isomorphic to a discrete subgroup of $\Iso(\matR^m)$ for some $m$ and we apply Theorem \ref{discrete:virtual:abelian:teo}.

(3) $\Rightarrow$ (4). By Exercise \ref{index:lambda:ex} we may suppose that $\Gamma$ is abelian. By adapting the proof of Lemma \ref{commute:lemma} to elliptics we see (exercise) that $\Gamma$ satisfies (2) and hence we get (4).

(4) $\Rightarrow (1)$. If $\Lambda(\Gamma)$ is empty then $\Gamma$ is finite and fixes a point by Proposition \ref{finite:fixed:prop}.
If it consists of one or two points, these are preserved by $\Gamma$.
\end{proof}


\subsection{Minimality}
Let $\Gamma$ be a non elementary non-trivial discrete group of isometries of $\matH^n$.
We are interested in the action of $\Gamma$ on $\Lambda(\Gamma)$. We want to prove that the action is \emph{minimal}, that is $\Lambda(\Gamma)$ has no invariant non-empty proper closed subset.

Recall from Section \ref{polyhedra:subsection} that every closed subset $S\subset \overline{\matH^n}$ has a well-defined convex hull $C(S)\subset \overline{\matH^n}$. The convex hull $C(S)$ is closed and is the intersection of all the closed half-spaces containing $S$. We have $C(S) \cap \partial \matH^n = S \cap \partial \matH^n$.

\begin{prop}
If $\Gamma$ is not elementary, its action on $\Lambda(\Gamma)$ is minimal.
\end{prop}
\begin{proof}
Let $S\subset \Lambda(\Gamma)$ be a non-empty closed $\Gamma$-invariant subset. Since $S$ is $\Gamma$-invariant, its convex hull $C(S)$ also is. Since $\Gamma$ is not elementary, $S$ contains at least two points and hence the intersection $C(S)\cap \matH^n$ is not empty. If $x\in C(S)\cap \matH^n$, its $\Gamma$-orbit is confined in $C(S)$ and hence also its accumulation points are: therefore $\Lambda(\Gamma)\subset C(S)\cap \partial \matH^n = S$ and hence $\Lambda(\Gamma) = S$.
\end{proof}

\begin{cor} \label{normal:limit:cor}
If $\Gamma$ is not elementary and $\Gamma' \triangleleft \Gamma$ is an infinite normal subgroup, then $\Lambda(\Gamma') = \Lambda (\Gamma)$.
\end{cor}
\begin{proof}
For every $\gamma \in \Gamma$ we have $\gamma^{-1}\Gamma' \gamma = \Gamma'$, so $\gamma$ sends the orbit $\Gamma'(x)$ to the orbit $\Gamma'(\gamma(x))$ and hence preserves $\Lambda(\Gamma')$. Therefore $\Lambda(\Gamma')$ is $\Gamma$-invariant.

The limit set $\Lambda(\Gamma')$ is not empty because $\Gamma'$ is infinite: the minimality of $\Lambda(\Gamma)$ implies that $\Lambda(\Gamma') = \Lambda(\Gamma)$.
\end{proof}


\subsection{The convex core}
If $C\subset \overline{\matH^n}$ is a closed convex set, we define the \emph{nearest point retraction}\index{nearest point retraction} 
$$r\colon \overline{\matH^n} \to C$$ 
as the map that sends $x$ to the point $r(x)\in C$ that is closer to $x$. If $x\in\partial \matH^n$, we interpret $r(x)$ as the first point of $C$ that is contained in some horosphere centred at $x$. We have $r(x)=x$ if and only if $x\in C$. The map $r$ is continuous. Using the geodesic from $x$ to $r(x)$ we can construct a natural deformation retraction of $\overline{\matH^n}$ onto the closed convex set $C$.

Let $\Gamma < \Iso(\matH^n)$ be a non elementary non-trivial discrete group. The convex hull of $\Lambda(\Gamma)$ is $\Gamma$-invariant, so it makes sense to define the following.\index{convex core} 

\begin{defn} The \emph{convex core} of the orbifold $O=\matH^n/_\Gamma$ is the quotient $C(\Lambda(\Gamma))/_\Gamma \subset O$ of the convex hull $C(\Lambda(\Gamma))$ of the limit set $\Lambda(\Gamma)$.
\end{defn}

We are of course mostly interested in the case where $\Gamma$ acts freely and hence $M=\matH^n/_\Gamma$ is a manifold.
The deformation retraction defined above is $\Gamma$-invariant, therefore every complete hyperbolic manifold $M$ deformation retracts onto its convex core. In particular, $M$ is homotopically equivalent to its convex core.


\subsection{The domain of discontinuity}
Let $\Gamma < \Iso(\matH^n)$ be a non elementary non-trivial discrete group. The \emph{domain of discontinuity} of $\Gamma$ is the open set\index{domain of discontinuity}\index{$\Omega(\Gamma)$}
$$\Omega(\Gamma) = \partial\matH^n \setminus \Lambda(\Gamma).$$
The following proposition explains the terminology.
\begin{prop}
The action of $\Gamma$ on $\matH^n \cup \Omega(\Gamma)$ is properly discontinuous.
\end{prop}
\begin{proof}
The nearest point retraction $r$ sends $\matH^n \cup \Omega(\Gamma)$ to $C(\Lambda(\Gamma)) \setminus \Lambda(\Gamma)$ and commutes with $\Gamma$. The action of $\Gamma$ on the latter set is properly discontinuous (since it is contained in $\matH^n$), so the action on the former also is.
\end{proof}

\begin{prop}
If $\Vol(\matH^n/_\Gamma)<+ \infty $ then $\Lambda(\Gamma) = \partial \matH^n$.
\end{prop}
\begin{proof}
If $\Omega(\Gamma)\neq \emptyset$, pick $x\in \Omega(\Gamma)$. The point $x$ has a neighbourhood system consisting of half-spaces. Since $\Gamma$ acts properly discontinuously on $\matH^n \cup \Omega(\Gamma)$, there is some half-space $H$ which intersects only finitely many $\Gamma$-translates, contradicting the finite volume hypothesis.
\end{proof}

In this book we are mostly interested in finite-volume complete hyperbolic manifolds or orbifolds $\matH^n/_\Gamma$, and for these the limit set is just the whole boundary, regardless of $\Gamma$. This apparently disappointing piece of information has some interesting algebraic consequences. 

\begin{cor} \label{normal:abelian:cor}
If $\Vol(\matH^n/_\Gamma) <+\infty$ then
$\Gamma$ does not contain any non-trivial virtually abelian normal subgroup.
\end{cor}
\begin{proof}
Let $H\triangleleft \Gamma$ be virtually abelian. If $H$ is infinite, then $\Lambda(H) = \Lambda (\Gamma)=\partial \matH^n$ by Corollary \ref{normal:limit:cor}, contradicting Proposition \ref{elementary:4:prop}. If $H$ is finite, then $\Fix(H)$ is a non-empty proper subspace of $\matH^n$ and $\Gamma$ acts on $\Fix(H)$ because $H$ is normal. If $\Fix(H)$ is a point then $\Gamma$ is elementary, otherwise we get $\Lambda(\Gamma) \subset \partial \Fix(H)$, a contradiction in both cases.
\end{proof}

\begin{cor}
The fundamental group of a finite-volume complete hyperbolic manifold is never solvable.
\end{cor}
\begin{proof}
Solvable groups have non-trivial normal abelian subgroups, as proved in Proposition \ref{solvable:normal:prop}.
\end{proof}


\subsection{Schottky groups}
In all the examples encountered up to now the limit set $\Lambda(\Gamma)$ consists of either few points or the whole of $\partial \matH^n$. There are many cases where $\Lambda(\Gamma)$ is a more interesting (and often beautiful) set. The simplest examples are probably the following.

Choose a number $k\geqslant 2$ and $2k$ half-spaces $H_1,\ldots,H_{2k} \subset \matH^n$ with disjoint closures in $\overline{\matH^n}$. 
The closed complement $C = \matH^n \setminus \interior{H_1 \cup \ldots \cup H_{2k}}$ is a convex subset bounded by $2k$ disjoint hyperplanes. If we pair isometrically these hyperplanes we get a complete (exercise) hyperbolic manifold $M$, which is hence $M=\matH^n/_\Gamma$ for some $\Gamma$. The hyperbolic manifold $M$ has infinite volume and is the interior of a compact manifold that decomposes into one 0-handle and $k$ 1-handles. The group $\Gamma$ is free with $k$ generators.\index{group!Schottky group}

\begin{ex} If $n=2$, the limit set $\Lambda(\Gamma)\subset \partial \matH^2 = S^1$ is a Cantor set.
\end{ex}


\subsection{Parabolic and hyperbolic points}
Let $\Gamma < \Iso(\matH^n)$ be a non elementary non-trivial discrete group. A \emph{parabolic point} $x\in \partial \matH^n$ for $\Gamma$ is a point that is fixed by some parabolic element $\gamma \in \Gamma$. Similarly, a \emph{hyperbolic point} is a point that is fixed by some hyperbolic element.\index{parabolic point}\index{hyperbolic point}

\begin{prop}
The set of all parabolic (hyperbolic) points is either empty or a dense subset of $\Lambda(\Gamma)$.
\end{prop}
\begin{proof}
They clearly form a $\Gamma$-invariant subset, so its closure also is. We conclude because $\Lambda(\Gamma)$ is minimal.
\end{proof}

\begin{cor} \label{parabolic:hyperbolic:dense:cor}
If $\Vol(\matH^n/_\Gamma)<+\infty $, the set of all parabolic (hyperbolic) points is either empty or dense in $\partial \matH^n$.
\end{cor}


\subsection{Horoballs in the hyperboloid model}
In the conformal models, horoballs are just Euclidean balls tangent to the boundary at infinity. In the hyperboloid model $I^n$ there is a more algebraic description. We denote by
$$L = \{x\in \matR^{n+1}\ \big|\ \langle x,x \rangle = 0, \ x_{n+1}>0\}$$ 
the positive light cone and recall from Section \ref{projective:compactification:subsection} that the boundary at infinity $\partial I^n$ may be interpreted as the set of rays in $L$. More than that, every vector $x\in L$ determines a horoball $O$ centred at $[x]\in\partial I^n$, via the equation
$$O = \big\{y\in I^n \ |\ -1 \leqslant \langle x,y \rangle < 0\big\}.$$
The horoball gets smaller as $x$ goes to infinity.
\begin{ex}
This is really a horoball centred at $[x]$.
\end{ex}
\begin{proof}[Hint]
Prove that the boundary horosphere $\langle x,y \rangle =-1$ is orthogonal to all the lines pointing to $x$. 
\end{proof} 

There is also a simple (and maybe surprising) geometric relation between the vector $x$ and the corresponding horoball in the Poincar\'e disc model $D^n$. Represent $D^n$ inside the hyperplane $x_{n+1} = 0$, and let $\pi \colon I^n \to D^n$ the isometry obtained by projecting towards $P=(0,\ldots,0,-1)$, considered in Section \ref{Poincare:subsection}. By projecting towards $P$ we also get a homeomorphism $\pi\colon L \to D^n$.

\begin{ex} \label{Euclidean-centre:ex}
The Euclidean centre of the horoball $\pi(O)$ is $\pi(x)$.
\end{ex}


\subsection{The Epstein--Penner decomposition} \label{EP:subsection}
We now show that every cusped finite-volume hyperbolic manifold decomposes canonically into some ideal polyhedra. This decomposition is known as the \emph{canonical} or \emph{Epstein--Penner decomposition}.\index{Epstein--Penner decomposition}

Let $M = \matH^n/_\Gamma$ be a non-compact finite-volume complete hyperbolic manifold. The manifold $M$ is diffeomorphic to the interior of a compact $N$ with $c\geqslant 1$ boundary components. We fix $c$ disjoint truncated cusps $H_1, \ldots, H_c \subset M$. Their lifts in $\matH^n$ are $c$ disjoint $\Gamma$-orbits $B_1^i, \ldots, B_c^i$ of disjoint horoballs.

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{horoballs-BW}{horoballs}} 
\nota{By glueing two identical ideal triangles along their sides we get a thrice-punctured sphere $S$, and we choose three disjoint truncated cusps in it having the same area (left). In the universal cover, the two ideal triangles of $S$ lift to the Farey tessellation already shown in Figure \ref{tiling_Farey:fig}, and each of the three truncated cusps lifts to infinitely many disjoint horoballs (right). The Euclidean centre of the horoballs is shown here, in relation to Exercise \ref{Euclidean-centre:ex}.}
\label{horoballs:fig}
\end{center}
\end{figure}


\begin{example}
Consider the thrice-punctured sphere $S$ obtained by gluing two identical copies of an ideal triangle along their sides. This is a complete finite-volume hyperbolic surface with three cusps. We may fix three disjoint truncated cusps of the same area, as sketched in Figure \ref{horoballs:fig}-(left). These lift to three families of disjoint horoballs as in Figure \ref{horoballs:fig}-(right).
\end{example}

We use the hyperboloid model $I^n$ and interpret a horoball as a point in the positive light cone $L$ as explained in the previous section. The $\Gamma$-orbits $B_1^i, \ldots, B_c^i$ of horoballs form a discrete subset in $L$. If we modify the initial truncated cusp $H_j$, all the points $B_j^i\in L$ are rescaled by the same constant.

We make a crucial observation: the points $B_j^i$ are discrete in $L$, but the rays that contain them form a countable dense subset of $L$, because they correspond to the parabolic points of $\Gamma$, that are dense by Corollary \ref{parabolic:hyperbolic:dense:cor}.

\begin{figure}
\begin{center}
\includegraphics[width = 13 cm] {\iftoggle{BW}{convex-hull-BW}{convex-hull}} 
\nota{A portion of the convex hull $C$ for the thrice-punctured sphere of Figure \ref{horoballs:fig}. As suggested by Exercise \ref{Euclidean-centre:ex} we determine the horoballs in $L$ by projecting the Euclidean centers of their representations in the disc model. The black half-line above each horoball in $L$ is contained in $C$, see Proposition \ref{Bji:prop}.}
\label{convex-hull:fig}
\end{center}
\end{figure}

We now define $C\subset \matR^{n+1}$ as the convex hull of the points $B_j^i$ in $\matR^{n+1}$. We note that $C$ is $\Gamma$-invariant. An example is shown in Figure \ref{convex-hull:fig}.
The convex hull will define a decomposition of $M$ into ideal polyhedra. 

The convex hull $C$ is contained in the convex hull of $L$, that consists of all the positive timelike and lightlike vectors. The following proposition says that $C$ intersects $L$ into countably many half-lines based at the points $B_j^i$.

\begin{prop} \label{Bji:prop}
The set $C\cap L$ is the set of points $\alpha B_j^i$ for some $\alpha \geqslant 1$.
\end{prop}
\begin{proof}
Pick a point $x\in L$ not of this type: the segment $0x$ does not intersect $\{B_j^i\}$. Since $\{B_j^i\}\subset L$ is discrete, we can perturb the hyperplane $H$ tangent in $x$ to $L$ so that it intersects $L$ into a small ellipsoid around $0x$, and so that $\{B_j^i\}$ lies on the opposite side of $H$ of $x$. Therefore $x \not \in C$.

Conversely, pick a point $x = \alpha B_{j_0}^{i_0}$. The rays containing the points $B_j^i$ form a dense set in $L$, so we can find a sequence of $B_j^i\neq B_{j_0}^{i_0}$ such that $[B_j^i]$ converges to $[B_{j_0}^{i_0}]$. Since $\{B^i_j\}$ is discrete, the points $B_j^i$ go to infinity in the sequence and hence the segment with endpoints $B_j^i$ and $B_{j_0}^{i_0}$ approaches $x$ in the limit. Therefore $x\in C$.
\end{proof}

\begin{prop}
Every timelike ray intersects $\partial C$ exactly once.
\end{prop}
\begin{proof}
Every timelike ray $r$ enters in the interior of a polyhedron spanned by some $B_j^i$, so it intersects $C$ and hence $\partial C$. Consider a point $x \in \partial C \cap r$. Every supporting hyperplane for $x$ must be spacelike because the rays containing the $B_j^i$ are dense. Therefore $C \cap r$ is a half-line and $x$ is its endpoint.
\end{proof}

In particular $\partial C = (\partial_{\rm l}C) \sqcup (\partial_{\rm t}C)$ consists of the lightlike vectors $\partial_{\rm l} C = C\cap L$ and some timelike vectors $\partial_{\rm t} C$. The previous proposition furnishes a natural 1-1 correspondence $\partial_{\rm t} C \longleftrightarrow I^n$ with the hyperboloid model by projecting along timelike lines.

\begin{prop}
The timelike boundary $\partial_{\rm t} C$ is tessellated by countably many Euclidean $n$-dimensional polyhedra with vertices in $\{B_j^i\}$.
\end{prop}
\begin{proof}
Consider a point $x\in\partial_{\rm t} C$ and a supporting hyperplane $H$. As already mentioned, the hyperplane $H$ is spacelike and the intersection $H\cap \partial_{\rm t} C$ is some $k$-dimensional polyhedron, convex hull of finitely many points in $\{B_j^i\}$. If $k<n$ we can rotate $H$ until it meets one more point $B_j^i$ and after finitely many rotations we get a $n$-dimensional polyhedron.

We have proved that $\partial_{\rm t} C$ is paved by $n$-dimensional polyhedra with vertices in $\{B_j^i\}$ and intersecting in common faces. The polyhedra are locally finite because $\{B_j^i\}$ is discrete, hence they form a tessellation.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 13 cm] {\iftoggle{BW}{hyperboloid-BW}{hyperboloid}} 
\nota{The $\Gamma$-invariant decomposition of the hyperbolic plane into ideal polygons obtained by projecting the Euclidean polygons of Figure \ref{convex-hull:fig} from $\partial C$ to $I^2$. This is in fact the Farey tessellation of Figure \ref{horoballs:fig}.}
\label{hyperboloid:fig}
\end{center}
\end{figure}

The tessellation of $\partial_{\rm t}C$ is $\Gamma$-invariant and projects to a $\Gamma$-invariant tessellation of the hyperbolic space $I^n$ into ideal polyhedra, which projects in turn to a tessellation of $M$ into finitely many ideal polyhedra, called the \emph{canonical} or \emph{Epstein-Penner decomposition}. An example is shown in Figure \ref{hyperboloid:fig}. We have discovered the following.

\begin{teo} \label{EP:teo}
Every finite-volume non-compact complete hyperbolic manifold can be tessellated into finitely many ideal polyhedra.
\end{teo}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{TBD}{3ps-1}} 
\includegraphics[width = 6 cm] {\iftoggle{BW}{TBD}{3ps-2}} 
\nota{Different choices of truncated cusps may lead to distinct decompositions into ideal polyhedra.}
\label{3ps:fig}
\end{center}
\end{figure}

The canonical tessellation depends only on the chosen initial truncated cusps $H_1,\ldots, H_c$. Different choices may give different canonical tessellations, an example is sketched in Figure \ref{3ps:fig}. We can parametrize these choices by recording the volumes $V_1,\ldots, V_c$>0 of the truncated cusps (or the areas of $\partial H_i$, that are $V_i/(n-1)$ by Proposition \ref{truncated:volume:prop}).

\begin{prop}
If we multiply all volumes $V_1,\ldots, V_c$ by the same constant $\lambda>0$ we get the same canonical tessellation.
\end{prop}
\begin{proof}
The set $B_j^i$ changes by a global rescaling, and hence also the tessellation does. Its projection on $I^n$ is unaffected.
\end{proof}

A way to get a truly canonical decomposition of $M$, which depends on no choice, consists of taking $V_1=\ldots = V_c>0$. Note that when $c=1$ any choice leads to the same canonical decomposition.
