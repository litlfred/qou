---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-040-131-simplifying-the-cusp-equations
section_title: "Simplifying the cusp equations"
section_number: 13.1
pages: 42-43
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.945
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\begin{lemma} 
The cusp equations are equivalent to the equations
\begin{equation} \label{eq:SimplifiedCuspEquation}
\prod_{j=1}^r\frac{(\beta_j)_{ll}}{(\beta_j)_{l+1,l+1}}\prod_{j=1}^s\frac{(\gamma_j)_{ll}}{(\gamma_i)_{l+1,l+1}}=1.
\end{equation}
Moreover, each factor is given by an expression of the form
\begin{equation}\label{eq:Simplification}
\frac{(\beta_j)_{ll}}{(\beta_j)_{l+1,l+1}}=-\prod_{k=1}^{n-1-l}X_{k,l,\Delta}^{\varepsilon_\circlearrowleft^{v_0v_1v_2}},\qquad \frac{(\gamma_j)_{ll}}{(\gamma_j)_{l+1,l+1}}=z_{l,\Delta}^{-\varepsilon_\circlearrowleft^{v_0v_1v_2}}
\end{equation}
where $v_0v_1v_2$ is the starting vertex of $\beta_j$, respectively, $\gamma_j$ and $\Delta$ is the corresponding simplex.
\end{lemma}

\begin{proof}
Equation \eqref{eq:SimplifiedCuspEquation} follows from the fact that the $n$th diagonal entry is $1$ for both short and middle edges.
By Remark~\ref{rm:DiagonalEntries}, the diagonal entries are expressions of the form
\begin{equation}
\label{main}
(\beta_j)_{ll}=(-1)^{n-l}\prod_{i=l}^{n-2}\prod_{k=1}^{n-1-i}X_{k,i}^{\varepsilon_\circlearrowleft^{v_0v_1v_2}},\quad (\gamma_j)_{ll}=\prod_{i=l}^{n-1}z_i^{-\varepsilon_\circlearrowleft^{v_0v_1v_2}}.
\end{equation}
Taking quotients, this proves the result.
\end{proof}



\begin{figure}[htb]
\begin{center}
\scalebox{0.9}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(603.37,193.08691)
 \put(0,0){\includegraphics{figures_gen/CuspEquationTerms_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(163.343821,169.0582396){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(299.167501,195.5816696){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(250.826331,11.8306896){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.743841,11.8306896){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_0$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(142.991721,121.047288){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\normalsize{$\beta^{v_1v_2v_0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(194.721618,54.35182){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{94.889168pt}
\textcolor{inkcol1}{\normalsize{$X_{1,l}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(137.696878,54.35182){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{94.889168pt}
\textcolor{inkcol1}{\normalsize{$X_{l-1,l}\cdots$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(462.284018,50.53463){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{94.889168pt}
\textcolor{inkcol1}{\normalsize{$z_l$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(403.417981,169.0582396){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(539.241661,195.5816696){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(490.900491,11.8306896){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(323.818001,11.8306896){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{102.55912pt}
\textcolor{inkcol1}{\normalsize{$v_0$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(382.249511,110.642968){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{150.545312pt}
\textcolor{inkcol1}{\normalsize{$\gamma^{v_1v_2v_3}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.485631,43.67588){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{82.118288pt}
\textcolor{inkcol1}{\normalsize{Level $l$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{center}
\caption{The terms in the simplified cusp equations at level $l$.}\label{fig:CuspEqTerms}
\end{figure}

\begin{remark}
Note that the contribution from a middle edge is (minus) the product of the $X$-coordinates at level $l$. The contribution from a short edge is the shape coordinate at level $l$. See Figure~\ref{fig:CuspEqTerms}. 
\end{remark}

\begin{remark}
Note that the cusp equations can be written in the form~\eqref{eq:GluinEqSimplified}, but with $1$ replaced by a sign.
\end{remark}
