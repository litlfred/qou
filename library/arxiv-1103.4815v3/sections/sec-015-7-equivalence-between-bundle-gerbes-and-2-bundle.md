---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-015-7-equivalence-between-bundle-gerbes-and-2-bundle
section_title: "Equivalence between Bundle Gerbes and 2-Bundles"
section_number: 7
pages: 38-39
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 1.0
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
\label{sec:equivalences}

In this section we show that Versions III and IV of smooth $\Gamma$-gerbes are equivalent in the strongest possible sense:

\begin{theorem}
\label{th:equivalence}
For $M$ a smooth manifold and $\Gamma$ a Lie 2-group, there is an equivalence of bicategories
\begin{equation*}
\grb\Gamma M \cong \zwoabun \Gamma M
\end{equation*}
between the bicategories of $\Gamma$-bundle gerbes and principal $\Gamma$-2-bundles over $M$.
This equivalence is natural in $M$, i.e. it is an  equivalence between pre-2-stacks.
\end{theorem}

Since the definitions of the bicategories  $\grb\Gamma M$ and $\zwoabun \Gamma M$, \emph{and} the above equivalence are all natural in $M$, we obtain automatically an induced equivalence for the induced bicategories over Lie groupoids (see Remarks \ref{rem:grbgrp} and \ref{rem:2bungrp}).

\begin{corollary}
For $\mathcal{X}$ a Lie groupoid and $\Gamma$ a Lie 2-group, there is an equivalence
\begin{equation*}
\grb\Gamma{\mathcal{X}} \cong \zwoabun\Gamma{\mathcal{X}}\text{.}
\end{equation*}
\end{corollary}


The following outlines the proof of Theorem \ref{th:equivalence}.  
In Section \ref{sec:extraction} we construct explicitly a 2-functor 
\begin{equation*}
\mathscr{E}_M: \zwoabun \Gamma M \to \grb\Gamma M\text{.}
\end{equation*}
Then we use a general criterion  assuring that $\mathscr{E}_M$ is an equivalence of bicategories. This criterion is stated in Lemma \ref{lem:equivalence}: it requires (A) that $\mathscr{E}_M$ is fully faithful on Hom-categories, and (B) to choose certain preimages of objects and 1-morphisms under $\mathscr{E}_M$. Under these circumstances, Lemma \ref{lem:equivalence} constructs an inverse 2-functor $\mathscr{R}_M$ together with the required pseudonatural transformations assuring that $\mathscr{E}_M$ and $\mathscr{R}_M$  form an equivalence of bicategories. Condition (A) is proved as Lemma \ref{lem:efullyfaithful} in Section \ref{sec:extraction}. The choices (B) are constructed in Section \ref{sec:reconstruction}. 


In order to prove that the 2-functors $\mathscr{E}_M$ extend to the claimed equivalence between pre-2-stacks, we use another criterion stated in Lemma \ref{lem:stackequivalence}. The only additional assumption of Lemma \ref{lem:stackequivalence} is that the given 2-functors $\mathscr{E}_M$ form a 1-morphism of pre-2-stacks; this is proved in Proposition \ref{prop:estack}. Then, the inverse 2-functors $\mathscr{R}_M$ obtained before automatically form an inverse 1-morphism between pre-2-stacks. 



\setsecnumdepth{2}
