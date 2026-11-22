---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-002-12-decorated-sl2c-representations
section_title: "Decorated SL(2,C)-representations"
section_number: 1.2
pages: 2-4
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.85
latex_coverage_ratio: 0.944
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
\label{sub.decorated}

The precise relationship between Ptolemy assignments and representations is given by
\begin{equation}\label{eq:summaryof1to1}
\xymatrix{\left\{\txt{Points in\\$P_2(\T)$}\right\}\ar@{<->}[r]^-{1-1}&\left\{\txt{Natural $(\SL(2,\C),P)$-\\cocycles on $M$}\right\}\ar@{<->}[r]^-{1-1}&\left\{\txt{Generically decorated\\
$(\SL(2,\C),P)$-representations}\right\}.}
\end{equation}
The concepts are briefly described below, and the correspondences are illustrated in Figures~\ref{fig:DecToPtolemy} and~\ref{fig:PtolemyToCocycle}. We refer to Section~\ref{sec:Notation} for a summary of our notation.
The bijections of~\eqref{eq:summaryof1to1} first appeared in Zickert~\cite{ZickertDuke} (in a slightly different form), and were generalized to $\SL(n,\C)$-representations in Garoufalidis--Thurston--Zickert~\cite{GaroufalidisThurstonZickert}. 

\begin{itemize}[itemsep=1mm]


\item \textit{Natural cocycle:} Labeling of the edges of each truncated simplex by elements in $\SL(2,\C)$ satisfying the cocycle condition (the product around each face is $1$). The long edges are counter diagonal, i.e.~of the form $\left(\begin{smallmatrix}0&-x^{-1}\\x&0\end{smallmatrix}\right)$, and the short edges are \emph{non-trivial} elements in $P$. Identified edges are labeled by the same group element.
\item \textit{Decorated representation:} A \emph{decoration} of a boundary-parabolic representation $\rho$ is an assignment of a coset $gP$ to each vertex of $\Mtildehat$ which is equivariant with respect to $\rho$. A decoration is \emph{generic} if for each edge joining two vertices, the two $P$-cosets $gP$, $hP$ are distinct as $B$-cosets. This condition is equivalent to $\det(ge_1,he_1)\neq 0$. Two decorations are considered equal if they differ by left multiplication by a group element $g$.
\end{itemize}

































































\begin{figure}[htb]
\begin{center}
\hspace{-30mm}
\begin{minipage}[c]{0.3\textwidth}
\scalebox{0.65}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(327.29865,196.42032)
 \put(0,0){\includegraphics{figures_gen/BasicPtolemy_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(72.834381,14.946098){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{02}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(200.606421,122.756458){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{23}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(22.034991,114.899308){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{01}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(126.320711,107.756458){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{12}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(109.177841,133.470748){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{03}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(133.463561,192.042178){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.560208pt}
\textcolor{inkcol1}{\Large{$c_{13}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hspace{-10mm}
\begin{minipage}[c]{0.3\textwidth}
\scalebox{0.65}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(234.20671,190.59085)
 \put(0,0){\includegraphics{figures_gen/TruncatedCocycle_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(134.850526,94.132236){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\alpha$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(80.534436,115.037126){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\beta$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}

\begin{minipage}[c]{0.3\textwidth}
\scalebox{0.62}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(466.72302,188.14412)
 \put(0,0){\includegraphics{figures_gen/PtolemyToCocycleShort_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-4.751029,22.196066){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$i$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(89.68401,195.207626){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(180.09267,21.966456){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$k$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(28.0647,120.024306){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$c_{ij}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(131.30331,119.758676){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$c_{jk}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(74.22969,14.702816){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$c_{ki}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(206.12483,21.323636){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$i$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(304.60049,193.325046){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(396.77039,22.471536){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$k$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(305.04954,117.233296){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\LARGE{${\beta\!=\!\left(\begin{smallmatrix}1&-\frac{c_{ki}}{c_{ij}c_{jk}}\\0&1\end{smallmatrix}\right)}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(135.5529,177.711596){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\LARGE{${\alpha\!=\!\left(\begin{smallmatrix}0&-c_{ij}^{-1}\\c_{ij}&0\end{smallmatrix}\right)}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(262.66347,88.343146){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\alpha$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(300.24217,130.696496){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\beta$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\\
\hspace{-20mm}
\begin{minipage}[t]{0.32\textwidth}
\captionsetup{width=1\textwidth}
\caption{Ptolemy assignment; the Ptolemy relation~\eqref{eq:PtolemyRelation} holds.}\label{fig:Ptolemy}
\end{minipage}
\hspace{-10mm}
\begin{minipage}[t]{0.32\textwidth}
\captionsetup{width=\textwidth}
\caption[Bla]{Natural cocycle; $\alpha$ is counter-diagonal, $\beta\in P$.}\label{fig:Cocycle}
\end{minipage}
\hspace{5mm}
\begin{minipage}[t]{0.32\textwidth}
\captionsetup{width=\textwidth}
\caption[Bla]{From Ptolemy assignments to natural cocycles.}\label{fig:PtolemyToCocycle}
\end{minipage}
\end{center}
\end{figure}


\begin{figure}[htb]
\begin{center}
\hspace{4mm}
\begin{minipage}[c]{0.3\textwidth}
\scalebox{0.7}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(314.1539,200.47701)
 \put(0,0){\includegraphics{figures_gen/Decoration_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.058597,177.913786){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$g_1P$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.625263,14.222236){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$g_0P$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(184.302827,16.357046){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$g_2P$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(228.333317,203.419946){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$g_3P$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.63}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(356.2648,197.84821)
 \put(0,0){\includegraphics{figures_gen/DecorationToPtolemy_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(94.080375,203.534216){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$g_jP$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.205343,19.248506){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$g_iP$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(158.653195,23.133176){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$i$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(254.367485,202.418896){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(216.429985,102.878696){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{${c_{ij}=\det(g_ie_1,g_je_1)}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\\
\begin{minipage}[t]{0.48\textwidth}
\captionsetup{width=1\textwidth}
\caption{Decoration; equivariant assignment of cosets.}\label{fig:Decoration}
\end{minipage}
\hspace{-2mm}
\begin{minipage}[t]{0.48\textwidth}
\captionsetup{width=\textwidth}
\caption[Bla]{From decorations to Ptolemy assignments.}\label{fig:DecToPtolemy}
\end{minipage}

\end{center}
\end{figure}



By ignoring the decoration, \eqref{eq:summaryof1to1} yields a map
\begin{equation}\label{eq:PtolemyToRep}
\mathcal R\colon P_2(\T)\to \big\{(\SL(2,\C),P)\text{-representations}\big\}
\big/\Conj.
\end{equation}
The representation corresponding to a Ptolemy assignment is given explicitly in terms of the natural cocycle.

\begin{remark}
Note that a natural cocycle canonically determines a representation of the edge path groupoid of the triangulation of $M$ by truncated simplices.
\end{remark}

\begin{remark} 
Every boundary-parabolic representation has a decoration, but a representation may have only non-generic decorations. 
The map $\mathcal R$ is thus not surjective in general, and the image depends on the triangulation. However, if the triangulation is sufficiently fine, 
$\mathcal R$ is surjective (see~\cite{GaroufalidisThurstonZickert}). The preimage of a representation depends on the image of the peripheral subgroups (see Proposition~\ref{prop:GenericBoundaryNonTrivial}).\end{remark}
