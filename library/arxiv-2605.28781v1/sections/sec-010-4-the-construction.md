---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-010-4-the-construction
section_title: "The construction"
section_number: 4
pages: 9-11
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.677
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
In this section we use the algebraic number theory facts of the previous section to prove Theorems [\[th-main\]](#th-main){reference-type="ref" reference="th-main"} and [\[th-mainmult\]](#th-mainmult){reference-type="ref" reference="th-mainmult"}.

::: lemma
[]{#lem-main label="lem-main"} There exists an absolute constant $c>0$ such that the following holds. Let $K$ be a totally real number field of degree $d\geq 2$ with discriminant $\Delta_K$ and let $X,Y\geq 2$. There exists a set $A\subset \mathcal{O}_K$ such that $$\frac{(cXY)^d}{Y\Delta_K^{3/2}}\leq \mathopen{}\left| A\mathclose{}\right|\leq (XY/c)^d,$$ $$\lvert AA\rvert\leq c^{-d}Y^{1-d}\Delta_K^2\mathopen{}\left| A\mathclose{}\right|^2,$$ and $$\mathopen{}\left| A+A\mathclose{}\right|\leq (e^Y/c)^d\Delta_K^{1/2}\mathopen{}\left| A\mathclose{}\right|.$$
:::

Theorem [\[th-main\]](#th-main){reference-type="ref" reference="th-main"} is an immediate consequence, letting $K$ be a totally real field of sufficiently large degree $d\geq 2$ with $\Delta_K \leq C^d$ for some absolute constant $C>0$, as provided by Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}, and choosing $Y=4C^2c^{-1}$, say.

::: proof
*Proof.* Without loss of generality, we can assume that $X$ and $Y$ are both sufficiently large (in absolute terms), and that $X$ is an integer. Let $G=B^\times(Y)$, so that by Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} and Lemma [\[lem-regbound\]](#lem-regbound){reference-type="ref" reference="lem-regbound"} $$Y^{d-1}d^{-1/2}\Delta_K^{-1}\leq Y^{d-1}d^{-1/2}R_K^{-1}\leq \mathopen{}\left| G\mathclose{}\right|\leq 10(5Y+1)^{d-1}.$$ Since $GG\subseteq B^\times(2Y)$, $$\lvert GG\rvert\leq (CY)^{d-1}\leq (C')^d\Delta_K\mathopen{}\left| G\mathclose{}\right|$$ for some absolute constants $C,C'>0$. Let $\epsilon>0$ be some small absolute constant to be chosen soon, and $$P=X+B^+(\epsilon X),$$ so that by Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} $$(\epsilon X)^d\Delta_K^{-1/2}\leq\mathopen{}\left| P\mathclose{}\right|\leq(2\epsilon X+1)^d.$$ Let $A=GP$. We first claim that $\mathopen{}\left| A\mathclose{}\right|=\mathopen{}\left| G\mathclose{}\right|\mathopen{}\left| P\mathclose{}\right|$, for which it suffices to prove that if $u_1/u_2=p_1/p_2$ with $u_i\in G$ and $p_i\in P$ then $u_1= u_2$. This follows since $u_1/u_2\in \mathcal{O}_K^\times$, and for all embeddings $\sigma$ and $p\in P$, $$\sigma(p)\in [X-\epsilon X, X+\epsilon X],$$ whence $$\frac{1-\epsilon}{1+\epsilon}\leq \sigma(p_1/p_2)\leq \frac{1+\epsilon}{1-\epsilon}.$$ Hence, provided $\epsilon>0$ is sufficiently small and $X$ is sufficiently large (which we can assume without loss of generality), $\sigma(p_1/p_2)\in (\phi^{-1},\phi)$. So by Lemma [\[lem-unitsep\]](#lem-unitsep){reference-type="ref" reference="lem-unitsep"} we have $u_1/u_2\in \{\pm 1\}$, and in fact $u_1/u_2\neq -1$ since otherwise $\sigma(p_1/p_2)=-1$. Therefore there exist constants $0<c<C$ such that $$\frac{(cXY)^d}{Y\Delta_K^{3/2}}\leq \mathopen{}\left| A\mathclose{}\right|\leq (CXY)^d.$$ For the product set, we note (using the trivial bound $\mathopen{}\left| PP\mathclose{}\right|\leq \mathopen{}\left| P\mathclose{}\right|^2$) $$\lvert AA\rvert\leq \lvert GG\rvert\lvert PP\rvert\leq  c^{-d}Y^{1-d}\Delta_K^2\mathopen{}\left| A\mathclose{}\right|^2.$$ Finally, every $\alpha\in A$ is an algebraic integer such that $\lvert \sigma(\alpha)\rvert\leq 2Xe^Y$ for all $\sigma$, and hence $A+A\subseteq B^+(4Xe^Y)$. By Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} $$\mathopen{}\left| A+A\mathclose{}\right|\leq (Ce^YX)^d\leq (C'e^Y)^d\Delta_K^{1/2}\mathopen{}\left| A\mathclose{}\right|$$ (using $\mathopen{}\left| A\mathclose{}\right|\geq \mathopen{}\left| P\mathclose{}\right|\geq (\epsilon X)^d\Delta_K^{-1/2}$) for some absolute constants $C,C'>0$. ◻
:::

A similar construction works for the proof of Theorem [\[th-mainmult\]](#th-mainmult){reference-type="ref" reference="th-mainmult"} -- in fact here the construction is even simpler, since we can just take $A=B^\times(Y)$.

::: lemma
[]{#lem-mainmult label="lem-mainmult"} There exists an absolute constant $c>0$ such that the following holds. Let $K$ be a totally real number field of degree $d\geq 2$ with discriminant $\Delta_K$ and let $Y\geq 2$. There exists a set $A\subset \mathcal{O}_K$ such that $$\frac{(cY)^d}{Y\Delta_K^{3/2}}\leq \mathopen{}\left| A\mathclose{}\right|\leq (Y/c)^d$$ and $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert)\leq (ke^Y/c)^d\textrm{ for any }k\geq 2.$$
:::

Once again, Theorem [\[th-mainmult\]](#th-mainmult){reference-type="ref" reference="th-mainmult"} is an immediate consequence, letting $K$ be a totally real number field of large degree $d$ with $\Delta_K\leq C^d$ for some constant $C>0$ and choosing $Y=(C')^{1/\epsilon}$ for some other constant $C'$, so that $$\max(\mathopen{}\left| kA\mathclose{}\right|,\lvert A^{(k)}\rvert)\leq (ke^Y/c)^d\leq \mathopen{}\left| A\mathclose{}\right|^{C^{1/\epsilon}+\epsilon \log k}.$$ This proves the second statement; to prove the first take $\epsilon=C/\log\log k$ for some sufficiently large constant $C>0$ (note that the choice of $A$ then depends on $k$).

::: proof
*Proof.* We argue as in the previous lemma, except that we simply take $A=G=B^\times(Y)$, so that by Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} and Lemma [\[lem-regbound\]](#lem-regbound){reference-type="ref" reference="lem-regbound"} $$Y^{d-1}d^{-1/2}\Delta_K^{-1}\leq \mathopen{}\left| A\mathclose{}\right|\leq 10(5Y+1)^{d-1}.$$ For any $k\geq 2$, since $A^{(k)}\subseteq B^\times(kY)$, $$\lvert A^{(k)}\rvert\leq (CkY)^{d-1}$$ for some absolute constant $C>0$. Furthermore, $A\subseteq B^+(e^Y)$, and hence $kA\subseteq B^+(ke^Y)$, so $$\mathopen{}\left| kA\mathclose{}\right|\leq (Cke^Y)^d.\qedhere$$ ◻
:::
