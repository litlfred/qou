---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-031-8-frobenius-perron-dimensions
section_title: "Frobenius-Perron dimensions"
section_number: 8
pages: 29-34
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.92
---
In this section we will give some applications of the Frobenius-Perron theorem to the theory of fusion categories. We work with categories over ${\mathbb{C}}$.

## Definition of the Frobenius-Perron dimensions

We start by recalling the Frobenius-Perron theorem (see [@Ga]).

::: theorem
Let $A$ be a square matrix with nonnegative entries.

1.  $A$ has a nonnegative real eigenvalue. The largest nonnegative real eigenvalue $\lambda(A)$ of $A$ dominates absolute values of all other eigenvalues of $A$.

2.  If $A$ has strictly positive entries then $\lambda(A)$ is a simple positive eigenvalue, and the corresponding eigenvector can be normalized to have strictly positive entries.

3.  If $A$ has an eigenvector $\mathbf f$ with strictly positive entries, then the corresponding eigenvalue is $\lambda(A)$.
:::

Now let $A$ be a unital based ring of finite rank in the sense of Lusztig (see, e.g., [@O] for a definition). Let $b_i$ be the basis of $A$ ($b_0=1$), and $[b_i]$ be the matrix of multiplication by $b_i\in A$ in the basis $b_j$. This matrix has nonnegative entries. Let $\lambda_i$ be the largest nonnegative eigenvalue of $[b_i]$. Since $b_i$ is clearly not nilpotent, this eigenvalue is actually positive.

We will call $\lambda_i$ the *Frobenius-Perron dimension* of $b_i$. We note that Frobenius-Perron dimensions for commutative based rings were defined and used in the book [@FK].

::: theorem
[]{#fp0 label="fp0"} The assignment $b_i\to \lambda_i$ extends to a homomorphism of algebras $A\to \mathbb R$.
:::

::: proof
*Proof.* For any $j$ define $z_j=\sum_i b_ib_jb_i^*$. We claim that $z_j$ is central. Indeed, let $b_ib_j=\sum_k N_{ij}^kb_k$. Then $N_{ri}^k=N_{k^*r}^{i^*}$, so $$b_rz_j=b_r\sum_i b_ib_jb_i^*=\sum_{k,i}N_{ri}^kb_kb_jb_i^*=
\sum_{k,i}N_{k^*r}^{i^*}b_kb_jb_{i^*}=
\sum_k b_kb_jb_{k^*}b_r=z_jb_r.$$ Let $z=\sum_j z_j$. Since $z_j$ contain $b_j$ as a summand, the matrix $[z]$ of multiplication by $z=
\sum_j z_j$ has strictly positive entries. Let $\mathbf f$ be the unique eigenvector of $[z]$ with positive entries and $f_0=1$ (its existence and uniqueness follows from the Frobenius-Perron theorem). Then $[b_j]\mathbf f$ must be a multiple of $\mathbf f$, since $\mathbf f$ has positive entries and $[z][b_j]=[b_j][z]$. So by the Frobenius-Perron theorem, $[b_j]\mathbf f = \lambda_j\mathbf f$, whence the statement follows. ◻
:::

We note that $b_i\to \lambda_i$ is the unique homomorphism of $A$ to $\mathbb R$ such that images of the basis vectors are positive. This is demonstrated by the following simple and probably well known lemma.

Let $A$ be a $\mathbb Z_+$-ring of finite rank with $\mathbb Z_+$-basis $b_i$ (see [@O] for definition).

::: lemma
[]{#uniq label="uniq"} If there exists a homomorphism $\phi:A\to \mathbb R$ such that $\phi(b_i)>0$ for all $i$, then $\phi$ is unique.
:::

::: proof
*Proof.* Let $[b_i]$ be the matrix of multiplication by $b_i$ in the basis $b_j$, and $\mathbf f$ be the column vector with entries $\phi(b_j)$. Then $[b_i]\mathbf f=\phi(b_i)\mathbf f$. But $[b_i]$ is a matrix with nonnegative entries, and $\mathbf f$ has positive entries. Thus, by the Frobenius-Perron theorem, $\phi(b_i)$ is the largest positive eigenvalue of $[b_i]$, and hence is uniquely determined. Lemma is proved. ◻
:::

::: remark
M. Müger pointed out to us that for any $i$ one has $\lambda_i\ge 1$; moreover if $\lambda_i<2$ then $\lambda_i=
2\cos(\pi/n)$ for some integer $n\ge 3$ (this follows from the well known Kronecker theorem on the eigenvalues of positive integer matrices).
:::

One can also define the Frobenius-Perron dimensions of basis elements of a based module over a unital based ring. Indeed, let $M$ be an indecomposable based $A$-module with basis $m_j$ (see [@O] for definition).

::: proposition
[]{#frobmod0 label="frobmod0"} There exists a unique up to scaling common eigenvector $\mathbf m$ of the matrices $[b_i]|_M$ of the operators $b_i$ in $M$, which has strictly positive entries. The corresponding eigenvalues are $\lambda_i$.
:::

::: proof
*Proof.* Let $z$ be the element from the proof of Theorem [\[fp0\]](#fp0){reference-type="ref" reference="fp0"}. The matrix $[z]|_M$ has strictly positive entries. Let $\mathbf m$ be an eigenvector of $[z]|_M$ with positive entries. It exists and is unique up to a positive scalar, by the Frobenius-Perron theorem. Hence, it is an eigenvector of $[b_i]|_M$, and the eigenvalues are $\lambda_i$ by Lemma [\[uniq\]](#uniq){reference-type="ref" reference="uniq"}. ◻
:::

Now let ${\mathcal C}$ be a fusion category. Let $K({\mathcal C})$ be the Grothendieck ring of ${\mathcal C}$. For any object $X\in {\mathcal C}$, define the Frobenius-Perron dimension of $X$, ${\rm FPdim}(X)$, to be the largest positive eigenvalue of the matrix $[X]$ of multiplication by $X$ in $K({\mathcal C})$. Since $K({\mathcal C})$ is a unital based ring of finite rank, Theorem [\[fp0\]](#fp0){reference-type="ref" reference="fp0"} implies the following result.

::: theorem
[]{#fp label="fp"} The assignment $X\to {\rm FPdim}(X)$ extends to a homomorphism of algebras $K({\mathcal C})\to \mathbb R$.
:::

Similarly, one can define Frobenius-Perron dimensions of simple objects of a module category over a fusion category. Namely, let ${\mathcal M}$ be an indecomposable module category over a fusion category ${\mathcal C}$. For any $X\in {\mathcal C}$ let $[X]_{\mathcal M}$ be the matrix of action of $X$ on the Grothendieck group of ${\mathcal M}$. Since the Grothendieck group $K({\mathcal M})$ is an indecomposable based module over $K({\mathcal C})$, Proposition [\[frobmod0\]](#frobmod0){reference-type="ref" reference="frobmod0"} implies

::: proposition
[]{#frobmod label="frobmod"} There exists a unique up to scaling common eigenvector $\mathbf m$ of the matrices $[X]_{\mathcal M}$, which has strictly positive entries. The corresponding eigenvalues are ${\rm FPdim}(X)$.
:::

The entries $\mu_i$ of $\mathbf m$ are called the Frobenius-Perron dimensions of simple objects $M_i$ of ${\mathcal M}$. Unlike Frobenius-Perron dimensions of objects of ${\mathcal C}$, they are well defined only up to scaling.

## Frobenius-Perron dimension of a fusion category

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

## Comparison of the global and Frobenius-Perron dimensions

::: proposition
[]{#domi label="domi"} Let ${\mathcal C}$ be a fusion category. Then for any simple object $V$ of ${\mathcal C}$ one has $|V|^2\le {\rm FPdim}(V)^2$, and hence $\dim({\mathcal C})\le {\rm FPdim}({\mathcal C})$. Hence, if $\dim({\mathcal C})={\rm FPdim}({\mathcal C})$ then $|V|^2={\rm FPdim}(V)^2$ for all simple objects $V$.
:::

::: proof
*Proof.* Let $X_i$ be the $i$-th simple object of ${\mathcal C}$, and $d_i=d(X_i)$ be its dimension introduced in the proof of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}. Then $|d_i|^2=|V|^2$, and $d_i$ is an eigenvalue of the matrix $T_i$. It follows from Section 3 that the absolute values of the entries of $T_i$ are dominated by the corresponding entries of the matrix $N_i$ of multiplication by $X_i$. Let $f_i$ be the Frobenius-Perron dimension of $X_i$, and consider a norm on the Grothendieck group $Gr_{{\mathbb{C}}}({\mathcal C})$ given by $||\sum a_iX_i||=\sum f_i|a_i|$. Let us estimate the norm of the operator $T_i$. We have $$||T_i\mathbf a||=\sum_jf_j|\sum_k(T_i)_{jk}a_k|\le 
\sum_{j,k}f_j(N_i)_{jk}|a_k|=
f_i\sum_kf_k|a_k|=f_i||\mathbf a||$$ Thus, $||T_i||\le f_i$. This implies that $|V|^2\le f_i^2$, which proves the proposition. ◻
:::

::: proposition
[]{#divi label="divi"} Let ${\mathcal C}$ be a fusion category of global dimension $D$ and Frobenius-Perron dimension $\Delta$. Then $D/\Delta$ is an algebraic integer, which is $\le 1$.
:::

::: proof
*Proof.* By Proposition [\[domi\]](#domi){reference-type="ref" reference="domi"}, we only need to prove that $D/\Delta$ is an algebraic integer.

First of all, we can assume without loss of generality that ${\mathcal C}$ is a spherical category. Indeed, if ${\mathcal C}$ is not spherical, then, as explained in Proposition [\[sphpiv\]](#sphpiv){reference-type="ref" reference="sphpiv"}, we can construct a spherical fusion category $\tilde {\mathcal C}$ which projects onto ${\mathcal C}$. It is easy to see that this category has global dimension $2D$ and Frobenius-Perron dimension $2\Delta$, so the ratio of dimensions is the same.

Now assume that ${\mathcal C}$ is spherical. Consider the Drinfeld center $Z({\mathcal C})$. This is a modular category of global dimension $D^2$, and by Proposition [\[squar\]](#squar){reference-type="ref" reference="squar"}, its Frobenius-Perron dimension is $\Delta^2$. Let $S=(s_{ij})$ be its S-matrix. It follows from Verlinde's formula (see [@BaKi]) that the commuting matrices $N_i$ of multiplication by simple objects $X_i$ of $Z({\mathcal C})$ have common eigenvectors $\mathbf v_j$ with eigenvalues $s_{ij}/s_{0j}$. In particular, there exists a unique (by nondegeneracy of $S$) distinguished label $j=r$ such that $s_{ir}/s_{0r}=f_i$, the Frobenius-Perron dimension of $X_i$. Since $S$ is symmetric, and $S^2$ is the charge conjugation matrix, we have $\Delta^2=\sum_i f_i^2=\delta_{rr^*}/s_{0r}^2$. Thus $r=r^*$ and $\Delta^2=1/s_{0r}^2=D^2/d_r^2$, where $d_r$ is the categorical dimension of the $r$-th simple object. So $D^2/\Delta^2=d_r^2$ is an algebraic integer. ◻
:::
