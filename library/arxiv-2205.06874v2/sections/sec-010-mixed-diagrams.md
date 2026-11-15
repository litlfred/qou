---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-010-mixed-diagrams
section_title: "Mixed diagrams"
section_number: null
pages: 14-17
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.981
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
\label{subsec:bimod}



The diagrams for pivotal 2-categories in the previous section can be used to describe morphisms in the pivotal 2-categories
$\Bimod^\theta(\mac,\mad)$ and $\mathrm{Mod}^\theta(\mac)$ from Theorem \ref{th:pivot}.  In this case, regions are labeled with (bi)module categories with (bi)module traces, lines with (bi)module functors and vertices with (bi)module natural transformations. The duals are given by adjoint functors and the pivot is the natural isomorphism between a bimodule functor and its double adjoint. 

To describe the interaction of the data in $\Bimod^\theta(\mac,\mad)$ with data from $\mac$ and $\mad$, we generalise pivotal 2-category diagrams. We consider  diagrams with additional lines and vertices labeled with data from $\mac$ and $\mad$. These diagrams may involve  crossings of  lines labeled by $\mac$ and $\mad$ as well as  crossings of such lines with lines labeled by $(\mac,\mad)$-bimodule functors. 


\begin{definition} \label{def:mixeddiag}Let $\mac,\mad$ be spherical fusion categories. A {\bf mixed diagram} for $\Bimod^\theta(\mac,\mad)$ is a  diagram  obtained by superimposing a diagram $D$ for $\Bimod^\theta(\mac,\mad)$ with diagrams $D_\mac$ for $\mac$ and $D_\mad$ for $\mad^{rev}$. It is called {\bf generic} if
\begin{compactitem}
\item no vertex of any diagram is on a line or vertex of any of the others,
\item each point is on at most two lines from distinct diagrams,
\item  each point  in the interior that is on lines of two distinct diagrams is a transversal crossing.
\end{compactitem}
\end{definition}

While each diagram for $\Bimod^\theta(\mac,\mad)$ describes a 2-morphism in $\Bimod^\theta(\mac,\mad)$, a mixed diagram for $\Bimod^\theta(\mac,\mad)$ can be viewed as a 2-category diagram for Cat. 



For this recall from Remark \ref{rem:macmodule} that each $\mac$-module category $\mam$ defines a monoidal functor $F:\mac \to \End(\mam)$ that assigns to  $c\in \Ob\mac $  the   functor $c\rhd-:\mam\to \mam$ and to a morphism $\alpha: c\to c'$ the  natural transformation $\alpha\rhd-:c\rhd-\Rightarrow c'\rhd-$. Its monoidal structure  is given by the 
coherence isomorphisms  from Definition \ref{def:modulecat}. 

The monoidal functor $F:\mac\to \End(\mam)$  preserves duals.
The adjoint of  $c\rhd -:\mam\to\mam$ is  $c^*\rhd-:\mam\to \mam$  with the (co)units  of the adjunction given by the  (co)evaluations  from \eqref{eq:coevl} and \eqref{eq:coevr}, up to coherence data:
\begin{align*}
&\eta^{c\rhd -}=c_{c,c^*,-}\circ (\coev^L_c\rhd -)
& &\epsilon^{c\rhd -}=(\ev^L_c\rhd -)\circ c^\inv_{c^*,c,-}
\\
&\eta'^{c\rhd -}= c_{c^*,c,-} \circ (\coev^R_c\rhd -)
& &\epsilon'^{c\rhd-}=(\mathrm{ev}^R_{c}\rhd -)\circ c^\inv_{c,c^*,-}.
\end{align*}
The  pentagon relation \eqref{eq:pentagoncdef}   and triangle relation \eqref{eq:trianglec} allow one to suppress bracketings and action of the unit object in expressions involving multiple action functors. They lead to  strictification and coherence theorems for module categories that generalise the ones for monoidal categories, see  \cite[Rem.~7.2.4]{EGNO}. 



One can therefore interpret diagrams for $\mac$  as  2-category diagrams for Cat, whose regions are labeled by a $\mac$-module category $\mam$ and whose lines by action functors $c\rhd -$ for $c\in \Ob\mac$. Vertices are labeled by natural transformations that are composites of natural transformations  $\alpha\rhd -$ for morphisms $\alpha$ in $\mac$   with the coherence isomorphisms $c$ and $\gamma$.
The result is a natural transformation between the endofunctors given by the objects at the top and bottom of the diagrams. It is  unique up to coherence data.


Analogous statements hold for $\mad$-right module categories $\mam$. The only difference is that the action is a right action and one has an associated monoidal functor $F:\mad^{rev}\to \End(\mam)$, whose coherence data is given by the natural isomorphisms $d_{-,i,j}: (-\lhd i)\lhd j\Rightarrow -\lhd(i\oo j)$ and  $\delta: -\lhd  e \Rightarrow \id_\mam$  from Definition \ref{def:modulecat}.

In this way, one can  interpret any mixed diagram for $\Bimod^\theta(\mac,\mad)$ \emph{without crossings} as a 2-category diagram  for Cat in which the objects and morphisms from $\mac$ and $\mad$ are replaced by the associated action functors and natural transformations for the bimodule category labeling their region in the diagram. 

Crossings of  lines labeled by   $c\in \Ob \mac$ and $d\in \Ob \mad$ and crossings of such lines with lines labeled by (bi)module functors $F$ also have a direct interpretation. The former correspond to the natural isomorphisms $b_{c,-,d}$   from Definition \ref{def:modulecat} and the latter  to the natural isomorphisms $s^F$ and $t^F$ from Definition \ref{def:modulefunc}. We represent them as over- and undercrossings.


\begin{definition} Let $D'$ be a generic mixed diagram for $\Bimod^\theta(\mac,\mad)$ that superimposes  diagrams $D$, $D_\mac$ and  $D_\mad$. The 2-category diagram associated to $D'$  is the diagram obtained by 
\begin{itemize}
\item replacing  labels $c\in\Ob\mac$, $d\in \Ob\mad$ in a region labeled   $\mam$ with  $c\rhd-:\mam\to\mam$, $-\lhd d:\mam\to \mam$,

\item replacing morphism labels $\alpha$ and $\beta$ from $\mac$ and $\mad$ by  natural transformations  composed of   $\alpha\rhd -$ and $-\lhd\beta$ and the coherence isomorphisms $c,\gamma$ and $d,\delta$ from Definition \ref{def:modulecat},

\item transforming crossings of a line from 
 $D_\mac$ with a line from $D$ or  $D_\mad$  into overcrossings of the line from $D_\mac$ and crossings of a line from $D$ with a line from $D_\mad$ into overcrossings of the line from $D$, 
 
 \item labeling the crossing points  with natural transformations as follows:
\begin{compactitem}
\item crossings of  a line  labeled by $c\in \Ob\mac$ with  a line labeled by $d\in\Ob\mad$ by the natural isomorphism 
$b_{c,-,d}: (c\rhd -)\lhd d\Rightarrow c\rhd(-\lhd d)$ and its inverse  from Definition \ref{def:modulecat} 
\begin{align}\label{pic:bimodule}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2);
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3,baseline=(current bounding box.center)]
\draw[line width=.5pt, color=gray] (2,2) node[anchor=south]{$d$}--(-2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (-2,2) node[anchor=south]{$c$}--(2,-2);
\end{tikzpicture}
\\
&b_{c,-,d}: (c\rhd -)\lhd d\Rightarrow c\rhd(-\lhd d)
&
&b^\inv_{c,-,d}:  c\rhd(-\lhd d)\Rightarrow (c\rhd -)\lhd d,
 \nonumber
\end{align}

\item crossings of a line labeled by $c\in\Ob\mac$ with  a line from $D$ labeled $F$ by the natural isomorphism 
$s^F: F(c\rhd -)\Rightarrow c\rhd F(-)$ and its inverse from Definition \ref{def:modulefunc} 
\begin{align}\label{pic:modulefunc}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, style=dashed, color=black,] (-2,2) node[anchor=south]{$F$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt, color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2);
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=1pt, style=dashed, color=black,] (2,2) node[anchor=south]{$F$}--(-2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt, color=black,] (-2,2) node[anchor=south]{$c$}--(2,-2);
\end{tikzpicture}
\\
 &s^F_{c,-}: F(c\rhd -)\Rightarrow c\rhd F(-)
& &s^{F\,\inv}_{c,-}:  c\rhd F(-)\Rightarrow F(c\rhd -),\nonumber
\end{align}
\item crossings of a line  labeled by $d\in\Ob\mad$ with  a line from $D$ labeled $F$ by the natural isomorphism 
$t^F: F( -)\lhd d\Rightarrow F(-\lhd d)$ and its inverse from Definition \ref{def:modulefunc} 
\begin{align}\label{pic:modulefuncinv}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt, style=dashed, color=black,] (2,2) node[anchor=south]{$F$}--(-2,-2);
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\draw[line width=.5pt, color=gray,] (2,2) node[anchor=south]{$d$}--(-2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt, style=dashed, color=black,] (-2,2) node[anchor=south]{$F$}--(2,-2);
\end{tikzpicture}\\
 &t^F_{-,d}: F(-)\lhd d\Rightarrow F(-\lhd d) 
& &t^{F\;\inv}_{-,d}:  F(-\lhd d)\Rightarrow F(-)\lhd d.\nonumber
\end{align}
\end{compactitem}
\end{itemize}
\end{definition}
In this way, every generic mixed diagram defines a 
2-category diagram for Cat that represents a unique natural transformation between the composites of the functors at the  top and  bottom of the diagram. 

\begin{definition} The {\bf evaluation} of a generic mixed diagram for $\Bimod^\theta(\mac,\mad)$ is the natural transformation represented by the associated 2-category diagram.
\end{definition}

The properties of the coherence isomorphisms associated to crossing points allow one to define the evaluation of non-generic  mixed diagrams. 
The invertibility of the isomorphisms $b$, $s^F$ and $t^F$ translates into diagrammatic identities that are an analogue of the Reidemeister 2 move for a braid diagram
\begin{align}\label{pic:rm2}
&\begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(2,-2)--(-2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=.5pt, color=black] (2,2) node[anchor=south]{$c$}--(-2,-2)--(2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(-2,-6);
\draw[line width=.5pt, color=black] (2,2) node[anchor=south]{$c$}--(2,-6);
\end{scope}
\end{tikzpicture}\quad

\begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray] (2,2) node[anchor=south]{$d$}--(-2,-2)--(2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(2,-2)--(-2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray] (2,2) node[anchor=south]{$d$}--(2,-6);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(-2,-6);
\end{scope}
\end{tikzpicture}\quad

\begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=1pt, dashed] (-2,2) node[anchor=south]{$F$}--(2,-2)--(-2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=.5pt, color=black] (2,2) node[anchor=south]{$c$}--(-2,-2)--(2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=1pt, dashed] (-2,2) node[anchor=south]{$F$}--(-2,-6);
\draw[line width=.5pt, color=black] (2,2) node[anchor=south]{$c$}--(2,-6);
\end{scope}
\end{tikzpicture}\quad

\begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=1pt, dashed] (2,2) node[anchor=south]{$F$}--(-2,-2)--(2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(2,-2)--(-2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=1pt, dashed] (2,2) node[anchor=south]{$F$}--(2,-6);
\draw[line width=.5pt, color=black] (-2,2) node[anchor=south]{$c$}--(-2,-6);
\end{scope}
\end{tikzpicture}

\quad \begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(2,-2)--(-2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=1pt, dashed] (2,2) node[anchor=south]{$F$}--(-2,-2)--(2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(-2,-6);
\draw[line width=1pt, dashed] (2,2) node[anchor=south]{$F$}--(2,-6);
\end{scope}
\end{tikzpicture}
\quad

\begin{tikzpicture}[scale=.15]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray] (2,2) node[anchor=south]{$d$}--(-2,-2)--(2,-6);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[color=white, fill=white] (0,-4) circle (.5);
\draw[line width=1pt, dashed] (-2,2) node[anchor=south]{$F$}--(2,-2)--(-2,-6);
\end{scope}
\node at (0,-2){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray] (2,2) node[anchor=south]{$d$}--(2,-6);
\draw[line width=1pt, dashed] (-2,2) node[anchor=south]{$F$}--(-2,-6);
\end{scope}
\end{tikzpicture}
\end{align}
Similarly, the hexagon relation \eqref{eq:hexa} for a $(\mac,\mad)$-bimodule functor  translates into a diagrammatic identity that is an analogue of the Reidemeister 3 move for a braid diagram
 \begin{align}\label{pic:hexagon}
 &\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
 \begin{scope}[shift={(-4,0)}]
  \draw[line width=.5pt,  color=gray,] (0,2) node[anchor=south]{$d$}--(-2,-4);
    \draw[color=white, fill=white] (-1,0) circle (.7);
     \draw[line width=1pt, style=dashed, color=black] (-2,2) node[anchor=south]{$F$}--(2,-4);
         \draw[color=white, fill=white] (.9,-1.7) circle (.7);
    \draw[line width=.5pt,  color=black] (2,2) node[anchor=south]{$c$}--(0,-4);
    \end{scope}
    \node at (0,-1)[anchor=west]{$=$};
     \begin{scope}[shift={(6,0)}]
  \draw[line width=.5pt,  color=gray,] (0,2) node[anchor=south]{$d$}--(2,-1);
      \draw[line width=.5pt,  color=gray] (2,-1) --(-2,-4);
         \draw[color=white, fill=white] (1,1) circle (.5);
         \draw[color=white, fill=white] (-1,-3) circle (.5);
              \draw[color=white, fill=white] (.5,-2) circle (.7);
   \draw[line width=1pt, style=dashed, color=black] (-2,2) node[anchor=south]{$F$}--(2,-4);
     \draw[color=white, fill=white] (-1,0) circle (.7);
    \draw[line width=.5pt,  color=black,] (2,2) node[anchor=south]{$c$}--(-2,-1);
        \draw[line width=.5pt,  color=black] (-2,-1) --(0,-4);
    \end{scope}
 \end{tikzpicture}
\end{align}

The naturality conditions from Definitions \ref{def:modulecat} and \ref{def:modulefunc} and the conditions on a bimodule natural transformation from  \eqref{eq:cnat} and \eqref{eq:dnat} 
 allow one to slide vertices under or over crossings. 
The naturality of the isomorphisms $b_{c,d,m}: (c\rhd m)\lhd d\to c\rhd (m\lhd d)$ in $c$ and $d$ is expressed as
\begin{align}\label{pic:natb}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) node[anchor=north]{$c'$};
\draw[fill=black] (1,1) circle (.15) node[anchor=west]{$\;\alpha$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) node[anchor=north]{$c'$};
\draw[fill=black] (-1,-1) circle (.15) node[anchor=east]{$\alpha\;$};
\end{scope}
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2) node[anchor=north]{$d'$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) ;
\draw[fill=gray, color=gray] (-1,1) circle (.15) node[anchor=east]{$\beta\;$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2) node[anchor=north]{$d'$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) ;
\draw[fill=gray, color=gray] (1,-1) circle (.15) node[anchor=west]{$\;\beta$};
\end{scope}
\end{tikzpicture}
\end{align}
The naturality of  $s^F_{c,m}: F(c\rhd m)\to c\rhd F(m)$ and  $t^F_{m,d}: F(m)\lhd d\to  F(m\lhd d)$ in $c$ and $d$ implies
\begin{align}\label{pic:natfuncconst}
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=1pt, style=dashed] (-2,2) node[anchor=south]{$F$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) node[anchor=north]{$c'$};
\draw[fill=black] (1,1) circle (.15) node[anchor=west]{$\;\alpha$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=1pt, style=dashed] (-2,2) node[anchor=south]{$F$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,color=black,] (2,2) node[anchor=south]{$c$}--(-2,-2) node[anchor=north]{$c'$};
\draw[fill=black] (-1,-1) circle (.15) node[anchor=east]{$\alpha\;$};
\end{scope}
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2) node[anchor=north]{$d'$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt,style=dashed] (2,2) node[anchor=south]{$F$}--(-2,-2) ;
\draw[fill=gray, color=gray] (-1,1) circle (.15) node[anchor=east]{$\beta\;$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray,] (-2,2) node[anchor=south]{$d$}--(2,-2) node[anchor=north]{$d'$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt,style=dashed] (2,2) node[anchor=south]{$F$}--(-2,-2) ;
\draw[fill=gray, color=gray] (1,-1) circle (.15) node[anchor=west]{$\;\beta$};
\end{scope}
\end{tikzpicture}
\end{align}
The defining conditions \eqref{eq:cnat} and \eqref{eq:dnat} on a $\mac$-module and $\mad$-right module natural transformation $\nu: F\Rightarrow G$ 
give the diagrammatic identities
 \begin{align}\label{pic:bimodulenat}
 &\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=1pt, style=dashed] (-2,2) node[anchor=south]{$F$}--(2,-2) node[anchor=north]{$G$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt,] (2,2) node[anchor=south]{$c$}--(-2,-2) ;
\draw[fill=black, color=black] (-1,1) circle (.2) node[anchor=east]{$\nu\;$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=1pt, style=dashed] (-2,2) node[anchor=south]{$F$}--(2,-2) node[anchor=north]{$G$};
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=.5pt] (2,2) node[anchor=south]{$c$}--(-2,-2) ;
\draw[fill=black, color=black] (1,-1) circle (.2) node[anchor=west]{$\;\nu$};
\end{scope}
\end{tikzpicture}
&
&\begin{tikzpicture}[scale=.3, baseline=(current bounding box.center)]
\begin{scope}[shift={(-4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt, style=dashed] (2,2) node[anchor=south]{$F$}--(-2,-2) node[anchor=north]{$G$};
\draw[fill=black] (1,1) circle (.2) node[anchor=west]{$\;\nu$};
\end{scope}
\node at (0,0){$=$};
\begin{scope}[shift={(4,0)}]
\draw[line width=.5pt, color=gray] (-2,2) node[anchor=south]{$d$}--(2,-2);
\draw[color=white, fill=white] (0,0) circle (.5);
\draw[line width=1pt, style=dashed] (2,2) node[anchor=south]{$F$}--(-2,-2) node[anchor=north]{$G$};
\draw[fill=black] (-1,-1) circle (.2) node[anchor=east]{$\nu\;$};
\end{scope}
\end{tikzpicture}
 \end{align}
In particular, identities \eqref{pic:natb} and \eqref{pic:natfuncconst} can be applied to the (co)evaluations for the duals in $\mac$ and $\mad$. This  allows one to slide maxima and minima of lines labeled with objects in $\mac$ and $\mad$ over or under lines labeled with bimodule functors. Similarly,  the (co)evaluations for  1-morphisms in $\Bimod^\theta(\mac,\mad)$ are
 $(\mac,\mad)$-bimodule natural transformations and hence satisfy identity \eqref{pic:bimodulenat}. This allows one to slide maxima and minima of lines labeled with bimodule functors over or under lines labeled with objects  from $\mac$ or $\mad$. 
 
Note  that the diagrammatic identities involving only lines  and vertices labeled by $\mac$ and $\mad$ are special cases of the ones involving data from $\Bimod^\theta(\mac,\mad)$. 
The diagrams \eqref{pic:bimodule} for the natural isomorphism $b_{c,-,d}: (c\rhd -)\lhd d\Rightarrow c\rhd(-\lhd d)$ are just the diagrams \eqref{pic:modulefunc} and \eqref{pic:modulefuncinv} for the $\mac$-module functor $-\lhd d:\mam\to\mam$ and the $\mad$-right module functor $c\rhd -:\mam\to\mam$. The identities \eqref{pic:natb}
are a special case of \eqref{pic:natfuncconst} and  \eqref{pic:bimodulenat}. 

The diagrammatic identities \eqref{pic:rm2} to \eqref{pic:bimodulenat} allow one to define the evaluation of non-generic  mixed diagrams.  
Any point of a mixed diagram that lies on more than two lines from distinct diagrams is on three lines, one from each diagram $D, D_\mac$ and $D_\mad$. By slightly displacing the lines  one can  transform such a triple point into multiple crossings of two lines. The diagrammatic identities for the crossings and their inverses and the identity \eqref{pic:hexagon} ensures that all diagrams obtained in this way have the same evaluation. 

Similarly, if there is a point on two lines from different diagrams that is not a transversal crossing, then by slightly displacing the lines one can either create a double crossing or ensure that the lines do not meet. Identities \eqref{pic:rm2}  ensure that all resulting diagrams have the same evaluations. 
Any  vertex  on  two lines from different diagrams can be displaced slightly from the crossing. 
Identities \eqref{pic:natb}, \eqref{pic:natfuncconst} and \eqref{pic:bimodulenat} ensure that all ways of doing so yield  diagrams with the same evaluation. 




\begin{definition} The evaluation of a  mixed diagram for $\Bimod^\theta(\mac,\mad)$ is defined as the evaluation of any generic  mixed diagram obtained by slightly displacing the lines and vertices of the diagram.
\end{definition}
