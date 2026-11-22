---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-003-13-a-unified-wrt-invariant-j-m-with-values-in-zq
section_title: "A unified WRT invariant $J_M$ with values in $\Zqh$"
section_number: 1.3
pages: 3-4
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:unif-wrt-invar-1 label="sec:unif-wrt-invar-1"}

The following is the main result of the present paper, and follows from Theorems [\[thm:41\]](#thm:41){reference-type="ref" reference="thm:41"} and [\[thm:65\]](#thm:65){reference-type="ref" reference="thm:65"}.

::: theorem
[]{#r40 label="r40"} There is an invariant $J_M\in \Zqh$ of an integral homology sphere $M$ such that for any root of unity $\zeta$ we have $$\label{e56}
    \mods _\zeta (J_M) = \tau _\zeta (M).$$
:::

The properties of the ring $\Zqh$ explained in the last subsection implies that the WRT function $\tau (M)$ may be regarded as an analytic function defined on $\calZ$. Let us describe some corollaries to Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} and properties of the ring $\Zqh$. (Part of the discussion below overlaps those in [@H:rims2001; @H:cyclotomic].)

An immediate consequence of Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} is the following generalization of Murakami's integrality result.

::: corollary
[]{#r14 label="r14"} For any integral homology sphere $M$ and for $\zeta \in \calZ$, we have $\tau _\zeta (M)\in \modZ [\zeta ]$.
:::

Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} immediately implies *Galois equivariance* of $\tau _\zeta (M)$. Namely, we have $$\label{e67}
  \tau _{\alpha (\zeta )}(M)=\alpha (\tau _\zeta (M))$$ for $\alpha \in \Gal(\modQ ^{ab}/\modQ )$ and $\zeta \in \calZ$. Here $\modQ ^{ab}$ denotes the maximal abelian extension of $\modQ$, which is generated over $\modQ$ by all roots of unity. ($\Gal(\modQ ^{ab}/\modQ )$ can be identified with the automorphism group of the group $\calZ\cong\modQ /\modZ$.) It is well known that the Galois equivariance of $\tau _\zeta (M)$ is implied by Reshetikhin and Turaev's definition. Theorem [\[r40\]](#r40){reference-type="ref" reference="r40"} reexplains it in an apparent way.

Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"} implies the following.

::: theorem
[]{#r48 label="r48"} The invariant $J_M$ is determined by the WRT function $\tau (M)$. (Thus $J_M$ and $\tau (M)$ have the same strength in distinguishing two integral homology spheres.) Moreover, both $J_M$ and $\tau (M)$ are determined by the values of $\tau _\zeta (M)$ for $\zeta \in \calZ'$, where $\calZ'\subset \calZ$ is any infinite subset with a limit point in the sense explained in Section [\[sec:ring-zqh-cyclotomic\]](#sec:ring-zqh-cyclotomic){reference-type="ref" reference="sec:ring-zqh-cyclotomic"}.
:::

The invariant $J_M$ unifies not only the WRT invariants but also the Ohtsuki series $\tau ^O(M)$. Namely, we have (Theorem [\[r52\]](#r52){reference-type="ref" reference="r52"}) $$\label{e12}
  \iota _1(J_M)=\tau ^O(M).$$

Injectivity of $\iota _\zeta$ in [\[e6\]](#e6){reference-type="eqref" reference="e6"} for each $\zeta \in \calZ$ implies that the $J_M$ and hence $\tau (M)$ are determined by the power series expansion $\iota _\zeta (J_M)\in \modZ [\zeta ][[q-\zeta ]]$. In particular, $J_M$ is determined by $\tau ^O(M)$, in view of [\[e12\]](#e12){reference-type="ref" reference="e12"}. Thus $J_M$ and $\tau ^O(M)$ have the same strength in distinguishing integral homology spheres. As a consequence, the Le-Murakami-Ohtsuki invariant [@LMO] determines $J_M$ and $\tau (M)$, since it determines $\tau ^O(M)$ (see [@Ohtsuki4]).

For further properties of $J_M$, see Sections [\[sec12\]](#sec12){reference-type="ref" reference="sec12"} and [\[sec13\]](#sec13){reference-type="ref" reference="sec13"}.
