---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-006-diagrams-for-spherical-fusion-categories
section_title: "Diagrams for spherical fusion categories"
section_number: null
pages: 11-12
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.98
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
We use the usual graphical calculus for monoidal categories, suppressing the tensor unit and  coherence data. Morphisms in diagrams are composed from top to bottom and tensor products  from the right to the left.  

We also use the usual diagrammatic notation for the duals. If the categories are pivotal, we draw oriented lines for the objects, where a line that is directed downwards and labeled $x^*$ is replaced by a line that is directed upwards and labeled $x$. Lines without arrows are assumed to be  oriented downwards. The diagrams for the (co)evaluations from \eqref{eq:coevl} and \eqref{eq:coevr} are
 \begin{align}\label{pic:unitcounitsphere}
&\begin{tikzpicture}[scale=.3]
\draw[line width=.5pt, ] (0,0)  .. controls (0,3) and (-3,3) .. (-3,0) node[sloped, pos=0.15, allow upside down]{\arrowIn} node[anchor=north]{$x$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=.5pt,] (0,3)  .. controls (0,0) and (-3,0) .. (-3,3) (0,3)node[anchor=south]{$x$} node[sloped, pos=0.9, allow upside down]{\arrowIn} ;
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=.5pt,] (0,0) .. controls (0,3) and (3,3) .. (3,0) node[anchor=north]{$x$} node[sloped, pos=0.15, allow upside down]{\arrowIn};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=.5pt, ] (0,3)node[anchor=south]{$x$}   .. controls (0,0) and (3,0) .. (3,3) node[sloped, pos=0.9, allow upside down]{\arrowIn} ;
\end{tikzpicture}\\
&\coev^L_x: e\to x\oo x^* & &\ev^L_x: x^*\oo x\to e & &\coev^R_x: e\to x^*\oo x & &\ev^R_x: x\oo x^*\to e, \nonumber
\end{align}
and the defining conditions \eqref{eq:snake} on the left duals read 
\begin{align}\label{pic:snake}
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-8,0)}]
\draw[line width=.5pt,stealth-] (0,0)  .. controls (0,3) and (3,3) .. (3,0) ;
\draw[line width=.5pt,stealth-] (3,0) .. controls (3,-3) and (6,-3) .. (6,0) ;
\draw[line width=.5pt] (0,0)--(0,-3);
\draw[line width=.5pt,stealth-] (6,0)--(6,3) node[anchor=south]{$x$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(2,0)}]
\draw[line width=.5pt,stealth-] (0,0)--(0,3) node[anchor=south]{$x$};
\draw[line width=.5pt] (0,-3)--(0,0);
\end{scope}
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-5,0)}]
\draw[line width=.5pt,stealth-] (0,0)  .. controls (0,3) and (3,3) .. (3,0) ;
\draw[line width=.5pt,stealth-] (-3,0) .. controls (-3,-3) and (0,-3) .. (0,0) ;
\draw[line width=.5pt] (-3,0)--(-3,3) node[anchor=south]{$x$};
\draw[line width=.5pt,stealth-] (3,0)--(3,-3) ;
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(2,0)}]
\draw[line width=.5pt,-stealth] (0,-3)--(0,0);
\draw[line width=.5pt] (0,0)--(0,3) node[anchor=south]{$x$};
\end{scope}
\end{tikzpicture}
\end{align}
Pivotality  is expressed in the diagram
\begin{align}\label{pic:pivotalfus}
\begin{tikzpicture}[scale=.25]
\begin{scope}[shift={(-8,0)}]
\draw[line width=.5pt] (0,0) .. controls (0,2) and (-2,2).. (-2,0);
\draw[line width=.5pt, -stealth] (0,0) .. controls (0,-2) and (2,-2).. (2,0);
\draw[line width=.5pt,stealth-] (-2,0) .. controls (-2,-6) and (4,-6).. (4,0);
\draw[line width=.5pt,-stealth] (2,0) .. controls (2,6) and (-4,6).. (-4,0);
\draw[line width=.5pt,-stealth] (4,4)node[anchor=south]{$x$}--(4,0);
\draw[line width=.5pt] (-4,0)--(-4,-4) node[anchor=north]{$y$};
\draw[fill=black] (0,0) circle(.25) node[anchor=west]{$\,\nu$};
\end{scope}
\node(0,0){$=$};
\draw[line width=.5pt] (4,4) node[anchor=south]{$x$}--(4,-4) node[anchor=north]{$y$};
\draw[fill=black] (4,0) circle(.25) node[anchor=west]{$\,\nu$};
\end{tikzpicture}
\end{align}
for all morphisms $\nu:x\to y$, and  a pivotal category is spherical iff for all $\alpha: x\to x$
\begin{align}\label{eq:tracesph}
\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-5,0)}]
\draw[line width=.5pt, ->,>=stealth] (-2,2) node[anchor=east]{$x$}--(-2,-2) node[anchor=east]{$x$};
\draw[line width=.5pt, <-,>=stealth] (2,2) --(2,-2) node[midway,anchor=west]{$x$};
\draw[fill=black] (-2,0)  circle (.2) node[anchor=east]{$\alpha$};
\draw[line width=.5pt, ->,>=stealth] (-2,-2) .. controls (-2,-4) and (2,-4)..(2,-2);
\draw[line width=.5pt, ->,>=stealth] (2,2) .. controls (2,4) and (-2,4)..(-2,2);
\node at (0,-4)[anchor=north]{$\tr^R(\alpha)$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(5,0)}]
\draw[line width=.5pt, <-,>=stealth] (-2,2)--(-2,-2) node[midway,anchor=east]{$x$}  ;
\draw[line width=.5pt, ->,>=stealth] (2,2)  node[anchor=west]{$x$} --(2,-2) node[anchor=west]{$x$} ;
\draw[fill=black] (2,0) node[anchor=west]{$\alpha$}  circle (.2);
\draw[line width=.5pt, <-,>=stealth] (-2,-2) .. controls (-2,-4) and (2,-4)..(2,-2);
\draw[line width=.5pt, <-,>=stealth] (2,2) .. controls (2,4) and (-2,4)..(-2,2);
\node at (0,-4)[anchor=north]{$\tr^L(\alpha)$};
\end{scope}
\end{tikzpicture}
\end{align}
