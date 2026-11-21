---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-017-gluing-identities-for-polygon-diagrams
section_title: "Gluing identities for polygon diagrams"
section_number: null
pages: 26-28
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.955
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
We consider the pivotal 2-category $\Bimod^\theta(\mac,\mad)$ for spherical fusion categories $\mac,\mad$.
We fix sets  $I_\mac$, $I_\mad$  and $I_\mam$ of representatives of the isomorphism classes of simple objects in $\mac$, $\mad$ and in each bimodule category  
$\mam$.  For each object $x$ in $\mac$, $\mad$ or $\mam$ and each simple object $i$ in the set of representatives, we choose projection morphisms $p^\alpha_{xi}: x\to i$ and inclusion morphisms $j^\alpha_{xi}:i\to x$ that satisfy  \eqref{eq:projincl}. 

Then we can glue and cut  polygon diagrams by summing  over the simple objects at their boundary segments and over bases of the morphism spaces at their boundary vertices.

\begin{theorem} \label{th:polyids}
The cyclic evaluations of the polygon diagrams for $\Bimod^\theta(\mac,\mad)$ satisfy:

\medskip
\begin{compactenum}
\item {\bf Gluing sides:} for all objects $m\in I_\mam$, $n\in I_\man$
\begin{align}\label{pic:gluepoly}
&\begin{tikzpicture}[scale=.3]
\node at (-22,0) {$\sum_{\alpha}$};
\begin{scope}[shift={(-15,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[line width=1.5pt, color=blue] (0:4.35)--(30:5) node[anchor=south]{$\;m$};
\draw[line width=1.5pt, color=blue] (30:5)--(60:4.35);
\draw[line width=1.5pt, color=red] (-30:5)--(-60:4.35);
\draw[line width=1.5pt, color=red] (0:4.35)--(-30:5) node[anchor=north]{$\;n$};
\draw[line width=1pt, dashed] (1,0) node[anchor=east]{$F$}--(0:4.35) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[color=red, fill=red] (0:4.35) circle (.2) node[anchor=west]{$\alpha$};
\node at (3,.5)[anchor=south, color=blue]{$\mam$};
\node at (3,-.5)[anchor=north, color=red]{$\man$};
\draw[draw=none, fill=gray, fill opacity=.2] (8,-2.5)--(8,2.5)--(13,2.5)--(13,-2.5)--(8,-2.5);
\draw[color=blue, line width=1.5pt] (8,0)--(8,2.5) node[anchor=south]{$m$}--(10.5,2.5);
\draw[color=red, line width=1.5pt] (8,0)--(8,-2.5) node[anchor=north]{$n$}--(10.5,-2.5);
\draw[line width=1pt, dashed] (8,0) --(10.5,0) node[anchor=west]{$F$} node[sloped, pos=0.7, allow upside down]{\arrowIn};
\draw[color=red, fill=red] (8,0) circle (.2) node[anchor=east]{$\alpha$};
\node at (9.5,.5)[anchor=south, color=blue]{$\mam$};
\node at (9.5,-.5)[anchor=north, color=red]{$\man$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(7,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[draw=none, fill=gray, fill opacity=.2] (4.33,-2.5)--(4.33,2.5)--(9.35,2.5)--(9.35,-2.5)--(9.35,-2.5);
\draw[line width=1.5pt, color=blue] (30:5) node[anchor=south]{$\;m$} --(60:4.35);
\draw[line width=1.5pt, color=blue] (4.34,2.5)--(6.84,2.5);
\draw[line width=1.5pt, color=red] (-30:5) node[anchor=north]{$\;n$} --(-60:4.35);
\draw[line width=1.5pt, color=red] (4.34,-2.5)--(6.84,-2.5);
\draw[line width=1pt, dashed] (1,0) node[anchor=east]{$F$}--(6,0) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\node at (3.5,.5)[anchor=south, color=blue]{$\mam$};
\node at (3.5,-.5)[anchor=north, color=red]{$\man$};
\end{scope}
\end{tikzpicture}
\end{align}

\bigskip
\item {\bf Gluing around a vertex:} for all objects $m\in I_\mam$
\begin{align}
\label{pic:closepoly}
&\begin{tikzpicture}[scale=.3]
\node at (-17,0) {$\sum_{n,\alpha} \dim(n)$};
\begin{scope}[shift={(-7,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (0,0)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5)--(0,0);
\draw[line width=1.5pt, color=red] (30:2.5)--(0,0) node[anchor=west]{$\;n$}--(-30:2.5);
\draw[line width=1.5pt, color=blue] (30:2.5)--(30:5) node[anchor=west]{$m$}--(60:4.35);
\draw[line width=1.5pt, color=blue] (-30:2.5)--(-30:5)node[anchor=west]{$m$} --(-60:4.35);
\draw[line width=1pt, dashed] (0,2.5) node[anchor=east]{$F$}--(30:2.5) node[sloped, pos=0.5, allow upside down]{\arrowIn};
\draw[line width=1pt, dashed] (-30:2.5)--(0,-2.5) node[anchor=east]{$F$} node[sloped, pos=0.5, allow upside down]{\arrowIn};

\draw[fill=blue, color=red] (30:2.5) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[fill=blue, color=red] (-30:2.5) circle (.2) node[anchor=west]{$\;\alpha$};
\node at (2,1.8)[anchor=south, color=blue]{$\mam$};
\node at (2,-1.8)[anchor=north, color=blue]{$\mam$};
\node at (-.5,0)[anchor=east, color=red]{$\man$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(7,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (0:5)--(72:5)--(144:5)--(216:5)--(288:5)--(0:5);
\draw[line width=1.5pt, color=blue] (-36:4)--(0:5) node[anchor=west]{$m$}--(36:4);
\draw[line width=1pt, dashed] (50:2)  .. controls (0:2)..(-50:2) node[anchor=north east]{$F$} node[sloped, pos=1, allow upside down]{\arrowIn};
\node at (2,0)[anchor=west, color=blue]{$\mam$};
\node at (1,0)[anchor=east, color=red]{$\man$};
\end{scope}
\end{tikzpicture}
\end{align}

\bigskip
\item {\bf Gluing a 2-gon:} for all objects $m,n\in I_\mam$, $x\in \Ob\mac$ or $x\in \Ob\mad$ and all morphisms $\phi: x\to x$ 
\begin{align}\label{pic:2gon} 
\begin{tikzpicture}[scale=.2]
\node at (-14,0) {$\sum_{m,n,\alpha}\dim(m)\dim(n)$};
\draw [blue,line width=1.5pt,domain=0:90] plot ({0.1*\x}, {5*sin(\x)});
\draw [blue,line width=1.5pt,domain=0:90] plot ({0.1*\x}, {-5*sin(\x)});
\draw [blue,line width=1.5pt,domain=0:90] plot ({0.1*\x+9}, {5*sin(\x+90)});
\draw [blue,line width=1.5pt,domain=0:90] plot ({0.1*\x+9}, {-5*sin(\x+90)});
\draw[line width=.5pt, color=black] (9,5)--(9,0) node[midway, anchor=west]{$x$} node[sloped, pos=.5, allow upside down]{\arrowOut} ;
\draw[line width=.5pt, color=black] (9,0)--(9,-5) node[midway, anchor=west]{$x$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[fill=blue, color=blue] (9,5) circle (.3) node[anchor=south]{$\alpha$};
\draw[fill=blue, color=blue] (9,-5) circle (.3) node[anchor=north]{$\alpha$};
\draw[fill=black] (9,0) circle (.3) node[anchor=west]{$\phi$};
\node at (3,0)[anchor=west, color=blue]{$\mam$};
\node at (0,0)[anchor=east, color=blue]{$m$};
\node at (18,0)[anchor=west, color=blue]{$n$};
\node at (22,0)[anchor=west]{$=\dim(\mam)$};
\draw[line width=.5pt] (37,3)--(37,-3) node[sloped, pos=.1, allow upside down]{\arrowOut} node[sloped, pos=1, allow upside down]{\arrowOut};
\draw[line width=.5pt] (33,-3)--(33,3) node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (33,3).. controls (33,5) and (37,5).. (37,3);
\draw[line width=.5pt] (33,-3).. controls (33,-5) and (37,-5).. (37,-3);
\draw[fill=black] (37,0) circle (.3) node[anchor=west]{$\phi$};
\node at (37,3)[anchor=west]{$x$};
\node at (37,-3)[anchor=west]{$x$};
\end{tikzpicture}
\end{align}

\pagebreak

\item {\bf Inserting a diagram for $\mac$ or $\mad$:} \\ for all objects $i\in I_\mac$, $x\in \Ob\mac$ or $i\in I_\mad$, $x\in \Ob\mad$ and morphisms $\phi: i\to x$ and $\psi: x\to i$
\begin{align}\label{pic:insert}
&\begin{tikzpicture}[scale=.26]
\node at (-10,0){$\sum_{\alpha}$};
\begin{scope}[shift={(-4,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[color=black, fill=white] (0,0) circle (3);
\draw[line width=.5pt, color=black] (0,3)--(0,0) node[midway, anchor=west]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (0,0)--(0,-3) node[midway, anchor=west]{$x$}  node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=east]{$\alpha$};
\end{scope}
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, stealth-] (0,3) node[anchor=south east]{$i$}.. controls (0,5) and (3,5) .. (3,3);
\draw[line width=.5pt] (0,-3)node[anchor=north east]{$i$}.. controls (0,-5) and (3,-5) .. (3,-3);
\draw[line width=.5pt, -stealth] (3,-3)--(3,0);
\draw[line width=.5pt,] (3,3)--(3,0);
\draw[line width=.5pt,-stealth] (0,3)--(0,0) node[anchor=east]{$x$};
\draw[line width=.5pt,-stealth] (0,0)--(0,-3);
\draw[color=black, fill=black] (0,2) circle (.2) node[anchor=east]{$\phi$};
\draw[color=black, fill=black] (0,-2) circle (.2) node[anchor=east]{$\alpha$};
\end{scope}
\node at (9,0){$=$};
\begin{scope}[shift={(16,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[color=black, fill=white] (0,0) circle (3);
\draw[line width=.5pt, color=black] (0,3)--(0,0) node[midway, anchor=west]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (0,0)--(0,-3) node[midway, anchor=west]{$x$}  node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=east]{$\phi$};
\end{scope}
\end{tikzpicture}\nonumber\\
&\begin{tikzpicture}[scale=.26]
\node at (-10,0){$\sum_{\alpha}$};
\begin{scope}[shift={(-4,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[color=black, fill=white] (0,0) circle (3);
\draw[line width=.5pt, color=black] (0,3)--(0,0) node[midway, anchor=west]{$x$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (0,0)--(0,-3) node[midway, anchor=west]{$i$}  node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=east]{$\alpha$};
\end{scope}
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, stealth-] (0,3) node[anchor=south east]{$i$}.. controls (0,5) and (3,5) .. (3,3);
\draw[line width=.5pt] (0,-3)node[anchor=north east]{$i$}.. controls (0,-5) and (3,-5) .. (3,-3);
\draw[line width=.5pt, -stealth] (3,-3)--(3,0);
\draw[line width=.5pt,] (3,3)--(3,0);
\draw[line width=.5pt,-stealth] (0,3)--(0,0) node[anchor=east]{$x$};
\draw[line width=.5pt,-stealth] (0,0)--(0,-3);
\draw[color=black, fill=black] (0,2) circle (.2) node[anchor=east]{$\alpha$};
\draw[color=black, fill=black] (0,-2) circle (.2) node[anchor=east]{$\psi$};
\end{scope}
\node at (9,0){$=$};
\begin{scope}[shift={(16,0)}]
\draw[draw=none, fill=gray, fill opacity=.2] (-30:5)--(30:5)--(90:5)--(150:5)--(210:5)--(270:5)--(330:5);
\draw[color=black, fill=white] (0,0) circle (3);
\draw[line width=.5pt, color=black] (0,3)--(0,0) node[midway, anchor=west]{$x$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt, color=black] (0,0)--(0,-3) node[midway, anchor=west]{$i$}  node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=east]{$\psi$};
\end{scope}
\end{tikzpicture}
\end{align}
\end{compactenum}
\end{theorem}
Here, the polygon diagrams on each side of a equation stand for the product of their cyclic evaluations.  It is assumed that all parts of the diagrams  that are not drawn coincide on the left-hand side and right-hand side    and that the object and morphism labels occur nowhere else in the diagrams. The vertex label $\alpha$ stands for the chosen projection and inclusion morphisms. The summations are over simple objects in the sets of representatives and over bases of the morphism spaces.  The functor $F$ in \eqref{pic:gluepoly} and \eqref{pic:closepoly} may  be a composite functor consisting of several lines or  an action functor $c\rhd -$ or $-\lhd d$. 


\begin{proof} Identity  \eqref{pic:gluepoly} follows from \eqref{eq:traceidnd}. 
The data at the boundaries and  in the interiors of the first and second diagram in \eqref{pic:gluepoly} that is not drawn combines into morphisms $\mu:n\to F(m)$ and $\nu: F(m)\to n$, respectively. The  diagram on the right-hand side of \eqref{pic:gluepoly}  is then given by the trace of $\nu\circ\mu$. Equation \eqref{eq:traceidnd}
 implies that the cyclic evaluations on the left-hand side and right-hand side  of \eqref{pic:gluepoly} are given by
\begin{align*}
\begin{tikzpicture}[scale=.3]
\node at (-8,0) {$\sum_{\alpha}$};
\begin{scope}[shift={(-3,0)}]
\draw[line width=1.5pt, color=red] (-.7,4)--(.7,4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (-.7,-4)--(.7,-4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (0,4)--(0,2);
\draw[line width=1pt, dashed] (0,2).. controls (-2,0).. (0,-2) node[midway, anchor=east]{$F$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=red] (0,-4)--(0,-2);
\draw[color=red, fill=red] (0,2) circle (.2) node[anchor=west]{$\mu$};
\draw[color=red, fill=red] (0,-2) circle (.2) node[anchor=west]{$\alpha$};
\end{scope}

\begin{scope}[shift={(3,0)}]
\draw[line width=1.5pt, color=red] (-.7,4)--(.7,4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (-.7,-4)--(.7,-4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (0,4)--(0,2);
\draw[line width=1pt, dashed] (0,2).. controls (-2,0).. (0,-2) node[midway, anchor=east]{$F$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=red] (0,-4)--(0,-2);
\draw[color=red, fill=red] (0,2) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=red, fill=red] (0,-2) circle (.2) node[anchor=west]{$\nu$};
\end{scope}
\node at (7,0) {$\stackrel{\eqref{pic:semisimpleids}}=$};
\begin{scope}[shift={(12,0)}]
\draw[line width=1.5pt, color=red] (-.7,4)--(.7,4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (-.7,-4)--(.7,-4) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=red] (0,4)--(0,2);
\draw[line width=1pt, dashed] (0,2).. controls (-2,0).. (0,-2) node[midway, anchor=east]{$F$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=red] (0,-4)--(0,-2);
\draw[color=red, fill=red] (0,2) circle (.2) node[anchor=west]{$\mu$};
\draw[color=red, fill=red] (0,-2) circle (.2) node[anchor=west]{$\nu$};
\end{scope}
\end{tikzpicture}
\end{align*}
The proof of \eqref{pic:insert} is analogous. The only difference is that it uses the traces of $\mac$ or $\mad$.
Identity \eqref{pic:closepoly}  is a direct consequence of the second identity in \eqref{eq:projincl}, depicted  in \eqref{pic:semisimpleids}. In this case, 
 the contributions of the diagram in the interior  and  the boundary morphisms that are not drawn  combine into a morphism  $\rho: F(m)\to F(m)$ in both diagrams. The cyclic evaluations of the left-hand side and right-hand side of \eqref{pic:closepoly}  are then given by
\begin{align*}
\begin{tikzpicture}[scale=.3]
\node at (-10,-1) {$\sum_{n,\alpha} \dim(n)$};

\begin{scope}[shift={(-3,0)}]
\draw[line width=1.5pt, color=red] (-2.5,4.4)--(.5,4.5) ;
\draw[line width=1.5pt, color=red] (-2.5,-6.5)--(.5,-6.5) ;
\draw[line width=1.5pt, color=blue] (0,4.5)node[ anchor=north west]{$m$} --(0,2) ;
\draw[line width=1.5pt, color=blue] (0,2)--(0,-1)node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=red] (0,-4)--(0,-1) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (0,-4)--(0,-6.5) node[anchor=south west]{$m$};
\draw[line width=1pt, dashed] (-1.5,4.5)node[anchor=north east]{$F$}--(0,2);
\draw[line width=1pt, dashed]  (0,2).. controls (-2,.5).. (0,-1) node[midway, anchor=east]{$F$};
\draw[line width=1pt, dashed] (-1.5,-6.5) node[anchor=south east]{$F$}--(0,-4);
\draw[color=red, fill=red] (0,2) circle (.2) node[anchor=west]{$\rho$};
\draw[color=red, fill=red] (0,-4) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=red, fill=red] (0,-1) circle (.2) node[anchor=west]{$\alpha$};
\end{scope}
\node at (1,0) {$\stackrel{\eqref{pic:semisimpleids}}=$};
\begin{scope}[shift={(6,0)}]
\draw[line width=1.5pt, color=red] (-2.5,2)--(.5,2) ;
\draw[line width=1.5pt, color=red] (-2.5,-4)--(.5,-4) ;
\draw[line width=1.5pt, color=blue] (0,2)node[ anchor=north west]{$m$} --(0,-4) node[anchor=south west]{$m$};
\draw[line width=1pt, dashed] (-1.5,2) node[anchor=north east]{$F$}--(0,-1);
\draw[line width=1pt, dashed] (-1.5,-4) node[anchor=south east]{$F$}--(0,-1);
\draw[color=red, fill=red] (0,-1) circle (.2) node[anchor=west]{$\rho$};
\end{scope}
\end{tikzpicture}
\end{align*}
Finally, to prove identity \eqref{pic:2gon}, we compute with the definition of  $\dim(n)$ and $\dim\mam$
\begin{align*}
\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-4,0)}]
\node at (-10,0){$\sum_{m,n,\alpha}$};
\node at (-6,0){$\dim(m)$};
\node at (-6,-1.5){$\dim(n)$};
\draw[line width=1.5pt, color=blue] (0,3.5)--(0,-3.5) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (-.5,3.5)--(.5,3.5) node[anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-.5,-3.5)--(.5,-3.5) node[anchor=west]{$m$};
\draw[line width=.5pt] (0,2)--(-2,0) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=south east]{$x$};
\draw[line width=.5pt] (-2,0)--(0,-2) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=north east]{$x$};
\draw[fill=black] (-2,0) circle (.2) node[anchor=east]{$\phi$};
\draw[blue,fill=blue] (0,2) circle (.2) node[anchor=west]{$\alpha$};
\draw[blue,fill=blue] (0,-2) circle (.2) node[anchor=west]{$\alpha$};
\end{scope}
\node at (-1.5,0){$\stackrel{\eqref{pic:cyclic trace}}=$};
\begin{scope}[shift={(11,0)}]
\node at (-9,0){$\sum_{m,n,\alpha}$};
\node at (-5,0){$\dim(m)$};
\node at (-5,-1.5){$\dim(n)$};
\draw[line width=1.5pt, color=blue] (0,3.5)--(0,-3.5) node[midway, anchor=west]{$m$};
\draw[line width=1.5pt, color=blue] (-2.5,3.5)--(.5,3.5);
\draw[line width=1.5pt, color=blue] (-2.5,-3.5)--(.5,-3.5);
\draw[line width=.5pt] (-2,3.5)--(-2,2) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=west]{$x$};
\draw[line width=.5pt] (-2,2)--(0,1) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=north east]{$x$};
\draw[line width=.5pt] (0,-1)--(-2,-3.5) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=east]{$x$};
\draw[fill=black] (-2,2) circle (.2) node[anchor=east]{$\phi$};
\draw[blue,fill=blue] (0,1) circle (.2) node[anchor=west]{$\alpha$};
\draw[blue,fill=blue] (0,-1) circle (.2) node[anchor=west]{$\alpha$};
\node at (0,3)[anchor=west, blue]{$n$};
\node at (0,-3)[anchor=west, blue]{$n$};
\end{scope}
\node at (14,0){$\stackrel{\eqref{pic:semisimpleids}}=$};
\begin{scope}[shift={(25,0)}]
\node at (-7,0){$\sum_{n}\dim(n)$};
\draw[line width=1.5pt, color=blue] (0,3.5)--(0,-3.5) node[midway, anchor=west]{$n$};
\draw[line width=1.5pt, color=blue] (-2.5,3.5)--(.5,3.5);
\draw[line width=1.5pt, color=blue] (-2.5,-3.5)--(.5,-3.5);
\draw[line width=.5pt] (-2,3.5)--(-2,0) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=east]{$x$};
\draw[line width=.5pt] (-2,0)--(-2,-3.5) node[sloped, pos=.5, allow upside down]{\arrowOut} node[midway, anchor=east]{$x$};
\draw[fill=black] (-2,0) circle (.2) node[anchor=east]{$\phi$};
\end{scope}
\node at (28,0){$\stackrel{\eqref{pic:cmoduletrace}}=$};
\begin{scope}[shift={(38,0)}]
\node at (-7,0){$\dim\mam$};
\draw[line width=.5pt] (-2,2)node[anchor=west]{$x$}--(-2,-2) node[anchor=west]{$x$} node[sloped, pos=.2, allow upside down]{\arrowOut} node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-4,-2)--(-4,2) node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-2,2)..controls (-2,3) and (-4,3)..(-4,2);
\draw[line width=.5pt] (-2,-2)..controls (-2,-3) and (-4,-3)..(-4,-2);
\draw[fill=black] (-2,0) circle (.2) node[anchor=west]{$\phi$};
\end{scope}
\end{tikzpicture}\\[-6ex]
\end{align*}
\end{proof}



Note that the first three identities in Theorem \ref{th:polyids} are precisely the elementary  transformations for polygon presentations of surface groups, see for instance  the books by Lee \cite[Ch.~6]{Lee} and by Seifert and Threlfall \cite[Ch.~6.38 and 6.40]{ST}.  Identity \eqref{pic:gluepoly} corresponds to the cutting and pasting operation,  identity \eqref{pic:closepoly} to the folding and unfolding operation and identity \eqref{pic:2gon} to the special case of the folding operation for $S^2$. 
 Identity \eqref{pic:insert} describes the insertion of data from spherical categories into polygon diagrams.
