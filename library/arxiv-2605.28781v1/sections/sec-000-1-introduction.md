---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.948
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
Given any finite set $A$ in some ring we define the sum set and product set of $A$ as $$A+A=\{a+b: a,b\in A\}\quad\textrm{and}\quad AA=\{ ab : a,b\in A\}.$$ The sum-product conjecture in a given ring is that at least one of these must grow near-maximally; more precisely $$\label{eq-sp}\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\geq \mathopen{}\left| A\mathclose{}\right|^{2-o(1)}$$ (where the $o(1)$ term tends $0$ as $\mathopen{}\left| A\mathclose{}\right|\to \infty$). This is often attributed to Erdős and Szemerédi, who proved the first results in this direction [@ErSz83], but it first appeared in the literature in a paper of Erdős in 1976 [@Er76] (in which he says he first made the conjecture 18 months earlier). This question makes sense over any ring (although there are obvious complications in finite rings or rings with zero divisors). Erdős [@Er76] asked this specifically for $\mathbb{Z}$, $\mathbb{R}$, and $\mathbb{C}$, although his main interest was for $A\subset \mathbb{Z}$.

Most proofs in the sum-product literature are geometric and combinatorial, using no number theory, and thus apply to any finite $A\subset \mathbb{R}$; the best result achieved in this direction so far is $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\geq \mathopen{}\left| A\mathclose{}\right|^{\frac{4}{3}+c-o(1)}\quad\textrm{for}\quad A\subset \mathbb{R}$$ for some small constant $c>0$. This was proved with $c=0$ by Solymosi [@So09] and for some $c>0$ by Konyagin and Shkredov [@KoSh16]. The value of $c$ has been improved a number of times since, with the current record of $c=\frac{10}{4407}$ due to Cushman [@Cu25].

In this paper we prove that the sum-product conjecture [\[eq-sp\]](#eq-sp){reference-type="eqref" reference="eq-sp"} is false over the reals, by constructing arbitrarily large counterexamples in totally real algebraic number fields of large degree. The degree of these fields tends to infinity as the sets grow (like $\asymp \log n$ for a counterexample of size $n$), and so [\[eq-sp\]](#eq-sp){reference-type="eqref" reference="eq-sp"} may still be true in number fields of bounded degree (and, in particular, the original setting of $\mathbb{Z}$).

::: theorem
[]{#th-headline label="th-headline"} There exists an absolute constant $c>0$ such that there are arbitrarily large finite $A\subset\mathbb{R}$ with $$\max(\mathopen{}\left| A+A\mathclose{}\right|,\mathopen{}\left| AA\mathclose{}\right|)\leq \mathopen{}\left| A\mathclose{}\right|^{2-c}.$$
:::

Our arguments deliver an explicit value of $c$, but this is a tedious calculation, and the value obtained is very small. Since the main interest of this result is the existence of an absolute constant $c>0$, we have chosen to present a non-explicit version of the proof, to better demonstrate the main ideas. In Section [\[sec-numerical\]](#sec-numerical){reference-type="ref" reference="sec-numerical"} we sketch how a version of the proof with explicit constants can deliver $c\geq 0.00000087$ (although this should not be taken too seriously, and can certainly be improved with a little more effort).

Theorem [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"} is easily deduced from the following more general result.

::: theorem
[]{#th-main label="th-main"} There exists an absolute constant $C>0$ such that the following holds. There are infinitely many $d$, with accompanying totally real number fields $K$ of degree $d$ over $\mathbb{Q}$, such that, for any $X\geq 1$, there exists $A\subset \mathcal{O}_K$ with $$X^{d} \leq \mathopen{}\left| A\mathclose{}\right|\leq (CX)^{d},$$ $$\mathopen{}\left| A+A\mathclose{}\right|\leq C^{d}\mathopen{}\left| A\mathclose{}\right|\textrm{, and}\quad\mathopen{}\left| AA\mathclose{}\right|\leq 2^{-d}\mathopen{}\left| A\mathclose{}\right|^2.$$
:::

By choosing an arbitrary embedding of $K$ into $\mathbb{R}$, and $X=C^{1/\epsilon}$, we deduce the following, which provides examples in which the sum set is very small, and yet there is still a power saving on the size of the product set.

::: corollary
[]{#cor-main label="cor-main"} There exists an absolute constant $c>0$ such that the following holds. For any $\epsilon\in (0,1)$ there are arbitrarily large $A\subset \mathbb{R}$ with $$\mathopen{}\left| A+A\mathclose{}\right|\leq \mathopen{}\left| A\mathclose{}\right|^{1+\epsilon}\textrm{ and }\mathopen{}\left| AA\mathclose{}\right|\leq \mathopen{}\left| A\mathclose{}\right|^{2-c\epsilon}.$$
:::

Theorem [\[th-headline\]](#th-headline){reference-type="ref" reference="th-headline"} is an immediate consequence. This result should also be compared to the lower bound of Solymosi [@So09], who proved that for any $A\subset \mathbb{R}$ $$\label{eq-sol}
\mathopen{}\left| A+A\mathclose{}\right|^2\mathopen{}\left| AA\mathclose{}\right|\geq \mathopen{}\left| A\mathclose{}\right|^{4-o(1)}.$$

Using similar ideas we also obtain new lower bounds in a number of other related problems of a sum-product flavour, which we summarise below.
