---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-041-83-comparison-of-the-global-and-frobenius-perron
section_title: "Comparison of the global and Frobenius-Perron dimensions"
section_number: 8.3
pages: 34-34
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.978
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
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
