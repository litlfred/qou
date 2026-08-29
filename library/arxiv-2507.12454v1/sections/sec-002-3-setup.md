---
doc_id: arxiv-2507.12454v1
doc_title: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT"
section_id: sec-002-3-setup
section_title: "Setup"
section_number: 3
pages: 8-9
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
doc_brief: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of"
---
After reviewing in detail the basic example, we turn to the general setup and precise def-
initions. There is no reason to consider only genus 0 surfaces, and the classical motivation
directly extends to the more general case, for instance ODEs can be studied on complex
curves of arbitrary genus.
Definition 3.1. Fixg≥ 0,n,k≥ 1 and Jordan formsJ1,J 2,...,J k∈ GLn. The associated
genusg character variety X = Charg;J1,...,Jk is the space
{(A1,...,A g,B 1...,B g,M 1,··· ,Mk) :Mi∼Ji,
COHOMOLOGY RINGS OF CHARACTER V ARIETIES 9
A1B1A−1
1 B−1
1 ··· AgBgA−1
g B−1
g M1··· Mk =I}/∼,
where∼ identifies tuples of matrices which are conjugate with respect to the GL n(C)
action.
Definition 3.2 ([HLRV11]). The data J1,...J k are generic if
(i) Qk
i=1 detJi = 1
(ii) Qk
i=1 detJ′
i̸= 1 for any 0<n′ <n and any block-decomposition
 
J′
i J′′
i
0 J′′′
i
!
∼Ji
(J′
i∈ GLn′).
Theorem 3.3 ([HLRV11]). For generic data n,k,J 1,...,J k, the quotient space X =
Charg;J1,...,Jk has the structure of a smooth affine algebraic variety.
In fact, considering functions on X of the form
tr(Mi1orAi1orBi1··· MimorAimorBim)
we can realize X as an algebraic subset of CN for suffuciently large N.
Basically, the same reasoning as in the Fricke-Klein situation can be applied in general.
However, the number of traces one needs to consider is uncontrollably large, and it seems
hopeless to be able to produce all equations by the elimination computation. Even if we do
obtain a complete list of equations, it is not clear which interesting information we should
be able to extract from such a list. For instance, equations in the case of genus 0, rank 2,
5 punctures are given in [Sim17]. We do hope, however, that computing the cohomology
ring is an achievable goal.
Problem 3.4. Compute the cohomology ring H∗(X, C).
