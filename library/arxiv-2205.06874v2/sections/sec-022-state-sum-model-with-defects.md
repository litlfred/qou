---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-022-state-sum-model-with-defects
section_title: "State sum model with defects"
section_number: null
pages: 37-39
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.995
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
In this section we show how the generalised 6j symbols for generic transversal defect tetrahedra  combine to state sums for a generic transversal triangulated 3-manifolds with defect data. 


Let $M$ be a generic transversal triangulated 3-manifold with defect data, $R$ its set of regions and $A$ its set of oriented defect areas.  We denote by $\mac_r$ the spherical fusion category assigned to the region $r$ and  by $\mam_a$ the bimodule category assigned to the defect area $a$. A vertex, edge or triangle of the triangulation is called {\bf boundary} if its is contained
 in $\partial M$ and  {\bf internal} otherwise. 
We use the following notation:
\begin{compactitem}
\item $\mathrm{Tet}$ for the set of tetrahedra of the triangulation, 
\item $\Delta$ for its set of triangles, $\Delta_{\partial M}$ for its set of boundary triangles and $\Delta_{i}$ for its set of internal triangles,
\item $E$ for its set of edges, $E_{\partial M}$ for its set of boundary edges and $E_{i}$ for its set of internal edges, $E_r$ for  its set of edges  in the region $r$ and $E_a$ for its set of edges that intersect a defect area $a$,
\item $V$ for its set of vertices, $V_{\partial M}$ for its set of boundary vertices,  $V_{i}$ for its set of internal vertices and $V_r$ for its set of vertices  in the region $r$.  
\end{compactitem}
 

We fix for each spherical fusion category $\mac$ and each bimodule category $\mam$ sets $I_{\mac}$ and $I_{\mam}$ of representatives of the isomorphism classes of simple objects and
associated projection and inclusion morphisms  as  in Section \ref{sec:projincl}.  
For each labeling $l$ of $M$  as in Definition \ref{def:label} 
 we denote by $l(e)\in I_{\mac_r}$ or $l(e')\in I_{\mam_a}$ the simple object assigned to  $e\in E_r$ or $e'\in E_a$. For an oriented triangle $f$ labeled with simple objects in the sets of representatives and associated projection or inclusion morphisms, we write $\Hom(f)$ for the associated morphism space from \eqref{pic:homspace}.

Each tetrahedron $t\in \mathrm{Tet}$ is equipped with the orientation induced by $M$. For the tetrahedra that intersect defect surfaces, this is already encoded in their labeling with defect data. For  tetrahedra that do not intersect defect surfaces, we always assume this orientation choice without emphasising it notationally. 
 


\begin{definition} \label{def:statesum} Let $M$ be a generic transversal triangulated  3-manifold with defect data,  $l_{\partial M}$ a labeling of its boundary edges with simple objects in the chosen sets of representatives and $b_{\partial M}$ an assignment of  morphisms from the morphism spaces \eqref{pic:homspace} to its boundary triangles. The state sum of $(M,l_{\partial M}, b_{\partial M})$ is
\begin{align}\label{eq:state sum}
\mathcal Z(M,l_{\partial M},b_{\partial M})=
\prod_{r\in R} \dim(\mathcal C_r)^{-\left(\Sigma_{v\in V_r} \epsilon(v)\right)}
\sum_{l}\sum_{b_i}   \prod_{t\in \mathrm{Tet}} \mathrm{6j}(t, l,b)\prod_{e\in E} \dim l(e)^{\epsilon(e)},
\end{align} 
where
\begin{compactitem}
\item  $\epsilon(v)=1$ for $v\in V_{i}$, $\epsilon(e)=1$ for $e\in E_i$ and $\epsilon(v)=1/2$ for $v\in V_{\partial M}$,  $\epsilon(e)=1/2$ for $e\in E_{\partial M}$,
\item $\Sigma_l$ is the sum over all labelings $l$ of  edges of $M$  with simple objects in  $I_{\mac_r}$ and $I_{\mam_a}$ that coincide with  $l_{\partial M}$ on the boundary,
\item $\Sigma_{b_i}$ is the sum over all labelings $b_i$ of internal triangles of $M$ with the projection and inclusion morphisms in the morphism spaces \eqref{pic:homspace},
\item $\Pi_{t\in \mathrm{Tet}}\, \mathrm{6j}(t, l, b)$ stands for the  product of the generalised 6j symbols $\mathrm{6j}(t, l, b)\in\C$ of all tetrahedra given by the labeling $l$ and the assignment $b=(b_i, b_{\partial M})$ of morphisms to the triangles. 
\end{compactitem}
We denote by $\mathcal Z(M, l_{\partial M})$ the associated  linear map 
\begin{align}\label{eq:statesummap}
\mathcal Z(M, l_{\partial M}): \bigotimes_{f\in \Delta_{\partial M}} \Hom(f)\to\C, \quad b_{\partial M}\mapsto \mathcal Z(M,l_{\partial M},b_{\partial M})
\end{align}
and by $\mathcal Z'(M,l_{\partial M},b_{\partial M})$ the rescaled state sum without the dimension factors of boundary edges and vertices
\begin{align}\label{eq:rescstate}
\mathcal Z(M, l_{\partial M}, b_{\partial M})=\left(\frac {\prod_{e\in E_{\partial M}} \dim l(e)} {\prod_{r\in R}\prod_{v\in V_r\cap V_{\partial M}} \dim \mac_r}  \right)^{1/2} \mathcal Z'(M, l_{\partial M}, b_{\partial M}).
\end{align}
\end{definition}

The product $\Pi_{t\in \mathrm{Tet}} \mathrm{6j}(t,l,b)$  in formula \eqref{eq:state sum} can also be viewed as the evaluation of the (unordered) tensor product $\otimes_{t\in \mathrm{Tet}} \mathrm{6j}(t)$ of the linear forms $\mathrm{6j}(t)$ in Definition \ref{def:gen6j} on a vector in the  tensor product of the morphism spaces for  the triangles. This vector is  defined by the labelings $l,b_i, b_{\partial M}$, and the sums over $l$ and $b_i$ eliminate the dependence on the labeling in the interior of $M$.



It is clear  that the linear map $\mathcal Z(M, l_{\partial M})$ does not depend on the choice of projection and inclusion morphisms for the interior triangles. If the simple objects assigned to the edges of the triangulation are fixed, then the projection and inclusion morphisms assigned to the interior triangles are fixed by \eqref{eq:projincl} up to simultaneous rescaling $p^\alpha_{xm}\to \lambda p^\alpha_{xm}$ and $j^\alpha_{xm}\to \lambda^\inv j^\alpha_{xm}$ for $\lambda=\lambda(x,m,\alpha)\in \C^\times$. As each interior triangle arises in exactly two tetrahedra with opposite orientations, the state sum is invariant under such rescalings.

To determine the dependence of the state sum   on the choice of representatives of simple objects, let $M$ be a  triangulated 3-manifold with defect data. Fix two sets of representatives $I,I'$ for each category labeling a region or  defect area and an isomorphism $\phi_{xx'}: x\to x'$ for each pair of isomorphic objects $x\in I$, $x'\in I'$. Note that this isomorphism is unique up to rescaling with $\C^\times$ and that it induces an isomorphism $\phi_f: \Hom(f)\to \Hom(f)'$ between the morphism spaces for a triangle $f$ labeled by isomorphic objects in $I$ and $I'$. 
More explicitly, these isomorphisms are given by 
\begin{align*}
&\phi_f: \Hom(m, F(j\rhd n))\to \Hom(m', F(j'\rhd n')), \quad \alpha\mapsto F(\phi_{jj'}\rhd \phi_{nn'})\circ \alpha\circ \phi^\inv_{mm'}\\
&\phi_f: \Hom(F(j\rhd n),n)\to \Hom(F(j'\rhd n'),m'), \quad \beta \mapsto \phi_{mm'} \circ \beta\circ F(\phi_{jj'}^\inv\rhd \phi_{nn'}^\inv).
\end{align*}
Definition \ref{def:gen6j} and the cyclic invariance of the trace imply that the 6j symbols are invariant under these isomorphisms, if they are applied to all morphism spaces simultaneously.  This yields


\begin{corollary} Let $M$ be a generic transversal  triangulated 3-manifold with defect data. Let $l_{\partial M}$ and $l_{\partial M}'$ be labelings of the boundary triangles with simple objects in two sets of representatives $I,I'$. Then 
$$\mathcal Z(M,l_{\partial_M})=\mathcal Z(M,l'_{\partial_M})\circ (\otimes_{f\in \Delta_{\partial M}}\phi_f):\bigotimes_{f\in \Delta_{\partial M}}\Hom(f)\to \C.$$
\end{corollary}

In particular, it follows that the state sum for a \emph{closed} generic transversal  triangulated 3-manifold with defect data does not depend on the choice of representatives of simple objects. 

It is also apparent from  Definition \ref{def:statesum} that the state sum \eqref{eq:state sum} is a direct generalisation of the usual Turaev-Viro-Barrett-Westbury state sum from \cite{BW,TV} and coincides with it if all defect areas, defect lines and defect vertices are trivial. This amounts to replacing all bimodule categories in \eqref{eq:state sum} by a single spherical fusion category $\mac$, viewed as a $(\mac,\mac)$-bimodule category, and all bimodule functors and natural transformations by identity functors and natural transformations. 

\begin{corollary}\label{cor:reducedstatesum}
For any triangulated 3-manifold without defects and any generic transversal triangulated 3-manifold with trivial defect data, labeled by a spherical fusion category $\mac$, the state sum from Definition \ref{def:statesum} reduces to the Turaev-Viro-Barrett-Westbury state sum
\begin{align}\label{eq:statesumsph}
\mathcal Z(M, l_{\partial M}, b_{\partial M})=\frac 1 {\dim\mac^{|V_{i}|+|V_{\partial M}|/2}}  \sum_{l}\sum_{b_i}   \prod_{t\in \mathrm{Tet}} \mathrm{6j}(t,l,b)\prod_{e\in E} \dim l(e)^{\epsilon(e)}.
\end{align} 
\end{corollary}

Another direct consequence of  Definition \ref{def:statesum} is that the state sum can be computed by gluing  triangulated 3-manifolds  along  boundary components. As in the case  without defects, this allows one to compute state sums by cutting  3-manifolds into simpler pieces. The only additional restriction  is that the defect surfaces must meet the cut transversally and all pieces must be generic and transversal.

\begin{corollary}\label{cor:gluing} Let $M_1$ and $M_2$ be generic  transversal  triangulated 3-manifolds with defect data and $M$ obtained by gluing $M_1$ and $M_2$ along a boundary component $\Sigma\subset \partial M_i$. Then
\begin{align}
\mathcal Z(M,l_{\partial M}, b_{\partial M})=\sum_{l_\Sigma} \mathcal Z(M_1,l_{\partial M_1}, b_{\partial M_1})\cdot \mathcal Z(M_2,l_{\partial M_2}, b_{\partial M_2}),
\end{align}
where the labelings $l_{\partial M}$ and $b_{\partial M}$ of $\partial M$ are induced by the labelings $l_{\partial M_i}$ and $b_{\partial M_i}$ of $\partial M_i$ and the
 sum is over the labelings of  edges in $\Sigma$ with simple objects and over dual bases of the  morphism spaces for  triangles in $\Sigma$.
\end{corollary}
