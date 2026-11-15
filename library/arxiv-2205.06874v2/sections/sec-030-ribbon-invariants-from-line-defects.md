---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-030-ribbon-invariants-from-line-defects
section_title: "Ribbon invariants from line defects"
section_number: null
pages: 59-68
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.756
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
In this section we show how defect lines on trivial defect surfaces give rise to ribbon invariants.  These surfaces are labeled by a spherical fusion category $\mac$ as a $(\mac,\mac)$-bimodule category.   As $\mac$ is a spherical fusion category, its center $\mathcal Z(\mac)$ is a  ribbon category, see for instance \cite[Lemma 10.1]{TVr}. By Example \ref{ex:modulefuncs}, the monoidal category $\End_\mac(\mac)$  is  monoidally equivalent to $\mathcal Z(\mac)$. 
Under this monoidal equivalence, an object $(a, \sigma_{-,a})$ of $\mathcal Z(\mac)$  corresponds to the $(\mac,\mac)$-bimodule functor $F=a\oo -:\mac\to\mac$ with coherence data
\begin{align}\label{eq:coeherencecenter}
&s^F_{c,c'}=a_{c,a,c'}\circ (\sigma_{c,a}^\inv\oo 1_{c'})\circ a_{a,c,c'}^\inv: a\oo ( c\oo c')\to (a\oo c)\oo c'\to (c\oo a)\oo c'\to c\oo (a\oo c'),\\ 
&t^F_{c,c'}=a_{a,c,c'}: (a\oo c)\oo c'\to a\oo (c\oo c')\nonumber
\end{align}
and a morphism $\alpha: a\to b$ in $\mathcal Z(\mac)$  to the $(\mac,\mac)$-bimodule natural transformation $\nu=\alpha\oo -: a\oo -\Rightarrow b\oo -$ from Example \ref{ex:modulefuncs}. 

Any diagram representing a ribbon tangle for $\mathcal Z(\mac)$ can be realised as a defect graph on a trivial defect disc. This amounts to replacing
over- and undercrossings in the diagram  with defect vertices labeled by (inverse) braidings
and maxima and minima  by defect vertices labeled with the (co)evaluations in $\mathcal Z(\mac)$.
Every  diagram $D$ for a $(0,0)$-ribbon tangle  then defines a morphism $\alpha\in \End_{\mathcal Z(\mac)}(e)$ and
a  bimodule natural transformation $\nu=\alpha\oo -:\id_{\mac}\Rightarrow\id_\mac$  with
 $\nu_x=\tr(\alpha) 1_x=\mathrm{ev}(D)1_x: x\to x$ for every  $x\in I_\mac$.


\begin{example}\label{ex:ribbonplane} Let $\mac$ be a spherical fusion category and $t$ a tetrahedron as in Figure \ref{fig:dectet} (b) with a trivial defect surface that contains a diagram $D$ for a  $(0,0)$-ribbon tangle  labeled with  $\mathcal Z(\mac)$. 
Then one has
$$
\mathcal Z'(t, l_{\partial M}, b_{\partial M})=\mathrm{ev}(D) \cdot \mathrm{6j}(t', l_{\partial M}, b_{\partial M}),
$$
where $t'$ is the tetrahedron with the same labels and without the defects and $\mathrm{ev}(D)\in\C$ the evaluation of $D$.
\end{example}

\begin{proof} The 6j symbol of the defect tetrahedron $t$ is obtained from the associated polygon diagram
\begin{align*}
\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=west]{$q$} --(4,-4) node[anchor=west]{$n$}--(-4,-4)node[anchor=east]{$m$}--(-4,4) node[anchor=east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[color=white, fill=white] (0,0) circle (1.8); 
\draw[line width=1pt, color=cyan, dashed] (0,0) node[anchor=south] {$D$} circle (1.5); 
\draw[fill=white, color=white] (1.5,0) circle (.4);
\draw[fill=white, color=white] (-1.5,0) circle (.4);
\draw[line width=.5pt, color=black] (4,0)--(-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}
\end{align*}
where the dashed circle labeled $D$ contains the diagram $D$. 
This diagram superimposes the 6j symbol for  $t'$  and the  diagram  $D$.
By \eqref{eq:coeherencecenter},  overcrossings of the line labeled $i$ over lines in $D$ correspond to half-braidings $\sigma_{i,a}^{\pm 1}$, while overcrossings of lines in $D$ over $j$ correspond to associators  in $\mac$. The line labeled $i$ describes the functor $i\oo -: \mac\to\mac$ and the line labeled $j$ the functor $-\oo j:\mac\to\mac$. Identities \eqref{pic:rm2} to \eqref{pic:bimodulenat}  allow one to separate the two diagrams and yield the result. 
\end{proof}


Example \ref{ex:ribbonplane} shows that ribbon invariants can be realised as line and point defects on a trivial defect plane. However, 
this involves ribbon diagrams  rather than ribbons in three-dimensional space, and the braidings are external input, namely  defect data labeling vertices. We now show how ribbon invariants are obtained from line defects in a 3-ball that are not confined to a plane and where the braidings  arise from the   state sum. 



\begin{example} \label{ex:braiding}Let $\mac$ be spherical fusion category  as a $(\mac,\mac)$-bimodule category and  $F=a\oo -:\mac\to\mac$ and $G=b\oo -:\mac\to \mac$  the bimodule functors  for  $(a, \sigma_{-,a}),(b, \sigma_{-,b})\in\mathcal \Ob \mathcal Z(\mac)$ with coherence data as in
\eqref{eq:coeherencecenter}.
We consider the following three tetrahedra labeled with objects  in $I_\mac$: 
\begin{align*}
\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=cyan, line width=1pt] (2, 1)--(-2,1) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=south]{$F$};
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$k$};
\draw[draw=none, fill=white] (0,2.4) circle(.3);
\draw[draw=none, fill=white] (0,-2.4) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[draw=none, fill=white] (0,0) circle(.3);
\draw[line width=1pt, color=black] (-5,0)--(5,0)  node[sloped, pos=0.2, allow upside down]{\arrowIn} node[pos=.2, anchor=south]{$j$};
\draw[line width=.5pt, -stealth] (2,1)--(2.5,1.5);
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0) --(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)   node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$l$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (1,0) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=magenta, line width=1pt] (1,2.4)--(1,-2.4) node[pos=.7, anchor=west]{$G$} node[sloped, pos=0.7, allow upside down]{\arrowIn} ;
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$k$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\end{tikzpicture}
\end{align*}
Glue the first tetrahedron  to the second along the two  faces labeled with  $j,m,n$ and $j, p, q$ and the second to the third along the two  faces labeled with  $k,m,p$ and $k,n,q$.  This yields a triangulated 3-ball $M$ with  a one-holed torus as a trivial defect surface. 
Then the rescaled state sum  $\mathcal Z'(M, l_{\partial M}, b_{\partial M})$ is the 6j symbol of the  tetrahedron
\begin{align*}
\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$l$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[draw=none, fill=white] (1,0) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=magenta, line width=1pt] (1,2.4)--(1,-2.4) node[pos=.7, anchor=west]{$G$} node[sloped, pos=0.7, allow upside down]{\arrowIn} ;
\draw[draw=none, fill=white] (1,1) circle(.3);
\draw[color=cyan, line width=1pt] (2, 1)--(-2,1) node[pos=.7, anchor=south]{$F$}node[sloped, pos=.7, allow upside down]{\arrowIn} ;
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\begin{scope}[shift={(12,0)}, scale=.8]
\node at (-6,0)[anchor=east]{$=$};
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white]  (-1.4,-.4) circle (.3);
\draw[color=white, fill=white]  (-2.4,-.2) circle (.3);
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east] {$q$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south] {$n$};
\draw[line width=.5pt] (0,-3)--(2,-1) node[midway, anchor=north west] {$m$};
\draw[line width=.5pt] (0,-3)--(-2,1) node[midway, anchor=north east] {$i$};

\draw[line width=1pt, color=cyan] (-2,1) ..controls (-3,-2).. (0,-3) node[midway, anchor=east]{$a$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\beta\;$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\end{scope}
\end{tikzpicture}
\end{align*}
where the crossing of the lines labeled $F$ and $G$ on the defect surface is assigned the $(\mac,\mac)$-bimodule natural transformation $\nu=\sigma_{a,b}^\inv\oo -: (b\oo a)\rhd -\Rightarrow (a\oo b)\rhd -$.
\end{example}

\begin{proof} The polygon diagram and the associated 6j symbols for the first tetrahedron are given by
\begin{align*}
\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=gray] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,-.5) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) .. controls (0,-1.5) ..  (-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (4,0)--(-4,0) node[pos=.8, anchor=south]{$F$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=gray] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=east]{$j$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[color=white, fill=white] (-2.2,.2) circle (.4);
\draw[line width=.5pt, color=black] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor= east]{$i$};
\draw[line width=1pt, color=cyan, dashed] (0,1)  .. controls (-5,0) and (-5,-2) .. (0,-3)  node[midway, anchor=south east]{$F$};
\node at (0,2)[anchor=west, color=black] {$q$};
\node at (0,0)[anchor=west, color=black] {$n$};
\node at (0,-2)[anchor=west, color=black] {$m$};

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=black, fill=black] (0,1) circle (.2) node[anchor=west]{$\;\beta$};
\draw[color=black, fill=black] (0,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=south east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$j$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(0,-3) node[midway, anchor=north east]{$i$};  
\draw[line width=1pt, color=cyan] (-2,1) ..controls (-3,-2).. (0,-3) node[midway, anchor=east]{$a$};
\draw[line width=.5pt] (2,-1)--(0,-3) node[midway, anchor=north west]{$m$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\beta\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\end{tikzpicture}
\end{align*}
where the first diagram for the 6j symbol is  in the diagrammatic notation of the previous sections and the second the usual diagram for a spherical fusion category as in \cite{TV, BW}, with the objects from $\mathcal Z(\mac)$ highlighted in colour. It is obtained from the second diagram by inserting the functor $-\oo j:\mac\to\mac$ for the  line labeled $j$ and the functor  $F(i\oo-)=a\oo (i\oo -):\mac\to\mac$ for the lines with $F$ and $i$. 

The polygon diagram and 6j symbols for the second tetrahedron are given by
\begin{align*}
\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$m$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$q$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=gray] (4,0)--(-4,0) node[pos=.8, anchor=north]{$j$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,0) circle (.4);
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.8, anchor=west]{$k$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\rho$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\gamma$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\tau$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\alpha$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=gray] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor= east]{$j$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[line width=.5pt, color=black] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor=east]{$k$};
\node at (0,2)[anchor=west, color=black] {$m$};
\node at (0,0)[anchor=west, color=black] {$n$};
\node at (0,-2)[anchor=west, color=black] {$q$};

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\rho$};
\draw[color=black, fill=black] (0,1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-1) circle (.2) node[anchor=west]{$\;\tau$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\alpha$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(2,1) node[midway, anchor=south west]{$m$};
\draw[line width=.5pt] (0,3)--(-2,-1) node[midway, anchor=south east] {$k$};
\draw[line width=.5pt] (-2,-1)--(2,1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (2,1)--(0,-3) node[midway, anchor=north west]{$j$};  
\draw[line width=.5pt] (-2,-1)--(0,-3) node[midway, anchor=north east]{$q$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\rho$};
\draw[color=black, fill=black] (2,1) circle (.2) node[anchor=west]{$\gamma\;$};
\draw[color=black, fill=black] (-2,-1) circle (.2) node[anchor=east]{$\;\tau$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\alpha$};
\end{tikzpicture}
\end{align*}
Note that here the polygon diagram is viewed from the back, not the front, since the trivial defect plane is oriented in the opposite direction. Again, the second diagram for the 6j symbol is the standard diagram for a spherical fusion category obtained by inserting the functors $k\oo-: \mac\to\mac$ and $-\oo j:\mac\to\mac$ for the black line labeled $k$ and the grey line labeled $j$ in the second diagram. 


The polygon diagram and the 6j symbols for the third tetrahedron are given by
\begin{align*}
\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=gray] (0,4).. controls (1.5,0)..(0,-4) node[pos=.8, anchor=west]{$l$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=magenta, dashed] (0,4)--(0,-4) node[pos=.8, anchor=east]{$G$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[fill=white, color=white] (.5,0) circle (.9);
\draw[line width=.5pt, color=black] (4,0)--(-4,0) node[pos=.8, anchor=south]{$k$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\nu$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\tau$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\mu$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\rho$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=1.5pt, color=black] (0,5)--(0,-5);
\draw[line width=1pt, color=magenta, dashed] (0,3)  .. controls (-5,2) and (-5,0) .. (0,-1)  node[midway, anchor= east]{$G$};
\draw[line width=.5pt, color=gray] (0,3)  .. controls (-3,2) and (-3,0) .. (0,-1)  node[midway, anchor= east]{$l$};
\draw[color=white, fill=white] (-2,0) circle (.4);
\draw[color=white, fill=white] (-2.2,-.5) circle (.4);
\draw[line width=.5pt, color=black] (0,1)  .. controls (-3,0) and (-3,-2) .. (0,-3)  node[midway, anchor= east]{$k$};
\node at (0,2)[anchor=west, color=black] {$q$};
\node at (0,0)[anchor=west, color=black] {$n$};
\node at (0,-2)[anchor=west, color=black] {$m$};

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (0,1) circle (.2) node[anchor=west]{$\;\tau$};
\draw[color=black, fill=black] (0,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\rho$};
\end{tikzpicture}

\qquad

\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-1.3,-.5) circle (.4);
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(0,-3) node[midway, anchor=north east]{$k$};  
\draw[line width=.5pt] (2,-1)--(0,-3) node[midway, anchor=north west]{$m$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\rho$};
\end{tikzpicture}
\end{align*}
Here, the second 6j symbol is obtained from the first by inserting the functor $k\oo -:\mac\to \mac$ for the black line labeled $k$ and the functor $G(-\oo l)=b\oo (-\oo l):\mac\to\mac$ for the
lines labeled $G$ and $l$. The crossing in the second 6j symbol stands for the morphism $\sigma^\inv_{k,b}: b\oo k\to k\oo b$ associated with $b$.  

The rescaled state sum is obtained by multiplying the three 6j symbols and the dimensions of the internal edges, summing over the labels $j,k\in I_\mac$  and over the morphisms $\alpha,\gamma,\rho,\tau$ assigned to the glued faces
\begin{align*}
&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\node at (-5,0) [anchor=east]{$\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\sum_{\substack{{j,k}\\{\alpha,\gamma,\rho,\tau}}} \dim(j)\dim(k)$};
\begin{scope}[shift={(0,0)}]
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=south east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$j$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(0,-3) node[midway, anchor=north east]{$i$};  
\draw[line width=1pt, color=cyan] (-2,1) ..controls (-3,-2).. (0,-3) node[midway, anchor=east]{$a$};
\draw[line width=.5pt] (2,-1)--(0,-3) node[midway, anchor=north west]{$m$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\beta\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\end{scope}

\begin{scope}[shift={(8,0)}]
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(2,1) node[midway, anchor=south west]{$m$};
\draw[line width=.5pt] (0,3)--(-2,-1) node[midway, anchor=south east] {$k$};
\draw[line width=.5pt] (-2,-1)--(2,1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (2,1)--(0,-3) node[midway, anchor=north west]{$j$};  
\draw[line width=.5pt] (-2,-1)--(0,-3) node[midway, anchor=north east]{$q$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\rho$};
\draw[color=black, fill=black] (2,1) circle (.2) node[anchor=west]{$\gamma\;$};
\draw[color=black, fill=black] (-2,-1) circle (.2) node[anchor=east]{$\;\tau$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\alpha$};
\end{scope}

\begin{scope}[shift={(17,0)}]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-1.3,-.5) circle (.4);
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(0,-3) node[midway, anchor=north east]{$k$};  
\draw[line width=.5pt] (2,-1)--(0,-3) node[midway, anchor=north west]{$m$};    

\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\rho$};
\end{scope}
\end{tikzpicture}
\end{align*}
To  compute this state sum we first use   \eqref{pic:gluepoly} to glue the polygon diagrams along the faces labeled by the objects $k,m,p$ and $q,j,p$  and the morphisms $\rho$ and $\alpha$. 
 We then  simplify the resulting expressions with  \eqref{eq:traceout}  and  apply  \eqref{eq:snake} together with the naturality of the half-braiding. This gives
\begin{align*}

&\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-2,-.2) circle(.4);
\node at (-3,-3) [anchor=east]{$\mathcal Z'(M, l_{\partial M}, b_{\partial M})\stackrel{\eqref{pic:gluepoly}}=\sum_{\substack{{j,k}\\{\gamma,\tau}}} \dim(j)$};
\node at (-3,-4)[anchor=east]{$\dim(k)$};
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-11)--(0,-13); 
\draw[line width=.5pt, color=black] (-1,-13)--(1,-13) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(-2,-5) node[midway, anchor=north east]{$k$};  
\draw[line width=.5pt] (2,-1)--(2,-3) node[midway, anchor=west]{$m$};  
\draw[line width=.5pt] (2,-3)--(-2,-5) node[midway, anchor=south]{$n$};    
\draw[line width=.5pt] (-2,-5)--(-2,-7) node[midway, anchor=east]{$q$};  
\draw[line width=.5pt] (2,-3)--(2,-9) node[midway, anchor=west]{$j$};  
\draw[line width=.5pt] (-2,-7)--(2,-9) node[midway, anchor=south]{$n$};  
\draw[line width=.5pt] (0,-11)--(2,-9) node[midway, anchor=north west]{$m$};  
\draw[line width=.5pt] (0,-11)--(-2,-7) node[midway, anchor=north east]{$i$};  


\draw[line width=1pt, color=cyan] (-2,-7) ..controls (-3,-10).. (0,-11) node[midway, anchor=east]{$a$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-2,-5) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-3) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (-2,-7) circle (.2) node[anchor=east]{$\;\beta$};
\draw[color=black, fill=black] (2,-9) circle (.2) node[anchor=west]{$\;\gamma$};
\draw[color=black, fill=black] (0,-11) circle (.2) node[anchor=west]{$\;\delta$};

\begin{scope}[shift={(13,0)}]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-2,-.2) circle(.4);
\node at (-3,-3) [anchor=east]{$\stackrel{\eqref{eq:traceout}}=\sum_{k,\tau} \dim(k)$};
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-11)--(0,-13); 
\draw[line width=.5pt, color=black] (-1,-13)--(1,-13) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south]{$n$};
\draw[line width=.5pt] (-2,1)--(-2,-5) node[midway, anchor=north east]{$k$};  
\draw[line width=.5pt] (2,-1)--(0,-11) node[midway, anchor=west]{$m$};  
\draw[line width=.5pt] (-2,-5)--(-2,-7) node[midway, anchor=east]{$q$};   
\draw[line width=.5pt] (0,-11)--(-2,-7) node[midway, anchor=north east]{$i$}; 
 
 \draw[line width=.5pt] (-2,-7).. controls (-1,-8) and (0,-8).. (0,-7);
 \draw[line width=.5pt] (-2,-5).. controls (-1,-4) and (0,-4).. (0,-5); 
 \draw[line width=.5pt] (0,-7)--(0,-5) node[midway, anchor=east]{$n$} node[sloped, pos=.5, allow upside down]{\arrowOut};


\draw[line width=1pt, color=cyan] (-2,-7) ..controls (-3,-10).. (0,-11) node[midway, anchor=east]{$a$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-2,-5) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (-2,-7) circle (.2) node[anchor=east]{$\;\beta$};
\draw[color=black, fill=black] (0,-11) circle (.2) node[anchor=west]{$\;\delta$};
\end{scope}

\begin{scope}[shift={(24.5,0)}]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-1.4,-.4) circle(.4);
\draw[color=white, fill=white] (.4,-.8) circle(.4);
\node at (-3,-3) [anchor=east]{$\stackrel{\eqref{eq:snake}}=\sum_{k,\tau} \dim(k)$};
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt] (0,-11)--(0,-13); 
\draw[line width=.5pt, color=black] (-1,-13)--(1,-13) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,3)--(-2,-2) node[midway, anchor=east]{$q$};
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (-2,-2).. controls (-.2,-5) and (.2,2).. (2,-1) node[midway, anchor=north west]{$n$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-2,-2)--(-2,-5) node[pos=.3, anchor=north east]{$k$};  
\draw[line width=.5pt] (2,-1)--(0,-11) node[midway, anchor=west]{$m$};  
\draw[line width=.5pt] (-2,-5)--(-2,-7) node[midway, anchor=east]{$q$};   
\draw[line width=.5pt] (0,-11)--(-2,-7) node[midway, anchor=north east]{$i$}; 
 
 \draw[line width=.5pt] (-2,-7).. controls (-1,-8) and (0,-8).. (0,-7);
 \draw[line width=.5pt] (-2,-5).. controls (-1,-4) and (0,-4).. (0,-5); 
 \draw[line width=.5pt] (0,-7)--(0,-5) node[midway, anchor=east]{$n$} node[sloped, pos=.5, allow upside down]{\arrowOut};


\draw[line width=1pt, color=cyan] (-2,-7) ..controls (-3,-10).. (0,-11) node[midway, anchor=east]{$a$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (-2,-2) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-2,-5) circle (.2) node[anchor=east]{$\tau\;$};
\draw[color=black, fill=black] (-2,-7) circle (.2) node[anchor=east]{$\;\beta$};
\draw[color=black, fill=black] (0,-11) circle (.2) node[anchor=west]{$\;\delta$};
\end{scope}
\end{tikzpicture}
\end{align*}
Applying again identities \eqref{eq:traceout}  and  \eqref{eq:snake} together with the naturality of the half-braiding   yields
\begin{align*}
\begin{tikzpicture}[scale=.4, baseline=(current bounding box.center)]
\node at (-5,0) [anchor=east]{$\mathcal Z'(M, l_{\partial M}, b_{\partial M})\stackrel{\eqref{eq:traceout}}=$};
\begin{scope}[scale=.7, shift={(0,2)}]
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white] (-1.7,-.3) circle(.4);
\draw[color=white, fill=white] (.2,-.7) circle(.4);
\draw[line width=.5pt, color=black] (-1.5,5)--(1.5,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt, color=black] (-1.5,-9)--(1.5,-9) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,-7)--(0,-9); 
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (0,3)--(-3,-3) node[pos=.3, anchor=east]{$q$};
\draw[line width=.5pt] (0,-7)--(2,-1) node[midway, anchor=north west]{$m$};
\draw[line width=.5pt]  (-3,-3).. controls (-1,-6.5) and  (0,2.5) ..  (2,-1) node[pos=.5, anchor=east]{$n$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[line width=.5pt] (0,-7)--(-3,-3) node[pos=.3, anchor=south west]{$i$}; 
\draw[line width=1pt, color=cyan] (-3,-3) ..controls (-4,-6).. (0,-7) node[midway, anchor=east]{$a$};

\draw[color=black, fill=black] (0,3) circle (.28) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (2,-1) circle (.28) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-3,-3) circle (.28) node[anchor=east]{$\beta\;$};
\draw[color=black, fill=black] (0,-7) circle (.28) node[anchor=west]{$\;\delta$};
\end{scope}

\begin{scope}[shift={(11,0)}]
\node at (-6,0)[anchor=east]{$\stackrel{\eqref{eq:snake}}=$};
\draw[line width=1pt, color=magenta] (0,3) ..controls (-6,2) and (-6,0) .. (2,-1) node[midway, anchor=east]{$b$};
\draw[color=white, fill=white]  (-1.4,-.4) circle (.3);
\draw[color=white, fill=white]  (-2.4,-.2) circle (.3);
\draw[line width=.5pt, color=black] (-1,5)--(1,5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,5)--(0,3); 
\draw[line width=.5pt, color=black] (-1,-5)--(1,-5) node[anchor=west]{$p$};
\draw[line width=.5pt] (0,-5)--(0,-3); 
\draw[line width=.5pt] (0,3)--(2,-1) node[midway, anchor=south west] {$l$};
\draw[line width=.5pt] (0,3)--(-2,1) node[midway, anchor=east] {$q$};
\draw[line width=.5pt] (-2,1)--(2,-1) node[midway, anchor=south] {$n$};
\draw[line width=.5pt] (0,-3)--(2,-1) node[midway, anchor=north west] {$m$};
\draw[line width=.5pt] (0,-3)--(-2,1) node[midway, anchor=north east] {$i$};

\draw[line width=1pt, color=cyan] (-2,1) ..controls (-3,-2).. (0,-3) node[midway, anchor=east]{$a$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\;\nu$};
\draw[color=black, fill=black] (2,-1) circle (.2) node[anchor=west]{$\;\mu$};
\draw[color=black, fill=black] (-2,1) circle (.2) node[anchor=east]{$\beta\;$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\;\delta$};
\end{scope}
\end{tikzpicture}
\end{align*}
\end{proof}


Example \ref{ex:braiding} allows one to construct any  ribbon link invariant for the centre $\mathcal Z(\mac)$ of a spherical fusion category $\mac$ from state sums that involve only defect surfaces and defect lines. This is achieved by considering a  ribbon diagram and realising each crossing as in Example \ref{ex:braiding}.  


\begin{example}\label{ex:tangleex} Let $\mac$ be a spherical fusion category with center $\mathcal Z(\mac)$ and $L$ a ribbon link whose connected components are labeled by objects of $\mathcal Z(\mac)$.  Let $M$ be the following triangulated 3-manifold with defect data:
\begin{enumerate}
\item  Realise a  ribbon diagram $D_L$ for $L$  as a  
PL diagram  that is the horizontal and vertical composite of the following squares  and the ones obtained by rotating them, reversing orientation in the third square and replacing an over- by an undercrossing in the last square 
\begin{align*}
\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, dotted] (-4,4)--(4,4) --(4,-4)--(-4,-4)--(-4,4);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, dotted] (-4,4)--(4,4) --(4,-4)--(-4,-4)--(-4,4);
\draw[line width=1pt, color=cyan, style=dashed] (4,0)--(-4,0) node[pos=.5, anchor=north] {$a$} node[sloped, pos=.5, allow upside down]{\arrowIn};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, dotted] (-4,4)--(4,4) --(4,-4)--(-4,-4)--(-4,4);
\draw[line width=1pt, color=cyan, style=dashed] (0,4)--(0,0)--(-4,0) node[pos=.6, anchor=north] {$a$} node[sloped, pos=.6, allow upside down]{\arrowIn};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=.3]
\draw[line width=1pt, dotted] (-4,4)--(4,4) --(4,-4)--(-4,-4)--(-4,4);
\draw[line width=1pt, color=magenta, style=dashed] (0,4)--(0,-4) node[pos=.8, anchor=west] {$b$} node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[fill=white, color=white] (0,0) circle (1.2);
\draw[line width=1pt, color=cyan, style=dashed] (4,0)--(-4,0) node[pos=.7, anchor=north] {$a$} node[sloped, pos=.7, allow upside down]{\arrowIn};
\end{tikzpicture}
 \end{align*}



\item  Assign to a  dashed line with label $(a,\sigma_{-,a})$ in $\mathcal Z(\mac)$   the $(\mac,\mac)$-bimodule functor $F_a=a\oo -: \mac\to\mac$  with coherence data as in \eqref{eq:coeherencecenter}, to a crossing with labels $a,b$  the bimodule natural transformation given by  $\sigma_{a,b}^{\pm 1}$, as in Example \ref{ex:braiding}, and to the midpoint of the second  and  third diagram either the identity or  the (co)units  of the  adjunction $F_a^l\dashv F_a$. 

\item Draw solid vertical and horizontal lines in each square that connect the midpoints of the boundary edges and end to the left of the dashed lines, viewed in the direction of their orientation. Let the vertical  line cross under and the horizontal  line over all other lines of the diagram. 

\item 
Label each vertex of the square and each solid line  by a simple object of $\mac$, such that the labels match at the vertices and edges where the squares are glued to form the  diagram $D_L$. Label each  endpoint of lines at the boundary  by a morphism in the appropriate morphism space in $\mac$
\begin{align*}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,0) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) --(-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}

&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,-.5) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) .. controls (0,-1.5) ..  (-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (4,0)--(-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}

&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,0) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) --(-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (0,4).. controls (-1,1).. (-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}

&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, color=magenta, dashed] (0,4)--(0,-4) node[pos=.8, anchor=east]{$b$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4).. controls (1.5,0) ..(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (.5,-.5) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) .. controls (0,-1.5) ..  (-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (4,0)--(-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{tikzpicture}                                             
\end{align*}

\item Assign to  each  square in 4.~a defect tetrahedron for the $(\mac,\mac)$-bimodule category $\mac$ whose 6j symbol is the polygon diagram in 4.~,  as in Figure \ref{fig:basictets}. Construct the last defect tetrahedron in Figure \ref{fig:basictets} as in Example \ref{ex:braiding} by gluing three tetrahedra with defect planes without crossings.

\item The polygon diagrams glue to a diagram that superimposes $D_L$ with additional edges labeled by objects of $\mac$, whose endpoints  are labeled by morphisms in $\mac$. This defines a gluing pattern for the associated tetrahedra, as   in Figure \ref{fig:braidingtet}, that yields  a triangulated 3-ball $M$ with a ribbon link $L'$ in the interior.
\end{enumerate}
The state sum of $M$ is  
\begin{align*}
\mathcal Z(M, l_{\partial M}, b_{\partial M})=\mathrm{ev}(D_L)\cdot\mathcal Z(M', l_{\partial M}, b_{\partial M}) ,
\end{align*}
where $\mathcal Z(M', l_{\partial M}, b_{\partial M})$ is the  state sum of the 3-ball $M'$ with the same labels, but without  defects.
\end{example}

\begin{figure}
\begin{align*}
&\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\begin{scope}[shift={(12,0)}, scale=.7]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,0) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) --(-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{scope}
\end{tikzpicture}
\\
&\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=cyan, line width=1pt] (2, 1)--(-2,1) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=south]{$F_a$};
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\begin{scope}[shift={(12,0)}, scale=.7]
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,-.5) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) .. controls (0,-1.5) ..  (-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (4,0)--(-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{scope}
\end{tikzpicture}
\\
&\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=cyan, line width=1pt] (1, 1)--(-2,1) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=south]{$F_a$};
\draw[color=cyan, line width=1pt] (1, 2.4)--(1,1) node[sloped, pos=0.7, allow upside down]{\arrowIn};
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\begin{scope}[shift={(12,0)}, scale=.7]
 \draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4)--(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (0,0) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) --(-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (0,4).. controls (-1,1).. (-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{scope}
\end{tikzpicture}
\\
&\begin{tikzpicture}[scale=.5]
\draw[line width=1pt, color=black] (-5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south east]{$p$};
\draw[line width=1pt, color=black] (5,0)--(0,4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=south west]{$q$};
\draw[line width=1pt, color=black] (-5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north east]{$m$};
\draw[line width=1pt, color=black] (5,0)--(0,-4)  node[sloped, pos=0.4, allow upside down]{\arrowIn} node[pos=.4, anchor=north west]{$n$};
\draw[line width=1pt, color=black] (-5,0)--(-.5,0)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[line width=1pt, color=black] (.5,0)--(5,0)  ;
\draw[draw=none, fill=white] (-2,0) circle(.3);
\draw[draw=none, fill=white] (2,0) circle(.3);
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[draw=none, fill=white] (1,0) circle(.3);
\draw[line width=1pt, dotted] (-2,2.4)--(-2,-2.4)--(2,-2.4)--(2,2.4)--(-2,2.4);
\draw[draw=none, fill=white] (0,2.4) circle(.5);
\draw[draw=none, fill=white] (0,-2.4) circle(.5);
\draw[color=magenta, line width=1pt] (1,2.4)--(1,-2.4) node[pos=.7, anchor=west]{$F_b$} node[sloped, pos=0.7, allow upside down]{\arrowIn} ;
\draw[draw=none, fill=white] (1,1) circle(.3);
\draw[color=cyan, line width=1pt] (2, 1)--(-2,1) node[pos=.7, anchor=south]{$F_a$}node[sloped, pos=.7, allow upside down]{\arrowIn} ;
\draw[draw=none, fill=white] (0,1) circle(.3);
\draw[line width=1pt, color=black] (0,-4)--(0,4)  node[sloped, pos=.3, allow upside down]{\arrowIn} node[pos=.3, anchor=east]{$i$};
\draw[line width=.5pt, -stealth] (2,-1)--(2.5,-1.5);
\begin{scope}[shift={(12,0)}, scale=.7]
\draw[line width=1pt, color=magenta, dashed] (0,4)--(0,-4) node[pos=.8, anchor=east]{$b$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[line width=1pt, dotted] (-4,4)--(4,4)node[anchor=south west]{$q$} --(4,-4) node[anchor=north west]{$n$}--(-4,-4)node[anchor=north east]{$m$}--(-4,4) node[anchor=south east]{$p$};
\draw[line width=.5pt, color=black] (0,4).. controls (1.5,0) ..(0,-4) node[pos=.2, anchor=west]{$j$}node[sloped, pos=.2, allow upside down]{\arrowOut};
\draw[fill=white, color=white] (.5,-.5) circle (1.2);
\draw[line width=.5pt, color=black] (4,0) .. controls (0,-1.5) ..  (-4,0) node[pos=.8, anchor=north]{$i$}node[sloped, pos=.8, allow upside down]{\arrowOut};
\draw[line width=1pt, color=cyan, dashed] (4,0)--(-4,0) node[pos=.8, anchor=south]{$a$}node[sloped, pos=.8, allow upside down]{\arrowIn};
\draw[color=black, fill=black] (0,4) circle (.2) node[anchor=south]{$\alpha$};
\draw[color=black, fill=black] (4,0) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,-4) circle (.2) node[anchor=north]{$\gamma$};
\draw[color=black, fill=black] (-4,0) circle (.2) node[anchor=east]{$\delta$};
\end{scope}
\end{tikzpicture}
\end{align*}
\caption{Defect tetrahedra assigned to the square diagrams from Example \ref{ex:tangleex}. The last tetrahedron is obtained by gluing three tetrahedra without crossings as in Example \ref{ex:braiding}.}
 \label{fig:basictets}
\end{figure}

\begin{figure}
\begin{center}
\def\svgwidth{.8\columnwidth}
 
 \end{center}
\caption{Gluing four defect tetrahedra and the associated polygon diagram.}
 \label{fig:braidingtet}
\end{figure}


\begin{proof} As the dimension factors for boundary edges and vertices coincide for $M$ and $M'$, it is sufficient to consider the rescaled state sums. 
By Proposition \ref{th:topological invariance} and Example \ref{ex:braiding}, the rescaled state sum for $M$ is the evaluation of the polygon diagram obtained by gluing all defect squares. This is the ribbon diagram $D_L$, superimposed with a graph labeled by  $\mac$,  which  is the dual of the triangulation on $\partial M$. 

The evaluation of this polygon diagram is computed as in Example \ref{ex:ribbonplane}. By \eqref{eq:coeherencecenter}   overcrossings of solid lines over lines in $T$ correspond to half-braidings of objects of $\mathcal Z(\mac)$ with objects in $\mac$, while undercrossings correspond to associators  in $\mac$.  As all vertices involve only solid lines,  one can use  identities \eqref{pic:rm2} to \eqref{pic:bimodulenat} to separate the graph labeled by $\mac$ and the 
 diagram  $D_L$. This yields the product of  the rescaled state sum $\mathcal Z'(M',l_{\partial M}, b_{\partial M})$ and the  evaluation of $D_L$.
\end{proof}


Example \ref{ex:tangleex} constructs a specific example of a triangulated  3-ball with a ribbon link as a defect. An analogous factorisation of the state sum is obtained for any  ribbon link labeled by $\mathcal Z(\mac)$   in any triangulated 3-ball labeled by $\mac$. This follows from the triangulation independence of the state sum and the fact that it is invariant under $\Delta$-moves, which encode ambient isotopies of ribbon links.


\begin{proposition}\label{prop:ribbonball} Let $M$ be a triangulated 3-ball labeled by a spherical fusion category $\mac$.  Let $L$ be a ribbon link in the interior of $M$ that is blackboard-framed with respect to a disc bisecting $M$ and labeled by $\mathcal Z(\mac)$. Then the state sum is given by
$$
\mathcal Z(M,l_{\partial M}, b_{\partial M})=\mathcal Z(M', l_{\partial M}, b_{\partial M})\cdot \mathrm{ev}(D_L),
$$
where $\mathcal Z(M', l_{\partial M}, b_{\partial M})$ is the state sum of the 3-ball $M'$  with the same labels, but  without the link, and $D_L$ a ribbon diagram obtained by projecting $L$ on the disc.
\end{proposition}

\begin{proof} 1.~We first show that the state sum is invariant under PL ambient isotopy of the ribbon link. By a result of Graeub \cite{Gr}, see also Burde and Zieschang \cite[Prop.~1.10]{BZ}
and Yetter \cite[Sec.~2.2]{Y}, two PL links in a 3-ball are ambient isotopic iff they are related by  a finite sequence of $\Delta$-moves. 
A $\Delta$-move 
places a triangle on the link that intersects it only  in one side and replaces this side by the other two sides of the triangle. 
\begin{center}
\begin{tikzpicture}[scale=.4]
\draw[line width=1pt] (0,1)--(5,1);
\draw[line width=1pt] (0,1)--(-1,.5);
\draw[line width=1pt] (5,1)--(6,.5);
\draw[line width=1pt, style=dashed] (0,1)--(2.5,3.5);
\draw[line width=1pt, style=dashed] (5,1)--(2.5,3.5);

\draw[line width=1pt, -stealth] (7.5,2)--(9.5,2) node[midway, anchor=south]{$\Delta$};

\begin{scope}[shift={(12,0)}]
\draw[line width=1pt] (0,1)--(-1,.5);
\draw[line width=1pt] (5,1)--(6,.5);
\draw[line width=1pt, ] (0,1)--(2.5,3.5);
\draw[line width=1pt, ] (5,1)--(2.5,3.5);
\draw[line width=1pt, style=dashed] (0,1)--(5,1);
\end{scope}
\end{tikzpicture}
\end{center}


An analogous result holds for ambient isotopies of blackboard-framed  ribbon links if one restricts attention to $\Delta$-moves that respect the framing, that is, keep the links blackboard framed  and can be realised without introducing kinks, see for instance \cite[Sec.~2.2]{Y}. Thus it is sufficient to show that the state sum is invariant under $\Delta$-moves that respect the blackboard framing of $L$. 



Consider a blackboard framed $\Delta$-move with a triangle $\Delta$.  By Corollary \ref{cor:pachner} and Lemma \ref{lem:finetriang}, suppose without loss of generality  that the tetrahedra intersecting $\Delta$ form a fine neighbourhood of $\Delta$ and that  gluing all tetrahedra that intersect $\Delta$ yields a triangulated 3-ball $B$ bisected by a defect plane that extends $\Delta$.

By Proposition \ref{th:topological invariance} the state sums for $B$ before and after the $\Delta$-move are obtained by projecting the dual of its boundary triangulation on the defect plane and evaluating the resulting polygon diagram. This yields ribbon diagrams that superimpose a ribbon segment labeled by $\mathcal Z(\mac)$ with the boundary diagrams labeled by $\mac$. The polygon diagrams before and after the $\Delta$-move are related by a $\Delta$-move on the ribbon segment in the polygon. Identities \eqref{pic:rm2} to \eqref{pic:natfuncconst}  imply that the evaluations of these polygon diagrams are equal.  As $M\setminus B$ is not affected by the $\Delta$-move,  the state sum of $M$ is invariant under the $\Delta$-move by Corollary \ref{cor:gluing}. 

2.~By applying 2d isotopies to the ribbon diagram $D_L$, one can transform it into a diagram $D'$ as in Example \ref{ex:tangleex} and construct a triangulated 3-ball $N$ with a ribbon link $L'$ in the interior that projects to $D'=D_{L'}$.  By Example \ref{ex:tangleex} one has
$\mathcal Z(N, l_{\partial N}, b_{\partial N})=\mathcal Z(N', l_{\partial N}, b_{\partial N})\cdot \mathrm{ev}(D_{L'})$, where $N'$ is the 3-ball  without $L'$.  

As the boundary triangulations of $M$ and $N$ are related by elementary shellings and inverse shellings with tetrahedra that do not intersect $L$ and $L'$, it is sufficient to show that  $\mathcal Z(M, l_{\partial M}, b_{\partial M})=\mathcal Z(N, l_{\partial N}, b_{\partial N})$, if the labeled boundary triangulations for $M$ and $N$ agree. 
As the link diagrams $D_L$ and $D_{L'}$ are isotopic, one has $\mathrm{ev}(D_{L})=\mathrm{ev}(D_{L'})$ and the links $L$ and $L'$ that project to $D_L$ and $D_{L'}$ are ambient isotopic. This allows one to transform $L$ into $L'$ by a finite sequence of $\Delta$-moves. The first part of the proof implies that this does not affect the state sum. By the triangulation independence of the usual Turaev-Viro-Barrett-Westbury state sum, one has $\mathcal Z(M', l_{\partial M}, b_{\partial M})=\mathcal Z(N', l_{\partial N}, b_{\partial N})$, and with
Theorem \ref{th:fulltopinv} this yields
$$\mathcal Z(M, l_{\partial M}, b_{\partial M})\stackrel{1.}=\mathcal Z(N, l_{\partial N}, b_{\partial N})\stackrel{\ref{ex:tangleex}}=\mathrm{ev}(D_{L'})\cdot \mathcal Z(N', l_{\partial N}, b_{\partial N})\stackrel{\ref{th:fulltopinv}}=\mathrm{ev}(D_{L})\cdot \mathcal Z(M', l_{\partial M}, b_{\partial M}).$$
\end{proof}

Proposition \ref{prop:ribbonball} can be generalised  to  ribbon tangles realised as defect graphs on trivial defect surfaces. One can also generalise it to ribbon links embedded  in more general 3-manifolds. Embedding a ribbon link $L$ labeled by $\mathcal Z(\mac)$ in a single tetrahedron labeled by $\mac$ and gluing it to the  tetrahedron with the opposite orientation  along all four faces yields the state sum for a 3-sphere  $L$  in the interior
$$\mathcal Z(S^3,L)=\frac{\mathrm{ev}(D_L)} {\dim \mac}.$$
This coincides with Turaev and Virelizier's  state sum graph TQFT  for a 3-sphere containing a ribbon link in  \cite[Th.~16.1]{TVbook}.  In fact, we expect that our state sums with defect lines and vertices on trivial defect surfaces always coincide with the corresponding  graph TQFTs with ribbons from \cite[Ch.~16]{TVbook} and \cite{TVr}.  It would  be nice to show this in full generality and  to compare with the results by Balsam and Kirillov in  \cite{KB,B} that also involve ribbons labeled by $\mathcal Z(\mac)$. 


We also expect that our state sum is  related  to the modular functor constructed from bimodule categories over finite tensor categories by Fuchs et al.~\cite{FSS} if one restricts the latter to our categorical data. However,  is not clear to us  how our construction is related to the work \cite{LY} by Lee and Yetter, which also constructs triangulation independent state sums with defect surfaces. However, the defect surfaces in \cite{LY} are labeled with different categorical data, namely  bicategories equipped with spherical duals and certain 2-functors. They  should be thought of as defects with additional structure, according to the authors. We believe that this is a different type of defect that cannot be related directly to our construction.

The examples in this section show that the  state sum models with defects give relevant information about defect surfaces and are easy to compute for simple categorical data. It would be feasible to investigate further examples that involve defect lines and points on non-trivial defect surfaces,  at least for spherical fusion categories $\mac=\mathrm{Vec}_G$ and $\mad=\mathrm{Vec}_{G'}$ and bimodule categories defined by finite transitive $G\times G'^{op}$-sets. In this case, the categorical defect data for defect lines and defect points  can be worked out explicitly to describe defects of all codimensions for Dijkgraaf-Witten theory \cite{DW}. It would also be interesting to investigate knotted defect surfaces beyond the torus and with less trivial categorical data.

With the results by Balsam and Kirillov \cite{BK,Kr}  on the relation between  Turaev-Viro-Barrett-Westbury state sums, Levin-Wen models \cite{LW} and Kitaev's quantum double models \cite{Kit}, it should also be possible to  apply our state sums with defects to those models and to make contact 
with the  work \cite{KK}  by Kitaev and Kong.
In the long run it would be desirable to determine if  our state sum model with defects defines a defect TQFT in the sense of  the works \cite{CMS,CRS2} by Carqueville et al.~and to relate it to the works \cite{CRS,domwall} by Carqueville et al.~and by Koppen et al.~on defects  and domain walls in the context of Reshetikhin-Turaev TQFTs. We leave these questions for future work.



\subsection{Acknowledgements} 
This article originated from discussions with John W.~Barrett. We had originally planned to work on this project together, but this became impossible due to the Covid-19 pandemic and its impact on  research and teaching. I am extremely grateful to him for helpful discussions, encouragement and comments on drafts of this article. 
I am also  grateful to Gregor Schaumann for  remarks and discussions on bimodule categories and bimodule traces,  to Andreas Knauf for discussions  and  comments on drafts of this article and to the referee for helpful comments and suggestions.
