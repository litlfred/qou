---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-088-261-the-generating-series-for-the-class-numbers
section_title: "The generating series for the class numbers"
section_number: 26.1
pages: 134-134
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.882
latex_coverage_ratio: 0.977
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:generatingseries label="subsection:generatingseries"}

Consider the quadratic forms $a x^{2} + 2 h x y + b y^{2}$, with $a,b,h \in {\mathbf Z}$, $a,b$ not both even ("uneven forms"), and $D := a b - h^{2} > 0$, up to the usual equivalence. For any $D \in {\mathbf N}^{*}$, write $F(D)$ the (finite) number of classes of such forms. []{#not112 label="not112"}

::: theo
[]{#theo:Mordell1916 label="theo:Mordell1916"} Let $f_{0,1}(x) = f_{0,1}(x,\omega)$ be the unique entire function solution of the system: $$\begin{cases}
f_{0,1}(x+1) = f_{0,1}(x), \\
f_{0,1}(x+\omega) + f_{0,1}(x) = \theta_{0,1}(x).
\end{cases}$$ Then, for $\Im(\omega) > 0$: $$\sum_{n \in {\mathbf N}^{*}} F(n) e^{{\text{i}}\pi n \omega} =
\dfrac{{\text{i}}}{4 \pi} ~ \dfrac{f_{0,1}'(0)}{\theta_{0,1}(0)} \cdot$$
:::

If one now defines $G_{0,1}(z) := \dfrac{f_{0,1}(x)}{\theta_{0,1}(x)}$ (which does make sense, since the right hand side is $1$-periodic), one falls upon the familiar $q$-difference equation: $$(\sqrt{q} z \sigma_q- 1) G_{0,1} = \sqrt{q} z.$$ We leave it as an exercise for the reader to characterize $G_{0,1}$ as the unique solution complying some polar conditions.
