---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-020-35-geodesic-boundary-non-complete-and-cone-manif
section_title: "Geodesic boundary, non-complete, and cone manifolds"
section_number: 3.5
pages: 105-109
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.84
latex_coverage_ratio: 0.939
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We now introduce three important variations on the complete hyperbolic manifolds theme.
The first consists of admitting a totally geodesic boundary, the second is a brief overlook of some phenomena that may occur when the completeness hypothesis is dropped, and in the third we allow some conical singularity on a codimension-two geodesic stratum.


\subsection{Hyperbolic manifolds with geodesic boundary}
We reformulate a definition of hyperbolic (elliptic, flat) manifolds that allows the presence of some geodesic boundary. These manifolds are useful because they can be glued along their boundaries to produce new hyperbolic (elliptic, flat) manifolds.
\index{hyperbolic manifold!with geodesic boundary}
\index{flat manifold!with geodesic boundary}
\index{elliptic manifold!with geodesic boundary}
\begin{defn} A \emph{hyperbolic} (\emph{elliptic, flat}) \emph{manifold} $M$ \emph{with geodesic boundary}
is a Riemannian manifold with boundary where every point has an open neighbourhood isometric to an open set in a half-space in $\matH^n$ ($S^n$, $\matR^n$).
\end{defn}

The boundary $\partial M$ of a hyperbolic (elliptic, flat) $n$-manifold with geodesic boundary is a hyperbolic (elliptic, flat) $(n-1)$-manifold without boundary. Theorem \ref{simply:teo} extends appropriately to this context.

\begin{teo}
Every complete simply connected hyperbolic $n$-manifold $M$ with geodesic boundary is isometric to the intersection of some half-spaces in $\matH^n$ with disjoint boundaries.
\end{teo}
\begin{proof}
We construct a developing map $D\colon M\to\matH^n$ as in Theorem \ref{simply:teo}. The map $D$ is injective, because every two points $p,q \in M$ are connected by a geodesic (exercise: use completeness and geodesic boundary), which is sent to a geodesic via $D$, so $p,q$ are sent to distinct points $D(p), D(q)$. 

Therefore $D(M)\subset \matH^n$ is isometric to $M$. Since it is complete and with geodesic boundary, its boundary consists of disjoint hyperplanes, and hence $D(M)$ is the intersection of half-spaces bounded by them.  
\end{proof}

An example is sketched in Figure \ref{universale:fig}. Every complete hyperbolic manifold with geodesic boundary can be enlarged to a hyperbolic manifold without boundary in a canonical way.

\begin{figure}
\begin{center}
\includegraphics[width = 4cm] {\iftoggle{BW}{universale-BW}{universale}}
\nota{An intersection of (possibly infinitely many!) half-planes. The universal cover of a hyperbolic surface with boundary is isometric to such an object.}
\label{universale:fig}
\end{center}
\end{figure}


\begin{cor} Every complete hyperbolic $n$-manifold $M$ with geodesic boundary is contained in a complete hyperbolic $n$-manifold $N$ without boundary, such that $N\setminus \interior M$ is diffeomorphic to $\partial M \times [0,+\infty)$.
\end{cor}
\begin{proof}
The proof of Proposition \ref{corto:prop} applies and shows that $M = \tilde M/_\Gamma$ where $\tilde M\subset \tilde \matH^n$ is an intersection of half-spaces and $\Gamma< \Iso(\tilde M)$ acts freely and properly discontinuously on $\tilde M$.

Every local isometry in $\matH^n$ extends to a global isometry, therefore $\Gamma < \Iso(\tilde M) < \Iso(\matH^n)$. The group $\Gamma$ acts freely on $\tilde M$ and hence also on $\matH^n$: if it had a fixed point $x\in \matH^n$, it would fix also the unique point $y \in \tilde M$ that is the closest to $x$.
The manifold $N=\matH^n/_\Gamma$ contains naturally $M$.

For every $p \in \partial M$, let $\gamma_p(t)$ be the unit speed geodesic starting at $p$ orthogonal to $\partial M$ and directed outward. By looking at the universal cover one sees easily that the map $\partial M \times [0,+\infty) \to N \setminus \interior M$, $(p,t)\mapsto \gamma_p(t)$ is a diffeomorphism (we use here that $\tilde M\subset \matH^n$ is convex).
\end{proof}


\subsection{Cut and paste}
Hyperbolic manifolds with geodesic boundary are useful because they can be glued to produce new hyperbolic manifolds.

Let $M$ and $N$ be hyperbolic manifolds with geodesic boundary and $\psi\colon \partial M \to \partial N$ be an isometry. Let $M\cup_\psi N$ be the topological space obtained by quotienting the disjoint union $M\sqcup N$ by the equivalence relation that identifies $p$ to $\psi(p)$ for all $p\in \partial M$.

\begin{prop} \label{geodesic:glue:prop}
The space $M\cup_\psi N$ has a natural structure of hyperbolic manifold.
\end{prop}
\begin{proof}
The interiors of $M$ and $N$ inherit their hyperbolic metrics. When we glue $p$ to $\psi(p)$ we get a point $q$ that has two half-disc neighbourhoods on its sides, which glue to a honest hyperbolic disc, inducing a hyperbolic metric near $q$.
\end{proof}

Conversely, if an orientable hyperbolic manifold $M$ contains an orientable geodesic hypersurface $N$, we can cut $M$ along $N$ to get a hyperbolic manifold with geodesic boundary. The boundary will consist of two copies of $N$.


\subsection{Non-complete hyperbolic manifolds} \label{non-complete:subsection}
There is no classification of simply connected non-complete hyperbolic manifolds: for instance, we may get plenty of uninteresting examples by removing complicated closed sets from $\matH^n$. However, the first part of the proof of Theorem \ref{simply:teo} still applies and provides the following:

\begin{prop}
Let $M$ be a non-complete simply connected hyperbolic $n$-manifold. There is a local isometry
$$D\colon M \to \matH^n$$
which is unique up to post-composing with $\Iso(\matH^n)$.
\end{prop}
\begin{proof}
Construct $D$ as in the proof of Theorem \ref{simply:teo}: the completeness of $M$ is used there only in the last paragraph to show that $D$ is a covering.
As a local isometry, the map $D$ is determined by its first-order behaviour at any point $p\in M$, and is hence unique up to post-composing with an isometry of $\matH^n$.
\end{proof}

The map $D$ is called a \emph{developing map} and is neither injective nor surjective in general. We can push-forward isometries along $D$ as follows. \index{developing map}

\begin{prop}
Let $M$ be a hyperbolic $n$-manifold and $D\colon M \to \matH^n$ be a local isometry. For every $g\in \Iso(M)$ there is a unique $\rho(g)\in \Iso(\matH^n)$ such that
$$\rho(g) \circ D = D\circ g.$$
The resulting map $\rho \colon \Iso(M) \to \Iso(\matH^n)$ is a homomorphism.
\end{prop}
\begin{proof}
Pick a point $p\in M$ and define $\rho(g)$ as the unique isometry of $\matH^n$ such that $\rho(g) \circ D = D\circ g$ on a small neighbourhood of $p$. This equality between local isometries holds locally and hence globally on $M$. The map $\rho$ is easily checked to be a homomorphism.
\end{proof}

The homomorphism $\rho$ is the \emph{holonomy} associated to $D$. If $M$ is a non-complete hyperbolic $n$-manifold, its universal covering $\pi\colon \tilde M \to M$ inherits a non-complete hyperbolic metric. Therefore we get a developing map 
$$D\colon \tilde M \to \matH^n$$ 
together with a holonomy \index{holonomy}
$$\rho \colon \Aut(\pi) \longrightarrow \Iso(\matH^n)$$
which is the restriction of $\rho$ to the subgroup $\Aut(\pi)<\Iso(\tilde M)$. By fixing a point in $\tilde M$ we identify $\Aut(\pi)$ with $\pi_1(M)$ and get a holonomy
$$\rho\colon \pi_1(M) \longrightarrow \Iso(\matH^n).$$

As every metric space, a non-complete Riemannian manifold $M$ has a unique \emph{completion} $\overline M$, a complete metric space that contains $M$ as an open dense set. The completion $\overline M$ is however not necessarily a manifold, except in some lucky cases. These lucky cases are extremely important in dimension three, as we will see in Chapter \ref{three:chapter}. In that chapter we will understand the completion $\overline M$ of a hyperbolic three-manifold by studying its developing map and holonomy.


\subsection{Singularities} \label{singularities:subsection}
A particular class of non-complete hyperbolic manifolds deserves our attention, because their completions are some nice and natural objects: manifolds with \emph{cone angles} along some codimension-two singular geodesic stratum.

Let $S\subset \matH^n$ be a codimension-two subspace. The incomplete hyperbolic manifold $\matH^n \setminus S$ has fundamental group $\matZ$ and we denote by
$$\pi \colon X \longrightarrow \matH^n \setminus S$$
its universal covering: here $X$ is an interesting non-complete simply connected hyperbolic manifold. Note that $\pi$ may be interpreted as a developing map $\pi\colon X\to \matH^n$ which is neither injective nor surjective.

\begin{ex}
The metric completion of $X$ is $\overline X = X \sqcup \tilde S$ where $\tilde S$ is an identical copy of $S$. The covering $\pi$ extends to a surjective map
$$\pi\colon \overline X \to \matH^n$$
that sends $\tilde S$ to $S$. If $p\in \tilde S$ and $q\in \overline X$ then $d(p,q) = d(\pi(p), \pi(q)).$
\end{ex}

The space $\tilde S$ is the \emph{singularity} of $\overline X$ and should be interpreted as lying in $\overline X$ with infinite cone angle: the space $\overline X$ looks like a book with infinitely many pages (it is not locally compact at $\tilde S$). Singularities with finite cone angles will be defined in the next section as quotients of this model. The dimensions that will be interesting for us are of course $n=2$ and $3$, where $\tilde S$ is a point and a line, respectively.


\subsection{Cone manifolds}
For every $\theta\in \matR$ there is a well-defined rotation $\Rot_\theta\colon \overline X \to \overline X$ of angle $\theta$ around $\tilde S$, which projects to a rotation in $\matH^n$ of angle $\theta$ around $S$; note that $\Rot_\theta \neq \id$ for all $\theta \neq 0$, including $\theta = 2k\pi$.

We fix $\theta \neq 0$, so that $\Rot_\theta$ generates a free cyclic group $\Gamma < \Iso(\overline X)$.

\begin{ex}
The metric space $\overline X/_\Gamma$ is the completion of $X/_\Gamma$ and is homeomorphic to $\matR^n$.
\end{ex}

The image of $\tilde S$ along the quotient $\pi\colon \overline X \to \overline X /_\Gamma$ is a copy of $\tilde S$ and should now be interpreted as a singularity with cone angle $\theta$. When $\theta = 2k\pi$ for some integer $k$ the map $\pi\colon \overline X \to \matH^n$ factors as
$$\overline X \overset {\pi_1} {\longrightarrow} \overline X/_\Gamma \overset {\pi_2} \longrightarrow \matH^n.$$
When $k=\pm 1$ the map $\pi_2$ is an isometry. We introduce the following definition.\index{hyperbolic manifold!with cone angles}

\begin{defn}
A \emph{hyperbolic manifold $M$ with cone angles} is a metric space with charts in some $\overline X/_\Gamma$ and transition maps that are isometries.
\end{defn}

The term ``isometries'' should be interpreted in the strongest sense: the transition maps send singular points to singular points, and outside of the singular points these are isometries of Riemannian manifolds.

The points in $M$ that are mapped along charts to some singular set form a hyperbolic codimension-two submanifold in $M$ with some cone angle $\theta$, and different components may have different cone angles.
Points with cone angle $2\pi$ may be considered as ordinary points, while points with cone angle different from $2\pi$ are \emph{singular} and form the \emph{singular locus} of $M$.

The singular locus of $M$ is a geodesic codimension-two manifold, and its complement is an ordinary hyperbolic manifold, whose metric completion is $M$.
Flat and spherical manifolds with cone angles are defined in the same way. \index{elliptic manifold!with cone angles} \index{flat manifold!with cone angles}


\subsection{Examples}
The following simple construction is already a source of many two-dimensional examples: let $P$ be any polygon in $\matH^2, \matR^2,$ or $S^2$, with some inner angles $\alpha_1,\ldots, \alpha_k$. By doubling $P$ along its edges we get a topological sphere with $k$ cone points of angles $2\alpha_1, \ldots, 2\alpha_k < 2\pi$. This is a hyperbolic, flat, or spherical surface with cone angles.

Another simple but maybe more intriguing construction is the following: pick any polyhedron $P$ in $\matH^3, \matR^3$, or $\matS^3$. The faces of $P$ are (hyperbolic, flat, or elliptic) polygons that glue isometrically along the edges: hence $\partial P$ is a topological sphere with a natural structure of (hyperbolic, flat, or elliptic) manifold with cone angles at the vertices.

To construct examples in dimension three we need a bit more work because polyhedra have more strata. Non-compact examples are easier to build: let $P\subset \matH^3$ be any ideal hyperbolic polyhedron, with some $k$ edges with dihedral angles $\alpha_1,\ldots, \alpha_k$; the double of $P$ is naturally a hyperbolic cone manifold where the edges form the singular locus with cone angles $2\alpha_1, \ldots, 2\alpha_k$.
