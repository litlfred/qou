---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-001-11-what-is-categorification
section_title: "What is categorification?"
section_number: 1.1
pages: 1-2
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.918
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
Categorification is perhaps best explained by defining decategorification.  Quite broadly, {\em decategorification} is a rigorously defined procedure for forgetting information and reducing the complexity of a given mathematical structure.   A bit more formally, a {\em decategorification} can be thought of as a map
\[
 \xy
  (-20,0)*+{\txt{$(n-1)$-category}}="1";
  (20,0)*+{\txt{$n$-category}}="2";
  {\ar_-{\cal{D}} "2";"1" };
 \endxy
\]
for simplifying an $n$-categorical structure into an $(n-1)$-categorical structure.

Categorifcation asks the question ``given a  specific $(n-1)$-category $A$, find an $n$-category $B$ such that $A \cong \cal{D}(B)$".  In this case, we say that $A$ is the decategorification of $B$ and that $B$ categorifies $A$. Often it is the case that the existence of a categorification of $A$ reveals new insights and hidden structure that could not be seen without knowledge of $B$.  For more introductory material on categorification see~\cite{BaezDolan,KMS,Lau3,Savage}.

An example when $n=1$ can be obtained by considering the 1-category $\cat{Vect}_{\k}$ of finite dimensional $\k$-vector spaces.  We can define a decategorification
\[
 \xy
  (-20,0)*+{\N}="1";
  (20,0)*+{\cat{Vect}_{\k}}="2";
  {\ar_{\cal{D}} "2";"1" };
 \endxy
\]
from the 1-category $\cat{Vect}_{\k}$ to the $0$-category, or set, of natural numbers $\N$ by setting $\cal{D}=\dim$.  In this example a natural number $n$ is categorified by any vector space $V$ with $\dim(V)=n$.  This categorification lifts much of the structure of natural numbers, i.e. $\dim(V \oplus W) = \dim(V) + \dim (W)$ and $\dim (V \otimes W) = \dim (V) \times \dim (W)$.

Generalizing the previous example, let $\cat{gVect}_{\k}$ denote the category of graded vector spaces $V = \oplus_{k \in \Z} V_k$.  One way to decategorify a graded vector space is to take its graded dimension
\[
 \xy
  (-20,0)*+{\N[q,q]^{-1}}="1";
  (20,0)*+{\cat{gVect}_{\k}}="2";
  {\ar_-{\cal{D} = \dim_q} "2";"1" };
 \endxy
\]
where
\[
 \dim_q V := \sum_{k \in \Z} q^k \dim V_k.
\]
This example can be extended another direction by considering the category $\Kom(\cat{gVect}_{\k})$ of complexes of graded vector spaces. The graded Euler characteristic gives rise to a decategorification map taking a bounded complex of graded vector spaces into a Laurent polynomial $\chi(C_{\bullet})=\sum_i (-1)^i \dim_q C^i \in \Z[q,q^{-1}]$.  While these examples may seem somewhat trivial, these elementary ideas resurface in more sophisticated categorifications discussed below.


Several important observations are in order.  A categorification need not be unique, in the sense that there may be two different
$n$-categories $B$ and $B'$ with $A=\cal{D}(B)=\cal{D}(B')$.  Furthermore, there may be several different ways to simplify a given
$n$-categorical structure into an $(n-1)$-categorical structure.  That is to say, it may be possible to decategorify a given structure in more than one way.  In this article we will focus on two ways of decategorifying an (additive) category to produce an abelian group.  These are the ``Grothendieck group" and ``trace".
