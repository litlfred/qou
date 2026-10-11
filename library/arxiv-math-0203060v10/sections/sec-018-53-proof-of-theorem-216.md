---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-018-53-proof-of-theorem-216
section_title: "Proof of Theorem 2.16"
section_number: 5.3
pages: 19-20
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
text_source: latex
latex_prose_ratio: 0.701
latex_coverage_ratio: 0.861
---
Let ${\mathcal M}$ be a possibly decomposable module category over ${\mathcal C}$. So ${\mathcal M}=\oplus {\mathcal M}_j$ is a direct sum of indecomposable subcategories. Now for each $i$ choose semisimple algebras $R_i$ with blocks labeled by simple objects of ${\mathcal M}_i$, and let $R=\oplus R_i$. Let $F$ be the fiber functor ${\mathcal C}\to R-\text{bimod}$, associated to $({\mathcal M},R)$, and let $B=\text{End}_k(F)$ be the corresponding weak Hopf algebra. Then by Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"} and Corollary [\[dual semisimplicity condition\]](#dual semisimplicity condition){reference-type="ref" reference="dual semisimplicity condition"} applied to $A=B^*$, we find that $B^*$ is semisimple. In other words, the the category ${\mathcal C}^*_{{\mathcal M}}$ is semisimple. This implies Theorem [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"}, since the category ${\rm Fun}_{{\mathcal C}}({\mathcal M}_1,{\mathcal M}_2)$ is contained in ${\mathcal C}^*_{{\mathcal M}_1\oplus {\mathcal M}_2}$. Theorem [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"} is proved.

## A refinement of Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"}

Let $A$ be a connected, but not necessarily coconnected, semisimple weak Hopf algebra. Let $\pi_i$ be the primitive idempotents in $A^*_s\cap Z(A^*)$, and let $A_{ij}\subset A$ be defined by $A_{ij}^*=\pi_iA^*S(\pi_j)$. It is easy to see that $A_{ij}=p_jAp_i$, where $p_i$ are the primitive idempotents of $A_s\cap A_t$. In particular, $A_{ii}$ are semisimple algebras.

In fact, for every $i$ the algebra $A_{ii}$ has a natural structure of a biconnected weak Hopf algebra, and its representation category $\text{Rep}(A_{ii})$ is equivalent to $\text{Rep}(A)$ via the usual Morita equivalence $V\to p_i V$, $V\in \text{Rep}(A)$. Indeed, this map is a tensor functor since $\Delta(p_i) =(p_i\otimes p_i)\Delta(1)$. To prove that it is an equivalence it suffices to show that the central support $\hat p_i$ of $p_i$ equals $1$. From the formula for $\Delta(p_i)$ above we have $\Delta(\hat p_iA) \subset \hat p_iA\otimes \hat p_iA$. But $\hat{p_i}A$ contains the matrix block $q_0A$ corresponding to the trivial representation of $A$ (which is irreducible since $A$ is connected). Hence, $\Delta(q_0A)\subset \hat p_iA\otimes \hat p_iA$ and so $\hat p_i=1$.

Let $q_{ir}$ be the primitive idempotents of $Z(A_{rr})$. Let $n_{ir}^2=\dim(q_{ir}(A_{rr})_t)$. We have the following refinement of Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"}.

::: theorem
[]{#refine label="refine"} One has $\text{Tr}(S^2|_{q_{jr}A_{rs}S(q_{is})})=\dim(\text{Rep}(A))n_{jr}^2n_{is}^2$.
:::

::: proof
*Proof.* The proof is completely analogous to the proof of Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"}. Namely, let $g$ be an element of $A$ such that $gxg^{-1}=S^2(x)$. Then $p_rgp_r$ realizes $S^2$ in $A_{rr}$. Hence, as was shown in the proof of Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"} for any $V\in \text{Rep}(A)$, one has $$\text{Tr}(p_rgp_r|_{q_{ir}V})=\text{Tr}_V(g)n_{ir}^2,$$ and $$\text{Tr}(p_rg^{-1}p_r|_{S(q_{ir})V})=\text{Tr}_V((g^{-1})^*)n_{ir}^2.$$ Now, $A_{rs}=\oplus_{V}p_sV\otimes (p_rV)^*$, and $S^2|_{A_{rs}}=p_sgp_s\otimes (p_rg^{-1}p_r)^*$. Hence, taking the sum over all $V$, we arrive at the result. ◻
:::

## Proof of Proposition [\[samedim\]](#samedim){reference-type="ref" reference="samedim"}

Let ${\mathcal C}$ be an indecomposable multi-fusion category. Fix an index $r$ and let ${\mathcal M}=\oplus_i {\mathcal C}_{ir}$. It is clear that ${\mathcal M}$ is an indecomposable ${\mathcal C}$-module category, and the category ${\mathcal C}^*_{\mathcal M}:={\rm Fun}_{\mathcal C}({\mathcal M},{\mathcal M})$ equals ${\mathcal C}_{rr}^{op}$.

Choose a semisimple algebra $R$ with blocks labeled by simple objects of ${\mathcal M}$. Let $R_j$ be the two sided ideal in $R$ whose blocks are labeled by simple objects of $\oplus_i {\mathcal C}_{ij}\subset {\mathcal M}$. Let $n_j^2=\dim(R_j)$. Let $F$ be the corresponding fiber functor, and $B=\text{End}_k(F)$ the corresponding weak Hopf algebra, and let $A=B^*$. Then $A$ is connected and semisimple. Therefore, by Theorem [\[refine\]](#refine){reference-type="ref" reference="refine"}, $\text{Tr}(S^2|_{q_{jr}A_{rs}S(q_{is})})=\dim(\text{Rep}(A))n_{is}^2n_{jr}^2$. Thus, using Lemma [\[identify\]](#identify){reference-type="ref" reference="identify"}, we get $$\begin{aligned}
\dim({\mathcal C}_{rs})n_{is}^2n_{jr}^2
&=& \text{Tr}(S^2|_{(\epsilon\leftharpoonup q_{jr})A_{rs}^*S(\epsilon\leftharpoonup q_{is})})\\
&=& \text{Tr}(S^2|_{q_{jr}A_{rs}S( q_{is})})\\
&=& \dim(\text{Rep}(A))n_{is}^2n_{jr}^2,
\end{aligned}$$ so $\dim({\mathcal C}_{rs})=\dim(\text{Rep}(A))$, as desired.

## Proof of Theorem [\[multi-fus\]](#multi-fus){reference-type="ref" reference="multi-fus"}

Without loss of generality it can be assumed that the multi-fusion category ${\mathcal C}$ is indecomposable. Let ${\mathcal M}_1$, ${\mathcal M}_2$ be module categories over ${\mathcal C}$. Let $\mathbf 1_i$ be the simple constituents of the unit object of ${\mathcal C}$. Then it is shown in the standard way that for each $i$, the restriction functor ${\rm Fun_{{\mathcal C}}}({\mathcal M}_1,{\mathcal M}_2)\to {\rm Fun_{{\mathcal C}_i}}(\mathbf 1_i{\mathcal M}_1,
\mathbf 1_i{\mathcal M}_2)$ is an equivalence of categories (one can construct a quasi-inverse functor by extending a functor from $\mathbf 1_i{\mathcal M}_1$ to $\mathbf 1_j{\mathcal M}_1$ by tensoring with objects of ${\mathcal C}_{ij}$ and checking various compatibilities). Therefore, the result follows from Theorem [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"}.
