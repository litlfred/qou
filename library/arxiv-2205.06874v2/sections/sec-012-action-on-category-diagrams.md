---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-012-action-on-category-diagrams
section_title: "Action on category diagrams"
section_number: null
pages: 17-18
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.991
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
We also use the diagrammatic calculus to describe   evaluation functors $\mathrm{ev}: \Fun(\mam,\man)\times \mam\to \man$ that send a pair $(F,m)$ of a functor $F:\mam\to\man$ and an object $m\in\Ob\mam$ to the object $F(m)$ and a pair $(\nu,\alpha)$ of a natural transformation $\nu: F\Rightarrow G$ and a morphism $\alpha:m\to m'$ to the morphism
$\nu_{m'}\circ F(\alpha)=G(\alpha)\circ \nu_m: F(m)\to G(m')$. 

For this, we describe objects  in $\mam$ by a thick  vertical line and morphisms between them by  vertices on this line. 
Composition of morphisms is from the top to the bottom, and identity morphisms are omitted from the diagrams. Thus, a line whose top end is labeled by an object $m$ in $\mam$ and whose bottom end by an object $m'$ in $\mam$ describes a morphism $\alpha:m\to m'$ in $\mam$. 

The diagram for the evaluation $\mathrm{ev}(\nu,\alpha): F(m)\to G(m')$ of a natural transformation $\nu: F\Rightarrow G$ in $\Fun(\mam,\man)$ on 
a  morphism $\alpha:m\to m'$ in $\mam$  is obtained by placing the  diagram for $\alpha$  
to the right of  a 2-category diagram  for  $\nu$, such that no vertex of the diagram for $\nu$ is on the same height as a vertex on the line for $\alpha$.
 
The morphism $\mathrm{ev}(\nu,\alpha)$  is obtained by horizontally projecting the diagram for $\nu$ on the line for $\alpha$.  All functors labeling dashed lines to the left of a line segment or vertex on the latter  are applied to the associated objects and morphisms in $\mam$.  Natural transformations labeling the vertices  in the diagram for $\nu$ are composed with all functors labeling lines to their left and right  and then evaluated  on the object of $\mam$ to their right. The resulting morphisms in $\man$ are then composed in order of their height.

\begin{example} The diagram 
\begin{align}\label{pic:evaluation}
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
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

\draw[line width=1.5pt, color=blue] (8,3)node[anchor=south]{$m$}--(8,-3) node[anchor=north]{$m''$} node[midway, anchor=west]{$m'$};
\draw[color=blue, fill=blue] (8,2) circle (.2) node[anchor=west]{$\phi$};
\draw[color=blue, fill=blue] (8,-2) circle (.2) node[anchor=west]{$\psi$};        
\end{tikzpicture}
\end{align}
describes the evaluation $\mathrm{ev}(\nu, \alpha): FK(m)\to GHL(m'')$ of  $\nu=(\rho L)\circ (F\sigma): FK\Rightarrow GHL$ from diagram \eqref{pic:diagram} on the morphism $\alpha=\psi\circ\phi: m\to m'\to m''$ in $\mam$. 
It is  the  composite 
\begin{align*}
&\mathrm{ev}(\nu,\alpha): FK(m)\xrightarrow{FK(\phi)}FK(m')\xrightarrow{F(\sigma_{m'})} FL(m')\xrightarrow{\rho_{L(m')}} GHL(m')\xrightarrow{GHL(\psi)} GHL(m'').
\end{align*}
\end{example}

Note that the evaluation depends only on the natural transformation represented by the diagram on the left  and on the morphism represented by the line on the right, but not on the relative position of vertices in the two diagrams. This follows from  naturality and corresponds to the  identity
\begin{align}\label{pic:naturality}
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-7,0)}]
\draw[line width=1pt, color=black, style=dashed] (0,3)node[anchor=south]{$K$}--(0,-3) node[anchor=north]{$L$};
\draw[line width=1.5pt, color=blue] (3,3)node[anchor=south]{$m$}--(3,-3) node[anchor=north]{$m'$};
\draw[fill=black] (0,1) circle (.2) node[anchor=east]{$\sigma\;$};
\draw[fill=blue, color=blue] (3,-1) circle (.2) node[anchor=west]{$\;\phi$};
\node  at (1.5,0) [color=blue]{$\mathcal M$};
\node  at (-3,0) [color=violet]{$\mathcal P$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(6,0)}]
\draw[line width=1pt, color=black, style=dashed] (0,3)node[anchor=south]{$K$}--(0,-3) node[anchor=north]{$L$};
\draw[line width=1.5pt, color=blue] (3,3)node[anchor=south]{$m$}--(3,-3) node[anchor=north]{$m'$};
\draw[fill=black] (0,-1) circle (.2) node[anchor=east]{$\sigma\;$};
\draw[fill=blue, color=blue] (3,1) circle (.2) node[anchor=west]{$\;\phi$};
\node  at (1.5,0) [color=blue]{$\mathcal M$};
\node  at (-3,0) [color=violet]{$\mathcal P$};
\end{scope}
\node at (0,-7){$L(\phi)\circ \sigma_m=\sigma_{m'}\circ K(\phi)$};
\end{tikzpicture}
\end{align}
which allows one to move vertices in the diagram for  $\Fun(\mam,\man)$ above or below vertices on the line for $\mam$. One can thus drop the requirement that  the  former are at different heights from the latter. Any diagram that violates this condition can be deformed into one that satisfies it by slightly  displacing the vertices on the line on the right. As all ways of doing so yield the same morphism, its evaluation is defined by these deformations.

We also use diagrammatic calculus to describe the composites of morphisms of the form $\mathrm{ev}(\nu,\alpha)$  with general morphisms in $\man$. The resulting diagrams consist of a multicoloured thick line on the right and a diagram for $\Fun(\mam,\man)$ to the left whose lines may end either at the top or bottom of the diagram for $\Fun(\mam,\man)$ or on vertices on the thick line on the right. For instance, the following diagrams describe morphisms $\tau: J(m)\to n$ and $\omega: n\to J(m)$ in $\man$ for a functor $J:\mam\to\man$
\begin{align}\label{pic:mixedmorphism}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (-4,4)node[anchor=south]{$J$}--(0,0);
\draw[line width=1.5pt, color=blue] (0,4) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,0)--(0,-4) node[anchor=north]{$n$};
\draw[color=red, fill=red] (0,0) circle (.2) node[anchor=west]{$\;\tau$};
\node at (-1.5,3.5) [color=blue]{$\mathcal M$};
\node at (-3,1) [color=red]{$\mathcal N$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, style=dashed] (-4,-4)node[anchor=north]{$J$}--(0,0);
\draw[line width=1.5pt, color=blue] (0,-4) node[anchor=north]{$m$}--(0,0);
\draw[line width=1.5pt, color=red] (0,0)--(0,4) node[anchor=south]{$n$};
\draw[color=red, fill=red] (0,0) circle (.2) node[anchor=west]{$\;\omega$};
\node at (-1.5,-3.5) [color=blue]{$\mathcal M$};
\node at (-3,-1) [color=red]{$\mathcal N$};
\end{tikzpicture}
\end{align}
In this diagram, the dashed line may also stand for a composite  functor and  may be replaced by several dashed lines that  end in a common vertex of the line on the right. 
For $\mac$-module or $\mad$-right module categories $\mam$ and $\man$, any dashed line  may be replaced by a thin black or grey line labeled with an object of $\mac$ or $\mad$ that stands for an endofunctor $c\rhd -$ or $-\lhd d$.
