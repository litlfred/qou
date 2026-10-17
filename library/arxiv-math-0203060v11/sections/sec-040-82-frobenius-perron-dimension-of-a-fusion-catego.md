---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-040-82-frobenius-perron-dimension-of-a-fusion-catego
section_title: "Frobenius-Perron dimension of a fusion category"
section_number: 8.2
pages: 31-34
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.951
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let ${\mathcal C}$ be a fusion category. Define the Frobenius-Perron dimension ${\rm FPdim}({\mathcal C})$ of ${\mathcal C}$ to be the sum of squares of Frobenius-Perron dimensions of simple objects of ${\mathcal C}$.

Also, define the regular representation $R_{\mathcal C}$ to be the (virtual) object $\oplus_{X\in Irr({\mathcal C})} {\rm FPdim}(X)X$, where $Irr({\mathcal C})$ is the set of isomorphism classes of simple objects of ${\mathcal C}$. It is clear that ${\rm FPdim}({\mathcal C})={\rm
  FPdim}(R_{\mathcal C})$.

::: proposition
[]{#freeness label="freeness"} Let $F:{\mathcal C}\to {\mathcal D}$ be a surjective tensor functor between fusion categories. Then $F(R_{\mathcal C})=\frac{{\rm FPdim}({\mathcal C})}{{\rm FPdim}({\mathcal D})}R_{\mathcal D}$.
:::

::: proof
*Proof.* Let $X$ be an object of ${\mathcal C}$ such that $F(X)$ contains all simple objects of ${\mathcal D}$. It exists since $F$ is surjective. The vectors of multiplicities of $F(R_{\mathcal C})$ and $R_{\mathcal D}$ are eigenvectors of the matrix of multiplication by $F(X)$. The matrix and the vectors have strictly positive entries. By the Frobenius-Perron theorem, this implies that $F(R_{\mathcal C})$ and $R_{\mathcal D}$ differ by a positive scalar. This scalar is readily found to be the claimed one by taking ${\rm FPdim}$ of $F(R_{\mathcal C})$ and $R_{\mathcal D}$. ◻
:::

::: corollary
[]{#freeness1 label="freeness1"} Let $A\subset B$ be an inclusion of finite dimensional semisimple quasi-Hopf algebras. Then $B$ is free as a left $A$-module.
:::

::: proof
*Proof.* In this case Frobenius-Perron dimensions coincide with the usual ones, so if ${\mathcal C}=\text{Rep}(B)$, ${\mathcal D}=\text{Rep}(A)$ then $R_{\mathcal C}=B$, $R_{\mathcal D}=A$, proving the claim. ◻
:::

::: remark
For Hopf algebras, Corollary [\[freeness1\]](#freeness1){reference-type="ref" reference="freeness1"} is the well known freeness theorem of Nichols and Zoeller [@NZ] (it is true in the nonsemisimple case as well). In the quasi-Hopf case it was independently obtained by P. Schauenburg (without the semisimplicity assumption), [@Scha].
:::

::: corollary
[]{#divis label="divis"} If $F:{\mathcal C}\to {\mathcal D}$ is surjective then ${\rm
    FPdim}({\mathcal C})$ is divisible by ${\rm FPdim({\mathcal D})}$ (i.e. the ratio is an algebraic integer).
:::

::: proof
*Proof.* Taking the multiplicity of the neutral object of ${\mathcal D}$ in Proposition [\[freeness\]](#freeness){reference-type="ref" reference="freeness"}, we find $\sum_{X\in Irr({\mathcal C})}{\rm FPdim}(X)[F(X):\mathbf 1]=
\frac{{\rm FPdim}({\mathcal C})}{{\rm FPdim}({\mathcal D})}$, which yields the statement. ◻
:::

::: proposition
[]{#squar label="squar"} For any fusion category ${\mathcal C}$, one has ${\rm FPdim}(Z({\mathcal C}))={\rm FPdim}({\mathcal C})^2$.
:::

::: remark
If ${\mathcal C}$ is a representation category of a quasi-Hopf algebra $A$, then Proposition [\[squar\]](#squar){reference-type="ref" reference="squar"} is saying that the Frobenius-Perron dimension of $Z({\mathcal C})$ is $\dim(A)^2$. This is a simple consequence of the result of Hausser and Nill [@HN], who constructed a quasi-Hopf algebra $D(A)$ (the double of $A$), isomorphic to $A\otimes A^*$ as a vector space, such that $Z({\mathcal C})=\text{Rep}(D(A))$.
:::

::: proof
*Proof.* Recall from Section 5 that $V\to I(V)$ denotes the induction functor. By Proposition [\[I(1)\]](#I(1)){reference-type="ref" reference="I(1)"}, we have $$\begin{aligned}
{\rm FPdim}(I(V))
&=& \oplus_{X\in Irr(Z({\mathcal C}))}{\rm FPdim}(X)[I(V):X]\\
&=& \oplus_{X\in Irr(Z({\mathcal C}))}{\rm FPdim}(X)[X|_{\mathcal C}:V] \\
&=& [R_{Z({\mathcal C})}:V]=\frac{{\rm FPdim}Z({\mathcal C})}{{\rm FPdim}{\mathcal C}}
[R_{\mathcal C}:V]=\frac{{\rm FPdim}Z({\mathcal C})}{{\rm FPdim}{\mathcal C}}{\rm FPdim}(V).
\end{aligned}$$ In particular, ${\rm FPdim}(I(\mathbf 1))=\frac{{\rm
    FPdim}Z({\mathcal C})}{{\rm FPdim}{\mathcal C}}$.

On the other hand, by Proposition [\[I(1)\]](#I(1)){reference-type="ref" reference="I(1)"}, $I(\mathbf 1)=\oplus_{Y\in
  Irr({\mathcal C})}Y\otimes Y^*$, which implies the desired statement (since the dimension of the right hand side is ${\rm
  FPdim}({\mathcal C})$). The proposition is proved. ◻
:::

::: corollary
[]{#fpdual label="fpdual"} Let ${\mathcal C}$ be a fusion category and ${\mathcal C}^*$ be its dual with respect to an indecomposable module category. Then ${\rm FPdim}({\mathcal C})={\rm FPdim}({\mathcal C}^*)$.
:::

::: proof
*Proof.* This follows from Proposition [\[squar\]](#squar){reference-type="ref" reference="squar"} and the fact that $Z({\mathcal C})$ is equivalent to $Z({\mathcal C}^*)$ [@O1; @Mu2]. ◻
:::

::: proposition
[]{#subdivi label="subdivi"} Let ${\mathcal C}$ be a full tensor subcategory of a fusion category ${\mathcal D}$. Then ${\rm FPdim}({\mathcal D})/{\rm FPdim}({\mathcal C})$ is an algebraic integer.
:::

::: proof
*Proof.* Consider the decomposition of ${\mathcal D}$, as a left module category over ${\mathcal C}$, in a direct sum of indecomposables. We have ${\mathcal D}=\oplus_{i=1}^r {\mathcal M}_r$. Let us consider the duals of ${\mathcal C}$ and ${\mathcal D}$ with respect to this module category. We have ${\mathcal D}^*={\mathcal D}^{op}$, and ${\mathcal C}^*$ is a multi-fusion category ${\mathcal C}^*=\oplus_{i,j=1}^r {\mathcal C}^*_{ij}$, where ${\mathcal C}^*_{ij}:={\rm Fun}({\mathcal M}_j,{\mathcal M}_i)$. Note that the Frobenius-Perron dimensions of ${\mathcal C}_{ii}^*$ are equal to ${\rm FPdim}({\mathcal C})$ by Corollary [\[fpdual\]](#fpdual){reference-type="ref" reference="fpdual"}.

Let $E_{ij}$ denote nonzero virtual objects of ${\mathcal C}^*_{ij}$, which satisfy the condition $X\otimes E_{ij}\otimes Y=
{\rm FPdim}(X){\rm FPdim}(Y)E_{ij}$, $X\in {\mathcal C}^*_{ii},Y\in
{\mathcal C}^*_{jj}$. Since the category ${\mathcal C}_{ij}^*$ is an indecomposable bimodule over ${\mathcal C}_{ii}^*$ and ${\mathcal C}_{jj}^*$, by the Frobenius-Perron theorem, the object $E_{ij}$ is unique up to scaling. We require that the coefficients in $E_{ij}$ be positive, which determines it uniquely up to a positive scalar.

To fix the scaling completely, we will require that $E_{ii}$, which is a multiple of the regular representation $R_{ii}$ in ${\mathcal C}^*_{ii}$, be actually equal to ${\rm FPdim}({\mathcal C})^{-1}R_{ii}$. Further, we normalize $E_{1j}$ arbitrarily, then normalize $E_{j1}$ by the condition $E_{j1}\otimes E_{1j}=E_{jj}$, and finally define $E_{jk}$ as $E_{j1}\otimes E_{1k}$. It is easy to see that $E_{ij}$ satisfy the matrix unit relations $E_{ij}\otimes E_{kl}=\delta_{jk}E_{il}$.

Now let $F:{\mathcal D}^*\to {\mathcal C}^*$ be the natural functor, $R$ be the regular representation of ${\mathcal D}^*$, and consider $F(R)\in {\mathcal C}^*$. We claim that $F(R)=\oplus_{i,j} b_{ij}E_{ij}$, where $b_{ij}>0$. Indeed, $F(R)^{\otimes 2}={\rm FPdim}({\mathcal D})F(R)$, so for any $i$ the virtual object $L_i:=\oplus_j b_{ij}E_{ij}$ is an eigen-object of the functor of right multiplication by $F(R)$. Since the category $\oplus_j {\mathcal C}_{ij}^*$ is an indecomoposable right module over ${\mathcal C}^*$, by the Frobenius-Perron theorem such eigen-object with positive coefficients is unique up to scaling. Thus, for any $X\in {\mathcal C}_{ii}^*$, $X\otimes L_i=c(X)L_i$, where $c(X)$ is a scalar. By the Frobenius-Perron theorem $c(X)={\rm
  FPdim}(X)$. Similarly, $P_j:=\oplus_i b_{ij}E_{ij}$ satisfies $P_j\otimes X={\rm FPdim}(X)P_j$, $X\in {\mathcal C}^*_{jj}$. This implies the claim.

Now let $B$ be the matrix $(b_{ij})$. Since $F(R)^{\otimes 2}={\rm FPdim}({\mathcal D})F(R)$, and $E_{ij}$ behave like matrix units, we have $B^2={\rm
  FPdim}({\mathcal D})B$. Thus eigenvalues of $B$ are ${\rm FPdim}({\mathcal D})$ and zero, and $B$ is diagonalizable. Since $b_{ij}>0$, by the Frobenius-Perron theorem the multiplicity of the eigenvalue ${\rm FPdim}({\mathcal D})$ is $1$, so the rank of $B$ is $1$. Hence $\text{Tr}(B)={\rm FPdim}({\mathcal D})$.

On the other hand, let us compute $b_{ii}$. We have $$\sum_{X\in Irr({\mathcal D})}{\rm FPdim}(X)[F(X):\mathbf 1_{ii}]=
b_{ii}/{\rm FPdim}({\mathcal C})$$ (as $E_{ii}=R_{ii}/{\rm
  FPdim}({\mathcal C})$). Thus, $b_{ii}/{\rm FPdim}({\mathcal C})$ is an algebraic integer. Summing over all $i$, we find that $\text{Tr}(B)/{\rm FPdim}({\mathcal C})={\rm FPdim}({\mathcal D})/{\rm FPdim}({\mathcal C})$ is an algebraic integer, as desired. ◻
:::

::: remark
Since $b_{ii}\ge 1$, we see that ${\rm FPdim}({\mathcal D})/{\rm FPdim}({\mathcal C})$ dominates the number of indecomposable blocks in ${\mathcal D}$ as a left ${\mathcal C}$-module category.
:::

::: remark
Let ${\mathcal M}_1={\mathcal C}$. Then ${\mathcal C}_{i1}^*={\mathcal M}_i$. It is easy to see that $F(R)_{i1}=\sum_{X\in Irr({\mathcal M}_i)}
{\rm FPdim}(X)X$. By uniqueness of eigen-object of $F(R)$ in $\oplus_j{\mathcal C}^*_{ji}$, we have $F(R)_{i1}\otimes F(R)_{1i}=
{\rm FPdim}({\mathcal C})F(R)_{ii}$. Thus, $$[F(R)_{ii}:\mathbf 1_{ii}]=\dim{\rm End}(F(R)_{i1},F(R)_{i1})/{\rm
FPdim}({\mathcal C})={\rm FPdim}({\mathcal M}_i)/{\rm FPdim}({\mathcal C}).$$ This implies the refinement of Theorem [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"} stating that ${\rm FPdim}({\mathcal M}_i)/{\rm FPdim}({\mathcal C})$ is an algebraic integer.
:::

::: remark
We do not know if the global dimension of a fusion category is divisible by the global dimension of its full tensor subcategory.
:::

::: example
The following example shows that Proposition [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"} is a property of tensor categories and not just of based rings.

Let $G$ be a finite group and $n$ a nonnegative integer. Consider the based ring $A_n(G)$ with basis $G\cup \lbrace
X\rbrace$, with multiplication given by the usual multiplication in $G$ and the relations $gX=Xg=X,g\in G$, and $X^2=nX+\sum_{g\in
  G}g$. Such rings for special $n,G$ can arise as Grothendieck rings of fusion categories (for example, the categories of [@TY], or representation categories of affine groups ${\rm Aff}(\mathbb F_q)$). We claim that if $A_n(G)$ is categorifiable, then the number $(n+\sqrt{n^2+4|G|})^2/4|G|$ is an algebraic integer. In particular, for $n\ne 0$ one has $|G|\le 2n^2$. (For $n=1$ we find $|G|=1,2$, so $G=1$ or $G=\mathbb Z/2\mathbb Z$, which was proved by T. Chmutova even for non-rigid categories). Indeed, let ${\mathcal C}$ be a fusion category with Grothendieck ring $A_n(G)$. Then the Frobenius-Perron dimensions of elements of $G$ are $1$, while the Frobenius-Perron dimension of $X$ is the largest root of the equation $x^2-nx-m=0$, where $m=|G|$. Thus $x=\frac{1}{2}(n+\sqrt{n^2+4m})$. By Proposition [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"}, $x^2/m$ should be an algebraic integer.
:::

::: proposition
[]{#dimgradi label="dimgradi"} If a fusion category ${\mathcal C}$ is faithfully graded by a finite group $G$, then the Frobenius-Perron dimensions of ${\mathcal C}_g$ are equal for all $g\in G$. In particular, $|G|$ divides ${\rm FPdim}({\mathcal C})$.
:::

::: proof
*Proof.* Let $R$ be the regular object of ${\mathcal C}$. Then $R=\oplus R_g$, where $R_g$ is a virtual object of ${\mathcal C}_g$. We have $R\otimes R_h={\rm FPdim}(R_h)R$. Taking the $gh$-th component of this equation, we find $R_g\otimes R_h={\rm FPdim}(R_h)R_{gh}$. Similarly, $R_g\otimes R={\rm FPdim}(R_g)R$, which yields $R_g\otimes R_h={\rm FPdim}(R_g)R_{gh}$. Since $R_{gh}\ne 0$, we get ${\rm FPdim}(R_g)={\rm FPdim}(R_h)$, i.e. ${\rm FPdim}(R_g)={\rm FPdim}(X)/|G|$. ◻
:::
