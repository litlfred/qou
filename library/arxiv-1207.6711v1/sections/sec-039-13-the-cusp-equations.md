---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-039-13-the-cusp-equations
section_title: "The cusp equations"
section_number: 13
pages: 41-42
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.893
latex_coverage_ratio: 0.918
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:CuspEquations}

The decomposition of $M$ into doubly truncated simplices and prisms induces a polyhedral decomposition of $\partial M$. Note that every simple closed curve in $\partial M$ is isotopic to an edge path in this decomposition. 

Let $\sigma$ be a natural $(\PGL(n,\C),B,H)$-cocycle on $M$. By Remark~\ref{rm:NaturalLift}, the restriction of $\sigma$ to $\partial M$ has a canonical lift (also denoted by $\sigma$) to a cocycle with values in $B\subset\GL(n,\C)$.  

\begin{definition}
Let $\lambda$ be a closed edge path in $\partial M$ and let $\beta_1,\dots\beta_r$ and $\gamma_1,\dots,\gamma_s$ be the labelings induced by $\sigma$ of the middle, respectively, short edges traversed by $\lambda$. For $l=1,\dots, n-1$, the \emph{level $l$ cusp equation} of $\lambda$ is the equation
\begin{equation}
\prod_{j=1}^r(\beta_j)_{ll}\prod_{j=1}^s(\gamma_j)_{ll}=1,
\end{equation}
where the subscript $ll$ denotes the $l$th diagonal entry.
\end{definition}

\begin{figure}[htb]
\begin{center}
\scalebox{0.9}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(373.12189,185.3125)
 \put(0,0){\includegraphics{figures_gen/doubleTruncatedCusp_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.463578,150.1093127){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(73.277382,105.6308027){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(100.152482,74.9208727){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(136.377192,84.5313627){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_4$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(203.263672,73.6577227){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_5$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(242.475462,53.1125927){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_6$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(273.741112,72.0415327){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_7$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(342.368492,106.1539327){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\gamma_8$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(56.182912,149.6627427){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\beta_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(174.032382,109.4500527){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\beta_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(294.316002,113.8548127){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{260.761352pt}
\textcolor{inkcol1}{\normalsize{$\beta_3$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{center}
\caption{A curve in the polyhedral decomposition of $\partial M$.}
\end{figure}

\begin{lemma}
The representation $\rho$ determined (up to conjugation) by $\sigma$ is boundary-unipotent if and only if the cusp equation at each level is satisfied for each edge path representing a generator of the fundamental group of a boundary component of $\partial M$.
\end{lemma}

\begin{proof}
By definition, $\rho$ is boundary-unipotent if and only if for each closed edge path $\lambda$ in $\partial M$, the product of the labelings of edges traversed by $\lambda$ is in $N$. This proves the result.
\end{proof}

\begin{remark}
Note that for $n=2$ we recover the traditional cusp equations.
\end{remark}
