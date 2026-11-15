---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-027-triangulation-independence
section_title: "Triangulation independence"
section_number: null
pages: 48-51
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.994
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
In this section we  show  that  any two generic transversal triangulations of a  3-manifold with defect data yield the same state sum if they agree at its boundary. 
Note that this does not follow directly from  Corollary \ref{cor:pachner}, because it is not guaranteed a priori  that such triangulations are related by \emph{generic  transversal} bistellar moves. 
As a first step, we derive a counterpart  of Proposition \ref{th:topological invariance}  for general defect surfaces. 

We again consider 3-manifolds $M$  that shell to fine neighbourhoods of a defect surface $D$ and project the dual of the boundary triangulation on $\partial M$  to $D$  as in Definition \ref{def:projection} with an orientation preserving PL homeomorphism $\phi: M\to [0,1]\times D$. The only difference to Proposition \ref{th:topological invariance}  is that $D$ is no longer a disc and the resulting diagram on $D$ must be cut along the triangulation to obtain a polygon diagram.





\begin{proposition}\label{lem:polystatesum}
Let  $M$ be a triangulated 3-manifold with defect data that shells to a fine neighbourhood  of a defect surface $D$ by shellings of tetrahedra that do not intersect $D$. 
Let $P$  be a polygon diagram obtained by projecting the dual of the  triangulation on $\partial M$ to $D$ and  cutting $D$ along the triangulation  to a disc. 
 Then 
\begin{align*}
\mathcal Z'(M,  l_{\partial M}, b_{\partial M})=
\sum_{l}\sum_{b_{\Delta_i}} \mathrm{ev}(P)\prod_{e\in E_{i}} \dim l(e),\\[-6ex]
\end{align*}
where 
\begin{compactitem}
\item $E_{i}$ and $\Delta_i$ are the sets of internal edges and triangles of $M$ that 
 correspond to boundary vertices and edges in $P$, 
\item the sum is over all assignments of simple objects to  edges in $E_i$ and bases of the morphism spaces of  triangles in  $\Delta_i$. 
\end{compactitem}
\end{proposition}

\begin{proof} 
The claim  follows by induction over the number $n$  of tetrahedra in $M$ that do not intersect $D$. 

1.~For $n=0$,  $M$ is a fine neighbourhood of $D$. Cutting $D$ along the triangulation to a disc corresponds to cutting $M$ to a 3-ball $B$ that is a fine neighbourhood of a defect disc. 
Edges in $E_i$ correspond to  boundary edges of $B$  and elements of $\Delta_i$ to boundary triangles in $B$.   Every labeling of internal edges in $M$  defines a labeling $l$ of  $E_i$ and a labeling $l'$ of the internal edges of $B$. 

The state sum for $M$ is given by formula \eqref{eq:state sum}. 
By Proposition \ref{th:topological invariance}, summing over the labeling $l'$ and the labelings of internal triangles of $B$  yields the state sum for $B$, which is the evaluation of $P$. 
As every edge in $E_i$ is internal in $M$, but  in the boundary of $B$, the state sum for $M$ is obtained by multiplying this expression with $\Pi_{e\in E_{i}} \dim l(e)$
and summing over the labelings of edges in $E_i$ and morphism spaces for triangles in $\Delta_i$.

2.~Suppose that  $M$ contains $n+1$ tetrahedra that do not intersect $D$. 
As $M$ shells to a fine neighbourhood of $D$, it is obtained by gluing a tetrahedron $t$  that does not intersect $D$ to triangulated manifold  $M'$ that also satisfies the assumptions and has $n$ tetrahedra that do not intersect $D$.  
If $t$ is contained in the region labeled by a spherical fusion category $\mac$, then by the induction hypothesis and 
Corollary \ref{cor:gluing} the state sum of $M$ is given by formula  \eqref{eq:indstate2} in the proof of Proposition \ref{th:topological invariance}. 

It remains to show that  \eqref{eq:indstate2} yields  $\ev(P)$. 
If $t$ is glued to $M'$ along a single face, this follows as in 2.(i) in the proof of Proposition \ref{th:topological invariance}. 
 If $t$ is glued to $M'$ along two faces $f,f'$ that share an edge $e=f\cap f''$ or along three faces $f,f', f''$ that share edges $e=f\cap f'$, $e'=f\cap f''$ and $e''=f'\cap f''$, 
  we can assume without loss of generality that the edges in the polygon diagram  $P'$ for $M'$  that correspond to $e$, $e'$, $e''$ do not intersect  $\partial P'$. This is possible, because the assumptions imply that they do not intersect a side of $P'$ that is contained in $\partial D$. If they intersect  sides of $P'$ that are in the interior of  $D$, we 
can apply identity \eqref{pic:gluepoly} to cut   $P'$, glue it back together in such a way that these edges do not intersect $\partial P'$ and reverse this transformation after the gluing of $t$.
The claim then  follows as in 2.(ii) and 2.(iii) in the proof of Proposition \ref{th:topological invariance}. \end{proof}

After summation over the objects and morphisms at its boundary, the evaluation of the polygon diagram in Proposition \ref{lem:polystatesum} is again independent of the choice of the  PL homeomorphism $\phi: M\to [0,1]\times D$ that defines the projection of the boundary graph on $D$. Lemma \ref{lem:projiso} ensures that different choices for $\phi$ yield PL isotopic projection maps and hence diagrams for spherical fusion categories with the same evaluations. Together with identities   \eqref{pic:rm2} to \eqref{pic:bimodulenat} 
and identities \eqref{pic:gluepoly} and \eqref{pic:closepoly} this ensures the polygon evaluations for different choice of $\phi$ are equal. 
As the latter  are precisely the cutting and gluing identities that relate different polygon presentations of surfaces, see for instance \cite[Ch.~6]{Lee} and \cite[Ch.~6.38 and 6.40]{ST}, it also follows that  all ways of cutting the surface in Proposition \ref{lem:polystatesum} 
yield the same value for the state sum. 

Note also that Proposition \ref{lem:polystatesum}  allows one to  drop the requirement that a fine triangulation is generic in the interior of $M$.
For a triangulation that is non-generic in the interior of $M$, a small displacement of the defect surfaces, defect lines and defect vertices yields a generic triangulation. As the cyclic evaluations of the associated polygon diagrams coincide, all such displacements have the same state sum.



It remains to show that the state sum from Proposition \ref{lem:polystatesum}  does not depend on the choice of the triangulation in the interior of $M$.  
This follows again from identities \eqref{pic:gluepoly} and \eqref{pic:closepoly}.


\begin{lemma} \label{lem:subdivide}
Let $M,M'$ be triangulated 3-manifolds with defect data that shell to fine neighbourhoods of a defect surface $D$ with shellings by tetrahedra that do not intersect $D$. Suppose that the triangulations of $M,M'$ coincide on the boundary. Then for all labelings $l_{\partial M}$ and $b_{\partial M}$ 
$$
\mathcal Z(M,l_{\partial M}, b_{\partial M})=\mathcal Z(M',l_{\partial M}, b_{\partial M}).
$$
\end{lemma}



\begin{proof}
By Proposition \ref{lem:polystatesum} the rescaled state sums for $M,M'$ are obtained by  projecting the dual graph of the boundary triangulation on $\partial M$ to $D$,  cutting $D$ along the triangulations to discs and evaluating the resulting  polygon diagrams $P,P'$. With identities \eqref{pic:gluepoly} and \eqref{pic:closepoly}  we can cut the polygon diagrams $P,P'$ into smaller pieces that are the intersections of $P,P'$ with the tetrahedra in the two  triangulations. 

More precisely, one obtains embedded graphs $\Gamma,\Gamma'$  on $D$, whose vertices, edges and faces are the intersections of $D$ with the edges, triangles and tetrahedra in the triangulations.   We denote by the same letters the associated graphs  on $P,P'$ and call  vertices or edges of $\Gamma,\Gamma'$ internal, if they are not contained in $\partial D$ and boundary otherwise.   By adjusting the triangulations, we can assume that $\Gamma,\Gamma'$ are \emph{generic}, meaning that
(i) defect vertices  and vertices labeled by  spherical fusion categories 
 are in the interior of faces of $\Gamma,\Gamma'$,
(ii) defect edges and edges labeled by spherical fusion categories intersect the edges of $\Gamma,\Gamma'$ transversally in the interior. 

With the labelings of the defects and the triangulations every face of $\Gamma$ and $\Gamma'$ becomes a polygon diagram. 
By Proposition \ref{lem:polystatesum},   \eqref{pic:gluepoly} and \eqref{pic:closepoly}, the rescaled state sums for $M,M'$  are
  obtained by multiplying the evaluations of these polygon diagrams for $\Gamma,\Gamma'$, rescaling with the dimensions of the simple objects at internal vertices and summing  over all  labelings of  internal vertices and over bases of the morphism spaces at internal edges.
 
Using again identities \eqref{pic:gluepoly} and \eqref{pic:closepoly}, we cut these polygon diagrams into smaller pieces that correspond to a common subdivision of $\Gamma$ and $\Gamma'$.  By slightly displacing the vertices of $M,M'$  one can achieve that the graphs $\Gamma,\Gamma'$ remain generic  and that  every  point $v''\in (\Gamma\cap \Gamma')\setminus \partial D$ is a transversal intersection point of an edge $e$ of $\Gamma$ and an edge $e'$  of $\Gamma'$, while all boundary edges and vertices of $\Gamma,\Gamma'$ remain fixed.  If the displacements of vertices  are sufficiently small, this does not change the evaluations of the polygon diagrams for $\Gamma,\Gamma'$ and hence preserves the state sums.

Let $\Gamma''$ be the embedded graph  on $D$
obtained by superimposing $\Gamma$ and $\Gamma'$ and inserting a new four-valent vertex at each intersection point $v''=e\cap e'$.  Then every edge of $\Gamma''$ is either on an edge of $\Gamma$ or of $\Gamma'$. Every vertex of $\Gamma''$ is either a vertex of $\Gamma$, of $\Gamma'$ or an intersection point of an edge of $\Gamma$ and an edge of $\Gamma'$.
  Summing the  product of polygon  evaluations for  $\Gamma''$ over the labelings at those  internal  edges and vertices  that lie on $\Gamma'$ 
  yields the corresponding  product of  polygon evaluations for $\Gamma$. Summing it instead over  the labelings at the internal  edges and vertices that lie on $\Gamma$ gives the corresponding  product of  polygon evaluations for $\Gamma'$. By combining these two summations one obtains that the state sums are equal. 
\end{proof}

By combining Lemma \ref{lem:subdivide} with the triangulation independence of Turaev-Viro-Barrett-Westbury state sums for spherical fusion categories, we can now show that the state sums for two generic transversal triangulations of a 3-manifold $M$ with defect data coincide, whenever their triangulations coincide at the boundary. 


\begin{theorem}\label{th:fulltopinv} Let $T,T'$ be generic transversal triangulations of a 3-manifold $M$ with defect data that coincide on $\partial M$.  Then for all boundary labelings $l_{\partial M}$  and $b_{\partial M}$   the state sums for  $T$ and $T'$ are equal:
$$
\mathcal Z(M,l_{\partial M}, b_{\partial M},T)=\mathcal Z(M, l_{\partial M}, b_{\partial M}, T').
$$
\end{theorem}

\begin{proof} By Lemma \ref{lem:finetriang} there are  finite sequences of  bistellar moves  between generic  transversal  tetrahedra that transform the triangulations $T,T'$ into triangulations $S,S'$ that satisfy (i)-(iii) in Lemma \ref{lem:finetriang}. By Corollary \ref{cor:pachner} one has $\mathcal Z(M,l_{\partial M}, b_{\partial M},T)=\mathcal Z(M,l_{\partial M}, b_{\partial M},S)$ and $\mathcal Z(M,l_{\partial M}, b_{\partial M},T')=\mathcal Z(M,l_{\partial M}, b_{\partial M},S')$. 
To show that $\mathcal Z(M,l_{\partial M}, b_{\partial M},S)=\mathcal Z(M,l_{\partial M}, b_{\partial M},S')$, we
denote by $\Sigma_i$ the connected components of the defect manifold $D=\amalg_{i=1}^n \Sigma_i$ and by $r_k$ the regions of $M$, which are the connected components of $M\setminus D=\amalg_{k=1}^m r_k$.

 By Lemma \ref{lem:finetriang} (ii)  gluing all tetrahedra in $S, S'$ that are contained in a region $r_k$ yields  triangulated  3-manifolds $R_k, R'_k$ that are PL homeomorphic to $\bar r_k$.  
 By Lemma \ref{lem:finetriang} (ii) gluing all tetrahedra in $S, S'$ that intersect $\Sigma_i$ yields fine neighbourhoods $D_i, D'_i$ of $\Sigma_i$.
 This implies that all boundary triangles in $D_i, D'_i$ that are internal triangles of $M$ are glued to boundary triangles in one of the 3-manifolds $R_k, R'_k$.
 More specifically, each connected component of $\partial D_i\setminus \partial M$ coincides with a unique boundary component of  some $R_k$,  up to the fact that they have  opposite orientations. 
 As $\partial D\subset \partial M$, all boundary triangles of $D_i$ and $D'_i$ that intersect $\Sigma_i$ are contained in $\partial M$ and hence coincide. 
 
As  $D_i$ and $D'_i$ are both PL homeomorphic  to  $[0,1]\times \Sigma_i$, their boundaries are PL homeomorphic. 
As their boundary triangulations agree on $\partial D\subset \partial M$, this allows one to transform each connected component of $\partial D'_i\setminus \partial M$ into the corresponding  connected component of  $\partial D_i\setminus \partial M$ by a finite number  shellings  or inverse shellings with tetrahedra that do not intersect any defect surface. Performing the same  shellings on the associated boundary component of $R'_k$   transforms it into the corresponding boundary component of  $R_k$.

For each labeling of the edges and triangles, performing  such a simultaneous  shelling or inverse shelling at $D'_i$ and $R'_k$ amounts to multiplying or dividing the state sum of $M'$ by the 6j symbol of a  tetrahedron $t$  labeled by a spherical fusion category, with the 6j symbol of the tetrahedron $\bar t$ with the same labeling, but the opposite orientation, and with  dimension factors associated to their edges.   The orthogonality relation \eqref{eq:orthogonalitysph} and identity \eqref{eq:dimformula} ensure that  this does not change the state sum. 

Hence, we can assume without loss of generality that the triangulations of all 3-manifolds $D'_i$ and $D_i$ coincide on the boundary and that the same holds for all  triangulated 3-manifolds $R_k$ and $R'_k$.  
  Under this assumption, the state sums of $D_i$ and $D'_i$  agree by Lemma \ref{lem:subdivide} for
 all labelings. 
 The state sums of $R_k$ and $R'_k$ are the usual Turaev-Viro-Barrett-Westbury state sums for a  spherical fusion category and are equal by Theorem \ref{th:pachinv}. 
 With Corollary \ref{cor:gluing} this yields 
 \begin{align*}
\mathcal Z(M, l_{\partial M}, b_{\partial M}, S)&=\sum_{l_{\partial}}\sum_{b_\partial}  \prod_{i=1}^n\mathcal Z(D_i, l_{\partial D_i}, b_{\partial D_i})\prod_{k=1}^m  \mathcal Z(R_k, l_{\partial R_k}, b_{\partial R_k})\\
&=\sum_{l_{\partial}}\sum_{b_\partial}  \prod_{i=1}^n\mathcal Z(D'_i, l_{\partial D'_i}, b_{\partial D'_i})\prod_{k=1}^m  \mathcal Z(R'_k, l_{\partial R'_k}, b_{\partial R'_k})=\mathcal Z(M, l_{\partial M}, b_{\partial M}, S'),
 \end{align*}
 where the sums are over all labelings $l_\partial$ of internal edges in $M$ that are boundary edges of  $D_i$, $D'_i$ and over dual bases of the morphism spaces for internal triangles  in $M$ that are boundary triangles of  $D_i$, $D'_i$. 
\end{proof}




Theorem \ref{th:fulltopinv}  extends the definition of the state sum for a defect manifold to triangulations that are non-generic or non-transversal in the interior of $M$.  
Together with Proposition \ref{lem:polystatesum} it shows that slightly perturbing the defect surface, defect lines or defect vertices in the interior of $M$ does not change the value of the state sum. This allows one to define the state sum of a non-generic triangulation as the state sum of a small generic deformation.
Similarly, any triangulation of $M$ with non-transversal tetrahedra in the interior can be refined 
 by  stellar subdivisions to a triangulation that is transversal. 
 One can then perturb the defect surfaces, lines and vertices  to make it generic. 
  By Theorem \ref{th:fulltopinv}  all ways of doing so yield the same  state sum. 



\begin{definition} Let $M$ be a 3-manifold with defect data and $T$ a triangulation of $M$ whose boundary triangles are transversal and generic. Then for all boundary labelings $l_{\partial M}$,  $b$   the state sum of $M$ is  defined as
\begin{align}
\mathcal Z(M,l_{\partial M},b_{\partial M}, T):=\mathcal Z(M,l_{\partial M}, b_{\partial M}, T'),
\end{align}
for any generic transversal triangulation $T'$ that coincides with $T$ on $\partial M$.
\end{definition}


\begin{corollary}\label{cor:generalinvariant} Let $M$ be a 3-manifold with defect data and $T,T'$ triangulations of $M$ that coincide on $\partial M$ and whose boundary triangles are transversal and generic.
Then their state sums coincide for all boundary  labelings $l_{\partial M}$,  $b_{\partial M}$. 
In particular, if $M$ is closed, its state sum does not depend on the choice of the triangulation.
\end{corollary}

In principle the dependence  of the state sum on boundary triangulations  and their labeling could be removed in the same way as  for  Turaev-Viro-Barrett-Westbury state sums without defects.  To obtain a topological quantum field theory from the latter one considers 
the vector spaces $V_{\partial M}(t,l)=\otimes_{f\in \Delta_{t}} \Hom(f,l)$ for a given triangulation $t$ of $\partial M$ and a labeling $l$ with simple objects. The state sum of a triangulated cyclinder $\partial M\times[0,1]$  then defines a linear map $\mathcal Z(\partial M\times[0,1], l): V_{\partial M}(t_0,l_0)\to V_{\partial M}(t_1,l_1)$, where $t_i$ is the boundary triangulation of $\partial M\times \{i\}$ and $l_i$ its labeling. By taking the projective limit of the system of all such state sums, one obtains the vector space that the associated TQFT assigns to $\partial M$, see  \cite[Sec.~13.3.2]{TVbook}. 

It is clear that an analogous procedure could be applied to state sum models with defects and seems plausible that this would result in a defect TQFT in the sense of \cite{CMS,CRS} by Carqueville et al.  For the spherical fusion categories $\mathrm{Vec}_G$ from Example \ref{ex:vectgomega} and oriented surfaces of genus $g\geq 1$  cylinders with  defects are considered in Example \ref{ex:surface}.
