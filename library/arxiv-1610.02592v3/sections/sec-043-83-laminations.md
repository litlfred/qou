---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-043-83-laminations
section_title: "Laminations"
section_number: 8.3
pages: 247-266
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.998
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
In this section we characterize geometrically the currents $\alpha\in\calC$ contained in the ``light cone,'' \emph{i.e.}~those with $i(\alpha,\alpha)=0$. Every such current may be represented as a \emph{measured geodesic lamination}, a closed subset of $S_g$ foliated by geodesics and equipped with a transverse measure. These unexpected objects play an important part in the topology of manifolds of dimension two and three.


\subsection{Geodesic laminations.}
Let $S = \matH^2/_\Gamma$ be a hyperbolic surface. Recall that in this chapter we consider geodesics only as subsets of $S$, neglecting their parametrisation. 

A \emph{geodesic lamination} $\lambda$ is a set of disjoint simple complete geodesics in $S$, whose union is a closed subset of $S$. Each geodesic may be closed or open and is called a \emph{leaf}; their union is the \emph{support} of $\lambda$. We will often confuse $\lambda$ with its support for simplicity, since the support determines the set of geodesics in all the interesting cases (see below).\index{geodesic lamination}

The following examples of geodesic laminations are fundamental:
\begin{itemize}
\item a geodesic multicurve (that is a finite set of disjoint simple closed geodesics) in $S$;
\item a set of disjoint lines in $\matH^2$ whose union is closed. 
\end{itemize}

A lamination in $\matH^2$ may be particularly complicated, see Figure \ref{lamination:fig}. Recall that $\calG = \calG(\matH^2)$ is the set of all lines in $\matH^2$, with its natural topology.

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{600px-lamination}{600px-lamination}}
\nota{A geodesic lamination in $\matH^2$.}
\label{lamination:fig}
\end{center}
\end{figure}

\begin{ex} 
A set $\lambda$ of disjoint lines in $\matH^2$ forms a closed set in $\matH^2$ if and only if $\lambda$ is closed when considered as a subset of $\calG$.
\end{ex}
If a set of disjoint lines in $\matH^2$ is not closed, it suffices to take its closure to get a lamination. Every lamination in $S=\matH^2/_\Gamma$ lifts to a $\Gamma$-invariant lamination  in $\matH^2$, hence the laminations in $S$ are in natural bijection with the $\Gamma$-invariant laminations in $\matH^2$. 


\subsection{Local behaviour}
A geodesic lamination is often too complicated to be determined with full precision. In fact, its topology is already quite involved, and we now start by examining it locally. Let $\lambda$ be a geodesic lamination on a hyperbolic surface $S=\matH^2/_\Gamma$. The following exercise may be proved by passing to the universal cover $\matH^2$.

\begin{ex} 
Every point $p\in \lambda$ has an open neighbourhood $U$ and a chart $U \to (-1,1) \times (-1,1)$ that sends $p$ to $(0,0)$ and $\lambda \cap U$ to $(-1,1) \times J$ for some closed subset $J\subset (0,1)$.
\end{ex}

What kind of $J\subset (0,1)$ may arise?
It is possible to construct some laminations in $\matH^2$ or in some simple hyperbolic surfaces like cusps and tubes, where their support is the whole manifold. In this case $J$ is the full interval $(0,1)$. These cases are however of no interest for us, because of the following.

\begin{prop} \label{empty:J:prop}
If $S$ has finite volume, then $J$ has empty interior.
\end{prop}
\begin{proof}
Suppose by contradiction that $J$ contains some open interval. This open interval determines a set of leaves of $\lambda$, whose lift in $\matH^2$ forms an open subset $U\subset \matH^2$ foliated into lines. Its limit in $\partial \matH^2$ has non-empty interior $S$. By Corollary \ref{parabolic:hyperbolic:dense:cor} there is a hyperbolic transformation $\gamma \in \Gamma$ with an attracting limit point in $S$. This implies easily that there are $\gamma$-translates of some lines in $U$ that intersect some lines of $U$ transversely, a contradiction. 
\end{proof}

\begin{cor}
If $S$ has finite volume, every geodesic lamination $\lambda$ in $S$ has empty interior and is determined by its support.
\end{cor}


\subsection{Complementary regions}
Let $\lambda \subset S$ be a geodesic lamination in a hyperbolic surface $S=\matH^2/_\Gamma$.
A \emph{complementary region} (shortly, a \emph{region}) is a connected component of the open complement $S\setminus \lambda$. The abstract completion of a complementary region is a hyperbolic surface with non-empty geodesic boundary consisting of lines and/or circles. 

In general, a complementary region may have genus and/or infinitely many boundary components. Note that in any case there are at most countably many regions, and hence only countably many leaves of $\lambda$ may be incident to a region: if $\lambda$ has uncountably many leaves (this will be the typical case), most leaves are not incident to any region (compare this with the Cantor subset in $[0,1]$, which contains uncountably many points, but only countably many of them are adjacent to some complementary open segment).

\begin{prop} \label{finite:regions:prop}
A geodesic lamination $\lambda\subset S_g$ in a closed hyperbolic surface $S_g=\matH^2/_\Gamma$ has at most $4g-4$ complementary regions. The boundary of each region has finitely many components.
\end{prop}
\begin{proof}
Every complementary region has area at least $\pi$ (the area of an ideal triangle) and a region with infinitely many boundary components has infinite area. By Gauss-Bonnet we get $\Area(S_g) = -2\pi\chi(S_g) = (4g-4)\pi$.
\end{proof}

We say that a lamination $\lambda \subset S_g$ is \emph{full} if every region is an ideal polygon.\index{geodesic lamination!full}












\subsection{Transverse measures}
Let $\lambda\subset S$ be a geodesic lamination in a hyperbolic surface $S$. A \emph{transverse arc} to $\lambda$ is the support of a simple regular curve $\alpha\colon [a,b] \to S$ transverse to each leaf of $\lambda$, whose endpoints $\alpha(a)$ and $\alpha(b)$ are not contained in $\lambda$.\index{geodesic lamination!measured geodesic lamination} 

\begin{defn} \label{measure:axioms:defn}
A \emph{transverse measure} for a lamination $\lambda\subset S$ is a locally finite Borel measure $L_\alpha$ on each transverse arc $\alpha$ such that:
\begin{enumerate}
\item if $\alpha' \subset \alpha$ is a sub-arc of $\alpha$, the measure $L_{\alpha'}$ is the restriction of $L_\alpha$;
\item the support of $L_\alpha$ is $\alpha\cap \lambda$;
\item the measure is invariant through isotopies of transverse arcs.
\end{enumerate}
\end{defn}
In particular every arc $\alpha$ transverse to $\lambda$ has a finite \emph{length}, defined as the total measure of the arc. The arc has length zero if and only if $\alpha\cap\lambda = \emptyset$. A \emph{measured geodesic lamination} is a geodesic lamination equipped with a transverse measure.

\begin{example} \label{weight:example}
A geodesic multicurve $\lambda \subset S$ has a natural transverse measure: for any transverse arc $\alpha$, the measure $L_\alpha$ on $\alpha$ is just the Dirac measure supported on the finite set $\alpha\cap\lambda$.

More generally, we may assign a positive weight $a_i>0$ at each component $\lambda_i$ of $\lambda$ and define a measured geodesic lamination by giving the weight $a_i$ at each intersection $\alpha \cap \gamma_i$. By varying weights we get distinct measured geodesic laminations with the same support.
\end{example}


\subsection{Currents and measured geodesic laminations}
Let $S_g=\matH^2/_\Gamma$ be a closed hyperbolic surface. We now construct a natural bijection between the measured geodesic laminations on $S_g$ and the geodesic currents $\lambda$ with $i(\lambda,\lambda)=0$, \emph{i.e.}~those lying in the ``light cone.'' We see a measured geodesic lamination in $S_g$ as a $\Gamma$-invariant measured geodesic lamination in $\matH^2$.

Let $\lambda \in \calC$ be a geodesic current with $i(\lambda,\lambda)=0$. By Remark \ref{correnti:oss} the support of $\lambda$ is a closed $\Gamma$-invariant subset of $\calG$ formed by disjoint lines, hence a $\Gamma$-invariant lamination in $\matH^2$. The geodesic current induces also a transverse measure as follows. Let $\alpha$ be an arc transverse to the lamination $\lambda$. Up to cutting $\alpha$ in finitely many arcs we may suppose that it intersects each leaf of $\lambda$ in at most one point. We define the measure of a Borel set $U\subset \alpha$ as the $\lambda$-measure in $\calG$ of the lines in $\lambda$ that it intersects.
\begin{ex}
This transverse measure satisfies the axioms of Definition \ref{measure:axioms:defn} and gives $\lambda$ the structure of a $\Gamma$-invariant measured geodesic lamination.
\end{ex}
\begin{prop}
We have just defined a bijection
$$\big\{ {\rm currents\ } \lambda {\rm \ with\ } i(\lambda,\lambda)=0 \big\}
\longleftrightarrow 
\big\{ {\rm measured\ geodesic\ laminations\ in\ } S_g\big\}
$$
\end{prop}
\begin{proof}
We define the inverse map by transforming a $\Gamma$-invariant measured geodesic lamination $\lambda$ into a geodesic current with support $\lambda \subset \calG$ as follows. For every leaf $l$ of $\lambda$, we pick a small transverse arc $\alpha$ that intersects all the leaves in a neighbourhood $U_l$ of $l$ in $\lambda$, each once. The measure on $\alpha$ translates into a measure on $U_l$, and all the measures on these small sets $U_l$ match to yield a measure on $\lambda$ thanks to Proposition  \ref{ricoprimento2:prop}. 
\end{proof}

We denote by $\calM\calL\subset \calC$ the set of all the measured geodesic laminations on $S_g$, henceforth identified with the currents lying in the ``light cone''. With this identification $\calML$ is independent on the auxiliary hyperbolic metric on $S_g$.\index{$\calML$}

Recall that a multicurve on $S_g$ is a finite collection of disjoint non-trivial simple closed curves. A multicurve determines a measured geodesic lamination: consider $n$ parallel components as a single one with weight $n$, take the geodesic representative of the resulting essential multicurve (keeping the same weights), and use Example \ref{weight:example}. We obtain the inclusions
$$\calS \subset \calM \subset \ML \subset \calC$$ 
where $\calS$ and $\calM$ are the sets of simple closed curves and multicurves in $S_g$.\index{$\calM$} 


\subsection{Some properties}
We can now use our knowledge of the geodesic currents to get some information about the measured geodesic laminations. 

\begin{prop} \label{at:most:two:prop}
Let $\lambda\subset S_g$ be a measured geodesic lamination. For every $p\in\partial \matH^2$, there are at most two lines in the preimage $\tilde\lambda\subset\matH^2$ incident to $p$, and if there are two, none of them projects to a closed geodesic in $\lambda$. 
\end{prop}
\begin{proof}
If there are at least three lines $l_1, l_2, l_3$ incident to $p$, with $l_2$ lying strictly between $l_1$ and $l_3$, we may find a small arc $\alpha$ transverse to $\tilde \lambda$, whose support lies between $l_1$ and $l_3$, that intersects $l_2$ and possibly other lines incident to $p$, and no other line of $\tilde \lambda$ (use Proposition \ref{empty:J:prop} near $l_2$ here). The lines intersected by $\alpha$ form a pencil with positive mass. By Proposition \ref{pencils:prop} the pencil consists of a single line, the axis of a hyperbolic element $\varphi\in \Gamma$.

On the other hand, if $p$ is the endpoint of the axis of some $\varphi$, then no other leaf $l\subset \tilde\lambda$ can be incident to $p$, otherwise infinitely many lines $\varphi^i(l)$ would also be, and the same argument above would give a contradiction.
\end{proof}

\begin{ex}
There are some geodesic laminations in $S_g$ that do not support any transverse measure.
\end{ex}
\begin{proof}[Hint]
Construct a geodesic lamination $\lambda \subset S_g$ consisting of some disjoint simple closed curves and finitely many open leaves that wind around them (see Section \ref{incomplete:metrics:subsection}). The pre-image $\tilde\lambda\subset\matH^2$ contradicts Proposition \ref{at:most:two:prop}.
\end{proof}









\subsection{Intersection form}
What is the geometric meaning of the intersection form $i$ of two geodesic currents, when applied to a measured geodesic lamination? Let $\lambda$ be a measured geodesic lamination in a hyperbolic closed surface $S_g=\matH^2/_\Gamma$. Three cases are relevant for us:

\begin{enumerate}
\item If $\gamma$ is a simple closed geodesic, then either $\gamma$ is contained in $\lambda$, and we get $i(\gamma, \lambda)=0$, or $\gamma$ is disjoint from $\lambda$, and we still get $i(\gamma,\lambda)=0$, or $\gamma$ is transverse to $\lambda$, and in that case $i(\lambda, \gamma)$ equals the full measure $L(\gamma)$ of $\gamma$ as a transverse curve to $\lambda$.
\item If $\lambda'$ is another measured geodesic lamination, then $i(\lambda, \lambda')$ ``counts'' the (possibly infinitely many) transverse intersections of $\lambda$ and $\lambda'$ with respect to the product of the two transverse measures.
\item If $m$ is a hyperbolic metric, then $i(\lambda, m)$ measures the ``length'' of $\lambda$ with respect to $m$, that is the integral over $\lambda$ of the usual length weighted with the transverse measure.
\end{enumerate}

We now consider a non-geodesic non-trivial simple closed curve $\gamma$ transverse to $\lambda$, and we denote by $L(\gamma)$ its full transverse $\lambda$-measure. The quantities $L(\gamma)$ and $i(\gamma, \lambda)$ need \emph{not} to be equal in this case (because $\gamma$ is not geodesic), but this phenomenon is easily controlled by a suitable version of the bigon criterion.

\begin{prop} \label{m:i:prop}
We have $L(\gamma) \geqslant i(\gamma, \lambda)$ and the equality holds $\Longleftrightarrow$ $\gamma$ forms no bigon with any leaf of $\lambda$.
\end{prop}
\begin{proof}
We follow the proof of Theorem \ref{bigono:teo}. Let $\tilde \lambda$ be the counterimage of $\lambda$ in $\matH^2$. A lift $\tilde\gamma$ of $\gamma$ has distinct endpoints in $\partial \matH^2$ and $\tilde \gamma$ must intersect the leaves of $\tilde\lambda$ whose endpoints are linked with them. The curve $\tilde \gamma$ intersects each such leaf only once and no other leaf $\Leftrightarrow$ $\tilde \gamma$ forms no bigon with any leaf of $\tilde \lambda$ $\Leftrightarrow$ $\gamma$ forms no bigon with any leaf of $\lambda$.
\end{proof}

\begin{prop} \label{sublamination:prop}
If $\lambda \in \calML$ is full, we have $i(\lambda, \alpha)>0$ for every current $\alpha$ that is not a measured sublamination of $\lambda$.
\end{prop}
\begin{proof}
If $i(\lambda, \alpha)=0$ then every line $l$ in the support of $\alpha$ is either a leaf of $\lambda$ or an infinite diagonal in some complementary ideal polygon; a diagonal would be an atomic point in $\alpha$ that would cover a closed geodesic and could be added to $\lambda$ contradicting 
Proposition \ref{at:most:two:prop}.
\end{proof}


\subsection{Train tracks}
How can one construct a measured geodesic lamination, concretely? There are some nice combinatorial tools designed to this purpose, called train tracks.\index{train track} 

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{switch-BW}{switch}}
\nota{A switch contains $a\geqslant 1$ and $b\geqslant 1$ branches on each side: here $a=3$ and $b=2$ (1). The complementary regions of a train track contain no discs, annuli, monogons, or bigons (2).}
\label{switch:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{Triple-torus-train-track-BW}{Triple-torus-train-track}}
\nota{A train track on the genus-three surface $S_3$. }
\label{train_track:fig}
\end{center}
\end{figure}

A \emph{train track} in a closed surface $S_g$ is a closed subset $\tau\subset S_g$ built by taking a finite set of points (called \emph{vertices} or \emph{switches}) and joining them with disjoint arcs called \emph{branches}. We require that every switch looks locally like Figure \ref{switch:fig}-(1): all branches have the same tangent line, and there is at least one branch at each side. 

The \emph{complementary regions} of $\tau$ are the abstract closures of the connected components of $S_g\setminus \tau$. Each complementary region is naturally a compact surface with finitely many singular vertices in its boundary having ``zero interior angle''. In the definition of a train track, we also require that no complementary region be a disc, an annulus, a monogon, or a bigon, as in Figure \ref{switch:fig}. An example is shown in Figure \ref{train_track:fig}. The exclusion of these complementary regions is essential to get the following.

\begin{ex}
A train track contains at most $-6\chi(S_g)$ switches and at most $-2\chi(S_g)$ regions; it contains $-6\chi(S_g)$ switches if and only if every switch is trivalent and every complementary region is a triangle. The sphere and the torus contain no train track. 
\end{ex}
\begin{proof}[Hint] Make the appropriate Euler characteristic computation.
\end{proof}

\begin{ex}
Construct a train track with $-2\chi(S_g)$ triangular complementary regions in $S_g$ for every $g\geqslant 2$. 
\end{ex}
\begin{proof}[Hint] Take a pants decomposition and add three arcs (tangent to the boundary) inside each pants to decompose it into two triangular regions.
\end{proof}

We obtain a finiteness property.

\begin{cor}
There are only finitely many train tracks $\tau$ in $S_g$ up to diffeomorphism (but not up to isotopy!).
\end{cor}
\begin{proof}
There are only finitely many combinatorial types for $\tau$, its complementary regions, and the way they are adjacent.
\end{proof}



\subsection{Weight systems}

A \emph{weight system} on a train track $\tau\subset S_g$ is the assignment of a non-negative real number, called \emph{weight}, to each branch of $\tau$, such that at every vertex the \emph{switch condition} holds: the sum of the weights on the left branches should be equal to the sum of the weights on the right branches. 

Let $w$ be an \emph{integral} weight system, that is one whose weights are all integers. The integral weight system $w$ determines a closed 1-manifold in $S_g$ as follows: replace every branch with weight $a$ with $a$ parallel copies of it, and pair all the branches at every switch in the obvious way (this is possible thanks to the switch condition).

\begin{prop}
The resulting closed 1-manifold is a multicurve.
\end{prop}
\begin{proof}
Since no complementary region of $\tau$ is a disc or monogon, the complementary regions of the closed 1-manifold have non-positive Euler characteristic (exercise).
\end{proof}

Our aim now is to use the train tracks to parametrise all the multicurves in $S_g$. Later on, we will extend everything from multicurves to measured geodesic laminations.


\subsection{A parametrisation for $\calM$} \label{parametrisation:M:subsection}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{pantaloni_anelli_ex-BW}{pantaloni_anelli_ex}}
\nota{Decompose $S$ into pairs of pants and annuli, so that each simple closed curve separates a pair of pants from an annulus. We mark a \iftoggle{BW}{}{blue }point in each curve.}
\label{pantaloni_anelli_ex:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{pantaloni_anelli_new2-BW}{pantaloni_anelli_new2}}
\nota{Identify each pair of pants and annulus with one of these two fixed models.}
\label{pantaloni_anelli:fig}
\end{center}
\end{figure}

Let $S_g$ have genus $g\geqslant 2$. We now construct finitely many train tracks that parametrise all the multicurves in $S_g$, and to this purpose we fix a frame similar to the one used in the Fenchel-Nielsen parametrisation of the Teichm\"uller space. 

We decompose $S_g$ into pairs of pants and annuli as in Figure \ref{pantaloni_anelli_ex:fig}. We mark \iftoggle{BW}{}{(in blue) }an arbitrary point in each closed curve and we also fix once for all a diffeomorphism (preserving orientation and marked points) between each pair of pants and annulus with the corresponding model in Figure \ref{pantaloni_anelli:fig}. The resulting parametrisation of $\calM$ will depend also on these fixed diffeomorphisms.

Let a \emph{colouring} be the assignment of a triple $a_i,b_i,c_i$ of non-negative numbers to each annulus of the decomposition, such that one of the following equalities holds:
$$a_i = b_i+c_i, \quad b_i = c_i+a_i, \quad c_i = a_i +b_i.$$
We assign the colour $a_i$ to each of the two curves that bound the annulus.
Since there are $-\frac 32\chi(S_g) = 3g-3$ annuli, we get $-\frac 92\chi(S_g) = 9g-9$ colours overall. The colouring is \emph{integral} if the colours are integers and also the following holds: 
for each pair of pants, the sum $a_i+a_j+a_k$ of the colours of its boundary curves must be even.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{pants_train_tracks-BW}{pants_train_tracks}}
\nota{The portion of weighted train track in a pair of pants $P$ is determined by the point $Q=[a_i,a_j,a_k]\in\matRP^2$. Having non-negative entries, the point $Q$ is contained in the triangle with vertices $[1,0,0], [0,1,0], [0,0,1]$. This triangle subdivides into four sub-triangles by adding the vertices $[0,1,1]$, $[1,0,1]$, $[1,1,0]$ and the shape of the train track depends on which sub-triangle contains $Q$. The three edges of the train track are given the weights indicated in the figure: these are the only weights that sum to $a_i, a_j, a_k$ at the boundaries. When $Q$ lies in the frontier of two or more triangles some branch has weight zero and we delete it: the different shapes prescribed by the adjacent triangles coincide after deleting this branch.}
\label{pants_train_tracks:fig}
\end{center}
\end{figure}

We now transform each colouring into a weighted train track $\tau$ as follows. The boundary components of each pair-of-pants $P$ are coloured by some triple $a_i, a_j, a_k$. We insert in $P$ a portion of train track as in Figure \ref{pants_train_tracks:fig}: its shape depends on the position of the point $[a_i,a_j,a_k]$ in $\matRP^2$ and its weights depend linearly on $a_i, a_j, a_k$. Note that there are finitely many possible shapes overall.

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{anelli_train_tracks-BW}{anelli_train_tracks}}
\nota{The portion of weighted train track in each annulus $A$ is determined by the point $Q=[a,b,c] = [a_i,b_i,c_i]\in \matRP^2$. By hypothesis $Q$ is contained in the boundary of the triangle with vertices $[1,0,0], [0,1,0], [0,0,1]$. The boundary subdivides into three segments and the shape of the train track depends on which segment contains $Q$. When $Q$ is a vertex some branch has weight zero and we delete it.}
\label{anelli_train_tracks:fig}
\end{center}
\end{figure}

We extend the train track inside each annulus $A$ coloured with $a_i, b_i, c_i$ as shown in Figure \ref{anelli_train_tracks:fig}. Again, the shape of the portion depends on the position of $[a_i,b_i,c_i]$ in $\matRP^2$. As a result we get a train track $\tau$ with integral weights and hence a multicurve.

\begin{prop} \label{parametrize:multicurves:prop}
The construction produces a bijection
$$\big\{ {\rm integral\ colourings}\big\} \longleftrightarrow \calM.$$
\end{prop}
\begin{proof}
We start by proving surjectivity. Given a multicurve $\mu\in \calM$, we minimise its intersections with our decomposition into pants and annuli: now $\mu$ intersects every pair of pants $P$ into non-trivial simple closed curves and arcs (an arc is trivial if it forms a bigon with $\partial P$). 

By decomposing $P$ into two hexagons, and minimising the intersections of the curves and arcs with them, one deduces easily that $P$ contains only three isotopy classes of non-trivial closed curves (one parallel to each component of $\partial P$) and six isotopy classes of non-trivial arcs (one connecting every pair of components of $\partial P$). Note that isotopies are \emph{not} required to fix $\partial P$ pointwise.

We isotope all the closed curves away from $P$ and place them inside the adjacent annuli, so there are only arcs. As above, we check easily that the isotopy class of the whole set of arcs in $P$ is determined by the intersection numbers $a_i, a_j, a_k$ with the components of $\partial P$ and is hence represented by the corresponding train track portion from Figure \ref{pants_train_tracks:fig}. 

We now turn to annuli. On each annulus $A$, there is only one isotopy class of non-trivial arcs and one isotopy class of non-trivial closed curves. However, an arc may wind many times around $A$ and we are not allowed to use isotopies that move $\partial A$ anymore because the configuration in $P$ is already fixed: one deduces easily that the triples $(a,b,c)$ from Figure \ref{anelli_train_tracks:fig} describe precisely all the possible configurations. 

The injectivity is surprisingly simple to prove: the configuration of $\mu$ that minimises its intersections with the decomposition into pairs of pants and annuli is unique thanks to Proposition \ref{minimale:unica:prop} and hence the numbers $a_i,b_i,c_i$ are easily determined by $\mu$. The proof is complete.
\end{proof}

We have found a complete combinatorial parametrisation for the set $\calM$, and we now want to extend it to $\calML$.


\subsection{Topological laminations} \label{topological:laminations:subsection}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{switch_weights-BW}{switch_weights}}
\nota{How to construct a lamination from a weighted train track. Here we have a switch with weights $a$, $b$, $c$ (1) and the switch condition $a=b+c$ allows all the Euclidean rectangles (2) to glue (3).}
\label{switch_weights:fig}
\end{center}
\end{figure}

A train track $\tau$ in $S_g$ with integer weights parametrises a multicurve. We now show that, more generally, a weighted train track parametrises a measured geodesic lamination. 

The construction goes as follows. First, we remove all the branches with zero weight, and we replace every branch of weight $a>0$ with a Euclidean rectangle of width $a$ and with arbitrary length as in Figure \ref{switch_weights:fig}-(2). Thanks to the switch conditions, these rectangles glue nicely at each switch as in Figure \ref{switch_weights:fig}-(3).

In Figure \ref{switch_weights:fig}-(3) we see that all the lines from left- and right-rectangles are matched in a 1-1 correspondence, with a finite number of exceptions. At each exception, some $m \geqslant 1$ left-lines are matched to some $n \geqslant 1$ right-lines at some point, and we have $m+n=3$ or 4. We call these lines and points \emph{singular}. 

After gluing the rectangles we get a closed subset $\lambda$ of $S_g$ foliated by lines, with finitely many singular points and lines. We now eliminate the singular points and lines by cutting $\lambda$ carefully along them: if $m+n=4$ this amounts simply to doubling the singular point; if $m+n=3$ we double the singular leaf by opening a small open corridor in the foliation, starting from the singular point and digging along the leaf. Since the singular leaf may be non-compact, for the process to converge in $S_g$ we need to shrink the width of the corridor sufficiently fast. 

After this cut we get a closed subset of $S_g$, which we still name $\lambda$, nicely partitioned into disjoint lines that may be either open or closed: we call it a \emph{topological lamination}. After the cut every rectangle of type $L\times [0,a]$ as in Figure \ref{switch_weights:fig} transforms into a set $L \times J$ where $J$ is obtained by cutting $[0,a]$ along (at most) countably many points. Note that $J$ may be a Cantor set.\index{topological lamination}

The set $J$ inherits from $[0,a]$ a Borel measure with total mass $a$. This measure gives a transverse measure to the leaves of the rectangle $L\times J$, and $\lambda$ inherits the structure of a measured topological lamination (the notion of a transverse measure is exactly the same as in the geodesic case).

It only remains to promote the topological lamination to a geodesic lamination: this is usually done by \emph{straightening} its leaves. We describe this procedure only for a particular class of train tracks: the ones introduced in the previous section to parametrise $\calM$.


\subsection{A parametrisation for $\ML$} \label{parametrizzazione:subsection}
We now extend the arguments of Section \ref{parametrisation:M:subsection}
from multicurves to laminations.

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{foglia_new-BW}{foglia_new}}
\nota{The decomposition into pants and annuli of $S_g$ is homotopic to a geodesic pants decomposition (with each curve counted twice) whose counterimage in $\matH^2$ consists of infinitely many disjoint ultraparallel lines as in the picture.
We show that the lift of a leaf $l$ of $\lambda$ in $\matH^2$ has two distinct endpoints in $\partial \matH^2$: if $l$ is a closed curve in an annulus $A$, then it is isotopic to a closed geodesic and we are done; if $l$ intersects annuli and pairs of pants into non-trivial arcs, its lift intersects the ultraparallel lines forming no bigons, hence it intersects each line at most once: therefore it has disjoint limits at $\pm \infty$ (left). The straightening replaces the lift with the unique line with these endpoints (right).}
\label{foglia_new:fig}
\end{center}
\end{figure}


We fix a decomposition of $S_g$ into 
pants and annuli. Every colouring $(a_i,b_i,c_i)$ produces a weighted train track, which in turn parametrises a measured topological lamination $\lambda$. We fix a hyperbolic structure $S_g = \matH^2/_\Gamma$. 

The lamination $\lambda$ can be \emph{straightened} to a measured geodesic lamination $\bar\lambda$ as follows. A leaf $l$ of $\lambda$ is either a closed curve in some annulus $A$, or it intersects every annulus $A$ and pair of pants $P$ in non-trivial arcs: in both cases, every lift of $l$ in $\matH^2$ is a curve with two distinct limit endpoints in $\partial \matH^2$, see Figure \ref{foglia_new:fig}. We replace every lift of $l$ with the unique line having these endpoints, and we do this for every leaf $l$ of $\lambda$. 

The result is a $\Gamma$-invariant closed set of disjoint lines in $\matH^2$ that project to a geodesic lamination $\bar\lambda$ in $S_g$. The transverse measure on $\lambda$ easily induces one on the straightened $\bar\lambda$: it suffices to consider transverse arcs contained in the decomposition into pairs of pants and annuli. Note that some parallel closed leaves of $\lambda$ may have collapsed to a single atom closed geodesic in $\bar\lambda$.


\begin{prop} \label{parametrize:laminations:prop}
The construction induces a bijection
$$\big\{ {\rm colourings}\big\} \longleftrightarrow \calML.$$
\end{prop}
\begin{proof}
We adapt the proof of Proposition \ref{parametrize:multicurves:prop}, starting with surjectivity: given a measured geodesic lamination $\lambda$, we determine a colour $(a_i,b_i,c_i)$ representing it.

The decomposition into pairs of pants and annuli is homotopic to a geodesic pants decomposition $\mu=\gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$ (with each curve counted twice). We set $a_i = i(\gamma_i,\lambda)$.

The measured geodesic lamination $\lambda \in \calML$ decomposes as $\lambda = \lambda_0 \sqcup \lambda_1$ where $\lambda_0 = \sum_ik_i\gamma_i$ is a weighted pants decomposition with support in $\mu$ and $\lambda_1$ is transverse to $\mu$. If $k_i\neq 0$ then necessarily $a_i=0$ and we set $b_i=c_i=k_i$.

At every pair of pants $P$ the three colours $a_i,a_j,a_k$ determine a portion of weighted train track as prescribed by Figure \ref{pants_train_tracks:fig}. The intersection $\lambda_1\cap P$ consists of geodesic and hence non-trivial arcs: therefore the weighted train track describes faithfully this portion of measured geodesic lamination, up to isotopy. The numbers $b_i$ and $c_i$ are then determined by the way these two portions wind and match along $\gamma_i$. The colours $(a_i,b_i,c_i)$ parametrise $\lambda$.

The choices of the colours $(a_i,b_i,c_i)$ were forced by the intersection of $\lambda$ with the two pants $P$ adjacent to $\gamma_i$ (exercise). This shows injectivity.
\end{proof}

We have parametrised $\calML$, and we now investigate its topology. The space of all colourings $(a_i,b_i,c_i)$ forms the subset $C\times \ldots \times C \subset \matR^3 \times \ldots \times \matR^3$ where $C \subset \matR^3$ is the cone based on the origin over the sides of the triangle with vertices $(1,1,0)$, $(0,1,1)$, and $(1,0,1)$, and is homeomorphic to $\matR^2$. The space of colourings is homeomorphic to $\matR^{2\cdot (3g-3)} = \matR^{6g-6}$, that is to the Teichm\"uller space itself!

The parametrisation identifies $\calML$ with  $C\times \ldots \times C$. We want to show that this identification is a homeomorphism, and to this purpose we study the intersection form.


\subsection{Intersection form}
We now show that the intersection form $i$ between curves and laminations has a surprisingly simple behaviour after that we parametrise the space $\calML$ as $C\times \ldots \times C$. 

We note that $C\times \ldots \times C$ is a piecewise-linear object in $\matR^{9g-9}$, that is it is the support of a simplicial complex. Recall that a continuous map between simplicial complexes is \emph{simplicial} if it sends each simplex onto a simplex in an affine linear way, and it is \emph{piecewise linear} if it restricts to a simplicial map on some subdivisions. Finally, the map is \emph{half-integral piecewise linear} if all the affine linear maps have half-integer (possibly integer) coefficients.

\begin{prop} \label{integral:PL:map:prop}
For every $\gamma\in\calS$ the map
\begin{align*}
C\times \ldots \times C & \to \matR \\
\lambda & \longmapsto i(\gamma, \lambda)
\end{align*}
is half-integral piecewise linear.
\end{prop}
\begin{proof}
A colour $(a_i,b_i,c_i)\in C\times \ldots \times C$ defines a weighted train track $\tau$ and hence a measured topological lamination $\lambda$, obtained by substituting every edge of $\tau$ with some product $L\times J$ of horizontal leaves. Thanks to Proposition \ref{m:i:prop} the intersection $i(\gamma, \lambda)$ is realized by some representative $\gamma$ which is either a leaf of $\lambda$ or is transverse to $\lambda$ and forms no bigon with any leaf of $\lambda$.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{monotonic-BW}{monotonic}}
\nota{A monotonic curve $\gamma$ intersects the products $L \times J$ in monotonic paths (left) and forms no bigons outside the products (right).}
\label{monotonic:fig}
\end{center}
\end{figure}

We say that a closed curve transverse to $\lambda$ is \emph{monotonic} if 
\begin{enumerate}
\item it intersects every product $L\times J$ into arcs that are monotonic in both coordinates, and the same monotonicity is preserved when the curve goes from one product $L\times J$ to an adjacent one as in Figure \ref{monotonic:fig}-(left);
\item it makes no bigons outside the rectangles as in Figure \ref{monotonic:fig}-(right).
\end{enumerate}

Concerning (1), a horizontal path in $L\times J$ disjoint from $\lambda$ is allowed, but it must keep being horizontal on the adjacent products. 

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{monotonic2-BW}{monotonic2}}
\nota{If a monotonic curve $\gamma$ forms a bigon with a leaf $\alpha$, by cutting carefully $\tau$ along $\gamma$ we construct a portion of train track on this bigon containing $\alpha$ and with truncated edges exiting orthogonally from $\gamma$ (left). We then simplify the triangles adjacent to $\gamma$ (right).}
\label{monotonic2:fig}
\end{center}
\end{figure}

A simple closed curve that forms no bigons with any leaf of $\lambda$ can be easily isotoped to be monotonic. Conversely, we now prove that a monotonic curve $\gamma$ forms no bigons with any leaf of $\lambda$. If it did, by cutting $\tau$ along $\gamma$ we would get an abstract bigon with a portion of train track as in Figure \ref{monotonic2:fig}-(left). If $\gamma$ is adjacent to some triangles as in Figure \ref{monotonic2:fig}-(right) we close them as shown there. Finally, by doubling the bigon along $\gamma$ we get a train track on a disc, and by doubling again we build a train track in a sphere, which is absurd (one checks easily that no complementary region is a disc, annulus, monogon, or bigon: there are no bigons because we have closed the triangles as in Figure \ref{monotonic2:fig}-(right)).

The $\lambda$-transversal length $L(\gamma)$ of a monotonic $\gamma$ is the sum of the lengths of the sub-paths intersecting sequences of products $L\times J$ as in Figure \ref{monotonic:fig}-(left). One checks easily that the length of each sub-path is a half-integer linear combination of the colours $(a_i,b_i,c_i)$. Therefore $L(\gamma) = i(\gamma,\lambda)$ is a half-integer combination of the colours.

If we vary the colouring $(a_i,b_i,c_i)$ a little, the curve $\gamma$ keeps being monotonic in the same way as before, except when a portion of $\gamma$ is horizontal: in that case the new monotonicity depends on how the colouring varies. In all cases, the new $\gamma$ is still monotonic, hence bigonless, hence $L(\gamma)=i(\gamma, \lambda)$ again. 

If there are no horizontal portions in $\gamma$, the length $L(\gamma)$ varies linearly with the same integral formula found above. If there are horizontal portions, then the colour lies in a hyperplane of $\matR^{9g-9}$, and there are two different linear formulas joining there. Hence $i(\gamma,\lambda)$ is half-integral piecewise linear.
\end{proof}

The map $\lambda \mapsto i(\gamma, \lambda)$ is also obviously homogeneous, in the sense that $i(\gamma, t\lambda) = ti(\gamma, \lambda)$ for all $t\geqslant 0$. 

The proof of Proposition \ref{integral:PL:map:prop} contains a recipe for calculating $i(\gamma, \lambda)$. It suffices to put $\gamma$ in monotonic position and then add the contributions of each monotonic arc. For instance, the $i$-th curve $\gamma_i$ of the pants decomposition has an obvious monotone position giving $i(\gamma_i,\lambda) = a_i$.

The colours $b_i$ and $c_i$ do not have such an immediate description, but the following holds anyway.

\begin{ex} \label{abc:ex}
There exist finitely many simple closed curves $\gamma_j$ whose intersections $i(\lambda, \gamma_j)$ determine the colouring $(a_i,b_i,c_i)$ representing $\lambda$ in a half-integral piecewise-linear continuous fashion.
\end{ex}
\begin{proof}[Hint] Choose some additional curves as in Proposition \ref{9g-9:prop} 
and compute their intersections with $\lambda$.
\end{proof}


\subsection{The Thurston boundary}
We can finally determine the topology of the measured geodesic laminations space $\calML$ and of the Thurston boundary of the Teichm\"uller space.

\begin{prop}
The colouring parametrisation induces a homeomorphism $\calML \isom \matR^{6g-6}$.
\end{prop}
\begin{proof}
The map $\calML \to C\times \ldots \times C \isom \matR^{6g-6}$ is continuous by Exercise \ref{abc:ex}. It is proper: if the colours $(a_i,b_i,c_i)$ stay bounded, the intersections $i(\lambda, \gamma_i)$ with finitely many filling curves $\gamma_i$ stay bounded, and hence $\lambda$ moves in a compact set by Proposition \ref{compattezza:C:prop}. The continuous map is a homeomorphism by Proposition \ref{propria:chiusa:cor}.
\end{proof} 

Let now $\matP\calML \subset \matP\calC$ be the set of all \emph{projective measured laminations}, that is the image of $\calML\setminus 0$ in $\matP\calC$. The set $\matP\calML$ contains the projective simple closed curves $\matP\calS$ and the projective multicurves $\matP\calM$.\index{geodesic lamination!projective measured geodesic lamination}

\begin{teo}
The following homeomorphism holds
$$\partial \Teich(S_g) = \matP\calML \isom S^{6g-7}.$$ 
The set $\matP\calS$ is dense in $\matP\calML$.
\end{teo}
\begin{proof}
The homeomorphism $\calML \isom \matR^{6g-6}$ induces $\matP\calML \isom S^{6g-7}$. Concerning the Thuston boundary, we know from Section \ref{pinching:twisting:subsection} and Proposition \ref{alpha:zero:prop} that 
$$\matP\calS \subset \partial \Teich(S_g) \subset \matP\calML.$$
We now show that $\matP\calS$ is dense in $\matP\calML$, and this concludes the proof. 

First, we prove that $\matP\calM$ is dense in $\matP\calML$. Rational colours $(a_i,b_i,c_i)$ form a dense subset of $C\times \ldots \times C$ and project to a dense subset of $\matP\calML$. Every rational colour is a multiple of an integer colour, which represents a multicurve.

Second, we prove that $\matP\calS$ is dense in $\matP\calM$. Let $\mu$ be a multicurve in $S_g$. Up to acting via $\MCG(S_g)$ we may suppose that $\mu$ is supported on the pants decomposition $\gamma_1,\ldots, \gamma_{3g-3}$ used to define $C\times \ldots \times C$, hence $\mu$ is defined by some integral colour $(a_i,b_i,c_i) = (0,b_i,b_i)$. Now pick any simple closed curve $\gamma$ with $a_i' = i(\gamma, \gamma_i)>0$ for all $i$, represented by some colours $(a_i', b_i', c_i')$. By Dehn twisting $\gamma$ along the $\gamma_i$ we vary the pair $b_i', c_i'$ as we please, and by twisting at the correct rates we construct a sequence of simple closed curves that converge projectively to $[\mu]$.
\end{proof}

The mapping class group $\MCG(S_g)$ acts naturally on the whole set $\calC$ of currents and in particular it acts by homeomorphisms on $\partial \Teich(S_g)$. 

The identification of $\partial\Teich(S_g) = \matP\calML$ with the projectivisation of $C\times \ldots \times C$ is of course not canonical because it depends on a decomposition of $S_g$ into pairs of pants and annuli. However, Proposition \ref{integral:PL:map:prop} and Exercise \ref{abc:ex} imply that any two different identifications differ by some projective integral piecewise-linear homeomorphisms, hence the Thurston boundary has a natural \emph{projective integral piecewise linear} structure, called PIP for short, which is preserved by $\MCG(S_g)$. In particular $\matP\calML$ contains some natural rational points, and these are $\matP\calM$.\index{PIP structure}


\subsection{A projection}
The reader has probably noted that the coordinates that yield the homeomorphisms $\Teich(S_g) \cong \matR^{6g-6}$ and $\partial \Teich(S_g)\cong S^{6g-7}$ are quite similar: they both depend on a pants decomposition $\mu$ plus some additional marking, and every curve of the pants decomposition contributes roughly with two parameters, a ``length'' and a ``twist''. It would now be reasonable to expect that both these coordinates merge nicely to give a global homeomorphism $\overline{\Teich(S_g)} \cong D^{6g-6}$, but this is unfortunately not the case. 

The proof that $\overline{\Teich(S_g)}$ is homeomorphic to $D^{6g-6}$ is disappointingly indirect. We first prove that $\overline{\Teich(S_g)}$ is a topological manifold with boundary, by constructing some charts. To construct a chart, we first build a map
$$q\colon\Teich(S_g) \to \ML$$ 
that depends only on a fixed pants decomposition $\mu$. For a given hyperbolic metric $m\in\Teich(S_g)$, we construct a measured geodesic lamination $q(m)$ as follows. We straighten $\mu$ to its geodesic representative (with respect to $m$), and we consider separately each geodesic pair of pants $P$ of the decomposition. We first show that $P$ has a natural partial foliation, that depends only on its metric, whose leaves are not geodesics. We then glue these partial foliations to get a partial foliation on $S_g$, and then straighten it to a geodesic lamination $q(m)$.

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{pants_q-BW}{pants_q}}
\nota{Every geodesic pair of pants $P$ has a natural partial foliation: the shape of the foliation is determined by the sub-triangle containing $Q=[a_1,a_2,a_3]$ in Figure \ref{pants_train_tracks:fig}, where $a_1,a_2,a_3$ are the lengths of $\partial P$; the two pictures shown here correspond to two cases. In each case, there are three rectangles: each is the $R$-neighbourhood of the corresponding (unique) orthogeodesic\iftoggle{BW}{}{ (drawn in blue)}, and $R$ is the linear combination of $a_1,a_2,a_3$ prescribed by Figure \ref{pants_train_tracks:fig}, that is the unique combination that guarantees that the three rectangles match nicely as in the figure (1). We cut the geodesic pants $P$ along the three\iftoggle{BW}{}{ blue} orthogeodesics and get two right-angled hexagons. Since by hypothesis the three \iftoggle{BW}{small}{red} sides have length $\geqslant \varepsilon/2$, one sees easily that the central triangle has diameter bounded by some constant $C'$ depending only on $\varepsilon$, and hence every leaf in each of the three rectangles is shorter than some $C''$ that also depends only on $\varepsilon$ (2).}
\label{pants_q:fig}
\end{center}
\end{figure}

The natural partial foliation on $P$ is constructed as follows. Let $g_{ij}$ be the unique orthogeodesic connecting the $i$-th and $j$-th boundary component of $P$, for all $1 \leqslant i,j \leqslant 3$. Let $a_1, a_2, a_3$ be the lengths of the boundaries of $P$. We consider the point $Q=[a_1,a_2,a_3]$ in the triangle of Figure \ref{pants_train_tracks:fig}, pick the three orthogeodesics $g_{ij}$ isotopic to the three curves indicated in the sub-triangle of Figure \ref{pants_train_tracks:fig} containing $Q$, and thicken each $g_{ij}$ to a metric $R$-neighbourhood of $g_{ij}$, where $R$ is the linear combination of $a_1,a_2,a_3$ indicated in Figure \ref{pants_train_tracks:fig}. The $R$-neighbourhood is naturally foliated into (non-geodesic) arcs staying at fixed distance from $g_{ij}$ and the foliated neighbourhoods cover nicely much of the pair of pants $P$, as shown in Figure \ref{pants_q:fig}-(1). 
Every foliated rectangle is equipped with a natural transverse measure induced by the orthogonal distance between leaves.

The partial foliations of all the pairs of pants of $S_g$ glue to a singular measured foliation for $S_g$, which straightens as prescribed in Section \ref{parametrizzazione:subsection} to a measured geodesic lamination $q(m)$. 

Let $\mu = \gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$ be our original pants decomposition.

\begin{prop} \label{q:homeom:prop}
The map $q$ restricts to a homeomorphism
$$q\colon \Teich(S_g) \longrightarrow \big\{\lambda \in \ML \ \big|\ i(\lambda, \gamma_i)>0\ \forall i\ \big\}.$$
\end{prop}
\begin{proof}
Compare the coordinates $(l_i, \theta_i)$ for $\Teich(S_g)$ and $(a_i,b_i,c_i)$ for $\ML$. The map $q$ sends $(l_i,\theta_i)$ to $(l_i,b_i,c_i)$ for some $(b_i,c_i)$ that depends homeomorphically on $\theta_i\in\matR$ for each $i$.
Note that $a_i = i(\lambda, \gamma_i)$.
\end{proof}


\subsection{The fundamental lemma}
We now show that the projection $q$ distorts very little the lengths of the simple closed curves, as long as we put a lower bound on the lengths of the curves $\gamma_1,\ldots \gamma_{3g-3}$ of the fixed pants decomposition $\mu$. This technical fact is called the Fundamental Lemma \cite{FLP}.

For every $\varepsilon > 0$, we define $V(\varepsilon) \subset \Teich(S_g)$ to be the open subset consisting of all metrics $m$ such that $i(m,\gamma_i)>\varepsilon$ for all $i$.

\begin{lemma}
For every simple closed curve $\alpha\in \calS$ there exists a constant $C>0$ such that, for all $m\in V(\varepsilon)$, we have
$$i(q(m),\alpha) \leqslant i (m,\alpha) \leqslant i(q(m), \alpha) + C.$$
\end{lemma}
\begin{proof}
We represent $q(m)$ as a singular partial foliation, without straightening it. The transverse measure of $q(m)$ is just the length of orthogonal geodesics, hence the $q(m)$-measure of any piecewise-transverse closed curve is smaller or equal than its length: this proves that  $i(q(m),\alpha) \leqslant i (m,\alpha)$.

We prove the other inequality. If $\alpha = \gamma_i$ then $i(m,\alpha) = i(q(m),\alpha)$, so we suppose that $i(\alpha, \mu)>0$. Up to isotopy we may take $\alpha$ to be monotonically transverse to $q(m)$, recall the proof of Proposition \ref{integral:PL:map:prop}. The curve $\alpha$ intersects each pair of pants $P$ into some essential arcs $\beta$ that cross each foliated rectangle monotonically. 

We can easily homotope each of these arcs $\beta \subset \alpha\cap P$ with fixed endpoints into a (not necessarily simple!) piecewise smooth arc that decomposes into finitely many sub-arcs, that are alternatively contained either in a component of $\partial P$ or in a leaf of some foliated rectangle. Each sub-arc in a component of $\partial P$ may make many full turns (and hence may not be injective). Each of the three rectangles contains at most one leaf that is a sub-arc of $\beta$. We arrange the homotopy efficiently so that the new $\beta$ has the same transverse $q(m)$-measure as before.

The transverse $q(m)$-measure of $\beta$ on the sub-arcs in $\partial P$ is equal to its length, whereas on the leaf sub-arcs it is zero. Therefore the $m$-length of $\beta$ is equal to its measure plus the length of at most 3 leaves of some rectangles in $P$. Figure \ref{pants_q:fig}-(2) shows that each such leaf is shorter than some constant $C''$ that depends only on $\varepsilon$. 

Note that $\alpha$ is decomposed into $i(\alpha, \mu)$ arcs like $\beta$.
By homotoping each $\beta$ as above we find a homotopic representative for $\alpha$ whose length is at most the $q(m)$-measure of $\alpha$ plus $C=3i(\alpha,\mu)C''$. The length of any homotopic representative is greater or equal than the length $i(m,\alpha)$ of the geodesic one, and this proves the second inequality.
\end{proof}

\begin{cor} \label{same:limit:cor}
Let $m_i \in V(\varepsilon)$ be a diverging sequence in $\Teich(S_g)$. The sequence converges in $\overline{\Teich(S_g)}$ $\Longleftrightarrow$ the sequence $[q(m_i)]\in\PML$ does, and in this case they tend to the same limit.
\end{cor}
\begin{proof}
If $m_i$ converges to some $[\alpha]\in\PML$, we have $\lambda_im_i \to \alpha$ for some real numbers $\lambda_i \to 0$. By the fundamental lemma, for every simple closed curve $\gamma \in \calS$ we get
$$\big|i \big(\lambda_im_i, \gamma\big) - i\big(\lambda_iq(m_i), \gamma\big) \big| \to 0.$$
Therefore $\lambda_iq(m_i)$ converges (on a subsequence) to a $\beta\in\calML$ such that $i(\alpha, \gamma) = i(\beta, \gamma)$ for all $\gamma \in \calS$. Exercise \ref{abc:ex} gives $\beta =\alpha$.

The other implication is analogous.
\end{proof}


\subsection{A topological chart}
Pick an arbitrary $[\lambda]\in \PML = \partial \Teich(S_g)$. We now construct an explicit neighbourhood of $[\lambda]$ in $\overline{\Teich(S_g)}$. 

Let $\mu = \gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$ be a pants decomposition such that $i(\gamma_i, \lambda)>0$ for all $i$. We fix $\varepsilon>0$ and define as above $V(\varepsilon)\subset \Teich(S_g)$ as the set of all the metrics $m$ such that $i(\gamma_i, m)> \varepsilon$ for all $i$. We define similarly $W\subset \PML$ as the set of all $[\alpha]$ such that $i(\gamma_i, \alpha) > 0 $ for all $i$. We have $[\lambda]\in W$. 

\begin{prop} We have 
$$\pi(q(V(\varepsilon))) = \pi(q(\Teich(S_g))) = W.$$
The set $W\cup V(\varepsilon)$ is an open neighbourhood of $[\lambda]$ in $\overline{\Teich(S_g)}$.
\end{prop}
\begin{proof}
Proposition \ref{q:homeom:prop} implies the second equality, the first holds because every $[\alpha] \in W$ is represented by an $\alpha$ with $i(\gamma_i, \alpha)\geqslant \varepsilon$.

The sets $W$ and $V(\varepsilon)$ are open in $\PML$ and $\Teich(S_g)$ respectively.
If $W\cup V(\varepsilon)$ were not open in $\overline{\Teich(S_g)}$, there would be a sequence $m_i \not\in V(\varepsilon)$ of metrics converging to some $[\alpha]\in W$. On a subsequence we may suppose that $i(m_i,\gamma_j)<\varepsilon$ for some fixed $j$ and therefore $i(\alpha, \gamma_i)=0$, a contradiction.
\end{proof}

We have found an open neighbourhood of $[\lambda]$ and we now want to determine its topology. 

\begin{prop}
There is a homeomorphism 
$$\phi\colon W\cup V(\varepsilon) \longrightarrow U $$
onto an open subset $U\subset H$ of a half-space $H\subset \matR^{6g-6}$, with $\phi(W) = U\cap \partial H$.
\end{prop}
\begin{proof}
We complete the pants decomposition $\mu$ to a filling set $\mu'\in \calC$ of simple closed curves in $S_g$, considered as a current. We know from Proposition \ref{bounded:metrics:compact:cor} that the metrics $m$ with $i(m,\mu')\leqslant M$ form a compact subset in $\Teich(S_g)$. We define the map
\begin{align*}
\phi \colon W \cup V(\varepsilon) & \longrightarrow W\times [0,1] \\
x & \longmapsto 
\left\{
\begin{array}{ll} (x,0) & {\rm if\ } x\in W, \\
(\pi(q(x)), e^{-i(q(x),\mu')}) & {\rm if\ } x\in V(\varepsilon).
\end{array}
\right.
\end{align*}

The map $\phi$ is continuous: if a sequence $m_i\in V(\varepsilon)$ of metrics tends to $[\alpha]\in\PML$, then $i(m_i,\mu')\to \infty$, hence $i(q(m_i),\mu')\to \infty$ by the fundamental lemma. Moreover $\pi(q(m_i)) \to [\alpha]$ by Corollary \ref{same:limit:cor}. Summing up, we get that $\phi(m_i) \to ([\alpha],0) = \phi([\alpha])$.

The map $\phi$ is injective: given two metrics $m,m'$, if the first components of $\phi(m), \phi(m')$ are equal then $q(m) = \lambda q(m')$, and if the second components are equal we get $\lambda = 1$.

By similar methods one proves that the image of $\phi$ is open and the inverse there is continuous. The set $W\times [0,1]$ embeds in $H$ since $W$ embeds in $\matR^{6g-7}$.
\end{proof}

\begin{cor} The space $\overline{\Teich(S_g)}$ is a topological manifold with boundary $\partial \Teich(S_g)$.
\end{cor}


\subsection{Conclusion} \label{MCG:conclusion:subsection}
We have discovered that $\overline{\Teich(S_g)}$ is a compact topological manifold with boundary, and we now invoke Theorem \ref{topological:disc:teo} to deduce that it is a disc. We have finally completed the proof of the following theorem, which is the main achievement of the whole chapter.

\begin{teo} \label{current:compactification:teo}
The closure $\overline{\Teich(S_g)}$ of $\Teich(S_g)$ in $\matP\calC$ is homeomorphic to the closed disc $D^{6g-6}$. Its interior is $\Teich(S_g)$ and its boundary contains $\calS$ as a dense subset.
\end{teo}

Thurston's original compactification theorem embeds everything in $\matR^\calS$ instead of $\calC$. We can easily deduce it from Theorem \ref{current:compactification:teo}.

\begin{proof}[Proof of Theorem \ref{compattificazione:teo}]
The natural map $\calC \to \matR^\calS$ induced by the intersection form $i$ is continuous since $i$ is, and it induces a continuous map $\varphi\colon\matP\calC \to \matP(\matR^\calS)$ on their projective spaces. 

The Teichm\"uller space is embedded in both projective spaces and $\varphi$ restricts to a homeomorphism between the two embeddings, and to a continuous surjective map from their compactifications. The map on compactifications is actually injective since $\varphi|_{\PML}$ is (intersections with simple closed curves distinguish laminations) and is hence a homeomorphism.
\end{proof}
