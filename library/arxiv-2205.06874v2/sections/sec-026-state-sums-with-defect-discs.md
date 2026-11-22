---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-026-state-sums-with-defect-discs
section_title: "State sums with defect discs"
section_number: null
pages: 44-48
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.978
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
To prove the triangulation independence of the state sum, we first show that the state sums of 3-balls $M$ that shell to fine neighbourhoods of defect 
discs $D$ are given as cyclic evaluations of certain polygon diagrams. 

These polygon diagrams are obtained by projecting the dual graphs of the boundary triangulations on $\partial M$ to the defect disc. As  $M$ is PL homeomorphic to $[0,1]\times D$ via an orientation preserving PL homeomorphism  $\phi: M\to [0,1]\times D$ by Lemma \ref{lem:finenbtop}, this projection is given by Definition \ref{def:projection}. Lemma \ref{lem:projiso} ensures that different choices of $\phi$ yield graphs on $D$ that are related by isotopies.


\begin{proposition}\label{th:topological invariance}
Let $M$ be a 3-manifold with defect data that shells to a fine neighbourhood 
 of  a defect disc $D$ by  shellings with tetrahedra that do not intersect $D$. 
Then for all labelings  $l_{\partial M}$, $b_{\partial M}$  as in Definition \ref{def:statesum}  
$$
\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\ev(P),
$$
where 
$\ev(P)$ is
the cyclic evaluation of the polygon diagram $P$ obtained by
\begin{compactitem}
\item projecting the dual graph of the boundary triangulation on $\partial M$ to $D$,
\item labeling the edges and vertices of the resulting diagram with the data  assigned by $l_{\partial M}$ and $b_{\partial M}$.
\end{compactitem}
\end{proposition}


\begin{proof}  
1.~We first suppose that $M$ is a fine neighbourhood of the defect disc $D$ and prove the claim by induction over the number of tetrahedra in the triangulation. For a single tetrahedron, this holds by definition of the generalised 6j symbol, see Figure \ref{fig:projecting}, and of the rescaled state sum. 

Any fine neighbourhood $M$ of $D$ with $n+1$ tetrahedra is obtained by gluing a single tetrahedron $t$ to a fine neighbourhood $M'$ of $D$ with $n$ tetrahedra.  
This follows, because  the triangulation of $M$ defines a cell complex structure on $D$ and 
 every cell decomposition of a disc is shellable, see for instance Sanderson \cite[Lemma 1]{S}. Shellings of the defect disc correspond to 3d shellings of its fine neighbourhood $M$.  
 
 The tetrahedron $t$ can be glued to $M'$ either along one or two faces. Gluing along three faces is not possible, as $t$ intersects $D$ either in three edges incident at a common vertex as in Figure \ref{fig:dectet} (a)  or in all except two opposite edges as in Figure \ref{fig:dectet} (b). The first case would yield a contradiction to the assumption that the defect surfaces in $M$ and $M'$ are both discs. In the second case there would be an internal  edge in $M$ common to two glued faces that does not intersect $D$, contradicting that
 $M$ is a fine neighbourhood of $D$.  
 
 
 
 By Corollary \ref{cor:gluing}, formula \eqref{eq:rescstate} and the induction hypothesis, the rescaled state sum for $M$ is
\begin{align}\label{eq:indstate}
\mathcal Z'(M, l_{\partial M}, b_{\partial M})
=\sum_{l}\sum_{b_g}
\prod_{e\in E_g} \dim l(e) \ev(P')\, \mathrm{6j}(t,l,b),
\end{align}
where 
\begin{compactitem}
\item $\ev(P')$ denotes the cyclic evaluation of the  corresponding polygon diagram for $M'$,  
\item $E_{g}$ is the set of internal edges in $M$ that correspond to boundary edges of $t$ and $M'$,
\item the sum $\Sigma_{l}$ runs over all labelings of edges in $E_g$ with simple objects in the chosen sets of representatives,
\item  the sum $\Sigma_{b_g}$ runs over bases of the morphism spaces for glued faces of $t$ and $M'$. 
\end{compactitem}
We compute the sum in \eqref{eq:indstate} depending on the number of glued faces of $t$:
 
 (i) If $t$ is glued to $M'$ along a single face $f$, then $E_g=\emptyset$.  
Identity \eqref{pic:gluepoly}  implies that the sum in \eqref{eq:indstate} is given by
$$\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\sum_{b_f} \ev(P')\, \mathrm{6j}(t,l,b)\stackrel{\eqref{pic:gluepoly}}=\ev(P).$$
(ii) If $t$ is glued to $M'$ along two faces $f,f'$ that share an edge $e$, then $E_g=\{e\}$ and $e$ intersects $D$.  Otherwise, $t$ would have to intersect 
$D$ in four edges, as in Figure \ref{fig:dectet} (b). As the intersections of the defect disc in $t$ with $f$ and $f'$ are both glued to the boundary of the defect disc in $M'$, 
the defect surface $D$ could not be a disc. 


We apply  identity \eqref{pic:gluepoly}  to 
 glue $t$ on $M'$ along $f$. This yields a polygon diagram $P''$ with the morphisms for $f'$ assigned to adjacent sides of $P''$ that are separated by a vertex labeled $l(e)$. 
Identity \eqref{pic:closepoly} implies that the state sum 
 in \eqref{eq:indstate} is given by
$$
\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\sum_{l(e)} \sum_{b_f, b_{f'}} \dim l(e)\, \ev(P')\, \mathrm{6j}(t,l,b)\stackrel{\eqref{pic:gluepoly}}=\sum_{l(e)} \sum_{b_{f'}} \dim l(e) \ev(P'') \stackrel{\eqref{pic:closepoly}}=\ev(P).
$$
This proves the claim for the case where $M$ is a fine neighbourhood of the defect disc.

2.~Suppose now that $M$ is obtained from a fine neighbourhood of the defect disc by inverse shellings with tetrahedra that do not intersect $D$. We prove the claim by induction over the number $n$ of tetrahedra in the triangulation that  do not intersect $D$. If $n=0$ the claim holds by 1.  

If $M$ contains $n+1$ tetrahedra that do not intersect $D$, then $M$ is obtained by gluing a tetrahedron $t$ that does not intersect $D$ to a defect 3-manifold $M'$ with $n$ tetrahedra that do not intersect $D$ and also satisfies the assumptions. If $t$  is contained in a region labeled by a spherical fusion category  $\mac$, then 
by Corollary \ref{cor:gluing} and the induction hypothesis, the rescaled state sum for $M$ is  given by
\begin{align}\label{eq:indstate2}
\mathcal Z'(M, l_{\partial M}, b_{\partial M})=
\sum_{l}\sum_{b_g}
\frac{ \prod_{e\in E_g} \dim l(e)}{\dim \mac^{v_g}}\, \ev(P')\, \mathrm{6j}(t,l,b),
\end{align}
where the notation is as in \eqref{eq:indstate} and $v_g\in\{0,1\}$ is the number of internal vertices in $M$ that correspond to boundary vertices of $t$ and $M'$.
We  compute the sum in \eqref{eq:indstate2} depending on the number of glued faces of $t$:

(i) If $t$ is glued to $M'$ along a single face $f$, then $E_g=\emptyset$ and $v_g=0$. 
Identity \eqref{pic:insert}  then implies that the state sum in \eqref{eq:indstate2} is given by
$$\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\sum_{b_f} \ev(P')\, \mathrm{6j}(t,l,b)\stackrel{\eqref{pic:insert}}=\ev(P).$$
(ii) If $t$ is glued to $M'$ along two faces $f,f'$ that share an edge $e$, then $E_g=\{e\}$ and $v_g=0$. 
We use identity \eqref{pic:insert} to insert the 6j symbol for $t$ into the diagram $P'$. This yields a polygon diagram $P''$ with the morphisms for $f'$  assigned to vertices in the interior
 that are connected by an edge labeled $l(e)$. 
Applying the second identity in \eqref{pic:semisimpleids} then yields
$$
\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\sum_{l(e)} \sum_{b_f, b_{f'}} \dim l(e)\, \ev(P')\, \mathrm{6j}(t,l,b)\stackrel{\eqref{pic:insert}}=\sum_{l(e)} \sum_{b_{f'}} \dim l(e) \ev(P'') \stackrel{\eqref{pic:semisimpleids}}=\ev(P).
$$
(iii) If $t$ is glued to $M'$ along three faces $f,f',f''$, then they share three edges $e=f\cap f'$, $e'=f\cap f''$ and $e''=f'\cap f''$, and there is exactly one vertex $v$ in $t$ that becomes internal after the gluing. Thus we have  $E_g=\{e,e',e''\}$ and  $v_g=1$.  
We first glue $t$ to $M'$ along $f$  with  identity \eqref{pic:insert}.  This eliminates the summation over $b_f$ in  \eqref{eq:indstate2} 
and  yields a polygon $P''$ with the morphisms for $f'$ assigned  to adjacent vertices in the interior that are connected by an edge labeled $l(e)$.  
Applying the second identity in \eqref{pic:semisimpleids} then eliminates the summation over $l(e)$ and  $b_{f'}$ and  the factor $\dim l(e)$ in \eqref{eq:indstate2}, as in (ii). This yields a polygon diagram $P'''$ that  differs from $P$ only in a disc in its interior, where one has
\begin{align}\label{eq:differenceii}
&\begin{tikzpicture}[scale=.3]
\node at (-3,0){$P'''$};
\draw[line width=.5pt] (0,0)--(0,-2) node[midway, anchor=west]{$i$};
\draw[line width=.5pt] (0,-2).. controls (-2,-4).. (0,-6) node[midway, anchor=east]{$l(e')$};
\draw[line width=.5pt] (0,-2).. controls (2,-4).. (0,-6) node[midway, anchor=west]{$l(e'')$};
\draw[line width=.5pt] (0,-6)--(0,-8) node[midway, anchor=west]{$i$};
\draw[fill=black] (0,-2) circle (.2) node[anchor=east]{$\gamma$};
\draw[fill=black] (0,-6) circle (.2) node[anchor=east]{$\gamma$};
\end{tikzpicture}
\qquad 
&\begin{tikzpicture}[scale=.3]
\node at (3,0){$P$};
\draw[line width=.5pt] (0,0)--(0,-8) node[midway, anchor=west]{$i$};
\end{tikzpicture}
\end{align}
with $\gamma\in \Hom(f'')$  and $i\in I_\mac$  labeling the remaining edge of $f''$.  Multiplying $\ev(P''')$ by $\dim l(e')\dim l(e'') \dim \mac^\inv$ and summing over $l(e'), l(e'')\in I_\mac$ and over  $\gamma\in \Hom(f'')$ then yields 
\begin{align*}
\mathcal Z'(M, l_{\partial M}, b_{\partial M})= \dim \mac^\inv \!\!\!\! \!\! \sum_{\gamma, l(e'), l(e'')} \!\!\!\!\!\!\ \dim l(e')\dim l(e'')\ev(P''')
\stackrel{\eqref{eq:2gonformula}}
=\ev(P).
\end{align*}
\end{proof}
 
Note that the evaluation of the diagram obtained by projecting the dual of the boundary triangulation on $M$ to the defect surface $D$ does not depend on the choice of the underlying PL homeomorphism $\phi: M\to [0,1]\times D$. By Lemma \ref{lem:projiso}  different choices of $\phi$ yield isotopic projection maps. Diagrams for spherical fusion categories that are related by PL isotopies have the same evaluation. This is well-known and  can be viewed as a special case of  \cite[Th.~1.12]{JS}, \cite[Th.~2.12]{BMS} for 2-category diagrams and \cite[Th.~3.9]{BMS}  for planar 2-category diagrams, see also the paragraphs after Example \ref{ex:2catdiagram} and Definition \ref{def:cyclictrans}. Together with identities \eqref{pic:rm2} to \eqref{pic:bimodulenat} this ensures that the evaluation of the resulting diagram is independent of $\phi$. 

As the evaluation of the polygon diagram in Proposition \ref{th:topological invariance} depends only on the  triangulation and labeling of $\partial M$ and on the defect data, we obtain

\begin{corollary} Let $M,M'$ be  triangulated 3-manifolds with defect data that satisfy the assumptions of Proposition \ref{th:topological invariance} and whose boundary triangulations coincide. Then for all labelings $l_{\partial M}$ of the boundary one has $\mathcal Z(M, l_{\partial M})=\mathcal Z(M', l_{\partial M})$.
\end{corollary}


In particular, this implies  that the state sum of any  generic transversal triangulated 3-manifold with defect data is invariant under generic transversal bistellar moves.  This follows with Corollary \ref{cor:gluing}, as the tetrahedra  in such moves define  triangulations  of a 3-ball
that satisfy the assumptions of Proposition \ref{th:topological invariance} and agree on its boundary.  


\begin{corollary}\label{cor:pachner} Let $M$ be a generic and transversal  triangulated 3-manifold with defect data and $l_{\partial M}$ a labeling of its boundary. 
Then the state sum $\mathcal Z(M, l_{\partial M})$ from Definition \ref{def:statesum} is invariant under  generic transversal bistellar moves in the interior of $M$.
\end{corollary}

\begin{figure}
\def\svgwidth{.9\columnwidth}

\caption{bistellar moves for tetrahedra without and with defect discs:\protect\newline
(a),(b):  encoding the associator of a spherical fusion category $\mac$,\protect\newline
(c)-(f):   encoding the natural isomorphism $c$ for a $\mac$-module category $\mam$,\protect\newline
(g)-(i):  encoding the natural isomorphism $b$ for a $(\mac,\mad)$-bimodule category $\mam$.
}
\label{fig:pachnerdef}
\end{figure}

All  generic transversal bistellar moves  for tetrahedra with defect surfaces are shown in Figure \ref{fig:pachnerdef}.  The moves for tetrahedra that also involve defect lines and defect vertices are analogous, but with the additional conditions that  defect vertices must not lie on faces  and defect edges must not intersect edges of the tetrahedra. 





The bistellar invariance of state sums for 3-manifolds with defect surfaces has a similar interpretation to the one for Turaev-Viro-Barrett-Westbury state sums outlined at the end of Section \ref{subsec:PLsubsec}. The moves  in Figure \ref{fig:pachnerdef} (c) to (f) encode the pentagon relation \eqref{eq:pentagoncdef} for the structure  isomorphisms $c_{i,j,m}: (i\oo j)\rhd m\to i\rhd (j\rhd m)$ for a $\mac$-module category and equivalent relations obtained from it by taking inverses. The  moves in Figure \ref{fig:pachnerdef} (g) to (i) encode the pentagon relation \eqref{eq:pentagonbdef} and the invertibility of the structure isomorphisms $b_{c,m,d}: (c\rhd m)\lhd d\to c\rhd (m\lhd d)$ in a $(\mac,\mad)$-bimodule category.  
The corresponding moves for surfaces with line and point defects combine these pentagon relations with the pentagon relations \eqref{eq:pentagoncfunc}, \eqref{eq:pentagondfunc} for $\mac$-module and $\mad$-right module functors and the hexagon relation \eqref{eq:hexa} for $(\mac,\mad)$-bimodule functors.

As for a spherical fusion category, the bistellar invariance for manifolds with defects can  be formulated as generalised  Biedenharn-Elliott and orthogonality relations for  6j symbols, which generalise the diagrammatic identities  \eqref{eq:biedenharneliotsph} and \eqref{eq:orthogonalitysph}. However, it becomes cumbersome to list all of these relations.
