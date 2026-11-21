---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-010-3-trace-of-a-linear-category
section_title: "Trace of a linear category"
section_number: 3
pages: 13-13
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{sec_trace_lincat}



In this section we define trace or zeroth  Hochschild homology groups for linear and additive categories, and  discuss their properties.

A category $\C$ is called {\it linear} if its hom-spaces are equipped
with structures of abelian groups and the composition maps are bilinear.
Such a structure is sometimes called an $\rm\bf {Ab}$-category, or a category enriched in the monoidal category $\rm \bf {Ab}$ of abelian groups.
A {\it linear} functor between two linear categories $\C$ and $\cal{D}$ is a functor $F:\C\to \cal{D}$ such that
for $x,y\in \Ob(\C)$ the map $F: \C(x,y)\to \cal{D}(F(x), F(y))$ is an abelian group homomorphism.

\nc\TL{\rm TL}
\begin{example} The Temperley-Lieb category $\TL$ is defined as a quotient of the $\Z[A,A^{-1}]$-span of  tangles by the Kauffman bracket skein relations:
\begin{align*}
 \left\langle \;\hackcenter{
\begin{tikzpicture}

\draw [very thick] (0,0) -- (1,1);
\draw [very thick] (1,0) -- (.6, .4);
\draw [very thick] (.4,.6) -- (0,1);
\end{tikzpicture} } \;
\right\rangle
\;\;  &= \;\; A \; \left\langle \;
\hackcenter{
\begin{tikzpicture}

\draw [very thick] (0,0) .. controls (.25,.25) and (.25,.75) .. (0,1);
\draw [very thick] (1,0) .. controls (.75,.25) and (.75,.75) .. (1,1);
\end{tikzpicture} } \; \right\rangle
\;\; + \;\; A^{-1}  \left\langle \;
 \hackcenter{
\begin{tikzpicture}

\draw [very thick] (0,0) .. controls (.25,.25) and (.75,.25) .. (1,0);
\draw [very thick] (0,1) .. controls (.25,.75) and (.75,.75) .. (1,1);
\end{tikzpicture} } \; \right\rangle,
\\
 \left\langle \;\hackcenter{ T  \coprod
\hackcenter{\begin{tikzpicture}

\draw [very thick] (0,.5).. controls ++(0,.35) and ++(0,.35) .. (.8,.5);
\draw [very thick] (0,.5).. controls ++(0,-.35) and ++(0,-.35) .. (.8,.5);
\end{tikzpicture} } } \; \right\rangle &= (-A^{-2}-A^{2}) \la T \ra.
\end{align*}
The objects of this category are natural numbers corresponding to the boundary points of the tangle.
A morphism in $\TL$ is a  $\Z[A,A^{-1}]$-linear combination of
crossingless matchings between the boundary points.
\[
\hackcenter{\begin{tikzpicture}
    \draw[thick] (-0.25,0.5) .. controls ++(0,-0.5) and ++(0,-0.5) .. (0.25,0.5);
    \draw[thick] (-1.25,0.5) .. controls ++(0,-0.5) and ++(0,-0.5) .. (-.75,0.5);
    \draw[thick] (-1.75,0.5) .. controls ++(-0,-0.5) and ++(0,0.85) .. (-0.25,-1);
    \draw[thick] (-2.25,-1) .. controls ++(-0,0.85) and ++(0,0.85) .. (-0.75,-1);
    \draw[thick] (-1.75,-1) .. controls ++(-0,0.35) and ++(0,0.35) .. (-1.25,-1);
    \draw[thick] (0.75,0.5) .. controls ++(-0,-0.5) and ++(0,0.5) .. (0.25,-1);
     \draw[thick] (1.25,-1) .. controls ++(-0,0.5) and ++(0,0.5) .. (0.75,-1);
      \node at (-0.25,0.5) {$\bullet$};
      \node at (-0.75,0.5) {$\bullet$};
      \node at (-1.25,0.5) {$\bullet$};
      \node at (-1.75,0.5) {$\bullet$};
      \node at (0.25,0.5) {$\bullet$};
      \node at (0.75,0.5) {$\bullet$};
      \node at (1.25,-1) {$\bullet$};
      \node at (-0.25,-1) {$\bullet$};
      \node at (-0.75,-1) {$\bullet$};
      \node at (-1.25,-1) {$\bullet$};
      \node at (-1.75,-1) {$\bullet$};
      \node at (-2.25,-1) {$\bullet$};
      \node at (.25,-1) {$\bullet$};
      \node at (.75,-1) {$\bullet$};



\end{tikzpicture}}
\]
\end{example}
