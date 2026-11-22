---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-008-31-the-additive-lattice
section_title: "The additive lattice"
section_number: 3.1
pages: 7-8
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.889
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
The ring of algebraic integers $\mathcal{O}_K$ can be viewed as a lattice of rank $d$ in $\mathbb{R}^d$ via the Minkowski embedding $$\alpha \mapsto (\sigma_1(\alpha),\ldots,\sigma_d(\alpha)),$$ where $\sigma_1,\ldots,\sigma_d$ are the embeddings $\sigma_i\colon K\hookrightarrow \mathbb{R}$. The covolume of this lattice is $\Delta_K^{1/2}$ (see [@La70 V, Lemma 2]). We write $$B^+(X) = \{ \alpha \in \mathcal{O}_K : \mathopen{}\left| \sigma_i(\alpha)\mathclose{}\right|\leq X\textrm{ for all }1\leq i\leq d\}.$$

::: lemma
[]{#lem-ball label="lem-ball"} Let $K$ be a totally real number field of degree $d$. For any $X\geq 1$ $$X^{d}\Delta_K^{-1/2}\leq \lvert B^+(X)\rvert\leq (2X+1)^{d}.$$
:::

::: proof
*Proof.* In the embedding described above, $B^+(X)$ is contained inside the $L^\infty$ ball of radius $X$. Moreover, points in this lattice are at least $1$-separated in the $L^\infty$ norm: if $x\neq y\in \mathcal{O}_K$ then, since $x-y$ is a non-zero algebraic integer, it has a non-zero integral norm. Furthermore, since $N(\alpha)=\prod_{i=1}^d \sigma_i(\alpha)$, we deduce $$1\leq \lvert N(x-y)\rvert\leq \prod_{i=1}^d\lvert \sigma_i(x-y)\rvert,$$ so there must exist $1\leq i\leq d$ such that $\lvert \sigma_i(x)-\sigma_i(y)\rvert\geq 1$. By a standard packing argument (for example, placing disjoint balls of radius $1/2$ around each lattice point) there are at most $(2X+1)^{d}$ many $1$-separated points in a ball of radius $X$, and we are done.

For the lower bound we use Blichfeldt's lemma: the covolume of the lattice is $\Delta_K^{1/2}$, and hence there exists some $a$ such that the number of lattice points in $a+\{ x\in \mathbb{R}^d : \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq X/2\}$ is at least $$\frac{\mathrm{vol}(\{ x: \mathopen{}\left\| x\mathclose{}\right\|_\infty \leq X/2\})}{\Delta_K^{1/2}}= \frac{X^{d}}{\Delta_K^{1/2}}.$$ The conclusion now follows by taking the difference set of these points. ◻
:::
