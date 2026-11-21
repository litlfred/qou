---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-009-3-angle-structures-and-the-casson-rivin-program
section_title: "Angle structures and the Casson-Rivin program"
section_number: 3
pages: 11-13
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.9
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:anglestructures}  

We will prove that the triangulation~$\tau_{p}$ of $X_{p}$ defined in~\ref{sec:anyp} is geometric by applying the Casson-Rivin program.  This section provides some definitions,  useful results, and a basic outline of the program.  For more details and a beautiful exposition, including an elementary proof of the Casson-Rivin Theorem, the reader is encouraged to read Futer and Gu\'eritaud's paper~\cite{AngledtoHyperbolic}.



\subsection{Angle structures} \label{sec:definitions}  

To move from a topological triangulation to a geometric one, we need a way to impose a hyperbolic structure on each tetrahedron where the face pairings are hyperbolic isometries. A start is to assign angles to the edges of the triangulation.

\begin{defn}\label{def:anglestructure}
An \emph{angle structure} on an ideal triangulation $\tau$ of a 3-manifold is an assignment of angles to the edges of the tetrahedra in~$\tau$ satisfying the following conditions:
\begin{enumerate}
\item Angles assigned to opposite edges of a tetrahedron are equal, meaning it is enough to specify three angles $\theta_{3i-2}$, $\theta_{3i-1}$, and $\theta_{3i}$, for each tetrahedron~$T_i\in\tau$;
\item $\theta_{3i-2}+\theta_{3i-1}+\theta_{3i} = \pi$ for all~$i$; and
\item The sum of the angles surrounding an edge of the 3-manifold equals $2\pi$.
\end{enumerate}
\end{defn}

This paper utilizes both \emph{taut angle structures}, where $\theta_k\in\{0,\pi\}$ for all~$k$, and \emph{positive angle structures}, where $\theta_k>0$ for all~$k$.  Note that Condition~(2) of the definition implies that a positive angle structure must have all angles strictly between~0 and~$\pi$.  In this case, the three angles that sum to~$\pi$ specify a \emph{positively oriented ideal hyperbolic tetrahedron}.  The tetrahedron is isometric to one whose vertices are at $0$, $1$, $\infty$, and a complex number~$z$ with $\text{Im}(z)>0$, where $0$, $1$, and $z$ form a Euclidean triangle having the assigned angles.  If $\text{Im}(z)=0$, the tetrahedron is said to be \emph{degenerate}, and, if $\text{Im}(z)<0$, \emph{negatively oriented}.  If an angle structure~$\theta$ assigns the same angles to two tetrahedra, $T_1$ and $T_2$, then we will say they are \emph{isometric with respect to $\theta$} and write $T_1\cong_\theta T_2$.  

We use $\mathcal A(\tau)$ to denote the space of all positive angle structures on a triangulation~$\tau$ and note that, if $\tau$ has $n$ tetrahedra, $\mathcal A(\tau)\subset(0,\pi)^{3n}$ is a convex polytope with compact closure.  As such, the points obtained through coordinate-by-coordinate averaging of elements of $\mathcal A(\tau)$ are again in $\mathcal A(\tau)$.  Also, real-valued functions defined on $\overline{\mathcal A(\tau)}$ attain their extreme values. See \cite[Proposition~3.2]{AngledtoHyperbolic} for more details about the space of angle structures.

As will be described in~\ref{sec:CR}, the initial step in the Casson-Rivin program is to argue that $\mathcal A(\tau)$ is nonempty, i.e., that the triangulation admits a positive angle structure.  We accomplish this in our case by first showing (in~\ref{sec:veering}) that~$\tau_{p}$ admits a special type of taut angle structure --- a veering angle structure.   The notion of \lq\lq veering,'' first introduced by Agol~\cite{AgolVeering}, has several equivalent formulations.  The simplest to apply to our triangulations is from~\cite{HodgsonEtal}.

\begin{defn}\label{def:veering}
A \emph{veering angle structure} on an ideal triangulation $\tau$ of an oriented 3-manifold $M$ is a taut angle structure meeting an additional condition:  The edges of $M$ can be colored red and blue in such a way that within each tetrahedron
\begin{itemize}
    \item two of the edges with angle~0 are red and two are blue (the color on an angle~$\pi$ edge can be either red or blue)
    \item when viewed from any of the four ideal vertices, the $\pi$-angled edge is followed in the counterclockwise direction by a blue edge and then a red edge.    
 \end{itemize}
Each tetrahedron in a veering triangulation appears as the one in Figure~\ref{fig:veering}, where the $\pi$-angled edges on the diagonal can be red or blue.  If there is also a consistent \lq\lq upward'' orientation on the four faces (for example out of the page in Figure~\ref{fig:veering}), the angle structure is \emph{transverse taut}.  A triangulation that admits a veering angle structure is said to be \emph{veering}.
\end{defn} 
\begin{figure}[ht]
\includegraphics{veering.pdf}
\caption{A tetrahedron in a veering triangulation.\label{fig:veering}}
\end{figure}

 Positive angle structures give geometric structures on the tetrahedra in a triangulation.  In turn, these structures determine the face-pairing isometries.  Condition~(3) of Definition~\ref{def:anglestructure} guarantees that, under these isometries, the tetrahedra fit together to fill the space around the edges of the manifold, because the sum of dihedral angles around any edge is~$2\pi$.  However, there is no guarantee that the result is metrically complete.  In fact, if a 3-manifold has a complete hyperbolic structure of finite volume, Mostow-Prasad rigidity ensures that the structure is unique up to isometry \cite{MostowRigidity} \cite{PrasadRigidity}, so one should not expect completeness for an arbitrary point in~$\mathcal A(\tau)$.  It turns out that the independent work of Casson and Rivin~\cite{Rivin}, which forms the basis of the Casson-Rivin program in~\cite{AngledtoHyperbolic} and outlined in~\ref{sec:CR}, connects the question of completeness to the volume associated to an angle structure in~$\mathcal A(\tau)$, i.e., the sum of the volumes of the corresponding hyperbolic tetrahedra.
