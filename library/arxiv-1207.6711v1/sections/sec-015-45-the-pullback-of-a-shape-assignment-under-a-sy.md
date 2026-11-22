---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-015-45-the-pullback-of-a-shape-assignment-under-a-sy
section_title: "The pullback of a shape assignment under a symmetry"
section_number: 4.5
pages: 13-14
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.853
latex_coverage_ratio: 0.913
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
Recall that we identify the symmetry group of $\Delta_n$ with $S_4$.

\begin{definition}\label{def:PullbackShapes}
Let $\sigma\in S_4$ and let $z\colon\Delta^3_{n-2}(\Z)\times\dot\Delta^3_2(\Z)\to \C\setminus\{0,1\}$ be a map. 
The \emph{pullback} of $z$ under $\sigma$ is the map given by
\begin{equation}\label{actiononshapeassignments}
\sigma^*z\colon \Delta^3_{n-2}(\Z)\times\dot\Delta^3_2(\Z)\to\C\setminus\{0,1\},\qquad (s,e)\mapsto (z^{\sigma(e)}_{\sigma (s)})^{\sgn(\sigma)}.
\end{equation}
\end{definition}

The pullback obviously satisfies the standard properties $\tau^*\sigma^*=(\sigma\tau)^*$ and $\id^*=\id$.

\begin{lemma}\label{shapesymmetries}
The pullback preserves shape assignments.
\end{lemma}

\begin{proof}
Let $z$ be a shape assignment. One easily checks that \eqref{eqn:shapeparamrel} is preserved under the $A_4$ action on the indices, so the result follows for $\sigma\in A_4$. Hence, all that remains is to prove the result for the permutation $\sigma_{01}$ switching $0$ and $1$. The equation
\begin{equation}
(\sigma_{01}^*z)_s^{0011}=(\sigma_{01}^*z)_s^{1100}=\frac{1}{1-(\sigma_{01}^*z)_s^{0101}}
\end{equation}
is equivalent to
\begin{equation}
(z^{0011}_{\sigma_{01}(s)})^{-1}=(z^{1100}_{\sigma_{01}(s)})^{-1}=\frac{1}{1-(z_{\sigma_{01}(s)}^{1001})^{-1}},
\end{equation}
which follows from \eqref{shapepar1} and \eqref{shapepar2}. The other equations are similarly verified.
\end{proof}

Note that if $\sigma\in A_4$ is a rotation, the pullback $\sigma^* z$ is the shape assignment obtained from $z$ by rotating the simplex by $\sigma$. If $\sigma$ is orientation reversing, one must also replace all the shape parameters by their inverses.

\begin{remark}\label{rm:reordering}
We view the pullback of a shape assignment on an ordered simplex $\Delta$ as the natural induced shape assignment on the simplex $\Delta'$ obtained from $\Delta$ by reordering the vertices such that the $i$th vertex of $\Delta'$ is the $\sigma(i)$th vertex of $\Delta$.
\end{remark}

\begin{figure}[htb]
\begin{center}
\begin{minipage}[b]{0.45\textwidth}
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(267.52676,120.92316)
 \put(0,0){\includegraphics{figures_gen/ActionReorder_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(245.410089,58.27812){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{167.018032pt}
\textcolor{inkcol1}{\normalsize{$\scriptstyle z^{0110}_{0021}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(101.2924538,58.27812){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{167.018032pt}
\textcolor{inkcol1}{\normalsize{$\scriptstyle (\sigma^*\!z)^{0101}_{0210}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
 
\end{minipage}
\hfill
\begin{minipage}[b]{0.45\textwidth}
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(267.52676,120.92316)
 \put(0,0){\includegraphics{figures_gen/ActionPullback_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(245.410089,58.27812){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{167.018032pt}
\textcolor{inkcol1}{\normalsize{$\scriptstyle z^{0110}_{0021}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(47.767577,118.85246){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{167.018032pt}
\textcolor{inkcol1}{\normalsize{$\scriptstyle (\sigma^*\!z)^{0101}_{0210}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup

\end{minipage}
\\
\begin{minipage}[t]{0.45\textwidth}
\caption{Reordering by $\sigma=(123)$.}
\end{minipage}
\begin{minipage}[t]{0.45\textwidth}
\caption{Pullback by $\sigma=(123)$.}
\end{minipage}
\end{center} 
\end{figure}
