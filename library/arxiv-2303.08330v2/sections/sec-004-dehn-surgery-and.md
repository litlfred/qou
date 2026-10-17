---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II"
section_id: sec-004-dehn-surgery-and
section_title: "Dehn surgery and"
section_number: null
pages: 7-8
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.951
---
In [@GPPV], it was conjectured that the $sl(2)$ WRT invariant of a rational homology 3-sphere $Y\, (b_1(Y)=0)$ decomposes into a linear combination of power series $\hat{Z}(q)$, which converges in $|q|<1$ and itself is an invariant of $Y$. Specifically, $$WRT[Y;k]= \frac{1}{i\sqrt{2k}} \sum_{a,b \in Spin^c (Y)} c^{WRT}_{ab}\, \hat{Z}_{b}(q) \Big\vert_{q \rightarrow e^{\frac{i2\pi}{k}}},$$ where $$\hat{Z}_{b}(Y;q) \in \frac{1}{2^c}q^{\Delta_{b}} \mathbb{Z}[[q]], \qquad |q|<1,\qquad \Delta_{b} \in \mathbb{Q},\quad c \in \mathbb{Z}_{\geq 0}.$$ Performing a Dehn surgery on a complement of a knot $K$ along a (negative) slope $-p/r$ [^1] yields a relation between $F_K (x,q)$ and $\hat{Z}(q)$ given by [@GM] $$\hat{Z}_{b}[Y_{-\frac{p}{r}}(K);q] = \pm q^d \mathcal{L}^{(b)}_{-p/r} \left[\left(x^{\frac{1}{2r}} - x^{-\frac{1}{2r}} \right)F_{K}(x,q) \right]\qquad d \in \mathbb{Q},$$ $$\mathcal{L}^{(b)}_{-p/r} : x^{u}q^{v} \mapsto \begin{cases}
      q^{u^2 r/p}q^v & \text{if}\quad ru - b \in p\mathbb{Z}\\
      0 & \text{otherwise}
\end{cases}$$ Performing surgeries along $-1/r$ slopes for a few $r$ results in $$\begin{aligned}
\hat{Z}_0 [S^{3}_{-\frac{1}{2}}(C_{11,2}(4_1));q] & = q^{\frac{167}{2}} \Big( -1+q^{13}-2 q^{59}+2 q^{76}-q^{133}-3 q^{134}-q^{135}+q^{154}+3 q^{155}+q^{156}\\
& -2q^{223}-2 q^{224}-5 q^{225}-2 q^{226}-2 q^{227}+2 q^{248}+2 q^{249} + \cdots  \Big)\\
\hat{Z}_0 [S^{3}_{-\frac{1}{3}}(C_{11,2}(4_1));q] & = q^{\frac{251}{2}}  \Big( -2+2 q^{13}-4 q^{89}+4 q^{106}-2 q^{201}-6 q^{202}-2 q^{203}+2 q^{222}+6 q^{223}\\
& +2 q^{224} -4 q^{337}-4 q^{338}-10 q^{339}-4 q^{340}-4 q^{341}+4 q^{362}+4 q^{363} + \cdots  \Big)\\
\hat{Z}_0 [S^{3}_{-\frac{1}{4}}(C_{11,2}(4_1));q] & = q^{\frac{335}{2}} \Big( -2+2 q^{13}-4 q^{119}+4 q^{136}-2 q^{269}-6 q^{270}-2 q^{271}+2 q^{290}+6 q^{291}\\
& +2 q^{292} -4q^{451}-4 q^{452}-10 q^{453}-4 q^{454}-4 q^{455}+4 q^{476}+4 q^{477} + \cdots  \Big)\\
\end{aligned}$$

[^1]: Surgery along a positive slope may not produce a power series; there has been some progress on positive surgery in [@P].
