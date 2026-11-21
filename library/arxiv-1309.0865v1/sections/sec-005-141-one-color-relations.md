---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-005-141-one-color-relations
section_title: "One color relations:"
section_number: 1.4.1
pages: 6-7
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.958
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
It was pointed out in \cite{EKh} that most of the one color relations can be concisely encoded in the statement that $B_s$ is a Frobenius object in the
category of $R$-bimodules. The trivalent vertices give the multiplication and comultiplication, whilst the dots provide the unit and counit. The Frobenius biadjunction of $B_s$ with itself arises from certain cups and caps, which are constructed from trivalent vertices and dots. The axioms governing Frobenius objects guarantees that any diagram involving one color is isotopy invariant. The one-color relations not involving polynomials are then the following:
\begin{gather*} \ig{1}{assoc1} \qquad \qquad \ig{1}{unit} \qquad \qquad \ig{1}{needle} \end{gather*}
In addition to the Frobenius relations, one has the following relations governing the interaction of colors and polynomials:
\begin{gather*}
\begin{array}{c}
\tikz[scale=0.9]{
\draw[dashed,gray] (0,0) circle (1cm);
\draw[color=red] (0,0.5) -- (0,-0.5);
\node[draw,fill,circle,inner sep=0mm,minimum size=1mm,color=red] at (0,0.5) {};
\node[draw,fill,circle,inner sep=0mm,minimum size=1mm,color=red] at (0,-0.5) {};
} \end{array}
=
\begin{array}{c}
\tikz[scale=0.9]{
\draw[dashed,gray] (0,0) circle (1cm);
\node at (0,0) {$\alpha_s$};
} \end{array}, \\

\begin{array}{c}
\tikz[scale=0.9]{
\draw[dashed,gray] (0,0) circle (1cm);
\draw[color=red] (0,-1) to (0,1);
\node at (-0.5,0) {$f$};
} \end{array}
=
\begin{array}{c}
\tikz[scale=0.9]{
\draw[dashed,gray] (0,0) circle (1cm);
\draw[color=red] (0,-1) to (0,1);
\node at (0.5,0) {${\color{red}s}(f)$};
} \end{array}
+
\begin{array}{c}
\tikz[scale=0.9]{
\draw[dashed,gray] (0,0) circle (1cm);
\draw[color=red] (0,-1) to (0,-0.5);
\draw[color=red] (0,1) to (0,0.5);
\node[color=red,draw,fill,circle,inner sep=0mm,minimum size=1mm] at (0,-0.5) {};
\node[color=red,draw,fill,circle,inner sep=0mm,minimum size=1mm] at
(0,0.5) {};
\node at (0,0) {$\partial_{\color{red}s} f$};
} \end{array}.
\end{gather*}
