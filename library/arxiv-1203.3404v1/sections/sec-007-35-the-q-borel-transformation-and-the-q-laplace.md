---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-007-35-the-q-borel-transformation-and-the-q-laplace
section_title: "The q-Borel transformation and the q-Laplace transformation"
section_number: 3.5
pages: 11-12
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.889
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanujan equation between the origin and the inﬁnity."
---
::: defi
For $f(t)=\sum_{n\ge 0}a_nt^n$, the $q$-Borel transformation is defined by $$g(\tau )=\left(\mathcal{B}_q^-f\right)(\tau ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\tau^n,$$ and the $q$-Laplace transformation is given by $$\left(\mathcal{L}_q^-g\right)(t):=\frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau },\qquad 0<r<\frac{1}{|q^2|}.$$
:::

The $q$-Borel transformation can be considered as a formal inverse of the $q$-Laplace transformation.

::: lem
For any entire function $f$, $$\mathcal{L}_q^-\circ\mathcal{B}_q^-f=f.$$
:::

::: proof
*Proof.* We can prove this lemma calculating residues of the $q$-Laplace transformation around the origin. ◻
:::

The $q$-Borel transformation has following operational relation;

::: lem
[]{#orqb label="orqb"} For any $l,m\in\mathbb{Z}_{\ge 0}$, $$\mathcal{B}_q^-(t^m\sigma_q^l)=q^{-\frac{m(m-1)}{2}}\tau^m\sigma_q^{l-m}\mathcal{B}_q^-.$$
:::
