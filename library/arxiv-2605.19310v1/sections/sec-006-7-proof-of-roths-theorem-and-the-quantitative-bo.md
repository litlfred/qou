---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-006-7-proof-of-roths-theorem-and-the-quantitative-bo
section_title: "Proof of Roth's theorem and the quantitative bound"
section_number: 7
pages: 8-9
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
::: proof
*Proof of Theorem [\[thm:roth\]](#thm:roth){reference-type="ref" reference="thm:roth"}.* Fix $\alpha_0>0$ and suppose, for contradiction, that there are arbitrarily large $N$ and 3AP-free sets $A\subset[N]$ with $\lvert A\rvert\geq\alpha_0N$. Applying Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}, then rescaling the progression it gives back to an interval, produces a new 3AP-free set with density increased by at least $c\alpha_0^{11}$. Repeating this, the density exceeds $1$ after $O(\alpha_0^{-11})$ steps.

It remains only to ensure that the iteration can be run for that many steps. At each step the ambient length is replaced by a progression of length at least $c\alpha_0^{16}N_j^{1/2}$. Since the number of steps depends only on $\alpha_0$, choosing the original $N$ sufficiently large in terms of $\alpha_0$ keeps every intermediate interval above the threshold in Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}. This contradiction proves the theorem. ◻
:::

A more careful analysis gives an explicit double-logarithmic bound.

::: corollary
[]{#cor:quantitative label="cor:quantitative"} There is an absolute constant $C>0$ such that $$r_3(N)\leq C\frac{N}{(\log\log N)^{1/11}}$$ for all sufficiently large $N$.
:::

::: proof
*Proof.* Let $A\subset[N]$ be 3AP-free, and write $\alpha=\lvert A\rvert/N$. Set $J=\lfloor c_0\alpha^{-11}\rfloor$, where $c_0>0$ is a sufficiently small absolute constant. If the density increment can be applied $J$ times, then each step increases the density by at least $c\alpha^{11}$, since the densities only increase. After $J$ steps the density would exceed $1$, which is impossible.

It remains to check that the lengths stay large enough for $J$ steps. At each step, after rescaling the subprogression back to an interval, Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"} gives $$\alpha_{j+1}\geq \alpha_j+c\alpha_j^{11},
        \qquad
        N_{j+1}\geq c\alpha_j^{16}N_j^{1/2}.$$ Since $\alpha_j\geq\alpha$, the length estimate implies $$\log N_{j+1}\geq \frac12\log N_j-C\log(e/\alpha).$$ Iterating this crude bound gives $$\log N_j\geq 2^{-j}\log N-C\log(e/\alpha).$$ Thus, if $\log N\geq C2^J\log(e/\alpha)$, then every $N_j$ with $j\leq J$ remains larger than a fixed power of $\alpha^{-1}$, and in particular remains above the threshold required by Proposition [\[prop:increment\]](#prop:increment){reference-type="ref" reference="prop:increment"}. Since $J\sim\alpha^{-11}$, this condition follows from $$\log\log N\geq C\alpha^{-11},$$ after increasing $C$.

Therefore, if $\log\log N$ were larger than a sufficiently large constant times $\alpha^{-11}$, the iteration could run for $J$ steps and force the density above $1$. Hence $\log\log N\lesssim\alpha^{-11}$, so $\alpha\lesssim(\log\log N)^{-1/11}$. Since $\alpha=\lvert A\rvert/N$, this gives $$r_3(N)\lesssim \frac{N}{(\log\log N)^{1/11}}.$$ This proves the corollary. ◻
:::
