---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-009-32-the-unit-lattice
section_title: "The unit lattice"
section_number: 3.2
pages: 8-9
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.738
latex_coverage_ratio: 0.989
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
The group of units $\mathcal{O}_K^\times$ of $K$ is the set of algebraic integers $\alpha$ such that $\alpha^{-1}$ is also an algebraic integer. By Dirichlet's unit theorem (see, for example, [@Ne99 Chapter 1.7]) the group of units (modulo the roots of unity) $\mathcal{O}_K^\times/\{\pm 1\}$ can be viewed as a lattice of rank $d-1$ in $\mathbb{R}^{d}$ via the embedding $$u\mapsto (\log \mathopen{}\left| \sigma_1(u)\mathclose{}\right|,\ldots,\log \mathopen{}\left| \sigma_d(u)\mathclose{}\right|).$$ This is a lattice of rank $d-1$ inside the hyperplane $$H=\{ x\in \mathbb{R}^d : x_1+\cdots+x_d=0\}.$$ The covolume of this lattice in $H$ is $\sqrt{d}R_K$, where $R_K$ is the regulator (see [@Ne99 Chapter 1, Proposition 7.5]). We write $$B^\times(Y) = \{ \alpha \in \mathcal{O}_K^\times : \mathopen{}\left| \log\mathopen{}\left| \sigma_i(\alpha)\mathclose{}\right|\mathclose{}\right|\leq Y\textrm{ for all }1\leq i\leq d\}.$$ We note here the trivial, but crucial, fact that integers in $B^\times(Y)$ are still bounded in the additive sense also, so that $$B^\times(Y)\subseteq B^+(e^Y).$$

It is a well-known fact that points in the unit lattice are separated by an absolute constant (independent of both the field and degree). This follows, for example, from Schinzel's lower bound for the Mahler measure [@Schinzel1973 Theorem 2]. For our purposes the following simple lemma (suggested by GPT-5.5 Pro) will suffice. Let $\phi=\frac{1+\sqrt{5}}{2}$, so that $0\leq x^2+x^{-2}-2<1$ whenever $x\in (\phi^{-1},\phi)$.

::: lemma
[]{#lem-unitsep label="lem-unitsep"} If $u\in \mathcal{O}_K^\times$ and $\phi^{-1}< \lvert \sigma_i(u)\rvert<\phi$ for all $1\leq i\leq d$ then $u\in\{\pm 1\}$.
:::

::: proof
*Proof.* Let $\alpha=u^2+u^{-2}-2\in \mathcal{O}_K$. If $\alpha \neq 0$ then, for each embedding $\sigma$, we have $$0<\sigma(u)^2+\sigma(u)^{-2}-2<1,$$ so $\sigma(\alpha)\in (0,1)$. This contradicts that $N(\alpha)=\prod \sigma(\alpha)$ must be an integer. It follows that $\alpha=0$, whence $u^2=1$ and so $u\in \{\pm 1\}$. ◻
:::

The proof of the following is similar to that of Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"}.

::: lemma
[]{#lem-ball-mult label="lem-ball-mult"} Let $K$ be a totally real number field of degree $d$. For any $Y\geq 1$ $$Y^{d-1}d^{-1/2}R_K^{-1}\leq \lvert B^\times(Y)\rvert\leq 10(5Y+1)^{d-1}.$$
:::

In the proof of Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} we will require bounds on the $(d-1)$-dimensional volume of $H\cap \{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq r\}$. Hensley [@He79] proved that $$\label{eq-hensley}
    (2r)^{d-1}\leq \mathrm{vol}_{d-1}(H\cap \{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq r\})\leq 5(2r)^{d-1}.$$ In fact, the central limit theorem implies that this volume is $\sim \sqrt{6/\pi}(2r)^{d-1}$ as $d\to \infty$ (a remark which Hensley attributes to Selberg).

::: proof
*Proof.* Losing only a factor of $2$ (since $u$ and $-u$ are both mapped to the same vector) the set $B^\times(Y)$ can be viewed as a subset of the $L^\infty$ ball of radius $Y$, intersected with the hyperplane $H$. Moreover, by Lemma [\[lem-unitsep\]](#lem-unitsep){reference-type="ref" reference="lem-unitsep"}, points in this lattice are at least $(\log \phi)$-separated in the $L^\infty$ norm. Indeed, if $x,y\in \mathcal{O}_K^\times$ and $x\not\in \{y,-y\}$ then $x/y\in \mathcal{O}_K^\times \backslash \{\pm 1\}$, and hence there exists $\sigma$ such that $$\lvert \sigma(x)\rvert/\lvert \sigma(y)\rvert \not\in(\phi^{-1},\phi).$$ Combining the same standard packing argument as in the proof of Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} with [\[eq-hensley\]](#eq-hensley){reference-type="eqref" reference="eq-hensley"}, there are at most $5(\frac{2}{c}Y+1)^{d-1}$ many $c$-separated points in $H$ intersected with an $L^\infty$ ball of radius $Y$. This proves the upper bound since $2/\log(\phi)<5$.

For the lower bound, we use the same idea as before: the covolume of the lattice is $\sqrt{d}R_K$, and hence there exists some $a$ such that the number of lattice points in $a+\{ x\in H : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq Y/2\}$ is at least $$\frac{\mathrm{vol}_{d-1}(\{ x\in H: \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq Y/2\})}{\sqrt{d}R_K}\geq \frac{Y^{d-1}}{\sqrt{d}R_K}.$$ The conclusion now follows by taking the difference set of these points. ◻
:::
