---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-025-neighbourhoods-of-defect-surfaces
section_title: "Neighbourhoods of defect surfaces"
section_number: null
pages: 41-44
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 1.0
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
\label{subsec:gentrans}


 In the presence of defects,  applying a bistellar move to a generic transversal triangulation may yield a triangulation that is no longer transversal or generic. 
  For this reason, it is not straightforward to establish invariance of the state sums via bistellar moves.  
  Instead, we refine the triangulations and decompose the underlying  defect 3-manifold   into certain neighbourhoods of defect surfaces and components contained in the regions between them. Their state sums are  computed separately and then  glued with Corollary \ref{cor:gluing}. This also gives a geometrical interpretation to the state sums and facilitates the computation of  examples.

The neighbourhoods of the defect surfaces we consider are similar to regular neighbourhoods, see \cite[Ch.~3]{RS}, but our defect surfaces are not realised as subcomplexes of the triangulation. 

\begin{definition} A 
 {\bf fine neighbourhood} of a defect surface $D$ is a connected
generic transversal  triangulated  3-manifold $M$ with defect surface $D\subset M$ such that
 $D\cap \partial M=\partial D$,  every vertex of $M$ is contained in $\partial M$  and every triangle or edge  in $M$ that does not intersect $D$ is contained in $\partial M$.
\end{definition}

By applying a finite number of  bistellar moves between generic transversal triangulations, any 
 generic transversal triangulation of a defect 3-manifold $M$ can be subdivided in such a way that the tetrahedra intersecting a given defect surface form a fine neighbourhood of the defect surface.  
 A bistellar move between two generic transversal triangulations is called {\bf generic transversal bistellar move} in the following. 
 



\begin{lemma} \label{lem:finetriang}Let $(M, D)$ be a defect 3-manifold  and $T$ a generic transversal  triangulation of $M$. 
Then there is a finite sequence of  generic transversal bistellar  moves  that transforms  $T$ into a generic transversal  triangulation $S$ such that:
\begin{compactenum}[(i)]
\item $S$ coincides with $T$ on $\partial M$,
\item the tetrahedra in $S$ contained in any region $r\subset M$ form a  3-manifold $R$ homeomorphic to $\bar r$,
\item the tetrahedra in $S$ that intersect any defect surface $\Sigma\subset D$ form a fine neighbourhood of $\Sigma$.
 \end{compactenum}
\end{lemma}

\begin{proof}  Let $D=\amalg_{j=1}^n \Sigma_j$ be the defect manifold, whose connected components are the defect surfaces $\Sigma_j$, and $M\setminus D=\amalg_{k=1}^m r_k$ with the regions $r_k$ as connected components.  

For each oriented edge in $T$ that intersects $D$ and hence is  oriented by $D$,  denote by $r_f$ the region that contains its target vertex  and by  $r_i$ the region that contains its starting vertex. Analogously, for each triangle and tetrahedron  in $T$ that intersects $D$,  denote by $r_f$ and $r_i$ the regions that contain the target vertices and starting vertices of its edges that intersect $D$.




The triangulation $S$ is constructed by a finite sequence of stellar subdivisions from  Section \ref{subsec:PLsubsec}, which are finite sequences of bistellar moves. 
We show  that this can be achieved with generic transversal bistellar moves. 


1.~In the first step, 
for each tetrahedron $t$ in $T$ that intersects $D$, choose a point $t_f\in r_f\cap \mathring{t}$  and  perform a 1-4  move  with $t_f$ as the new vertex. 
This  subdivides $t$ into four transversal tetrahedra. By adjusting the position of $t_f$ one can achieve that none of the new triangles contains a defect vertex and none of the new edges intersect defect lines. Hence,  all four tetrahedra are generic. This yields a generic transversal   triangulation $T'$ related to $T$ by generic transversal bistellar moves.

2.~In the second step, for each triangle $\Delta$ in $T'$ that intersects $D$ and is not contained in $\partial M$, choose a point $\Delta_f\in r_f\cap\mathring{\Delta}$ and perform the stellar subdivision on $\Delta$ with $\Delta_f$ as the new vertex. The  two bistellar moves that combine to this stellar subdivision involve only transversal tetrahedra. By adjusting the position of $\Delta_f$ one can achieve that  none of the  triangles arising in these moves  contains a defect vertex and none of the edges  intersect a defect line. With this, all of the tetrahedra become generic and we obtain a generic transversal  triangulation $T''$ related to $T'$ by generic transversal bistellar moves. 

3.~In the third step, for each edge $e$ in $T''$ that intersects $D$ and is not contained in  $\partial M$, choose a point $e_f\in r_f\cap\mathring{e}$  and perform a stellar subdivision on $e$ with $e_f$ as the new vertex. All tetrahedra arising in the bistellar moves that combine to this stellar subdivision
 are transversal. By adjusting the position of $e_f$, one can achieve that none of their triangles  contains a defect vertex and none of their edges intersects a defect line. Hence,  all tetrahedra in this sequence of bistellar moves are generic. 

This yields a generic  transversal  triangulation $T'''$ related to $T$ by generic transversal bistellar moves. The associated subdivisions of defect tetrahedra are shown in Figure \ref{fig:barycentric}.  We equip each new edge in $T'''$ that intersects $D$ with the induced orientation and choose an arbitrary orientation for the other new edges.  

4.~We then apply steps 1 to 3  to the triangulation $T'''$, but now with  additional vertices $t_i\in r_i\cap\mathring{t}$, $\Delta_i\in r_i\cap \mathring{\Delta}$, $e_i\in r_i\cap\mathring{e}$ in the region $r_i$ instead of $r_f$. The positions of these new vertices can again be chosen in such a way that this defines a finite sequence of  bistellar moves between generic transversal tetrahedra. 

The result is a generic transversal triangulation $S$  that coincides with $T$ on $\partial M$ by construction.  
We denote by $S_j$ the triangulated 3-manifold formed by all tetrahedra in $S$ that intersect a defect surface $\Sigma_j$. 
By construction, every vertex of $S_j$ and every edge or triangle of $S_j$ that does not intersect $\Sigma_j$ is contained in $\partial S_j$, and hence $S_j$ is a fine neighbourhood of $\Sigma_j$.  For each tetrahedron $t$ in the  triangulation $T$ that intersects  $\Sigma_j$,   the union  of the tetrahedra in its subdivision that are contained in a region $r_k$  is PL homeomorphic to  the closure of $(t\setminus D)\cap r_k$. These PL homeomorphisms and the identity maps for tetrahedra in $T$ that do not intersect $D$  glue to a PL homeomorphism from  the union of all tetrahedra in $S$  in $r_k$ to $\bar r_k$.  
\end{proof}



\begin{figure}
\begin{center}
\def\svgwidth{.99\columnwidth}
 
\end{center}
$\quad$

\vspace{-2cm}
\caption{Subdivisions of tetrahedra intersecting the defect manifold $D$ with new vertices $t_f$, $\Delta_f$ and $e_f$ that span the surface $E_f$.  Edges in the  subdivision that intersect $D$ are drawn in blue, edges  that lie in the region  $r_f$ in black and edges in the region $r_i$ in grey.}
\label{fig:barycentric}
\end{figure}

 A  fine neighbourhood of a defect surface $D$ is shown in Example \ref{ex:surface} and Figure \ref{eq:prism}. Generic transversal triangulations that do not form fine neighbourhoods  of their defect surfaces are given in  Examples \ref{ex:tetrahedronsphere}, \ref{ex:genusg} and \ref{ex:knotcomplement}, see also Figures \ref{fig:handle} and \ref{fig:knotcomplement}. In particular, any fine neighbourhood of  $D$ must have topology $[0,1]\times D$. 

\begin{lemma}\label{lem:finenbtop}
Let $M$ be a triangulated 3-manifold that shells to  a fine neighbourhood of a defect surface $D$  by elementary shellings with tetrahedra that do not intersect $D$. Then $M$  is PL homeomorphic to $[0,1]\times D$.
\end{lemma}

\begin{proof} If $M$ is a fine neighbourhood of $D$, this follows by applying  the same subdivision procedure as in the proof of Lemma \ref{lem:finetriang}, but to every edge and triangle that intersects the defect surface $D$, including the ones in $\partial M$.  Denote by $E_f$ the 2d PL surface spanned by the vertices $t_f$, $\Delta_f$ and $e_f$,  by $E_i$ the 2d PL surface spanned by the new vertices $t_i$, $\Delta_i$ and $e_i$, as shown in Figure \ref{fig:barycentric}. For each tetrahedron $t$ in the original triangulation  with $t\cap D\neq \emptyset$  the tetrahedra in its subdivision that intersect $D$ form  the region between the surfaces $E_t\cap t$ and $E_i\cap t$ in Figure \ref{fig:barycentric} This region  is PL homeomorphic to $[0,1]\times (t\cap D)$.  
The PL homeomorphisms for the tetrahedra $t$ with $t\cap D\neq \emptyset$ glue to a PL homeomorphism that sends the union  of all tetrahedra in the subdivision that intersect $D$  to $[0,1]\times D$.  As $M$ is related to it by elementary shellings, it is PL homeomorphic to $[0,1]\times D$ by Theorem \ref{th:pachshell}.
For a 3-manifold $M$  that shells to a fine neighbourhood of $D$ with elementary shellings by tetrahedra that do not intersect $D$ the claim follows  with Theorem \ref{th:pachshell}.
\end{proof}


In the following, we will often project graphs on the boundary of a manifold $M$ with a defect surface $D\subset M$ to the defect surface $D$. This is achieved via  orientation preserving  PL homeomorphisms $\phi: M\to [0,1]\times D$. We denote by $p_D: [0,1]\times D\to  D$, $(t,d)\mapsto d$ and $p_t:[0,1]\times D\to [0,1]$, $(t,d)\mapsto t$ the projection maps for the product, which are PL maps by construction. 


\begin{definition} \label{def:projection}Let $M$ be a triangulated 3-manifold with a defect surface $D\subset M$  and 
$\phi: M\to [0,1]\times D$ an orientation preserving PL homeomorphism with $p_D\circ \phi\vert_D=\mathrm{id}_D$. 
The {\bf  projections} induced by $\phi$ are the PL homeomorphisms
$P_i(\phi): \phi^\inv(\{i\}\times D)\to D$, $m\mapsto p_D\circ \phi(m)$ for $ i=0,1$.
\end{definition}

The diagrams obtained by projecting graphs on $\partial M$ to a defect surface $D\subset M$  depend on the choice of the underlying  PL homeomorphism. That their \emph{evaluations} are independent of this choice follows from the fact that different choices of PL homeomorphisms yield PL isotopic projection maps. 


\begin{lemma} \label{lem:projiso}Let $\phi_1,\phi_2: M\to [0,1]\times D$ be orientation preserving PL homeomorphisms with $p_D\circ \phi_1\vert_D=p_D\circ \phi_2\vert_D=\mathrm{id}_D$. Then the projection maps  $P_i(\phi_1)$ and $P_i(\phi_2)$ are PL isotopic for $i=0,1$. 
\end{lemma}

\begin{proof} By a well-known result of Epstein \cite[Th.~6.4]{E}, an orientation preserving PL homeomorphism from a 2-manifold with compact boundary components to itself is  
PL isotopic to the identity iff it is  homotopic to the identity. It is therefore sufficient to show that $P_i(\phi_2)$ and $P_i(\phi_1)$ are homotopic.  For this, we construct homeomorphisms $\phi'_i: M\to [0,1]\times D$ that coincide with $\phi_i$ on $\partial M_i:=\phi_1^\inv(\{i\}\times D)=\phi_2^\inv(\{i\}\times D)$ and  homotopies from $\phi'_2\vert_{\partial M_i}$ to $\phi'_1\vert_{\partial M_i}$.  For $i=0$ and $j=1,2$, we consider the continuous maps
\begin{align*}
F_j:[0,1]\times D\to [0,1], \;(t,d)\mapsto \begin{cases}\frac t {2 p_t(\phi_j(d))} & t\in[0, p_t(\phi_j(d))]\\
\frac {1-t}{2(1-p_t(\phi_j(d)))}+\frac {t-p_t(\phi_j(d))}{1-p_t(\phi_j(d))} & t\in[p_t(\phi_j(d)), 1]
\end{cases}
\end{align*}
and the homeomorphisms
$\phi_j': M\to [0,1]\times D$, $m\mapsto (F_j(\phi_j(m)), p_D(\phi_j(m)))$
that satisfy $\phi'_j(m)=\phi_j(m)$ for all $m\in \partial M_0\cup \partial M_1$, $p_D\circ \phi'(d)=d$ and $p_t\circ \phi'_j(d)=\tfrac 1 2$ for all $d\in D$. Then the continuous map
\begin{align*}
h:[0,1]\times \partial M_0\to D,\; (t,m)\mapsto p_D\circ \phi_2'\circ \phi'^\inv_1(\tfrac t 2 , p_D(\phi'_1(m)))
\end{align*}
satisfies $h(0,m)=P_0(\phi_2)(m)$ and $h(1,m)=P_0(\phi_1)(m)$ for all $m\in \partial M_0$ and is a homotopy from $P_0(\phi_1)$ to $P_0(\phi_2)$.  
The proof that $P_1(\phi_1)$ and $P_1(\phi_2)$ are homotopic is analogous.
\end{proof}
