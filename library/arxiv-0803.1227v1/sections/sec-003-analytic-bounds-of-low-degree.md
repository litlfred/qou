---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-003-analytic-bounds-of-low-degree
section_title: "Analytic bounds of low degree"
section_number: null
pages: 5-7
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
From the explicit description of the zonal functions [\[P1\]](#P1){reference-type="eqref" reference="P1"}, we have deduced convenient polynomials of low degree which verify the positivity property. Using formula ([\[FUNDA\]](#FUNDA){reference-type="ref" reference="FUNDA"}) we derive the analytic bounds of Theorems [\[THM1\]](#THM1){reference-type="ref" reference="THM1"} and [\[THM2\]](#THM2){reference-type="ref" reference="THM2"}.\

::: theorem
[]{#THM1 label="THM1"} Let $\Code$ be a unitary space time code with diversity sum $\Sigma \Nu$, the following upper bounds hold : $$\noindent  \quad |\Code|\le  \frac{2(\Sigma \Nu)^2}{2(\Sigma \Nu)^2-1},
    \quad \text{if }(\Sigma \Nu)^2 >\frac{1}{2}$$ $$\label{DEG2SUM}
   \quad |\Code| \le \frac{8n^2(\Sigma \Nu)^2}{4n^2(\Sigma \Nu)^2-(2n^2-1)}, 
     \text{if }(\Sigma \Nu)^2 > \frac{2n^2-1}{4n^2}$$ $$\quad |\Code| \le \frac{16 n^2 (\Sigma \Nu)^2} {2n(2n-1)(\Sigma \Nu)^2-(2n^2-n-2)},$$ $$\\ \quad \text{if } (\Sigma \Nu)^2 \ge \frac{2n^2-n-2}{2n(2n-1)}$$\
:::

::: theorem
[]{#THM2 label="THM2"} Let $\Code$ be a unitary space time code with diversity product $\Pi \Nu$, the following upper bounds hold : $$|\Code| \le \frac{2(\Pi \Nu)^2}{2(\Pi \Nu)^2-1}, \quad \text{if }(\Pi \Nu)^2 > \frac{1}{{2}}$$

$$\label{DEG2PROD}
   |\Code| \le \frac{8n(\Pi \Nu)^2 }{4n(\Pi \Nu)^2-(2n-1) },  \text{if }(\Pi \Nu)^2 > \frac{2n-1}{4n}, \ n \ge 3$$

$$|\Code| \le \frac{8(\Pi \Nu)^6+4(\Pi \Nu)^4+8(\Pi \Nu)^2}{8(\Pi \Nu)^6-\frac{1}{4}},$$\
$$\text{if }(\Pi \Nu)^2 \ge \frac{1}{2}, \ n=2.$$\
:::

The proofs of these theorems are based on Theorem [\[FUNDATHM\]](#FUNDATHM){reference-type="ref" reference="FUNDATHM"} and on the following lemma :

::: lemma
Let $y_j=\cos \theta_j$ and $m_{[a_1,...,a_r]}(y)$ the elementary symmetric polynomials in the $y_j=\cos \theta_j$. The following polynomials are linear combination of the zonal functions [\[P1\]](#P1){reference-type="eqref" reference="P1"} with non negative coefficients: $$\begin{array}{l}  Q_{[0]}=1 \\
 Q_{[11]}=m_{[11]}(y)+\frac{(n-1)}{4}\\
 Q_{[1]}=m_{[1]}(y) \\
 Q_{[2]}=m_{[2]}(y)+m_{[11]}(y)-\frac{(n+1)}{4}\\
  Q_{[1,1,1]} =\ m_{[1,1,1]}(y) + \frac{(n-2)}{4}m_{[1]}(y)\\
 Q_{[2,1]} =\  m_{[2,1]}(y) +2 m_{[1,1,1]}(y) -\frac{1}{4} m_{[1]}(y) \\
 Q_{[3]} = \  m_{[3]}(y)+m_{[2,1]}(y)+m_{[1,1,1]}(y) -\frac{(n+2)}{4} m_{[1]}(y)\\
  \end{array}$$\
:::

::: proof
*Theorem [\[THM1\]](#THM1){reference-type="ref" reference="THM1"}, Sketch.* Let $s=\frac 1 n \sum_{j=1}^n \cos \theta_j$ so that $s=1-2d_\Sigma^2$. We apply formula ([\[FUNDA\]](#FUNDA){reference-type="ref" reference="FUNDA"}) with the polynomials : $P=Q_{[1]}-ns$, $P=(Q_{[1]}-ns)(Q_{[1]}+n)$, $P=(Q_{[1]}-ns)R$, where $R$ is the symmetrization of $(y_1+1)(y_2+1)$. ◻
:::

::: proof
*Theorem [\[THM2\]](#THM2){reference-type="ref" reference="THM2"}, Sketch.* Let $p=2d_\pi^2$. We apply formula ([\[FUNDA\]](#FUNDA){reference-type="ref" reference="FUNDA"}) with the polynomials : $P=Q_{[1]}-n(p-1)$, $P=Q_{[2]}+\frac{(n+1)p}{2}Q_{[1]}+\frac{(n+1)(2n(p-1)+1)}{4}$ (if $n\ge 3$),\
$P=Q_{[2]}+(\frac{p^2}{2}+2p-1)Q_{[1]}+(p^3-\frac{1}{4})$ (if $n=2$).\
 ◻
:::
