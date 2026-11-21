---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-039-81-definition-of-the-frobenius-perron-dimensions
section_title: "Definition of the Frobenius-Perron dimensions"
section_number: 8.1
pages: 29-31
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.894
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
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
