---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-041-71-negative-positive-decompositions
section_title: "Negative-positive decompositions"
section_number: 7.1
pages: 70-72
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.984
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-negpos}


For the rest of this chapter we will be interested in embedded graphs, not isotopy classes thereof. We will abusively use the term \emph{Soergel graph} to refer to a graph embedded without
horizontal tangent lines, so that no two vertices share the same $y$-coordinate. This kind of graph can be written as the product of the generators in the introduction, tensored with
identity maps. Recall that those generators were the bottom boundary dot, the top boundary dot, the trivalent split, the trivalent merge, the $2m$-valent vertex viewed as a map with $m$ inputs and $m$
outputs, and polynomials. In all our arguments, polynomials will be treated separately from other parts of a graph.

Given such a graph, it has \emph{height} $k$ if it is a product of $k$ generators, ignoring the polynomials. At a given $y$-coordinate without a vertex, we say the diagram has \emph{width}
$k$ if the object given by the horizontal line at that coordinate is $B_{\un{x}}$ for a sequence of length $k$ (i.e. if the horizontal line passes through $k$ strands). The \emph{maxwidth} of a
diagram is the maximal width attained.

We classify the generators as being \emph{positive}, \emph{neutral}, or \emph{negative}, depending on whether they increase, preserve, or decrease the width when reading from bottom to
top. Thus a top boundary dot and a splitting trivalent are positive, a $2m$-valent vertex and a box are neutral, and a bottom boundary dot and a merging trivalent are negative. Note that
light leaves $\LL_{{\un{x}},\eb}$ are constructed purely out of non-positive maps. The \emph{negative height} of a map is the number of negative generators used, and similarly for the
\emph{positive height}.

\igc{1}{generatorsposneg}

The central generator is supposed to represent any $2m$-valent vertex.

A graph will be called \emph{negative-positive} if it consists of a composition of negative and neutral (\emph{non-positive}) maps followed by a composition of positive and neutral
(\emph{non-negative}) maps. In other words, the maximal width is attained on the outside; the map shrinks in width towards the middle and then expands again. We say the map is
\emph{strictly} negative-positive if the width shrinks non-trivially. Because polynomials are neutral, they can appear anywhere. Given a morphism in $\DC$, an expression for it as a
$\Bbbk$-linear combination of negative-positive graphs is called a \emph{negative-positive decomposition}.

Any map of the form $\LL_{{\un{x}},\eb}$ is constructed out of non-positive generators. Thus every double leaves map $\LLL$ is a negative-positive map, and the main theorem implies that every morphism in $\DC$ has a negative-positive decomposition.

We state some lemmas about negative-positive decompositions:

\begin{claim} Consider the Jones-Wenzl morphism as a degree $0$ map (i.e. the RHS of \eqref{twocoloridemp}). With the exception of the identity map, every other diagram is strictly
negative-positive. Moreover, every other diagram attains a width $\le m-2$. \end{claim}

\begin{proof} This is obvious. Perhaps it is most evident using the diagrammatic cellular structure on the Temperley-Lieb algebra. \end{proof}

\begin{claim} Any strictly non-positive map from $B_{\un{w}}$, for ${\un{w}}$ a reduced expression, is in the span of maps with a bottom boundary dot. \label{posrexhasdot} \end{claim}

\begin{proof} No rex can be the source of a merging trivalent $ss \to s$. Thus the map must consist of some rex move with polynomials followed by a bottom dot. We know,
using \eqref{dot2m}, that a dot on top of a $2m$-valent vertex yields a sum of diagrams, each of which has a bottom boundary dot. Thus we can ``pull" the dot successively through all the
$2m$-valent vertices in the rex move (ignoring any polynomials) until we have a bottom boundary dot. \end{proof}

\begin{claim} If $\phi = fgh$ where $f$ is non-negative, $h$ is non-positive, and $g$ has a (strictly) negative-positive decomposition, then $\phi$ has a (strictly) negative-positive
decomposition. \end{claim}

\begin{proof} This is obvious. \end{proof}

\begin{lemma} \label{rexmovesmlt} Let ${\un{w}}$ and ${\un{w}}'$ be two rexes for the same element $w \in W$, and let $\beta$ and $\beta'$ be two rex moves from ${\un{w}}$ to ${\un{w}}'$. Then $\beta -
\beta'$ has a strictly negative-positive decomposition. In particular, $\beta -
\beta'$ is in the span of diagrams having both a bottom and a top boundary dot.\end{lemma}

\begin{proof} We already know (see section \ref{subsec-RexMoves}) that two rex moves can be connected by a series of transformations. These transformations correspond to the Zamolodchikov
relations \eqref{A3std}, \eqref{B3std}, \eqref{H3std}, \eqref{A1I2mstd}, and the relation \eqref{2misomstd}. The difference between two rex moves which differ by a single transformation in
$\DC$ is given by the analog of each of these relations: \eqref{A3}, \eqref{B3}, \eqref{H3}, \eqref{A1I2m}, and \eqref{twocoloridemp}. Applying the transformation for $A_3$ or $B_3$ or
$A_1 \times I_2(m)$ will yield no difference between the rex moves. Applying the transformation for $H_3$ or \eqref{twocoloridemp} will have a difference with a strictly negative-positive
decomposition. More precisely, this transformation is applied somewhere within the rex move, but using the previous claim, the overall difference will still have a strictly
negative-positive decomposition. We can write $\beta - \beta' = (\beta - \beta_1) + (\beta_1 - \beta_2) + \ldots +(\beta_k -\beta')$ where each successive difference corresponds to a
single transformation. The result follows. \end{proof}

For $w \in W$ and an arbitrary sequence ${\un{x}}$ we write $w \le {\un{x}}$ if there exists a subsequence $\eb$ of ${\un{x}}$ expressing $w$.

\begin{lemma} \label{rexesonlyplz} Let ${\un{x}}$ be a sequence. The identity of $B_{\un{x}}$ has a negative-positive decomposition where each term factors through some $B_{\un{w}}$ for some reduced
expression ${\un{w}}$ for $w \le {\un{x}}$. \end{lemma}

\begin{proof} Let us use induction on the length of ${\un{x}}$. Whenever ${\un{x}}$ is a reduced expression the statement is trivial. Suppose that ${\un{x}}$ contains a repeated index $ss$. One can apply
the relation \eqref{iiidemp2} give a negative-positive decomposition where each term factors through ${\un{x}}'$, the sequence identical to ${\un{x}}$ except with one copy of $s$ removed. Applying
the inductive hypothesis to ${\un{x}}'$ and nesting negative-positive decompositions, we have the result for ${\un{x}}$.

Suppose that ${\un{x}}$ is not a reduced expression. There is some finite sequence of braid relations $\ubr{sts\ldots}{m} = \ubr{tst\ldots}{m}$ which, when applied to ${\un{x}}$, yield a new
sequence which has a repeated index. Let us induct on the number of such relations which need to be applied before a repeated index is reached. For each relation applied, we can use
\eqref{twocoloridemp} to replace the identity $\1_{sts\ldots}$ inside $\1_{\un{x}}$ with the doubled $2m$-valent vertex (the LHS of \eqref{twocoloridemp}) plus a linear combination of strictly
negative-positive maps. The doubled $2m$-valent vertex yields a neutral map factoring through some sequence ${\un{x}}'$ which is closer to having a repeated index. Therefore, by induction,
$\1_{\un{x}}$ has a negative-positive decomposition as desired. \end{proof}
