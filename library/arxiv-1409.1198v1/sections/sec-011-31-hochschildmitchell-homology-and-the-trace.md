---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-011-31-hochschildmitchell-homology-and-the-trace
section_title: "Hochschild–Mitchell homology and the trace"
section_number: 3.1
pages: 13-14
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.877
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{sec_HH0trace}



Any ring $R$ with unit $1_R$ can be viewed as a linear category with one object $\ast$ and whose morphisms $\Hom(\ast,\ast)$ are given by the abelian group $R$.  Composition is given by multiplication in $R$ and the identity morphisms of $\ast$ corresponds to the unit $1_R \in R$.
Utilizing this observation, it possible to define the Hochschild--Mitchell homology of an arbitrary linear category as follows.

Let $\modC $ be a small linear category. Define the {\em Hochschild--Mitchell complex} of $\modC $
$$
C_{\bullet}=C_{\bullet}(\modC ):\quad \quad \dots\longrightarrow C_n \xto{d_n} C_{n-1} \xto{d_{n-1}} \dots \xto{d_2} C_1 \xto{d_1} C_0 \longrightarrow 0,
$$
where
$$
C_n=C_n(\modC ):=\bigoplus_{x_0,\dots,x_n\in\Ob(\C)}\C(x_n,x_0)\otimes\C(x_{n-1},x_n)\otimes\dots\otimes\C(x_0,x_1),
$$
$$
d_n(\sigma_n\otimes\sigma_{n-1}\otimes\dots\otimes\sigma_0):=\sum_{i=0}^{n-1}(-1)^i\sigma_n\otimes\dots\otimes\sigma_{n-i}\sigma_{n-i-1}\otimes\dots\otimes\sigma_0+
(-1)^n\sigma_0\sigma_n\otimes\sigma_{n-1}\otimes\dots\otimes\sigma_{1}.
$$


The Hochschild--Mitchell homology $\HH_{\bullet}(\modC )$ of $\modC $ is defined to
be the homology of the chain complex $C_{\bullet}(\modC )$.  One can easily check that if $\modC$ is a unital ring $R$ regarded as a linear category, then this definition agrees with the one given in section~\ref{subsec_HH0ring}.



In this article we will be especially concerned with the zeroth Hochschild--Mitchell homology
$\HH_0(\modC )=C_0/d_1(C_1)$ of $\modC$.  We introduce the notation
\[
\Tr(\modC ) := \HH_0(\modC )
\]
which we call the  {\em trace} of the linear category $\modC$.  This terminology is justified by the following observation. For any $x\in \Ob(\C)$ we denote by $\C(x,x)=\Hom_\C(x,x)=\End_\C(x)$ the
space of its endomorphisms.  Then it is an easy calculation to verify that the trace $\Tr(\modC )$ of the linear category $\modC$ is given by
\begin{gather*}
  \Tr(\C )=
\left( \bigoplus_{x\in \Ob(\modC )}\modC (x,x) \right)/\Span\{fg-gf\},
\end{gather*}
where $f$ and $g$ run through all pairs of morphisms $f\col
x\longrightarrow y$, $g\col y\longrightarrow x$ with $x,y\in
\Ob(\modC )$.

We denote by $[f]$ the equivalence class of $f\in \C(x,x)$ in $\Tr(\C)$.
The trace $\Tr$ gives rise to a functor from the category of (small) linear
categories to the category of abelian groups.
