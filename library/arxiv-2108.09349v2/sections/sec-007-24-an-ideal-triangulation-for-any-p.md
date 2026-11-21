---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-007-24-an-ideal-triangulation-for-any-p
section_title: "An ideal triangulation for any p"
section_number: 2.4
pages: 10-10
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.788
latex_coverage_ratio: 1.0
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:anyp}

Guided by the previous examples along with Figure~\ref{fig:p=3},  form an initial triangulation, $\hat{\tau}_p$,  of $X_{p}$, the complement of the closure of $C^2\sigma_1^p\sigma_2^{-1}$, that consists of $2p+4$ tetrahedra:  $t_1^\prime$ and $w_0^\prime$ (n\'ee~$t_2^\prime$) in $\Delta_t$; $w_p$ (n\'ee~$m_1$) and $m_2$ in $\Delta_m$; $b_1$ and $b_2^\prime$ in $\Delta_b$; and $w_i$ and $w_i^\prime$ in $\Delta_{wi}$ where $i=1,\dots, p-1$.  The face pairings of $\hat{\tau}_p$ are determined by sliding faces along the braid and using the full-twist identifications at the top and bottom of the product region as described in~\ref{sec:p=1} and~\ref{sec:p=3}.  As before, the addition of the $w$-layers does not affect identifications amongst $m_2$, $b_1$, $b_2^\prime$, and $t_1^\prime$, so the Pachner moves depicted in Figures~\ref{fig:3-2move} and~\ref{fig:2-0move} can be applied.  Define $\tau_{p}$ to be the resulting triangulation.  As with $\tau_{2}$, the observations about $\tau_{3}$ from the previous section apply to $\tau_{p}$, yielding the  face pairings listed in Table~\ref{table:anyp} for $p>1$.  (For $p=1$, see Figure~\ref{fig:2-0move}.)

\begin{table}[ht]
\caption{Face pairings for~$\tau_{p}$, a triangulation of $X_{p}$ for $p>1$.\label{table:anyp}}
\begin{tabular}{ |l c l l |}
   \hline
$w_i^\prime(015)$    &$\sim$	&$w_{i+1}(105)$ & $i=0,\dots,p-1$\\
  \hline
 $w_i^\prime(125)$    &$\sim$	&$w_{i+1}^\prime(025)$ & $i=0,\dots,p-2$\\
  \hline
$w_i(025)$    &$\sim$	&$w_{i+1}(125)$ & $i=1,\dots,p-1$\\
  \hline
 $w_i(012)$    &$\sim$	&$w_{i+1}^\prime(102)$ &$i=1,\dots,p-2$\\
  \hline
  $w_0^\prime(012)$    &$\sim$	&$w_p(021)$&\\
  \hline
$w_0^\prime(025)$    &$\sim$	&$w_p(520)$&\\
  \hline
$s(cad)$    &$\sim$	&$w_1(125)$ &\\
  \hline
$s(abc)$    &$\sim$	&$w_1^\prime(201)$&\\
  \hline
$s(dbc)$    &$\sim$	&$w_{p-1}^\prime(125)$&\\
 \hline
$s(bad)$    &$\sim$	&$w_{p-1}(201)$&\\
 \hline
 \end{tabular}
\end{table}

The triangulation $\hat{\tau}_p$ had $2p+4$ tetrahedra.  The 3-2 Pachner move reduced this number by one and the 2-0 Pachner move further reduced the number of tetrahedra by two, so $\tau_{p}$ has $2p+1$ tetrahedra and thus $4p+2$ face pairings.  There are exactly $4p+2$ identifications in Table~\ref{table:anyp} (and six in Figure~\ref{fig:2-0move}).  Thus, the definition of the triangulation~$\tau_{p}$ is complete.  

Note that most of the tetrahedra in~$\tau_{p}$ (all but $s$) are visible in the complement of the 6-braid $\sigma_1^p\sigma_4^{-1}$.  Using this visualization can help us quickly deduce relationships between the tetrahedra.  For example, Figure~\ref{fig:anyp} shows how $w_0^\prime$, $w_1$, $w_1^\prime$, $\dots$, $w_{p-1}$, $w_{p-1}^\prime$, and $w_p$ are situated in the braid complement, and all but six face pairings of~$\tau_{p}$ can be derived directly from following their faces through the half-twists in the braid.

\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{anypRev.pdf}
\put(0.7, 1.1){\tiny0}\put(2.03, 1.1){\tiny1}\put(3.36, 1.1){\tiny2}\put(4.69, 1.1){\tiny3}\put(6.02, 1.1){\tiny4}\put(7.35, 1.1){\tiny5}
\put(0.7, 3.1){\tiny0}\put(2.03, 3.1){\tiny1}\put(3.36, 3.1){\tiny2}\put(4.69, 3.1){\tiny3}\put(6.02, 3.1){\tiny4}\put(7.35, 3.1){\tiny5}
\put(0.7, 5.1){\tiny0}\put(2.03, 5.1){\tiny1}\put(3.36, 5.1){\tiny2}\put(4.69, 5.1){\tiny3}\put(6.02, 5.1){\tiny4}\put(7.35, 5.1){\tiny5}
\put(0.7, 7.1){\tiny0}\put(2.03, 7.1){\tiny1}\put(3.36, 7.1){\tiny2}\put(4.69, 7.1){\tiny3}\put(6.02, 7.1){\tiny4}\put(7.35, 7.1){\tiny5}
\put(0.7, 9.1){\tiny0}\put(2.03, 9.1){\tiny1}\put(3.36, 9.1){\tiny2}\put(4.69, 9.1){\tiny3}\put(6.02, 9.1){\tiny4}\put(7.35, 9.1){\tiny5}
\put(0.7, 11.1){\tiny0}\put(2.03, 11.1){\tiny1}\put(3.36, 11.1){\tiny2}\put(4.69, 11.1){\tiny3}\put(6.02, 11.1){\tiny4}\put(7.35, 11.1){\tiny5}
\put(0.7, 13.1){\tiny0}\put(2.03, 13.1){\tiny1}\put(3.36, 13.1){\tiny2}\put(4.69, 13.1){\tiny3}\put(6.02, 13.1){\tiny4}\put(7.35, 13.1){\tiny5}
\put(0.7, 15.1){\tiny0}\put(2.03, 15.1){\tiny1}\put(3.36, 15.1){\tiny2}\put(4.69, 15.1){\tiny3}\put(6.02, 15.1){\tiny4}\put(7.35, 15.1){\tiny5}
\put(0.7, 17.1){\tiny0}\put(2.03, 17.1){\tiny1}\put(3.36, 17.1){\tiny2}\put(4.69, 17.1){\tiny3}\put(6.02, 17.1){\tiny4}\put(7.35, 17.1){\tiny5}
\put(0.7, 19.1){\tiny0}\put(2.03, 19.1){\tiny1}\put(3.36, 19.1){\tiny2}\put(4.69, 19.1){\tiny3}\put(6.02, 19.1){\tiny4}\put(7.35, 19.1){\tiny5}

\put(12.4,17.1){\small$w_0^\prime$}
\put(10.4,13.1){\small$w_1$}\put(12.4,13.1){\small$w_1^\prime$}
\put(10.4,9.1){\small$w_2$}\put(12.4,9.1){\small$w_2^\prime$}\put(14.5,9.1){\small$s$}
\put(10.4,5.1){\small$w_{p-1}$}\put(12.4,5.1){\small$w_{p-1}^\prime$}
\put(10.4,1.1){\small$w_p$}

\put(11.75, 19.1){\tiny0}\put(13.35, 19.1){\tiny5}
\put(11.75, 17.4){\tiny1}\put(13.35, 17.4){\tiny2}

\put(9.75, 15.1){\tiny1}\put(11.35, 15.1){\tiny2}\put(11.75, 15.1){\tiny0}\put(13.35, 15.1){\tiny5}
\put(9.75, 13.4){\tiny0}\put(11.35, 13.4){\tiny5}\put(11.75, 13.4){\tiny1}\put(13.35, 13.4){\tiny2}

\put(9.75, 11.1){\tiny1}\put(11.35, 11.1){\tiny2}\put(11.75, 11.1){\tiny0}\put(13.35, 11.1){\tiny5}\put(13.75, 11.1){\tiny d}\put(15.35, 11.1){\tiny c }
\put(9.75, 9.4){\tiny0}\put(11.35, 9.4){\tiny5}\put(11.75, 9.4){\tiny1}\put(13.35, 9.4){\tiny2}\put(13.75, 9.4){\tiny a}\put(15.35, 9.4){\tiny b}

\put(9.75, 7.1){\tiny1}\put(11.35, 7.1){\tiny2}\put(11.75, 7.1){\tiny0}\put(13.35, 7.1){\tiny5}
\put(9.75, 5.4){\tiny0}\put(11.35, 5.4){\tiny5}\put(11.75, 5.4){\tiny1}\put(13.35, 5.4){\tiny2}

\put(9.75, 3.1){\tiny1}\put(11.35, 3.1){\tiny2}
\put(9.75, 1.4){\tiny0}\put(11.35, 1.4){\tiny5}


\end{overpic}
\caption{The tetradedra of~$\tau_{p}$ with $[w_0^\prime(01)]$ colored red.  All but $s$ are shown in the braid complement on the left.  The dashed arrows on the right indicate that a bottom face of the originating tetrahedron is identified through a half-twist to a top face of the target tetrahedron.  Among faces unpaired by half-twists, the top faces of $w_0^\prime$ are identified to the bottom faces of $w_p$ and $s$ is glued to the top faces of $w_1$ and $w_1^\prime$ and the bottom faces of $w_{p-1}$ and $w_{p-1}^\prime$ as in Table~\ref{table:anyp}.\label{fig:anyp}}
\end{figure}
