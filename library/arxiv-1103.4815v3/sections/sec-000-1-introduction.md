---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.986
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{intro}

Let $G$ be a Lie group and $M$ be a smooth manifold.
There are (among others) the following four   ways to say what a  {\em smooth $G$-bundle} over $M$ is:
\begin{enumerate}[(1)]

\item 
\emph{\v Cech 1-Cocycles}: an open cover $\left \lbrace U_i \right \rbrace$ of $M$, and for each non-empty intersection $U_i \cap U_j$ a smooth map $g_{ij}:U_i \cap U_j \to G$ satisfying the cocycle condition 
\begin{equation*}
g_{ij} \cdot g_{jk}=g_{ik}\text{.}
\end{equation*}

\item 
\emph{Classifying maps}: a continuous map 
$$ f: M \to \mathfrak B G$$
to the classifying space $\mathfrak B G$ of the group $G$.


\item
\emph{Bundle 0-gerbes}: a surjective submersion $\pi:Y \to M$ and a smooth map $g: Y \times_M Y \to G$ satisfying 
\begin{equation*}
\pi_{12}^{*}g \cdot \pi_{23}^{*}g = \pi_{13}^{*}g\text{,}
\end{equation*}
where $\pi_{ij}: Y \times_M Y \times_M Y \to Y \times_M Y$ denotes the projection to the $i$th and the $j$th factors. 


\item
\emph{Principal bundles}: a surjective submersion $\pi: P \to M$ with a smooth action of $G$ on $P$ that preserves $\pi$, such that the map
\begin{equation*}
P \times G \to P \times_M P : (p,g) \mapsto (p,p.g)
\end{equation*}
is a diffeomorphism. 

\end{enumerate}
It is well-known that these four versions of \quot{smooth $G$-bundles} are all equivalent. Indeed, (1) forms the smooth $G$-valued \v Cech cohomology in degree one, whereas (2) is known to be equivalent to continuous $G$-valued \v Cech cohomology, which in turn coincides with the smooth $G$-valued \v Cech cohomology. Further, (3) and (4) form equivalent categories; and isomorphism classes of the objects  (3) are in bijection with equivalence classes of the cocycles (1).


In this article we provide an analogous picture for \emph{smooth $\Gamma$-gerbes}, where  $\Gamma$ is a strict Lie 2-group. In particular, $\Gamma$ can be the automorphism 2-group of an ordinary Lie group $G$, in which case the term \quot{non-abelian $G$-gerbe} is commonly used. We compare the following four versions:
\begin{description}
\item[\normalfont Version I:] 
\emph{Smooth, non-abelian \v Cech $\Gamma$-cocycles} (Definition \ref{def:cocycles}). These form the classical, smooth groupoid-valued cohomology $\h^1(M,\Gamma)$ in the sense of Giraud \cite{giraud} and Breen \cite[Ch. 4]{breen3}, \cite{breen2}. 

\item[\normalfont Version II:] 
\emph{Classifying maps} (Definition \ref{def:classmap}). These are continuous maps $f: M \to \mathfrak B |\Gamma|$ to the classifying space of the geometric realization of $\Gamma$; such maps have been introduced and studied by Baez and Stevenson \cite{baez8}. 
 

\item[\normalfont Version III:]
\emph{$\Gamma$-bundle gerbes} (Definition \ref{def:grb}). These have been developed by Aschieri, Cantini and Jurco \cite{aschieri} as a generalization of the abelian bundle gerbes of Murray \cite{murray}. Here we present an equivalent  definition by applying a higher categorical version  \cite{nikolaus2} of  Grothendieck's stackification construction to the monoidal pre-2-stack of principal $\Gamma$-bundles. 

\item[\normalfont Version IV:]
\emph{Principal $\Gamma$-2-bundles} (Definition \ref{def:zwoabun}). These have been introduced by Bartels \cite{bartels}; their total spaces are Lie groupoids on which the Lie 2-group $\Gamma$ acts in a certain way. Compared to Bartels' definition, ours uses a  stricter and easier notion of such an action. 

\end{description}
We prove that all four versions are equivalent, and follow the same line of arguments as in the case of $G$-bundles outlined above:
\begin{itemize}

\item 
Baez and Stevenson have shown that homotopy classes of classifying maps of Version II are in bijection with the continuous groupoid-valued \v Cech cohomology $\h^1_c(M,\Gamma)$. We prove  (Proposition \ref{smoothening}) that the inclusion of \emph{smooth} into \emph{continuous} \v Cech $\Gamma$-cocycles induces a bijection $\h^1_c(M,\Gamma) \cong \h^1(M,\Gamma)$. These two results establish the equivalence between our Versions I and II (Theorem \ref{th:classifying}). 
\item
$\Gamma$-bundle gerbes and principal $\Gamma$-2-bundles over $M$ form bicategories. We prove (Theorem \ref{th:equivalence}) that these bicategories are equivalent, and so establish the equivalence between Versions III and IV. Our proof provides explicit 2-functors in both directions. 

\item
We prove the equivalence between Versions I and III by showing that non-abelian $\Gamma$-bundle gerbes are classified by the non-abelian cohomology group $\h^1(M,\Gamma)$ (Theorem \ref{th:gerbesclass}).
\end{itemize}


\begin{comment}
We remark that there exist other version of non-abelian gerbes, which will not be treated here; for example the \quot{charted 2-bundles} of Baas-B�kstedt-Kro \cite{baas2} (see Remark \ref{rem:baas}), \quot{Lie groupoid $G$-extensions} \cite{laurent1}, or \quot{2-group bundles} \cite{ginot1} (see Remark \ref{rem:ginot}). \end{comment}


The  first aim of this paper is to  simplify and clarify the notion of a non-abelian gerbe. This concerns  the notion of a $\Gamma$-bundle gerbe (Version III), for which we give a new, conceptually clear, and manifestly 2-categorical definition. It also concerns the notion of a principal 2-bundle (Version IV), for which we provide a new definition that is carefully balanced between generality and simplicity. 



The second aim of this paper is to make it possible to compare and transfer available  results between  the various versions. Indeed, none of the three equivalences above is available in the existing literature. As an example why such equivalences can be useful, we use Theorem \ref{th:equivalence} -- the equivalence between $\Gamma$-bundle gerbes and principal $\Gamma$-2-bundles -- in order to carry two facts  about $\Gamma$-bundle gerbes over to principal $\Gamma$-2-bundles. We prove: 
\begin{enumerate}
\item 
Principal $\Gamma$-2-bundles form a 2-stack over smooth manifolds (Theorem \ref{th:2stack}).
This is a new and evidently important result, since it explains precisely in which way one can \emph{glue} 2-bundles from local patches. 

\item
If $\Gamma$ and $\Omega$ are weakly equivalent Lie 2-groups, the 2-stacks of principal $\Gamma$-2-bundles and principal $\Omega$-2-bundles are equivalent (Theorem \ref{extequivbun}). This is another new result that generalizes the well-known fact that principal $G$-bundles and principal $H$-bundles form equivalent stacks, whenever $G$ and $H$ are isomorphic Lie groups.
 
\end{enumerate}
The two facts about $\Gamma$-bundle gerbes (Theorems \ref{th:stack} and \ref{extequiv}) on which these results are based are proved in an outmost abstract way: the first is a mere consequence of the definition of $\Gamma$-bundle gerbes that we give, namely via a 2-stackification procedure for principal $\Gamma$-bundles. The second follows  from the fact that principal $\Gamma$-bundles and principal $\Omega$-bundles form equivalent monoidal pre-2-stacks, which we deduce as a corollary of their description by anafunctors.

\begin{comment}
We  remark that there  exist other valuable versions of non-abelian gerbes that will not be treated in this article, e.g. Breen-Messing \cite{breen1} and Laurent-Gengoux-Sti�non-Xu \cite{laurent1} and Genougy-Stienon.  
\end{comment}






The present paper is part of a larger program. In a forthcoming paper, we address the discussion of non-abelian lifting problems, in particular string structures. In a second forthcoming paper we will present the picture of four equivalent versions in a setting \emph{with connections}, based on the results of the present paper. Our motivation is  to understand the role of 2-bundles with connections in higher gauge theories, where they serve as \quot{B-fields}.  
Here, two (non-abelian) 2-groups are especially important, namely the string group \cite{baez9} and the Jandl group \cite{nikolaus2}. More precisely, string-2-bundles appear in supersymmetric sigma models that describe fermionic string theories \cite{bunke1}; while Jandl-2-bundles appear in unoriented sigma models that describe e.g. bosonic type-I string theories \cite{schreiber1}.


This paper is organized as follows. In Section \ref{preliminaries} we recall and summarize the theory of principal groupoid bundles and their description by anafunctors. The rest of the paper is based on this theory. In Sections \ref{versionI}, \ref{versionII}, \ref{versionIII} and \ref{sec:2bundle} we introduce our four versions of smooth $\Gamma$-gerbes, and establish all but one equivalence. The remaining equivalence, the one between bundle gerbes and principal 2-bundles, is discussed in Section \ref{sec:equivalences}. 
 

\paragraph{Acknowledgements.}  
We thank Christoph Wockel for helpful
discussions. We also thank the Erwin Schr�dinger Institute in Vienna and the Instituto Superior T�cnico in Lisbon for kind invitations.  
TN is supported by the Collaborative 
Research Centre 676 ``Particles, Strings and the Early Universe - the Structure of Matter 
and Space-Time'' and the cluster of excellence
``Connecting particles with the cosmos''. 


\setsecnumdepth{2}
