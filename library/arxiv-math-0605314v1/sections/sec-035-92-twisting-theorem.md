---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-035-92-twisting-theorem
section_title: "Twisting theorem"
section_number: 9.2
pages: 34-34
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:twisting-theorems label="sec:twisting-theorems"}

::: theorem
[]{#thm:99 label="thm:99"} Let $L_1\cup \cdots\cup L_m\cup K$ be an $(m+1)$-component, algebraically-split, $0$-framed link such that $K$ is an unknot. Set $L=L_1\cup \cdots\cup L_m$, and let $L_{(K,\pm 1)}$ denote the framed link in $S^3$ obtained from $L$ by $\pm 1$-framed surgery along $K$. Then, for any $x_1,\ldots,x_m\in \hP$, we have $$\label{eq:81}
    J_{L\cup K}(x_1,\ldots,x_m,\omega ^{\mp1})=J_{L_{(K,\pm 1)}}(x_1,\ldots,x_m).$$
:::

::: proof
*Proof.* By Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"}, it suffices to prove [\[eq:81\]](#eq:81){reference-type="eqref" reference="eq:81"} for $x_1,\ldots,x_m\in \modP$. In fact, we will show [\[eq:81\]](#eq:81){reference-type="eqref" reference="eq:81"} for $x_1,\ldots,x_m\in \modR _{\modQ (v)}$. (Well-definedness of the left-hand side of [\[eq:81\]](#eq:81){reference-type="eqref" reference="eq:81"} in this case follows from the argument below.) Apply the standard "fusing" argument to the strands running through the unknot $K$, see Figure [\[X01\]](#X01){reference-type="ref" reference="X01"}. In the left-hand side, the strands running through $K$ are paired in such a way that each pair contains two segments from the same component of $L$ in the opposite orientations. By fusing these strands, we obtain a linear combination of trivalent colored graphs, where each term has exactly one edge $e$ running through $K$, colored by an even number. Hence, there is $y\in \modS _{\modQ (v)}$ such that $$J_{L\cup K}(x_1,\ldots,x_m,\omega ^{\mp1}) =J_H(y,\omega ^{\mp1}) =\langle \omega ^{\mp1},y\rangle ,$$ where $H$ denotes the Hopf link with $0$-framings. By Proposition [\[thm:38\]](#thm:38){reference-type="ref" reference="thm:38"}, the right-hand side is equal to $J_{U_\mp}(y)$, where $U_\mp$ denotes the $\mp1$-framed unknot. Since we have $$J_{U_\mp}(y)=J_{L_{(K,\pm 1)}}(x_1,\ldots,x_m),$$ we have [\[eq:81\]](#eq:81){reference-type="eqref" reference="eq:81"}. ◻
:::
