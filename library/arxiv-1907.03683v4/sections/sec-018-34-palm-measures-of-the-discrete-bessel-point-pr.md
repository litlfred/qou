---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-018-34-palm-measures-of-the-discrete-bessel-point-pr
section_title: "Palm measures of the discrete Bessel point process"
section_number: 3.4
pages: 17-18
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.982
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
In regards of subsection [\[secpalm\]](#secpalm){reference-type="ref" reference="secpalm"} and Proposition [\[proppalm\]](#proppalm){reference-type="ref" reference="proppalm"}, we can now give a description of the Palm measures of the discrete Bessel point process $\mathfrak{S}^0_*(\mathbb{P}_\alpha)$, the determinantal point process with kernel $K_\alpha$ given by ([\[discretebesselkernel\]](#discretebesselkernel){reference-type="ref" reference="discretebesselkernel"}).

::: thm
[]{#thmpalmbessel label="thmpalmbessel"}Let $\tilde{u}_1,...,\tilde{u}_k \in \mathbb{Z}$ be pairwise distinct. For $\alpha >0$, let $\left( \mathfrak{S}^0_* (\mathbb{P}_\alpha) \right)^{k}$ be the reduced Palm measure of the discrete Bessel point process at $\tilde{u}_1,...,\tilde{u}_k$. Then, the process $\left( \mathfrak{S}^0_* (\mathbb{P}_\alpha) \right)^{k}$ is a determinantal process with kernel $$\begin{aligned}
K_\alpha^{\tilde{u}_1,...,\tilde{u}_k}(x,y):=\frac{\alpha^{\frac{2k+1}{2}}}{C_{k,k}^2 \prod_{i=1}^k|(x-\tilde{u}_i)(y-\tilde{u}_i)|} \frac{A_{k,k}(x)A_{k,1+k}(y)-A_{k,k}(y)A_{k,1+k}(x)}{x-y}.
\end{aligned}$$
:::

::: rem
[]{#remtasep label="remtasep"}From [@borodingorin], Theorem 4.1, the kernel $K_\alpha^{\tilde{u}_1,...,\tilde{u}_k}$ serves as the correlation kernel of the TASEP with initial step condition at time $t=\alpha$ under the condition that the position $\tilde{u}_1,...,\tilde{u}_k$ are occupied.
:::

::: proof
*Proof of Theorem [\[thmpalmbessel\]](#thmpalmbessel){reference-type="ref" reference="thmpalmbessel"}.* By Propositions [\[proppalm\]](#proppalm){reference-type="ref" reference="proppalm"} and [\[propchristoffel\]](#propchristoffel){reference-type="ref" reference="propchristoffel"}, the reduced Palm measure at $\tilde{u}_1+N,...,\tilde{u}_k+N$ of the $N$-th Charlier ensemble with parameter $\alpha/N$, shifted by $-N$, is a determinantal point process with kernel $K_{N-k}^{\alpha/N,k}(x+N,y+N)$. The case $k=0$ of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} together with Proposition [\[propcvpalm\]](#propcvpalm){reference-type="ref" reference="propcvpalm"} imply that the reduced Palm measure of the $N$-th Charlier ensemble at $\tilde{u}_1+N,...,\tilde{u}_k+N$ shifted by $-N$ converges to the reduced Palm measure of the discrete Bessel point process at points $\tilde{u}_1,...,\tilde{u}_k$. On the other hand, slight modifications of the proof of Theorem [\[thm1\]](#thm1){reference-type="ref" reference="thm1"} (precisely, we just replace $N$ by $N-k$) lead to $$\begin{aligned}
\lim_{N \rightarrow +\infty} K_{N-k}^{\alpha/N,k}(x+N,y+N)= K_{\alpha}^{\tilde{u}_1,...,\tilde{u}_k}(x,y).
\end{aligned}$$ We deduce from this fact that the latter kernel $K_{\alpha}^{\tilde{u}_1,...,\tilde{u}_k}$ serves as a kernel for the point process $\left( \mathfrak{S}^0_*(\mathbb{P}_\alpha)\right)^{k}$. ◻
:::
