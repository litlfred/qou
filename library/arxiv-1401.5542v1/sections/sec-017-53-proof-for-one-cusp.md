---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-017-53-proof-for-one-cusp
section_title: "Proof for one cusp"
section_number: 5.3
pages: 13-13
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.64
latex_coverage_ratio: 1.0
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
We first prove Theorem~\ref{thm:PtolemyEqTrace} in the case where there is only one cusp. In this case, all edges are self edges, and $T$ consists of a single edge $\varepsilon_1$.
\begin{lemma}\label{lemma:BootStrapEdgeOneCusp} For any self edge $\varepsilon$, we have $m_1c_\varepsilon\in k_\rho$. 
\end{lemma}
\begin{proof}
Let $X_1$ be a peripheral path such that $X_1\varepsilon$ is a loop (see Figure~\ref{fig:SelfEdgeCase}), and let $x_1$ be such that $\gamma(X_1)=\beta(x_1)$. We have
\begin{equation}\label{eq:OneCuspTraceRel}
\Tr(\gamma(X_1\varepsilon))=\Tr(\beta(x_1)\alpha(c_\varepsilon)) =\Tr\left(\begin{pmatrix}1&x_1\\0&1\end{pmatrix}\begin{pmatrix}0&-c_\varepsilon^{-1}\\c_\varepsilon&0\end{pmatrix}\right)=x_1c_\varepsilon\in k_\rho.
\end{equation}
Applying the same computation to the loop $X_1 M_1 \varepsilon$ yields
\begin{equation}
\Tr(\beta(x_1)\beta(m_1)\alpha(c_\varepsilon))=(x_1+m_1)c_\varepsilon\in k_\rho,
\end{equation}
and the result follows.
\end{proof}
Since the Ptolemy coordinate of $\varepsilon_1$ is $1$, it follows that $m_1\in k_\rho$. Since all edges are self edges, we have $c_\varepsilon\in k_\rho$ for all $1$-cells $\varepsilon$. This concludes the proof in the one cusped case.


\begin{figure}[htb]
\begin{center}
\hspace{-10mm}
\begin{minipage}[c]{0.3\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(235.52596,245.00639)
 \put(0,0){\includegraphics{figures_gen/SelfEdgeBootStrap_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(157.61284,157.186559){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{98.516592pt}
\textcolor{inkcol1}{\large{$\beta(m_1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(74.40285,147.405567){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{69.262756pt}
\textcolor{inkcol1}{\large{$X_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(75.28559,124.596669){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{98.516592pt}
\textcolor{inkcol1}{\large{$\beta(x_1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(152.05261,76.736547){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{95.93536pt}
\textcolor{inkcol1}{\large{$\varepsilon$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(177.02256,66.75248){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{154.012832pt}
\textcolor{inkcol1}{\large{$\alpha(c_\varepsilon)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(126.74744,147.557807){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{69.262756pt}
\textcolor{inkcol1}{\large{$M_1$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hspace{2mm}
\begin{minipage}[c]{0.6\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(447.41534,169.52409)
 \put(0,0){\includegraphics{figures_gen/TwoCuspEdge_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(192.092684,23.022627){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{176.040232pt}
\textcolor{inkcol1}{\large{$\alpha(c_{\varepsilon})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(191.10446,72.425037){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{176.040232pt}
\textcolor{inkcol1}{\large{$\alpha(-c_{\varepsilon})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(321.108055,71.183027){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{176.040232pt}
\textcolor{inkcol1}{\large{$\beta(-m_{j})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(76.758924,70.086057){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{176.040232pt}
\textcolor{inkcol1}{\large{$\beta(m_i)$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\\
\begin{minipage}[t]{0.32\textwidth}
\captionsetup{width=1\textwidth}
\caption{Self edge.}\label{fig:SelfEdgeCase}
\end{minipage}
\hspace{2mm}
\begin{minipage}[t]{0.64\textwidth}
\captionsetup{width=\textwidth}
\caption[Bla]{Edge between cusps.}\label{fig:TwoCuspCase}
\end{minipage}
\end{center}
\end{figure}
