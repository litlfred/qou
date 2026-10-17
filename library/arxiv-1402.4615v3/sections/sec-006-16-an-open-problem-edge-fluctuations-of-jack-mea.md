---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-006-16-an-open-problem-edge-fluctuations-of-jack-mea
section_title: "An open problem: edge fluctuations of Jack measure"
section_number: 1.6
pages: 12-12
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
Another natural question on asymptotics of Jack measure is the behavior of the first few rows of the Young diagrams. This kind of results, orthogonal to the ones in this paper, is called *edge fluctuations*. Our law of large number on the bulk on Young diagrams implies that, for any fixed positive integer $k$ and real number $C<1$, $$\mathbb{P}\left[ \frac{(\lambda_{(n)})_k}{\sqrt{n}} \leq \frac{2\, C}{\sqrt{\alpha}} \right] \to 0,$$ while Lemma [\[lem:FiniteSupport\]](#lem:FiniteSupport){reference-type="ref" reference="lem:FiniteSupport"} tells us that $(\lambda_{(n)})_k/\sqrt{n}$ exceeds $(2e)/\sqrt{\alpha}$ with exponentially small probability.

A natural conjecture, considering the case $\alpha=1$ where the edge fluctuations are well described (see [@Okounkov2000; @BorodinOkounkovOlshanski2000] and references therein) and the link with $\beta$-ensemble, would be the following: for each integer $k \ge 1$, the quantity $(\lambda_{(n)})_k/\sqrt{n}$ converges in probability towards $2/\sqrt{\alpha}$ and the joint vector $$\left[ n^{1/3} \left( \frac{(\lambda_{(n)})_j}{\sqrt{n}} - \frac{2}{\sqrt{\alpha}} \right) \right]_{1 \le j \le k}$$ converges in law towards the $\beta$-Tracy-Widom distribution, which has been introduced and studied in [@BetaEdgeFluctuations] to study edge fluctuations of $\beta$-ensemble. Naturally, a similar conjecture can be formulated for the lengths of the first columns of the Young diagram $\lambda_{(n)}$.

These conjectures hold true for the first row/column in the case $\alpha=1/2$ and $\alpha=2$. The proof uses the combinatorial interpretation of Jack measure at these particular values of $\alpha$, using Robinson-Schensted on random fixed point free involutions: see [@BaikRainsMonotomeSubsequenceInvolutions].

We have not made computer experiments to confirm this conjecture and let this problem wide open for future research.
