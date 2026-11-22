---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-034-9-twists
section_title: "Twists"
section_number: 9
pages: 32-34
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.89
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec9 label="sec9"}

In this section, we introduce an element $\omega \in \hP$ satisfying a "twisting property".

## The twist element $\omega \in \hP$ {#sec:twist-element-hr-1}

Define two elements $\omega _+,\omega _-\in \hP$ by $$\omega _\pm =\sum_{n=0}^\infty (\pm 1)^n v^{\pm \hf n(n+3)}P'_n.$$

Set $\modS _{\modQ (v)}=\modS \otimes _{\Zqq}\modQ (v)\subset \modR _{\modQ (v)}$. By Proposition [\[r23\]](#r23){reference-type="ref" reference="r23"}, the bilinear map $\langle ,\rangle \zzzcolon \modP \times \modS _{\modQ (v)}\rightarrow \modQ (v)$ induces a bilinear map $$\langle ,\rangle \zzzcolon \hP\times \modS _{\modQ (v)}\rightarrow \modQ (v).$$

::: proposition
[]{#thm:38 label="thm:38"} For each $x\in \modS _{\modQ (v)}$, we have $$\begin{gathered}
    \label{eq:67}
    \langle \omega _\pm ,x\rangle =J_{U_\pm }(x),
  
\end{gathered}$$ where $U_\pm$ is a $\pm 1$-framed unknot.
:::

::: proof
*Proof.* We may assume $x=\V'_{2k}=\V_{2k}/[2k+1]$, $k\ge 0$, without loss of generality.

By [\[eq:37\]](#eq:37){reference-type="eqref" reference="eq:37"}, we have $$\label{e40}
      \langle \omega _\pm ,\V'_{2k}\rangle 
      =\sum_{n\ge 0}(\pm 1)^nv^{\pm \hf n(n+3)}\langle P'_n,\V'_{2k}\rangle 
      =\sum_{n=0}^k (\pm 1)^nv^{\pm \hf n(n+3)}\frac{\{k+n\}_{2n}}{\{n\}!}.$$

Since $\V_{2k}$ is an irreducible $U_h$-module, we have $\modr ^{\mp1}\modv _i^{2k}=J_{U_\pm }(\V'_{2k})\modv _i^{2k}$ for all $i=0,\ldots,2k$. (Recall that $\modr \in U_h$ denotes the ribbon element, and $\modv ^{2k}_i$ for $i=0,\ldots,2k$ denote the basis elements of the irreducible left $U_h$-module $\V_{2k}$.) Consider the case $i=k$. By straightforward calculations using [\[eq:65\]](#eq:65){reference-type="eqref" reference="eq:65"} and [\[eq:66\]](#eq:66){reference-type="eqref" reference="eq:66"}, we obtain $$\modr ^{\mp1}\modv ^{2k}_k
    =\sum_{n=0}^k(\pm 1)^nv^{\pm \hf n(n+3)}\frac{\BB{k+n}{2n}}{\{n\}!}\modv ^{2k}_k.$$ Hence, $J_{U_\pm }(\V'_{2k})$ is equal to the right-hand side of [\[e40\]](#e40){reference-type="eqref" reference="e40"}. Hence, we have [\[eq:67\]](#eq:67){reference-type="eqref" reference="eq:67"} for $x=\V'_{2k}$. ◻
:::

::: proposition
[]{#thm:42 label="thm:42"} $\omega _+$ and $\omega _-$ are inverse to each other in the algebra $\hP$.
:::

::: proof
*Proof.* A direct proof using [\[eq:69\]](#eq:69){reference-type="eqref" reference="eq:69"} is possible. Here we give another proof.

By Proposition [\[thm:38\]](#thm:38){reference-type="ref" reference="thm:38"} and the fact that $\langle -,\V'_{2p}\rangle \zzzcolon \modS _{\modQ (v)}\rightarrow \modQ (v)$ is a $\modQ (v)$-algebra homomorphism, we have $$\langle \omega _+\omega _-,\V'_{2p}\rangle 
    =\langle \omega _+,\V'_{2p}\rangle \langle \omega _-,\V'_{2p}\rangle 
    =q^{p(p+1)}q^{-p(p+1)}
    =1=\langle 1,\V'_{2p}\rangle$$ for each $p\ge 0$. Hence, we have $\langle \omega _+\omega _-,x\rangle =\langle 1,x\rangle$ for all $x\in \modS _{\modQ (v)}$. Since the map $$\hP \rightarrow \Fun(\modS _{\modQ (v)},\modQ (v)),\quad x\mapsto (y\mapsto \langle x,y\rangle ),$$ is injective (by Proposition [\[r23\]](#r23){reference-type="ref" reference="r23"}), it follows that $\omega _+\omega _-=1$. (Here $\Fun(\modS _{\modQ (v)},\modQ (v))$ denotes the set of functions on $\modS _{\modQ (v)}$ with values in $\modQ (v)$.) ◻
:::

Set $\omega =\omega _+$. We have $\omega _-=\omega ^{-1}$.

::: remark
[]{#r28 label="r28"} The twist element $\omega$ was announced first in [@H:iias2000] in a formulation using skein theory, and then in [@H:rims2001] in the present form (without proofs). Later, Masbaum [@Masbaum] gave a proof using skein theory.
:::
