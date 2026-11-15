---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-028-52-jones-wenzl-morphisms
section_title: "Jones-Wenzl morphisms"
section_number: 5.2
pages: 42-45
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.982
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-JW}


Presenting the Bott-Samelson category in rank $2$ is the topic of \cite{EDihedral}. The calculations and proofs are too long to duplicate or fully discuss in this paper. If the reader is
willing to accept the Jones-Wenzl morphisms as black boxes\footnote{no pun intended!}, satisfying the properties stated in this section and the next, then the reader need not consult
\cite{EDihedral}. We assume the reader is familiar with quantum numbers and Temperley-Lieb algebras; background can be found in \cite{EDihedral}.

Fix $m<\infty$. Consider the Temperley-Lieb algebra $TL$ over $\ZM[z]$ with $m-1$ strands, where the circle is evaluates to $-z$. In any $\Bbbk[z]$-algebra we will use quantum
numbers to indicate the images of certain polynomials in $z$, where $[2]$ is the image of $z$. For instance, $[3]$ is the image of $z^2-1$. When we say that $q$ is specialized to a
primitive $2m$-th root of unity in a $\ZM[z]$-algebra, we mean that $m$ satisfies the minimal polynomial of $[2]$ at this root of unity, which equates to the statements that $[m]=0$, $[k]\ne 0$ for $0< k < m$, and $[m-1]=1$.

After inverting some quantum numbers, Temperley-Lieb algebras contain elements known as \emph{Jones-Wenzl projectors}, and the Jones-Wenzl projector on $m-1$ strands $JW_{m-1}$ is known to
be negligible and rotation-invariant when $q$ is specialized to a primitive $2m$-th root of unity. The Jones-Wenzl projector $JW_m$ can be defined whenever certain quantum binomial
coefficients are invertible. Using diagrammatics for the Temperley-Lieb algebra, the Jones-Wenzl projector can be described as a linear combination of crossingless matchings.

\begin{ex} $\ig{1}{JWinTL}$ \end{ex}

Any crossingless matching will divide the planar strip into $2(m-1)$ regions, which can be colored (say, red and blue) so that colors always alternate across a strand. This gives rise to
the \emph{two-colored Temperley-Lieb algebra}, which is an endomorphism algebra appearing inside a 2-category with 2 objects, red and blue. In this algebra, the value of a blue circle
surrounded by red and a red circle surrounded by blue can be different scalars; so we define this algebra over the ring $\ZM[x,y]$. Jones-Wenzl projectors still exist, but each comes in
two flavors with different coefficients, depending on whether blue or red appears on the far right. The other flavor is obtained by switching the colors and switching $x$ and $y$.

\begin{ex} $\ig{1}{JWin2TL}$ \end{ex}

Choose two indices $s,t \in S$. Given a 2-colored crossingless matching, we obtain a Soergel graph on the planar disc as follows: deformation retract each region into a tree composed out
of trivalent and univalent vertices, and color these trees appropriately. The result will always be a Soergel graph of degree $+2$. In order for this map to be well-defined, not just for
crossingless matchings but also for diagrams with embedded circles, one must specialize $\ZM[x,y]$ to $\Bbbk$ under the map sending $x \mapsto a_{st}$ and $y \mapsto a_{ts}$. The reader
should convince themselves that this makes sense, using \eqref{dotforcegeneral}, \eqref{alphais}, and \eqref{needle} until the scalar $\pa_s(\a_t) = a_{st}$ appears. Associated to the
Jones-Wenzl projector we have a linear combination of Soergel graphs, which we call the \emph{Jones-Wenzl morphism}. It comes in two color-flavors, as before.

\begin{ex} $\ig{1}{JWinSoergAlt}$ \end{ex}

The coefficients in these Jones-Wenzl projectors are rational functions in the 2-colored quantum numbers, as in Definition \ref{def:2qnum}. When $[m]_x=[m]_y=0$, one can show that
$JW_{m-1}$ is well-defined within $\ZM[x,y]$ (i.e. no denominators are necessary). If either $m$ is odd or if $m$ is even and $[m-1]=1$, $JW_{m-1}$ will be rotation-invariant (under
color-preserving rotations). If $m$ is even and $[m-1]=1$, it is also the case that rotating the left-blue-aligned Jones-Wenzl morphism by one strand yields the left-red-aligned
Jones-Wenzl morphism. If $m$ is odd, this holds if and only if $[m-1]_x = [m-1]_y = 1$; this is the feature behind the definition of a balanced realization. Using the examples above, the
reader should convince themselves of these rotational facts when $m=4$ (since $a_{st} a_{ts} = 2$) or when $m=3$ and $a_{st}=a_{ts}= \pm 1$. More discussion of the non-balanced case is
found in Section \ref{nonbalanced}.

The Jones-Wenzl Soergel graph above is not technically a morphism in $\DC$, because it lives on the planar disc, but it can be plugged into another diagram to produce a planar strip graph.
This is done in relation \eqref{dot2m}, where the rotation-invariant $JW_{m-1}$ is used. An implication of \eqref{dot2m} and \eqref{assoc2} is the following relation.
\begin{equation} \ig{1}{twocoloridemp} \label{twocoloridemp} \end{equation}
Note that here and henceforth, we will only use $JW_{m-1}$ when $m_{s,t}=m$, which we abbreviate as $JW$.

On the RHS of \eqref{twocoloridemp}, we took the Jones-Wenzl in the two-colored Temperley-Lieb algebra, transformed it into a degree $2$ Soergel graph on the disc, and then transformed it
again into a degree $0$ endomorphism of a color-alternating Bott-Samelson in $\DC$, by placing trivalent vertices on each side. This general procedure can be applied to any two-colored
crossingless matching, giving a map from the two-colored Temperley-Lieb algebra to a certain endomorphism ring in $\DC$. This map is a homomorphism. because $JW_{m-1}$ is idempotent in
$TL$, the RHS of \eqref{twocoloridemp} is also idempotent. The $2m$-valent vertex is thus ``half an idempotent."

The defining properties of the Jones-Wenzl projectors in $TL$ correspond to the following two properties in Soergel graphs. The first is that the coefficient of a certain graph is $1$, as
can be seen from the examples above. This is the graph which, when trivalent vertices are attached to make a degree $0$ morphism, becomes the identity map. The second property is called
\emph{death by pitchfork}:

\begin{equation} \ig{1}{JWpitch} \label{JWpitch} \end{equation}

Now let us note some properties of any $(m-1,m-1)$ crossingless matching, transformed into a Soergel graph. When viewed as a degree $+2$ graph on the disc, there will be a boundary dot on
at least one of any $m-1$ adjacent strands. When viewed as a degree $+0$ endomorphism of a length $m$ color-alternating object $B_s \ot B_t \ot \ldots$ in $\DC$, it can be given a
\emph{negative-positive decomposition}. That is, we say the initial \emph{width} of the map is $m$, the number of strands on the boundary. Reading from bottom to top, we may first apply
all negative maps (i.e. bottom boundary dots, merging trivalents, and caps) which are the maps which decrease the width. Then we can apply all positive maps (i.e. cups, splitting
trivalents, top boundary dots), increasing the width back up to $m$. The morphism will factor through a length $k$ color-alternating object $B_s \ot B_t \ot \ldots$ for some $k \le m$
which is the minimal width reached. Whenever the crossingless matching is not the identity map, we have $k < m$. These properties will be used in Chapter \ref{sec-LLLproof}.

\begin{remark} \label{twocolorrelncatfd} Consider the usual Temperley-Lieb category over a $\ZM[z]$-algebra where $[m]=0$ and $[k] \ne 0$ for $0 < k < m$. Then the Temperley-Lieb algebra
with $k$ strands is isomorphic to (an integral form of) the endomorphism ring of the $U_q(\mathfrak{sl}_2)$-representation $V_1^{\ot k}$ (at generic $q$), for any $0 \le k<m$. The direct
sum decomposition \[V_1^{\ot m-1} \cong V_d^{\oplus c_{m-1,d}} \] implies the existence of certain idempotents (and isomorphisms between their images within an isotypic component) which
produce this splitting. A similar statement can be made for the two-colored Temperley-Lieb category. We can transform these maps into degree $0$ morphisms in $\DC$, to obtain a direct sum
decomposition for any color-alternating $B_s \ot B_t \ot \ldots$ of length $\le m$. This can be used to categorify relation \eqref{rank2hecke}. See \cite{EDihedral} for more details.

However, we cannot assume in general that $[k] \ne 0$ for all $k < m$. For instance, this is false when we take a realization of a finite dihedral group, and view it as a non-faithful
realization of a larger dihedral group. Nonetheless, we will soon categorify the relation of Example \ref{rank2heckeEx}. \end{remark}
