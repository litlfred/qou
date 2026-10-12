---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-002-12-an-outline-of-the-paper
section_title: "An outline of the paper"
section_number: 1.2
pages: 5-5
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.981
---
\label{sub-intropart2}
The paper is organized as follows.
\begin{itemize}
\item Section~\ref{sec-tilting} contains 
the definition and some basic properties of the category 
of $\Uq$-tilting modules $\T$ as well as the category of projective 
endofunctors of it. Most of Section~\ref{sec-tilting} is known, 
but we have included some new observations.
\item In Section~\ref{sec-quiver} we recall Khovanov-Seidel's $m$-quiver 
algebra $\Am$ and introduce the ``infinite version'' $\Ai$. 
We show that the regular blocks of 
$\T$ embed into the
module category of $\Ai$. 
Since $\Ai$ is naturally graded, we thus, define 
blockwise a grading on $\T$ and $\Endo(\T_{\lambda})$.
\item Section~\ref{sec-dia} finally provides the diagrammatic interpretation of the results from before.
That is, we introduce a diagram category $\QD$ which is a quotient of the diagram 
category studied by Elias~\cite{el1} and show that the additive closure of $\QD$ and 
$\Tgrl$ are equivalent as graded categories. Similarly, we enrich $\QD$ and obtain a 
diagrammatic description of the (graded) category of endofunctors as well.
\end{itemize}
Everything is very explicit and we try to 
illustrate this with examples along the way.

\begin{rem}\label{remark-colors}
We use colors in this paper. Some of them are not important and only 
for illustration. But in Section~\ref{sec-dia} we 
need red and green and it is crucial 
that they are different.
The reader 
who has a black-and-white version can distinguish these 
since green appears lightly shaded.
\end{rem}

\noindent \textbf{Acknowledgements:} We thank 
Christian Blanchet, Ben Elias, Gregor Masbaum, Catharina Stroppel, Pedro Vaz and 
Geordie Williamson for many helpful discussions. 
Special thanks to Geordie Williamson for pointing 
out a connection of the tilting category to an 
anti-spherical quotient of Elias' dihedral cathedral. We are also 
grateful to the anonymous referees for many careful comments and corrections.
D.T. thanks the Danish summer for, 
positively formulated, not distracting him from typing this paper.


\section{The tilting category \texorpdfstring{$\T$}{T}}\label{sec-tilting}

In this section we describe the category $\T$ of 
$\Uq=\Uq(\mathfrak{sl}_2)$-tilting modules for the quantum enveloping 
algebra\footnote{We like to work over the cyclotomic field $\bC$, but any field of characteristic zero containing $q$ would work.} of $\mathfrak{sl}_2$ at a fixed root of unity $q$.
We give a hopefully self-contained summary of the results in the $\mathfrak{sl}_2$ case 
since most results are either spread out over the 
literature or only mentioned implicitly. But 
we have also included some new observations related to our context.



We mostly follow~\cite[Chapters~1,~2,~3]{ja} with our 
notation, $v$ denotes an indeterminate, $q\in\bC$ denotes a 
fixed root of unity and all module categories 
in this section are categories of \textit{left} 
modules.
