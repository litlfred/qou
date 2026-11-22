---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-010-8-biconnected-graphs
section_title: "Biconnected graphs"
section_number: 8
pages: 22-35
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.99
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:biconnected}


This section gives further detail to the argument of \cite[\S12.7~p.131]{Hales:2006:DCG:4}.  There it is claimed that
the proof of the main estimate~\cite[Theorem~12.1]{Hales:2006:DCG:4} can be reduced to the case of polygonal standard regions.
This claim is correct. 
However, the justification of this claim is not complete in the original proof.
This section gives complete justification of the claim.   The main result is Theorem~\ref{thm:biconnected}, stated below.

This section patches the original proof.  As such, it should be imagined this section to be inserted as an addendum, directly following Section~12.13 in the original proof, as a new Section~12.14.  (In fact, Section~12.13 is itself an addendum to the 1998 preprint, making this section the second addendum to Section~12.)  If the actual insertion were to be carried out, the corresponding changes to the numbering of the results in this section would be made: Theorem~\ref{thm:biconnected} below would be inserted as a new Theorem~{12.21}, and so forth. 

In the original proof, the boundaries of standard regions may fail to be
simple polygons.  In fact, the failure of the boundaries to be polygons may be quite
severe: the boundaries may contain multiple components and articulation vertices.
An {\it articulation}
vertex in a graph is a vertex whose removal increases the number of connected
components of the graph.  A connected graph is {\it biconnected} if it contains no
articulation vertex.

In the original proof, each standard region is first prepared by a process
of erasure (described in \cite[\S11.1]{Hales:2006:DCG:4}), then deformed in a way
to transform its boundary into a simple polygon.  The deformation
is made in such a way that the values of 
two key functions $\op{vor}_{0,R}$ and $\tau_{0,R}$ are left unchanged.
These are the functions that enter into the main estimate~\cite[Theorem~12.1]{Hales:2006:DCG:4}.

What the original proof fails to consider
is a particular hypothetical situation where the deformation might fail.  This situation is illustrated in Fig.~\ref{fig:biconnected}, where the rigid movement of set of vertices (such as the illustrated triangle with vertex $w$)
is blocked by a nearby vertex $v$ that is not visible from $w$, when the distance between $v$ and $w$ drops
to the minimum value $2$. This section presents a proof that this hypothetical situation does
not occur.

 The strategy of the proof in this section is to use a deformation argument.  A general decomposition star is deformed until the graph attached to it becomes biconnected.  In a biconnected planar graph with at least three vertices, each face is a simple polygon.  Thus, by producing a biconnected graph, we achieve our objective.  
In the original proof of the Kepler conjecture, biconnected graphs are not
mentioned by name.   Nevertheless, most of the graphs that occur in the late stages
of the original proof are biconnected.

In more detail, the proof in this section will produce a sequence of
admissible deformations of a decomposition star $D$ in such a way that
the individual standard regions $R$ are preserved in number and identity (but
not in shape) by the deformations.
The deformations will preserve the values of $\op{vor}_{0,R}(D)$ and
$\tau_{0,R}(D)$, for each standard region $R$. 
The deformations will change the combinatorial structure of the graph
formed by all the subregions of the decomposition star. 
At the conclusion of the deformation, the decomposition star $D$ will have
a graph (formed by all the subregions of the decomposition star) 
that is biconnected.  As in the original proof, the decomposition star
is first simplified by a process of erasure, before the deformations begin.

In the remainder of this section, 
we adopt notation, definitions, and conventions without further comment
from \cite{Hales:2006:DCG:4}.  

\begin{figure}
\begin{center}
\includegraphics[width=5cm]{biconnected.pdf}
\end{center}
\caption{In this figure (not to scale), segments represent geodesic arcs on the unit sphere.  The shaded region is a subregion whose boundary is not a simple polygon.
We wish to rigidly slide the triangle containing the vertex $w$ until a new visible distinguished edge forms
(say from $w$ to $u$).  We will show that this rigid motion does not decrease the distance between
two vertices (say $w$ and $v$)  to the minimum distance $2$.}
\label{fig:biconnected}
\end{figure}



\subsection{Context}

We work in the following restrictive
context for Theorem~\ref{thm:biconnected} and its proof.  
We fix a packing centered at a vertex at the origin.
As described in Section~12.6 of the original proof, we assume that all upright quarters
are erased, except loops (that is, those surrounded by anchored simplices).    
Let $U$ be the set of (non null) vertices of of height at most $2.51$.  As usual, we say two edges $\{u_1,u_2\}$ and $\{u_1',u_2'\}$ {\it cross}
if the interiors of the triangles formed by $\{0,u_1,u_2\}$ and $\{0,u_1',u_2'\}$ intersect.

We form the set of edges $E'$ between vertices in $U$, consisting of
\begin{itemize}
\item all standard edges; that is, $\{v,w\}\subset U$ such that $0<\|v-w\|\le 2.51$.
\item all edges $\{v,w\}\subset U$ of an anchored simplex, whenever the upright diagonal of the anchored simplex is an unerased loop.
\item all edges $\{v,w\}\subset U$ such that $0<\|v-w\|\le\sqrt8$, where $\{v,w\}$ does not cross any other edge in previous two items.  (If two of these edges cross, pick only one of them. This can only happen with conflicting diagonals
of a quad cluster.)
\end{itemize}
These edges do not cross.  A {\it special simplex} $\{0,u,v,w\}$ has one edge $\{v,w\}$ of length at least $\sqrt8$,
called the {\it special edge}.  
A special edge has length at most $3.2$.
The other vertex $u$ is called a {\it special vertex} (or {\it special corner}).
Let $E=E'\setminus S$, where $S$ is the set of special edges (that
is, the edges of special simplices shared with an anchored simplex).
 The projection of the line segments formed by $E$ to the
unit sphere is a planar graph.
The complement of this graph in the unit sphere
is a disjoint union of connected components.  The closures of these connected components are called {\it subregions}.

We call a {\it loop subregion} one that contains an unerased loop $\{0,v\}$.
If $R$ is a loop subregion, then there are no enclosed vertices of height $\le 2.51$ over the
subregion.  The corners of $R$ are the anchors of the upright diagonal together with the special corners
of the subregion.  The subregion $R$ is star convex with center point at the projection of $v$ to the unit sphere.
It follows that the boundary of $R$ is a simple polygon.

The graph $\Gamma$ with vertices $U$ and edges $E$ is not necessarily connected.  The aim is to deform
$U$ (and $D$) to create a biconnected graph (without changing the values of $\op{vor}_{0,R}(D)$ and $\tau_{0,R}(D)$ for {\it standard regions} $R$; the values for individual subregions will change).  Once the graph $\Gamma$
is biconnected, the subregions are simple polygons as desired.

The deformation of $U$ is {\it admissible} if it satisfies the following three conditions.
\begin{itemize}
\item If the graph $\Gamma$ is not connected,
the deformation acts by a rotation about the origin 
on the vertices of a single chosen connected component of $\Gamma$,
leaving all other vertices of $U$ fixed.  (For example, in Figure~\ref{fig:biconnected}, the entire triangle with vertex $w$ may be rotated.)  In particular,
$\|v\|$, for $v\in U$, is constant.
\item If the graph $\Gamma$ is connected, but not biconnected, with a chosen articulation vertex $a$, then
the deformation acts by a rotation about the axis $\{0,a\}$ on the vertices of a single component of $\Gamma\setminus\{a\}$,
leaving all other vertices of $U$ fixed.
\item The distance between $v,w$ remains at least $2$, for all $v,w\in U$.
\end{itemize}

The deformation stops when either of the following {\it halting conditions} are met:
{
\renewcommand{\labelenumi}{(H{\theenumi})}
\begin{enumerate}
\item $\|v-w\|\le\sqrt8$, where the edge $\{v,w\}\not\in E'$, with $\{v,w\}\subset U$, does not cross any edge in $E'$, or
\item $\|v-w\|$ decreases to $2$ for some $v,w\in U$, and $\{v,w\}$ crosses an edge in $E'$.
\end{enumerate}
}

We warn that the deformation is allowed to assume configurations in which the distance between some $u\in U$ and the upper endpoint of an unerased upright diagonal $d$ is less than $2$.  This is not a problem because the vertex $u$ does not end up as a corner of the loop subregion to which the upright diagonal $d$ belongs.  (In particular, the halting condition (H1) prevents a new special vertex from being added to a loop subregion.) Thus, when a single subregion is considered in isolation, all distances between pairs of vertices in that subregion are at least $2$.

In the restrictive context that has been described in this section, we have the following result.

\begin{thm}\label{thm:biconnected}  
If the graph $\Gamma=(U,E)$ is not biconnected, then a nontrivial admissible
deformation 
of $U$ exists. 
The  halting condition (H2) never holds.  The admissible
deformation can always be continued until the halting
condition (H1) holds.
\end{thm}

\begin{figure}
\begin{center}
\includegraphics[width=10cm]{cases.pdf}
\end{center}
\caption{Theorem~\ref{thm:biconnected} breaks into various cases: (a) two edges with
distinct endpoints, (b) three or more edges, (c) two edges, or (d) a single edge
passing through the triangle $\{0,v,w\}$.}
\label{fig:cases}
\end{figure}

We break the proof of Theorem~\ref{thm:biconnected} into cases (a), (b), (c), (d) according
to the number and combinatorial structure of the edges $\{u_1,u_2\}$
that pass through the triangle $\{0,v,w\}$.  See Figure~\ref{fig:cases}.
Lemma~\ref{lemma:double-edge} below gives Case (a): we cannot have two such edges $\{u_1,u_2\}$ and $\{u_1',u_2'\}$ with distinct endpoints.   It follows that there is an endpoint $u_2$ shared by every edge that passes through the
triangle $\{0,v,w\}$.  Lemma~\ref{lemma:three-edge} below gives Case (b): there cannot be three or more edges.  Finally, Cases (c) and (d) of one or two edges $\{u_1,u_2\}$ are treated in further subsections.  Each subsection is organized
around one of the main cases (with introductory Section~\ref{sec:pre}): Cases (a), (b), (c), and (d) are
treated in the four Sections~\ref{sec:22}, \ref{sec:13}, \ref{sec:12}, \ref{sec:11}, respectively.


When $U$ is deformed until the halting condition (H1) holds, a new edge $\{v,w\}$ can be added to $E$.
The theorem is repeated to add further edges, until a biconnected graph is obtained.  
The remainder of this section explains why the halting condition (H2) never holds.  For
this, we assume on the contrary, that $\|v-w\|=2$, where $\{v,w\}$ belong to different connected components
of $\Gamma$ (if $\Gamma$ is not connected) and different connected components of $\Gamma\setminus\{a\}$ (if $a$
is an articulation vertex of a connected graph $\Gamma$).  When this situation occurs, we say that $v,w$ belong to
different bicomponents.  Without loss of generality, we may also assume that $\{v,w\}$ crosses some edge of $E'$.


\subsection{Preliminary lemmas}\label{sec:pre}

Lemma~\ref{lemma:1} below shows that a vertex does not cross over an edge during a deformation; the halting conditions for the vertex are met before it reaches the edge.  Recall that the term {\it geometric considerations} refers to a specific collection of methods introduced in \cite[\S4.2]{Hales:2006:DCG} to prove the existence and non-existence of various simple configurations of points in $\ring{R}^3$.

\begin{lemma}\label{lemma:1} Let $S=\{0,v,,u_1,u_2\}$ be a set of four distinct points in $\ring{R}^3$ whose pairwise distances are at least $2$.  Suppose that $\|u\|\le 2.51$, for all $u\in S$.  If the segment $\{0,v\}$ meets the segment $\{u_1,u_2\}$, then $\|v-u_1\|,\|v-u_2\|\le 2.51$.
\end{lemma}

\begin{proof} This follows by geometric considerations.
\end{proof}

The next two lemmas give conditions under which the halting condition (H2) cannot hold.

\begin{lemma}\label{lemma:prelim}  Let $S=\{v,w,u_1,u_2,v_0\}$ be a set of five distinct points in $\ring{R}^3$ whose
pairwise distances are at least $2$. Suppose that the segment $\{v,w\}$ passes through
$\{v_0,u_1,u_2\}$. Assume
$$
\begin{array}{lll}
\|u_1-u_2\|\le 3.2,\\
\|v_0-u\|\le 2.51,\text{ for } u \in S.\\
\end{array}
$$
Then $\|v-w\|>2$.
\end{lemma}

\begin{proof} This follows by geometric considerations.
\end{proof}

\begin{lemma}\label{lemma:291}  Let $S=\{v,w,u_1,u_2,v_0\}$ be a set of five distinct points in $\ring{R}^3$ whose
pairwise distances are at least $2$. Suppose that the segment $\{u_1,u_2\}$ passes through
$\{v_0,v,w\}$. Assume
$$
\begin{array}{lll}
\|u_1-u_2\|\le 2.91,\\
\|v_0-u\|\le 2.51,\text{ for } u \in S.\\
\end{array}
$$
Then $\|v-w\|>2$.
\end{lemma}



\begin{proof} This follows by geometric considerations.
\end{proof}

By Lemmas~\ref{lemma:prelim} and \ref{lemma:291}, we may assume that for each edge $\{u_1,u_2\}$ that $\{v,w\}$ crosses,
we have that $\{u_1,u_2\}$ passes through $\{0,v,w\}$ and that $\|u_1-u_2\|>2.91$.  This means that the edge $\{u_1,u_2\}$ is an edge of an anchored simplex,
so that the edge is special or bounds a loop subregion.
This loop subregion will provide the key to the proof, because we will show
that it prevents the distance between $v$ and $w$ from becoming $2$,
as assumed  (Fig.~\ref{fig:biconnectedloop}).


\begin{remark}
As an aside, we mention that this issue of biconnected graphs is a major issue only in the 
proof of the Kepler conjecture and not
in the proof of the dodecahedral conjecture~\cite{Hales:2008:Dodec}.  In the proof of the dodecahedral conjecture there are no loops of anchored simplices, and without loops there are no difficulties: edges of length at most
$\sqrt8$ can be be used instead of the set $E'$.  Lemmas~\ref{lemma:prelim} and~\ref{lemma:291} suffice.
\end{remark}

\begin{figure}
\begin{center}
\includegraphics[width=5cm]{biconnectedloop.pdf}
\end{center}
\caption{In this figure (not to scale), segments represent geodesic arcs on the unit sphere.  The two shaded regions represent
subregions.    There are possibly other subregions partitioning the unshaded portions of the figure.  These other subregions are not represented in this figure.  The shaded region marked $L$ represents a loop subregion. The other shaded region represents a subregion with two boundary components that is undergoing a deformation, by the motion of the triangle with vertex $v$.  The situation of Fig.~\ref{fig:biconnected} does not exist
(as will be shown).  The  intervening loop subregion $L$  forces
$v$ and $w$ to be more than the minimum distance apart.}
\label{fig:biconnectedloop}
\end{figure}



\subsection{Case (a): Edge crossings with distinct endpoints}\label{sec:22}


\begin{lemma}\label{lemma:double-edge} 
There does not exist a set $S=\{0,v,w,u_1,u_2,u_1',u_2'\}$ of seven distinct points
in $\ring{R}^3$ whose pairwise distances are at least $2$ and that satisfies the following conditions.
\begin{itemize}
\item The edges $\{u_1,u_2\}$ and $\{u_1',u_2'\}$ do not cross.
\item The edges $\{u_1,u_2\}$ and $\{u_1',u_2'\}$ both pass through $\{0,v,w\}$.
\item $\|u\|\le 2.51$ for all $u\in S$.
\item $\|v-w\|=2$.
\item $\|u_1-u_2\|,\|u_1'-u_2'\|\le 3.2$.
\item $u_1$ and $u_1'$ lie in the same half-space bounded by the plane $\{0,v,w\}$.
\item The directed segment from $v$ to $w$ crosses the segment $\{u_1',u_2'\}$ before the segment $\{u_1,u_2\}$.
\end{itemize}
\end{lemma}

Note that the last two conditions can always 
be achieved by suitable labels on the points $\{u_1,u_2,u_1',u_2'\}$.

\begin{proof}
This will follow as a direct consequence of Lemmas~\ref{lemma:7small} and~\ref{lemma:7big} below.
\end{proof}

\begin{lemma}\label{lemma:diam} 
Let $S=\{u,v,w\}$ be a triangle such that each side has length at least $2$, and such that $\|u-v\|\le 2.51$, $\|u-w\|\le 2.51$, $\|v-w\|=2$.  Let $X$ be the set of points in the convex hull of $S$ that have distance at least $1.2$ from each vertex of $S$.  Then the diameter of $X$ is less than $1.044$.
\end{lemma}

\begin{proof} Let $x=\|u-v\|$ and $y=\|u-w\|$.  Assume $x\ge y$.  As $u$ moves away from $v$, along a fixed line through $v$ and an initial position $u_0$, the region $X$ expands.  Thus, we may assume that $x=2.51$.   The boundary of $X$ is a polygonal curve consisting of line segments and concave arcs of circles.  The diameter is realized by the distance between two vertices $p_i(y)$ of the polygonal curve. We consider two cases according to $y\le 2.4$ and $y\ge 2.4$ because the structure of the polygonal curve changes at $y=2.4$.  We calculate $\|p_i(y)-p_j(y)\|$ directly, checking for each $(i,j)$ that the distances are less than $1.044$.
\end{proof}

\begin{lemma}\label{lemma:7small}  
Let $S=\{0,,v,w,u_1,u_2,u_1',u_2'\}\subset\ring{R}^3$
be a configuration of seven points that satisfies
the conditions of Lemma~\ref{lemma:double-edge}.  Then there exist
a point $p$ on the segment $\{u_1,u_2\}$ and  a point $p'$ on the segment
$\{u_1',u_2'\}$ such that $\|p-p'\|<1.044$.
\end{lemma}

\begin{proof} Let $u\in\{0,v,w\}$.  By the metric constraints, the
distance from $u$ to the segment $\{u_1,u_2\}$ (resp. $\{u_1',u_2'\}$) is at least
$$\sqrt{2^2 - (3.2/2)^2} = 1.2.$$
Let $p$ (resp. $p'$) be the point of intersection of the segment $\{u_1,u_2\}$ 
(resp. $\{u_1',u_2'\}$) with
the convex hull of $\{0,v,w\}$.  By Lemma~\ref{lemma:diam},
we have $\|p-p'\|<1.044$.
\end{proof}

\begin{lemma}\label{lemma:abc}
Let $S=\{u_1,u_1',u_2,u_2'\}\subset\ring{R}^3$ be a set of four distinct points such that the distance between each pair of points is at least $2$.  Assume that
$$
\|u_1-u_2\|\le 3.2,\quad \|u_1'-u_2'\|\le 3.2.
$$
If any of the following conditions hold:
{
\renewcommand{\labelenumi}{(\Alph{enumi})~~}
\begin{enumerate}
\item $\|u_1-u_2'\|,\|u_1'-u_2\|\ge 2.91$;
\item $\|u_1-u_1'\|,\|u_2-u_2'\|\ge 2.85,\quad \|u_1-u_2'\|\ge 2.91$;\quad or
\item $\|u_1-u_1'\|\ge 3.64,\quad \|u_1-u_2'\|\ge 2.91$;
\end{enumerate}
}
then every point on the segment $\{u_1,u_2\}$ has distance greater than $1.044$ from every point on the segment $\{u_1',u_2'\}$.
\end{lemma}

\begin{proof} Assume for a contradiction that the assumptions hold and that
the conclusion is false for some configuration.  The metric constraints can be used to show that the segments $\{u_1,u_2\}$ and $\{u_1',u_2'\}$ can be stretched along their axes without decreasing any edge length.  

Thus we may assume without loss of generality that $\|u_1-u_2\|=\|u_1'-u_2'\|=3.2$.  Decreasing one dihedral angle of the simplex $S$ at a time, we may move the segments closer together, until all four edges $\{u_i,u_j'\}$ attain their minimum length.  

Then we have three rigidly determined simplices (A), (B), (C) (with equality constraints).  An explicit coordinate calculation of the distance between the two segments shows that the distance is greater than $1.044$ in each case.
\end{proof}


\begin{lemma}\label{lemma:7big}  
Let $S=\{0,,v,w,u_1,u_2,u_1',u_2'\}\subset\ring{R}^3$
be a configuration of seven points that satisfies
the conditions of Lemma~\ref{lemma:double-edge}.  Then there do not exist
a point $p$ on the segment $\{u_1,u_2\}$ and  a point $p'$ on the segment
$\{u_1',u_2'\}$ such that $\|p-p'\|<1.044$.
\end{lemma}

\begin{proof}  Assume for a contradiction that such $p,p'$ exist.
In Lemma~\ref{lemma:abc}, we may assume that none of the
conditions A, B, C hold.  By obvious symmetry, without loss of generality, we may assume by case A
that $\|u_2-u_1'\|<2.91$.  By Lemma~\ref{lemma:291}, this implies that $\{u_1',u_2\}$ does not pass through $\{0,v,w\}$.  By the conditions of the lemma, the segment $\{u_1,u_1'\}$ does not meet the plane $\{0,v,w\}$, so that $\{u_1,u_1'\}$ does not pass through $\{0,v,w\}$.  This means that the triangle $\{u_1,u_1',u_2\}$ is linked around $\{0,v,w\}$; and  some edge of $\{0,v,w\}$ passes through $\{u_1,u_1',u_2\}$.  Up to symmetry there are two cases: (1) $\{0,v\}$ passes through $\{u_1,u_1',u_2\}$, or (2) $\{v,w\}$ passes through $\{u_1,u_1',u_2\}$.

In the first case, recall that $\{u_1',u_2'\}$ does not cross $\{u_1,u_2\}$.
So $u_2'$ is enclosed over $(0,\{u_1,u_1',u_2\})$.  Then $\{u_2',u_1\}$
and $\{u_2',u_1'\}$ pass through $\{0,v,w\}$.  By Lemma~\ref{lemma:291}, we
have $\|u_2'-u_1\|,\|u_2'-u_1'\|\ge 2.91$.  As we are assuming that C does not hold, we have $\|u_1-u_1'\|\le 3.64$.  We claim that $\{0,u_2'\}$
passes through $\{u_1,u_1',u_2\}$.  Otherwise, $u_2'$ lies in the convex hull of $\{0,u_1,u_1',u_2\}$ and a coordinate calculation shows that the upper bounds on the edges of the simplex $\{0,u_1,u_1',u_2\}$ are inconsistent with the lower bounds on the distances from $u_2'$ to the vertices of the simplex.  Since $\{0,u_2'\}$ passes through $\{u_1,u_1',u_2\}$ we may use geometric considerations to show that $\|u_2'\| > 2.51$.  This is contrary to the hypotheses of Lemma~\ref{lemma:double-edge}.

In the second case, $\{v,w\}$ passes through $\{u_1,u_1',u_2\}$ and through $\{u_1',u_2',u_2\}$.  Geometric considerations give $\|u_1-u_1'\|>2.85$ and $\|u_2-u_2'\|> 2.85$.  Assuming that B does not hold gives $\|u_1-u_2'\|< 2.91$.  The first paragraph of the proof now gives that $\{u_2,u_2',u_1\}$ links around the triangle $\{0,v,w\}$.  The edge $\{v,w\}$ does not pass through $\{u_2,u_2',u_1\}$.  (This can be seen by drawing the relative positions of $p(u)$, for $u\in S$, in the projection $p$ of the points to a plane orthogonal to $\{v,w\}$.)  Thus, we are in the first case, which has already been treated.
\end{proof}


\subsection{Case (b): Triple edge crossings}\label{sec:13}

By Lemma~\ref{lemma:double-edge}, there is a common endpoint $u_2$ such that every edge
of $E'$ that passes through $\{0,v,w\}$ has $u_2$ as an endpoint.
Next we show that there cannot be three such edges.  


\begin{lemma}\label{lemma:three-edge}
There does not exist a set of seven distinct points
$$S=\{0,v,w,u_1,u_1',u_1'',u_2\}$$ in $\ring{R}^3$ that satisfies
the following conditions.
\begin{itemize}
\item The distance between each pair of distinct points in $S$ is at least $2$.
\item The edges $\{u_1,u_2\}$, $\{u_1',u_2\}$, and $\{u_1'',u_2\}$ pass through
$\{0,v,w\}$.
\item $\|u\|\le 2.51$, for all $u\in S$.
\item $\|v-w\|=2$.
\item $\|u-u_2\|\le 3.2$, for $u=u_1,u_1',u_1''$.
\end{itemize}
\end{lemma}

\begin{proof}
Assume for a contradiction that $S$ exists.
We may pivot $w$ around the axis $\{0,v\}$ until $\|w-u_2\|\le 2.51$.  (The metric constraints on
edge lengths show that the condition $\Delta>0$
is preserved for the simplices $\{u,u_2,v,w\}$ and $\{u,u_2,w,0\}$, for $u=u_1,u_1',u_1''$, throughout
this pivot.)  A similar
pivot of $v$ gives $\|v-u_2\|\le 2.51$.
We may order the vertices in cyclic order around $\{0,u_2\}$ as
$$(w_1,w_2,w_3,w_4,w_5)=(w,u_1,u_1',u_1'',v),$$ 
so that setting
$d(w_i,w_j) = \dih(0,u_2,w_i,w_j)$, we have
$$d(w_1,w_5)=\sum_{i=1}^4 d(w_i,w_{i+1})\ge d(w_2,w_3)+d(w_3,w_4).$$
Interval calculations\footnote{\calc{2799256461}, \calc{5470795818}} 
give $d(w_2,w_3),d(w_3,w_4)\ge 0.7$
and $d(w_1,w_5)< 1.4$. We obtain an immediate contradiction:
$$1.4 > d(w_1,w_5) \ge 0.7 + 0.7.$$
\end{proof}


\subsection{Case (c): Double edge crossings}\label{sec:12}

This subsection treats the case of two edges crossings in the proof
of Theorem~\ref{thm:biconnected}.
We continue to assume the general context of Theorem~\ref{thm:biconnected}.  As usual, 
the edge $\{u_1,u_2\}\in E'$ crosses $\{v,w\}$.

\begin{lemma}\label{lemma:special}
Let $\{u_1,u_2,w,v\}$ be a set of four distinct points
in $\ring{R}^3$ (in the given context).  
Assume that
 $\|v-u_i\|\le 2.51$, for $i=1,2$.
Assume that no edge of $E'$ crosses $\{v,w\}$
in the open 
half-space $A$ containing $v$ bounded by the plane $\{0,u_1,u_2\}$.
(That is, $\{u_1,u_2\}$ is the first edge to cross $\{v,w\}$, moving
from $v$ toward $w$.)
Assume there is a loop subregion $L$ along 
$\{u_1,u_2\}$ on the $A$-side
of $\{u_1,u_2\}$.  Then $\{u_1,u_2\}$ is a special edge of $E'$ with
corner $v$.
In particular, $\{u_1,u_2\}\not\in E$, so that it is not a bounding
edge of a subregion.
\end{lemma}

\begin{proof}
Assume for a contradiction that $\{u_1,u_2\}$ is not special.
Note that loop subregions have simple polygonal boundaries and
remain rigid under all the deformations.  In particular,
the upright diagonal, special corners, and so forth
remain rigidly positioned with respect to the corners of the subregion.

Since there are no further edges crossing $\{v,w\}$, the subregion
$L$ extends to $v$.  Hence $v$ is a corner of the subregion $L$.
It is either an anchor or a special corner (with respect to $L$). However, it cannot be a special
corner, by the assumption that $\{u_1,u_2\}$ is not a special edge.
Hence it is an anchor.  Also, $u_1$ and $u_2$ are anchors.

To reach a contradiction, 
we consider possible locations of the upright diagonal $\{0,u\}$,
and show that it has nowhere to go (Figure~\ref{fig:nogo}).  
Since $\{u_1,u_2\}$ is an edge,
the points $u_1,u_2$ are consecutive anchors. This prevents $u$ from lying over the region $B$.  
Also, the upright diagonal of any
unerased loop has at least four anchors (say $v,u_1,u_2,w$).  Moreover, some anchored simplex around the upright diagonal is not an upright quarter (because of the edge $\{u_1,u_2\}$).  Geometric considerations based
on these constraints (say $\|w-u_1\|\ge 2.51$) show that
the fourth anchor $w$ is not in $A$.  This prevents $u$ from
being located over the region $A$.
A vertex $u_j$ cannot be enclosed over an upright quarter $\{0,u,v,u_i\}$.  This excludes
 region $C$.  Finally, an edge $\{v,u_i\}$
of length at most $2.51$ cannot pass through a triangle $\{0,u,u_j\}$
of sides at most $2.51,2.51,\sqrt8$ (excluding $D$).
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width=5cm]{nogo.pdf}
\end{center}
\caption{The upright diagonal $u$ cannot be placed over any of
the regions $A,B,C,D$.  The lines (not to scale) represent geodesic arcs on the
sphere passing through the pairs of points in $\{p(u_1),p(u_2),p(v)\}$,
where $p$ denotes projection to the unit sphere.}
\label{fig:nogo}
\end{figure}

\begin{lemma}\label{lemma:circuit} 
Let $\{u_1,u_2,w,v\}$ be a set of four distinct points
in $\ring{R}^3$ (in the given context).  
Assume that
 $\|v-u_i\|\le 2.51$, for $i=1,2$.
Assume that no edge of $E$ crosses $\{v,w\}$
in the open 
half-space $A$ containing $v$ bounded by the plane $\{0,u_1,u_2\}$.
(That is, $\{u_1,u_2\}$ is the first edge to cross $\{v,w\}$, moving
from $v$ toward $w$.)
Then 
both edges $\{u_1,v\}$ and $\{u_2,v\}$ belong to $E$.
In particular, there is a circuit of the graph $\Gamma$ through $v,u_1,u_2$.
\end{lemma}

\begin{proof} If
there is a loop subregion $L$ along 
$\{u_1,u_2\}$ on the $A$-side
of $\{u_1,u_2\}$, Lemma~\ref{lemma:special} implies that
$\{u_1,u_2\}$ is a special edge of $E'$ with
corner $v$.  In particular, $\{u_1,v\}$ and $\{u_2,v\}$ are
edges of $E$. The conclusion follows in this case.


 Now assume that there is no loop subregion along
$\{u_1,u_2\}$ on the $A$ side of $\{u_1,u_2\}$.

Let $S$ be the finite set of points of $U$ enclosed
over the simplex $\{0,u_1,u_2,v\}$.  We show by contradiction
that $S$ is empty.
The plane $\{0,v,w\}$ separates
$S$ into a disjoint union $S = S_1\cup S_2$, according to those
in the same half-space as $u_i$, $i=1,2$.
We form the convex hull of the projection $p$ to the unit sphere of the 
points $S_i\cup\{u_i,v\}$.  As in~\cite[\S12.13]{Hales:2006:DCG:4},
form a sequence of geodesic arcs on the unit sphere from $p(u_i)$
to $p(v)$.  Let $p(w_i)$, for $w_i\in S_i$, be the other endpoint
of the arc starting at $p(u_i)$ (or set $w_i=v$ if $S_i=\emptyset$.  

For some $w'\in\{w_1,w_2\}\setminus\{v\}$,  the edges $\{w',u_i\}$ do not cross any edges
of $E$.  Furthermore, geometric considerations show that
$\|w'-u_i\|\le 2.51$, for $i=1,2$.  By the criteria for forming
edges of $E$, we must have $\{w',u_i\}\in E$ for $i=1,2$.  This
contradicts the assumption that $\{v,w\}$ does not cross any edges
of $E$ over $A$.  Hence $S=\emptyset$.

Since $S=\emptyset$, the edges $\{v,u_i\}$ do not cross any edges
of $E$.  By the criteria for forming edges of $E$, they belong to $E$.
This completes the proof.
\end{proof}

We are ready to prove the next major case of Theorem~\ref{thm:biconnected}.
We continue to work in the general context of that theorem, with $v$ and $w$
in different bicomponents of the graph $\Gamma$.

\begin{lemma}\label{lemma:double-cross}  
In this context, there does not exist a set of six points $\{0,v,w,u_1,u_1',u_2\}$
where $\{u_1,u_2\}$ and $\{u_1',u_2\}$ pass through $\{0,v,w\}$ and such that
  $$\|u_1-u_2\|\le 3.2,\quad \|u_1'-u_2\|\le 3.2.$$
\end{lemma}

\begin{proof}  We argue by contradiction.  We may assume that $\{u_1,u_1'\}$ are ordered so that the cyclic order around $\{0,u_2\}$ is
$(w_1,w_2,w_3,w_4)=(v,u_1',u_1,w)$. 
By the previous results, there are at most two edges that pass through $\{0,v,w\}$
in this manner.  In particular, the part of the line segment $\{v,w\}$ between the crossings
of $\{u_1,u_2\}$ and $\{u_1',u_2\}$ lies in a single subregion $L$.  

We claim that we do not have $\|v-u_1'\|,\|v-u_2\|,\|w-u_1\|,\|w-u_2\|\le 2.51$.  Otherwise, we break
into two cases and derive a contradiction as follows.  Either (1) $L$ is a loop subregion, or (2)
$L$ is not a loop subregion, but both regions adjacent to $L$ (along edges $\{u_1,u_2\}$, $\{u_1',u_2\}$)
are loop subregions.  In case (1),
$\{u_1,u_2,u_1'\}$ are corners of the loop subregion $L$.  Hence, they lie on a circuit in $\Gamma$
formed by the corners of that loop subregion.  
If $\|v-u_2\|,\|v-u_1'\|\le 2.51$, then by Lemma~\ref{lemma:circuit}, the points
$\{v,u_1',u_2\}$ lie on a circuit in $\Gamma$.  A similar conclusion holds if corresponding inequalities
hold $\|w-u_2\|,\|w-u_1\|\le 2.51$.  If all four inequalities hold, then these circuits put $v,w$ in the
same bicomponent of $\Gamma$, which is contrary to hypothesis.  
In case (2), then by Lemma~\ref{lemma:circuit}, $\{v,u_2\},\{v,u_1'\}\in E$, so $\{u_1',u_2\}$ is a special
edge and $L$ is a loop subregion.  This is contrary to the assumption of case (2).
Hence we may assume by symmetry and without
loss of generality that $\|v-u_1'\|\ge 2.51$ or $\|v-u_2\|\ge 2.51$.

We may stretch along the edges $\{u_2,u_1\}$, $\{u_2,u_1'\}$, moving $u_1,u_1'$, 
until $\|u_2-u_1\|=\|u_2-u_1'\|=3.2$.   We may add inequality
$$
\|u_2\|\le 2.23,
$$
for otherwise by geometric considerations $\|u_2-u_1'\|> 3.2$.  Similarly, $\|u_1'\|\le 2.23$.
If $\|u_2-v\|\ge 2.51$, we may pivot $v$ toward $u_2$ around the axis $\{0,w\}$ until $\|u_2-v\|\le 2.51$.
Similarly, we may assume that $\|u_2-w\|\le 2.51$.

Set $d(i,j) = \op{dih}(0,u_2,w_i,w_j)$.
Then interval arithmetic calculations\footnote{\calc{7431506800}, \calc{5568465464}, \calc{4741571261}, \calc{6915275259} } give the contradiction:
$$
1.3 > d(1,4) = d(1,2) +d(2,3)+d (3,4) > 0.5 + 0.8 + 0 = 1.3.
$$
\end{proof}


\subsection{Case (d): Single edge crossings}\label{sec:11}

This subsection treats the proof of Theorem~\ref{thm:biconnected}
in the case of a single edge crossing $\{u_1,u_2\}$.  This is
the final case of the proof.
We continue to assume the notation and general context of that theorem.
In particular,  $v$ and $w$ lie in different bicomponents of
the graph $\Gamma$.

\begin{lemma}  Let $\{0,u_1,u_2,v,w\}$ be a set of five distinct
points such that $\{u_1,u_2\}$ is the only edge of $E'$ that
crosses $\{v,w\}$.  Then $\|v-w\|>2$.
\end{lemma}

\begin{proof} We assume for a contradiction that $\|v-w\|=2$.
We consider four cases depending on lengths.  

{\it Case 1:} $\|u-u_i\|\le 2.51$, for $i=1,2$ and $u=v,w$.
By Lemma~\ref{lemma:circuit}, there are circuits running through
$\{u,u_1,u_2\}$, for $u=v,w$.  This is contrary to the assumption
that $v,w$ lie in different bicomponents of the graph $\Gamma$.  (In the remaining cases, there is
no loss in generality to assume $\|w-u_2\|\ge 2.51$.)

{\it Case 2:} $\|w-u_2\|\ge 2.51$, $\|v-u_1\|\ge 2.51$.
Geometric considerations give the contradiction
$\|u_1-u_2\|>3.2$.

{\it Case 3:} $\|w-u_2\|\ge 2.51$, $\|v-u_2\|\ge 2.51$.
Geometric considerations gives the contradiction
$\|u_1-u_2\|>3.2$.

{\it Case 4:} $\|w-u_2\|\ge 2.51$, $\|v-u_i\|\le 2.51$, for $i=1,2$.
The edge $\{u_1,u_2\}$ cannot be a special edge of $E'$.  Otherwise,
$v,w$ are corners of the same loop subregion.  This contradicts
the running assumption that these two vertices belong to separate
bicomponents of the graph $\Gamma$.  By Lemma~\ref{lemma:special}, there is no loop subregion along $\{u_1,u_2\}$ on the $v$-side.
Since $\{u_1,u_2\}$ has length greater than $\sqrt8$, there
is a loop subregion $L$ bounded by the edge, and it must then lie
on the $w$-side.  Thus, $w$ is a corner of $L$ and the circuit of
$\Gamma$ described by the boundary of $L$ passes through $w,u_1,u_2$.
By Lemma~\ref{lemma:circuit}, there is a circuit of $\Gamma$ through
$v,u_1,u_2$.  Hence, $v,w$ lie in the same biconnected component,
which is contrary to the running assumption.
\end{proof}
