---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-004-23-smooth-2-functors
section_title: "Smooth 2-Functors"
section_number: 2.3
pages: 10-10
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
\label{sec3}
\label{sec3_1}

This section and the forthcoming Section \ref{sec:smoothnessconditions} prepare two tools we need in Section \ref{sec:smoothdescent}  in order to specify the sub-2-category of smooth descend data. The first tool is the concept  of \emph{smooth 2-functors}. 


The general idea behind \quot{smooth functors} is to consider them internal to smooth manifolds. That is, the sets of objects and morphisms of the involved categories are smooth manifolds, and a smooth functor consists of a smooth map between the objects and a smooth map between the morphisms. Categories internal to smooth manifolds are called \emph{Lie categories}, internal groupoids are called \emph{Lie groupoids}. The same idea applies to 2-functors between \emph{2}-categories.


In the context of the present paper, we want to consider smooth  2-functors defined on the path 2-groupoid $\mathcal{P}_2(X)$ of a smooth manifold $X$,  respectively. However, $\mathcal{P}_2(X)$ is \emph{not} internal to smooth manifolds, not even infinite-dimensional ones. Instead, we consider it internal to a larger category of generalized manifolds, so-called \emph{diffeological spaces} \cite{souriau1}. Diffeological spaces and diffeological maps form a category $D^{\infty}$ that enlarges the category $C^{\infty}$ of smooth manifolds by means of a full and faithful functor
$C^{\infty} \to D^{\infty}$.
For an introduction to diffeological spaces we refer the reader to  \cite{baez6} or  \cite[Appendix A.2]{schreiber3}.  


Diffeological spaces admit many constructions that are not possible in the category of smooth manifolds. We need three of them. Firstly, if $X$ and $Y$ are diffeological spaces, the set $D^{\infty}(X,Y)$ of smooth maps from $X$ to $Y$ is again a diffeological space. In particular, the set of smooth maps between smooth manifolds is a diffeological space. Secondly, every subset of a diffeological space is a diffeological space. Thirdly, the quotient of every diffeological space by any equivalence relation is a diffeological space. These constructions are relevant because they show that the set $P^1X$ of thin homotopy classes of paths in $X$  as well as the set $B^{2}X$ of thin homotopy classes of bigons in $X$  are diffeological spaces.
We conclude that the path 2-groupoid $\mathcal{P}_2(X)$ of  a smooth manifold $X$ is internal to diffeological spaces, and we have a corresponding 2-category $\mathrm{Funct}^{\infty}(\mathcal{P}_2(X),S)$ of smooth  2-functors with values in some Lie 2-category $S$.
