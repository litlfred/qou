---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-048-1232-the-ohtsuki-series
section_title: "The Ohtsuki series"
section_number: 12.3.2
pages: 41-42
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.963
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:ohtsuki-series label="sec:ohtsuki-series"} As mentioned in the introduction, according to Lawrence's conjecture proved by Rozansky, the Ohtsuki series $\tau ^O(M)$ for an integral homology sphere can be defined as the unique element $\tau ^O(M)\in \modZ [[q-1]]$ such that for each root of unity $\zeta$ of odd prime power order $r$, $\tau ^O(M)|_{q=\zeta }$ converges $p$-adically to $\tau _\zeta (M)\in \modZ [\zeta ]$, i.e., we have $$\label{e59}
  \mods _\zeta (\tau ^O(M))=\tau _\zeta (M)$$ in $\modZ _p[\zeta ]\cong\varprojlim_n\modZ [\zeta ]/(p^n)\cong\varprojlim_n\modZ [\zeta ]/((\zeta -1)^n)$, where $$\mods _\zeta \zzzcolon \modZ [[q-1]]\rightarrow \modZ _p[\zeta ]$$ denote the ring homomorphism induced by the evaluation map $$\mods _\zeta \zzzcolon \modZ [q]\rightarrow \modZ [\zeta ],\quad  f(q)\mapsto f(\zeta ).$$ These properties characterize $\tau ^O(M)$.

::: theorem
[]{#r52 label="r52"} For every integral homology sphere $M$, we have $\iota _1(J_M)=\tau ^O(M)$.
:::

::: proof
*Proof.* For each root of unity $\zeta$ of prime power order $r=p^e$, we have the following commutative diagram $$\begin{CD}
      \Zqh @>\iota _1>> \modZ [[q-1]]\\
      @V\mods _\zeta VV @VV\mods _\zeta V\\
      \modZ [\zeta ] @>>i> \modZ _p[\zeta ].
    \end{CD}$$ Here $i$ is the inclusion. By the commutativity of the diagram and by Theorem [\[thm:65\]](#thm:65){reference-type="ref" reference="thm:65"}, we have $\mods _\zeta \iota _1(J_M)=i\mods _\zeta (J_M)=i(\tau _\zeta (M))$. Therefore, by [\[e59\]](#e59){reference-type="eqref" reference="e59"}, we have $\mods _\zeta (\iota _1(J_M))=\mods _\zeta (\tau ^O(M))$. The assertion follows from Lemma [\[lem:8\]](#lem:8){reference-type="ref" reference="lem:8"}. ◻
:::

::: lemma
[]{#lem:8 label="lem:8"} The map $$\modZ [[q-1]]\rightarrow \prod_{p:\text{odd prime}}\modZ _p[\zeta _p],\quad
    x\mapsto(\mods _{\zeta _p}(x))_p,$$ is injective. Here $\zeta _p=\exp\frac{2\pi \sqrt{-1}}{p}$.
:::

::: proof
*Proof.* Write $x=\sum_{n\ge 0}x_n(q-1)^n$. We assume that $\mods _{\zeta _p}(x)=0$ for all $p$, and we see that $x_n=0$ by induction on $n$. Let $n\ge 0$ and suppose that $x_0=\cdots=x_{n-1}=0$. Then, for every odd prime $p$, we have $\mods _{\zeta _p}(x)\equiv x_n(\zeta -1)^n\mod (\zeta -1)^{n+1}$. Therefore, $x_n$ is divisible by $p$. It follows that $x_n=0$. ◻
:::
