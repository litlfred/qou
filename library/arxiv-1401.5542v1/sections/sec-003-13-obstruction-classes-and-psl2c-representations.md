---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-003-13-obstruction-classes-and-psl2c-representations
section_title: "Obstruction classes and PSL(2,C)-representations"
section_number: 1.3
pages: 4-4
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 1.0
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
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
