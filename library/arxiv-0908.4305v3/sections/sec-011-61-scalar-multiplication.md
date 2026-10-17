---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-011-61-scalar-multiplication
section_title: "Scalar Multiplication"
section_number: 6.1
pages: 52-53
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.896
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#scalar_mult label="scalar_mult"}

To prove facts about scalar multiplication, we use the following lemma:

::: lemma
[]{#essinverseproduct label="essinverseproduct"} Given a groupoid $\Lambda$ and a functor between groupoids $p\colon X\rightarrow Y$, then the functor $c\times p \colon\Lambda\times Y\rightarrow 1\times X$ (where $c\colon\Lambda\rightarrow 1$ is the unique morphism from $\Lambda$ to the terminal groupoid $1$) satisfies: $$|(c\times p)^{-1}(1, x)|=|\Lambda| \, |p^{-1}(x)|$$ for all $x \in X$.
:::

::: proof
*Proof.* By the definition of full inverse image we have $$(c\times p)^{-1}(1, x) \cong\Lambda \times p^{-1}(x)  .$$ In the product $\Lambda \times p^{-1}(x)$, an automorphism of an object $(\lambda,y)$ is an automorphism of $\lambda$ together with an automorphism of $y$. We thus obtain $$|(c\times p)^{-1}(1, x)| = 
\sum_{[\lambda] \in \underline{\Lambda}} \;
\sum_{[y]\in \underline{p^{-1}(x)}} 
\frac{1}{|{\rm Aut}(\lambda)|} \,
\frac{1}{|{\rm Aut}(y)|}$$ which is equal to $|\Lambda|\,|p^{-1}(x)|$, as desired. ◻
:::

::: proposition
[]{#scalarmult1 label="scalarmult1"} Given a groupoid $\Lambda$ and a groupoid over $X$, say $v \colon\Psi \rightarrow X$, the groupoid $\Lambda \times \Psi$ over $X$ satisfies $$\utilde{\Lambda \times \Psi} = |\Lambda|\utilde{\Psi}.$$
:::

::: proof
*Proof.* This follows from Lemma [\[essinverseproduct\]](#essinverseproduct){reference-type="ref" reference="essinverseproduct"}. ◻
:::

::: proposition
[]{#scalarmult2 label="scalarmult2"} Given a tame groupoid $\Lambda$ and a tame span $$\xymatrix{
& S\ar[dl] \ar[dr] & \\
Y & & X
}$$ then $\Lambda \times S$ is tame and $$\utilde{\Lambda \times S} = |\Lambda| \, \utilde{S}.$$
:::

::: proof
*Proof.* This follows from Lemma [\[essinverseproduct\]](#essinverseproduct){reference-type="ref" reference="essinverseproduct"}. ◻
:::
