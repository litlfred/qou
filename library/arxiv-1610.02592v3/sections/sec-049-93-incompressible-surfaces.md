---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-049-93-incompressible-surfaces
section_title: "Incompressible surfaces"
section_number: 9.3
pages: 295-302
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.913
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We have proved that every compact oriented 3-manifold decomposes along essential spheres and discs, into some canonical pieces that do not contain essential spheres or discs anymore. 

We would like to pursue this strategy with the next simplest surfaces, namely tori and annuli. To this purpose we define the important notion of \emph{incompressible} surface in a three-manifold, which applies to all surfaces of non-positive Euler characteristic.


\subsection{Incompressible surfaces}
Throughout all this section $M$ denotes a compact orientable 3-manifold with (possibly empty) boundary. Let $S\subset M$ be a properly embedded orientable surface. A \emph{compressing disc} for $S$ is a disc $D\subset M$ with $\partial D = D \cap S$, such that $\partial D$ does not bound a disc in $S$. With this hypothesis, the surgery in Figure \ref{incompressible:fig} is called a \emph{compression}: it transform $S$ into a new surface $S'\subset M$ which is simpler than $S$.\index{compressing disc}

\begin{prop}  \label{S':simpler:prop}
The surface $S'$ may have one or two components $S_i'$, and $\chi(S_i')>\chi(S)$ for each component. 
\end{prop}
\begin{proof}
We have $\chi(S') = \chi(S) + 2$. If $S'$ has one component we are done, so suppose $S' = S_1' \sqcup S_2'$. Since $\partial D$ did not bound a disc in $S$, no $S_i'$ is a sphere, hence $\chi(S_i')\leqslant 1$ that implies $\chi(S_i')> \chi(S)$ for $i=1,2$.
\end{proof}

A properly embedded connected orientable compact surface $S\subset M$ with $\chi(S)\leqslant 0$ is \emph{compressible} if it has a compressing disc, and \emph{incompressible} otherwise. See Figure \ref{incompressible3:fig}-(top).\index{surface!compressible and incompressible surface} 

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{incompressible3-BW}{incompressible3}}
\nota{A surface $S$ is incompressible ($\partial$-incompressible) if the existence of a disc $D$ as in the top-left (bottom-left) picture implies the existence of another disc $D'\subset S$ as in the top-right (bottom-right) picture. If in addition $M$ is irreducible ($\partial$-irreducible) the two discs $D$ and $D'$ form a sphere (disc) which bounds a ball (is $\partial$-parallel), and hence by substituting $D'$ with $D$ we get two isotopic surfaces.}
\label{incompressible3:fig}
\end{center}
\end{figure}



\begin{cor} Let $S\subset M$ be any properly embedded orientable surface. After compressing it a finite number of times it transforms into a disjoint union of spheres, discs, and incompressible surfaces.
\end{cor}
\begin{proof}
We compress $S$ as much as we can; after finitely many steps we must stop because of Proposition \ref{S':simpler:prop}.
\end{proof}

\begin{rem}
By definition, an orientable 3-manifold is $\partial$-irreducible if and only if its boundary consists of incompressible components. (Strictly speaking, a boundary component is not properly embedded and hence cannot be incompressible: we implicitly push it inside the 3-manifold.)
\end{rem}

A simple incompressibility criterion is the following.

\begin{prop} \label{pi1:prop}
Let $S\subset M$ be an orientable, connected, properly embedded surface with $\chi(S)\leqslant 0$. If the map $\pi_1(S) \to \pi_1(M)$ induced by inclusion is injective, then $S$ is incompressible.
\end{prop}
\begin{proof}
Suppose that a disc $D$ compresses $S$. Its boundary $\partial D$ is a non-trivial element in $\pi_1(S)$ because it does not bound a disc in $S$ by Proposition \ref{disco:prop}, but is clearly trivial in $\pi_1(M)$: a contradiction.
\end{proof}

The converse is also true, but its proof is much harder! We will complete it at the end of this chapter. For the moment we content ourselves with the following.

\begin{prop} \label{incompressible:boundary:prop}
If $S\subset M$ is incompressible, every component of $\partial S$ is non-trivial in $\partial M$.
\end{prop}
\begin{proof}
If a component of $\partial S$ is trivial in $\partial M$, it bounds a disc $D\subset \partial M$ there. By taking an innermost one we get $D\cap S = \partial D$, and by pushing $D$ inside $M$ we find a compressing disc for $S$.
\end{proof}


\subsection{Tori}
The first closed surface to look at is the torus.

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{torus-BW}{torus}}
\nota{A torus in an irreducible 3-manifold is either incompressible, or it bounds a solid torus (left), or is contained in a ball (right).}
\label{torus_irred:fig}
\end{center}
\end{figure}

\begin{prop} \label{T:M:prop}
Let $T\subset M$ be a torus in an irreducible 3-manifold. One of the following holds:
\begin{enumerate}
\item $T$ is incompressible,
\item $T$ bounds a solid torus,
\item $T$ is contained in a ball.
\end{enumerate}
\end{prop}
\begin{proof}
If $T$ is not incompressible, it compresses along a disc $D$. The result of the compression is necessarily a sphere $S\subset M$ which bounds a ball $B$ since $M$ is irreducible. If $B$ is disjoint from $T$, then $T$ bounds a solid torus as in Fig.\ref{torus_irred:fig}-(left). If $B$ contains $T$, then case (3) holds as shown in Figure \ref{torus_irred:fig}-(right).
\end{proof}

If $M=S^3$ the case (3) can be excluded: if $T$ is contained in a ball $B$, then it bounds a solid torus ``on the outside'' using the complementary ball $S^3\setminus B$. We will also exclude the case (1) when we show that $S^3$ contains no incompressible surfaces.


\subsection{$\partial$-incompressible surfaces}
There is of course also a $\partial$-version of incompressibility. Let $S\subset M$ be a properly embedded orientable surface in a 3-manifold $M$. A \emph{$\partial$-compressing disc} for $S$ is a disc $D$ with $\partial D = \alpha \cup \beta$, where $\alpha$ lies in $S$ and $\beta$ in $\partial M$ as in Figure \ref{incompressible2:fig}-(left); we also require that there is no sub-disc $D'\subset S$ with $\partial D' = \alpha\cup \beta' $ and $\beta'\subset\partial S$. 
The move in Figure \ref{incompressible2:fig} is a \emph{$\partial$-compression} and transforms $S$ into a surface $S'\subset M$ simpler than $S$:

\begin{prop}
The surface $S'$ may have one or two components $S_i'$, and $\chi(S_i')>\chi(S)$ for each component. 
\end{prop}
\begin{proof}
We have $\chi(S') = \chi(S) + 1$. If $S'$ has one component we are done, so suppose $S' = S_1' \sqcup S_2'$. Since $\alpha$ did not bound a disc in $S$, no $S_i'$ is a disc, hence $\chi(S_i')\leqslant 0$ that implies $\chi(S_i')> \chi(S)$ for $i=1,2$.
\end{proof}

A properly embedded connected orientable compact $S\subset M$ with $\chi(S)\leqslant 0$ is \emph{$\partial$-compressible} if it has a $\partial$-compressing disc, and \emph{$\partial$-incompressible} otherwise. See Figure \ref{incompressible3:fig}.\index{surface!$\partial$-compressible and $\partial$-incompressible surface}

\begin{cor} Let $S\subset M$ be any properly embedded orientable surface. After $\partial$-compressing it a finite number of times it transforms into a disjoint union of spheres, discs, and $\partial$-incompressible surfaces.
\end{cor}


\subsection{Annuli}
The first non-closed surface to look at is the annulus. Let a \emph{tube} be the tubular neighbourhood of a properly embedded arc.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{annulus-BW}{annulus}}
\nota{An annulus $A$ in an irreducible and $\partial$-irreducible 3-manifold is either incompressible and $\partial$-incompressible, or is parallel to an annulus in $\partial M$ (left), or bounds a tube (centre), or is contained in a ball intersecting $\partial M$ in a disc (right).}
\label{annulus:fig}
\end{center}
\end{figure}

\begin{prop} \label{A:M:prop}
Let $A\subset M$ be a properly embedded annulus in an irreducible and $\partial$-irreducible 3-manifold. One of the following holds:
\begin{enumerate}
\item $A$ is incompressible and $\partial$-incompressible,
\item $A$ bounds a tube,
\item $A$ is parallel to an annulus in $\partial M$,
\item $A$ is contained in a ball $B$ intersecting $\partial M$ in a disc.
\end{enumerate}
\end{prop}
\begin{proof}
If $A$ compresses along a disc $D$, it transforms into two discs that are parallel to two discs $D_1, D_2 \subset \partial M$ since $M$ is $\partial$-irreducible. If $D_1\cap D_2 = \emptyset$ then $A$ bounds a tube as in Figure \ref{annulus:fig}-(right); if $D_1 \subset D_2$ then $A$ is contained in a ball $B$ intersecting $\partial M $ in $D_2$.

 If $A$ $\partial$-compresses along a disc $D$, it transforms into a disc which is again $\partial$-parallel and hence $A$ is as in Figure \ref{annulus:fig}-(left) or bounds a tube.
\end{proof}

As a corollary, we get a simple criterion for detecting incompressible and $\partial$-incompressible annuli:

\begin{cor} \label{A:non-parallel:cor}
Let $A\subset M$ be a properly embedded annulus in an irreducible and $\partial$-irreducible 3-manifold. If the components of $\partial A$ are non-trivial and non-parallel in $\partial M$, the annulus $A$ is incompressible and $\partial$-incompressible.
\end{cor}


\subsection{Handlebodies}
We study some examples. We investigate the incompressible and $\partial$-incompressible surfaces in the three-sphere and in the handlebodies. Recall that a ($\partial$)-incompressible surface is always compact, orientable, connected, properly embedded, and with non-positive Euler characteristic by hypothesis.

\begin{prop}
There are no incompressible surfaces in $\matR^3$.
\end{prop}
\begin{proof}
Let $S$ be a surface in $\matR^3$. By applying as is the proof of Alexander Theorem \ref{Alexander:teo} we find that $S$ transforms into spheres after surgerying along discs. Therefore $S$ compresses somewhere.
\end{proof}

A high genus closed surface may be embedded in $\matR^3$ in a rather complicated way (which may be hard to imagine) and the proposition says that no matter how intricate the surface is, there is always a compressing disc somewhere that one can use to simplify the picture. After finitely many compressions the complicated surface is atomised into some trivial spheres. 

\begin{cor} \label{no:inc:B:cor}
There are no incompressible surfaces in $S^3$.
\end{cor}
\begin{cor} \label{B:cor}
There are no incompressible surfaces in the ball $B$.
\end{cor}
\begin{proof}
Use Proposition \ref{incompressible:boundary:prop}.
\end{proof}

\begin{cor}
Every torus in $S^3$ bounds a solid torus and every properly embedded annulus in $B$ bounds a tube.
\end{cor}
\begin{proof}
Apply Propositions \ref{T:M:prop} and \ref{A:M:prop}. Since the manifold is $S^3$ or $B$, the cases (3) or (4) easily imply (2).
\end{proof}

The solid torus in $S^3$ and the tube in $B$ may of course be knotted! We now turn to handlebodies. Recall that a handlebody of genus $g\geq 1$ is irreducible by Corollary \ref{handle:irr:cor}, but it is clearly not $\partial$-irreducible.

\begin{prop}[Handlebodies] \label{handlebodies:prop}
The genus-$g$ handlebody $H_g$ contains no incompressible and $\partial$-incompressible surfaces.
\end{prop}
\begin{proof}
Suppose that $S\subset H_g$ is incompressible and $\partial$-incompressible. Pick disjoint essential discs $D_1,\ldots, D_g$ that cut $H_g$ into a ball $B$. Put $S$ in transverse position with respect to $\sqcup_i D_i$, so that the intersection of $S$ with $\sqcup_i D_i$ consists of circles and properly embedded arcs. Since $H_g$ is irreducible and $S$ is incompressible and $\partial$-incompressible, all these intersections can be removed by an isotopy of $S$, as explained below. Then Corollary \ref{B:cor} gives a contradiction.

The intersections removal goes as follows. Let $\alpha$ be one arc or circle in $S \cap D_j$. Since $S$ is incompressible and $\partial$-incompressible, there is a disc $D'\subset S$ bounded by $\alpha$ (if $\alpha$ is a circle) or by $\alpha \cup \beta$ with $\beta\subset \partial S$ (if $\alpha$ is an arc) as in Figure \ref{incompressible3:fig}. After substituting $\alpha$ with an innermost intersection of $D'$ with $\sqcup_i D_i$ we may suppose that $D'$ is entirely contained in $B$ and hence we may eliminate $\alpha$ with an isotopy as explained in Figure \ref{incompressible3:fig}. 
\end{proof}

We can be more specific on the solid torus $H_1$.

\begin{prop} \label{incompressible:solid:torus:prop}
Every incompressible surface in a solid torus is a $\partial$-parallel annulus.
\end{prop}
\begin{proof}
Every incompressible surface $S\subset H_1$ is $\partial$-compressible by Proposition \ref{handlebodies:prop}. If we $\partial$-compress it, we get either a disc or an incompressible surface again. Therefore $S$ is constructed iteratively from some discs by a sequence of moves opposite to the $\partial$-compression, that produce incompressible surfaces at each step. 
One easily sees that the only incompressible surface that this move can produce at the first step is a $\partial$-parallel annulus (from a single disc), and then one gets stuck.
\end{proof}

\begin{warning}
The handlebody $H_2$ contains many complicated properly embedded incompressible surfaces! However, these are all $\partial$-compressible. The main difference between $H_1$ and $H_2$ is that $\pi_1(H_2)=\matZ*\matZ$ is a free group of rank two and contains many free groups of arbitrarily high rank, so there is a lot of space for $\pi_1$-injective incompressible surfaces in $H_2$ with boundary (whose fundamental group is free).
\end{warning}


\subsection{Line bundles}
We now turn to product line bundles. Recall that $S_g$ is the closed orientable surface of genus $g$. 

\begin{prop}[Line bundles] \label{line:bundles:prop}
Fix $g\geqslant 1$. The product $M=S_g\times [-1,1]$ is irreducible and $\partial$-irreducible. The incompressible and $\partial$-incompressible surfaces in $M$ are precisely the following (up to isotopy):
\begin{itemize}
\item the \emph{horizontal} surface $S_g\times 0$,
\item a \emph{vertical} annulus $\gamma \times [-1,1]$ for each non-trivial simple closed curve $\gamma\subset S_g$.
\end{itemize}
\end{prop}
\begin{proof}
We know that $M$ is irreducible by Proposition \ref{product:irr:prop}. The horizontal surface and the vertical annuli are both incompressible and $\partial$-incompressible by 
Propositions \ref{pi1:prop} and \ref{A:non-parallel:cor}. Propositions \ref{pi1:prop} also shows that $M$ is $\partial$-irreducible.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{prisms-BW}{prisms}}
\nota{A move that decreases the intersection number of $S$ with the vertical edges (left). The surface $S$ intersects every prism into horizontal triangles (centre) or vertical rectangles (right).}
\label{prisms:fig}
\end{center}
\end{figure}

We now prove that every incompressible and $\partial$-incompressible $S$ is either vertical or horizontal, up to isotopy. We use a version of normal surface theory, with prisms instead of tetrahedra. 

A triangulation $\Delta$ of $S_g$ determines a decomposition of $S_g\times [-1,1]$ into prisms. Every vertex $v$ of $\Delta$ gives rise to a vertical edge $e=v\times [-1,1]$. We suppose that $S$ is transverse to the prisms and has minimum intersection number with the vertical edges. The intersection of $S$ with a vertical rectangular face consists of arcs and circles. The simplification argument described below shows that after an isotopy we get only horizontal or vertical arcs (that is, arcs joining opposite sides of the rectangle).
By further isotopies we can also supppose that $S$ intersects every horizontal triangle of the prism into arcs joining distinct sides. Therefore $S$ intersects necessarily every prism into either horizontal triangles or vertical rectangles as in Figure \ref{prisms:fig}-(centre) and (right). These pieces glue up to give a horizontal or vertical surface.

Here is the simplification argument. There cannot be arcs with endpoints in two consecutive edges, because they could be removed by an isotopy as in Figure \ref{prisms:fig}-(left) contradicting minimality. Analogously there are no arcs with both endpoints in the same vertical edge. Circles and arcs with endpoints in the same horizontal edge are removed as in the proof of Proposition \ref{handlebodies:prop}.  
\end{proof}
