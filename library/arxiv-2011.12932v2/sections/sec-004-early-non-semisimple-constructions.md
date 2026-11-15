---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-004-early-non-semisimple-constructions
section_title: "Early non-semisimple constructions"
section_number: null
pages: 3-4
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.984
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
Reshetikhin and Turaev's work immediately sparked a wide interest in the newly born field of quantum topology, and some natural questions quickly emerged. First of all, is it possible to figure out the relevant combinatorics for elements of ribbon Hopf algebras arising from the construction of \cite{RT90} without relying on their representation theory? Answering this question required learning how to deal with Hopf algebras themselves, which, in the relevant family of concrete examples, are not semisimple, and thus are not completely determined by their simple modules. Therefore, another natural question was: can we relax the semisimplicity requirement of Turaev? Lawrence explained in \cite{La90} how to construct so-called \textit{universal link invariants} using directly quantum groups, and thus bypassing their representation theory. These ideas were expanded by Hennings \cite{H96}, who upgraded Lawrence's construction to obtain invariants of closed oriented 3-manifolds starting from finite-dimensional factorizable\footnote{Factorizability is the appropriate non-degeneracy condition for ribbon Hopf algebras in the non-semisimple setting, see Section \ref{S:L-mod_cat}.} ribbon Hopf algebras. Since semisimplicity was no longer required, this constituted the first non-semisimple generalization of Reshetikhin--Turaev invariants, and the start of non-semisimple quantum topology. Hennings' result was reformulated by Kauffman and Radford avoiding the use of orientations for framed links \cite{KR94}. Both of these constructions were extended by Lyubashenko, who proposed a more general definition of modular category with respect to Turaev's original one, and used it to build topological invariants of 3-manifolds and projective representations of mapping class groups of surfaces \cite{L94}. For such a modular category $\calC$, which is allowed to be non-semsimple, we denote with $\rmL_\calC$ the corresponding Lyubashenko invariant of closed oriented 3-manifolds. The main families of examples are provided by categories of finite-dimensional representations of small quantum groups, without quotient operations. In Section \ref{S:sl_2_non-sem-sim}, we discuss the case of $\bar{U}_q \fsl_2$. 

Lyubashenko's work raised again some natural questions:
\begin{enumerate}
 \item Since this construction produces all the desired byproducts one expects to obtain from a TQFT, is there actually a TQFT lying behind them? 
 \item Given that the loss of algebraic information is successfully avoided, do we get finer topological invariants and mapping class group representations?
\end{enumerate}  
A few results which appeared in the early stages of the development of this new approach seemed to suggest negative answers to both questions. More precisely, it was first shown by Ohtsuki in a special case \cite{Oh95}, and later by Kerler in general \cite{K96b}, that if $\calC$ is a non-semisimple modular category, and if $M$ is a closed oriented 3-manifold with first Betti number $b_1(M) > 0$, then
\[
 \rmL_\calC(M) = 0.
\]
This is a deep obstruction for the definition of TQFT extensions. Indeed, it is a standard consequence of symmetric monoidality that the dimension of the state space $\rmV_\calC(\Sigma)$ of a closed oriented surface $\Sigma$ for a TQFT $\rmV_\calC$ extending $\rmL_\calC$ is
\[
 \dim_\Bbbk \rmV_\calC(\Sigma) = \rmL_\calC(\Sigma \times S^1).
\]
This means that Lyubashenko's invariant associated with a non-semisimple modular category $\calC$ cannot be extended to a TQFT, at least not in the sense of Atiyah. For years, the most involved achievement in a non-semisimple setting was a result of Lyubashenko and Kerler \cite{KL01} which produces a partial version of an Extended TQFT (ETQFT for short) satisfying only weak monoidality properties.\footnote{Very briefly, an ETQFT is a 2-categorical analogue of a TQFT, i.e. a symmetric monoidal 2-functor from a 2-category of cobordisms to a 2-category of linear categories (several choises are possible also for the target). Kerler and Lyubashenko's 2-functors are only defined for connected surfaces, with symmetric monoidal structure induced by connected sum instead of disjoint union.} Furthermore, it was later shown that, at least for small quantum $\fsl_2$, Hennings and Lyubashenko's invariants can be expressed as functions of Witten--Reshetikhin--Turaev ones \cite{CKS07}. More precisely, if $\calC$ is the category of finite-dimensional representations of $\bar{U}_q \fsl_2$, and if $\bar{\calC}$ is the semisimple quotient of $\calC$ inducing Witten's invariants, then for every 3-manifold $M$ we have
\[
 \rmL_\calC(M) = h_1(M) \RT_{\bar{\calC}}(M),
\]
where $h_1(M) = \left| H_1(M) \right|$ if $b_1(M) = 0$, and $h_1(M) = 0$ if $b_1(M) > 0$. Because of these hurdles, these deep works were underestimated for quite some time. This is not to say that the constructions were forgotten, as the number of publications containing reviews of Hennings' approach witnesses \cite{K96a,V03,H05}. However, a feeling that no additional topological information could be accessed through non-semisimple generalizations of Reshetikhin and Turaev's work started to spread.
