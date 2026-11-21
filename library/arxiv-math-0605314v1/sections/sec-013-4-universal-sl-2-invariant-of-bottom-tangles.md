---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-013-4-universal-sl-2-invariant-of-bottom-tangles
section_title: "Universal $sl_2$ invariant of bottom tangles"
section_number: 4
pages: 14-16
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.953
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec4 label="sec4"}

In this section, we recall the definition of the universal invariant of bottom tangles, and prove necessary results.

## Bottom tangles {#sec:bottom-tangles}

Here we recall from [@H:universal] the notion of bottom tangles.

An $n$-component *bottom tangle* $T=T_1\cup \cdots\cup T_n$ is a framed tangle in a cube, which is drawn as a diagram in a rectangle as usual, consisting of $n$ arcs $T_1,\ldots,T_n$ such that for each $i=1,\ldots,n$ the component $T_i$ runs from the $2i$th endpoint on the bottom to the $(2i-1)$st endpoint on the bottom, where the endpoints are counted from the left. For example, see Figure [\[fig:bt\]](#fig:bt){reference-type="ref" reference="fig:bt"} (a). (Here and in what follows, we use the blackboard framing convention.)

For each $n\ge 0$, let $\BT_n$ denote the set of the isotopy classes of $n$-component bottom tangles. Set $\BT=\bigcup_{n\ge 0}\BT_n$.

The *closure* $\cl(T)$ of $T$ is the $n$-component, oriented, ordered framed link in $S^3$, obtained from $T$ by pasting a "$\cup$-shaped tangle" to each component of $L$, as depicted in Figure [\[fig:bt\]](#fig:bt){reference-type="ref" reference="fig:bt"} (b). For any oriented, ordered framed link $L$, there is a bottom tangle whose closure is isotopic to $L$.

The *linking matrix* of a bottom tangle $T=T_1\cup \cdots\cup T_n$ is defined as that of the closure $T$. Thus the linking number of $T_i$ and $T_j$, $i\neq j$, is defined as the linking number of the corresponding components in $\cl(T)$, and the framing of $T_i$ is defined as the framing of the closure of $T_i$.

A link or a bottom tangle is called *algebraically-split* if the linking matrix is diagonal.

For $n\ge 0$, let $\BT^0_n$ denote the subset of $\BT_n$ consisting of algebraically-split, $0$-framed bottom tangles. Set $\BT^0=\bigcup_{n\ge 0}\BT^0_n\subset \BT$.

## Universal $sl_2$ invariant of bottom tangles {#sec:univ-sl2-invar}

For each ribbon Hopf algebra $H$, there is a "universal invariant" of links and tangles from which one can recover the operator invariants, such as the colored Jones polynomials. Such universal invariants has been studied in [@Lawrence:89; @Lawrence:90; @Reshetikhin:89; @Lee:90; @Ohtsuki:93; @Kauffman:93; @Kerler:97; @Kauffman-Radford:01]. Here we need only the case of bottom tangles, which is described in [@H:universal].

For $T=T_1\cup \cdots\cup T_n\in \BT_n$, we define the *universal $sl_2$ invariant* $J_T\in U_h^{\ho n}$ of $T$ as follows. We choose a diagram for $T$, which is obtained from copies of *fundamental tangle*, see Figure [\[fig:fundamental\]](#fig:fundamental){reference-type="ref" reference="fig:fundamental"}, by pasting horizontally and vertically.

For each copy of fundamental tangle in the diagram of $T$, we put elements of $U_h$ with the rule described in Figure [\[fig:fundamental2\]](#fig:fundamental2){reference-type="ref" reference="fig:fundamental2"}.

We set $$J_T =\sum J_{(T_1)}\otimes \cdots\otimes J_{(T_n)}\in U_h^{\ho n},$$ where for each $i=1,\ldots,n$, the $i$th tensorand $J_{(T_i)}$ is defined to be the product of the elements put on the component $T_i$. Here the elements read off along each component are written from right to left. Then $J_T$ does not depend on the choice of diagram, and defines an isotopy invariant of bottom tangles.
