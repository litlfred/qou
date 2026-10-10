---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-008-3-algebraic-number-theory
section_title: "Algebraic number theory"
section_number: 3
pages: 7-8
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
text_source: latex
latex_prose_ratio: 0.744
latex_coverage_ratio: 0.798
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
In this section we review the necessary concepts required from algebraic number theory; with the exception of Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}, these are all classical results that can be found in most textbooks on the subject.

Let $K$ be a totally real number field of degree $d$ over $\mathbb{Q}$, and let $\Delta_K$ be the discriminant of $K$ (which is strictly positive if $K$ is totally real). Let $R_K$ be the regulator of $K$. For those unfamiliar with algebraic number theory, the important role of these parameters for our purposes is that they control the covolume of the lattices of the algebraic integers and units respectively. The only fact that we will require about $K$ (aside from it being totally real) is that these are both bounded above by $O(1)^d$. This is usually done with emphasis on $\Delta_K$, but similar control on $R_K$ follows from the following lemma.

::: lemma
[]{#lem-regbound label="lem-regbound"} If $K$ is a totally real number field of degree $d\geq 2$ then $$R_K \leq \Delta_K.$$
:::

::: proof
*Proof.* As in the proof of [@La70 XIII, Theorem 3], for any real $s>1$, if $h_K$ is the class number of $K$ then $$2^dR_Kh_K\leq 2s(s-1)(\pi^{-d/2}\Delta_K^{1/2})^s \Gamma(s/2)^d\zeta(s)^d.$$ In particular, letting $s=2$, since $h_K\geq 1$ and $d\geq 2$, $$R_K\leq R_Kh_K \leq 4(\pi/12)^d\Delta_K\leq \Delta_K.\qedhere$$ ◻
:::

It therefore suffices to produce $K$ with $\Delta_K\leq O(1)^d$, for arbitrarily large $d$. Such towers were first constructed by Martinet [@Ma78].

::: theorem
[]{#th-tower label="th-tower"} There exists an absolute constant $C>0$ such that, for infinitely many $d$, there exist totally real number fields $K$ with degree $d$ with $\Delta_K\leq C^d$.
:::

There are $d$ embeddings $K\hookrightarrow \mathbb{R}$. These let us view the algebraic integers as $d$-dimensional lattices. As we are concerned with both sums and products, both the additive and multiplicative versions of these lattices will be useful to us.

## The additive lattice

The ring of algebraic integers $\mathcal{O}_K$ can be viewed as a lattice of rank $d$ in $\mathbb{R}^d$ via the Minkowski embedding $$\alpha \mapsto (\sigma_1(\alpha),\ldots,\sigma_d(\alpha)),$$ where $\sigma_1,\ldots,\sigma_d$ are the embeddings $\sigma_i\colon K\hookrightarrow \mathbb{R}$. The covolume of this lattice is $\Delta_K^{1/2}$ (see [@La70 V, Lemma 2]). We write $$B^+(X) = \{ \alpha \in \mathcal{O}_K : \mathopen{}\left| \sigma_i(\alpha)\mathclose{}\right|\leq X\textrm{ for all }1\leq i\leq d\}.$$

::: lemma
[]{#lem-ball label="lem-ball"} Let $K$ be a totally real number field of degree $d$. For any $X\geq 1$ $$X^{d}\Delta_K^{-1/2}\leq \lvert B^+(X)\rvert\leq (2X+1)^{d}.$$
:::

::: proof
*Proof.* In the embedding described above, $B^+(X)$ is contained inside the $L^\infty$ ball of radius $X$. Moreover, points in this lattice are at least $1$-separated in the $L^\infty$ norm: if $x\neq y\in \mathcal{O}_K$ then, since $x-y$ is a non-zero algebraic integer, it has a non-zero integral norm. Furthermore, since $N(\alpha)=\prod_{i=1}^d \sigma_i(\alpha)$, we deduce $$1\leq \lvert N(x-y)\rvert\leq \prod_{i=1}^d\lvert \sigma_i(x-y)\rvert,$$ so there must exist $1\leq i\leq d$ such that $\lvert \sigma_i(x)-\sigma_i(y)\rvert\geq 1$. By a standard packing argument (for example, placing disjoint balls of radius $1/2$ around each lattice point) there are at most $(2X+1)^{d}$ many $1$-separated points in a ball of radius $X$, and we are done.

For the lower bound we use Blichfeldt's lemma: the covolume of the lattice is $\Delta_K^{1/2}$, and hence there exists some $a$ such that the number of lattice points in $a+\{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq X/2\}$ is at least $$\frac{\mathrm{vol}(\{ x: \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq X/2\})}{\Delta_K^{1/2}}= \frac{X^{d}}{\Delta_K^{1/2}}.$$ The conclusion now follows by taking the difference set of these points. ◻
:::

## The unit lattice

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

In the proof of Lemma [\[lem-ball-mult\]](#lem-ball-mult){reference-type="ref" reference="lem-ball-mult"} we will require bounds on the $(d-1)$-dimensional volume of $H\cap \{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq r\}$. Hensley [@He79] proved that $$\begin{equation}
\label{eq-hensley}
    (2r)^{d-1}\leq \mathrm{vol}_{d-1}(H\cap \{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq r\})\leq 5(2r)^{d-1}.
\end{equation}$$ In fact, the central limit theorem implies that this volume is $\sim \sqrt{6/\pi}(2r)^{d-1}$ as $d\to \infty$ (a remark which Hensley attributes to Selberg).

::: proof
*Proof.* Losing only a factor of $2$ (since $u$ and $-u$ are both mapped to the same vector) the set $B^\times(Y)$ can be viewed as a subset of the $L^\infty$ ball of radius $Y$, intersected with the hyperplane $H$. Moreover, by Lemma [\[lem-unitsep\]](#lem-unitsep){reference-type="ref" reference="lem-unitsep"}, points in this lattice are at least $(\log \phi)$-separated in the $L^\infty$ norm. Indeed, if $x,y\in \mathcal{O}_K^\times$ and $x\not\in \{y,-y\}$ then $x/y\in \mathcal{O}_K^\times \backslash \{\pm 1\}$, and hence there exists $\sigma$ such that $$\lvert \sigma(x)\rvert/\lvert \sigma(y)\rvert \not\in(\phi^{-1},\phi).$$ Combining the same standard packing argument as in the proof of Lemma [\[lem-ball\]](#lem-ball){reference-type="ref" reference="lem-ball"} with [\[eq-hensley\]](#eq-hensley){reference-type="eqref" reference="eq-hensley"}, there are at most $5(\frac{2}{c}Y+1)^{d-1}$ many $c$-separated points in $H$ intersected with an $L^\infty$ ball of radius $Y$. This proves the upper bound since $2/\log(\phi)<5$.

For the lower bound, we use the same idea as before: the covolume of the lattice is $\sqrt{d}R_K$, and hence there exists some $a$ such that the number of lattice points in $a+\{ x\in H : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq Y/2\}$ is at least $$\frac{\mathrm{vol}_{d-1}(\{ x\in H: \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq Y/2\})}{\sqrt{d}R_K}\geq \frac{Y^{d-1}}{\sqrt{d}R_K}.$$ The conclusion now follows by taking the difference set of these points. ◻
:::
