---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
text_source: latex
latex_prose_ratio: 0.654
latex_coverage_ratio: 0.891
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by theA-coordinates on"
---
\subsection{The Ptolemy coordinates}
\label{sub.ge}

The Ptolemy coordinates for boundary-unipotent representations of a 
3-manifold group in $\SL(n,\C)$ were introduced in 
Garoufalidis--Thurston--Zickert~\cite{GaroufalidisThurstonZickert} inspired by the $\mathcal A$-coordinates 
on higher Teichm\"{u}ller space due to Fock and Goncharov
\cite{FockGoncharov}. In this paper we will focus primarily on representations in $\SL(2,\C)$ and $\PSL(2,\C)$.  


Given a topological ideal triangulation $\T$ of an oriented compact 3-manifold $M$, 
a \emph{Ptolemy assignment} (for $\SL(2,\C)$) is an assignment of a non-zero 
complex number (called a \emph{Ptolemy coordinate}) to each $1$-cell of $\CT$, such that for each simplex, the Ptolemy coordinates assigned to the edges $\varepsilon_{ij}$
satisfy the \emph{Ptolemy relation}
\begin{equation}\label{eq:PtolemyRelation}
c_{03}c_{12}+c_{01}c_{23}=c_{02}c_{13}.
\end{equation}
The set of Ptolemy assignments is thus an affine variety $P_2(\T)$, which is cut out by homogeneous quadratic polynomials. 

In this paper we define the Ptolemy field of a boundary-unipotent representation and show that it is isomorphic to the trace field. This gives rise to an efficient algorithm for \emph{exact} computation of the trace field of a hyperbolic manifold.







 



\subsection{Decorated $\SL(2,\BC)$-representations}
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



\subsection{Obstruction classes and $\PSL(2,\C)$-representations}
There is a subtle distinction between representations in $\SL(2,\C)$ versus $\PSL(2,\C)$. The geometric representation of a hyperbolic manifold always lifts to an $\SL(2,\C)$-representation, but for a one-cusped manifold, no lift is boundary-parabolic (any lift will take a longitude to an element of trace $-2$~\cite{Calegari}). 

The obstruction to lifting a boundary-parabolic $\PSL(2,\C)$-representation to a boundary-parabolic $\SL(2,\C)$-representation is a class in $H^2(\widehat M;\Z/2\Z)$. For each such class there is a Ptolemy variety $P^\sigma_2(\T)$, which maps to the set of $\PSL(2,\C)$-representations with obstruction class $\sigma$. More precisely, $P^\sigma_2(\T)$ is defined for each $2$-cocycle $\sigma\in Z^2(\widehat M;\Z/2\Z)$, and up to canonical isomorphism only depends on the cohomology class of $\sigma$. The Ptolemy variety for the trivial cocycle equals $P_2(\T)$. The analogue of~\eqref{eq:summaryof1to1} is
\begin{equation}\label{eq:1to1Obstruction}
\xymatrix{\left\{\txt{Points in\\$P^{\sigma}_2(\T)$}\right\}\ar@{<->}[r]^-{1-1}&\left\{\txt{Lifted natural\\$(\PSL(2,\C),P)$-cocycles\\with obstruction cocycle $\sigma$}\right\}\ar@{->>}[r]&\left\{\txt{Generically decorated\\
$(\PSL(2,\C),P)$-representations\\with obstruction class $\sigma$}\right\}.}
\end{equation}
A lifted natural cocycle is defined as above, except that the product along a face is now $\pm I$, where the sign is determined by $\sigma$. The right map is no longer a $1$-$1$ correspondence; the preimage of each decorated representation is the choice of lifts, i.e.~parametrized by a cocycle in $Z^1(\widehat M;\Z/2\Z)$. We refer to \cite{GaroufalidisThurstonZickert} for details. As in~\eqref{eq:PtolemyToRep}, ignoring the decoration yields a map
\begin{equation}\label{eq:PtolemyToRepObstruction}
\mathcal R\colon P_2^{\sigma}(\T)\to \left\{\txt{$(\PSL(2,\C),P)$-representations\\with obstruction class $\sigma$}\right\}
\big/\Conj.
\end{equation}
which is explictly given in terms of the natural cocycle.
\begin{theorem}[Garoufalidis--Thurston--Zickert~\cite{GaroufalidisThurstonZickert}]\label{thm:EssentialEdges}
If $M$ is hyperbolic, and all edges of $\T$ are essential, the geometric representation is in the image of $\mathcal R$.
\end{theorem}
\begin{remark}
If $\T$ has a non-essential edge, all Ptolemy varieties will be empty. Hence, if $P^\sigma_2(\T)$ is non-empty for some $\sigma$, and if $M$ is hyperbolic, the geometric representation is detected by the Ptolemy variety of the geometric obstruction class.
\end{remark}


\subsection{Our results}
We view the Ptolemy varieties $P^\sigma_2(\T)$ as subsets of an ambient space $\C^e$, with coordinates indexed by the $1$-cells of $\T$. Let $T=(\C^*)^v$, with the coordinates indexed by the boundary components of $M$. 

\begin{definition} The \emph{diagonal action} is the action of $T$ on $P^\sigma_2(\T)$ where $(x_1,\dots,x_v)\in T$ acts on a Ptolemy assignment by replacing the Ptolemy coordinate $c$ of an edge $e$ with $x_ix_jc$, where $x_i$ and $x_j$ are the coordinates corresponding to the ends of $e$. Let 
\begin{equation}
P^\sigma_2(\T)_\rd=P^\sigma_2(\T)\big/T.
\end{equation}
\end{definition}


\begin{definition}
A boundary-parabolic $\PSL(2,\C)$-representation is \emph{generic} if it has a generic decoration. It is \emph{boundary-non-trivial} if each peripheral subgroup has non-trivial image.
\end{definition}
\begin{remark}
Note that the notion of genericity is with respect to the triangulation. By Theorem~\ref{thm:EssentialEdges}, if all edges of $\T$ are essential (and $\T$ has no interior vertices), the geometric representation of a cusped hyperbolic manifold is always generic and boundary-non-trivial.
\end{remark}
\begin{remark}
Note that if $M$ has spherical boundary components (e.g.~if $\T$ is a triangulation of a closed manifold), no representation is boundary-non-trivial.
\end{remark}

\begin{proposition}\label{prop:GenericBoundaryNonTrivial}
The map $\mathcal R$ in~\eqref{eq:PtolemyToRepObstruction} factors through $P_2^{\sigma}(\T)_{\rd}$, i.e.,~we have
\begin{equation}\label{eq:GenericBoundaryNonTrivial}
\cxymatrix{{\mathcal R\colon P_2^{\sigma}(\T)_{\rd}\ar@{->}[r]& \left\{\txt{$(\PSL(2,\C),P)$-representations\\with obstruction class $\sigma$}\right\}\big/\Conj.}}
\end{equation}
The image is the set of generic representations, and the preimage of a generic, boundary-non-trivial representation is finite and parametrized by $H^1(\widehat M;\Z/2\Z)$. 
\end{proposition}
\begin{remark}
For the corresponding map from $P_2(\T)_\rd$ to $(\SL(2,\C),P)$-representations, the preimage of a generic boundary-non-trivial representation is a single point.
\end{remark}

\begin{remark}\label{rm:HigherComponents}
The preimage of a representation which is not boundary-non-trivial is never finite. In fact its dimension is the number of boundary-components that are collapsed. In particular, it follows that if $c\in P_2^{\sigma}(\T)_{\rd}$ is in a $0$-dimensional component (which is not contained in a higher dimensional component), the image is boundary-non-trivial.
\end{remark}

By geometric invariant theory, $P^\sigma_2(\T)_\rd$ is a variety whose coordinate ring is the ring of invariants $\mathcal O^T$ of the coordinate ring $\mathcal O$ of $P^\sigma_2(T)$.

\begin{definition}\label{def:PtolemyField}
Let $c\in P^\sigma_2(\T)$. The Ptolemy field of $c$ is the field
\begin{equation}
k_c=\Q\left(\big\{p(c_1,\dots,c_e)\mid p\in\mathcal O^T\big\}\right).
\end{equation}
The Ptolemy field of a generic boundary-non-trivial representation is the Ptolemy field of any preimage under~\eqref{eq:GenericBoundaryNonTrivial}.
\end{definition}
Clearly, the Ptolemy field only depends on the image in $P^\sigma_2(\T)_\rd$. Our main result is the following.
\begin{theorem}\label{thm:PtolemyFieldEqualsTraceField}
The Ptolemy field of a boundary-non-trivial, generic, boundary-parabolic representation $\rho$ in $\PSL(2,\C)$ or $\SL(2,\C)$ is equal to its trace field.\qed
\end{theorem}
\begin{remark}
For a cusped hyperbolic $3$-manifold the \emph{shape field} is in general smaller than the trace field. The shape field equals the \emph{invariant trace field} (see, e.g.,~\cite{MaclachlanReid}).
\end{remark}
For computations of the Ptolemy field, we need an explicit description of the ring of invariants $\mathcal O^T$, or equivalently, the reduced Ptolemy variety $P^\sigma_2(\T)_\rd$.

\begin{proposition}\label{prop:FixDecoration}
There exist $1$-cells $\varepsilon_1,\dots,\varepsilon_v$ of $\T$ such that the reduced Ptolemy variety $P_2^{\sigma}(\T)_{\rd}$ is naturally isomorphic to the subvariety of $P^\sigma_2(\T)$ obtained by intersecting with the affine hyperplane $c_{\varepsilon_1}=\dots=c_{\varepsilon_v}=1$. 
\end{proposition}

\begin{corollary}
Let $c\in P^\sigma_2(\T)_\rd$. Under an isomorphism as in Proposition~\ref{prop:FixDecoration}, the Ptolemy field of $c$ is the field generated by the Ptolemy coordinates.\qed 
\end{corollary}
\begin{remark} 
A concrete method for selecting $1$-cells as in Proposition~\ref{prop:FixDecoration} is described in Section~\ref{sec:AlphaStarBasic}.
\end{remark}
Analogues of our results for higher rank Ptolemy varieties are discussed in Section~\ref{sec:HigherPtolemy}. The analogue of Proposition~\ref{prop:GenericBoundaryNonTrivial} holds for representations that are \emph{boundary-non-degenerate} (see Definition~\ref{def:BoundaryNonDeg}), and the analogue of Proposition~\ref{prop:FixDecoration} leads to a simple computation of the Ptolemy field. 
\begin{conjecture}
The Ptolemy field of a boundary-non-degenerate, generic, boundary-unipotent representation $\rho$ in $\SL(n,\C)$ or $\PSL(n,\C)$ is equal to its trace field.\qed
\end{conjecture}

\begin{remark}
The computation of reduced Ptolemy varieties is remarkably efficient using Magma~\cite{Magma}.
For all but a few census manifolds, primary decompositions of the (reduced) Ptolemy varieties $P^\sigma_2(\T)$ can be computed in a fraction of a second on a standard laptop. A database of representations can be found at \url{http://ptolemy.unhyperbolic.org/}~\cite{Unhyperbolic}.
All our tools have been incorporated into SnapPy~\cite{SnapPy} by the second author and the Ptolemy fields obtained through:

\begin{verbatim}
>>> from snappy import Manifold
>>> p=Manifold("m019").ptolemy_variety(2,'all')
>>> p.retrieve_solutions().number_field()
... [[x^4 - 2*x^2 - 3*x - 1], [x^4 + x - 1]]
 \end{verbatim}
 
The number fields are grouped by obstruction class. In this example, we see that the Ptolemy variety for the non-trivial obstruction class has a component with number field $x^4+x-1$, which is the trace field of m019. The above code retrieves a precomputed decomposition of the Ptolemy variety from~\cite{Unhyperbolic}.
In sage or SnapPy with Magma installed, you can use \texttt{p.compute\_solutions().number\_field()} to compute the decomposition.
\end{remark}
