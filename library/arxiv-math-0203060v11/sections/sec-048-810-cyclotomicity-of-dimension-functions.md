---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-048-810-cyclotomicity-of-dimension-functions
section_title: "Cyclotomicity of dimension functions"
section_number: 8.10
pages: 41-42
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.944
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
[]{#cy label="cy"} The forgetful functor $Z({\mathcal C})\to {\mathcal C}$ induces a homomorphism of rings $F:K(Z({\mathcal C}))\to K({\mathcal C})$. It is clear that the image of this map is contained in the center $Z(K({\mathcal C}))$ of the ring $K({\mathcal C})$.

::: lemma
[]{#centers label="centers"} The map $K(Z({\mathcal C}))\otimes {\Bbb Q} \to Z(K({\mathcal C}))\otimes {\Bbb Q}$ is surjective.
:::

::: proof
*Proof.* Recall that $I: {\mathcal C}\to Z({\mathcal C})$ denotes the induction functor, that is the left adjoint to the forgetful functor $Z({\mathcal C})\to {\mathcal C}$. We will denote the induced map $K({\mathcal C})\to K(Z({\mathcal C}))$ by the same letter. Let $b_i$ be the basis of $K({\mathcal C})$. We have by Proposition [\[I(1)\]](#I(1)){reference-type="ref" reference="I(1)"} $F(I(x))=\sum_ib_ixb_i^*$ for any $x\in K({\mathcal C})$. In particular for $x\in Z(K({\mathcal C}))$ we have $F(I(x))=x\sum_ib_ib_i^*$. Finally note that the operator of multiplication by the element $\sum_ib_ib_i^*\in Z(K({\mathcal C}))$ is a self-adjoint positive definite operator $K({\mathcal C})\to K({\mathcal C})$ (with respect to the usual scalar product defined by $(b_i,b_j^*)=\delta_{ij}$) and hence invertible. The Lemma is proved. ◻
:::

::: remark
In the special case ${\mathcal C}=\text{Rep}(H)$ for some Hopf algebra $H$ Lemma [\[centers\]](#centers){reference-type="ref" reference="centers"} was proved in [@KSZ] 6.3.
:::

::: theorem
[]{#cyclotomic label="cyclotomic"} Let ${\mathcal C}$ be a fusion category over $\Bbb C$ and let $L$ be an irreducible representation of $K({\mathcal C})$. There exists a root of unity $\xi$ such that for any object $X$ of ${\mathcal C}$ one has $\text{Tr}([X],L)\in {\mathbb Z}[\xi]$.
:::

::: proof
*Proof.* First of all we can assume without loss of generality that the category ${\mathcal C}$ is spherical. Indeed as explained in Proposition [\[sphpiv\]](#sphpiv){reference-type="ref" reference="sphpiv"} we can construct a spherical fusion category $\tilde {\mathcal C}$ which projects onto ${\mathcal C}$; moreover the map $K(\tilde {\mathcal C})\to K({\mathcal C})$ is surjective and the simple objects of $\tilde {\mathcal C}$ map to the simple objects of ${\mathcal C}$.

Now let ${\mathcal C}$ be spherical and let $b_i$ be the basis of $K({\mathcal C})$. The element $e_L=\sum_i\text{Tr}(b_i,L)b_i^*$ is proportional to a primitive central idempotent in $K({\mathcal C})$, see e.g. [@Lu] 19.2 (b). By Lemma [\[centers\]](#centers){reference-type="ref" reference="centers"} there exists a primitive central idempotent $\tilde e_L\in K(Z({\mathcal C}))$ such that $e_L$ is proportional to $F(\tilde e_L)$. The element $\tilde e_L$ can expressed in terms of $S-$matrix of the category $Z({\mathcal C})$, see e.g. [@BaKi]. By Theorem [\[app\]](#app){reference-type="ref" reference="app"} there exists a root of unity $\xi$ such that the entries of $S-$matrix lie in ${\Bbb Q} (\xi)$ and thus $\tilde e_L\in K(Z({\mathcal C}))\otimes
{\Bbb Q} (\xi)$. Hence $e_L$ is proportional to some element of $K({\mathcal C})\otimes
{\Bbb Q} (\xi)$. Now the coefficient of $b_0=1\in K({\mathcal C})$ in $e_L$ equals to $\dim (L)\in {\Bbb Q} (\xi)$ and is nonzero. Hence $e_L\in K({\mathcal C})\otimes {\Bbb Q} (\xi)$ and $\text{Tr}(b_i,L)\in {\Bbb Q} (\xi)$. Obviously the number $\text{Tr}(b_i,L)$ is an algebraic integer and the ring of integers in $\Bbb Q(\xi)$ is $\Bbb Z[\xi]$. The Theorem is proved. ◻
:::

::: remark
Again in the case when ${\mathcal C}=\text{Rep}(H)$ for some Hopf algebra $H$ Theorem [\[cyclotomic\]](#cyclotomic){reference-type="ref" reference="cyclotomic"} is proved in [@KSZ] 6.3.
:::

::: corollary
Any irreducible representation of $K({\mathcal C})$ is defined over some cyclotomic field. In particular for any homomorphism $\phi: K({\mathcal C})\to {\mathbb{C}}$ we have $\phi (b_i)\in {\Bbb Q} [\xi]$ for some root of unity $\xi$.
:::

::: proof
*Proof.* Let ${\Bbb Q}^{ab}$ be the field of all cyclotomic numbers. We already proved that $K({\mathcal C})\otimes {\Bbb Q}^{ab}$ decomposes into direct sum of simple algebras (such decomposition is the same as the decomposition of $1\in K({\mathcal C})$ into the sum of primitive central idempotents). Now it is well known that the Brauer group of ${\Bbb Q}^{ab}$ is trivial. The result follows. ◻
:::

::: corollary
Let ${\mathcal C}$ be a fusion category over $\Bbb C$. There exists a root of unity $\xi$ such that for any object $X$ of ${\mathcal C}$ one has ${\rm FPdim}(X)\in {\mathbb Z}[\xi]$.
:::
