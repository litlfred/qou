---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-048-65-construction-of-the-double-leaves-basis
section_title: "Construction of the double leaves basis"
section_number: 6.5
pages: 43-44
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.919
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#LL label="LL"}

In this section we consider two arbitrary sequences (not necessarily reduced) of simple reflections $\underline{s}=s_1\cdots s_n$ and $\underline{r}=r_1\cdots r_p.$ We are interested in calculating the space $\mathrm{Hom}(B_{\underline{s}}, B_{\underline{r}})$.

**Philosophy:** *The natural basis between Bott-Samelson bimodules is the tree $\mathbb{T}_{\underline{s}}$ \"pasted\" with the tree $\mathbb{T}_{\underline{r}}$ inverted.*

For any light leaf $l:B_{\underline{r}}\rightarrow B_{\underline{t}}$ in $\mathbb{T}_{\underline{r}}$ we can find its *adjoint light leaf* $l^a:B_{\underline{t}} \rightarrow  B_{\underline{r}}$ by replacing each morphism in the set $\{m_s, j_s, f_{sr}\}$ by its adjoint. So we obtain a tree $\mathbb{T}_{\underline{r}}^a$ where the arrows go from children to parents.

Let $\mathbb{L}_{\underline{s}}$ be the set of light leaves of $\mathbb{T}_{\underline{s}}$ (recall that each leaf of the tree is seen as a morphism between Bott-Samelson bimodules).

Let $h\in \mathbb{L}_{\underline{s}}$ and $g\in \mathbb{L}_{\underline{r}}^a$, with $h\in\mathrm{Hom}(B_{\underline{s}},B_{\underline{x}})$ and $g \in\mathrm{Hom}(B_{\underline{y}},B_{\underline{r}})$, where $\underline{x}$ and $\underline{y}$ are reduced expressions of the elements $x, y\in W$ respectively. We define $$g\cdot h=
\begin{cases}
\hspace*{0.1cm} g\circ F\circ  h \hspace*{0.3cm} \mathrm{if}\ x=y\\
\hspace*{0.7cm} \emptyset\hspace*{0.96cm} \mathrm{if}\ x\neq y
\end{cases}$$ where $F$ is any path morphism in $\mathrm{Hom}(B_{\underline{x}}, B_{\underline{y}})$. We call the set $\mathbb{L}_{\underline{r}}^a\cdot \mathbb{L}_{\underline{s}}$ the *double leaves basis* of $\mathrm{Hom}(B_{\underline{s}}, B_{\underline{r}}).$ The following theorem is proved in [@li3].

::: thm
[]{#LL label="LL"} The Double Leaves Basis is a basis as a right (or left) $R$-module of the space $\mathrm{Hom}(B_{\underline{s}}, B_{\underline{r}}).$
:::

The proof of Theorem [\[LL\]](#LL){reference-type="ref" reference="LL"} is quite close to the proof of [@Li1 Théorème 5.1].

::: remark
Twice in this construction we said "where $F$ is any path morphism". Of course, for this basis to be well defined, these choices must be done once and for all. But what is quite striking about this theorem is that with any of these choices, Theorem [\[LL\]](#LL){reference-type="ref" reference="LL"} holds. There is a way to solve this ambiguity problem that we explore in the paper in preparation [@LW].
:::

::: ques
Give an algorithm to express a composition of double leaves as a linear combination of double leaves.
:::
