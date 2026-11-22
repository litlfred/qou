---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-004-linear-constraints
section_title: "linear constraints"
section_number: null
pages: 9-10
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
The distance distribution $A_j$ of $C$ in ([\[eq:dist_distriubtion\]](#eq:dist_distriubtion){reference-type="ref" reference="eq:dist_distriubtion"}) can be represented in terms of $x_{i,i',j,j'}^{t,t'}$ as $$A_{j} = \sum_{i+i' = j} \binom{n_{1}}{i} \binom{n_{2}}{i'} x_{i, 0, i', 0}^{0, 0}.$$ Furthermore, the propagation rule $A(n-1, 2e-1) = A(n, 2e)$ [@MS77] implies that we need to consider only even distance $j$.

::: lemma
[@Bes80 Lemma $7$] $$\sum_{i = 0}^{n} \binom{n-i}{k}A_{i} \leq \binom{n}{k} A(n-k, d). \label{le3}$$
:::

::: lemma
[@MEL02 Theorem $9$] $$\label{le4}
        A_{n-\frac{d}{2}}+\left\lfloor \frac{2n}{d} \right\rfloor \sum_{i < \lfloor \frac{d}{2} \rfloor}A_{n-i} \leq \left\lfloor \frac{2n}{d} \right\rfloor.$$
:::

Our SDP also benefits from bounds on $A(n,d,w)$, the maximum size of a length-$n$ code with minimum distance $d$ and constant weight $w$.

::: lemma
[@Bes80 Lemma $5$] Let $P = A(n-1, d, \frac{1}{2}d+1)$, $Q = A(n-\frac{1}{2}d, d, \frac{1}{2}d+1)$, $R = A(n-\frac{1}{2}d+2, d, \frac{1}{2}d+2)$, then $$\label{le5}
        \begin{aligned}
            &(\frac{1}{2}d+2)A_{n-\frac{1}{2}d-2}+\frac{1}{2}d(P-Q)A_{n-\frac{1}{2}d} +(n P-(\frac{1}{2}d+2)R)A_{n-\frac{1}{2}d+2}+n P\sum_{i = n-\frac{1}{2}d+3}^{n} A_{i} \leq n P.
        \end{aligned}$$
:::

::: lemma
[@MEL02 Theorem $10$] For $i = 1, \dots, \frac{d}{2}-1$, $$\label{le6}
        \begin{aligned}
            A_{n-\frac{d}{2}-i}+&(A(n, d, \frac{d}{2}+i)-A(n-\frac{d}{2}+i, d, \frac{d}{2}+i))A_{n-\frac{d}{2}+i}+A(n, d, \frac{d}{2}+i)\sum_{j>i}A_{n-\frac{d}{2}+j} \leq A(n, d, \frac{d}{2}+i).
        \end{aligned}$$
:::

::: lemma
[@Sch05 (25)] For $i = 0, \dots, n$, $$\label{le7}
        A_{i} \leq A(n, d, i).$$
:::

We also have additional linear constraints from doubly constant-weight codes. Let $T(w_{1}, t_{1}, w_{2}, t_{2}, d)$ be the maximum possible size of a doubly constant-weight code, which is a $(t_{1}+t_{2}, d, w_{1}+w_{2})$ constant-weight code such that every codeword has exactly $w_{1}$ and $w_{2}$ ones on the first $t_{1}$ and next $t_{2}$ coordinates, respectively.

::: lemma
[@KT13 Theorem $3$] For $i, j, t \in \{0, \dots, n\}$, we have $$\label{le14}
        x_{i, j}^{t} \leq \frac{T(t, i, j-t, n-i, d)}{\binom{i}{t} \binom{n-i}{j-t}}x_{i, 0}^{0}.$$
:::
