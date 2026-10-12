---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-006-3-the-ptolemy-varieties
section_title: "The Ptolemy varieties"
section_number: 3
pages: 7-8
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by theA-coordinates on"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.833
---
\label{sec:PtolemyVariety}
We define the Ptolemy variety for $n=2$ following Garoufalidis--Thurston--Zickert~\cite{GaroufalidisThurstonZickert} (see also Garoufalidis--Goerner--Zickert~\cite{GaroufalidisGoernerZickert}).


\subsection{The $\SL(2,\C)$-Ptolemy variety}
Assign to each oriented edge $\varepsilon_{ij,k}$ of $\Delta_k\in \T$ a \emph{Ptolemy coordinate $c_{ij,k}$}. Consider the affine algebraic set $A$ defined by the \emph{Ptolemy relations}
\begin{equation}\label{eq:PtolemyRelationijk}
c_{03,k}c_{12,k}+c_{01,k}c_{23,k}=c_{02,k}c_{13,k}, \qquad k=1,2,\dots,t,
\end{equation}
the \emph{identification relations}
\begin{equation}\label{eq:IdentificationRelations}
c_{ij,k}=c_{i^\prime j^\prime,k^\prime}\qquad \text{when}\qquad \varepsilon_{ij,k}\sim\varepsilon_{i^\prime j^\prime,k^\prime},
\end{equation}
and the \emph{edge orientation relations} $c_{ij,k}=-c_{ji,k}$. By only considering $i<j$, we shall always eliminate the edge orientation relations.
\begin{definition}\label{def:PtolemyVariety} The \emph{Ptolemy variety} $P_2(\T)$ is the Zariski open subset of $A$ consisting of points with non-zero Ptolemy coordinates.
\end{definition}
\begin{remark} One can concretely obtain $P_2(\T)$ from $A$ by adding a dummy variable $x$ and a dummy relation $x\prod c_{ij,k}=1$.
\end{remark}

\begin{remark}\label{rm:PickRepresentative} We can eliminate the identification relations~\eqref{eq:IdentificationRelations} by selecting a representative for each edge cycle. This gives an embedding of the Ptolemy variety in an ambient space $\C^e$, where it is cut out by $s$ Ptolemy relations, one for each simplex. Note that when all boundary components are tori, $s=e$.
\end{remark}


\subsubsection{The figure-$8$ knot}
Consider the ideal triangulation of the figure-$8$ knot complement shown in Figure~\ref{fig:Fig8Ordered}. The Ptolemy variety $P_2(\T)$ is given by
\begin{equation}\label{eq:Fig8PtolemyUnsimplified}
\begin{aligned}[c]
c_{03,0}c_{12,0}+c_{01,0}c_{23,0}&=c_{02,0}c_{13,0},\\
c_{03,1}c_{12,1}+c_{01,1}c_{23,1}&=c_{02,1}c_{13,1},
\end{aligned}
\qquad 
\begin{aligned}[c]
c_{02,0}&=c_{12,0}=c_{13,0}=c_{01,1}=c_{03,1}=c_{23,1}\\
c_{01,0}&=c_{03,0}=c_{23,0}=c_{02,1}=c_{12,1}=c_{13,1}.
\end{aligned}
\end{equation}
By selecting representatives $\varepsilon_{23,0}$ and $\varepsilon_{13,0}$ for the $2$ edge cycles, $P_2(\T)$ embeds in $\C^2$ where it is given by
\begin{equation}\label{eq:Fig8PtolemyTrivial}
c_{23,0}c_{13,0}+c_{23,0}^2=c_{13,0}^2,\qquad c_{13,0}c_{23,0}+c_{13,0}^2=c_{23,0}^2.
\end{equation}
It follows that $P_2(\T)$ is empty, which is no surprise, since the only boundary-parabolic $\SL(2,\C)$-representations of the figure-$8$ knot are abelian. To detect the geometric representation, we need to consider \emph{obstruction classes} (see Section~\ref{sec:ObstructionClasses} below).


\subsubsection{The figure-$8$ knot sister}
Consider the ideal triangulation of the figure-$8$ knot sister shown in Figure~\ref{fig:Fig8SisOri}. The Ptolemy variety $P_2(\T)$ is given by
\begin{equation}\label{eq:Fig8SisPtolemyUnsimplified}
\begin{aligned}[c]
c_{03,0}c_{12,0}+c_{01,0}c_{23,0}&=c_{02,0}c_{13,0},\\
c_{03,1}c_{12,1}+c_{01,1}c_{23,1}&=c_{02,1}c_{13,1},
\end{aligned}
\qquad 
\begin{aligned}[c]
c_{01,0}=-c_{03,0}=c_{23,0}=-c_{01,1}=c_{03,1}=-c_{23,1}\\
c_{02,0}=-c_{12,0}=c_{13,0}=-c_{02,1}=c_{12,1}=-c_{13,1}
\end{aligned}
\end{equation}
Selecting representatives $\varepsilon_{23,0}$ and $\varepsilon_{13,0}$ for the $2$ edge cycles, $P_2(\T)\in\C^2$ is given by
\begin{equation}\label{eq:Fig8SisPtolemyTrivial}
c_{23,0}c_{13,0}+c_{23,0}^2=c_{13,0}^2,\qquad c_{23,0}c_{13,0}+c_{23,0}^2=c_{13,0}^2.
\end{equation}
This is equivalent to
\begin{equation}
x^2-x-1=0,\qquad x=\frac{c_{13,0}}{c_{23,0}}.
\end{equation}




\begin{figure}[htpb]
\centering
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.57}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(522.27557,212.41415)
 \put(0,0){\includegraphics{figures_gen/Fig8Triangulation_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(94.449251,12.219258){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{02,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(33.020681,129.362118){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{01,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(243.734971,116.504978){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{23,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(172.306401,219.362128){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{13,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(170.877821,118.647838){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{12,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(88.734971,123.647838){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{03,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(410.877831,220.076408){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{13,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(488.020691,129.362118){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{23,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(338.734971,12.219258){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{02,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(282.306391,135.790688){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{01,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(410.877821,118.647828){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{12,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(330.877831,125.790678){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{03,1}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Ordered triangulation of the figure $8$ knot. The signs indicate the non-trivial obstruction class.}\label{fig:Fig8Ordered}
\end{minipage}	
\hspace{2mm}
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.57}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(522.27557,212.41415)
 \put(0,0){\includegraphics{figures_gen/Fig8SisterTriangulation_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(173.458011,219.841498){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{13,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(418.925081,221.861818){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{13,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(337.276041,10.739918){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{02,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(488.625611,124.887168){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{23,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(277.503721,134.988688){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{01,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(413.874321,114.785638){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{12,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(330.031651,125.897318){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{03,1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(92.645821,10.862478){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{02,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(32.036651,130.948078){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{01,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(239.117931,111.755188){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{23,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(87.595051,123.877008){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{03,0}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(173.335481,115.795808){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\LARGE{$c_{12,0}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Oriented triangulation of the figure $8$ knot sister. The signs indicate the non-trivial obstruction class.}\label{fig:Fig8SisOri}
\end{minipage}					

\end{figure}
\begin{remark}
Note that for ordered triangulations, the identification relations~\eqref{eq:IdentificationRelations} do not involve minus signs. The triangulation in Figure~\ref{fig:Fig8Ordered} is not oriented.



\end{remark}
