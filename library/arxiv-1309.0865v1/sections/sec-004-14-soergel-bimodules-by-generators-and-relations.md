---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-004-14-soergel-bimodules-by-generators-and-relations
section_title: "Soergel bimodules by generators and relations"
section_number: 1.4
pages: 4-6
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.964
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
A \emph{Bott-Samelson bimodule} is a bimodule of the form $B_{\un{w}} \define B_s \ot_R B_t \ot_R \cdots \ot_R B_u$ for an expression $\un{w}=st\dots u$. They form a full
monoidal subcategory of $R-\Bim$, which we denote $\BSBim$. By definition, any Soergel bimodule is a direct sum of shifts of summands of bimodules in $\BSBim$. Said another way, the
category of Soergel bimodules $\SBim$ is the Karoubi envelope of (the additive, graded envelope of) $\BSBim$. The upshot is that in order to describe the category of Soergel bimodules it
is enough to describe the monoidal category of Bott-Samelson bimodules. This is an easier problem because (in contrast to Soergel bimodules) one has concrete combinatorial realizations of
the objects in $\BSBim$.

In this paper we describe the monoidal category of Bott-Samelson bimodules by
generators and relations. (There is one caveat, involving standard parabolic subgroups of type $H_3$ which shall be discussed in section \ref{threecolorintro} below.) Such a description has already been given by Libedinsky
\cite{LibRA} in the right-angled case (i.e. when $m_{st} \in \{2,\infty\}$), in type $A$ by the first author and Khovanov \cite{EKh}, and in dihedral type by the first author in
\cite{EDihedral}. This is the next step in the algebraization of $\HC$, freeing the category of Soergel bimodules from its realization as a full subcategory of a bimodule category. Said
another way, in this paper we give a $2$-presentation of $\BSBim$, in analogy to the $1$-presentation of $\HB$ given by Iwahori. Our presentation will use the technology of planar
diagrammatics.

We assign a color to each element of $S$, which allows us to encode a Bott-Samelson bimodule as a sequence $\un{w}$ of colored dots ordered on
a line. A morphism between Bott-Samelson bimodules will be given by a linear combination of isotopy classes of decorated graphs embedded in the planar strip $\RM \times [0,1]$. The edges
in these graphs will be colored, and may run into the bottom boundary $\R \times \{0\}$ or the top boundary $\R \times \{1\}$, yielding a sequence of colored dots on each boundary. A
morphism from $B_{\un{w}}$ to $B_{\un{y}}$ will have bottom boundary $\un{w}$ and top boundary $\un{y}$. For example, the following planar diagram
\igc{1}{morphismexample}
represents a map from $rgrgrgbr$ to $grbgrbr$.

For the moment, let us ignore the notion of isotopy classes of graphs, and consider instead diagrams which can be constructed from horizontal and vertical concatenation of the following generators. Here is a list of generating morphisms, their degrees and the maps of Soergel bimodules which they represent:
\[
\begin{array}{cccc}
\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (3,0) circle (1cm);
\draw[color=blue] (3,-1) to (3,0);
\node[circle,fill,draw,inner sep=0mm,minimum size=1mm,color=blue] at (3,0) {};}\end{array}& \text{deg 1} & B_{\color{blue}s} \to R  & f \otimes g \mapsto fg 
\\
\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (3,0) circle (1cm);
\draw[color=blue] (3,1) to (3,0);
\node[circle,fill,draw,inner sep=0mm,minimum size=1mm,color=blue] at (3,0) {};}\end{array}
& \text{deg 1}&
R \to B_{\color{blue}s}  & 1 \mapsto \frac{1}{2}(\alpha_s \otimes 1 + 1
  \otimes \alpha_s)
\\
\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (0,0) circle (1cm);
\draw[color=blue] (-30:1cm) -- (0,0) -- (90:1cm);
\draw[color=blue] (-150:1cm) -- (0,0);}\end{array}
&  \text{deg -1} & 
B_{\color{blue}s} B_{\color{blue}s} \to B_{\color{blue}s}  & 1 \otimes g \otimes 1 \mapsto \partial_s g
  \otimes 1
\\

\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (0,0) circle (1cm);
\draw[color=blue] (30:1cm) -- (0,0) -- (-90:1cm);
\draw[color=blue] (150:1cm) -- (0,0);}\end{array}
&  \text{deg -1} & B_{\color{blue}s} \to B_{\color{blue}s} B_{\color{blue}s}  & 1 \otimes 1 \mapsto 1 \otimes 1
  \otimes 1 \\
\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (0,0) circle (1cm);
\node at (0,0) {$f$};}\end{array}
&  \text{deg f} &
R \to R  & 1 \mapsto f
\\
\begin{array}{c}\tikz[scale=0.5]{\draw[dashed] (0,0) circle (1cm);
\draw[color=blue] (0,0) -- (22.5:1cm);
\draw[color=blue] (0,0) -- (67.5:1cm);
\draw[color=blue] (0,0) -- (112.5:1cm);
\draw[color=blue] (0,0) -- (157.5:1cm);
\draw[color=blue] (0,0) -- (-22.5:1cm);
\draw[color=blue] (0,0) -- (-67.5:1cm);
\draw[color=blue] (0,0) -- (-112.5:1cm);
\draw[color=blue] (0,0) -- (-157.5:1cm);
\draw[color=red] (0,0) -- (0:1cm);
\draw[color=red] (0,0) -- (45:1cm);
\draw[color=red] (0,0) -- (90:1cm);
\draw[color=red] (0,0) -- (135:1cm);
\draw[color=red] (0,0) -- (180:1cm);
\draw[color=red] (0,0) -- (-45:1cm);
\draw[color=red] (0,0) -- (-90:1cm);
\draw[color=red] (0,0) -- (-135:1cm);
}\end{array}
&  \text{deg 0}&  \ubr{B_{\color{blue}s}B_{\color{red}t} \dots }{m_{st}}  \to \ubr{B_{\color{red}t} B_{\color{blue}s} \dots }{m_{st}}    & 
\end{array}
\]
In the above, $\alpha_s$ denotes a fixed choice of equation for the hyperplane fixed by $s$, and $\pa_s$ denotes the Demazure operator $\pa_s(f) \define (f - sf)/\a_s$. We refer to the first two morphisms as \emph{dots}, the second two morphisms as \emph{trivalent vertices}, and the final morphism as the \emph{$2m_{st}$-valent vertex}.

We have not given a formula for the $2m_{st}$-valent vertex, as it is both difficult and unenlightening to write down explicitly in general. It can be described conceptually as follows. Let $B_{s,t}$ denote the indecomposable Soergel bimodule indexed by the longest element of the (finite) rank two parabolic subgroup generated by $s$ and $t$.  The bimodules $B_{\color{blue}s}B_{\color{red}t} \dots $ and $B_{\color{red}t} B_{\color{blue}s} \dots $ each contain $B_{s,t}$ as a summand with multiplicity one. The $2m_{st}$-valent vertex is the projection and inclusion of this common summand. (This determines the morphism up to a scalar, and there is a simple way to fix this choice of scalar.)

It is a result due to Libedinsky \cite{Lib} that these morphisms generate all morphisms between Bott-Samelson bimodules. In this paper we determine the relations which they satisfy. Let us
call a subset $J \subset S$ \emph{finitary} if the corresponding parabolic subgroup is finite. In the Iwahori presentation of $\HB$ for a Coxeter system, there is a generator
$T_s$ for each $s \in S$, i.e. for each finitary subset of rank $1$; there is a quadratic relation for each finitary subset of rank $1$, and a braid relation for each finitary subset of
rank $2$. In our $2$-presentation of $\BSBim$, the generating objects $B_s$ are associated to $s \in S$ (i.e. finitary subsets of rank $1$), the generating morphisms are associated to
finitary subsets of size $\le 2$, and the relations are associated to finitary subsets of of size $\le 3$.

Because the simple reflections are encoded by colors, we refer to a relation as
a \emph{one}, \emph{two} or \emph{three color relation}, depending on the size of the subset of $S$ involved. As one might guess, the relations become more complicated as the number of
colors increases. Here is a description of the relations:
