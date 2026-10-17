---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-005-15-quantum-group-categorifications
section_title: "Quantum group categorifications"
section_number: 1.5
pages: 4-5
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.977
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
There is a strong interplay between quantum link invariants and algebraic objects known as quantum groups. Given the existence of link homology theories categorifying link invariants, it is perhaps not surprising to discover that quantum groups can also be categorified.  In this article we will examine how the two notions of decategorification given by the Grothendieck group and the trace can be applied to categorified quantum groups.


Quantum groups are Hopf algebras associated to Lie algebras $\mf{g}$.  They are obtained by $q$-deforming the universal enveloping algebra $\mathbf{U}(\mf{g})$.   Lusztig's modified, or idempotented, form $\dot{\mathbf{U}}(\mf{g})$ of the quantum group $\mathbf{U}_q(\mf{g})$ is well suited for categorification. These algebras are equipped with a family of orthogonal idempotents $1_{\lambda}$ indexed by the weight lattice $X$ of $\mf{g}$.  Any $\k$-algebra $A$ equipped with orthogonal idempotents indexed by a set $X$ can be regarded as an additive category whose objects are the elements of $X$.  Given two elements $\lambda, \mu \in X$,  $\k$-vector space of maps from $\lambda$ to $\mu$ can be defined by $1_{\mu} A 1_{\lambda}$.  In this framework, the idempotents $1_{\lambda}$ are thought of as identity morphisms from the object $\lambda$ to itself.  Composition in the category
\[
1_{\mu'} A 1_{\lambda'} \times 1_{\mu} A 1_{\lambda}\to \delta_{\mu,\lambda'} 1_{\mu'} A 1_{\lambda}
\]
is given by multiplication in $A$.



By thinking of a quantum group $\mathbf{U}_q(\mf{g})$ as a linear category in this way, we are naturally led to consider a categorification of $\mathbf{U}_q(\mf{g})$ given by the structure of a 2-category and our decategorification map must reduce a linear 2-category to a linear 1-category.











Associated to a field $\k$ and a symmetrizable Kac-Moody algebra $\mf{g}$, a 2-category $\UcatD(\mf{g})$ was defined in \cite{KL3} generalizing the $\mf{sl}_2$ case from \cite{Lau1}.   The 2-category $\UcatD(\mf{g})$ is the idempotent completion, or Karoubi envelope, of a 2-category $\Ucat(\mf{g})$ defined in terms of a graphical calculus.  More precisely, the objects of the category $\Ucat(\mf{g})$ are indexed by the weight lattice $X$ of $\mf{g}$.  The morphisms are formal direct sums of composites of maps $\onel \maps \lambda \to \lambda$, $\cal{E}_i \onel \maps \lambda \to \lambda + \alpha_i$, and $\cal{F}_i\onel \maps \lambda \to \lambda-\alpha_i$ corresponding to the Chevalley basis of $\mf{g}$.  For each 1-morphism $x$ there is also a grading shifted 1-morphism $x\la t\ra$ in $\Ucat(\mf{g})$.  The 2-morphisms are given by $\Bbbk$-linear degree preserving combinations of certain planar diagrams modulo local relations. See Figure~\ref{fig_Ucat-diagram} for an example of planar diagram in $\Ucat(\mf{g})$.

\begin{figure}[h]
 $
 \vcenter{
    \xy 0;/r.16pc/:
  (-8,-4)*{\fecross};(8,-4)*{\fecross};
  (0,2)*{\scap};(0,4)*{\lcap};
  (0,-10)*{\scupfe};(0,-14)*{\lcupef};
  (13,-12)*{\scs i}; (13,5)*{\scs k};
   (-18,-18)*{\lambda'};
  \endxy} \;\;
  \vcenter{\xy 0;/r.16pc/:
 (-4,-15)*{}; (-20,25) **\crv{(-3,-6) & (-20,4)}?(0)*\dir{<}?(.6)*\dir{}+(0,0)*{\bullet};
 (-12,-15)*{}; (-4,25) **\crv{(-12,-6) & (-4,0)}?(0)*\dir{<}?(.6)*\dir{}+(.2,0)*{\bullet};
 ?(0)*\dir{<}?(.75)*\dir{}+(.2,0)*{\bullet};?(0)*\dir{<}?(.9)*\dir{}+(0,0)*{\bullet};
 (-28,25)*{}; (-12,25) **\crv{(-28,10) & (-12,10)}?(1)*\dir{>};
  ?(.2)*\dir{}+(0,0)*{\bullet}?(.35)*\dir{}+(0,0)*{\bullet};
 (-36,-15)*{}; (-36,25) **\crv{(-34,-6) & (-35,4)}?(1)*\dir{>};
 (-28,-15)*{}; (-42,25) **\crv{(-28,-6) & (-42,4)}?(1)*\dir{>};
 (-42,-15)*{}; (-20,-15) **\crv{(-42,-5) & (-20,-5)}?(1)*\dir{>};
 (6,10)*{\cbub{m}{}};
 (-23,0)*{\cbub{}{}};
 (-2,-12)*{\scs i}; (-14,-12)*{\scs k};  (-19,-12)*{\scs i};
    (-46,22)*{\scs \ell}; (-33,22)*{\scs i}; (-10,22)*{\scs j};
    (8,18)*{\scs j}; (-20,7)*{\scs \ell};
 \endxy}
 \vcenter{ \xy 0;/r.16pc/: (-14,8)*{\xybox{
 (0,-10)*{}; (-16,10)*{} **\crv{(0,-6) & (-16,6)}?(.5)*\dir{};
 (-16,-10)*{}; (-8,10)*{} **\crv{(-16,-6) & (-8,6)}?(1)*\dir{}+(.1,0)*{\bullet};
  (-8,-10)*{}; (0,10)*{} **\crv{(-8,-6) & (-0,6)}?(.6)*\dir{}+(.2,0)*{\bullet}?
  (1)*\dir{}+(.1,0)*{\bullet};
  (0,10)*{}; (-16,30)*{} **\crv{(0,14) & (-16,26)}?(1)*\dir{>};
 (-16,10)*{}; (-8,30)*{} **\crv{(-16,14) & (-8,26)}?(1)*\dir{>};
  (-8,10)*{}; (0,30)*{} **\crv{(-8,14) & (-0,26)}?(1)*\dir{>}?(.6)*\dir{}+(.25,0)*{\bullet};
 (-18,-8)*{\scs i}; (-6,-8)*{\scs i}; (2,-8)*{\scs k};
   }};
 (5,0)*{\lambda};
 \endxy}$
\caption{An example of a diagram representing a 2-morphism in $\Ucat(\mf{g})$ from
$
\cal{E}_i^2\cal{E}_{\ell}\cal{F}_i \cal{F}_k \cal{F}_i \cal{E}_i\cal{E}_i \cal{E}_k \onel
$
to $
 \cal{E}_{\ell} \cal{E}_i \cal{F}_j \cal{F}_j \cal{F}_i \cal{E}_j \cal{E}_i \cal{E}_k \cal{E}_i\onel\la t\ra
$.  The degree $\la t \ra$ of this 2-morphism is determined by the relationship between the simple roots $i,j,k, \ell$ in the Cartan datam associated to $\mf{g}$.} \label{fig_Ucat-diagram}
\end{figure}

Extending the split Grothendieck group decategorification map for linear categories, it is possible to define the split Grothendieck group $K_0$ of a linear 2-category.  It was shown in \cite{KL3} for $\mf{g}=\mf{sl}_n$ that applying this notion of decategorification to the Karoubi envelope $\UcatD(\mf{sl}_n)$ of the 2-category $\Ucat(\mf{sl}_n)$ produces the integral idempotented form of the quantum enveloping algebra $\mathbf{U}_q(\mf{sl}_n)$.  Hence, with this notion of decategorification the 2-category $\UcatD(\mf{sl}_n)$ can be viewed as a categorification of the quantum group $\mathbf{U}_q(\mf{sl}_n)$.  The $n=2$ case of this result was proven in~\cite{Lau1} and the case of general $\mf{g}$ appears in \cite{Web5}.  For a closely related construction see ~\cite{Rou2}.


More recently it has been shown that using a 2-categorical analog of the trace as the decategorification map produces some very rich structures~\cite{BHLZ,Marko,BGHL}.   The trace relation can be realized diagrammatically by considering the diagrams for $\Ucat(\mf{g})$ on an annulus.
\[
 \vcenter{ \xy 0;/r.16pc/:
 (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-2,-.6) to (-2,.6) .. controls ++(0,1.85) and ++(0,1.85) .. (2,.6)
   to (2,-.6)  .. controls ++(0,-1.85) and ++(0,-1.85) .. (-2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.25,0) .. controls ++(0,.35) and ++(0,.35) .. (0.25,0)
            .. controls ++(0,-.35) and ++(0,-.35) .. (-0.25,0);
\end{tikzpicture}}
 };
(10,8)*{\lambda}; (-15,12)*{\lambda'};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};

 
 (8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
(-2,-3)*{\scs i}; (-15,-3)*{\scs i};
 (-10,1)*{\bullet};
 \endxy}
\]
The invariance of the graphical calculus of $\Ucat(\mf{g})$ under planar deformations allows us to slide portions of the diagram around the annulus imposing the trace relation.
