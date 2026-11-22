---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-008-diagrams-for-2-categories
section_title: "Diagrams for 2-categories"
section_number: null
pages: 12-13
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
A {\bf 2-category diagram} for a 2-category $\mac$  is a direct generalisation of a diagram for a monoidal category. It is a PL stratification $\emptyset\subset X^0\subset X^1\subset X^2=[0,1]^2$ of  the unit square. Elements of $X^0$ are called {\bf vertices}, connected components of $X^1\setminus X^0$ {\bf lines} and connected components of $X^2\setminus X^1$ {\bf regions} of the diagram.  Lines may end at the top and bottom of the square only and all vertices are  in the interior. A diagram is called  {\bf progressive}, if its horizontal projection is regular, i.e.~its restriction to each line is a PL isomorphism onto the image. It is called {\bf generic}, if no two vertices are at the same height.  In pictures, we often omit the  unit square that borders  the diagram for better legibility.

 Regions in the diagram are labeled by objects of $\mac$, lines by 1-morphisms and vertices by 2-morphisms. Diagrams are read from top to bottom, and can be composed horizontally if the top of one diagram matches the bottom of the other. This corresponds to the vertical composition of 2-morphisms. Horizontal composition is from the right to the left. This is analogous to the usual calculus for monoidal categories, up to the fact that regions of the diagrams are labeled with objects, lines with 1-morphisms and vertices with 2-morphisms. 
 
A  diagram whose right-hand side is labeled by an object $\mathcal A$, whose left-hand side by an object $\mathcal B$ and with   lines at its upper and lower boundary labeled with 1-morphisms $F_1,...,F_n$  and  $G_1,...,G_m$,  from the right to the left, describes a 2-morphism $\nu: F_n\cdots F_1\Rightarrow G_m\cdots G_1$ between 1-morphisms $F_n\cdots F_1:\mathcal A\to\mathcal B$ and $G_m\cdots G_1:\mathcal A\to\mathcal B$.
This 2-morphism is obtained by first  horizontally composing the 2-morphisms at the vertices in the diagram with the 1-morphisms on the lines to the left and right and then composing the resulting 2-morphisms  in their vertical order. 

\begin{example}\label{ex:2catdiagram} The diagram 
\begin{align}\label{pic:diagram}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, color=black, style=dashed, ] (0,3)node[anchor=south]{$F$}--(0,-1); 
\draw[line width=1pt, color=black, style=dashed,] (0,-1)--(-2,-3) node[anchor=north]{$G$}; 
\draw[line width=1pt, color=black, style=dashed, ] (0,-1)--(2,-3) node[anchor=north]{$H$};
 \draw[line width=1pt, color=black, style=dashed, ] (4,3) node[anchor=south]{$K$} --(4,1.2) ;
 \draw[line width=1pt, color=black, style=dashed, ] (4,1)--(4,-3) node[anchor=north]{$L$}; 
 \draw[fill=black] (0,-1) circle (.2) node[anchor=east]{$\rho$};
  \draw[fill=black] (4,1) circle (.2) node[anchor=east]{$\sigma$};
  \node at (6,0)[anchor=west, color=blue]{$\mathcal M$};
    \node at (2.5,0)[anchor=east, color=violet]{$\mathcal P$};
      \node at (0,-2.5)[color=cyan ]{$\mathcal Q$};
        \node at (-2,0)[anchor=east, color=red]{$\mathcal N$};
\end{tikzpicture}
\end{align}
for the 2-category Cat with functors  $K,L:\mathcal M\to\mathcal P$, $F:\mathcal P\to\mathcal N$, $H:\mathcal P\to\mathcal Q$ and $G:\mathcal Q\to\mathcal N$ and natural transformations $\sigma: K\Rightarrow L$ and $\rho: F\Rightarrow GH$ describes the natural transformation $(\rho  L)\circ (F\sigma): FK\Rightarrow GHL$ with component morphisms
$\rho_{L(m)}  \circ  F(\sigma_m): FK(m)\to FL(m)\to GHL(m)$. 
\end{example}

It is shown in \cite[Th.~1.12]{JS} in the smooth context, see also \cite[Th.~2.12]{BMS} for the PL setting, that 2-category diagrams represent the same 2-morphisms if they are related by PL isotopies that start at the identity and define a one-parameter family of isomorphisms of diagrams. An isomorphism of diagrams is a PL homeomorphism  that is the identity on the boundary of the diagram  and such that the homeomorphism and its inverse preserve all skeleta of the diagram. 
This invariance is  a consequence of the identity
\begin{align}
\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-9,0)}]
\draw[line width=1pt, color=black, style=dashed] (0,3)node[anchor=south]{$F$}--(0,-3) node[anchor=north]{$G$};
\draw[line width=1pt, color=black, style=dashed] (3,3)node[anchor=south]{$H$}--(3,-3) node[anchor=north]{$K$};
\draw[fill=black] (0,1) circle (.2) node[anchor=east]{$\nu\;$};
\draw[fill=black] (3,-1) circle (.2) node[anchor=west]{$\;\mu$};
\node  at (6,0) [color=blue]{$\mathcal A$};
\node  at (1.5,0) [color=violet]{$\mathcal B$};
\node  at (-3,0) [color=red]{$\mathcal C$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(6,0)}]
\draw[line width=1pt, color=black, style=dashed] (0,3)node[anchor=south]{$F$}--(0,-3) node[anchor=north]{$G$};
\draw[line width=1pt, color=black, style=dashed] (3,3)node[anchor=south]{$H$}--(3,-3) node[anchor=north]{$K$};
\draw[fill=black] (0,-1) circle (.2) node[anchor=east]{$\nu\;$};
\draw[fill=black] (3,1) circle (.2) node[anchor=west]{$\;\mu$};
\node  at (6,0) [color=blue]{$\mathcal A$};
\node  at (1.5,0) [color=violet]{$\mathcal B$};
\node  at (-3,0) [color=red]{$\mathcal C$};
\end{scope}
\node at (0,-6) {$(G\mu)\circ (\nu H)=(\nu K)\circ(F\mu)$.};
\end{tikzpicture}
\end{align}
for all 1-morphisms $F,G:\mathcal B\to\mathcal C$ and $H,K:\mathcal A\to\mathcal B$ and 2-morphisms  $\nu: F\Rightarrow G$ and $\mu: H\Rightarrow K$.
It allows one to  associate 2-morphisms to non-generic diagrams by perturbing them to generic ones. 
In the 2-category Cat this identity expresses the naturality of natural transformations.
