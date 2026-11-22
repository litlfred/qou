---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-008-341-bulk-correlations
section_title: "BULK CORRELATIONS"
section_number: 3.4.1
pages: 20-21
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.872
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
Our conventions are such that if we have $N$ eigenvalues, the global spectral density is normalized to $N$ so that the mean level spacing is of order $1/N$. Local spectral correlation functions $R_k(\lambda_1,\ldots,\lambda_k)$ in the bulk of the spectrum are thus characterized by $\lambda_p\sim{\cal O}(1)$ and $|\lambda_p-\lambda_q|\sim{\cal O}(1/N)$. Universal correlation functions are obtained by rescaling the eigenvalues according to the average local level spacing. This procedure, known as unfolding, is discussed in more detail in Sec. [\[unfolding\]](#unfolding){reference-type="ref" reference="unfolding"}. The rescaled eigenvalues with average level spacing equal to unity are denoted by $x_k$.

In the bulk of the spectrum, the RMT results for the $R_k$ are identical for the chiral ensembles and the corresponding nonchiral ensembles [@Fox64; @nagao]. For simplicity, let us consider the simplest ensemble, the chUE. On the unfolded scale, we obtain in the limit $N\to\infty$ $$\label{det}
  R_k(x_1,\ldots,x_k)=\det[K(x_p,x_q)]_{p,q=1,\ldots,k}$$ with the sine kernel $$K(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)}\:.$$ The fact that $K(x,y)$ depends only on $|x-y|$ reflects the translational invariance of the spectral properties after unfolding. The results for the chOE and the chSE are somewhat more complicated than those for the chUE [@Mehta].

Other quantities can be derived from the $R_k$. As a measure of short-range correlations between the eigenvalues, one considers the nearest-neighbor spacing distribution $P(s)$, which is the probability density to have a spacing of $s$ between adjacent levels. In random matrix theories, one finds that $P(s) \sim s^\beta$ for small values of $s$ and has a Gaussian tail for large spacings. Long-range spectral correlations are characterized by the level-number variance $\Sigma^2(L)$ given by $$\Sigma^2(L)=\left\langle(n(L)-L)^2\right\rangle\:,$$ where $n(L)$ is the number of levels in an interval of length $L$, or by the spectral rigidity $\Delta_3(L)$ [@deltaDM], which is defined as an integral transform of $\Sigma^2(L)$, $$\Delta_{3}(L)=\frac{2}{L^4}\int_0^Ldu\:(L-u)(L^2-Lu-u^2)\Sigma^2(u)\:.$$ The advantage of using the $\Delta_3$-statistic is that its statistical fluctuations are much smaller than those of the $\Sigma^2$-statistic. The quantities $\Sigma^2$ and $\Delta_3$ can be derived from the two-point function $R_2$. To compute $P(s)$, one needs all $k$-point functions. These quantities are very different for systems with correlated eigenvalues (described by RMT) and systems with uncorrelated eigenvalues (described by the Poisson ensemble). For example, the large-$L$ behavior of the chUE results is given by $\Sigma^2(L)\sim(\ln L)/\pi^2$ and $\Delta_3(L)\sim(\ln L)/2\pi^2$, whereas for uncorrelated eigenvalues one finds $\Sigma^2(L)=L$ and $\Delta_3(L)=L/15$.
