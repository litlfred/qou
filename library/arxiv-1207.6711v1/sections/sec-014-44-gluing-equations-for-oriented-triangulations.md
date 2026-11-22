---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-014-44-gluing-equations-for-oriented-triangulations
section_title: "Gluing equations for oriented triangulations"
section_number: 4.4
pages: 10-13
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.839
latex_coverage_ratio: 0.914
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:GluingEquations}

Let $\T$ be an \emph{oriented} triangulation $\mathcal{T}$. The gluing equations are indexed by (non-vertex) integral points of $\mathcal{T}$ defined below and come in three flavors: \emph{edge equations}, \emph{face equations}, and \emph{interior equations}. In Section~\ref{sec:ShapeAssignmentSymmetries} we generalize the gluing equations to all concrete triangulations.

Recall that $\mathcal{T}$ is an identification of $\widehat{M}$ with a quotient of a disjoint union of standard simplices. Hence, $\mathcal{T}$ comes naturally equipped with a map
\begin{equation}
q\colon \coprod\Delta^3_n \rightarrow \widehat{M}.
\end{equation}


\begin{definition}\label{def:IntegralPoint}
An \emph{integral point} of $\mathcal{T}$ is a point $p$ in  
$$q\left(\coprod\Delta^3_n(\Z)\right)\subset \widehat{M}.$$
We view $p$ as an equivalence class of pairs $(t,\Delta)$ with $t\in\Delta^3_n(\Z)$ and $\Delta\in\mathcal T$ and write $(t,\Delta)\in p$ if $(t,\Delta)$ is a representative of $p$. The set of all integral points of $\mathcal{T}$ is denoted by $\mathcal{T}(\Z)$.
\end{definition}

\begin{definition} Let $p$ be an integral point of $\mathcal T$ represented by $(t,\Delta)$.
\begin{enumerate}[(i)]
\item We call $p$ a \emph{vertex point} if $t$ is a vertex of $\Delta^3_n(\Z)$.
\item We call $p$ an \emph{edge point} if $t$ is on an edge of $\Delta^3_n(\Z)$.
\item We call $p$ a \emph{face point} if $t$ is on a face $\Delta^3_n(\Z)$.
\item We call $p$ an \emph{interior point} if $t$ is in the interior of $\Delta^3_n(\Z)$, i.e.~if $t\in\Delta_n^3(\Z_+)$.
\end{enumerate}
We denote the set of non-vertex integral points by $\dot{\mathcal T}_n(\Z)$.
\end{definition}

\begin{definition}\label{def:GluingEquationsOri}
A shape assignment on an ordered triangulation $\mathcal{T}$ is a shape assignment $z^e_{s,\Delta}$ for each simplex $\Delta\in\mathcal{T}$ such that for each non-vertex integral point $p\in\dot{\mathcal{T}}_n(\Z)$, the \emph{generalized gluing equation}
\begin{equation}
\prod\limits_{(t,\Delta)\in p}\,\prod\limits_{t = s + e} z^e_{s,\Delta} = 1. \label{eqn:GeneralizedGluing}
\end{equation}
is satisfied. The variety of shape assignments on $\T$ is denoted by $V_n(\T)$.
\end{definition}



\begin{figure}
\begin{center}
\subfigure[$z_0z''_1z'_2=1$]{
\includegraphics[scale=0.35]{figures_src/tetGluing1Left}} 
\subfigure[$z_{1200,0}^{1100}z_{0102,1}^{0101}z_{0120,2}^{0110}=1$]{
\includegraphics[scale=0.35]{figures_src/tetGluing1Right}}
\end{center}
\caption{Edge equations for $n=2$ (traditional notation) and $n=5$. \label{fig:edgeGluing}}
\end{figure}

\begin{figure}
\begin{center}
\scalebox{0.9}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(250.9994,128.3062)
 \put(0,0){\includegraphics{figures_gen/tetFaceGluingEquation_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.554993,78.085836){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\Delta_0$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(238.867707,80.281936){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\Delta_1$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}\\
\bigskip
$\phantom{=1} \underbrace{z^{0011}_{2011,0}z^{1001}_{1021,0}z^{1010}_{1012,0}}_{t_0=2022}\underbrace{z^{0011}_{0211,1}z^{0101}_{0121,1}z^{0110}_{0112,1}}_{t_1=0222}=1$
\end{center}
\caption{A face equation for $n=6$. The indicated face-pairing is encoded by the permutation $\sigma=(0231)\in S_4$.}\label{fig:faceGluing}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[scale=0.35]{figures_gen/tetInternalGluingEquation_included}\\
\bigskip
$\underbrace{z^{0011}_{2210} z^{0101}_{2120} z^{0110}_{2111}z^{1001}_{1220} z^{1010}_{1211} z^{1100}_{1121}}_{t=2221}=1$
\end{center}
\caption{An internal equation for $n=7$.\label{fig:internalGluing}}
\end{figure}

 Note that the gluing equation for an integral point $p$ sets equal to $1$ the product of the shape parameters of all edges of subsimplices such that the edge midpoint intersects $p$.
The generalized gluing equations come in three different flavors depending on the type of the integral point $p$.
\begin{itemize}
\item {\bf Edge equations:} If $p$ is an edge point, the equation is similar to the usual gluing equation in that the number of terms equals the length of the edge cycle. There are $n-1$ edge gluing equations per edge of $\mathcal{T}$ involving shape parameters at different levels. See Figure \ref{fig:edgeGluing}.
\item {\bf Face equations:} If $p$ is a face point, the product consists of six terms with three terms from each of the two simplices sharing the face. There are $\binom{n-1}{2}$ equations per face. See Figure \ref{fig:faceGluing}.

\item {\bf Internal equations:} If $p$ is an interior point, the equation consists of six terms involving subsimplices of the same simplex, i.e.~this equation is independent of the triangulation. There are $\binom{n-1}{3}$ equations per simplex. See Figure \ref{fig:internalGluing}.
\end{itemize}

\begin{remark}
There are no vertex equations. If $p$ is a vertex point, \eqref{eqn:GeneralizedGluing} is tautologically satisfied since the product is empty. 
\end{remark}
