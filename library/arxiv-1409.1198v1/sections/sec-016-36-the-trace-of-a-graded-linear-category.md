---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-016-36-the-trace-of-a-graded-linear-category
section_title: "The trace of a graded linear category"
section_number: 3.6
pages: 18-19
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.97
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
A {\em graded} linear category is a category equipped with an auto-equivalence $\la 1 \ra$. We denote by $\la t \ra$ the auto-equivalence obtained by applying $\la 1 \ra$ $t$ times.  Thus, given any object $x\in \Ob(\modC)$, there exists an object $x \la t \ra \in \Ob(\modC)$ for all $t$.  Likewise, given any morphism $f \maps x \to y$ in $\modC$, there is a morphism $f \la t \ra \maps x \la t \ra \to y \la t \ra$.  This equips Hom-sets with the structure of  $\Z$-graded abelian groups in which composition maps are grading preserving.

Given a graded linear category $\modC$, its Grothendieck group $K_0(\modC)$ is a $\Z[q,q^{-1}]$-module with $[x \la t \ra]_{\cong} := q^t[x]$.  Likewise, the trace $\Tr(\modC)$ is $\Z[q,q^{-1}]$-module with $[f\la t \ra] = q^t [f]$ for an endomorphism $f \maps x \to x$ in $\modC$.    In this case, the generalized Chern character map
\[
 K_0(\modC) \to \Tr(\modC)
\]
is a homomorphism of $\Z[q,q^{-1}]$-modules.

A graded linear category $\modC$ is said to {\em admit a translation} if for every object $x$ in $\modC$ and integer $t\in \Z$, there is an isomorphism  $x \to x\la t \ra$.  Given any graded linear category $\modC$, we can form a graded linear category $\modC^{\ast}$ that admits translations by declaring that $\Ob(\C)=\Ob(\C^{\ast})$ and setting
\[
 \modC^{\ast}(x,y) := \bigoplus_{t \in \Z} \modC(x,y\la t\ra),
\]
for all objects $x,y \in \Ob(\modC)$.  The translations $x \to x \la t \ra$ is given by $1_x$ in $\modC^{\ast}$ since
\[
 1_x \in \modC(x,x\la 0 \ra) = \modC\left(x,\left(x\la t \ra\right) \la -t\ra\right) \subset \modC^*(x,x\la t \ra),
\]
has inverse
\[
 1_x\la t\ra \in \modC(x \la t \ra, x \la t \ra) = \modC(x \la t \ra, (x \la 0 \ra) \la t \ra)   \subset \modC^{\ast}(x\la t\ra, x).
\]


By enlarging the hom spaces by adding isomorphisms $x \to x \la t\ra$, the Grothendieck group  of graded linear category with translation $\modC^{\ast}$ is only a $\Z$-module rather than a $\Z[q,q^{-1}]$-module since $[x\la t \ra]_{\cong} = [x]_{\cong}$.   However, the trace $\Tr(\modC^{\ast})$ changes more drastically because, rather than only considering degree preserving endomorphisms $f\maps x \to x$ in $\modC$, we can now consider arbitrary degree maps $x \to x\la t \ra$ and compose with the translation map from $x\la t \ra \to x$ to get a new endomorphism.  Furthermore, using the translations $x \cong x \la t \ra$, it is not hard to see that given any endomorphism $f\maps x \to x$, we have $[f\la t \ra] = [f]$ in $\Tr(\modC^{\ast})$, so that the graded version of the trace $\Tr(\modC^{\ast})$ is also just a $\Z$-module.



As explained at the beginning of section~\ref{sec_HH0trace}, any ring with unit can be viewed as a linear category
with one object $\ast$.  A graded ring $R = \oplus_{n \in \Z} R_n$ can be viewed as a graded category whose objects are indexed by the integers $n = \ast \la n \ra$ for $n \in \Z$.  The morphisms from $n$ to $m$ are given by the abelian group $R_{m-n}$.   Composition is given by the grading preserving multiplication in $R$.  Example \ref{example_chern-char} can be generalized to show that the generalized Chern character map  $K_0(R) \to \Tr(R_0)$ is an isomorphism whenever $R$ is a graded local ring, so that the trace of the degree zero part of the ring is isomorphic to the Grothendieck ring.

\begin{exercise} \label{ex_equiv}
If $\modC$ denotes the graded linear category associated to a graded ring $R$, then the graded linear category with translation $\modC^{\ast}$ is equivalent as a category to the linear category with one object $\ast$ obtained by forgetting the grading on $R$.
\end{exercise}



\begin{example}
The nilHecke algebra $\NH_n$ is a graded algebra with $\deg(x_i)=2$ and $\deg(\partial_i)=-2$.  Recall that the nilHecke ring $\NH_n$ is isomorphic as a graded algebra to the matrix ring ${\Mat}((n)^!_{q^2} ; \sym_n)$ of $n! \times n!$ matrices with coefficients in the ring $\sym_n=\Z[x_1,\dots,x_n]^{S_n}$ of symmetric functions in $n$ variables.  Here we write $(n)^!_{q^2}:= (1-q^{2n})/(1-q^2)$ for the non-symmetrized quantum integers and each variable of $\sym_n$ has degree $2$.

To compute the trace of $\NH_n$ regarded as a graded category $\modC$, observe that $\Tr(\modC) = \Tr(\sym)$ and that $\sym$ is positively graded and one dimensional in degree zero, in particular it is graded local, so that the graded trace of $\Tr(\modC) \cong K_0(\NH_n) \cong \Z$.  Compare this result with section~\ref{sample} where we showed $\Tr(\NH_n) \cong \sym_n$.   Exercise~\ref{ex_equiv} shows that by enlarging the graded category $\modC$ to $\modC^{\ast}$, we again have $\Tr(\modC^{\ast}) = \sym_n$.
\end{example}
