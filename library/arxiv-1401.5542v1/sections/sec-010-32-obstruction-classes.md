---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-010-32-obstruction-classes
section_title: "Obstruction classes"
section_number: 3.2
pages: 8-9
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.73
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
\label{sec:ObstructionClasses}
Each class in $H^2(\widehat M;\Z/2\Z)$ can be represented by a $\Z/2\Z$-valued $2$-cocycle on $\widehat M$, i.e.~an assignment of a sign to each face of $\T$.  
\begin{definition} Let $\sigma$ be a $\Z/2\Z$-valued $2$-cocycle on $\widehat M$. The \emph{Ptolemy variety} for $\sigma$ is defined as in Definition~\ref{def:PtolemyVariety}, but with the Ptolemy relation replaced by
\begin{equation}\label{eq:PtolemyRelationObstruction}
\sigma_{0,k}\sigma_{3,k}c_{03,k}c_{12,k}+\sigma_{0,k}\sigma_{1,k}c_{01,k}c_{23,k}=\sigma_{0,k}\sigma_{2,k}c_{02,k}c_{13,k},
\end{equation}
where $\sigma_{i,k}$ is the sign of the face of $\Delta_k$ opposite vertex $i$.
\end{definition}
\begin{remark} Multiplying $\sigma$ by a coboundary $\delta(\tau)$ corresponds to multiplying the Ptolemy coordinate of a one-cell $e$ by $\tau(e)$ (see~\cite{GaroufalidisThurstonZickert} for details). Hence, up to canonical isomorphism, the Ptolemy variety $P^\sigma_2(\T)$ only depends on the cohomology class of $\sigma$. The Ptolemy variety $P_2(\T)$ is the Ptolemy variety for the trivial obstruction class.
\end{remark}


\subsubsection{Examples}
In both examples above, $H^2(\widehat M;\Z/2\Z)=\Z/2\Z$, and the non-trivial obstruction class $\sigma$ is indicated in Figures~\ref{fig:Fig8Ordered} and~\ref{fig:Fig8SisOri}.

For the Figure-$8$ knot, $P^{\sigma}_2(\T)$ is given by
\begin{equation}\label{eq:Fig8PtolemyNontrivial}
-c_{23,0}c_{13,0}+c_{23,0}^2=-c_{13,0}^2,\qquad -c_{13,0}c_{23,0}+c_{13,0}^2=-c_{23,0}^2,
\end{equation}
which is equivalent to
\begin{equation}
x^2-x+1=0,\qquad x=\frac{c_{13,0}}{c_{23,0}}.
\end{equation} 
The corresponding representations are the geometric representation and its conjugate.

For the Figure 8 knot sister, the Ptolemy variety becomes
\begin{equation}\label{eq:Fig8SisPtolemyNontrivial}
-c_{23,0}c_{13,0}-c_{23,0}^2=c_{13,0}^2,\qquad -c_{23,0}c_{13,0}-c_{23,0}^2=c_{13,0}^2,
\end{equation}
which is equivalent to
\begin{equation}
x^2+x+1=0,\qquad x=\frac{c_{13,0}}{c_{23,0}}.
\end{equation}
