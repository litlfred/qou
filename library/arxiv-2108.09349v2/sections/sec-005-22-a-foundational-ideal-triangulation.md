---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-005-22-a-foundational-ideal-triangulation
section_title: "A foundational ideal triangulation"
section_number: 2.2
pages: 4-10
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.976
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


\subsection{Adding layers to extend to $p=2$ and $3$} \label{sec:p=3}

It will be more instructive to first extend the construction of the previous section to $p=3$.  To triangulate the complement of the closure of $C^2\sigma_1^3\sigma_2^{-1}$, where there are four half-twists in the braid, begin with five layers:  $\Delta_t$, $\Delta_m$, and $\Delta_b$ and two layers inserted between $\Delta_t$ and $\Delta_m$, labelled $\Delta_{w1}$ and $\Delta_{w2}$.  Place two tetrahedra in each layer as indicated in Figure~\ref{fig:p=3}.  Though $\Delta_t$ is depicted slightly differently (as one layer with the shared face of $t_1^\prime$ and $t_2^\prime$, 025, positioned in the middle), all tetrahedra in $\Delta_t$, $\Delta_m$, and~$\Delta_b$ are named and situated exactly as in~Figure~\ref{fig:p=1}.  The new tetrahedra, those in the~$\Delta_{wi}$ layers, will be called $w_i$ and $w_i^\prime$, where a prime still indicates the tetrahedron is behind the plane of the page.

\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{p=3.pdf}
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

\put(8,2){\small$\Delta_b=$}\put(8,6){\small$\Delta_m=$}\put(8,10){\small$\Delta_{w2}=$}\put(8,14){\small$\Delta_{w1}=$}\put(8,18){\small$\Delta_t=$}

\put(10.4,17.1){\small$t_1^\prime$}\put(12.4,17.1){\small$t_2^\prime$}
\put(10.4,13.1){\small$w_1$}\put(12.4,13.1){\small$w_1^\prime$}
\put(10.4,9.1){\small$w_2$}\put(12.4,9.1){\small$w_2^\prime$}
\put(10.4,5.1){\small$m_1$}\put(12.4,5.1){\small$m_2$}
\put(10.4,1.1){\small$b_1$}\put(12.4,1.1){\small$b_2^\prime$}

\put(9.75, 19.1){\tiny0}\put(11.35, 19.1){\tiny5}\put(11.75, 19.1){\tiny0}\put(13.35, 19.1){\tiny5}
\put(9.75, 17.4){\tiny2}\put(11.35, 17.4){\tiny3}\put(11.75, 17.4){\tiny1}\put(13.35, 17.4){\tiny2}

\put(9.75, 15.1){\tiny1}\put(11.35, 15.1){\tiny2}\put(11.75, 15.1){\tiny0}\put(13.35, 15.1){\tiny5}
\put(9.75, 13.4){\tiny0}\put(11.35, 13.4){\tiny5}\put(11.75, 13.4){\tiny1}\put(13.35, 13.4){\tiny2}

\put(9.75, 11.1){\tiny1}\put(11.35, 11.1){\tiny2}\put(11.75, 11.1){\tiny0}\put(13.35, 11.1){\tiny5}
\put(9.75, 9.4){\tiny0}\put(11.35, 9.4){\tiny5}\put(11.75, 9.4){\tiny1}\put(13.35, 9.4){\tiny2}

\put(9.75, 7.1){\tiny1}\put(11.35, 7.1){\tiny2}\put(11.75, 7.1){\tiny3}\put(13.35, 7.1){\tiny4}
\put(9.75, 5.4){\tiny0}\put(11.35, 5.4){\tiny5}\put(11.75, 5.4){\tiny2}\put(13.35, 5.4){\tiny5}

\put(9.75, 3.1){\tiny2}\put(11.35, 3.1){\tiny3}\put(11.75, 3.1){\tiny2}\put(13.35, 3.1){\tiny5}
\put(9.75, 1.4){\tiny0}\put(11.35, 1.4){\tiny5}\put(11.75, 1.4){\tiny3}\put(13.35, 1.4){\tiny4}


\end{overpic}
\caption{A triangulation of the complement of the closure of $C^2\sigma_1^3\sigma_2^{-1}$, with $\Delta_t$ depicted as one layer with the shared face of $t_1^\prime$ and $t_2^\prime$, 025, positioned in the middle.\label{fig:p=3}}
\end{figure}

The face pairings are determined in the same manner as they were for $p=1$, but now over half of the twenty face pairings result from moving through a half-twist from the bottom of one layer to the top of the next.  These appear in the left column of Table~\ref{table:p=3prelim}.  The middle column contains the face pairings that come directly from Table~\ref{table:p=1prelim}  and are unaffected by adding the $w$-layers.  The final column contains more complicated face pairings that do not occur in Table~\ref{table:p=1prelim} because these triangles hit tetrahedra in the $w$-layers before encountering their mates  from Table~\ref{table:p=1prelim}.  For example,  $t_1^\prime(035)$ is identified to $\triangle 025$ in the front, which, after passing through the half-twist, becomes $\triangle 125$, a top face of $w_1$, so $t_1^\prime(035)$ hits  $w_1$ before it gets to $m_1$.  We will call this initial triangulation~$\hat{\tau}_3$, and, as in the $p=1$ case, will perform simplifying Pachner moves on $\hat{\tau}_3$ to create $\tau_{3}$.  The shadings in Table~\ref{table:p=3prelim} will help us determine the resulting identifications.
\begin{table}[ht]
\caption{Face pairings for $\hat{\tau}_3$, an initial triangulation of $X_3$.\label{table:p=3prelim}}
\definecolor{lightgray}{gray}{0.8}
\begin{tabular}{ |l c l|  }
  \hline
\rowcolor{White} $t_2^\prime(015)$    &$\sim$	&$w_1(105)$\\
  \hline
 \rowcolor{White} $t_2^\prime(125)$    &$\sim$	&$w_1^\prime(025)$\\
  \hline
\rowcolor{White}   $w_1(025)$    &$\sim$	&$w_2(125)$\\
  \hline
\rowcolor{White}  $w_1(012)$    &$\sim$	&$w_2^\prime(102)$\\
  \hline
\rowcolor{White} $w_1^\prime(015)$    &$\sim$	&$w_2(105)$\\
  \hline
\rowcolor{White}  $w_1^\prime(125)$    &$\sim$	&$w_2^\prime(025)$\\
  \hline
\rowcolor{White}  $w_2(025)$    &$\sim$	&$m_1(125)$\\
 \hline
\rowcolor{White}  $w_2^\prime(015)$    &$\sim$	&$m_1(105)$\\
 \hline
\rowcolor{lightgray}  $m_1(025)$    &$\sim$	&$b_1(025)$\\
  \hline
\rowcolor{Gray}  $m_2(234)$    &$\sim$	&$b_2^\prime(243)$\\
  \hline
\rowcolor{Gray}   $m_2(245)$    &$\sim$	&$b_1(235)$\\
  \hline
\end{tabular}\quad
\begin{tabular}{ |l c l|  }
 \hline
\rowcolor{Gray}   $t_1^\prime(023)$    &$\sim$	&$m_2(523)$\\
  \hline
 \rowcolor{lightgray}  $t_1^\prime(025)$    &$\sim$	&$t_2^\prime(025)$\\
  \hline
\rowcolor{Gray}    $t_1^\prime(235)$    &$\sim$	&$b_2^\prime(245)$\\
  \hline
 \rowcolor{White}  $t_2^\prime(012)$    &$\sim$	&$m_1(021)$\\
  \hline
\rowcolor{Gray}   $b_1(023)$    &$\sim$	&$b_2^\prime(523)$\\
 \hline
\end{tabular}\quad
\begin{tabular}{ |l c l|  }
 \hline
  \rowcolor{lightgray}  $t_1^\prime(035)$    &$\sim$	&$w_1(125)$\\
  \hline
 \rowcolor{lightgray}   $m_2(345)$    &$\sim$	&$w_1^\prime(201)$\\
  \hline
 \rowcolor{lightgray}  $b_1(035)$    &$\sim$	&$w_2^\prime(125)$\\
 \hline
\rowcolor{lightgray}   $b_2^\prime(345)$    &$\sim$	&$w_2(201)$\\
 \hline
\end{tabular}
\end{table}


Again, three tetrahedra in $\hat{\tau}_3$ surround the 24 edge of $m_2$ (which is identified to the 23 edges of $b_1$ and $b_2^\prime$), allowing for the same 3-2 move  shown in Figure~\ref{fig:3-2move}.  Thus  $m_2$, $b_1$, and $b_2^\prime$ are replaced by $\bar s$ and $s$.  As before, we can then perform a 2-0  move collapsing $t_1^\prime$ and $\bar s$ because they are identified across the edge $23=2a$.  Again,  $t_1^\prime(025)$ and $t_1^\prime(035)$ are identified with $\bar s(c2d)$ and $\bar s(cad)$ as in Figure~\ref{fig:2-0move}.  Let~$\tau_{3}$ be the resulting triangulation of $X_3$, consisting of the seven remaining tetrahedra: $t_2^\prime$, $w_1$, $w_1^\prime$, $w_2$, $w_2^\prime$, $m_1$, and~$s$.

The face pairings in the darkest cells in Table~\ref{table:p=3prelim}  involve only the four replaced or collapsed tetrahedra ($m_2$, $b_1$, $b_2^\prime$, $t_1^\prime$), so none of them will survive the Pachner moves defining~$\tau_{3}$.  The face pairings in the unshaded cells, on the other hand, do not involve any of these tetrahedra, and are, thus, unaffected by the two Pachner moves.  

The remaining face pairings of~$\tau_{3}$ come from those in the light gray cells in Table~\ref{table:p=3prelim}.  They involve the faces of $m_2$, $b_1$, $b_2^\prime$, and~$t_1^\prime$ that survive the Pachner moves.  In other words, these faces do appear in~$\tau_{3}$.  They are just relabelled by the Pachner moves.  Consider first $m_1(025)\sim b_1(025)$.  Under the 3-2 move shown in Figure~\ref{fig:3-2move},  $b_1(025)$ becomes  $\bar s(d2c)$, which is identified by the 2-0 move in Figure~\ref{fig:2-0move} to $t_1^\prime(520)$.  This face is  paired with $t_2^\prime(520)$, so, after the two Pachner moves, $m_1(025)$ is identified with $t_2^\prime(520)$, which we choose to write as $t_2^\prime(025)\sim m_1(520)$.  

The final four faces to be relabelled --- $t_1^\prime(035)$, $m_2(345)$, $b_1(035)$, and $b_2^\prime(345)$ --- are all faces that belong to the new tetrahedra $s$.  More specifically, the 2-0 move identifies $t_1^\prime(035)$ with $\bar s(cad)$, which is the new face introduced by the 3-2 move, the face shared by $\bar s$ and $s$.  Thus, after the two Pachner moves, $t_1^\prime(035)$ becomes $s(cad)$.  The other three faces form the rest of $s$ as indicated in Figure~\ref{fig:3-2move} and are thus the faces $s(abc)$, $s(dbc)$, and $s(bad)$, respectively.  Table~\ref{table:p=3} contains all identifications of~$\tau_{3}$, where the first column still lists face pairings that result from moving from the bottom of one layer to the top of the next and the final column now shows how the new tetrahedron, $s$, glues in. 

\begin{table}[ht]
\caption{Face pairings for~$\tau_{3}$, a triangulation of $X_3$.\label{table:p=3}}
\begin{tabular}{ |l c l|  }
   \hline
$t_2^\prime(015)$    &$\sim$	&$w_1(105)$\\
  \hline
$t_2^\prime(125)$    &$\sim$	&$w_1^\prime(025)$\\
  \hline
$w_1(025)$    &$\sim$	&$w_2(125)$\\
  \hline
 $w_1(012)$    &$\sim$	&$w_2^\prime(102)$\\
  \hline
$w_1^\prime(015)$    &$\sim$	&$w_2(105)$\\
  \hline
 $w_1^\prime(125)$    &$\sim$	&$w_2^\prime(025)$\\
  \hline
  $w_2(025)$    &$\sim$	&$m_1(125)$\\
 \hline
$w_2^\prime(015)$    &$\sim$	&$m_1(105)$\\
 \hline 
 \end{tabular}\quad
\begin{tabular}{ |l c l|  }
 \hline
 $t_2^\prime(012)$    &$\sim$	&$m_1(021)$\\
  \hline
 $t_2^\prime(025)$    &$\sim$	&$m_1(520)$\\
  \hline
 \end{tabular}
 \quad
\begin{tabular}{ |l c l|  }
 \hline
$s(cad)$    &$\sim$	&$w_1(125)$\\
  \hline
$s(abc)$    &$\sim$	&$w_1^\prime(201)$\\
  \hline
$s(dbc)$    &$\sim$	&$w_2^\prime(125)$\\
 \hline
$s(bad)$    &$\sim$	&$w_2(201)$\\
 \hline
\end{tabular}
\end{table}

The reader likely anticipates that we will create the desired triangulation of~$X_{p}$ in two steps:   First form an initial triangulation, $\hat{\tau}_p$, consisting of the tetrahedra in Figure~\ref{fig:p=1} together with some $w$-layers between $\Delta_t$ and $\Delta_m$ and then perform two Pachner moves --- a correct guess that will be made explicit in the next section.  Before moving on, we make some observations about the $p=3$ construction and address the $p=2$ case.

Figure~\ref{fig:p=3} shows that $t_2^\prime$ is situated and labelled in exactly the same way as $w_1^\prime$ and~$w_2^\prime$, so the labels on the bottom faces of $t_2^\prime$, 015 and 125, are the same as those on $w_1^\prime$ and~$w_2^\prime$.  Furthermore, as the face $t_2^\prime(015)$ slides through the half-twist, it rotates to the front, matching with $w_1(105)$, just as the 015 face of $w_1^\prime$ matches with $w_2(105)$.  Similarly, as the face $t_2^\prime(125)$ slides through the half-twist, it stays in the back, matching with $w_1^\prime(025)$, just as the the 125 face of $w_1^\prime$ matches with $w_2^\prime(025)$.  In these identifications, $t_2^\prime$ is acting as a tetrahedron labelled $w_0^\prime$ would.  A similar analysis at the bottom of the $w$-layers shows that the top faces of $m_1$ glue to the bottom faces of $w_2$ in the same way those in a tetrahedron labelled $w_3$ would.

Using this relabelling, we make several observations about the face pairings in~$\tau_{3}$.

\begin{itemize}

\item
By relabelling $t_2^\prime$ as $w_0^\prime$ and $m_1$ as $w_3$, the unshaded face pairings in the first column of Table~\ref{table:p=3prelim} can be summarized as follows:
\begin{center}
\begin{tabular}{ l c l l  }

$w_i^\prime(015)$    &$\sim$	&$w_{i+1}(105)$	&for $i=0,1,2$;\\

 $w_i^\prime(125)$    &$\sim$	&$w_{i+1}^\prime(025)$	&for $i=0,1$;\\

$w_i(025)$    &$\sim$	&$w_{i+1}(125)$	&for $i=1,2$; and\\

$w_i(012)$    &$\sim$	&$w_{i+1}^\prime(102)$	&for $i=1$.\\



 \end{tabular}
\end{center}
These inter-$w$ identifications of $\hat{\tau}_3$ are not affected by Pachner moves involving $m_2$, $b_1$, $b_2^\prime$, and~$t_1^\prime$, so they are also face pairings of~$\tau_{3}$, as shown in the first column of Table~\ref{table:p=3}.

\item
The top faces of $w_0^\prime$ are not included in the identifications listed above, and neither are the bottom faces of $w_3$.  These faces are identified to each other.  More specifically, after the Pachner moves, $w_0^\prime(012)\sim w_3(021)$ and $w_0^\prime(025)\sim w_3(520)$.  Both of these pairings also occur in~$\tau_{1}$ (see the table in Figure~\ref{fig:2-0move}) and were, thus, unaffected by the addition of the $w$-layers.  These face pairings appear in the second column of Table~\ref{table:p=3}.


\item
The face pairings in the third column of Table~\ref{table:p=3}, those involving~$s$, can be characterized as follows:  Two of the faces of $s$ are identified to top faces in the first $w$-layer, $w_1(125)$ and $w_1^\prime(201)$, and the other two are identified to bottom faces in the last $w$-layer, $w_2(201)$ and $w_2^\prime(125)$.
\end{itemize}

Properly interpreted, these observations also apply when $p=2$.  Let the triangulation~$\tau_{2}$ of $X_{2}$, the complement of the closure of $C^2\sigma_1^2\sigma_2^{-1}$, consist of $w_0^\prime$, $w_1$, $w_1^\prime$, $w_2$, and $s$.  Because there is only one $w$-layer, it is both the first $w$-layer and the last $w$-layer, and the final observation tells us that the faces of $s$ are identified to four faces in~$\Delta_{w1}$.  Harvesting the remaining face pairings from the first two observations, we obtain the face pairings for~$\tau_{2}$ given in Table~\ref{table:p=2}.


\begin{table}[ht]
\caption{Face pairings for~$\tau_{2}$, a triangulation of $X_{2}$.\label{table:p=2}}
\begin{tabular}{ |l c l|  }
   \hline
$w_0^\prime(015)$    &$\sim$	&$w_1(105)$\\
  \hline
$w_0^\prime(125)$    &$\sim$	&$w_1^\prime(025)$\\
  \hline
$w_1(025)$    &$\sim$	&$w_2(125)$\\
  \hline
$w_1^\prime(015)$    &$\sim$	&$w_2(105)$\\
  \hline
 \end{tabular}\quad
\begin{tabular}{ |l c l|  }
 \hline
 $w_0^\prime(012)$    &$\sim$	&$w_2(021)$\\
  \hline
 $w_0^\prime(025)$    &$\sim$	&$w_2(520)$\\
  \hline
 \end{tabular}\quad
\begin{tabular}{ |l c l|  }
 \hline
$s(cad)$    &$\sim$	&$w_1(125)$\\
  \hline
$s(abc)$    &$\sim$	&$w_1^\prime(201)$\\
  \hline
$s(dbc)$    &$\sim$	&$w_1^\prime(125)$\\
 \hline
$s(bad)$    &$\sim$	&$w_1(201)$\\
 \hline
\end{tabular}
\end{table}
