---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-005-22-a-foundational-ideal-triangulation
section_title: "A foundational ideal triangulation"
section_number: 2.2
pages: 4-7
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.972
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:p=1}

To specify the triangulation of $X_{1}$, we will place tetrahedra in a product region from which the 6-braid, $\sigma_1\sigma_4^{-1}$, has been removed.   The left diagram in Figure~\ref{fig:p=1} shows this region with the braid in the plane of the page, except near the crossings.  

The method of Appendix~\ref{app:seeing2-bridge} suggests using three layers of tetrahedra (one on either side of the two crossings).  Label the top, middle, and bottom layers $\Delta_t$, $\Delta_m$, and $\Delta_b$ (with $\Delta_t$ split into $\Delta_{tt}$ and $\Delta_{tb}$).  The six ideal tetrahedra that will triangulate the complement are shown in Figure~\ref{fig:p=1}:  $t_1^\prime$~and~$t_2^\prime$ in $\Delta_t$, $m_1$ and $m_2$ in $\Delta_m$, and $b_1$ and $b_2^\prime$ in $\Delta_b$, where a prime indicates that the tetrahedron is behind the plane of the page; the labels on the ideal vertices come from the labels on their punctures (0 through 5 when read left to right); and the \lq\lq top'' faces of a tetrahedron are above the \lq\lq bottom'' faces relative to the product region.  

The edges of the tetrahedra are drawn both in the braid complement on the left and in flattened versions in the center and on the right.  On the left,  layers are expanded by making two copies of the edges where the top of a tetrahedron meets the bottom, allowing the faces of the tetrahedra and their remaining edges to be seen more easily.  The flattened versions show just one copy of each edge. 

The tetrahedra $t_1^\prime$ and $t_2^\prime$ share the face 025, shaded orange on the left, and their flattened versions are drawn separately.  The pair $m_1$ and $m_2$ share only an edge (thickened in the center diagram), so their interiors do not overlap when flattened, and they can both be seen when drawn side-by-side.  The same is true for~$b_1$ and~$b_2^\prime$.

The left figure contains additional segments that divide the boundaries of each layer into triangles.  These curves appear gray in the diagram and will be useful in determining the face pairings for this initial triangulation, which we shall refer to as~$\hat{\tau}_1$.
\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{p=1light.pdf}\put(0.7, 1.1){\tiny0}\put(2.03, 1.1){\tiny1}\put(3.36, 1.1){\tiny2}\put(4.69, 1.1){\tiny3}\put(6.02, 1.1){\tiny4}\put(7.35, 1.1){\tiny5}
\put(0.7, 3.1){\tiny0}\put(2.03, 3.1){\tiny1}\put(3.36, 3.1){\tiny2}\put(4.69, 3.1){\tiny3}\put(6.02, 3.1){\tiny4}\put(7.35, 3.1){\tiny5}
\put(0.7, 5.1){\tiny0}\put(2.03, 5.1){\tiny1}\put(3.36, 5.1){\tiny2}\put(4.69, 5.1){\tiny3}\put(6.02, 5.1){\tiny4}\put(7.35, 5.1){\tiny5}
\put(0.7, 7.1){\tiny0}\put(2.03, 7.1){\tiny1}\put(3.36, 7.1){\tiny2}\put(4.69, 7.1){\tiny3}\put(6.02, 7.1){\tiny4}\put(7.35, 7.1){\tiny5}
\put(0.7, 9.1){\tiny0}\put(2.03, 9.1){\tiny1}\put(3.36, 9.1){\tiny2}\put(4.69, 9.1){\tiny3}\put(6.02, 9.1){\tiny4}\put(7.35, 9.1){\tiny5}
\put(0.7, 11.1){\tiny0}\put(2.03, 11.1){\tiny1}\put(3.36, 11.1){\tiny2}\put(4.69, 11.1){\tiny3}\put(6.02, 11.1){\tiny4}\put(7.35, 11.1){\tiny5}
\put(0.7, 13.1){\tiny0}\put(2.03, 13.1){\tiny1}\put(3.36, 13.1){\tiny2}\put(4.69, 13.1){\tiny3}\put(6.02, 13.1){\tiny4}\put(7.35, 13.1){\tiny5}

\put(7.8,1.9){\small$\Delta_b=$}\put(7.8,5.9){\small$\Delta_m=$}\put(7.8,9.9){\small$\Delta_{tb}=$}\put(7.8,11.9){\small$\Delta_{tt}=$}

\put(13.1,1.9){\small$=$}\put(13.1,5.9){\small$=$}\put(13.1,9.9){\small$=$}\put(13.1,11.9){\small$=$}

\put(14.4,11.1){\small$t_1^\prime$}
\put(16.4,9.1){\small$t_2^\prime$}
\put(14.4,5.1){\small$m_1$}\put(16.4,5.1){\small$m_2$}
\put(14.4,1.1){\small$b_1$}\put(16.4,1.1){\small$b_2^\prime$}

\put(9.1, 11.1){\tiny0}\put(9.766, 11.1){\tiny1}\put(10.432, 11.1){\tiny2}\put(11.098,11.1){\tiny3}\put(11.764, 11.1){\tiny4}\put(12.43, 11.1){\tiny5}
\put(9.1, 9.1){\tiny0}\put(9.766, 9.1){\tiny1}\put(10.432, 9.1){\tiny2}\put(11.098,9.1){\tiny3}\put(11.764, 9.1){\tiny4}\put(12.43, 9.1){\tiny5}
\put(9.1, 7.1){\tiny0}\put(9.766, 7.1){\tiny1}\put(10.432, 7.1){\tiny2}\put(11.098, 7.1){\tiny3}\put(11.764, 7.1){\tiny4}\put(12.43, 7.1){\tiny5}
\put(9.1, 2.43){\tiny0}\put(9.766, 2.43){\tiny1}\put(10.432, 2.43){\tiny2}\put(11.098, 2.43){\tiny3}\put(11.764, 2.43){\tiny4}\put(12.43, 2.43){\tiny5}

\put(13.75, 13.1){\tiny0}\put(15.35, 13.1){\tiny5}
\put(13.75, 11.4){\tiny2}\put(15.35, 11.4){\tiny3}

\put(15.75, 11.1){\tiny0}\put(17.35, 11.1){\tiny5}
\put(15.75, 9.4){\tiny1}\put(17.35, 9.4){\tiny2}

\put(13.75, 7.1){\tiny1}\put(15.35, 7.1){\tiny2}\put(15.75, 7.1){\tiny3}\put(17.35, 7.1){\tiny4}
\put(13.75, 5.4){\tiny0}\put(15.35, 5.4){\tiny5}\put(15.75, 5.4){\tiny2}\put(17.35, 5.4){\tiny5}

\put(13.75, 3.1){\tiny2}\put(15.35, 3.1){\tiny3}\put(15.75, 3.1){\tiny2}\put(17.35, 3.1){\tiny5}
\put(13.75, 1.4){\tiny0}\put(15.35, 1.4){\tiny5}\put(15.75, 1.4){\tiny3}\put(17.35, 1.4){\tiny4}


\end{overpic}
\caption{A triangulation of the complement of the closure of $C^2\sigma_1\sigma_2^{-1}$.\label{fig:p=1}}
\end{figure}

When comparing to Appendix~\ref{app:seeing2-bridge}, the reader should be concerned that the pairs of tetrahedra do not fill the entire layer.  In $\Delta_m$, for example, the tetrahedra are only in front of the plane of the page.  Nonetheless, if we slide the faces of these six tetrahedra around the link --- up and down the braid and through the full twists at the top and bottom --- they \emph{will} fill out the entire product region.  For example, face 235 on the bottom of $t_1^\prime$ can slide down the braid through $\Delta_{tb}$ and~$\Delta_m$ and past the $\sigma_4^{-1}$ half-twist to be identified with the 245 face of $b_2^\prime$.  We denote such faces and face pairings by:  
$$t_1^\prime(235)\sim b_2^\prime(245),$$
taking care that the order of the vertices indicates the correct match.  Images of the intersection of this triangle's path with each layer's boundary are shaded pink in the diagram.  They make use of the afore-mentioned additional gray segments and show that the back 235 region of $\Delta_m$ is indeed covered.  

As indicated in Figure~\ref{fig:p=1}, $t_1^\prime$ sits on top of $t_2^\prime$ with their  025 faces identified.  The remaining faces on the top of the tetrahedra in $\Delta_t$ and those on the bottom of the tetrahedra in $\Delta_b$ are triangles appearing in the previous section (\ref{sec:fulltwist}) and are identified by the full-twist identifications described there.  For example,  the face $b_1(023)$ on the bottom of $\Delta_b$ is the triangle $\triangle 023$, which is identified to $\triangle 523$, which is the 523 face of~$b_2^\prime$, another face on the bottom of~$\Delta_b$, so $b_1(023)\sim b_2^\prime(523)$.  These faces are shaded green.

Sometimes the full-twist identifications will combine with sliding along the braid.  To see such a combination, look at triangles shaded blue, starting with the 125 face of~$t_2^\prime$.  After traveling through the half-twist that interchanges 0 and 1, $t_2^\prime(125)$ becomes $\triangle 025$ on the top of $\Delta_m$ still in the back.  Then it can travel through $\Delta_m$ and $\Delta_b$ all the way to $\triangle 025$ on the bottom of $\Delta_b$ in the back.  This triangle is identified to $\triangle 035$ in the front, i.e., the 035 face of~$b_1$, so $t_2^\prime(125)\sim b_1(035)$.

The remaining face pairings of~$\hat{\tau}_1$ are obtained by sliding the remaining faces along the braid, twisting through half-twists and using full-twist identifications at the top and bottom as needed.  The reader may enjoy tracing the long and twisted journey of $t_2^\prime(012)$ to its mate, $m_1(021)$.  All twelve face pairings of~$\hat{\tau}_1$ are listed in Table~\ref{table:p=1prelim}.  

\begin{table}[ht]
\caption{Face pairings for~$\hat{\tau}_1$, an initial triangulation of $X_{1}$.\label{table:p=1prelim}\\}
\begin{tabular}{ |l c l|  }
 \hline
 $t_1^\prime(023)$    &$\sim$	&$m_2(523)$\\
  \hline
 $t_1^\prime(025)$    &$\sim$	&$t_2^\prime(025)$\\
  \hline
 $t_1^\prime(035)$    &$\sim$	&$m_1(125)$\\
  \hline
 $t_1^\prime(235)$    &$\sim$	&$b_2^\prime(245)$\\
  \hline
 $t_2^\prime(015)$    &$\sim$	&$m_1(105)$\\
  \hline
 $t_2^\prime(012)$    &$\sim$	&$m_1(021)$\\
  \hline
 $t_2^\prime(125)$    &$\sim$	&$b_1(035)$\\
  \hline
 $m_1(025)$    &$\sim$	&$b_1(025)$\\
  \hline
 $m_2(345)$    &$\sim$	&$b_2^\prime(354)$\\
  \hline
 $m_2(234)$    &$\sim$	&$b_2^\prime(243)$\\
  \hline
 $m_2(245)$    &$\sim$	&$b_1(235)$\\
  \hline
 $b_1(023)$    &$\sim$	&$b_2^\prime(523)$\\
 \hline
\end{tabular}
\end{table}

For reasons explained in~\ref{sec:veering}, the triangulation~$\hat{\tau}_1$ is not quite what we want for our triangulation of~$X_{1}$.  Instead, we  will simplify~$\hat{\tau}_1$ by applying Pachner moves (also known as bistellar flips, introduced in~\cite{Pachner}).  Table~\ref{table:p=1prelim} shows the following identifications of the 24 edge of $m_2$:
$$
24 \text{ in } m_2\sim 23 \text{ in } b_1\sim 23 \text{ in } b_2^\prime \sim_{\text{back to}}24 \text{ in } m_2.
$$
Whenever three tetrahedra surround an edge, we can perform a 3-2 Pachner move that replaces them with two tetrahedra sharing a face.  Figure~\ref{fig:3-2move} shows how to replace $m_2$, $b_1$, and $b_2^\prime$ with $\bar s$ on the top and $s$ on the bottom.  Label the vertices of $s$ with $abcd$ (circled in the diagram), where 
$a$~represents 3 in $m_2$ and 4 in $b_2^\prime$; 
$b$~represents 3 in $b_1$ and $b_2^\prime$ and 4 in $m_2$; 
$c$~represents 5 in $m_2$ and $b_1$; and 
$d$~represents 0 in $b_1$ and 5 in $b_2^\prime$.
The surviving faces of $m_2$, $b_1$, and $b_2^\prime$ are renamed as follows:
$m_2(235) \mapsto \bar s(2ac)$,
$m_2(345) \mapsto s(abc)$,
$b_1(025) \mapsto \bar s(d2c)$,
$b_1(035)  \mapsto s(dbc)$,
$b_2^\prime(245) \mapsto \bar s(2ad)$, and
$b_2^\prime(345) \mapsto s(bad)$.  
Making these substitutions and adding $\bar s(acd)\sim s(acd)$ yields the face pairings listed in Figure~\ref{fig:3-2move}.

\begin{figure}[ht]\vskip.25in
\begin{subfigure}{.4\textwidth}

\begin{overpic}[unit=.25in]{3-2move.pdf}
\put(1,1.7){\small$s$}\put(.9,5){\small$\bar s$}
\put(1.8,3.2){\small$m_2$}
\put(3.2,4.2){\begin{turn}{60}\small$b_2^\prime$\end{turn}}
\put(1.6,4){\begin{turn}{40}\reflectbox{\small$b_1$}\end{turn}}

\put(4.2,3){\tiny$a$}\put(2.2,.15){\tiny$b$}\put(.15,3){\tiny$c$}\put(3.6,5.73){\tiny$d$}

\put(2.2,6.45){\tiny2}

\put(2,.6){\begin{turn}{-55}\tiny4\end{turn}}
\put(2.3,.4){\begin{turn}{60}\tiny4\end{turn}}
\put(1.89,.85){\begin{turn}{-55}\tiny3\end{turn}}
\put(2.43,.65){\begin{turn}{60}\tiny3\end{turn}}

\put(3.9,3.25){\begin{turn}{60}\tiny4\end{turn}}
\put(3.8,2.95){\begin{turn}{60}\tiny3\end{turn}}

\put(.4,3.4){\begin{turn}{-55}\tiny5\end{turn}}
\put(.53,3.1){\begin{turn}{-55}\tiny5\end{turn}}

\put(3.2,5.6){\begin{turn}{-215}\tiny0\end{turn}}
\put(3.4,5.45){\begin{turn}{-215}\tiny5\end{turn}}


\end{overpic}
\end{subfigure}
\begin{subfigure}{.4\textwidth}{\begin{tabular}{ |l c l|  }
 \hline
 $t_1^\prime(023)$    &$\sim$	&$\bar s(c2a)$\\
  \hline
 $t_1^\prime(025)$    &$\sim$	&$t_2^\prime(025)$\\
  \hline
 $t_1^\prime(035)$    &$\sim$	&$m_1(125)$\\
  \hline
 $t_1^\prime(235)$    &$\sim$	&$\bar s(2ad)$\\
  \hline
 $t_2^\prime(015)$    &$\sim$	&$m_1(105)$\\
  \hline
 $t_2^\prime(012)$    &$\sim$	&$m_1(021)$\\
  \hline
 $t_2^\prime(125)$    &$\sim$	&$s(dbc)$\\
  \hline
 $m_1(025)$    &$\sim$	&$\bar s(d2c)$\\
  \hline
 $s(abc)$    &$\sim$	&$s(bda)$\\
  \hline
 $\bar s(acd)$    &$\sim$	&$s(acd)$\\
  \hline
 \end{tabular}
}
\end{subfigure}\caption{A 3-2 move eliminates the 24 edge of $m_2$, which is also the 23 edge in $b_1$ and $b_2^\prime$, and yields the indicated face pairings.}\label{fig:3-2move} 
\end{figure}

Next, observe that the 23 edge of $t_1^\prime$ is identified to the $2a$ edge of $\bar s$, which is taken back to the 23 edge of $t_1^\prime$.  This very short cycle of edges means $t_1^\prime$ and $\bar s$ are identified across an edge, so we can perform a 2-0 Pachner move to collapse~$t_1^\prime$ and~$\bar s$.  This move identifies  $t_1^\prime(025)$ with $\bar s(c2d)$ and $t_1^\prime(035)$ with $\bar s(cad)$.  See Figure~\ref{fig:2-0move}, which shows how~$t_1^\prime$ and~$\bar s$ are stacked before they are collapsed and eliminated.  The 2-0 move results in a triangulation of $X_{1}$ comprising three tetrahedra --- $t_2^\prime,$ $m_1,$ and $s$ --- whose face pairings are in Figure~\ref{fig:2-0move}.  Define~$\tau_{1}$ to be this triangulation.   

\begin{figure}[ht]\vskip.25in
\begin{subfigure}{.4\textwidth}

\begin{overpic}[unit=.25in]{2-0move.pdf}
\put(.6,1.2){\small$t_1^\prime$}\put(5,1.2){\small$\bar s$}

\put(1.75,5.7){\tiny5}\put(6.15,5.7){\tiny$d$}
\put(0,2.9){\tiny2}\put(3.4,2.9){\tiny3}\put(4.4,2.9){\tiny2}\put(7.8,2.9){\tiny$a$}
\put(1.75,0.1){\tiny0}\put(6.15,0.1){\tiny$c$}

\end{overpic}
\end{subfigure}
\quad
\begin{subfigure}{.4\textwidth}{\begin{tabular}{ |l c l|  }
 \hline
 $t_2^\prime(015)$    &$\sim$	&$m_1(105)$\\
  \hline
 $t_2^\prime(012)$    &$\sim$	&$m_1(021)$\\
  \hline
 $t_2^\prime(025)$    &$\sim$	&$m_1(520)$\\
 \hline 
 $t_2^\prime(125)$    &$\sim$	&$s(dbc)$\\
  \hline
 $m_1(125)$    &$\sim$	&$s(cad)$\\
 \hline
 $s(abc)$    &$\sim$	&$s(bda)$\\
  \hline
\end{tabular}
}
\end{subfigure}
\caption{A 2-0 move eliminates $t_1^\prime$ and $\bar s$, stacked as indicated, and yields face pairings for $\tau_1$, a triangulation of $X_1$.\label{fig:2-0move}}
\end{figure}
