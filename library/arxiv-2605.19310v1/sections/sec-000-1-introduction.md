---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.971
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
In 1953, Roth proved that every subset of the integers of positive upper density contains a nontrivial three-term arithmetic progression. This can be stated in the following finite form.

::: theorem
[]{#thm:roth label="thm:roth"} For every $\alpha>0$, if $N$ is sufficiently large, then every set $A\subset\{0,1,\ldots,N-1\}$ with $\lvert A\rvert\geq\alpha N$ contains a three-term arithmetic progression $x,\,x+r,\,x+2r$ with $r\neq 0$.
:::

Roth's theorem is a foundational result in density Ramsey theory; its extension to longer arithmetic progressions is a celebrated theorem of Szemerédi  [@Szemeredi75]. Proofs of Roth's theorem have been given using quite different methods: Roth's original proof is Fourier analytic [@Roth53]; Furstenberg proved Szemerédi's theorem in full using ergodic-theoretic methods [@Furstenberg77]; and graph-theoretic proofs of Roth's theorem follow from the triangle removal lemma of Ruzsa and Szemerédi [@RS78]. More combinatorial proofs have also been given using Szemerédi's cube lemma [@GRS] as well as using ideas related to the more general Hales--Jewett theorem [@DHJ]. There is also a rich history of quantitative improvements, which we do not attempt to summarize here; see [@Green; @P] for recent surveys.

Roth's original proof uses a density-increment argument. Starting with a set $A\subset[N]$ with no nontrivial three-term progressions, one proves that $A$ has increased density on a long subprogression. Passing to that progression and rescaling, one repeats the argument. If the original interval is sufficiently long, the density would eventually have to exceed $1$, providing a contradiction. The purpose of this note is to give a proof with the same density-increment structure, but without using Fourier analysis. Instead of detecting a large Fourier coefficient, we estimate certain averages over subprogressions directly.

The combinatorial approaches to Roth's theorem have typically produced very weak quantitative bounds. The argument here stays close to Roth's density-increment framework and gives a bound of the form $$r_3(N)\lesssim \frac{N}{(\log\log N)^c}$$ with $c=1/11$. This can be improved somewhat at the expense of complicating the exposition, but the argument in its current form does not seem capable of recovering the exponent $c=1$ obtained by Roth's original argument.
