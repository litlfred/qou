---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-015-72-finite-fields
section_title: "Finite fields"
section_number: 7.2
pages: 16-17
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.971
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
::: theorem
[]{#finite-field-main label="finite-field-main"} There exist constants $c>0$ and $f<1$ such that for each $\delta \in (0,1)$, for each prime $p$ sufficiently large depending on $\delta$, there exists $A \subset \mathbb F_p$ with $p^{f\delta}< \mathopen{}\left| A\mathclose{}\right| < p^{\delta}$ and $\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-c}$.
:::

Sum-product results in finite fields typically require both an upper bound and a lower bound on the size of $A$, so we have stated this result with an upper bound and a lower bound.

It may be possible to prove a result with tighter control on $\mathopen{}\left| A\mathclose{}\right|$ in terms of $p$, by choosing $p$ after constructing a field $K$ and a subset of $\mathcal O_K$, at the cost that this result would hold for infinitely many primes instead of all primes.

The value of $c$ obtained from our argument is very small. It is slightly worse than the explicit value of $c$ we obtain for the main theorem, owing to the dependence of this argument on Lemma [\[field-existence-split-p\]](#field-existence-split-p){reference-type="ref" reference="field-existence-split-p"}. It may be possible to prove a similar result in finite fields of large size and small characteristic, with a better exponent, using the results of the next subsection and reducing modulo a prime of the function field $\mathbb F_q(C)$. To make this interesting, one would have to check that the sets produced this way are far from any subfield of the finite field, for example as in the finite field sum-product estimate of Li and Roche-Newton [@Li2011].

::: proof
*Proof.* We apply Lemma [\[field-existence-split-p\]](#field-existence-split-p){reference-type="ref" reference="field-existence-split-p"} for a $d$ to be chosen later to produce a number field $K$ of degree $d$ in which $p$ splits completely. We apply Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"} to produce $A \subset \mathcal O_K$. Since the prime $p$ splits completely in $K$, we may choose a prime $\mathfrak p$ of $\mathcal O_K$ lying over $p$, with residue field $\mathbb F_p$, to obtain a surjection $\mathcal O_K \to \mathbb F_p$. We will consider the image of $A$ inside $\mathbb F_p$.

In the proof of Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"}, it is observed that every $\alpha \in A$ has $\mathopen{}\left| \sigma(\alpha)\mathclose{}\right|\leq 2X e^Y$ for all $\sigma$, and thus for $\alpha_1 \neq \alpha_2$ in $A$ we have $\mathopen{}\left| \sigma(\alpha_1-\alpha_2)\mathclose{}\right|\leq 4 X e^Y$ and hence the norm of $\alpha_1-\alpha_2$, which is the product of its image under all embeddings $\sigma$, is at most $(4X e^Y)^d$. If $\alpha_1$ and $\alpha_2$ have the same image in $\mathbb F_p$, then $\alpha_1-\alpha_2$ must be divisible by $\mathfrak p$ and hence have a norm a multiple of $p$.

It follows that for the map $\mathcal O_K \to\mathbb F_p$ to be injective on $A$, it suffices to have $(4 Xe^Y)^d <p$.

From Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"}, $\mathopen{}\left| A\mathclose{}\right| \leq (XY/c')^d$ for an absolute constant $c'$. Thus to have $\mathopen{}\left| A\mathclose{}\right|<p^\delta$, it suffices to have $(XY/c')^{d}<p^\delta$. Let $d$ be the least power of $2$ such that $(4 Xe^Y)^d <p$ and $(XY/c')^{d}<p^\delta$. Arguing as in the proof of Theorems [\[th-main\]](#th-main){reference-type="ref" reference="th-main"} and [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"}, we have $\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-c}$. Since $p$ is sufficiently large, $d$ is sufficiently large to be used in this argument.

It remains to prove $\mathopen{}\left| A\mathclose{}\right|> p^{\frac{\delta}{f}}$. To do this, we use Lemma [\[lem-main\]](#lem-main){reference-type="ref" reference="lem-main"} which gives $$\label{A-lb-fin-case} \mathopen{}\left| A\mathclose{}\right| \geq \frac{ (c' XY)^d}{ Y \Delta_K^{3/2}} \geq  \frac{ (c' XY)^d}{ Y C^{3d/2}}$$ which, with parameters chosen as in the proof of Theorems [\[th-main\]](#th-main){reference-type="ref" reference="th-main"} and [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"}, is exponentially large in $d$. Since $d$ is the least power of $2$ such that $(4 Xe^Y)^d <p$ and $(XY/c')^{\frac{d}{\delta}}<p$, we have either $(4 Xe^Y)^{2d} \geq p$ or $(XY/c')^{\frac{2d}{\delta}}\geq p$. Combining either one of these with [\[A-lb-fin-case\]](#A-lb-fin-case){reference-type="eqref" reference="A-lb-fin-case"} gives a lower bound of a power of $p^\delta$, as desired. ◻
:::
