---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
text_source: latex
latex_prose_ratio: 0.615
latex_coverage_ratio: 0.958
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM — We construct topological triangulations for complements of ( −2, 3,n )-pretzel knots and links with n≥ 7."
---
\label{sec:intro}

A knot or link in $S^3$ is \emph{hyperbolic} if its complement admits a complete hyperbolic structure.  A braid on $n$ strands, which is represented by a word in the braid group, $w\in B_n$, is hyperbolic if its braid closure, $L_w$, is.  Hyperbolic braids formed from three strands have been characterized by Futer, Kalfagianni, and Purcell \cite{FareyManifolds}, a characterization that depends on their representation in the braid group.  $B_3$ has two generators, $\sigma_1$ and $\sigma_2$ shown in Figure~\ref{fig:B3gen}, and one relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2 $.  The square of this element is commonly denoted by $C$, which is central.  In \cite[Theorem~5.5]{FareyManifolds}, Futer, Kalfagianni, and Purcell have shown that $S^3- L_w$ is hyperbolic if and only if $w$ is conjugate to $C^k\sigma_1^{p_1}\sigma_2^{-q_1}\cdots\sigma_1^{p_s}\sigma_2^{-q_s}$  with $k\in\Z$ and $p_i$, $q_i$, and $s$ positive integers, and $w$ is not conjugate to $\sigma_1^{p_0}\sigma_2^{q_0}$ for some integers~$p_0$ and~$q_0$ (closures of such braids are either unknots, torus knots, or connected sums of torus knots).  The proof is by contradiction; they show the required hyperbolic structures exist without  constructing associated triangulations.  In this paper, we construct geometric triangulations for braids with $k=2$, $s=1$, $p_1\ge1$, and $q_1=1$ thus offering a direct proof of the \lq\lq if'' direction of their theorem in these cases.  
\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{B3gen.pdf}
\put(1.8,.3){\small{$\sigma_1$}}
\put(8.35,.3){\small{$\sigma_2$}}
\end{overpic}
\caption{The generators of $B_3$, the braid group on three strands.\label{fig:B3gen}}
\end{figure}


Let $L_p$ be the braid closure of $C^2\sigma_1^p\sigma_2^{-1}$ with $p\ge1$, which has one component if $p$ is odd and two if $p$ is even.  The complement of $L_p$ is homeomorphic to the complement of a $(-2,3,p+6)$-pretzel (Corollary~\ref{cor:pretzelstoo}), so proving $C^2\sigma_1^p\sigma_2^{-1}$ is hyperbolic will cover those pretzel knots and links as well.  To show $C^2\sigma_1^p\sigma_2^{-1}$ is hyperbolic, we will first decompose its complement into ideal tetrahedra whose faces are identified in pairs  (Section~\ref{sec:idealtriangulationsq=1}).  These topological triangulations (one for each $p$) are very much in the spirit of the canonical decompositions first described for 2-bridge knot and link complements by Sakuma and Weeks in~\cite{SakumaWeeks}. It turns out that, as in the 2-bridge case detailed by Futer in~\cite[Appendix]{GwithF2Bridge}, our triangulations are not just topological; they are also \emph{geometric} (though not canonical).  In other words, each ideal tetrahedron can be given a hyperbolic shape of positive volume and, when the faces are paired by hyperbolic isometries, the resulting hyperbolic structure on $S^3-L_p$ is metrically complete. 


To prove that our topological triangulations are geometric, we will employ the \lq\lq Casson-Rivin program'' laid out by Futer and Gu\'eritaud in~\cite{AngledtoHyperbolic} --- their survey of Casson and Rivin's technique for finding the hyperbolic structure on a 3-manifold whose boundary consists of tori.  Gu\'eritaud has implemented this program for punctured torus bundles and 4-punctured sphere bundles~\cite{GwithF2Bridge} and Futer for 2-bridge knots~\cite[Appendix]{GwithF2Bridge}, whereas Gu\'eritaud and Schleimer have applied it to layered solid tori and Dehn fillings~\cite{DehnFillings} and Ham and Purcell used the same procedure to determine geometric triangulations on highly twisted links~\cite{HighlyTwisted}.  


Geometric triangulations can lead to better understandings of the geometry of finite-volume hyperbolic 3-manifolds, including simpler proofs.  However, it is not known whether every such 3-manifold admits a geometric triangulation.  Currently the list of infinite families of finite-volume hyperbolic 3-manifolds that have been shown to admit geometric triangulations is short: punctured torus bundles and 4-punctured sphere bundles~\cite{GwithF2Bridge}, 2-bridge knots and links~\cite[Appendix]{GwithF2Bridge}, and certain Dehn fillings of fully-augmented 2-bridge knots and links~\cite{HighlyTwisted}. The main result of this paper is that the $(-2,3,n)$-pretzel knots and links with $n\ge 7$ can be added to the list. 

\subsection*{Organization} 
After constructing the topological triangulations in Section~\ref{sec:idealtriangulationsq=1}, we offer definitions and a basic outline of the Casson-Rivin program in Section~\ref{sec:anglestructures}. 
The first step of the program is carried out in Section~\ref{sec:anglestructuresnonempty}, where we show that the space of positive angle structures for our triangulations (Definition~\ref{def:anglestructure}) is nonempty. The final step --- arguing that the critical point of the volume functional (Definition~\ref{def:volume}) is a positive angle structure --- is presented in Section~\ref{sec:proofq=1} with some comments about extending the construction in Section~\ref{sec:extendingconstruction}.

\subsection*{Acknowledgments} 
The explicit triangulations appearing here, as well as several more in the infinite family, were confirmed using the software packages Regina~\cite{Regina} and SnapPy \cite{SnapPy} and checked against the census of veering triangulations created by Giannopolous, Schleimer, and Segerman \cite{VeeringCensus}.  See the Regina data file at \href{https://tinyurl.com/ReginaFileC2sigma1psigma2inv}{https://tinyurl.com/ReginaFileC2sigma1psigma2inv} for the triangulations constructed in Section~\ref{sec:idealtriangulationsq=1}.

To make the graphics more accessible to those with color vision deficiencies, I have used two of Paul Tol's qualitative color schemes --- \emph{bright} (Figures~\ref{fig:fulltwist} and~\ref{fig:clasp}) and \emph{light} (Figures~\ref{fig:p=1} and~\ref{fig:firstlayer}).  His palettes are mathematically designed to appear distinct to all \cite{PaulTol}.

David Futer kindly gave feedback on an early draft of Appendix~\ref{app:seeing2-bridge} for which I am grateful.  

I especially want to thank Bill Dunbar for many helpful conversations.  There is no aspect of this paper --- the structure, the notation, the figures, the tables, the exposition, the results --- that has not been improved by his insights, careful reading, and self-described picky-ness.  I am also grateful for several useful suggestions offered by the referee.  That said, any remaining errors are mine.
