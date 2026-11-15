---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-008-09-integrals-in-quantum-groupoids
section_title: "Integrals in quantum groupoids"
section_number: 0.9
pages: 10-11
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.95
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
::: definition
[]{#integral label="integral"} A left (right) *integral* in $H$ is an element $l\in H$ ($r\in H$) such that $$hl =\varepsilon_t(h)l, \qquad (rh = r\varepsilon_s(h)) \qquad \mbox{ for all } h\in H.$$
:::

These notions clearly generalize the corresponding notions for Hopf algebras ([@M], 2.1.1). We denote $\int_H^l$ (respectively, $\int_H^r$) the space of left (right) integrals in $H$ and by $\int_H = \int_H^l \cap \int_H^r$ the space of two-sided integrals.

An integral in $H$ (left or right) is called *non-degenerate* if it defines a non-degenerate functional on $\widehat H$. A left integral $l$ is called *normalized* if $\varepsilon_t(l)=1$. Similarly, $r\in \int_H^r$ is normalized if $\varepsilon_s(r)=1$.

A dual notion to that of left (right) integral is the left (right) invariant measure. Namely, a functional $\phi \in \widehat H$ is said to be a left (right) *invariant measure* on $H$ if $$(\mbox{id}\otimes \phi)\Delta = (\varepsilon_t\otimes \phi)\Delta,\qquad  (\mbox{resp.}, 
(\phi\otimes \mbox{id})\Delta = (\phi\otimes \varepsilon_s)\Delta).$$ A left (right) invariant measure is said to be normalized if $(\mbox{id}\otimes\phi)\Delta(1)=1$ (resp., $(\phi\otimes \mbox{id})\Delta(1)=1$).

::: example
[]{#examples of integrals label="examples of integrals"} (i) Let $G^0$ be the set of units of a finite groupoid $G$, then the elements $l_e = \sum_{gg^{-1}=e}\,g\,(e\in G^0)$ span $\int_{kG}^l$ and elements $r_e = \sum_{g^{-1}g=e}\,g\,(e\in G^0)$ span $\int_{kG}^r$. (ii) If $H = (kG)^*$ then $\int_H^l = \int_H^r =\mbox{span}\{p_e,\,e\in G^0\}$.
:::

The next proposition gives a description of the set of left integrals.

::: proposition
[]{#integral properties label="integral properties"} The following conditions for $l\in H$ are equivalent:

1.  $l\in \int_H^l$,

2.  $(1\otimes h)\Delta(l) =(S(h)\otimes 1)\Delta(l)$ for all $h\in H$,

3.  $(\mbox{id}\otimes l)\Delta(\widehat H) =\widehat H_t$,

4.  $(\mbox{Ker\,}\,\varepsilon_t)l =0$,

5.  $S(l)\in \int_H^r$.
:::

::: proof
*Proof.* The proof is a straightforward application of Definitions [\[finite quantum groupoid\]](#finite quantum groupoid){reference-type="ref" reference="finite quantum groupoid"}, [\[integral\]](#integral){reference-type="ref" reference="integral"}, Propositions [\[counital properties\]](#counital properties){reference-type="ref" reference="counital properties"} and [\[S and counital maps\]](#S and counital maps){reference-type="ref" reference="S and counital maps"}, and is left as an exercise for the reader. ◻
:::
