---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-051-91-list-of-modifications
section_title: "List of modifications"
section_number: 9.1
pages: 43-44
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.96
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Fusion and multi-fusion categories in characteristic $p$ are defined in the same way as in charactersitic zero. Below we will describe the modifications which need to be made to validate the statements from the previous sections in this case.

**Section 2.** The statements of subsections 2.1, 2.2 which make sense generalize without changes, except the last statement of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}, which claims that the global dimension of a fusion category is nonzero. This is in fact false in positive characteristic. For example, if $G$ is a finite group whose order is divisible by $p$, then the category of modules over the function algebra ${\rm Fun}(G,k)$ is a fusion category of global dimension $|G|=0$. This is the main difference between the zero and positive characteristic case. To deal with this difference, we introduce the following definition.

::: definition
A fusion category over $k$ is said to be nondegenerate if its global dimension is nonzero. An indecomposable multi-fusion category is nondegenerate if at least one of its component categories is nondegenerate. A multi-fusion category is nondegenerate if all its indecomposable parts are nondegenerate. A regular semisimple weak Hopf algebra over $k$ is nondegenerate if its category of representations is a nondegenrate multi-fusion category.
:::

Theorems [\[dualcat\]](#dualcat){reference-type="ref" reference="dualcat"}, [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"}, [\[multi-fus\]](#multi-fus){reference-type="ref" reference="multi-fus"} remain valid if the category ${\mathcal C}$ is nondegenerate. Proposition [\[samedim\]](#samedim){reference-type="ref" reference="samedim"} remains true without any additional conditions.

In Section 2.5 (and at other places throughout), the algebra $R$ has to be chosen in such a way that its block sizes are not divisible by $p$ (since only such algebras admit a symmetric separability idempotent). Theorem [\[Schlah\]](#Schlah){reference-type="ref" reference="Schlah"} is valid for such $R$. Corollary [\[Schlah1\]](#Schlah1){reference-type="ref" reference="Schlah1"} and Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"} also remain valid. Theorem [\[sscoss\]](#sscoss){reference-type="ref" reference="sscoss"} is valid for nondegenerate weak Hopf algebras.

Theorems [\[van\]](#van){reference-type="ref" reference="van"}, [\[ocnrig\]](#ocnrig){reference-type="ref" reference="ocnrig"}, [\[multocnrig\]](#multocnrig){reference-type="ref" reference="multocnrig"}, [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"}, and Corollary [\[ocnrigmod\]](#ocnrigmod){reference-type="ref" reference="ocnrigmod"} remain valid for nondegenerate categories. More precisely, in Theorems [\[van\]](#van){reference-type="ref" reference="van"}, [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"} one only needs nondegeneracy of the category ${\mathcal C}$.

::: remark
We note that the nondegeneracy condition is essential. For example, if $A$ is the Hopf algebra ${\rm Fun}(G,k)$, where the order of $G$ is divisible by $p$, then Theorem [\[dualcat\]](#dualcat){reference-type="ref" reference="dualcat"} is false for $\text{Rep}(A)$, and Theorem [\[sscoss\]](#sscoss){reference-type="ref" reference="sscoss"} is false for $A$. Similarly, Theorem [\[van\]](#van){reference-type="ref" reference="van"} is false for $\text{Rep}(A)$ and the identity functor, since the corresponding cohomology is $H^i(G,k)$, which may be nonzero if the order of $G$ is divisible by $p$. However, we do not know a counterexample to Theorem [\[ocnrig\]](#ocnrig){reference-type="ref" reference="ocnrig"} in positive characteristic.
:::

**Sections 3-7.** While Section 3 makes no sense in positive characteristic, the material of Section 4 generalizes without changes, as long as one considers regular weak Hopf algebras. The only change in Section 5 is that one should always choose nonzero block sizes for the algebra $R$ (except subsections 5.8,5.9 where the characteristic should be zero). Theorems [\[acyclic\]](#acyclic){reference-type="ref" reference="acyclic"} and [\[rigweak\]](#rigweak){reference-type="ref" reference="rigweak"} are valid for nondegenerate weak Hopf algebras.

**Section 8.** The results of Section 8.1 generalize without changes, since they have nothing to do with the characteristic of the ground field. So do the results of Section 8.2, except Proposition [\[squar\]](#squar){reference-type="ref" reference="squar"}, Corollary [\[fpdual\]](#fpdual){reference-type="ref" reference="fpdual"}, and Proposition [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"}, which are valid for nondegenerate categories. Finally, let us point out that Theorem [\[quasihopf\]](#quasihopf){reference-type="ref" reference="quasihopf"} is valid in positive characteristic.

**Example.** A semisimple Hopf algebra $H$ is nondegenerate if and only if it is cosemisimple. Indeed, if $H$ is nondegenerate, then so is $\text{Rep}(H)$, and hence $H^*$ is semisimple, since $\text{Rep}(H^{*op})$ is a dual category to $\text{Rep}(H)$. Conversely, if $H$ is cosemisimple, then $\text{Tr}(S^2)\ne 0$ ([@LR1]), so the global dimension of $\text{Rep}(H)$ is nonzero, and $H$ is nondegenerate.
