---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-058-112-knots-and-links
section_title: "Knots and links"
section_number: 11.2
pages: 353-360
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.825
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Knots and links are fundamental and beautiful objects in geometric topology. Knots and links in $S^3$ have a combinatorial and mildly two-dimensional nature because they can be treated as planar diagrams, but they should be considered as intrinsically three-dimensional objects.


\subsection{Definition}
A \emph{link} in a 3-manifold $M$ is a compact submanifold of dimension one. Being compact, it consists of finitely many circles, and a connected link is called a \emph{knot}. Links and knots are usually considered up to ambient isotopy.\index{link}\index{knot}

\begin{figure}
\begin{center}
\includegraphics [width = 4 cm] {Trefoil_knot_left.png}
\quad
\includegraphics [width = 4 cm] {\iftoggle{BW}{Blue_Trefoil_Knot-BW}{512px-Blue_Trefoil_Knot}}
\nota{Every knot may be described via a planar diagram with over/under crossings (left) and its tubular neighbourhood is a knotted solid torus (right).}
\label{trefoil_knots:fig}
\end{center}
\end{figure}

Every link in $S^3$ can be projected to a plane: if the link is generic with respect to the projection, its image is a \emph{diagram} as in Figure \ref{trefoil_knots:fig}-(left). Every link in $S^3$ can be described via a diagram and can be thus treated combinatorially, but it is important to note that the same link can be represented via infinitely many diagrams and it is hard in general to tell whether two given diagrams represent the same link. The \emph{trivial knot} (or \emph{unknot}) $K\subset S^3$ is the one that has a planar diagram without crossings.\index{unknot}


\subsection{Chirality}
The \emph{mirror image} of a knot or link is obtained by reflecting it with respect to any plane in $S^3$. On a diagram, this operation is realised simply by inverting all crossings simultaneously.

A knot is \emph{chiral} if it is not isotopic to its mirror image, and \emph{achiral} otherwise. For instance, the trivial knot is achiral, but the trefoil knot (shown in Figure \ref{trefoil_knots:fig}) is chiral.\index{knot!trefoil knot}
As in the rest of this book, we mostly ignore orientation issues and often consider implicitly two mirrored knots or links as equivalent.\index{knot!achiral and chiral knot}


\subsection{Link complement}
The tubular neighbourhood of a link $L$ in an orientable $M$ consists of solid tori by Proposition \ref{S1:bundle:prop}, and the \emph{link complement} of $L$ is the three-manifold with boundary obtained from $M$ by removing the interiors of these solid tori. If $M$ is compact, the link complement also is.\index{link complement}

\begin{prop}
Let $K\subset S^3$ be a knot. The complement of $K$ is an irreducible manifold. Moreover, the following facts are equivalent:
\begin{enumerate}
\item $K$ is trivial,
\item $K$ bounds a disc in $S^3$,
\item the complement of $K$ is a solid torus.
\end{enumerate}
\end{prop}
\begin{proof}
The complement of $K$ is irreducible by Proposition \ref{connected:boundary:prop}.
The implication (1)$\Rightarrow$(2) is the smooth Jordan curve theorem, and (2)$\Rightarrow$(1) holds because all discs in a connected three-manifold are isotopic. 

A trivial knot thickens to a standardly embedded solid torus, whose complement is a solid torus: hence (1)$\Rightarrow$(3). Conversely, if the complement of $K$ is a solid torus then $S^3$ decomposes into two solid tori as $S^3=L(1,q)$. The meridian of the complement solid torus extends to a disc with boundary $K$, hence (3)$\Rightarrow$(2).
\end{proof}

\begin{cor} \label{H:tori:cor}
All Heegaard tori for $S^3$ are isotopic
\end{cor}
\begin{proof}
A Heegaard torus $T\subset S^3$ is by definition a torus that decomposes $S^3$ into two solid tori. By the proposition the core of one of these solid tori is always isotopic to a trivial knot and hence $T$ is isotopic to a standard torus.
\end{proof}

A link complement in $S^3$ can be reducible: this holds precisely when there is a sphere $\Sigma \subset S^3$ disjoint from the link $L$ that cut $S^3$ into two balls, each containing some components of $L$. In that case we say that the link is  \emph{split}.\index{link!split link}

\begin{cor}
Let $L\subset S^3$ be a non-trivial knot or non-split link. The link complement is Haken.
\end{cor}
\begin{proof}
The link complement $M$ is irreducible by assumption; by Proposition \ref{irreducible:solid:torus:prop}, if $M$ contains an essential disc then it is a solid torus and hence $L$ is the trivial knot, which is excluded. Now $M$ is Haken by Corollary \ref{boundary:implies:Haken:cor}.
\end{proof}


\subsection{Prime knots}
There is an operation on knots in $S^3$ called \emph{connected sum}, similar to the one on manifolds and described in Figure \ref{sum_of_knots:fig}. 
A connected sum is \emph{trivial} if one of the two knots is trivial; a non-trivial knot is \emph{prime} if it is not the result of a non-trivial connected sum, and \emph{composite} otherwise.\index{knot!prime and composite knot}

\begin{figure}
\begin{center}
\includegraphics [width = 12.5 cm] {\iftoggle{BW}{Sum_of_knots-BW}{Sum_of_knots}}
\nota{Connected sum of knots: put two knots in disjoint balls and connect them with a band as shown.}
\label{sum_of_knots:fig}
\end{center}
\end{figure}

The \emph{crossing number} of a knot is the minimum number of crossings in a diagram describing it.\index{knot!crossing number} Prime knots with small crossing number have been tabulated since the XIX century: at present all the prime knots with up to 16 crossing have been classified (by Hoste -- Thistlethwaite -- Weeks \cite{HTW} in 1998) and the first 14 numbers of them are listed in Table~\ref{prime:knots:table}. The prime knots with $\leqslant 7$ crossings are shown in Figure \ref{Knot_table:fig}: the first three in the list are the unknot, the \emph{trefoil}, and the \emph{figure-eight knot}.\index{knot!figure-eight knot} 

\begin{table}
\begin{center}
\begin{tabular}{c||ccccccccccccccc}
 $c$       & \phantom{\Big|}\!\! $0$ & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$
 & $9$ & $10$ & $11$ & $12$ & $13$ & $14$ \\
 \hline \hline
$n$ & 
\phantom{\Big|}\!\!
1 & 0 & 0 & 1 & 1 & 2 & 3 & 7 & 21 & 49 & 165 & 552 & 2176 & 9988 & 46972 
\end{tabular}
\vspace{.2 cm}
\nota{The number $n$ of prime knots with $c$ crossings, for all $c\leqslant 14$.}
\label{prime:knots:table}
\end{center}
\end{table}

\begin{figure}
\begin{center}
\includegraphics [width = 10 cm] {Knot_table.pdf}
\nota{Prime knots in $S^3$ with at most $7$ crossings. The knots $3_1$ and $4_1$ are the \emph{trefoil} and the \emph{figure-eight} knots respectively.}
\label{Knot_table:fig}
\end{center}
\end{figure}

A connected sum gives rise to a sphere which intersects the new knot in two points, see Figure \ref{sum_of_knots3:fig}. The sphere intersects the knot complement into an essential annulus. 

\begin{figure}
\begin{center}
\includegraphics [width = 6 cm] {Sum_of_knots3.pdf}
\nota{A connected sum produces a sphere (dotted in the figure) intersecting the knot in two points.}
\label{sum_of_knots3:fig}
\end{center}
\end{figure}


\subsection{Torus knots}
We now introduce a simple and natural family of prime knots. 
Consider the standardly embedded torus $T\subset S^3$ with meridian $m$ and longitude $l$ oriented as in Figure \ref{torus:ml:fig}. A pair $(p,q)$ of coprime integers determines a simple closed curve in $T$ that is homologically $qm + pl$, and such a curve is called a \emph{$(p,q)$-torus knot}. More generally, a pair of integers $(a,b)$ determines a multicurve in $T$ that is homologically $bm+al$, called an \emph{$(a,b)$-torus link}.\index{knot!torus knot}\index{link!torus link}

\begin{figure}
\begin{center}
\reflectbox{\includegraphics[width = 5 cm] {\iftoggle{BW}{800px-Toroidal_coord_resized-BW}{800px-Toroidal_coord_resized}}}
\nota{The meridian $m$ (\iftoggle{BW}{light grey}{red}) and longitude $l$ (\iftoggle{BW}{dark grey}{blue}) of a standard torus are oriented as shown here, like a right-hand screw.}
\label{torus:ml:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Blue_7_1_Knot-BW}{480px-Blue_7_1_Knot}}
\includegraphics[width = 5 cm] {\iftoggle{BW}{3D-Link-BW}{3D-Link}}
\nota{The torus knot $(2,-7)$ and the torus link $(2,-8)$.}
\label{torus_knot:fig}
\end{center}
\end{figure}

For instance, the trefoil knot is a $(2,-3)$-torus knot. More examples are in Figure \ref{torus_knot:fig}. The knots $3_1$, $5_1$, and $7_1$ from Figure \ref{Knot_table:fig} are torus knots.

\begin{ex} \label{trivial:torus:knot:ex}
If $|p|\leqslant 1$ or $|q|\leqslant 1$ the torus knot is the unknot. The torus knots with parameters $(p,q)$, $(-p,-q)$, and $(q,p)$ are isotopic, the torus knot with parameters $(p,-q)$ is the mirror image of $(p,q)$.
\end{ex}

The complement of a torus knot is a quite simple kind of Seifert manifold. In the following we suppose that $p,q \geqslant 1$ are coprime. 

\begin{prop} \label{torus:knot:complement:prop}
The complement of a $(p,q)$-torus knot is a Seifert manifold fibering over the orbifold $(D,p,q)$. More precisely, it is
$$\big(D, (p,r), (q,s)\big)$$
where $(r,s)$ is any pair such that $ps+qr = 1$.
\end{prop}
\begin{proof}
Let $K \subset T \subset S^3$ be the $(p,q)$-torus knot. The pair $(r,-s)$ determines another simple closed curve $\alpha \subset T$ that intersects $K$ in one point. The complement of $K$ in a tubular neighbourhood $T\times [-1,1]$ of $T$ is diffeomorphic to $P\times S^1$, where $P$ is a pair of pants. On the tori $T\times \{-1\}$ and $T \times 1$ the curves $\partial P \times \{{\rm pt}\}$ and $\{{\rm pt}\} \times S^1$ are isotopic to $\alpha$ and $K$.

The complement of $T\times [-1,1]$ in $S^3$ consists of two solid tori, with meridians $(1,0)$ and $(0,1)$. Read in the basis $(\alpha, K)$ the meridians are $(q,s)$ and $(p,r)$. The complement of $K$ in $S^3$ is obtained from $P\times S^1$ by filling these curves and hence we get $\big(D, (p,r), (q,s)\big)$.
\end{proof}

In particular the complement of the trefoil knot is $\big(D,(2,1), (3,1)\big)$. If we suppose $p,q\geqslant 2$, two torus knots with distinct (unordered) parameters have non-diffeomorphic complements and hence are not isotopic.
Our intuition says that a torus knot is prime, and we can prove this rigorously.

\begin{prop}
Every torus knot is prime. 
\end{prop}
\begin{proof}
If $K$ is obtained as a non-trivial connected sum, there is an essential annulus in the complement, whose boundary curves are meridians of $K$. There is only one essential annulus in $\big(D, (p,r), (q,s)\big)$ and its boundary curves are not meridians.
\end{proof}

The $(2,2)$-torus link is called the \emph{Hopf link} and is drawn in Figure \ref{Hopf_link:fig}.\index{link!Hopf link}

\begin{ex} The complement of the Hopf link is $T\times [0,1]$. Any two distinct fibres of the Hopf fibration form a Hopf link.
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Hopf_Link-BW}{617px-Hopf_Link}}
\nota{The Hopf link is the $(2,2)$-torus link.}
\label{Hopf_link:fig}
\end{center}
\end{figure}


\subsection{Satellite knots}
We have discovered that che composite knots contain essential annuli in their complement, and we now look for essential tori. It is convenient to introduce the following definition.

\begin{defn}
A knot $K\subset S^3$ is a \emph{satellite} if its complement contains an essential torus.\index{knot!satellite knot}
\end{defn}

We now formulate an equivalent and more inspiring definition of satellite knots which justifies the terminology. A knot in a solid torus $D^2 \times S^1$ is \emph{local} if it is contained in a ball, and a \emph{core} if it is isotopic to $\{x\} \times S^1$. An embedding $\varphi\colon D^2 \times S^1 \hookrightarrow S^3$ is \emph{trivial} (or \emph{unknotted}) if the image of a core is a trivial knot.

\begin{prop}
A knot $K\subset S^3$ is satellite $\Longleftrightarrow$ it is the image of a knot $K' \subset D^2 \times S^1$ which is neither local nor a core, along a non-trivial embedding $\varphi \colon D^2\times S^1 \hookrightarrow S^3$.
\end{prop}
\begin{proof}
A knot $K=\varphi(K')$ constructed in this way is satellite, because the torus $\varphi (S^1\times S^1)$ is essential in the complement of $K$: it is incompressible (on one side because $\varphi$ is non-trivial, and on the other because $K'$ is not local) and not $\partial$-parallel (because $K'$ is not a core).

Conversely, if $K$ is a satellite knot then its complement contains an essential torus $T\subset S^3$. As every torus in $S^3$, the torus $T$ bounds a solid torus. Since $T$ is essential, the knot $K$ is contained in this solid torus in a non-local and non-core way.
Moreover the solid torus is knotted, otherwise $T$ would be compressible on the other side.
\end{proof}

The non-trivial embedding $\varphi$ sends the core curve of $D^2\times S^1$ to some non-trivial knot $H\subset S^3$ called the \emph{companion} of $K$: we should think of $K$ as orbiting as a ``satellite'' around its companion $H$, with orbit path $K'$. When $K'$ is contained in the boundary of the solid torus $D^2\times S^1$ the satellite knot $K$ is called a \emph{cable} knot. Some examples are shown in Figure \ref{satellites:fig}.\index{knot!cable knot}

\begin{figure}
\begin{center}
\includegraphics[width = 5.5 cm] {B_sat1.png}
\includegraphics[width = 5 cm] {B_sat2.png}
\nota{Two satellite knots.}
\label{satellites:fig}
\end{center}
\end{figure}




\subsection{Simple complements}
Recall from Section \ref{simple:manifold:subsection} that a compact three-manifold is simple if it contains no essential sphere, disc, torus, and annulus. Which knots have a simple complement? To answer to this question, we need a general lemma on three-manifolds that identifies the few cases where there are essential annuli without essential tori.

\begin{lemma} \label{only:annuli:lemma}
Let $M$ be irreducible and $\partial$-irreducible, with boundary consisting of tori. The manifold $M$ contains no essential tori but contains some essential annuli $\Longleftrightarrow$ it is diffeomorphic to one of the following:
$$\big(D,(p_1,q_1), (p_2,q_2)\big), \quad \big( A, (p,q) \big), \quad P\times S^1$$
with $p_1,p_2 \geqslant 2$. Here $P$ is a pair of pants.
\end{lemma}
\begin{proof}
Propositions \ref{v:h:prop} and \ref{incompressible:vertical:prop} imply that the Seifert manifolds listed contain vertical essential annuli, but not essential tori. 

Conversely, let $M$ contain an essential annulus $A$. Suppose that $A$ connects two distinct boundary tori $T,T'$ of $M$. A regular neighbourhood of $T\cup T'\cup A$ is diffeomorphic to $P\times S^1$, and its boundary contains a third torus $T''\subset M$. Since $T''$ cannot be essential, it is either boundary parallel or bounds a solid torus in $M$, and $M$ is diffeomorphic respectively  to $P\times S^1$ or a Dehn filling of it. In the latter case, the Dehn filling is not fibre-parallel because $M$ is $\partial$-reducible (use Corollary \ref{fiber:parallel:cor}), hence we get a Seifert manifold of type $\big(A, (p,q) \big)$.

If $A$ connects one boundary component to itself we conclude similarly and may also get $M = \big(D, (p_1,q_1), (p_2,q_2)\big)$. 
\end{proof}

We can now state and prove an important trichotomy on knots. 

\begin{prop} \label{trichotomy:knots:prop}
Every knot $K\subset S^3$ is either a torus knot, a satellite knot, or has a simple complement.
\end{prop}
\begin{proof}
We only need to prove that if the complement $M$ contains an essential annulus and no essential tori then $K$ is a torus knot. The previous lemma gives $M=\big(D,(p_1,q_1),(p_2,q_2)\big)$, and to get $S^3$ back we must have a Dehn filling $S^3 = \big(S^2,(p_1,q_1), (p_2,q_2), (1,n)\big)$. In particular $K$ is isotopic to a fibre and hence contained in a vertical Heegaard torus for $S^3$. Heegaard tori are standard by Corollary \ref{H:tori:cor}, and hence $K$ is a torus knot.
\end{proof}

The relevance of this proposition will be magnified later, after introducing geometrisation. Note that in particular all the composite knots are satellite knots: where is the essential torus?
