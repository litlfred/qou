---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-020-labeling-of-the-triangulation
section_title: "Labeling of the triangulation"
section_number: null
pages: 29-31
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.956
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
To define the state sum of a generic  transversal    triangulated 3-manifold with defect data, we assign   objects and morphisms of the associated categories to the edges and triangles of the triangulation. For this,  we fix sets  $I$ of representatives of the isomorphism classes of simple objects and associated projection and inclusion morphisms $p^\alpha_{xi}: x\to i$ and $j^\alpha_{xi}: i\to x$ satisfying \eqref{eq:projincl} 
 for all spherical fusion categories at the regions of $M$ and for all bimodule categories at the defect areas.

\begin{definition} \label{def:label} Let $M$ be generic transversal   triangulated 3-manifold with defect data. A {\bf labeling} of $M$  is an assignment of the following data to the edges of the triangulation:
\begin{compactenum}[(i)]
\item to each 
edge $e$ contained in a region labeled by  $\mac$, a simple object $l(e)\in I_{\mac}$,
\item to each  
edge $e$ that intersects a defect area labeled $\mam$, a  simple object $l(e)\in I_{\mam}$.
\end{compactenum}
A  pair $(M,l)$ of a generic  transversal  triangulated 3-manifold $M$ with defect data  and a labeling $l$ is called a {\bf labeled defect 3-manifold}.
\end{definition}

Note that the orientation of the edges  from Section \ref{subsec:triangsec}  is arbitrary in (i), but fixed by the orientations of the defect  surfaces  in (ii). In (i) we would assign to the edge with the opposite orientation the unique object in $I_\mac$ that represents the isomorphism class of the dual object $l(e)^*$. In (ii) orientation could only be reversed simultaneously for all edges of a tetrahedron  that intersect a  defect surface. This would amount to reversing the orientation of each defect area  and replacing its bimodule category $\mathcal M$ by $\mathcal M^\#$, as explained in Section \ref{subsec:triangsec}.
In this case, we would assign to the edge with the opposite orientation  the same object as an object of  $\mam^\#$.



A labeling of a triangulated manifold with defect data defines a labeling of each triangle in the triangulation. To each labeled triangle, we associate two morphism spaces,
 one for each orientation. 
 For a triangle labeled by objects in $(\mac,\mad)$-bimodule categories $\mam$, $\man$ that intersects a defect line labeled by a bimodule  functor  $F:\mam\to\man$ or  $G:\man\to\mam$, the associated morphisms spaces are 

\begin{align}\label{pic:homspace}
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n\in I_\man$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m\in I_\mam$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c\in I_\mac$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (0,3)--(3,0) node[midway, anchor=south west]{$m\in I_\mam$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=red] (0,3)--(-3,0) node[midway, anchor=south east]{$n\in I_\man$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c\in I_\mac$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\end{tikzpicture}
&
&\begin{array}{ll}
+: \Hom_\man(F(c\rhd m), n)\\
-: \Hom_\man(n, F(c\rhd m))
\end{array}
\\
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n\in I_\man$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m\in I_\mam$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c\in I_\mac$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\end{tikzpicture}
&
&
\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (0,3)--(3,0) node[midway, anchor=south west]{$m\in I_\mam$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=red] (0,3)--(-3,0) node[midway, anchor=south east]{$n\in I_\man$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c\in I_\mac$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\end{tikzpicture}
&
&\begin{array}{ll}
+: \Hom_\mam(c\rhd m, G(n))\\
-: \Hom_\mam(G(n), c\rhd m)
\end{array}\nonumber\\
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (3,0)--(0,-3) node[midway, anchor=north west]{$n\in I_\man$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (-3,0)--(0,-3) node[midway, anchor=north east]{$m\in I_\mam$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt, gray] (3,0)--(-3,0) node[midway, anchor=south]{$d\in I_\mad$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,-.8)--(0,-1.4) node[midway,anchor=west]{$F$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (3,0)--(0,-3) node[midway, anchor=north west]{$m\in I_\mam$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=red] (-3,0)--(0,-3) node[midway, anchor=north east]{$n\in I_\man$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt, gray] (-3,0)--(3,0) node[midway, anchor=south]{$d\in I_\mad$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,-.8)--(0,-1.4) node[midway,anchor=west]{$F$};
\end{tikzpicture}
&
&\begin{array}{ll}
+: \Hom_\man(F(m\lhd d),n)\\
-: \Hom_\man(n,F(m\lhd d))\\
\end{array}\nonumber
\\
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (3,0)--(0,-3) node[midway, anchor=north west]{$n\in I_\man$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (-3,0)--(0,-3) node[midway, anchor=north east]{$m\in I_\mam$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt, gray] (3,0)--(-3,0) node[midway, anchor=south]{$d\in I_\mad$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,-.8)--(0,-1.4) node[midway,anchor=west]{$G$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (3,0)--(0,-3) node[midway, anchor=north west]{$m\in I_\mam$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=red] (-3,0)--(0,-3) node[midway, anchor=north east]{$n\in I_\man$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt, gray] (-3,0)--(3,0) node[midway, anchor=south]{$d\in I_\mad$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,-.8)--(0,-1.4) node[midway,anchor=west]{$G$};
\end{tikzpicture}
&
&\begin{array}{ll}
+:\Hom_\mam(m\lhd d, G(n))\\
-:\Hom_\mam(G(n), m\lhd d).
\end{array}\nonumber
\end{align}
Here, the triangles are equipped with the orientation induced by their edge orientation and the embedding in the plane, via the right-hand rule. The first triangle in each line has positive (+) and the second negative (-) orientation. The arrows  indicate the orientation of the defect line relative to the orientation of the triangle. They agree, if the arrow points downwards, and are opposite, if it points upwards. As the orientation of the defect lines is fixed, reversing the orientation of the triangle reverses the  orientation of this arrow.



The morphism spaces are obtained from the triangles as follows: 
The objects in $\mac$ and $\mad$  act on the object of $\mam$ or $\man$ with whom they share a vertex with one incoming and one outgoing edge. Arrows labeled with $\mac$ have this vertex as their starting vertex, arrows labeled by $\mad$ as their target vertex. 
The morphisms go from the object on the left to the one on the right. The functor is applied to the object on the left, if its arrow points downwards, and to the one on the right, if it points upwards.

For $\mam=\man$ and $F=G=\id_\mam$,  the diagrams in the first and the second row and in the third and the fourth row in \eqref{pic:homspace} coincide. Setting $\mam=\man=\mac$, $\rhd=\oo=\lhd$ and $F=G=\id_\mac$  yields the usual assignment of morphisms to triangles for the Turaev-Viro-Barrett-Westbury invariants of a spherical fusion category.
