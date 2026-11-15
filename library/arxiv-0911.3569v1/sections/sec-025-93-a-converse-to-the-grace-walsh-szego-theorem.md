---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-025-93-a-converse-to-the-grace-walsh-szego-theorem
section_title: "A converse to the Grace-Walsh-Szego Theorem."
section_number: 9.3
pages: 28-29
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.912
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
The argument of Sections 4.2 and 4.3 can be used to prove the following.

\begin{exercise}
If $f\in\Stab[\x]^\ma$ is multiaffine and stable then
$$
T_{\S(m)} (f) = \frac{1}{m!} \sum_{\sigma\in\S(m)} \sigma(f)
$$
is multiaffine and stable.
\end{exercise}

This is in fact equivalent to the GWS Theorem,
since for all $f\in\CC[\x]^{\ma}$, $T_{\S(m)}f(\x) = \Pol_{m} f(x,\ldots,x)$.
For which transitive permutation groups $G\leq\S(m)$ does
the linear transformation $T_G = |G|^{-1}\sum_{\sigma\in G}\sigma$
preserve stability?  The answer:\ not many, and they give nothing new.

\begin{theorem}[Theorem 6 of \cite{BW}.]
Let $G\leq\S(m)$ be a transitive permutation group such that
$T_G$ preserves stability.  Then $T_G=T_{\S(m)}$.
\end{theorem}
