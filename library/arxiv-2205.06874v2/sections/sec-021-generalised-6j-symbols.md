---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-021-generalised-6j-symbols
section_title: "Generalised 6j symbols"
section_number: null
pages: 31-37
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.97
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
We now associate a generalised 6j symbol to each  labeled generic  transversal tetrahedron $t$ with a defect surface. Note that such a defect tetrahedron  is more than a combinatorial tetrahedron with categorical data assigned to each oriented edge. It consists of a combinatorial tetrahedron $t$, an oriented defect polygon $P$,  an assignment of certain edges of $t$ to the vertices  of $P$ and an assignment of the vertices of $t$ to the two regions labeled by $\mac$ and $\mad$. 
  In particular,  a labeled generic  transversal tetrahedron inherits an orientation, because the defect surface is oriented and assigning $\mac$ and $\mad$ to the two sides of the surface specifies a positive normal vector to the surface
  
  \begin{figure} 
\centering
\def\svgwidth{.85\columnwidth}

\caption{Projecting the data from spherical categories on the polygon.}
\label{fig:projecting}
\end{figure}
  
   The orientation of $t$ induces an orientation of all of its triangles. To each oriented triangle we assign a morphism in the associated morphism space from \eqref{pic:homspace}. 
To a tetrahedron with these assignments, we  associate a polygon diagram $D$ as follows:

\begin{enumerate}
\item The  defect surface in $t$ is a polygon $P$.  The defect data in $P$, viewed from the region labeled  $\mac$ towards the region labeled $\mad$, defines a cyclic equivalence class of  diagrams for $\Bimod^\theta(\mac,\mad)$. 

\item Pushing the endpoints of defect lines on each side of $P$ to the middle without creating crossings does not change the cyclic equivalence class of the diagram. We thus assume that each side of $P$ is the endpoint of exactly one defect line as  in Figure \ref{fig:dectet}, possibly labeled with  a composite of functors.  

\item Draw  $t$  such that  edges and triangles labeled by data from $\mac$ and $\mad$ lie on the corresponding sides of the polygon $P$ and that edges intersecting $P$ are oriented by the positive normal vector of $P$. 

\item For each edge $e$ of $t$ that does not intersect $P$, draw the dual edge $\bar e$, starting and ending
 on the boundary  $\partial P$ and with its endpoints are displaced slightly from the endpoints of defect lines. They are displaced  towards the starting and target end of $e$, if $e$ is contained in the region for $\mac$ and $\mad$, respectively.
Orient $\bar e$ by duality, as shown in Figure \ref{fig:projecting}, and project it on $P$.

\item Label the vertices of $P$ with the simple objects of the associated edges of $t$ and the projected edges  with the simple objects 
 of their duals in $t$. Label the endpoints of defect lines and the projected vertices in $P$ with the morphisms assigned to the corresponding triangles in $t$. The result is a polygon diagram $D$.  The diagrams for the tetrahedra in Figures \ref{fig:dectet} and \ref{fig:projecting} are  shown in \eqref{fig:diagramproj}.
\end{enumerate}





Note that the word \emph{project} in 3.~is used informally here. For the tetrahedron in Figure \ref{fig:projecting} (a) it means  drawing a trivalent vertex on $P$  whose incident edges are connected with the endpoints on $\partial P$. For the tetrahedron in Figure \ref{fig:projecting} (b) it amounts to drawing two edges that connect  endpoints on opposite sides of $P$. The properties of diagrams for spherical fusion categories and identities \eqref{pic:rm2} to \eqref{pic:bimodulenat} ensure that all ways of doing so yield polygon diagrams with the same evaluation.  


Note also that  tetrahedra that do not intersect defect surfaces can be viewed as special cases of Figure \ref{fig:dectet} (a) and (b). 
Each such tetrahedron has one vertex with only outgoing  edges, which can be taken as the lower vertex in Figure \ref{fig:dectet} (a) or as the left vertex in Figure \ref{fig:dectet}  (b). 
Up to  orientation reversal  the tetrahedron then coincides with the one in  Figure \ref{fig:dectet} (a) or (b), if the defect surfaces  are labeled with the spherical fusion category $\mac$  as a $(\mac,\mac)$-bimodule category, with identity functors and with  identity natural transformations. 

Interpreting a combinatorial tetrahedron as a tetrahedron with trivial defects amounts to a choice of orientation: one needs to specify an orientation for the trivial defect surface and to specify its  normal vector. We therefore  treat \emph{oriented} tetrahedra labeled by a spherical fusion category $\mac$  as generic transversal tetrahedra with trivial defect data.  In the following, we assume that all tetrahedra are equipped with an orientation. 

\begin{definition}\label{def:gen6j}
Let $(t,l)$ be a labeled generic transversal tetrahedron  with an assignment $b$ of morphisms in the spaces \eqref{pic:homspace} to its triangles.
The {\bf generalised 6j symbol} $\mathrm{6j}(t,l,b)$  is the cyclic evaluation  of the associated polygon diagram $D$. This defines a linear map
$$
\mathrm{6j}(t): \bigotimes_{f\in\Delta} \Hom(f,l)\to \C, \quad b\mapsto \mathrm{6j}(t,l,b),
$$
where $\Delta$ denotes the set of triangles of $t$,  $\Hom(f,l)$ the  morphism space from \eqref{pic:homspace}  for a triangle $f\in \Delta$ and the tensor product stands for the unordered tensor product of these morphism spaces for all triangles.
\end{definition}



\begin{example}
The generalised 6j symbols for the tetrahedra in Figure \ref{fig:dectet}  are the cyclic evaluations of  
\begin{align}\label{fig:diagramproj}
\begin{tikzpicture}[scale=.35]
\draw[line width=1.5pt, color=blue] (-4,-1)--(0,-6) node[anchor=north]{$m$}--(4,-1);
\draw[line width=1.5pt, color=violet] (-4,-1)--(-8,4) node[anchor=east]{$p$}--(0,4);
\draw[line width=1.5pt, color=red] (0,4)--(8,4)node[anchor=west]{$n$}--(4,-1) ;
\draw[line width=1pt, dashed] (-1,0)--(0,4) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[midway, anchor=south west]{$H$};
\draw[line width=1pt, dashed] (-4,-1)--(-1,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[midway, anchor=north]{$F$};
\draw[line width=1pt, dashed] (-1,0)--(4,-1) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[midway, anchor=north]{$G$};
\draw[fill=white, color=white] (-.7,1.4) circle(.3);
\draw[line width=.5pt] (-4,-1)--(-2,2) node[sloped, pos=0.5, allow upside down]{\arrowOut} node[midway, anchor=east]{$i\,$};
\draw[line width=.5pt] (-2,2)--(0,4) node[sloped, pos=0.5, allow upside down]{\arrowOut} node[midway, anchor=east]{$k\,$};
\draw[line width=.5pt] (-2,2)--(4,-1) node[sloped, pos=0.5, allow upside down]{\arrowOut} node[midway, anchor=south]{$j$};
\draw[fill=black, color=black] (-1,0) circle (.2) node[anchor=south east]{$\nu$};
\draw[fill=black, color=black] (-2,2) circle (.2) node[anchor=east]{$\alpha$};

\draw[fill=red, color=red] (0,4) circle (.2) node[anchor=south]{$\gamma$};
\draw[fill=blue, color=blue] (-4,-1) circle (.2) node[anchor=north east]{$\beta$};
\draw[fill=blue, color=blue] (4,-1) circle (.2) node[anchor=north west]{$\delta$};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=.35]
\draw[line width=1.5pt, color=violet] (-6,0)--(-6,6) node[anchor=south east]{$p$}--(0,6);
\draw[line width=1.5pt, color=cyan] (0,6)--(6,6) node[anchor=south west]{$q$}--(6,0);
\draw[line width=1.5pt, color=red] (6,0)--(6,-6) node[anchor=north west]{$n$}--(0,-6);
\draw[line width=1.5pt, color=blue] (0,-6)--(-6,-6) node[anchor=north east]{$m$}--(-6,0);
\draw[line width=.5pt, color=gray] (0,6).. controls (3,0).. (0,-6) node[sloped, pos=0.6, allow upside down]{\arrowOut} node[midway, anchor=north west]{$d$};
\draw[fill=white, color=white] (2.3,0) circle(.3);
\draw[fill=white, color=white] (2,-2) circle(.3);
\draw[line width=1pt, dashed] (0,6)--(0,0) node[sloped, pos=0.6, allow upside down]{\arrowIn} node[midway, anchor=west]{$F$};
\draw[line width=1pt, dashed] (6,0)--(0,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[midway, anchor=south]{$G$};
\draw[line width=1pt, dashed] (0,0)--(-6,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[midway, anchor=south]{$H$};
\draw[line width=1pt, dashed] (0,0)--(0,-6) node[sloped, pos=0.6, allow upside down]{\arrowIn} node[midway, anchor=west]{$K$};
\draw[fill=white, color=white] (0,-2.3) circle(.3);
\draw[line width=.5pt,] (6,0).. controls (0,-3).. (-6,0) node[sloped, pos=0.6, allow upside down]{\arrowOut} node[midway, anchor=north east]{$c\;\;\;$};
\draw[fill=black, color=black] (0,0) circle (.2) node[anchor=south east]{$\nu$};

\draw[fill=violet, color=violet] (0,6) circle (.2) node[anchor=south]{$\alpha$};
\draw[fill=cyan, color=cyan] (6,0) circle (.2) node[anchor=west]{$\beta$};
\draw[fill=blue, color=blue] (0,-6) circle (.2) node[anchor=north]{$\gamma$};
\draw[fill=violet, color=violet] (-6,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}
\end{align}
and given by the diagrams
\begin{align}\label{fig:6jgeneral}
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[midway, anchor=south east]{$F$};
\draw[line width=.5pt, color=black] (0,4)--(-2,1)  node[midway, anchor=west]{$i$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[midway, anchor=north]{$H$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-1)  node[midway, anchor=south]{$k$};

\draw[color=white, fill=white] (-1.4,-.5) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[midway, anchor=north east]{$G$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-4)  node[midway, anchor=west]{$j$};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\;$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}

\qquad\qquad\qquad\qquad
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=violet] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=cyan] (0,4)--(0,1) node[midway, anchor=west]{$q$};
\draw[line width=1.5pt, color=red] (0,1)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,-4)--(0,-5);

\draw[line width=.5pt, color=gray] (0,4) .. controls (-2,2.5)  and (-2,.5).. (0,-1) node[midway, anchor=west]{$d$};
\draw[color=white, fill=white] (-1.1,.83) circle (.4);
\draw[color=white, fill=white] (-.8,0) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (0,4) --(-5,0)  node[midway, anchor=south east]{$F$};
\draw[line width=1pt, color=black, style=dashed] (0,1) --(-5,0) node[midway, anchor=south]{$\;\;G$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-1)  node[midway, anchor=north]{$\;\;K$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-4) node[midway, anchor=north east]{$H$};

\draw[color=white, fill=white] (-1.2,-.83) circle (.4);

\draw[line width=.5pt, color=black] (0,-4) .. controls (-2,-2.5)  and (-2,-.5).. (0,1) node[midway, anchor=west]{$c$};

\draw[color=violet, fill=violet] (0,4) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[color=cyan, fill=cyan] (0,1) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-5,0) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\end{align}
\end{example}




Definition \ref{def:gen6j} also defines the usual 6j symbols of tetrahedra labeled by a spherical fusion category $\mac$  that occur in the Turaev-Viro-Barrett-Westbury state sum. 
However, they are not defined as 6j symbols of combinatorial tetrahedra, as in \cite{BW}, but as 6j symbols of \emph{oriented} combinatorial tetrahedra. 

The 6j symbols from Definition \ref{def:gen6j} 
encode the natural transformations on the defect polygon and the coherence isomorphisms for the defect data. If the former are trivial, we obtain the following cases:

\begin{itemize}
\item If  $\map=\man=\mam$, $F=G=H=\id_\mam$ and $\nu=\id_{\id_\mam}$ for the tetrahedron in Figure \ref{fig:dectet} (a) and the associated 6j symbol in  \eqref{fig:6jgeneral}, we obtain a number that characterises the isomorphism $c_{j,k,p}: (j\oo k)\rhd p\to j\rhd (k\rhd p)$ from Definition \ref{def:modulecat}. 
It follows from \eqref{eq:projincl} that it is given by
\begin{align}\label{eq:c6j}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$c_{j,k,p}=\sum_{\substack{{i,m,n}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(i)$};
\node at (-6,0) {$\dim(m)$};
\node at (-6,-1) {$\dim(n)$};
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,-5);

\node at (0,1.5)[anchor=west, color=blue] {$p$};
\node at (0,-1.5)[anchor=west, color=blue] {$n$};

\draw[line width=.5pt, color=black] (0,3) --(-3,1)  node[midway, anchor=south east]{$i$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0)  node[midway, anchor=south west]{$k$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3)  node[midway, anchor=north east]{$j$};

\draw[color=blue, fill=blue] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,0) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\alpha\;$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt] (-4,5)node[anchor=south]{$j$}--(-3,4);
\draw[line width=.5pt] (-2,5)node[anchor=south]{$k$}--(-3,4);
\draw[line width=.5pt] (-3,4)--(0,1) node[midway, anchor=north east]{$i$};
\draw[line width=.5pt] (0,-1)--(-4,-5) node[anchor=north]{$j$};
\draw[line width=.5pt] (0,-3)--(-2,-5) node[anchor=north]{$k$};
\draw[color=blue, line width=1.5pt] (0,5)node[anchor=south]{$p$}--(0,-5) node[anchor=north]{$p$} node[midway, anchor=west]{$m$};
\node at (0,-2) [color=blue, anchor=west]{$n$};

\draw[fill=black] (-3,4) circle (.2) node[anchor=east]{$\alpha$};
\draw[fill=blue, color=blue] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[fill=blue, color=blue] (0,-1) circle (.2) node[anchor=west]{$\;\delta$};
\draw[fill=blue, color=blue] (0,-3) circle (.2) node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}
where the sum runs over  simple objects $i\in I_\mac$, $m,p\in I_\mam$ and  bases of the associated  morphism spaces. 

There is an analogous generalised 6j symbol for $\mad$-right module categories, which arises from a tetrahedron analogous to Figure \ref{fig:dectet} (a), but with a vertex in the region labeled by $\mad$ and with the orientations of the coloured edges reversed. 

\item In particular, if  $\mam$ is a spherical fusion category $\mac$ as a left module category over itself, we obtain the usual 6j symbol for the spherical fusion category $\mac$ that encodes the associator on simple objects:
\begin{align}\label{eq:a6j}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$a_{j,k,p}=\sum_{\substack{{i,m,n}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(i)$};
\node at (-6,0) {$\dim(m)$};
\node at (-6,-1) {$\dim(n)$};
\draw[line width=.5pt] (-1,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=.5pt, ] (-1,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=.5pt,] (0,5)--(0,-5);

\node at (0,1.5)[anchor=west, ] {$p$};
\node at (0,-1.5)[anchor=west, ] {$n$};

\draw[line width=.5pt, color=black] (0,3) --(-3,1)  node[midway, anchor=south east]{$i$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0)  node[midway, anchor=south west]{$k$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3)  node[midway, anchor=north east]{$j$};

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\alpha\;$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt] (-4,5)node[anchor=south]{$j$}--(-3,4);
\draw[line width=.5pt] (-2,5)node[anchor=south]{$k$}--(-3,4);
\draw[line width=.5pt] (-3,4)--(0,1) node[midway, anchor=north east]{$i$};
\draw[line width=.5pt] (0,-1)--(-4,-5) node[anchor=north]{$j$};
\draw[line width=.5pt] (0,-3)--(-2,-5) node[anchor=north]{$k$};
\draw[color=black, line width=.5pt] (0,5)node[anchor=south]{$p$}--(0,-5) node[anchor=north]{$p$} node[midway, anchor=west]{$m$};
\node at (0,-2) [color=black, anchor=west]{$n$};

\draw[fill=black] (-3,4) circle (.2) node[anchor=east]{$\alpha$};
\draw[fill=black, color=black] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[fill=black, color=black] (0,-1) circle (.2) node[anchor=west]{$\;\delta$};
\draw[fill=black, color=black] (0,-3) circle (.2) node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}


\item Setting $\maq=\map=\man=\mam$,  $F=G=H=K=\id_\mam$ and $\nu=\id_{\id_\mam}$   in Figure \ref{fig:dectet} (b) and  \eqref{fig:6jgeneral}  yields the 6j symbol that characterises the isomorphism $b_{c,n,d}: (c\rhd n)\lhd d\to c\rhd (n\lhd d)$ from Definition \ref{def:modulecat}: 
\begin{align}\label{eq:6jb}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$b_{c,n,d}=\sum_{\substack{{m,p,q}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(m)$};
\node at (-6,0) {$\dim(p)$};
\node at (-6,-1) {$\dim(q)$};
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,-5);
\draw[line width=.5pt, color=gray] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=south east]{$d$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[line width=.5pt, color=black] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor=south east]{$c$};
\node at (0,2)[anchor=west, color=blue] {$q$};
\node at (0,0)[anchor=west, color=blue] {$n$};
\node at (0,-2)[anchor=west, color=blue] {$m$};

\draw[color=blue, fill=blue] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=blue, fill=blue] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt, color=gray] (-4,5) node[anchor=south]{$d$}--(0,1);
\draw[line width=.5pt, color=black] (-2,5) node[anchor=south]{$c$}--(0,3);
\draw[line width=1.5pt, color=blue] (0,5) node[anchor=south]{$n$}--(0,-5)  node[anchor=north]{$n$};
\node at (0,2) [anchor=west, color=blue]{$q$};
\node at (0,0) [anchor=west, color=blue]{$p$};
\node at (0,-2) [anchor=west, color=blue]{$m$};
\draw[line width=.5pt, color=black] (-4,-5) node[anchor=north]{$c$}--(0,-1);
\draw[line width=.5pt, color=gray] (-2,-5) node[anchor=north]{$d$}--(0,-3);
\draw[color=blue, fill=blue] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,1) circle (.2)node[anchor=west]{$\;\alpha$};
\draw[color=blue, fill=blue] (0,-1) circle (.2)node[anchor=west]{$\;\delta$};
\draw[color=blue, fill=blue] (0,-3) circle (.2)node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}



\item  In particular, for $\mam=\mac=\mad$ identity  \eqref{eq:6jb}  yields  the usual 6j symbol for a spherical fusion category $\mac$ that encodes its associator, but in  
 a  diagrammatic representation different from \eqref{eq:a6j}
  \begin{align}\label{eq:6ja2}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$a_{c,n,d}=\sum_{\substack{{m,p,q}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(m)$};
\node at (-6,0) {$\dim(p)$};
\node at (-6,-1) {$\dim(q)$};
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=south east]{$d$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[line width=.5pt, color=black] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor=south east]{$c$};
\node at (0,2)[anchor=west, color=black] {$q$};
\node at (0,0)[anchor=west, color=black] {$n$};
\node at (0,-2)[anchor=west, color=black] {$m$};

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=black, fill=black] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=black, fill=black] (0,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt, color=black] (-4,5) node[anchor=south]{$d$}--(0,1);
\draw[line width=.5pt, color=black] (-2,5) node[anchor=south]{$c$}--(0,3);
\draw[line width=.5pt, color=black] (0,5) node[anchor=south]{$n$}--(0,-5)  node[anchor=north]{$n$};
\node at (0,2) [anchor=west, color=black]{$q$};
\node at (0,0) [anchor=west, color=black]{$p$};
\node at (0,-2) [anchor=west, color=black]{$m$};
\draw[line width=.5pt, color=black] (-4,-5) node[anchor=north]{$c$}--(0,-1);
\draw[line width=.5pt, color=black] (-2,-5) node[anchor=north]{$d$}--(0,-3);
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=black, fill=black] (0,1) circle (.2)node[anchor=west]{$\;\alpha$};
\draw[color=black, fill=black] (0,-1) circle (.2)node[anchor=west]{$\;\delta$};
\draw[color=black, fill=black] (0,-3) circle (.2)node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}


\item If we set $\maq=\map$, $\man=\mam$,  $G=H: \mam\to\map$, $F=\id_\map$, $K=\id_\mam$, $\nu=\id_{G}$ and $c=e$ in Figures \ref{fig:dectet} (b) and \eqref{fig:6jgeneral}, we obtain the 6j symbol for the isomorphism $t^G_{n,d}: G(n)\lhd d\to G(n\lhd d)$ from Definition \ref{def:modulefunc}:
\begin{align}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$t^G_{n,d}=\sum_{\substack{{m,p,q}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(m)$};
\node at (-6,0) {$\dim(p)$};
\node at (-6,-1) {$\dim(q)$};
\draw[line width=1.5pt, color=violet] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,1);
\draw[line width=1.5pt, color=violet] (0,-3)--(0,-5);
\draw[line width=1.5pt, color=blue] (0,1)--(0,-3);
\draw[line width=.5pt, color=gray] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=south east]{$d$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[line width=1pt, color=black, dashed] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor=south east]{$G$};
\node at (0,2)[anchor=west, color=violet] {$q$};
\node at (0,0)[anchor=west, color=blue] {$n$};
\node at (0,-2)[anchor=west, color=blue] {$m$};

\draw[color=violet, fill=violet] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=violet, fill=violet] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt, color=gray] (-4,5) node[anchor=south]{$d$}--(0,1);
\draw[line width=1pt, color=black, dashed] (-2,5) node[anchor=south]{$G$}--(0,3);
\draw[line width=1.5pt, color=blue] (0,5) node[anchor=south]{$n$}--(0,3);  
\draw[line width=1.5pt, color=blue] (0,-1)-- (0,-5)  node[anchor=north]{$n$};
\draw[line width=1.5pt, color=violet] (0,-1)-- (0,3) ;
\node at (0,2) [anchor=west, color=violet]{$q$};
\node at (0,0) [anchor=west, color=violet]{$p$};
\node at (0,-2) [anchor=west, color=blue]{$m$};
\draw[line width=1pt, color=black, dashed] (-4,-5) node[anchor=north]{$G$}--(0,-1);
\draw[line width=.5pt, color=gray] (-2,-5) node[anchor=north]{$d$}--(0,-3);
\draw[color=violet, fill=violet] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=violet, fill=violet] (0,1) circle (.2)node[anchor=west]{$\;\alpha$};
\draw[color=violet, fill=violet] (0,-1) circle (.2)node[anchor=west]{$\;\delta$};
\draw[color=blue, fill=blue] (0,-3) circle (.2)node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}


\item Setting instead $\map=\mam$, $\maq=\man$, $F=K: \man\to\mam$, $G=\id_\man$, $H=\id_\mam$, $\nu=\id_{F}$ and $d=e$  in Figures \ref{fig:dectet} (b) and  \eqref{fig:6jgeneral}  yields the 6j symbol for the isomorphism $s^F_{c,n}: F(c\rhd n)\to c\rhd F(n)$ from Definition \ref{def:modulefunc}: 
\begin{align}
\begin{tikzpicture}[scale=.38, baseline=(current bounding box.center)]
\node at (-11,0) {$s^F_{c,n}=\sum_{\substack{{m,p,q}\\{\alpha,\beta,\gamma,\delta}}}$};
\node at (-6,1) {$\dim(m)$};
\node at (-6,0) {$\dim(p)$};
\node at (-6,-1) {$\dim(q)$};
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,3);
\draw[line width=1.5pt, color=blue] (0,-1)--(0,-5);
\draw[line width=1.5pt, color=red] (0,-1)--(0,3);
\draw[line width=1pt, dashed] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=south east]{$F$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[line width=.5pt, color=black] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor=south east]{$c$};
\node at (0,2)[anchor=west, color=red] {$q$};
\node at (0,0)[anchor=west, color=red] {$n$};
\node at (0,-2)[anchor=west, color=blue] {$m$};

\draw[color=blue, fill=blue] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=red, fill=red] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=1pt, dashed] (-4,5) node[anchor=south]{$F$}--(0,1);
\draw[line width=.5pt, color=black] (-2,5) node[anchor=south]{$c$}--(0,3);
\draw[line width=1.5pt, color=red] (0,5) node[anchor=south]{$n$}--(0,1);
\draw[line width=1.5pt, color=red] (0,-3)--(0,-5)  node[anchor=north]{$n$};
\draw[line width=1.5pt, color=blue] (0,-3)--(0,1);
\node at (0,2) [anchor=west, color=red]{$q$};
\node at (0,0) [anchor=west, color=blue]{$p$};
\node at (0,-2) [anchor=west, color=blue]{$m$};
\draw[line width=.5pt, color=black] (-4,-5) node[anchor=north]{$c$}--(0,-1);
\draw[line width=1pt, dashed] (-2,-5) node[anchor=north]{$F$}--(0,-3);
\draw[color=red, fill=red] (0,3) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,1) circle (.2)node[anchor=west]{$\;\alpha$};
\draw[color=blue, fill=blue] (0,-1) circle (.2)node[anchor=west]{$\;\delta$};
\draw[color=blue, fill=blue] (0,-3) circle (.2)node[anchor=west]{$\;\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}
\end{itemize}
In all cases the diagrammatic expressions for the inverses of the coherence isomorphisms 
are obtained  by reflecting  the diagrams on a horizontal axis. This corresponds to evaluating the associated polygon diagrams counterclockwise and to an orientation reversal of the associated defect surface. This is possible, because all of the bimodule natural transformations in these tetrahedra are bimodule natural isomorphisms and hence their directions can be reversed, see the discussion before Definition \ref{def:oppoly}. 



We now investigate how the 6j symbols depend on the orientations of  edges  labeled by objects  in spherical fusion categories. 
Recall that reversing the orientation of such an edge does not affect  the orientations of the adjacent  triangles and tetrahedra. 
Although it induces an odd permutation of the vertex numbers, which may be viewed as an orientation reversal for the associated \emph{combinatorial} tetrahedron, the orientations in our formalism are fixed as part of the data. 

Reversing the orientation of such an edge  and replacing its label by its dual induces natural isomorphisms between the morphism spaces for the adjacent triangles. 
 
 For a $\mac$-module functor  $F:\mam\to\man$ and the first  morphism space from \eqref{pic:homspace}, we obtain
 the following isomorphism
that  is natural in $c\in \Ob\mac$, $m\in\Ob \mam$ and $n\in \Ob\man$
\begin{align}\label{eq:reverse edge}
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\node at (0,-2) {$\Hom_\man(F(c\rhd m), n)$};
\begin{scope}[shift={(7,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=.5pt, color=black] (-1,2) node[anchor=south]{$c$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,2) node[anchor=south]{$F$}--(0,0);
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\alpha$};
 \end{scope}
\end{tikzpicture}
&
&\longrightarrow
&
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c^*$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\node at (0,-2) {$\Hom_\man(F(m), c^*\rhd n)$};
\begin{scope}[shift={(8,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,2) node[anchor=south]{$F$}--(0,0);
\draw[color=white, fill=white]  (-1.4,1.4) circle (.4);
\draw[line width=.5pt, color=black] (0,0).. controls (-.5,2) and (-2,2).. (-2,0);
\draw[line width=.5pt, color=black] (-2,-2) node[anchor=north]{$c$} -- (-2,0) node[sloped, pos=0.5, allow upside down]{\arrowOut} ;
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\alpha$};
 \end{scope}
\end{tikzpicture}\\
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\node at (0,-2) {$\Hom_\man(F(c\rhd m), n)$};
\begin{scope}[shift={(7,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,2) node[anchor=south]{$F$}--(0,0);
\draw[color=white, fill=white] (-1,1) circle (.3);
\draw[line width=.5pt, color=black] (-1,2) node[anchor=south]{$c$}--(-1,0);
\draw[line width=.5pt, color=black] (-1,0) .. controls  (-1,-1) and (-.25, -1) .. (0,0) node[sloped, pos=0.8, allow upside down]{\arrowOut};
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\beta$};
 \end{scope}
\end{tikzpicture}
&
&\longleftarrow
&
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c^*$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, stealth-] (0,.8)--(0,1.4) node[midway,anchor=west]{$F$};
\node at (0,-2) {$\Hom_\man(F(m), c^*\rhd n)$};
\begin{scope}[shift={(8,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,2) node[anchor=south]{$F$}--(0,0);
\draw[line width=.5pt, color=black] (-2,-2) node[anchor=north]{$c$} -- (0,0) node[sloped, pos=0.5, allow upside down]{\arrowOut} ;
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\beta$};
 \end{scope}
\end{tikzpicture}\nonumber
\end{align}
For a $\mac$-module functor  $G:\man\to\mam$ and the third  morphism space from  \eqref{pic:homspace} we have the isomorphism 
\begin{align}\label{eq:reverse edge2}
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\node at (0,-2) {$\Hom_\man(c\rhd m, G(n))$};
\begin{scope}[shift={(7,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,-2) node[anchor=north]{$G$}--(0,0);
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\alpha$};
 \end{scope}
\end{tikzpicture}
&
&\longrightarrow
&
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c^*$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\node at (0,-2) {$\Hom_\man(m, G(c^*\rhd n))$};
\begin{scope}[shift={(8,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,-2) node[anchor=north]{$G$}--(0,0);
\draw[color=white, fill=white]  (-1,-1) circle (.4);
\draw[line width=.5pt, color=black] (-1,0).. controls (-1,1) and (-.25,1).. (0,0);
\draw[line width=.5pt, color=black] (-1,-2) node[anchor=north]{$c$} -- (-1,0) node[sloped, pos=0.7, allow upside down]{\arrowOut} ;
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\alpha$};
 \end{scope}
\end{tikzpicture}\\
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (-3,0)--(3,0) node[midway, anchor=north]{$c$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\node at (0,-2) {$\Hom_\man(c\rhd m, G( n))$};
\begin{scope}[shift={(7,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,-2) node[anchor=north]{$G$}--(0,0);
\draw[color=white, fill=white] (-1.5,-1.5) circle (.3);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(-2,0);
\draw[line width=.5pt, color=black] (-2,0) .. controls  (-2,-2) and (-.5, -2) .. (0,0) node[sloped, pos=0.8, allow upside down]{\arrowOut};
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\beta$};
 \end{scope}
\end{tikzpicture}
&
&\longleftarrow
&
&\begin{tikzpicture}[scale=.45, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=red] (0,3)--(3,0) node[midway, anchor=south west]{$n$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1.5pt, color=blue] (0,3)--(-3,0) node[midway, anchor=south east]{$m$}node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=.5pt] (3,0)--(-3,0) node[midway, anchor=north]{$c^*$} node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=1pt, -stealth] (0,.8)--(0,1.4) node[midway,anchor=west]{$G$};
\node at (0,-2) {$\Hom_\man(m, G(c^*\rhd n))$};
\begin{scope}[shift={(8,0)}]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,-2) node[anchor=north]{$n$}--(0,0);
\draw[line width=1pt, color=black, dashed] (-2,-2) node[anchor=north]{$G$}--(0,0);
\draw[line width=.5pt, color=black] (-1,-2) node[anchor=north]{$c$} -- (0,0) node[sloped, pos=0.5, allow upside down]{\arrowOut} ;
\draw[fill=red, color=red] (0,0) circle (.2) node[anchor=west]{$\beta$};
 \end{scope}
\end{tikzpicture}\nonumber.
\end{align}
The isomorphisms for the other  morphism spaces  from \eqref{pic:homspace}
are analogous, just that the black line labeled $c$ may be replaced by a grey line labeled $d$ that crosses under  the dashed lines for the functors. 

With these transformations of the morphism spaces one finds that reversing the orientation of an edge labeled by a spherical fusion category does not affect the generalised 6j symbols of defect tetrahedra.


\begin{lemma}\label{lem:sphlemma}  The 6j symbol of  a labeled generic transversal tetrahedron is invariant under reversing an edge labeled with an object $c\in I_\mac$ or $d\in I_\mad$, replacing its label with the dual and transforming the morphisms at its triangles according to \eqref{eq:reverse edge} and \eqref{eq:reverse edge2}.
\end{lemma}

\begin{proof} This follows by a direct diagrammatic computation from  \eqref{eq:reverse edge} and \eqref{eq:reverse edge2},  together with identity \eqref{pic:snake}  and the second  identity in \eqref{eq:functortrpivot} for the trace, applied to the black and grey lines of the diagram. It also uses identities \eqref{pic:rm2} to \eqref{pic:bimodulenat}  that encode the  Reidemeister moves and  the naturality conditions for the over- and undercrossings. 
For the first diagram in \eqref{fig:6jgeneral} this yields 
\begin{align*}
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[midway, anchor=south east]{$F$};
\draw[line width=.5pt, color=black] (0,4)--(-2,1)  node[midway, anchor=west]{$i$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[midway, anchor=north]{$H$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-1)  node[midway, anchor=south]{$k$};

\draw[color=white, fill=white] (-1.4,-.5) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[midway, anchor=north east]{$G$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-4)  node[midway, anchor=east]{$j$};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\;$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake}}=

\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-1,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-1,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[midway, anchor=south east]{$F$};
\draw[line width=.5pt, color=black] (0,4)--(-2,1)  node[midway, anchor=west]{$i$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[midway, anchor=north]{$H$};

\draw[color=white, fill=white] (-1.4,-.5) circle (.4);
\draw[color=white, fill=white] (-.8,-.8) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[midway, anchor=north east]{$G$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-4)  node[midway, anchor=east]{$j$};
\draw[line width=.5pt, color=black] (0,-1) .. controls (-1,-3) and (-.7,3)..(-2,1) node[sloped, pos=0.5, allow upside down]{\arrowOut} node[midway, anchor=west]{$k$};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\;$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake},\eqref{eq:functortrpivot}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-3.5,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-3.5,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[pos=.2, anchor=south]{$F$};
\draw[line width=.5pt, color=black] (0,4)--(-2,1)  node[midway, anchor=west]{$i$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[pos=.7, anchor=north]{$H$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-1)  node[pos=.7, anchor=south]{$k$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[pos=.7, anchor=north east]{$G$};

\draw[color=white, fill=white] (-3,2) circle (.4);
\draw[color=white, fill=white] (-2.2,-2) circle (.4);


\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,0) and (-3,0).. (-3,1);
\draw[line width=.5pt, color=black] (-3,1) --(-3,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=east]{$j$};
\draw[line width=.5pt, color=black] (-3,-5) --(-3,-4) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=east]{$j$};
\draw[line width=.5pt, color=black] (-3,-4) .. controls (-3,-1) and (-.5,-1).. (0,-4);

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\end{align*}
\begin{align*}
\stackrel{\eqref{pic:snake}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-3.5,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-3.5,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[pos=.35, anchor=south]{$F$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[pos=.7, anchor=north]{$H$};
\draw[line width=.5pt, color=black] (-2,1) --(0,-1)  node[pos=.7, anchor=south]{$k$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[pos=.7, anchor=north east]{$G$};

\draw[color=white, fill=white] (-3,2) circle (.4);
\draw[color=white, fill=white] (-2.2,-2) circle (.4);
\draw[color=white, fill=white] (-1,3.2) circle (.4);
\draw[color=white, fill=white] (-.6,3.6) circle (.4);


\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,0) and (-3,0).. (-3,1);
\draw[line width=.5pt, color=black] (-3,1) --(-3,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=east]{$j$};
\draw[line width=.5pt, color=black] (-3,-5) --(-3,-4) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=east]{$j$};
\draw[line width=.5pt, color=black] (-3,-4) .. controls (-3,-1) and (-.5,-1).. (0,-4);

\draw[line width=.5pt, color=black] (0,4) .. controls (-.4,2) and (-.75,6).. (-1,3)  node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (-1,3)--(-1,1)   node[midway, anchor=west]{$i$};
\draw[line width=.5pt, color=black] (-1,1) .. controls (-1.25,0) and (-1.75,3).. (-2,1)  node[sloped, pos=0.5, allow upside down]{\arrowOut};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\,$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake},\eqref{eq:functortrpivot}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-4,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-4,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[pos=.35, anchor=south]{$F$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[pos=.7, anchor=north]{$H$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[pos=.7, anchor=north east]{$G$};

\draw[color=white, fill=white] (-3,2) circle (.4);
\draw[color=white, fill=white] (-3.5,1.6) circle (.4);
\draw[color=white, fill=white] (-2.2,-2) circle (.4);
\draw[color=white, fill=white] (-1,3.2) circle (.4);
\draw[color=white, fill=white] (-.6,3.6) circle (.4);
\draw[color=white, fill=white] (-3.2,-1.2) circle (.4);
\draw[color=white, fill=white] (-2.5,0) circle (.4);


\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,.5) and (-3,.5).. (-3,1);
\draw[line width=.5pt, color=black] (-3,1) --(-3,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=west]{$j$};
\draw[line width=.5pt, color=black] (-3,-5) --(-3,-4) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=west]{$j$};
\draw[line width=.5pt, color=black] (-3,-4) .. controls (-3,-1) and (-.5,-1).. (0,-4);

\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,0) and (-3.5,0).. (-3.5,1.5);
\draw[line width=.5pt, color=black] (-3.5,1.5) --(-3.5,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=east]{$k$};
\draw[line width=.5pt, color=black] (-3.5,-5) --(-3.5,-3) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=east]{$k$};
\draw[line width=.5pt, color=black] (0,-1) .. controls (-1,1) and (-3.5,1).. (-3.5,-3);

\draw[line width=.5pt, color=black] (0,4) .. controls (-.4,2) and (-.75,6).. (-1,3)  node[sloped, pos=0.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (-1,3)--(-1,1)   node[midway, anchor=west]{$i$};
\draw[line width=.5pt, color=black] (-1,1) .. controls (-1.25,0) and (-1.75,3).. (-2,1)  node[sloped, pos=0.5, allow upside down]{\arrowOut};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\,$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=blue] (-4,5)--(1,5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-4,-5)--(1,-5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,4)--(0,-1)node[midway, anchor=west]{$p$};
\draw[line width=1.5pt, color=red] (0,-1)--(0,-4) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-5);

\draw[line width=1pt, color=black, style=dashed] (0,4)--(-5,1)  node[pos=.35, anchor=south]{$F$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-1)  node[pos=.7, anchor=north]{$H$};
\draw[line width=1pt, color=black, style=dashed] (-5,1) --(0,-4)  node[pos=.7, anchor=north east]{$G$};

\draw[color=white, fill=white] (-3,2) circle (.4);
\draw[color=white, fill=white] (-3.5,1.6) circle (.4);
\draw[color=white, fill=white] (-2.2,-2) circle (.4);
\draw[color=white, fill=white] (-3.2,-1.2) circle (.4);
\draw[color=white, fill=white] (-2.5,0) circle (.4);


\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,.5) and (-3,.5).. (-3,1);
\draw[line width=.5pt, color=black] (-3,1) --(-3,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=west]{$j$};
\draw[line width=.5pt, color=black] (-3,-5) --(-3,-4) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=west]{$j$};
\draw[line width=.5pt, color=black] (-3,-4) .. controls (-3,-1) and (-.5,-1).. (0,-4);

\draw[line width=.5pt, color=black] (-2,1) .. controls (-2,0) and (-3.5,0).. (-3.5,1.5);
\draw[line width=.5pt, color=black] (-3.5,1.5) --(-3.5,5) node[sloped, pos=0.8, allow upside down]{\arrowOut}  node[pos=.8, anchor=east]{$k$};
\draw[line width=.5pt, color=black] (-3.5,-5) --(-3.5,-3) node[sloped, pos=0.5, allow upside down]{\arrowOut}  node[midway, anchor=east]{$k$};
\draw[line width=.5pt, color=black] (0,-1) .. controls (-1,1) and (-3.5,1).. (-3.5,-3);

\draw[line width=.5pt, color=black] (0,4)--(-2,1)   node[midway, anchor=west]{$i$};

\draw[color=blue, fill=blue] (0,4) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=red, fill=red] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=blue, fill=blue] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-2,1) circle (.15) node[anchor=east]{$\alpha\,$};
\draw[ fill=black] (-5,1) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\end{align*}
and for the second diagram in \eqref{fig:6jgeneral}
\begin{align*}
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=violet] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=cyan] (0,4)--(0,1) node[midway, anchor=west]{$q$};
\draw[line width=1.5pt, color=red] (0,1)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,-4)--(0,-5);

\draw[line width=.5pt, color=gray] (0,4) .. controls (-2,2.5)  and (-2,.5).. (0,-1) node[midway, anchor=west]{$d$};
\draw[color=white, fill=white] (-1.1,.83) circle (.4);
\draw[color=white, fill=white] (-.8,0) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (0,4) --(-5,0)  node[midway, anchor=south east]{$F$};
\draw[line width=1pt, color=black, style=dashed] (0,1) --(-5,0) node[midway, anchor=south]{$\;\;G$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-1)  node[midway, anchor=north]{$\;\;K$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-4) node[midway, anchor=north east]{$H$};

\draw[color=white, fill=white] (-1.2,-.83) circle (.4);

\draw[line width=.5pt, color=black] (0,-4) .. controls (-2,-2.5)  and (-2,-.5).. (0,1) node[midway, anchor=west]{$c$};

\draw[color=violet, fill=violet] (0,4) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[color=cyan, fill=cyan] (0,1) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-5,0) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake},\eqref{eq:functortrpivot}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=violet] (-2,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-2,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=cyan] (0,4)--(0,1) node[midway, anchor=west]{$q$};
\draw[line width=1.5pt, color=red] (0,1)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,-4)--(0,-5);

\draw[line width=.5pt, color=gray] (0,4) .. controls (-.5,2)  and (-1.5,2).. (-1.5,4);
\draw[line width=.5pt, color=gray] (-1.5,4)--(-1.5,5) node[sloped, pos=0.2, allow upside down]{\arrowOut} node[pos=.2, anchor=east]{$d$};
\draw[line width=.5pt, color=gray] (0,-1) .. controls (-.5,1)  and (-1.5,1).. (-1.5,-1);
\draw[line width=.5pt, color=gray] (-1.5,-5)--(-1.5,-1) node[sloped, pos=0.2, allow upside down]{\arrowOut} node[pos=.2, anchor=east]{$d$};
\draw[color=white, fill=white] (-1.4, 3) circle (.4);
\draw[color=white, fill=white] (-1.5,-2.8) circle (.4);
\draw[color=white, fill=white] (-.5,.2) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (0,4) --(-5,0)  node[midway, anchor=south east]{$F$};
\draw[line width=1pt, color=black, style=dashed] (0,1) --(-5,0) node[midway, anchor=south]{$\;\;G$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-1)  node[midway, anchor=north]{$\;\;K$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-4) node[midway, anchor=north east]{$H$};

\draw[color=white, fill=white] (-1.2,-.83) circle (.4);

\draw[line width=.5pt, color=black] (0,-4) .. controls (-1.5,-2.5)  and (-1.5,-.5).. (0,1) node[midway, anchor=west]{$c$};

\draw[color=violet, fill=violet] (0,4) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[color=cyan, fill=cyan] (0,1) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-5,0) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\end{align*}
\begin{align*}
\stackrel{\eqref{pic:snake},\eqref{eq:functortrpivot}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=violet] (-3,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-3,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=cyan] (0,4)--(0,1) node[midway, anchor=west]{$q$};
\draw[line width=1.5pt, color=red] (0,1)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,-4)--(0,-5);

\draw[line width=.5pt, color=gray] (0,4) .. controls (-.5,2)  and (-1.5,2).. (-1.5,4);
\draw[line width=.5pt, color=gray] (-1.5,4)--(-1.5,5) node[sloped, pos=0.2, allow upside down]{\arrowOut} node[pos=.2, anchor=west]{$d$};
\draw[line width=.5pt, color=gray] (0,-1) .. controls (-.5,.2)  and (-1.5,.2).. (-1.5,-1);
\draw[line width=.5pt, color=gray] (-1.5,-5)--(-1.5,-1) node[sloped, pos=0.2, allow upside down]{\arrowOut} node[pos=.2, anchor=west]{$d$};
\draw[color=white, fill=white] (-1.4, 3) circle (.4);
\draw[color=white, fill=white] (-1.5,-2.8) circle (.4);
\draw[color=white, fill=white] (-1.5,-.8) circle (.4);
\draw[color=white, fill=white] (-1.5,-1.8) circle (.2);

\draw[line width=1pt, color=black, style=dashed] (0,4) --(-5,0)  node[pos=.6, anchor=south east]{$F$};
\draw[line width=1pt, color=black, style=dashed] (0,1) --(-5,0) node[pos=.3, anchor=south]{$\;\;G$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-1)  node[midway, anchor=north]{$\;\;K$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-4) node[midway, anchor=north east]{$H$};

\draw[color=white, fill=white] (-2.2,-2.5) circle (.4);
\draw[color=white, fill=white] (-2,.8) circle (.4);
\draw[color=white, fill=white] (-2.5,2) circle (.4);

\draw[line width=.5pt, color=black] (0,-4) .. controls (-.5,-1)  and (-2.5,-1).. (-2.5,-4);
\draw[line width=.5pt, color=black] (0,1) .. controls (-.5,0)  and (-2.5,0).. (-2.5,1.5);
\draw[line width=.5pt, color=black] (-2.5,-5)--(-2.5,-4) node[sloped, pos=0.8, allow upside down]{\arrowOut} node[pos=.8, anchor=east]{$c$};
\draw[line width=.5pt, color=black] (-2.5,1.5)--(-2.5,5) node[sloped, pos=0.8, allow upside down]{\arrowOut} node[pos=.8, anchor=east]{$c$};

\draw[color=violet, fill=violet] (0,4) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[color=cyan, fill=cyan] (0,1) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-5,0) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\stackrel{\eqref{pic:snake},\eqref{eq:functortrpivot}}=
\begin{tikzpicture}[scale=.5, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=violet] (-1.5,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=violet] (-1.5,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=cyan] (0,4)--(0,1) node[midway, anchor=west]{$q$};
\draw[line width=1.5pt, color=red] (0,1)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,5)--(0,4);
\draw[line width=1.5pt, color=violet] (0,-4)--(0,-5);

\draw[line width=.5pt, color=gray] (0,4) .. controls (-2,2.5)  and (-2,.5).. (0,-1) node[pos=.4, anchor=east]{$d$};
\draw[color=white, fill=white] (-1.1,.83) circle (.4);

\draw[line width=1pt, color=black, style=dashed] (0,4) --(-5,0)  node[midway, anchor=south east]{$F$};
\draw[line width=1pt, color=black, style=dashed] (0,1) --(-5,0) node[midway, anchor=south]{$\;\;G$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-1)  node[midway, anchor=north]{$\;\;K$};
\draw[line width=1pt, color=black, style=dashed] (-5,0) --(0,-4) node[midway, anchor=north east]{$H$};

\draw[color=white, fill=white] (-1.2,-.83) circle (.4);
\draw[color=white, fill=white] (-.9,-3.2) circle (.4);
\draw[color=white, fill=white] (-1,1) circle (.4);
\draw[color=white, fill=white] (-1,3) circle (.4);

\draw[line width=.5pt, color=black] (0,-4) .. controls (-.25,-2)  and (-1,-2).. (-1,-4);
\draw[line width=.5pt, color=black] (0,1) .. controls (-.25,0)  and (-1,0).. (-1,1);
\draw[line width=.5pt, color=black] (-1,-5)--(-1,-4) node[sloped, pos=0.8, allow upside down]{\arrowOut} node[pos=.8, anchor=east]{$c$};
\draw[line width=.5pt, color=black] (-1,1)--(-1,5) node[sloped, pos=0.8, allow upside down]{\arrowOut} node[pos=.8, anchor=east]{$c$};

\draw[color=violet, fill=violet] (0,4) circle (.15) node[anchor=west]{$\;\alpha$};
\draw[color=cyan, fill=cyan] (0,1) circle (.15) node[anchor=west]{$\;\beta$};
\draw[color=blue, fill=blue] (0,-1) circle (.15) node[anchor=west]{$\;\gamma$};
\draw[color=violet, fill=violet] (0,-4) circle (.15) node[anchor=west]{$\;\delta$};
\draw[ fill=black] (-5,0) circle (.15) node[anchor=east]{$\nu\;$};
\end{tikzpicture}
\end{align*}
\end{proof}





The generalised 6j symbols are also invariant under a simultaneous orientation reversal  of the defect surface and all  defect lines on the surface, if the defect data is transformed accordingly.

\begin{lemma}\label{lem:mirror}
The 6j symbol of  a labeled generic transversal tetrahedron is invariant under 
\begin{compactitem} 
\item reversing the orientation of all defect areas and all defect lines, 
\item replacing each $(\mac,\mad)$-bimodule category $\mam$ by the $(\mad,\mac)$-bimodule category $\mam^\#$, 
\item replacing each bimodule functor $F:\mam\to\man$ by $F^\#:\mam^\#\to \man^\#$,
\item replacing each bimodule natural transformation $\nu: F\Rightarrow G$ by $\nu^\#: G^\#\Rightarrow F^\#$.
\end{compactitem}
\end{lemma}

\begin{proof} 
By Lemma \ref{lem:sphlemma}, one may additionally reverse the orientation of all edges labeled with objects in spherical fusion categories and replace those objects by their duals without changing the associated 6j symbol. 

Let $t$ be a generic transversal tetrahedron and $t'$ the tetrahedron obtained  from $t$ by reversing the orientations of all defect areas,  defect lines and edges of $t$ 
 and transforming their labels accordingly.  For each triangle of $t$ the corresponding triangle of $t'$ has  the same morphism space assigned to it  by \eqref{pic:homspace}, but interpreted as a morphism space in the opposite category. For instance, $\Hom_\mam(F(c\rhd m), n)$ is viewed as $\Hom_{\mam^\#}(n, F(m\lhd c^*))$  and $\Hom_{\mam}(m\lhd d, G(n))$ is viewed as $\Hom_{\mam^\#}(G(n), d^*\rhd m)$. 

Projecting  the data from the spherical fusion categories on the defect plane of $t'$ then  yields a mirror image of the polygon diagram for $t$, in which the orientation of all interior lines is reversed, each bimodule category $\mam$ is replaced by its opposite $\mam^\#$, each bimodule functor $F$ by $F^\#$, each bimodule natural transformation $\nu$ by $\nu^\#$
and each object in a spherical fusion category by its dual. As the left action of $c\in \Ob\mac$ or the right action of $d\in \Ob\mad$ on $\mam$ corresponds to the right action of $c^*$ and the left action of $d^*$ on $\mam^\#$, the evaluations of the polygon diagrams for $t'$ and $t$ are equal by Corollary \ref{rem:polyback}.\end{proof}
