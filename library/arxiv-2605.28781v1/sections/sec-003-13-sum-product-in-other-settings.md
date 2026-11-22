---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-003-13-sum-product-in-other-settings
section_title: "Sum-product in other settings"
section_number: 1.3
pages: 3-4
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.936
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
Finally, in Section [\[sec-variants\]](#sec-variants){reference-type="ref" reference="sec-variants"} we discuss variants of our construction. We first obtain, via only a slight modification of the argument, analogues of all of the above results for $A\subset \mathbb{Q}_p$ for any prime $p$.

The second variant, obtained by taking the construction in $\mathbb{Q}_p$ 'modulo $p$' in a suitable sense, provides an upper bound for the sum-product problem in the finite field $\mathbb{F}_p$, another natural setting. We state a slightly simplified version here (see Theorem [\[finite-field-main\]](#finite-field-main){reference-type="ref" reference="finite-field-main"} for the full version).

::: theorem
There exists a constant $c>0$ such that, for all sufficiently large primes $p$, there exists $A \subset \mathbb F_p$ with $p^{c}< \mathopen{}\left| A\mathclose{}\right| < p^{1/2}$ and $\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-c}$.
:::

We note that such a result for $\mathopen{}\left| A\mathclose{}\right|$ very small in terms of $p$ is a consequence of Theorem [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"} combined with the transference method of Vu, Wood, and Wood [@VWW11], but here we are able to find sum-product counterexamples which are reasonably 'large' (in that $\mathopen{}\left| A\mathclose{}\right|\geq p^c$ for some constant $c>0$).

The first sum-product results for subsets of $\mathbb{F}_p$ of size $p^\delta$ for some $\delta>0$ were obtained by Bourgain, Katz, and Tao [@BKT04]. The best result thus far obtained in this direction is due to Mohammadi and Stevens [@MoSt23], who proved that if $\mathopen{}\left| A\mathclose{}\right|< p^{1/2}$ then $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\geq \mathopen{}\left| A\mathclose{}\right|^{\frac{5}{4}-o(1)}.$$

The third variant, which is more involved, constructs sum-product counterexamples in infinite fields of fixed positive characteristic.

::: theorem
[]{#th-ffmain label="th-ffmain"} There exists an absolute constant $c>0$ such that, for any prime $p$, if $q$ is an power of $p$ then there exist arbitrarily large $A\subset \mathbb{F}_{q}((t))$ such that $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-\frac{c}{\log p}}.$$
:::

In small characteristics the exponent saving is reasonably good -- for example when $q=1024$ we obtain $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{1.906}.$$ The best known lower bound for the sum-product problem in function fields, due to Bloom and Jones [@BlJo14], is that for any $q$ and $A\subset \mathbb{F}_q((t))$, $$\max(\mathopen{}\left| A+A\mathclose{}\right|, \mathopen{}\left| AA\mathclose{}\right|)\geq  q^{-1/5}\mathopen{}\left| A\mathclose{}\right|^{6/5-o(1)}$$ (where the $o(1)$ exponent tends to zero as $\mathopen{}\left| A\mathclose{}\right|\to \infty$).
