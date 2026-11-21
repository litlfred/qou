---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-003-22-semisimplification-of-a-spherical-tensor-cate
section_title: "Semisimplification of a spherical tensor category"
section_number: 2.2
pages: 4-5
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.974
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
We recall the theory of semisimplifications of spherical tensor categories, due to Barrett and Westbury, [@BW]. We give proofs for reader's convenience.

Let $\mathbf{k}$ be an algebraically closed field, and $\mathcal{C}$ be a spherical tensor category over $\mathbf{k}$ (see [@EGNO], Subsection 4.7).

::: definition
A morphism $f: X\to Y$ in $\mathcal{C}$ is called *negligible* if for any morphism $g: Y\to X$ one has $\text{Tr}(f\circ g)=0$.
:::

::: lemma
[]{#charneg label="charneg"} ([@B2], Exercise 3(ii), Subsection 2.18) Let $X=\oplus_i X_i$ and $Y=\oplus_j Y_j$ be decompositions of $X,Y$ into indecomposable objects, and $f=\oplus_{i,j}f_{ij}$ be a morphism $X\to Y$, where $f_{ij}: X_i\to Y_j$. Then $f$ is negligible if and only if for each $i,j$ either $\dim Y_j=0$ or $f_{ij}$ is not an isomorphism (equivalently, either $\dim X_i=0$ or $f_{ij}$ is not an isomorphism).
:::

::: proof
*Proof.* First let us prove the lemma when $X,Y$ are indecomposable. If $f: X\to Y$ is not an isomorphism, then for any $g: Y\to X$, the morphism $f\circ g: Y\to Y$ is not an isomorphism, either; otherwise $f$ is injective (hence not surjective) and $X\cong {\rm Im}f\oplus {\rm Ker}g$, with both summands nonzero, giving a contradiction. Hence, $f\circ g$ is nilpotent and $\text{Tr}(f\circ g)=0$. Also, if $f$ is an isomorphism (so $\dim X=\dim Y$) then for any $g: Y\to X$, one has $f\circ g=\lambda{\rm Id}+h$, where $\lambda\in \bold k$ and $h: Y\to Y$ is nilpotent. Hence $\text{Tr}(f\circ g)=\lambda \dim Y=\lambda \dim X$. If $\dim X=\dim Y=0$, this is always zero, while if $\dim X=\dim Y\ne 0$ then we can take $g=f^{-1}$ (so that $\lambda=1$), and $\text{Tr}(f\circ g)=\dim Y\ne 0$, as desired.

Now consider the general case. Suppose the condition of the lemma is satisfied, and $g: Y\to X$ is a morphism, $g=(g_{ji})$. Then $\text{Tr}(f\circ g)=\sum_{i,j}\text{Tr}(f_{ij}\circ g_{ji})$. If either $\dim Y_j=0$ or $f_{ij}$ is not an isomorphism (equivalently, either $\dim X_i=0$ or $f_{ij}$ is not an isomorphism) for all $i,j$ then by the indecomposable case, $\text{Tr}(f_{ij}\circ g_{ji})=0$ for all $i,j$, hence $\text{Tr}(f\circ g)=0$. However, if for some $i,j$ this condition is violated, then we can take $g_{ji}=f_{ij}^{-1}$ and $g_{pq}=0$ for $(p,q)\ne (i,j)$, so that $\text{Tr}(f\circ g)=\dim X_i=\dim Y_j$. This implies the lemma. ◻
:::

Let $\mathcal{N}(\mathcal{C})$ be the collection of negligible morphisms of $\mathcal{C}$.

::: lemma
[]{#tensid label="tensid"} $\mathcal{N}(\mathcal{C})$ is a tensor ideal in $\mathcal{C}$.
:::

::: proof
*Proof.* It is clear that a linear combination of negligible morphisms is negligible. Also, it is easy to see that $f\circ a, b\circ f$ are negligible for any $a,b$ (when these compositions make sense). It remains to show that the tensor products $a\otimes f$ and $f\otimes b$ are negligible. Let us prove this for $a\otimes f$, where $a: Z\to T$; the case of $f\otimes b$ is similar. Let $g: T\otimes Y\to Z\otimes X$. Then $\text{Tr}((a\otimes f)\circ g)=\text{Tr}(f\circ g')$, where $g':=\text{Tr}_T((a\otimes {\rm Id})\circ g)$. Hence $\text{Tr}((a\otimes f)\circ g)=0$ and $a\otimes f$ is negligible, as desired. ◻
:::

Thus we can define a spherical tensor category $\overline{\mathcal{C}}:=\mathcal{C}/\mathcal{N}(\mathcal{C})$.

::: proposition
[]{#semisi label="semisi"} The category $\overline{\mathcal{C}}$ is a semisimple tensor category. The simple objects of $\overline{\mathcal{C}}$ are the indecomposable objects of $\mathcal{C}$ of nonzero dimension.
:::

::: proof
*Proof.* It is clear that indecomposable objects of $\overline{\mathcal{C}}$ are images of indecomposable objects of $\mathcal{C}$. More precisely, if $X,Y\in \mathcal{C}$ are indecomposable then by Lemma [\[charneg\]](#charneg){reference-type="ref" reference="charneg"}, $\mathrm{Hom}_{\overline{\mathcal{C}}}(X,Y)=0$ if $X\ncong Y$ or $\dim X=0$ or $\dim Y=0$ (i.e., if $\dim X=0$, then $X=0$ in $\overline{\mathcal{C}}$), and $\dim \mathrm{Hom}_{\overline{\mathcal{C}}}(X,Y)=1$ if $X\cong Y$ and $\dim X\ne 0$. This implies the proposition. ◻
:::

::: definition
The category $\overline{\mathcal{C}}$ is called the *semisimplification* of $\mathcal{C}$.
:::

Note that the category $\overline{\mathcal{C}}$ comes equipped with a natural monoidal functor ${\bold S}: \mathcal{C}\to \overline{\mathcal{C}}$, which we call the *semisimplification functor*. This functor, however, is not a tensor functor, since it is not left or right exact, in general. We will denote the image ${\bold S}(X)$ of an object $X$ under this functor by $\overline{X}$.
