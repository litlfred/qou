---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-016-projections-and-inclusions-for-simple-objects
section_title: "Projections and inclusions for simple objects"
section_number: null
pages: 24-26
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.858
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
Let $\mam$ a finite semisimple  $\C$-linear category, equipped with a trace $\theta$ in the sense of Definition \ref{def:moduletrace} and let $I$ be a set of representatives of the isomorphism classes of its simple objects. 
Then  every object $x$ in $\mam$ can be expressed as a direct sum $x\cong \oplus_{m\in I} m^{\oplus n_{xm}}$ with multiplicities $n_{xm}=\dim_\C \Hom_\mam(m,x)\in\mathbb N_0$. 
One can choose bases
 $\{p^\alpha_{xm}\}$ of $\Hom_\mathcal M(x,m)$ and  $\{j^\alpha_{xm}\}$ of $\Hom_\mam(m,x)$ with $m\in I$ and $\alpha\in\{1,..., n_{xm}\}$
such that 
\begin{align}\label{eq:projincl}
p^\beta_{xm'} \circ j^\alpha_{xm}=\frac{\delta_{\alpha\beta} \delta_{mm'}}{\dim(m)}1_m \qquad\qquad 1_x=\sum_{m\in I}\sum_{\alpha=1}^{n_{xm}} \dim(m) \;\; j^\alpha_{xm}\circ p^\alpha_{xm}
\end{align}
for all $m,m'\in I$, where $\dim(m)=\theta_m(1_m)$. 
Their normalisation is fixed by \eqref{eq:projincl}  such that  
\begin{align}
\theta_m(p^\beta_{xm}\circ j^\alpha_{xm})=\delta_{\alpha\beta},
\end{align}
and this implies with the cyclicity of the trace 
\begin{align}\label{eq:dimformula}
\sum_{m\in I} \dim(m) \dim_{\C}\Hom_\mam(m,x)=\dim (x).
\end{align}
The identities \eqref{eq:projincl}  imply for all morphisms $\phi: m\to x$ and $\psi:x\to m$
\begin{align}\label{eq:traceidnd}
\phi=\sum_{\alpha=1}^{n_{xm}} \theta_m(p^\alpha_{xm}\circ \phi)\; j^\alpha_{xm}\qquad  \psi=\sum_{\alpha=1}^{n_{ym}} \theta_m(\psi\circ j^\alpha_{xm})\; p^\alpha_{xm}
\end{align}
and for all morphisms $\chi: x\to y$
 \begin{align}\label{eq:traceidnd2}
\chi=\sum_{m\in I}\sum_{\alpha=1}^{n_{xm}}\sum_{\beta=1}^{n_{ym}} \dim(m)\,\theta_m(p^\beta_{ym}\circ \chi\circ j^\alpha_{xm})\;  j^\beta_{ym} \circ p^\alpha_{xm}.
\end{align}
These identities are represented  by the diagrams
\begin{align}\label{pic:traceidnd}
&\begin{tikzpicture}[scale=.3]
\node at (-3,0) [anchor=west] {$\sum_\alpha$}; 
\draw[line width=1.5pt,color=blue] (0,4)--(0,-4) node[midway, anchor=west]{$x$};
\draw[line width=1.5pt,color=blue] (-.5,4)--(.5,4) node[anchor=west]{$m$};
\draw[line width=1.5pt,color=blue] (-.5,-4)--(.5,-4)node[anchor=west]{$m$}; 
\draw[color=blue, fill=blue] (0,2) circle (.2) node[anchor=west]{$\phi$};
\draw[color=blue, fill=blue] (0,-2) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=blue, line width=1.5pt] (3,4) node[anchor=west]{$m$}--(3,-4) node[anchor=west]{$x$};
\draw[color=blue, fill=blue] (3,0) circle (.2) node[anchor=west]{$\alpha$};
\node at (6,0){$\stackrel{\eqref{eq:traceidnd}}=$};
\draw[color=blue, line width=1.5pt] (8,4) node[anchor=west]{$m$}--(8,-4) node[anchor=west]{$x$};
\draw[color=blue, fill=blue] (8,0) circle (.2) node[anchor=west]{$\phi$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\node at (-3,0) [anchor=west] {$\sum_\alpha$}; 
\draw[line width=1.5pt,color=blue] (0,4)--(0,-4) node[midway, anchor=west]{$x$};
\draw[line width=1.5pt,color=blue] (-.5,4)--(.5,4) node[anchor=west]{$m$};
\draw[line width=1.5pt,color=blue] (-.5,-4)--(.5,-4)node[anchor=west]{$m$}; 
\draw[color=blue, fill=blue] (0,2) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=blue, fill=blue] (0,-2) circle (.2) node[anchor=west]{$\psi$};
\draw[color=blue, line width=1.5pt] (3,4) node[anchor=west]{$x$}--(3,-4) node[anchor=west]{$m$};
\draw[color=blue, fill=blue] (3,0) circle (.2) node[anchor=west]{$\alpha$};
\node at (6,0){$\stackrel{\eqref{eq:traceidnd}}=$};
\draw[color=blue, line width=1.5pt] (8,4) node[anchor=west]{$x$}--(8,-4) node[anchor=west]{$m$};
\draw[color=blue, fill=blue] (8,0) circle (.2) node[anchor=west]{$\psi$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\node at (-11,0) [anchor=west] {$\sum_m\sum_{\alpha,\beta}\dim(m)$}; 
\draw[line width=1.5pt,color=blue] (0,4)--(0,-4);
\node at (0, 1.5)[anchor=west, color=blue]{$x$};
\node at (0, -1.5)[anchor=west, color=blue]{$y$};
\draw[line width=1.5pt,color=blue] (-.5,4)--(.5,4) node[anchor=west]{$m$};
\draw[line width=1.5pt,color=blue] (-.5,-4)--(.5,-4)node[anchor=west]{$m$}; 
\draw[color=blue, fill=blue] (0,3) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=blue, fill=blue] (0,0) circle (.2) node[anchor=west]{$\chi$};
\draw[color=blue, fill=blue] (0,-3) circle (.2) node[anchor=west]{$\beta$};
\draw[color=blue, line width=1.5pt] (3,4) node[anchor=west]{$x$}--(3,-4) node[anchor=west]{$y$} node[midway, anchor=west]{$m$};
\draw[color=blue, fill=blue] (3,2) circle (.2) node[anchor=west]{$\alpha$};
\draw[color=blue, fill=blue] (3,-2) circle (.2) node[anchor=west]{$\beta$};
\node at (6,0){$\stackrel{\eqref{eq:traceidnd2}}=$};
\draw[color=blue, line width=1.5pt] (8,4) node[anchor=west]{$x$}--(8,-4) node[anchor=west]{$y$};
\draw[color=blue, fill=blue] (8,0) circle (.2) node[anchor=west]{$\chi$};
\end{tikzpicture}
\end{align}


If $\mam$ and $\man$ are bimodule categories with bimodule traces over spherical  fusion categories $\mac$ and $\mad$ and $F:\mam\to\man$ is a $\C$-linear functor, then one can characterise $F$ by decomposing the images of simple objects $m\in I_\mam$ into simple objects $n\in I_\man$. We write $p^\alpha_{Fmn}=p^\alpha_{F(m)n}: F(m)\to n$
and $j^\alpha_{Fmn}=j^\alpha_{F(m)n}: n\to F(m)$ for the associated projection and inclusion morphisms satisfying \eqref{eq:projincl} and denote them by
\begin{align}\label{pic:projincl}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1.5pt, color=blue] (0,2) node[anchor=south]{$m$}--(0,0);
\draw[line width=1.5pt, color=violet] (0,0)-- (0,-2) node[anchor=north]{$n$};
\draw[line width=1pt, style=dashed] (-2,2) node[anchor=south]{$F$}--(0,0);
\draw[color=violet, fill=violet] (0,0) circle(.2) node[anchor=west]{$\;\alpha$};
\end{tikzpicture}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1.5pt, color=blue] (0,-2) node[anchor=north]{$m$}--(0,0);
\draw[line width=1.5pt, color=violet] (0,0)-- (0,2) node[anchor=south]{$n$};
\draw[line width=1pt, style=dashed] (-2,-2) node[anchor=north]{$F$}--(0,0);
\draw[color=violet, fill=violet] (0,0) circle(.2) node[anchor=west]{$\;\alpha$};
\end{tikzpicture}
\end{align}
such that the  identities \eqref{eq:projincl} are given by
\begin{align}\label{pic:semisimpleids}
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-3,0)}]
\draw[line width=1.5pt, color=violet] (0,3) node[anchor=south]{$n$}--(0,2);
\draw[line width=1pt, style=dashed] (0,2)..controls (-2,0).. (0,-2) node[midway,anchor=east]{$F$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[midway,anchor=west]{$m$};
\draw[line width=1.5pt, color=violet] (0,-3) node[anchor=north]{$n'$}--(0,-2);
\draw[fill=violet, color=violet] (0,2) circle (.2) node[anchor=west]{$\;\alpha$};
\draw[fill=violet, color=violet] (0,-2) circle (.2) node[anchor=west]{$\;\beta$};
\end{scope}
\node at (0,0) [anchor=west] {$=\frac{\delta_{\alpha\beta}\delta_{nn'}}{\dim(n)}$};
\draw[line width=1.5pt, color=violet] (6,3) node[anchor=south]{$n$}--(6,-3);
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\begin{scope}[shift={(-3,0)}]
\node at (-9,0)[anchor=west] {$\sum_{n,\alpha}\dim(n)$};
\draw[line width=1pt, style=dashed] (-2,3) node[anchor=south]{$F$}--(0,1);
\draw[line width=1pt, style=dashed] (-2,-3) node[anchor=north]{$F$}--(0,-1);
\draw[line width=1.5pt, color=blue] (0,3) node[anchor=south]{$m$}--(0,1);
\draw[line width=1.5pt, color=blue] (0,-3) node[anchor=north]{$m$}--(0,-1);
\draw[line width=1.5pt, color=violet] (0,1) --(0,-1) node[midway,anchor=west]{$n$};
\draw[fill=violet, color=violet] (0,1) circle (.2) node[anchor=south west]{$\;\alpha$};
\draw[fill=violet, color=violet] (0,-1) circle (.2) node[anchor=north west]{$\;\alpha$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=1pt, style=dashed] (-2,3) node[anchor=south]{$F$}--(-2,-3);
\draw[line width=1.5pt, color=blue] (0,3) node[anchor=south]{$m$}--(0,-3);
\end{scope}
\end{tikzpicture}
\end{align}
For functors that are 1-morphisms in the pivotal 2-categories $\Bimod^\theta(\mac,\mad)$ and $\mathrm{Mod}^\theta(\mac)$ from Theorem \ref{th:pivot} and hence have left and right adjoints, the morphisms $p^\alpha_{Fmn}$ and $j^\alpha_{Fmn}$ from \eqref{pic:projincl} can also be modified by composing them with the units and counits of the adjunctions. 
By composing them with the component morphisms of  $\eta'^{F}:\id_\mam\Rightarrow F^lF$ and $\epsilon^F:F^lF \Rightarrow \id_\man$,  introduced before Corollary \ref{cor:functortrace},  one obtains 
\begin{align}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1.5pt, color=violet] (0,0)--(0,3) node[anchor=south]{$n$}; 
\draw[line width=1.5pt, color=blue] (0,0)--(0,-3) node[anchor=north]{$m$}; 
\draw[line width=1pt, dashed] (0,0).. controls (0,-2) and (-2,-2)..(-2,0); 
\draw[line width=1pt, dashed] (-2,0)--(-2,3) node[sloped, pos=.5, allow upside down]{\arrowIn} node[pos=.5,anchor=east]{$F$}; 
\draw[color=violet, fill=violet] (0,0) circle (.2) node[anchor=west]{$\alpha$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\draw[line width=1.5pt, color=blue] (0,0)--(0,3) node[anchor=south]{$m$}; 
\draw[line width=1.5pt, color=violet] (0,0)--(0,-3) node[anchor=north]{$n$}; 
\draw[line width=1pt, dashed] (0,0).. controls (0,2) and (-2,2)..(-2,0); 
\draw[line width=1pt, dashed] (-2,-3)--(-2,0) node[sloped, pos=.5, allow upside down]{\arrowIn} node[pos=.5,anchor=east]{$F$}; 
\draw[color=violet, fill=violet] (0,0) circle (.2) node[anchor=west]{$\alpha$};
\end{tikzpicture}\\
&
\pi^\alpha_{F^lnm}: F^l(n)\to m
&
&\iota^\alpha_{F^lnm}: m\to F^l(n)\nonumber
\end{align}
These morphisms satisfy identities analogous to \eqref{pic:semisimpleids}. For all $m,m'\in I_\mam$ and $n\in I_\man$  one has
\begin{align}\label{eq:genorthcheck}
&\begin{tikzpicture}[scale=.3]
\draw[line width=1.5pt, color=blue] (0,1)--(0,4) node[anchor=south]{$m$};
\draw[line width=1.5pt, color=blue] (0,-1)--(0,-4) node[anchor=north]{$m'$};
\draw[line width=1.5pt, color=violet] (0,1)--(0,-1) node[pos=.5, anchor=west]{$n$};
\draw[line width=1pt, dashed] (0,1).. controls (0,3) and (-2,3).. (-2,1);
\draw[line width=1pt, dashed] (-2,-1)--(-2,1) node[sloped, pos=.5, allow upside down]{\arrowIn} node[pos=.5, anchor=east]{$F$};
\draw[line width=1pt, dashed] (0,-1).. controls (0,-3) and (-2,-3).. (-2,-1) ;
\draw[color=violet, fill=violet] (0,1) circle (.2) node[anchor=south west]{$\,\alpha$};
\draw[color=violet, fill=violet] (0,-1) circle (.2) node[anchor=north west]{$\,\beta$};
\node at (2,0)[anchor=west]{$=\frac{\delta_{\alpha\beta}\delta_{mm'}}{\dim(m)}$};
\draw[line width=1.5pt, color=blue] (9,-4)--(9,4) node[anchor=south]{$m$};
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3]
\node at (-2,0)[anchor=east]{$\sum_{m,\alpha}\dim(m)$};
\draw[line width=1.5pt, color=violet] (0,2)--(0,4) node[anchor=south]{$n$};
\draw[line width=1.5pt, color=violet] (0,-2)--(0,-4) node[anchor=north]{$n$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[pos=.5, anchor=west]{$m$};
\draw[line width=1pt, dashed] (0,2).. controls (0,0) and (-2,0).. (-2,2);
\draw[line width=1pt, dashed] (-2,2)--(-2,4) node[sloped, pos=.5, allow upside down]{\arrowIn} node[anchor=south]{$F$};
\draw[line width=1pt, dashed] (0,-2).. controls (0,0) and (-2,0).. (-2,-2) ;
\draw[line width=1pt, dashed] (-2,-4)node[anchor=north]{$F$} --(-2,-2) node[sloped, pos=.5, allow upside down]{\arrowIn} ;
\draw[color=violet, fill=violet] (0,2) circle (.2) node[anchor=west]{$\,\alpha$};
\draw[color=violet, fill=violet] (0,-2) circle (.2) node[anchor=west]{$\,\alpha$};
\node at (3,0){$=$};
\draw[line width=1pt, dashed] (5,-4)--(5,4) node[sloped, pos=.5, allow upside down]{\arrowIn} node[anchor=south]{$F$};
\draw[line width=1.5pt, color=violet] (7,-4)--(7,4) node[anchor=south]{$n$};
\end{tikzpicture}
\end{align}
The first identity  follows directly from the fact that $m,m'\in I_\mam$ are simple, by taking the trace and then using its cyclicity, the second identity in \eqref{eq:functortrpivot} and the first identity in \eqref{eq:projincl} and \eqref{pic:semisimpleids}. For the second identity note that  the morphisms $\pi^\alpha_{F^lnm}$ and $\iota^\alpha_{F^lnm}$ can be expressed as linear combinations
\begin{align}\label{eq:lincombi}
\pi^{\alpha}_{F^lnm}=\sum_{\beta} M^{\alpha\beta} p^\beta_{F^lmn}\qquad \iota^{\alpha}_{F^lnm}=\sum_{\beta} N^{\alpha\beta} j^\beta_{F^lmn}
\end{align}
with invertible complex matrices $M=(M^{\alpha\beta})$ and $N=(N^{\alpha\beta})$.
 The first identity in \eqref{eq:genorthcheck} implies $M^T=N^\inv$.  Inserting \eqref{eq:lincombi} into the left-hand side of the second equation in \eqref{eq:genorthcheck}, together with the identity $M^T=N^\inv$ and the second identity in \eqref{eq:projincl} and \eqref{pic:semisimpleids} then yields the second identity in \eqref{eq:genorthcheck}.
This implies for all $n\in I_\man$
\begin{align}\label{eq:traceout}
\begin{tikzpicture}[scale=.3]
\node at (-6,0)[anchor=east]{$\sum_{m,\alpha}\dim(m)$};
\draw[line width=1.5pt, color=violet] (0,2)--(0,4) node[anchor=south]{$n$};
\draw[line width=1.5pt, color=violet] (0,-2)--(0,-4) node[anchor=north]{$n$};
\draw[line width=1.5pt, color=blue] (0,2)--(0,-2) node[pos=.5, anchor=west]{$m$};
\draw[line width=1pt, dashed] (0,2)--(-4,0) node[pos=.5, anchor=south]{$F$};
\draw[line width=1pt, dashed] (0,-2)--(-4,0) node[pos=.5, anchor=north]{$F$};
\draw[line width=1pt, dashed] (-4,4)node[anchor=south]{$G$} --(-4,-4) node[anchor=north]{$H$};
\draw[fill=black] (-4,0) circle (.2) node[anchor=east]{$\nu$};
\draw[fill=violet, color=violet] (0,2) circle (.2) node[anchor=west]{$\,\alpha$};
\draw[fill=violet, color=violet] (0,-2) circle (.2) node[anchor=west]{$\,\alpha$};
\node at (2,0)[anchor=west]{$=$};

\begin{scope}[shift={(18,0)}]
\node at (-6,0)[anchor=east]{$\sum_{m,\alpha}\dim(m)$};
\draw[line width=1.5pt, color=violet] (0,2)--(0,4) node[anchor=south]{$n$};
\draw[line width=1.5pt, color=violet] (0,-2)--(0,-4) node[anchor=north]{$n$};
\draw[line width=1.5pt, color=blue] (0,-2)--(0,2) node[midway, anchor=west]{$m$};
\draw[line width=1pt, dashed] (-4,4)node[anchor=south]{$G$} --(-4,-4) node[anchor=north]{$H$};
\draw[line width=1pt, dashed] (0,2).. controls (-1,-2) and (-3,4)..(-4,0) node[sloped, pos=.5, allow upside down]{\arrowIn} node[pos=.5,anchor=south]{$F$};
\draw[line width=1pt, dashed] (0,-2).. controls (-1,2) and (-3,-4)..(-4,0) node[sloped, pos=.5, allow upside down]{\arrowIn} node[pos=.5,anchor=north]{$F$};
\draw[fill=black] (-4,0) circle (.2) node[anchor=east]{$\nu$};
\draw[fill=violet, color=violet] (0,2) circle (.2) node[anchor=west]{$\,\alpha$};
\draw[fill=violet, color=violet] (0,-2) circle (.2) node[anchor=west]{$\,\alpha$};
\end{scope}
\node at (22,0){$\stackrel{\eqref{eq:genorthcheck}}=$};

\begin{scope}[shift={(30,0)}]
\draw[line width=1.5pt, color=violet] (0,-4)--(0,4) node[anchor=south]{$n$};
\draw[line width=1pt, dashed] (-4,4)node[anchor=south]{$G$} --(-4,-4) node[anchor=north]{$H$};
\draw[line width=1pt, dashed] (-4,0).. controls (-4,2) and (-2,2)..(-2,0);
\draw[line width=1pt, dashed, -stealth] (-4,0).. controls (-4,-2) and (-2,-2)..(-2,0) node[anchor=west]{$F$};
\draw[fill=black] (-4,0) circle (.2) node[anchor=east]{$\nu$};
\end{scope}
\end{tikzpicture}
\end{align}


In particular, identities \eqref{pic:semisimpleids}, \eqref{eq:genorthcheck} and \eqref{eq:traceout} hold for endofunctors  
 $F=c\rhd -: \mam\to \mam$ or $F=-\lhd d:\mam\to\mam$ for a $(\mac,\mad)$-bimodule category $\mam$. In this case, we use thin black or grey lines labeled $c$ or $d$ instead of dashed lines,  and the upward arrows denote the duals in $\mac$ and $\mad$.  Identities \eqref{pic:semisimpleids}, together with \eqref{eq:catdimension},  \eqref{eq:dimensionsmodule} and  \eqref{eq:dimformula},  then imply for all simple objects $n\in I_\mam$
\begin{align}\label{eq:2gonformula}
\begin{tikzpicture}[scale=.25]
\begin{scope}[shift={(-3,0)}]
\node at (-10,0) {$\sum_{i,m, \alpha}\dim(i)\dim(m)$};
\draw[line width=1.5pt, color=blue] (0,4) node[anchor=south]{$n$}--(0,-4) node[anchor=north]{$n$} node[midway, anchor=west]{$m$};
\draw[line width=.5pt, color=black] (0,2).. controls (-2,0)..(0,-2) node[midway, anchor=east]{$i$};
\draw[color=blue, fill=blue] (0,2) circle (.2) node[anchor=west]{$\alpha$}; 
\draw[color=blue, fill=blue] (0,-2) circle (.2) node[anchor=west]{$\alpha$}; 
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(7,0)}]
\node at (-3,0) {$\dim(\mac)$};
\draw[line width=1.5pt, color=blue] (0,4) node[anchor=south]{$n$}--(0,-4) node[anchor=north]{$n$}; 
\end{scope}
\end{tikzpicture}
\end{align}
