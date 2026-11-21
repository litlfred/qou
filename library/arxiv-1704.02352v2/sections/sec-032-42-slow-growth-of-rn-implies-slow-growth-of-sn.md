---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-032-42-slow-growth-of-rn-implies-slow-growth-of-sn
section_title: "Slow growth of (Rn) implies slow growth of (Sn)"
section_number: 4.2
pages: 30-31
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.837
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
::: lemma
[]{#lem:small-free label="lem:small-free"} Let $(\mathcal{S}_l)_{l\geq 2}$ be a sequence of real numbers and let $(\mathcal{R}_l)_{l\geq 2}$ given by [\[eq:r-s\]](#eq:r-s){reference-type="eqref" reference="eq:r-s"} be the corresponding sequence of free cumulants. Assume that the sequence of free cumulants fulfills the estimate $$\label{eq:free-are-small}
    | \mathcal{R}_l | \leq C^l\ l^{ml}$$ for some constants $m,C\geq 0$ and all $l\geq 2$.

Then the sequence $(\mathcal{S}_l)$ fulfills an analogous estimate $$\label{eq:free-are-smallS}
    | \mathcal{S}_l | \leq C^l\ l^{ml};$$ possibly for another value of the constant $C$.
:::

::: proof
*Proof.* The expansion [\[eq:s-r\]](#eq:s-r){reference-type="eqref" reference="eq:s-r"} for $\mathcal{S}_l$ in terms of the free cumulants gives immediately: $$\begin{gathered}
    \label{eq:ograniczenie}
    |\mathcal{S}_l| \leq \sum_{i\geq 1} \frac{1}{i!}  (l-1)_{i-1}\  
    C^l\sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }} k_1^{m k_1} \cdots
    k_i^{m k_i} \\
    \leq C^l l^{ml}\sum_{i\geq 1} \frac{1}{i!}  (l-1)_{i-1}
    \sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }}1.
    
\end{gathered}$$ Since $$\sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }}1 =
    \sum_{\substack{k_1,\dots,k_i\geq 1 \\ k_1+\cdots+k_i=l-i
    }}1=\binom{l-1-i}{i-1},$$ we can bound the sum on the right-hand side of [\[eq:ograniczenie\]](#eq:ograniczenie){reference-type="eqref" reference="eq:ograniczenie"} as follows: $$\begin{gathered}
    \sum_{i\geq 1} \frac{1}{i!}  (l-1)_{i-1}
    \sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }} 1 \leq
    \sum_{i\geq 1}\binom{l-1}{i-1}\binom{l-1-i}{i-1} \leq \\
    \sum_{i\geq
        0}\binom{l-1}{i}^2 
    \leq \left(\sum_{i\geq 0}\binom{l-1}{i}\right)^2\leq 2^{2l},
    
\end{gathered}$$ which plugged into [\[eq:ograniczenie\]](#eq:ograniczenie){reference-type="eqref" reference="eq:ograniczenie"} yields $$|\mathcal{S}_l| \leq (4C)^l\ l^{ml},$$ which finishes the proof. ◻
:::
