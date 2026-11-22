---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-050-94-haken-manifolds
section_title: "Haken manifolds"
section_number: 9.4
pages: 302-311
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.645
latex_coverage_ratio: 0.998
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
There are two classes of irreducible closed three-manifolds: those that contain incompressible surfaces, and those that do not. Both classes are very important and contain a wealth of interesting manifolds.

The manifolds belonging to the first class are called \emph{Haken manifolds} and are somehow easier to study, because they can be cut into balls via a standard procedure called \emph{hierarchy}: we cut the manifold along an essential surface, then along another, and we iterate until we get balls. We study these manifolds here. We also prove the converse of Proposition \ref{pi1:prop}, that is that a closed surface is incompressible if and only if it is $\pi_1$-injective, see Theorem \ref{incompressible:teo}.


\subsection{Introduction}
If not otherwise mentioned, all the 3-manifolds $M$ we will consider in this section will be connected, compact, oriented and with (possibly empty) boundary.
We introduce a definition.

\begin{defn} A \emph{Haken manifold} is a compact, connected, oriented 3-manifold $M$ with (possibly empty) boundary, which is irreducible, $\partial$-irreducible, and contains an incompressible and $\partial$-incompressible surface.\index{three-manifold!Haken three-manifold}
\end{defn} 

The reader should not be frightened by the abundance of adjectives: this definition is really clever because it summarises various reasonable hypothesis in a unique word. The rest of this chapter is mainly devoted to the study of Haken manifolds. We start by looking at their boundaries.

\begin{prop}
Every boundary component $X$ of a Haken manifold $M$ has $\chi(X)\leqslant 0$ and is incompressible.
\end{prop}
\begin{proof}
No component $X$ of $\partial M$ is a sphere: if it were so, it would bound a ball $B$ and we would have $M=B$, contradicting Corollary \ref{B:cor}. Hence $\chi(X)\leqslant 0$ and $X$ is incompressible
because $M$ is $\partial$-irreducible.
\end{proof}

We now prove that there are plenty of Haken manifolds. We start with a general proposition.

\begin{prop}
Let $M$ be an oriented, compact, irreducible, and $\partial$-irreducible 3-manifold with (possibly empty) boundary.
Every non-trivial homology class $\alpha \in H_2(M,\partial M;\matZ)$ is represented by a disjoint union of incompressible and $\partial$-incompressible oriented surfaces.
\end{prop}
\begin{proof}
Every class $\alpha$ is represented by a properly embedded oriented surface $S$ by Proposition \ref{homology:prop}. A compression as in Figure \ref{incompressible:fig} and \ref{incompressible2:fig} does not alter the homology class of the surface: indeed in homology we have $S'-S = \partial B$ where $B=D\times [-1,1]$ is a tubular neighbourhood of the compressing disc $D$. Hence $[S'] = [S] = \alpha$.

We compress $S$ until its connected components are either incompressible and $\partial$-incompressible surfaces, discs, or spheres. Since $M$ is irreducible and $\partial$-irreducible, discs and spheres bound balls and are hence homologically trivial, so they can be removed.
\end{proof}

\begin{cor} 
Let $M$ be oriented, compact, irreducible, and $\partial$-irreducible. If $H_2(M,\partial M; \matZ)\neq \{e\}$ then $M$ is Haken. 
\end{cor}
\begin{cor} \label{boundary:implies:Haken:cor}
Let $M$ be oriented, compact, irreducible, and $\partial$-irreducible. 
If $\partial M \neq \emptyset$ and $M\neq B$, then $M$ is Haken.
\end{cor}
\begin{proof}
If $\partial M$ contains a sphere, it bounds a ball $B$ and hence $M=B$. Otherwise $H_1(\partial M)$ has positive rank, and hence $H_2(M,\partial M)=H^1(M)$ also has positive rank by Corollary \ref{rank:cor}.
\end{proof}

We recall that every compact orientable 3-manifold decomposes along spheres and disc into irreducible and $\partial$-irreducible pieces. If one such piece has non-empty boundary then either it is ball, or it is Haken.

The following lemma will be useful soon. It says that every Haken manifold contains an interesting ``spanning'' surface $S$, that touches all the boundary components (the spanning surface need not to be connected).

\begin{lemma} \label{chiappa:tutto:lemma}
Every Haken manifold $M$ contains an oriented surface $S$, whose components are incompressible and $\partial$-incompressible, such that $[\partial S\cap X]\in H_1(X,\matZ)$ is non-trivial for every boundary component $X$ of $M$.
\end{lemma}
\begin{proof}
We have $\partial M = X_1\sqcup \ldots \sqcup X_k$ with $\chi(X_i)\leqslant 0$ for all $i$. Proposition \ref{lagrangian:prop} says that the image of 
$$\partial \colon H_2(M,\partial M, \matZ) \longrightarrow H_1(\partial M,\matZ)$$
is a lagrangian subgroup $L$ of maximal rank. We have 
$$H_1(\partial M, \matZ) = \oplus_{i=1}^k H_1(X_i, \matZ).$$
The decomposition is orthogonal with respect to the symplectic intersection form $\omega$. There is an $\alpha\in L$ whose projection to each $H_1(X_i,\matZ)$ is non-trivial: if not, the space $L$ would be $\omega$-orthogonal to some $H_1(X_i,\matZ)$ and hence contained in a smaller symplectic subspace, a contradiction since $L$ has maximal rank.
Pick any incompressible and $\partial$-incompressible surface $S$ such that $\partial [S] = \alpha$.
\end{proof}


\subsection{Normal surfaces}
On Haken manifolds, incompressible surfaces are efficiently detected by normal surfaces.  

\begin{prop} \label{normal:incompressible:prop}
Let $M$ be Haken and $T$ be a triangulation for $M$. Every compact surface $S\subset M$ whose components are all incompressible and $\partial$-incompressible is isotopic to a normal surface.
\end{prop}
\begin{proof}
We know that $S$ becomes normal after surgeries as in Figure \ref{incompressible:fig} or Figure \ref{incompressible2:fig}. These surgeries are actually isotopies since $S$ is incompressible and $\partial$-incompressible, and $M$ is irreducible and $\partial$-irreducible (see Figure \ref{incompressible3:fig}).
\end{proof}

Note that in the proof of Proposition \ref{normal:incompressible:prop}, as in many other proofs, it is crucial that $M$ be irreducible and $\partial$-irreducible.
We can now apply Lemma \ref{non:parallel:lemma} to get the following.

\begin{cor} \label{incompressible:cor}
Let $M$ be a Haken manifold. There is a $K>0$ such that every set $S$ of pairwise disjoint and non-parallel incompressible and $\partial$-incompressible surfaces in $M$ consists of at most $K$ elements.
\end{cor}

Our aim is now to cut a Haken manifold iteratively along incompressible and $\partial$-incompressible surfaces. The two-dimensional analogue to keep in mind is the following: every surface $S_g$ of genus $\geqslant 2$ can be cut into pairs-of-pants; a pair-of-pants is a quite simple surface, but we are still not satisfied and we further cut it along three arcs into two discs (two hexagons). We have constructed a two-step decomposition of $S_g$ into discs: this is what we would like to extend from two to three dimensions.


\subsection{Cutting along surfaces}
When we cut a 3-manifold along an incompressible surface, some nice properties of the manifold are preserved.

\begin{prop} \label{cut:surface:prop}
Let $M$ be compact and irreducible, and $S\subset M$ be either an essential disc or an incompressible surface. Let $M'$ be obtained by cutting $M$ along $S$. The following holds:
\begin{itemize}
\item the manifold $M'$ is irreducible;
\item a closed $\Sigma\subset M'$ is incompressible in $M'$ $\Longleftrightarrow$ it is so in $M$.
\end{itemize}
\end{prop}
\begin{proof}
We prove that $M'$ is irreducible. Let $\Sigma\subset M'$ be a sphere. Since $M$ is irreducible, the sphere $\Sigma$ bounds a ball $B\subset M$. The ball $B$ cannot contain $S$ because all surfaces in a ball are compressible. Therefore $B\subset M'$ and $M'$ is irreducible.

To prove the second assertion, we show that $\Sigma$ has a compressing disc $D$ in $M$ if and only if it has one in $M'$. If $D$ lies in $M'$ then of course it lies also in $M$. Conversely, suppose $D$ lies in $M$. Put $D$ in transverse position with respect to $S$ and pick an innermost intersection circle in $D$, bounding a disc $D'\subset D$. Since $D'$ cannot compress $S$, and since $M$ is irreducible, the disc $D'$ can be isotoped away from $S$. This simplifies $D\cap S$ and after finitely many steps we get $D\cap S = \emptyset$ and hence $D\subset M'$.
\end{proof}

\begin{cor} \label{Haken:cor}
If we cut a Haken 3-manifold along a closed incompressible surface, we get a disjoint union of Haken 3-manifolds.
\end{cor}

The following consequence is also interesting.

\begin{cor} \label{handlebody:closed:cor}
Let $M$ be compact with non-empty boundary. If $M$ is irreducible, then either it is a handlebody or it contains a closed incompressible surface. 
\end{cor}
\begin{proof}
The manifold $M$ decomposes along essential discs into manifolds $M_1, \ldots, M_k$ that are irreducible and $\partial$-irreducible. If every $M_i$ is a ball then $M$ is a handlebody. If $M_i$ is not a ball, the closed surface $S=\partial M_i$ is not a sphere and is incompressible in $M_i$, and hence also in $M$ by Proposition \ref{cut:surface:prop}.
\end{proof}


\subsection{Hierarchies}
We want to use incompressible surfaces to cut every Haken manifold into simpler pieces. The procedure goes as follows.

A \emph{hierarchy} for a Haken 3-manifold $M$ is a sequence of 3-manifolds\index{hierarchy}
$$M=M_0 \stackrel{S_0}\rightsquigarrow M_1 \stackrel{S_1}\rightsquigarrow M_2 \stackrel{S_2}\rightsquigarrow \ldots \stackrel{S_{h-1}}\rightsquigarrow M_h $$
where each $M_{i+1}$ is obtained cutting $M_i$ along a properly embedded (possibly disconnected) surface $S_i\subset M_i$, such that the following holds:
\begin{itemize}
\item every component of $S_i$ is an incompressible and $\partial$-incompressible surface or an essential disc, for all $i$;
\item the final manifold $M_h$ consists of balls.
\end{itemize}
The number $h$ is the \emph{height} of the hierarchy. We now show that every Haken manifold can be ``atomised'' into balls in three steps.
\begin{teo} \label{hierarchy:teo}
Every Haken manifold has a hierarchy of height $3$.
\end{teo}

\begin{proof}
Let $S_0$ be a maximal family of pairwise disjoint and non-parallel closed incompressible surfaces in $M$, which exists by Corollary \ref{incompressible:cor}. We cut $M_0=M$ along $S_0$ and get $M_1$.

Every connected component $M_1^i$ of $M_1$ is Haken by Corollary \ref{Haken:cor}. 
By Lemma \ref{chiappa:tutto:lemma} for every $i$ there is a ``spanning'' surface $S_1^i\subset M_1^i$ made of incompressible and $\partial$-incompressible components that intersects every boundary component of $M_1^i$. We cut $M_1$ along the spanning $S_1 = \sqcup S_1^i$ and get a new manifold $M_2$. 

We now prove that $M_2$ contains no closed incompressible surface. Indeed, if $\Sigma\subset M_2$ were closed and incompressible, then it would be so also in $M$ by Proposition \ref{cut:surface:prop}. Since $S_0$ is maximal, the surface $\Sigma$ would be parallel to a component of $S_0$, that is it would cobound a $\Sigma \times [0,1]$ with it. Since the spanning surface $S_1$ intersects all the boundary components of $M_1$, a component of $S_1$ would be contained in $\Sigma \times [0,1]$ and would intersect the boundary only on the side of $S_0$: this is excluded by Proposition \ref{line:bundles:prop} (products do not contain incompressible and $\partial$-incompressible surfaces with boundary only on one side).

Every component of $M_2$ is a handlebody by Corollary \ref{handlebody:closed:cor}. We cut it along a set $S_2$ of essential discs to get balls.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 8 cm] {\iftoggle{BW}{hierarchy-BW}{hierarchy}}
\nota{The strata $S_0$, $S_1$, and $S_2$ intersect in vertices (left). The boundary of each ball $B\subset M_2$ is tessellated into domains belonging to $S_0, S_1$, or $S_2$. Three of them intersect at a 3-valent vertex (right).}
\label{hierarchy:fig}
\end{center}
\end{figure}

Hierarchies may be used to prove theorems on Haken manifolds. We will now use them to prove that incompressible surfaces must be $\pi_1$-injective: we need a preliminary discussion and a lemma.

In our hierarchy of height $3$, the surfaces in $S_0$ are closed, the spanning surfaces in $S_1$ have boundary, and $S_2$ consists of discs. To simplify notations, we redefine $S_0$ as $\partial M \cup S_0$. 

It is convenient to consider all the surfaces $S_0$, $S_1$, and $S_2$ inside $M$, without cutting $M$ along them.  With this perspective $\partial S_1$ is glued to $S_0$ and $\partial S_2$ is glued to $S_0\cup S_1$, via transverse maps. Every intersection $S_0\cap S_1 \cap S_2$ is a \emph{vertex} as in Figure \ref{hierarchy:fig}-(left). The space $X=S_0\cup S_1 \cup S_2$ is a two-dimensional cell complex whose complement in $M$ is a union of open balls: such an object $X$ is usually called a \emph{spine} for $M$.

We say that our hierarchy of height $3$ is \emph{minimal} if the essential discs in $S_2$ are chosen to minimise the total number of vertices. We can of course suppose that the hierarchy is minimal.

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{hierarchy2-BW}{hierarchy2}}
\nota{If $\gamma$ intersects at most three domains, it bounds a disc $D$ intersecting only these domains, as shown here.}
\label{hierarchy2:fig}
\end{center}
\end{figure}

The final manifold $M_3$ is the abstract closure of $M\setminus (S_0\cup S_1 \cup S_2)$ and consists of balls.
The boundary of every such ball $B$ is tessellated into domains belonging to $S_0$, $S_1$, or $S_2$. Three domains intersect at 3-valent vertices as in Figure \ref{hierarchy:fig}-(right). 
We say that $B$ is \emph{essential} if every simple closed curve $\gamma\subset \partial B$ transverse to the tessellation and intersecting $\leqslant 3$ domains is the boundary of a disc $D\subset \partial B$ intersecting only these domains: see Figure \ref{hierarchy2:fig}. 

\begin{lemma} \label{minimal:essential:lemma}
If the hierarchy is minimal, every ball in $M_3$ is essential.
\end{lemma}
\begin{proof}
Let $\gamma\subset \partial B$ intersect $k\leqslant 3$ domains. The curve $\gamma$ obviously bounds a properly embedded disc $D'\subset B$. 
If $k=1$, the curve is entirely contained in $S_i$ for some $i$. Since $S_0$ and $S_1$ are incompressible and $S_2$ consists of discs, the curve $\gamma$ bounds a disc $D$ also in $S_i$. Since $S_1$ is incompressible and $S_2$ consists of essential discs, the boundary components of $S_j$ with $j>i$ are not attached in the interior of $D$, so $D$ is entirely contained in the domain containing $\gamma$ and we are done.

If $k=2$, the curve $\gamma$ is contained in $S_i\cup S_j$ for some $i<j$. If $(i,j) = (0,1)$ we use that $S_1$ is $\partial$-incompressible to get a disc $D$ as in Figure \ref{hierarchy2:fig}-(top-right). If $j=2$, then $\gamma$ cuts a disc in $S_2$ into two discs $D_1 \cup D_2$. 

We have three half-discs $D', D_1, D_2$ intersecting in an arc, all contained in a handlebody $H\subset M_2$. Recall that $H\setminus S_2$ consists of balls. 
If we replace $D_1\cup D_2$ by either $D_1 \cup D'$ or $D_2 \cup D'$ (say, the first) we still get a disc system that cuts $H$ into balls, and hence another hierarchy. By minimality $D_2=D$ is adjacent to no vertices, \emph{i.e.}~it is as in Figure \ref{hierarchy2:fig}-(top-right) and we are done. 

The case $k=3$ is analogous: the curve $\gamma$ cuts a disc in $S_2$ into two parts $D_1\cup D_2$ and we may replace it with $D_1\cup D'$. By minimality $D_2$ is incident to at most one vertex $v$: we isotope $\gamma$ through $v$ as in Figure \ref{hierarchy3:fig}, and then conclude using the $k=2$ case.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{hierarchy3-BW}{hierarchy3}}
\nota{By minimality the region in $S_2$ is incident to a single vertex and we can slide $\gamma$ through it. Then we resume to the $k=2$ case.}
\label{hierarchy3:fig}
\end{center}
\end{figure}


\subsection{Dehn's Lemma}
Proposition \ref{pi1:prop} says that an orientable connected properly embedded $\pi_1$-injective surface $S\subset M$ with $\chi(S)\leqslant 0$ is incompressible. We can finally prove the converse, at least for closed surfaces.

The following result is often proved as a corollary of a famous topological fact called the \emph{Dehn Lemma}. We do not state Dehn's Lemma here, and we prove directly the following using hierarchies.\index{Dehn lemma}

\begin{teo} \label{incompressible:teo}
Let $M$ be a compact oriented 3-manifold. A connected oriented closed $S\subset M$ with $\chi(S)\leqslant 0$ is incompressible if and only if the induced map $i_*\colon \pi_1(S) \to \pi_1(M)$
is injective.
\end{teo}
\begin{proof}
We know one implication from Proposition \ref{pi1:prop}; here we suppose that $S$ incompressible and prove that $i_*\colon \pi_1(S) \to \pi_1(M)$ is injective. 

The decomposition of $M$ into irreducible and $\partial$-irreducible factors is made by cutting $M$ along 
essential spheres and discs transverse to $S$. Since $S$ is incompressible, we may surger $S$ along these spheres and discs without altering $i_*$, so that $S$ is disjoint from them and hence contained in a single factor. Therefore we may suppose $M$ is irreducible and $\partial$-irreducible. 

Now $M$ contains the incompressible $S$ and is hence Haken. Theorem \ref{hierarchy:teo} furnishes a hierarchy of height $\leqslant 3$. We may suppose that $S_0$ is a maximal system of closed incompressible surfaces containing $S$ and that the hierarchy is minimal. The balls in $M_3$ are essential by Lemma \ref{minimal:essential:lemma}.

Suppose by contradiction that $i_*$ is not injective: there is a loop $\gamma\colon S^1 \to S$ which is homotopically trivial in $M$ but not in $S$. The triviality in $M$ furnishes a continuous map $f\colon D^2 \to M$ which extends $\gamma$. We homotope $f$ to a smooth map, transverse to all the strata of $S_0\cup S_1\cup S_2$.

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Dehn-BW}{Dehn}}
\nota{The counterimage of $S_0\cup S_1 \cup S_2$ along $f$. An edge with label $i$ goes to $S_i$ (unlabelled edges go to $S_0$). Here there is a $0$-gon (\iftoggle{BW}{light grey}{yellow}) and three $2$-gons (\iftoggle{BW}{grey}{green}). The correct notion of $k$-gon should be clear from the picture.}
\label{Dehn:fig}
\end{center}
\end{figure}

By transversality, the counterimage $f^{-1}(S_0\cup S_1 \cup S_2)$ is a graph in $D^2$ as in Figure \ref{Dehn:fig}, which divides $D^2$ into regions. The graph is itself a hierarchy, with edges of type $0,1,2$ attached iteratively.
An easy Euler characteristic argument shows that at least one region $R$ is a $k$-gon with $k\leqslant 3$, see Figure \ref{Dehn:fig}. The region $R$ is mapped inside a ball $B\subset M_3$, and $\partial R$ is mapped to an immersed curve $\alpha\subset\partial B$ intersecting $k\leqslant 3$ domains of the tessellated $\partial B$. 

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{Dehn2-BW}{Dehn2}}
\nota{The immersed curve $\alpha$ intersects $k\leqslant 3$ regions and is hence of one of these types (because $B$ is essential).}
\label{Dehn2:fig}
\end{center}
\end{figure}

Since $B$ is essential, the curve $\alpha$ is of one of the types shown in Figure \ref{Dehn2:fig}. In all cases we may slide the disc $f(R)$ away from $B$ and decrease the number of regions in $D$ by destroying $R$. After finitely many homotopies of this kind we get $f(D)\cap (S_0 \cup S_1 \cup S_2) = \emptyset$ and hence $f(D)$ is entirely contained in a ball $B\subset M_3$. Therefore $\gamma$ is trivial in $S$, a contradiction.
\end{proof}

\begin{cor}
The fundamental group of a Haken manifold is infinite.
\end{cor}
\begin{proof}
It contains the fundamental group of a closed surface with $\chi\leqslant 0$, which is infinite.
\end{proof}
\begin{cor}
Elliptic 3-manifolds are not Haken.
\end{cor}

We will see in the subsequent chapters that every flat 3-manifold is Haken. Hyperbolic 3-manifolds may or may not be Haken.


\subsection{Essential surfaces} \label{essential:subsection}
Topologists sometimes use the term ``essential'' to summarise various reasonable notions in a single word. We already know what an essential disc or sphere is (see Section \ref{essential:discs:subsection}) and we now turn to surfaces with non-positive Euler characteristic. 

Let $M$ be a compact oriented three-manifold and $S\subset M$ be a properly embedded connected compact surface with $\chi(S)\leqslant 0$. We say that $S$ is \emph{essential} if it is incompressible, $\partial$-incompressible, and not $\partial$-parallel.\index{surface!essential surface}


\subsection{Simple manifolds} \label{simple:manifold:subsection}
Let $M$ be irreducible and $\partial$-irreducible. We introduce yet some more definitions. We say that
\begin{itemize}
\item $M$ is \emph{atoroidal} if it does not contain essential tori,
\item $M$ is \emph{acylindrical} if it does not contain essential annuli.
\end{itemize}

Finally, the manifold $M$ is \emph{simple} if it is atoroidal and acylindrical. We can summarise this definition as follows:\index{three-manifold!atoroidal and acylindrical three-manifold}\index{three-manifold!simple three-manifold}

\begin{defn} A compact oriented 3-manifold $M$ with (possibly empty) boundary is \emph{simple} if it does not contain any essential sphere, disc, torus, or annulus.
\end{defn}

Many examples come from elliptic and hyperbolic geometry:

\begin{prop}
Every closed elliptic or hyperbolic 3-manifold $M$ is simple.
\end{prop}
\begin{proof}
We know that $M$ is irreducible. The manifold $M$ does not contain incompressible tori because $\pi_1(M)$ does not contain $\matZ \times \matZ$: if $M$ is elliptic then $\pi_1(M)$ is finite, if it is hyperbolic we use Corollary \ref{no:ZxZ:cor}.
\end{proof}

The flat geometry is an exception: the three-torus $S^1\times S^1\times S^1$ contains many incompressible tori and is hence not simple. For instance, the two-torus $S^1\times S^1 \times p$ is incompressible (because it is $\pi_1$-injective).

Our next goal will be to decompose every irreducible and $\partial$-irreducible manifold $M$ along some canonical set of essential tori and annuli into some pieces. These pieces will be either simple, or belong to a particular class: the \emph{Seifert manifolds}. We introduce this class in the next chapter. 


\subsection{References}
The main sources that we have used for this chapter are an unfinished book of Hatcher \cite{H} and Fomenko--Matveev \cite{FoMa}. The proof of Theorem \ref{incompressible:teo} through hierarchies is due to Aitchison and Rubinstein \cite{AR}.



\chapter{Seifert manifolds} \label{Seifert:chapter}

In the previous chapter we have proved various general theorems on three-manifolds, and it is now time to construct examples. A rich and important source is a family of manifolds built by Seifert in the 1930s, which generalises circle bundles over surfaces by admitting some ``singular'' fibres. The three-manifolds that admit such kind of fibration are now called \emph{Seifert manifolds}. 

In this chapter we introduce and completely classify (up to diffeomorphisms) the Seifert manifolds. In Chapter \ref{eight:chapter} we will then show how to \emph{geometrise} them, by assigning a nice Riemannian metric to each. We will show, for instance, that all the elliptic and flat three-manifolds are in fact particular kinds of Seifert manifolds.


\section{Lens spaces}
We introduce some of the simplest 3-manifolds, the lens spaces. These manifolds (and many more) are easily described using an important three-dimensional construction, called \emph{Dehn filling}.\index{Dehn filling}


\subsection{Dehn filling} \label{Dehn:filling:subsection}
If a 3-manifold $M$ has a spherical boundary component, we can cap it off with a ball. If $M$ has a toric boundary component, there is no canonical way to cap it off: the simplest object that we can attach to it is a solid torus $D\times S^1$, but the resulting manifold depends on the gluing map. This operation is called a \emph{Dehn filling} and we now study it in detail.

Let $M$ be a 3-manifold and $T\subset \partial M$ be a boundary torus component. 
\begin{defn}
A \emph{Dehn filling} of $M$ along $T$ is the operation of gluing a solid torus $D\times S^1$ to $M$ via a diffeomorphism $\varphi\colon \partial D\times S^1 \to T$. 
\end{defn}

The closed curve $\partial D \times \{x\}$ is glued to some simple closed curve $\gamma\subset T$, see Figure \ref{DF:fig}. The result of this operation is a new manifold $M^{\rm fill}$, which has one boundary component less than $M$.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{DF-BW}{DF}}
\nota{The Dehn filling $M^{\rm fill}$ of a 3-manifold $M$ is determined by the unoriented simple closed curve $\gamma \subset T$ to which a meridian $\partial D$ of the solid torus is attached.}
\label{DF:fig}
\end{center}
\end{figure}

\begin{lemma} \label{pq:lemma}
The manifold $M^{\rm fill}$ depends only on the isotopy class of the unoriented curve $\gamma$.
\end{lemma}
\begin{proof}
Decompose $S^1$ into two closed segments $S^1 = I\cup J$ with coinciding endpoints. The attaching of $D\times S^1$ may be seen as the attaching of a 2-handle $D\times I$ along $\partial D \times I$, followed by the attaching of a 3-handle $D\times J$ along its full boundary. 

If we change $\gamma$ by an isotopy, the attaching map of the 2-handle changes by an isotopy and hence gives the same manifold. The attaching map of the 3-handle is irrelevant by Proposition \ref{cap:prop}.
\end{proof}

We say that the Dehn filling \emph{kills} the curve $\gamma$, since this is what really happens on fundamental groups, as we now see. 

The \emph{normaliser} of an element $g\in G$ in a group $G$ is the smallest normal subgroup $N(g) \triangleleft G$ containing $g$. The normaliser depends only on the conjugacy class of $g^{\pm 1}$, hence  the subgroup $N(\gamma)\triangleleft \pi_1(M)$ makes sense without fixing a basepoint or an orientation for $\gamma$.\index{normaliser}

\begin{prop} 
We have
$$\pi_1(M^{\rm fill}) = \pi_1(M) /_{N(\gamma)}.$$
\end{prop}
\begin{proof}
The Dehn filling decomposes into the attachment of a 2-handle over $\gamma$ and of a 3-handle. By Van Kampen, the first operation kills $N(\gamma)$,
and the second leaves the fundamental group unaffected.
\end{proof}

Let a \emph{slope} on a torus $T$ be the isotopy class $\gamma$ of an unoriented homotopically non-trivial simple closed curve.\index{slope} The set of slopes on $T$ was indicated by $\calS$ in Chapter \ref{Teichmuller:chapter}. If we fix a basis $(m, l)$ for $H_1(T,\matZ)=\pi_1(T)$, every slope may be written as $\gamma = \pm (pm + ql)$ for some coprime pair $(p,q)$. Therefore we get a 1-1 correspondence
$$\calS \longleftrightarrow \matQ\cup \{\infty\}$$
by sending $\gamma$ to $\frac pq$. If $T$ is a boundary component of $M$, every number $\frac pq$ determines a Dehn filling of $M$ that kills the corresponding slope $\gamma$. 

Different values of $\frac pq$ typically produce non-diffeomorphic manifolds $M^{\rm fill}$: this is not always true - a notable exception is described in the next section - but it holds in ``generic'' cases.


\subsection{Lens spaces}
The simplest manifold that can be Dehn-filled is the solid torus $M=D\times S^1$ itself. The oriented \emph{meridian} $m=S^1 \times \{y\}$ and \emph{longitude} $l=\{x\}\times S^1$ form a basis for $H_1(\partial M,\matZ)$.\index{meridian and longitude}

\begin{defn} The \emph{lens space} $L(p,q)$ is the result of a Dehn filling of $M=D\times S^1$ that kills the slope $qm+pl$.\index{lens space}
\end{defn}

A lens space is a three-manifold that decomposes into two solid tori. We have already encountered lens spaces in the more geometric setting of Section \ref{lens:subsection}, and we will soon prove that the two definitions are coherent. Since $L(p,q)=L(-p,-q)$ we usually suppose $p\geqslant 0$.

\begin{ex}
We have $\pi_1\big(L(p,q)\big) = \matZ/_{p\matZ}$. 
\end{ex}

\begin{prop}
We have $L(0,1) = S^2\times S^1$ and $L(1,0) = S^3$.
\end{prop}
\begin{proof}
The lens space $L(0,1)$ is obtained by killing $m$, that is by mirroring $D\times S^1$ along its boundary. The lens space $L(1,0)$ is $S^3$ because the complement of a standard solid torus in $S^3$ is another solid torus, with the roles of $m$ and $l$ exchanged (exercise).
\end{proof}

\begin{ex} \label{fill:T:ex}
Every Dehn filling of one component of the product $T\times [0,1]$ is diffeomorphic to $D\times S^1$. Therefore by Dehn-filling both components of $T\times [0,1]$ we get a lens space.
\end{ex}

The solid torus $D\times S^1$ has a non-trivial self-diffeomorphism 
$$(x, e^{i\theta}) \longmapsto (xe^{i\theta}, e^{i\theta})$$
called a \emph{twist} along the disc $D\times \{y\}$. The solid torus can also be \emph{mirrored} via the map
$$(x,e^{i\theta}) \longmapsto (x,e^{-i\theta}).$$

\begin{ex} \label{pqpq:ex}
We have $L(p,q)\isom L(p,q')$ if $q' \equiv \pm q^{\pm 1}$ (mod $p$).
\end{ex}
\begin{proof}[Hint]
Twist, mirror, and exchange the two solid tori giving $L(p,q)$.
\end{proof}

\begin{rem}
The meridian $m$ of the solid torus $M=D\times S^1$ may be defined intrinsically as the unique slope in $\partial M$ that is homotopically trivial in $M$. The longitude $l$ is \emph{not} intrinsically determined: a twist sends $l$ to $m+l$. The solid torus contains infinitely many non-isotopic longitudes, and there is no intrinsic way to choose one of them.
\end{rem}


\subsection{Equivalence of the two definitions}
When $p>0$, we have defined the lens space $L(p,q)$ in two different ways: as the $(q,p)$-Dehn filling of the solid torus, and as an elliptic manifold in Section \ref{lens:subsection}. In the latter description we set
$$\omega = e^{\frac{2\pi i}p}, \qquad f(z,w) = (\omega z, \omega^qw)$$ 
and define $L(p,q)$ as $S^3/_\Gamma$ where $\Gamma = \langle f \rangle$ is generated by $f$. We now show that the two definitions produce the same manifolds.

\begin{prop}
The manifold $S^3/_{\langle f \rangle}$ is the $(q,p)$-Dehn filling of the solid torus.
\end{prop}
\begin{proof}
The isometry $f$ preserves the central torus 
$$T = \big\{(z,w)\ \big|\ |z|=|w| = \tfrac {\sqrt 2}2 \big\}$$
that divides $S^3$ into two solid tori
\begin{align*}
N^1 & = \big\{(z,w)\ \big|\ |z| \leqslant \tfrac {\sqrt 2}2,\ |w| = \sqrt{1-|z|^2}\big\}, \\
N^2 & = \big\{(z,w)\ \big|\ |w| \leqslant \tfrac {\sqrt 2}2,\ |z| = \sqrt{1-|w|^2}\big\}.
\end{align*}
Identify $T$ with $S^1\times S^1 = \matR^2/_{\matZ^2}$ in the obvious way, so that  $H_1(T) = \matZ \times \matZ$. The meridians of $N^1$ and $N^2$ are $(1,0)$ and $(0,1)$. The isometry $f$ act on $T$ as a translation of vector $v=\big(\frac 1p, \frac qp\big)$. The quotient $T/_{\langle f\rangle}$ is again a torus, with fundamental domain the parallelogram generated by $v$ and $w=(0,1)$.

The quotients $N^1/_{\langle f \rangle}$, and $N^2/_{\langle f \rangle}$ are again solid tori. Therefore $S^3/_{\langle f \rangle}$ is also a union of two solid tori. Their meridians are the projections of the horizontal and vertical lines in $\matR^2$ to $T/_{\langle f \rangle} = \matR^2/_{\langle v,w \rangle}$. In the basis $(v,w)$ these meridians are $pv -qw$ and $w$ respectively. Therefore $S^3/_{\langle f\rangle}$ is a $(-q,p)$-Dehn filling on the solid torus, which is diffeomorphic to the $(q,p)$-Dehn filling by mirroring the solid torus.
\end{proof}

\begin{cor}
We have $L(1,0) = S^3$ and $L(2,1) = \matRP^3$.
\end{cor}
\begin{proof}
We have $f = \id$ and $f=-\id$, correspondingly.
\end{proof}


\subsection{Classification of lens spaces}
Which lens spaces are diffeomorphic? It is not so easy to answer this question, because many lens spaces like $L(5,1)$ and $L(5,2)$ have the same homotopy and homology groups, while there is no evident diffeomorphism between them. 
A complete answer was given by Reidemeister in 1935, who could distinguish lens spaces using a new invariant, now known as the \emph{Reidemeister torsion}.\index{Reidemeister torsion} More topological proofs were discovered in th 1980s by Bonahon and Hodgson. We follow here Hatcher \cite{H}.

\begin{teo} \label{Lpq:teo}
The lens spaces $L(p,q)$ and $L(p',q')$ are diffeomorphic $\Longleftrightarrow$ $p=p'$ and $q' \equiv \pm q^{\pm 1}$ (mod $p$).
\end{teo}
\begin{proof}
We may suppose $p>1$.
Exercise \ref{pqpq:ex} furnishes one implication, so we start with a lens space $L(p,q)$ and we prove that there is (up to isotopy) only one torus $T$ dividing $L(p,q)$ into two solid tori: this fact then implies that one can recover $p$ and $q$ intrinsically from $L(p,q)$, up to the stated ambiguity for $q$ (which depends on the chosen longitudes and orientations, and changes by switching the solid tori). So we suppose that there is another torus $T'$.

Let $\Sigma$ be the core circle of one solid torus adjacent to $T'$. If we can isotope $\Sigma$ inside the torus $T$, we are done: in that case $T'$ is isotopic to the boundary of a small tubular neighbourhood of $\Sigma$, hence both $T$ and $T'$ are cut into two annuli $T = A_1 \cup A_2$ and $T' = A_1' \cup A_2'$ such that $\Sigma \subset A_1$, all four annuli share the same boundaries, and $A_2$ is contained in the large outside solid torus bounded by $T'$; the annulus $A_2$ is incompressible in this solid torus by Proposition \ref{pi1:prop} (otherwise $\Sigma$ would be homotopically trivial, contradicting $p>1$) and hence $\partial$-parallel by Proposition \ref{incompressible:solid:torus:prop}, so it is isotopic to either $A_1'$ or $A_2'$, suppose to $A_2'$; since $A_1$ is clearly isotopic to $A_1'$ we conclude that $T$ and $T'$ are isotopic.

Our aim is now to prove that $\Sigma$ can be isotoped inside $T$. To this purpose we construct two different objects from $T'$ and $T$, a \emph{spine} $\Delta$ and a \emph{foliation} $\calF$. The spine $\Delta\subset M$ is built by adding to $\Sigma$ the meridian $D$ of the other solid torus incident to $T'$, enlarged so that $\partial D$ is glued along $\Sigma$ like a degree-$p$ covering. Note that $M\setminus \Delta$ is an open ball.

We construct the foliation $\calF$ of $M$ by subdividing each solid torus bounded by $T$ into concentric tori, with a central singular circle in each. We represent $\calF$ as the level sets of a map $f\colon L(p,q) \to [0,1]$ where the singular circles are the extreme levels $f^{-1}(0)$ and $f^{-1}(1)$.

We now put $\Delta$ in some good position with respect to $\calF$. We first perturb $\Sigma$ so that it is disjoint from the singular circles of $\calF$ and $f|_\Sigma$ is a Morse function with singular points in distinct levels. At every local maximum (minimum) of $f|_\Sigma$ we isotope $\Delta$ so that the $p$ sheets of $\Delta$ lie above (below) $\Sigma$ as in Figure \ref{sheets_above:fig}. Finally, we require $\Delta$ to be transverse to the two singular circles of $\calF$ and $f|_{\Delta \setminus \Sigma}$ to be a Morse function, with critical points at distinct levels (also distinct from those of the critical points of $f|_\Sigma$).

\begin{figure}
\begin{center}
\includegraphics[width = 3 cm] {sheets_above}
\nota{We require the $p$ sheets of the spine $\Delta$ to lie above every local maximum for $f|_\Sigma$.}
\label{sheets_above:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{lens_singular-BW}{lens_singular}}
\nota{The singular points in $D$ can be centres (top left), saddles (top right) and half-saddles (bottom).}
\label{lens_singular:fig}
\end{center}
\end{figure}

The foliation $\calF$ induces a singular foliation on $\Delta$ that pulls back to $D$ via the map $D\to \Delta$. There are three types of singular points in the foliation, shown in Figure \ref{lens_singular:fig}: centres, saddles, and half-saddles.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{lens_leaves-BW}{lens_leaves}}
\nota{A singular leaf exiting from a singular point may be of one of these kinds. The dots in (e) indicate that there might be another half-saddle at the other endpoint: this is because there are half-saddles at the same level (precisely $p$ for every local maximum or minimum for $f|_\Sigma$).}
\label{lens_leaves:fig}
\end{center}
\end{figure}

A leaf in $D$ incident to a singular point is \emph{singular}. Since we minimised the critical points that may stay at the same level, the singular leaves exiting from a singular point may be only of the six possible kinds shown in Figure \ref{lens_leaves:fig}.  
The saddles and half-saddles of type (a) and (e) are called \emph{essential}, and the others \emph{inessential}.
In (a) the singular leaves divide $D$ into four \emph{quarter discs}, and in (e) they cut off two or more \emph{half discs}.

Among all possible good configurations of $\Delta$, we pick one that minimises first the number of critical points in $f|_\Sigma$, and second the number of essential saddles.

Let $D' \subset D$ be a quarter or half-disc not containing any smaller quarter or half-disc. Define $\alpha = D' \cap \partial D$. Suppose first that $D'$ is a half-disc and both endpoints of $\alpha$ are singular. The singular disc $D'$ can contain some singular point of type (b), and it certainly contains one singular point of type (f), see Figure \ref{lens_leaves1:fig}-(left). (It contains no other singular point except these.) The image of $D'$ in $\Delta$ is shown in Figure \ref{lens_leaves1:fig}-(right). In this case we can slide $\alpha$ along $D'$ to the \iftoggle{BW}{light grey}{green} arc shown in the figure which lies entirely in a level torus of $f$. If we could do this for all the arcs of $\partial D$ cut by singular points, we would happily isotope $\Sigma$ inside a torus level and hence into $T$, and we would be done.

There are however two other cases to consider, and both will be excluded by our minimality assumption on $\Delta$. One is that $D'$ may be a half-disc with only one singular endpoint for $\alpha$, as in Figure \ref{lens_leaves2:fig}. In that case we can isotope $\alpha$ to the \iftoggle{BW}{light grey}{green} curve through $D'$, dragging the spine $\Delta$ behind. In the new configuration $f|_\Sigma$ has strictly less critical points, a contradiction.

\begin{figure}
\begin{center}
\includegraphics[width = 8.5 cm] {\iftoggle{BW}{lens_leaves1-BW}{lens_leaves1}}
\nota{The disc $D'$ is a half-disc and $\alpha$ is incident to two singular points.}
\label{lens_leaves1:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 8.5 cm] {\iftoggle{BW}{lens_leaves2-BW}{lens_leaves2}}
\nota{The disc $D'$ is a half-disc and $\alpha$ is incident to one singular point.}
\label{lens_leaves2:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{lens_leaves3-BW}{lens_leaves3}}
\nota{The disc $D'$ is a quarter disc.}
\label{lens_leaves3:fig}
\end{center}
\end{figure}

In the last case $D'$ is a quarter disc as in Figure \ref{lens_leaves3:fig} and we can isotope $\alpha$ to the \iftoggle{BW}{light grey}{green} curve dragging $\Sigma$ as above, but more carefully: we enlarge the other $p-1$ sheets of $\Delta$ by parallel copies of $D'$. In the new configuration the number of critical points in $f|_\Sigma$ is unchanged, but there are strictly fewer essential saddles: at least one is destroyed and no new one is created. (Note that many inessential saddles may be created.) This is also excluded.
\end{proof}

We have discovered, in particular, that there are closed three-manifolds like $L(5,1)$ and $L(5,2)$ that are not diffeomorphic, although their fundamental groups are both isomorphic to $\matZ/_{5\matZ}$; the two manifolds are both covered by $S^3$, so they also have isomorphic higher homotopy groups.
