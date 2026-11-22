---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-009-diagrams-for-pivotal-2-categories
section_title: "Diagrams for pivotal 2-categories"
section_number: null
pages: 13-14
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 1.0
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
If the 2-category under consideration 
 is a pivotal 2-category in the sense \cite[Def.~A.12]{G14} or, more strictly, a planar 2-category in the sense of \cite[Def.~3.2.1]{BMS}, we use the diagrams for planar 2-categories introduced in \cite[Def.~3.5]{BMS}. The main examples are  $\mathrm{Mod}^\theta(\mac)$ and $\Bimod^\theta(\mac,\mad)$ from Theorem \ref{th:pivot}. 
 
 The  diagrams for pivotal 2-categories are essentially the diagrams  for a pivotal monoidal category.
The only difference is that regions of the diagram are labeled with objects, lines with 1-morphisms and vertices with 2-morphisms. 
As for a pivotal category, the pivotal structure implies that left duals are also right duals and that double duals of a 1-morphism $F$ are 2-isomorphic to $F$.
We thus denote the duals of a 1-morphism $F$ by a dashed line  labeled $F$ with an arrow that points upwards. Lines without arrows are assumed to be oriented downwards.
The (co)evaluations of the duals, which  generalise \eqref{eq:coevl} and \eqref{eq:coevr}, are then given by the diagrams
\begin{align}\label{pic:unitcounit}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (0,0)  .. controls (0,3) and (-3,3) .. (-3,0) node[sloped, pos=0.15, allow upside down]{\arrowIn} node[anchor=north]{$F$};
\node  at (-1.5,0) [color=blue, anchor=south]{$\mathcal A$};
\node  at (1,0) [color=red, anchor=south]{$\mathcal B$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (0,3)  .. controls (0,0) and (-3,0) .. (-3,3) (0,3)node[anchor=south]{$F$} node[sloped, pos=0.9, allow upside down]{\arrowIn} ;
\node  at (1,3) [color=blue, anchor=north]{$\mathcal A$};
\node  at (-1.5,3) [color=red, anchor=north]{$\mathcal B$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (0,0) .. controls (0,3) and (3,3) .. (3,0) node[anchor=north]{$F$} node[sloped, pos=0.15, allow upside down]{\arrowIn};
\node  at (4,0) [color=blue, anchor=south]{$\mathcal A$};
\node  at (1.5,0) [color=red, anchor=south]{$\mathcal B$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (0,3)node[anchor=south]{$F$}   .. controls (0,0) and (3,0) .. (3,3) node[sloped, pos=0.9, allow upside down]{\arrowIn} ;
\node  at (1.5,3) [color=blue, anchor=north]{$\mathcal A$};
\node  at (4,3) [color=red, anchor=north]{$\mathcal B$};
\end{tikzpicture}
\\
&\eta^F: \id_{\mathcal B}\Rightarrow FF^l &
&\epsilon^F: F^lF\Rightarrow \id_{\mathcal A}
&
&\eta'^F:  \id_{\mathcal A} \Rightarrow F^lF &
&\epsilon'^F:FF^l\Rightarrow \id_{\mathcal B}\nonumber 
\end{align}
that generalise \eqref{pic:unitcounitsphere}. The defining conditions on the left (co)evaluations, which  generalise \eqref{eq:snake}, read
\begin{align}\label{pic:adjunction}
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-8,0)}]
\draw[line width=1pt, style=dashed,] (0,0)  .. controls (0,3) and (3,3) .. (3,0);
\draw[line width=1pt, style=dashed,-stealth] (6,0) .. controls (6,-3) and (3,-3) .. (3,0) ;
\draw[line width=1pt, style=dashed] (0,0)--(0,-3)  node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1pt, style=dashed] (6,3) node[anchor=south]{$F$}--(6,0) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\node  at (.5,-2) [color=blue, anchor=west]{$\mathcal A$};
\node  at (-.5,-2) [color=red, anchor=east]{$\mathcal B$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(2,0)}]
\draw[line width=1pt, style=dashed] (0,3) node[anchor=south]{$F$}--(0,-3) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\node  at (.5,-2) [color=blue, anchor=west]{$\mathcal A$};
\node  at (-.5,-2) [color=red, anchor=east]{$\mathcal B$};
\end{scope}
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-5,0)}]
\draw[line width=1pt, style=dashed, stealth-] (0,0)  .. controls (0,3) and (3,3) .. (3,0) ;
\draw[line width=1pt, style=dashed] (-3,0) .. controls (-3,-3) and (0,-3) .. (0,0) ;
\draw[line width=1pt, style=dashed] (-3,0)--(-3,3) node[anchor=south]{$F$} node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1pt, style=dashed] (3,-3)--(3,0) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\node  at (-3.5,2) [color=blue, anchor=east]{$\mathcal A$};
\node  at (-2.5,2) [color=red, anchor=west]{$\mathcal B$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(2,0)}]
\draw[line width=1pt, style=dashed] (0,-3)--(0,3) node[anchor=south]{$F$}  node[sloped, pos=0.5, allow upside down]{\arrowIn};
\node  at (-.5,-2) [color=blue, anchor=east]{$\mathcal A$};
\node  at (.5,-2) [color=red, anchor=west]{$\mathcal B$};
\end{scope}
\end{tikzpicture}
\end{align}
 and the pivotality condition that generalises \eqref{pic:pivotalfus} is expressed in the diagrammatic identity
\begin{align}\label{pic:pivotal}
\begin{tikzpicture}[scale=.25]
\begin{scope}[shift={(-8,0)}]
\draw[line width=1pt, dashed] (0,0) .. controls (0,2) and (-2,2).. (-2,0);
\draw[line width=1pt, dashed, -stealth] (0,0) .. controls (0,-2) and (2,-2).. (2,0);
\draw[line width=1pt, dashed,stealth-] (-2,0) .. controls (-2,-6) and (4,-6).. (4,0);
\draw[line width=1pt, dashed,-stealth] (2,0) .. controls (2,6) and (-4,6).. (-4,0);
\draw[line width=1pt, dashed,-stealth] (4,4)node[anchor=south]{$F$}--(4,0);
\draw[line width=1pt, dashed] (-4,0)--(-4,-4) node[anchor=north]{$G$};
\draw[fill=black] (0,0) circle(.25) node[anchor=west]{$\,\nu$};
\node at (5,3)[anchor=west, color=blue]{$\mathcal A$};
\node at (-5,-3)[anchor=east, color=red]{$\mathcal B$};
\end{scope}
\node(0,0){$=$};
\draw[line width=1pt, dashed] (4,4) node[anchor=south]{$F$}--(4,-4) node[anchor=north]{$G$};
\draw[fill=black] (4,0) circle(.25) node[anchor=west]{$\,\nu$};
\node at (3,3)[anchor=east, color=red]{$\mathcal B$};
\node at (5,3)[anchor=west, color=blue]{$\mathcal A$};
\end{tikzpicture}
\end{align}

In the diagrammatic calculus the pivotal structure allows one to drop the requirement that the diagrams are {\em progressive}, i.e.~that the horizontal projection of the diagram is regular. 
Instead, singular points of the projection are labeled with (co)evaluations.  Although we draw them as smooth maxima and minima for diagrammatic convenience, they represent   vertices in a PL diagram. While a diagram with maxima and minima is never progressive itself, it stands for the progressive diagram obtained by replacing maxima and minima with vertices labeled by (co)evaluations, see \cite[Sec.~3.2]{BMS}. 


This enlarges the class of diagrams that represent the same 2-morphism. 
It is shown in  \cite[Th.~3.9]{BMS} that  planar 2-category diagrams related by orientation preserving PL homeomorphisms that preserve the unit square  represent the same 2-morphism if their labels are transformed accordingly. This means that the objects labeling the regions and the 1-morphisms labeling lines of the diagrams must coincide, while the 2-morphisms at the vertices are composed with the (co)evaluations of the 1-morphisms at the incident lines. 

 Composing a
2-morphism $\nu: F_{n}\cdots F_1\Rightarrow G_m\cdots G_1$ with the (co)evaluations for $F_n$ and $G_1$ from \eqref{pic:unitcounit} transforms it  into  2-morphisms $\nu': F_{n-1}\cdots F_1 \Rightarrow F_{n}^l G_m\cdots G_1$ 
 and $\nu'': F_{n}\cdots F_1 G^l_1\Rightarrow G_m\cdots G_2$.
\begin{align}
&\begin{tikzpicture}[scale=.25]
\begin{scope}[shift={(-9,0)}]
\draw[line width=1pt, dashed] (0,0)--(-5,5) node[anchor=south]{$F_n$};
\draw[line width=1pt, dashed] (0,0)--(-1,5) node[anchor=south]{$F_{n-1}$};
\node at (1,4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(5,5) node[anchor=south]{$F_1$};

\draw[line width=1pt, dashed] (0,0)--(-5,-5) node[anchor=north]{$G_m$};
\node at (-1,-4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(1,-5) node[anchor=north]{$G_{2}$};
\draw[line width=1pt, dashed] (0,0)--(5,-5) node[anchor=north]{$G_1$};
\draw[fill=black] (0,0) circle (.25) node[anchor=east]{$\nu\;$};
\node at (3,0) [color=blue, anchor= west]{$\mathcal A$};
\node at (-3.5,4.5) [color=violet, anchor= west]{$\mathcal B$};
\node at (-3,0) [color=red, anchor=east]{$\mathcal C$};
\node at (3.5,-4.5) [color=cyan, anchor=east]{$\mathcal D$};
\end{scope}
\begin{scope}[shift={(11,0)}]
\draw[line width=1pt, dashed] (0,0) .. controls (-1,3) and (-2,2) .. (-4,0);
\draw[line width=1pt, dashed] (-9,-5) node[anchor=north]{$F_n$}--(-4,0) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1pt, dashed] (0,0)--(-1,5) node[anchor=south]{$F_{n-1}$};
\node at (1,4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(5,5) node[anchor=south]{$F_1$};

\draw[line width=1pt, dashed] (0,0)--(-5,-5) node[anchor=north]{$G_m$};
\node at (-1,-4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(1,-5) node[anchor=north]{$G_{2}$};
\draw[line width=1pt, dashed] (0,0)--(5,-5) node[anchor=north]{$G_1$};
\draw[fill=black] (0,0) circle (.25) node[anchor=east]{$\nu\;$};
\node at (3,0) [color=blue, anchor= west]{$\mathcal A$};
\node at (-7,0) [color=violet, anchor= west]{$\mathcal B$};
\node at (-6.5,-5) [color=red, anchor=south]{$\;\;\mathcal C$};
\node at (3.5,-4.5) [color=cyan, anchor=east]{$\mathcal D$};
\end{scope}
\draw[line width=1pt, -stealth] (-1,0)--(1,0);
\end{tikzpicture}\nonumber\\
\intertext{}
&\begin{tikzpicture}[scale=.25]
\begin{scope}[shift={(-9,0)}]
\draw[line width=1pt, dashed] (0,0)--(-5,5) node[anchor=south]{$F_n$};
\draw[line width=1pt, dashed] (0,0)--(-1,5) node[anchor=south]{$F_{n-1}$};
\node at (1,4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(5,5) node[anchor=south]{$F_1$};

\draw[line width=1pt, dashed] (0,0)--(-5,-5) node[anchor=north]{$G_m$};
\node at (-1,-4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(1,-5) node[anchor=north]{$G_{2}$};
\draw[line width=1pt, dashed] (0,0)--(5,-5) node[anchor=north]{$G_1$};
\draw[fill=black] (0,0) circle (.25) node[anchor=east]{$\nu\;$};
\node at (3,0) [color=blue, anchor= west]{$\mathcal A$};
\node at (-3.5,4.5) [color=violet, anchor= west]{$\mathcal B$};
\node at (-3,0) [color=red, anchor=east]{$\mathcal C$};
\node at (3.5,-4.5) [color=cyan, anchor=east]{$\mathcal D$};
\end{scope}
\draw[line width=1pt, -stealth] (-1,0)--(1,0);
\begin{scope}[shift={(11,0)}]
\draw[line width=1pt, dashed] (0,0)--(-5,5) node[anchor=south]{$F_n$};
\draw[line width=1pt, dashed] (0,0)--(-1,5) node[anchor=south]{$F_{n-1}$};
\node at (1,4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(5,5) node[anchor=south]{$F_1$};

\draw[line width=1pt, dashed] (0,0)--(-5,-5) node[anchor=north]{$G_m$};
\node at (-1,-4){$\ldots$};
\draw[line width=1pt, dashed] (0,0)--(1,-5) node[anchor=north]{$G_{2}$};
\draw[line width=1pt, dashed] (0,0) .. controls (1,-3) and (2,-2) .. (4,0);
\draw[line width=1pt, dashed] (4,0)--(9,5) node[anchor=south]{$G_1$}  node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[fill=black] (0,0) circle (.25) node[anchor=east]{$\nu\;$};
\node at (6,5) [color=blue, anchor= north]{$\mathcal A\;\;$};
\node at (-3.5,4.5) [color=violet, anchor= west]{$\mathcal B$};
\node at (-3,0) [color=red, anchor=east]{$\mathcal C$};
\node at (6,0) [color=cyan, anchor=west]{$\mathcal D$};
\end{scope}
\end{tikzpicture}
\label{fig:updown}
\end{align}

The pivotal 2-category structure ensures that  
 all diagrams that are related by the two moves  in \eqref{fig:updown}  and have the same edge labels  represent the same 2-morphism. 





\begin{definition}\label{def:cyclictrans} Let $\mac$ be a 2-category. 
 A {\bf cyclic transformation} of a 2-morphism $\nu: F_{n}\cdots F_1\Rightarrow G_m\cdots G_1$ is a 2-morphism obtained by applying a finite sequence of the moves in \eqref{fig:updown}. 
Two  2-morphisms $\nu$ and $\nu'$ are called {\bf cyclically equivalent} if they are related by a cyclic transformation. 
\end{definition}

In pictures, we sometimes suppress the change in the labeling and the units and counits of the adjunctions and use the label $\nu$ for a cyclic equivalence class of 2-morphisms.
