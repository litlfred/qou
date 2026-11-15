---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-037-101-admissible-framed-links-and-the-hoste-moves
section_title: "Admissible framed links and the Hoste moves"
section_number: 10.1
pages: 34-35
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.962
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:hoste-moves label="sec:hoste-moves"}

A framed link $L$ in $S^3$ is said to be *admissible* if $L$ is algebraically split and $\pm 1$-framed. Surgery on $S^3$ along an admissible framed link yields an integral homology sphere. Conversely, each integral homology sphere $M$ can be obtained as the result of surgery on $S^3$ along an admissible framed link.

In the definition of the Reshetikhin-Turaev invariant [@Reshetikhin-Turaev:invariants] and its variants, one uses Kirby's theorem [@Kirby] or its variant by Fenn and Rourke [@Fenn-Rourke]. Fenn and Rourke's theorem states that two framed links in $S^3$ yields orientation-preserving homeomorphic results of surgery if and only if they are related by a sequence of isotopies and *Fenn-Rourke moves*, where a Fenn-Rourke move is either surgery on a unknotted, $\pm 1$-framed component, or the inverse operation. See Figure [\[fig:FR\]](#fig:FR){reference-type="ref" reference="fig:FR"}.

We use the following version of Fenn-Rourke's theorem, which was conjectured by Hoste [@Hoste].

::: theorem
[]{#r32 label="r32"} Two admissible framed links $L$ and $L'$ in $S^3$ yield orientation-preserving homeomorphic results of surgery if and only if $L$ and $L'$ are related by a sequence of isotopies and *Hoste moves*. Here a Hoste move is defined to be a Fenn-Rourke move between two admissible framed links.
:::

## Definition of $J_M$ {#sec:defin-unif-sl2}

Let $M$ be an integral homology sphere. Choose an admissible framed link $L=L_1\cup \cdots\cup L_m$ in $S^3$ such that $S^3_L\cong M$. For $i=1,\ldots,m$, let $f_i=\pm 1$ denote the framing of $L_i$. Let $L^0=L^0_1\cup \cdots\cup L^0_m$ denote the link $L$ with $0$ framings. Set $$\label{eq:42}
  J_M= J_{L^0}(\omega ^{-f_1},\omega ^{-f_2},\ldots,\omega ^{-f_m})\in \Zqh.$$

::: theorem
[]{#thm:41 label="thm:41"} For an integral homology sphere $M$, the element $J_M\in \Zqh$ defined in [\[eq:42\]](#eq:42){reference-type="eqref" reference="eq:42"} does not depend on the choice of $L$. Hence, the correspondence $M\mapsto J_M$ defines an invariant of integral homology spheres with values in $\Zqh$.
:::

::: proof
*Proof.* Let $I(L)$ denote the right-hand side of [\[eq:42\]](#eq:42){reference-type="eqref" reference="eq:42"}. Clearly, $I(L)$ is an isotopy invariant of admissible framed links. By Theorem [\[r32\]](#r32){reference-type="ref" reference="r32"}, it suffices to prove that $I(L)$ is invariant under Hoste moves. Observe that $I(L)$ is invariant under permutation of components. Therefore, it suffices to show that if the last component $L_m$ of $L$ is an unknot, then $$J_{L^0}(\omega ^{-f_1},\ldots,\omega ^{-f_{m-1}},\omega ^{-f_m})
    =J_{(L^0\setminus L^0_m)_{L_m}}(\omega ^{-f_1},\ldots,\omega ^{-f_{m-1}}),$$ where $(L^0\setminus L^0_m)_{L_m}$ is obtained from $L^0\setminus L^0_m$ by performing surgery along $L_m$ with framing $f_m$. This identity follows from Theorem [\[thm:99\]](#thm:99){reference-type="ref" reference="thm:99"}. Hence the assertion. ◻
:::

In Section [\[sec:an-alternative-proof\]](#sec:an-alternative-proof){reference-type="ref" reference="sec:an-alternative-proof"}, we give an alternative proof of Theorem [\[thm:41\]](#thm:41){reference-type="ref" reference="thm:41"}.
