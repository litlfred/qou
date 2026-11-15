---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-004-14-overview-of-the-paper
section_title: "Overview of the Paper"
section_number: 1.4
pages: 5-6
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.974
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sub:Overview}

In Section~\ref{sec:TriangulationSection} we define the notion of a \emph{concrete triangulation}, which is a triangulation together with a vertex ordering of each simplex. Two types of concrete triangulations are particularly important, \emph{oriented} triangulations and \emph{ordered} triangulations. 


In Section~\ref{sec:ThurstonReview} we review Thurson's gluing equations, and 
in Section~\ref{sec:GeneralizedGluingEq} we define the analogues for $n\geq 2$. The key notion is that of a \emph{shape assignment}, which is defined first for a simplex and later for a triangulation. A shape assignment on a triangulation is a shape assignment on each simplex, such that the shapes satisfy the generalized gluing equations. 


In Section~\ref{sec:PtolemyReview} we review the theory of Ptolemy coordinates developed in~\cite{GaroufalidisThurstonZickert}, and in Section~\ref{sec:PtolemyToShapes} we define a map $\mu$ from Ptolemy assignments to shape assignments. 
In section~\ref{sec:Symplectic} we prove Theorem~\ref{thm:soft} and discuss some applications in quantum topology.
Sections~\ref{sec:Decorations}-\ref{sec:ReconstructRep} are devoted to proving Theorem~\ref{thm:MainThm}.
In Section~\ref{sec:Decorations}, we briefly review the notion of a decoration, and define the maps $\mathcal C$ and $\mathcal Z$ in \eqref{eqn:DiagramIntro}. In Section~\ref{sec:NaturalCocycles} we define the notion of a natural cocycle, and define the maps $\mathcal L_{\alpha\beta}$ and $\mathcal L_{\alpha\beta\gamma}$. In Section~\ref{sec:ExplicitFormulas}, we show that the natural cocycle of a decoration is given explicitly in terms of the shapes (or Ptolemy coordinates), and in Section~\ref{sec:ReconstructRep} we show that the bottom maps of \eqref{eqn:DiagramIntro} are bijective concluding the proof of Theorem~\ref{thm:MainThm}. In Section~\ref{sec:Duality} we discuss a duality between Ptolemy coordinates and shape coordinates, and in Section~\ref{sec:CuspEquations} we show how to add cusp equations to ensure that the representations are boundary-unipotent. Finally, in Section~\ref{sec:Example} we write down the gluing equations and cusp equations for the figure-eight knot complement for $n=3$ and $n=4$.


\begin{remark}\label{rm:ObstructionCocycles}
The $\SL(2,\C)$-Ptolemy varieties are often empty for the cusped census manifolds. Even though the geometric representation of a cusped hyperbolic manifold lifts to $\SL(2,\C)$, no lift is boundary-unipotent, and often (non-trivial) boundary-unipotent $\SL(2,\C)$-representations don't exist.
In Garoufalidis-Thurston-Zickert, we also considered Ptolemy varieties for $p\SL(n,\C)=\SL(n,\C)\big/\pm I$, defined when $n$ is even via an obstruction class in $H^2(M,\partial M;\Z/2\Z)$. The primary purpose of this was to ensure that the image of the geometric representation under the unique irreducible representation $\PSL(2,\C)\to p\SL(n,\C)$ is detected for all census manifolds (more generally, for triangulations where all edges are essential). In this paper we shall only consider the $\SL(n,\C)$-Ptolemy variety. 

One can develop all the theory using the $p\SL(n,\C)$-Ptolemy varieties, but since our main interest here is in the shape coordinates (and for clarity of exposition), we shall not do this here.
\end{remark}

\begin{remark}\label{rm:Volume}
In Garoufalidis-Thurston-Zickert~\cite{GaroufalidisThurstonZickert} we defined the volume (in fact, complex volume) of a boundary-unipotent $\SL(n,\C)$-representation and gave an explicit formula using the Ptolemy coordinates. Similary, one can define the volume of a decorated $\PGL(n,\C)$-representation by adding the volumes of each of the shapes. The volume is an invariant of a decorated $\PGL(n,\C)$-representation (in the sense of Remark~\ref{rm:DecorationsAndBundles}), but we do not know if the volume is independent of the decoration. This is non-trivial even for $n=2$, where it was first proved by Francaviglia~\cite{FrancavigliaVolume}. We shall not deal with this here. 
\end{remark}
