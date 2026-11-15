---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q -Airy function"
section_id: sec-008-41-the-q-borel-transformation-and-the-q-laplace
section_title: "The q-Borel transformation and the q-Laplace transformation"
section_number: 4.1
pages: 9-10
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.846
doc_brief: "A connection formula between the Ramanujan function and the q -Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
::: defi
For $f(t)=\sum_{n\ge 0}a_nt^n$, the $q$-Borel transformation is defined by $$g(\tau )=\left(\mathcal{B}_qf\right)(\tau ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\tau^n,$$ and the $q$-Laplace transformation is given by $$\left(\mathcal{L}_qg\right)(t):=\frac{1}{2\pi i}\int_{|\tau |=r}g(\tau )\theta\left(\frac{t}{\tau}\right)\frac{d\tau}{\tau },\qquad 0<r<\frac{1}{|q^2|}.$$
:::

The $q$-Borel transformation can be considered as a formal inverse of the $q$-Laplace transformation.

::: lem
For any entire function $f$, $$\mathcal{L}_q\circ\mathcal{B}_qf=f.$$
:::

::: pf
We can prove this lemma calculating residues of the $q$-Laplace transformation around the origin.

------------------------------------------------------------------------
:::

The $q$-Borel transformation has following operational relation;

::: lem
[]{#orqb label="orqb"} For any $l,m\in\mathbb{Z}_{\ge 0}$, $$\mathcal{B}_q(t^m\sigma_q^l)=q^{-\frac{m(m-1)}{2}}\tau^m\sigma_q^{l-m}\mathcal{B}_q.$$
:::
