---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-039-9-dependency-graphs-and-mod-gaussian-convergence
section_title: "Dependency graphs and mod-Gaussian convergence"
section_number: 9
pages: 69-70
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.956
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{sec:depgraph}

Dependency graphs are a classical tool in the literature to prove convergence in distribution towards a Gaussian law of the sum of {\em partly} dependent random variables. They are used in various domains, such as random graphs~\cite[pages 147-152]{JLR00}, random polytopes~\cite{BV07}, patterns in random permutations~\cite{Bona10}. As dependency graphs give a natural framework to deal in a uniform way with different kinds of objects, a natural question is the following:  when we have a dependency graph with good properties, can we obtain more precise or other results than convergence in distribution? Here is a brief presentation of the literature around this question.\vspace{2mm}
\begin{itemize}
    \item In \cite{BR89}, P. Baldi and Y. Rinott give precise estimates for the total variation distance between the relevant sequence of random variables and the Gaussian distribution.\vspace{2mm}
  \item In \cite{Jan04}, S. Janson has established some large deviation result involving the fractional chromatic number of the dependency graph.\vspace{2mm}
  \item More recently, H. D\"oring and P. Eichelsbacher have shown how dependency graphs can be used to obtain some moderate deviation principles
      \cite[Section 2]{DE12}.\vspace{2mm}
\end{itemize}
Here, we shall see a link between dependency graphs and mod-Gaussian convergence. This gives us a large collection of examples, for which the material of this article gives automatically some {\em precise} moderate deviation results. Our deviation result has a larger domain of validity than the one of D{\"o}ring and Eichelsbacher --- see below.\bigskip

In this section, we establish a general result involving dependency graphs (Theorem~\ref{thm:dependencygraphsrefined}). In the next two sections, we focus on examples and derive the mod-Gaussian convergence of the following renormalized statistics:\vspace{2mm}
\begin{itemize}
  \item subgraph count statistics in Erd\"os-R\'enyi random graphs (Section \ref{sec:erdosrenyi});\vspace{2mm}
  \item random character values from central measures on partitions (Section \ref{sec:central}).
\end{itemize}
\medskip
