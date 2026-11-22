---
doc_id: arxiv-2605.19310v1
doc_title: "A Fourier-Free Density-Increment Proof of Roth's Theorem"
section_id: sec-007-8-further-remarks
section_title: "Further remarks"
section_number: 8
pages: 9-10
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.573
doc_brief: "A Fourier-Free Density-Increment Proof of Roth's Theorem — We give an elementary, Fourier-free proof of Roth’s theorem."
---
Although the proof above is written without Fourier analysis, several of the steps have a simple Fourier interpretation. Let $e(x)=e^{2\pi i x/m}$ and $\widehat f(\xi)=\sum_{x\in\mathbb{Z}_m} f(x)e(-\xi x)$. One then has $\widehat R(\xi)=\lvert\widehat f(\xi)\rvert^2$. Hence Parseval gives $$\mathcal E(f)=\sum_{t\in\mathbb{Z}_m}R(t)^2=
\frac1m\sum_{\xi\in\mathbb{Z}_m}\lvert\widehat f(\xi)\rvert^4.$$ Thus, up to the normalization convention, $\mathcal E(f)$ is the fourth power of what is called in the modern Gowers-style literature the $U^2$-norm. In the usual modern Fourier-analytic proofs of Roth's theorem, the implication from a small $3$-term progression count to a large $U^2$-norm is standard.

The key non-negativity statement in Lemma [\[lem:pos\]](#lem:pos){reference-type="ref" reference="lem:pos"} also has a short Fourier explanation. If $h,k\in\mathbb{Z}_m^\times$ and $\lambda=kh^{-1}$, then $$\label{eq:fourier-positivity}
\sum_{d\in\mathbb{Z}_m}R(hd)R(kd)
=\sum_{t\in\mathbb{Z}_m}R(t)R(\lambda t)
=\frac1m\sum_{\xi\in\mathbb{Z}_m}
\lvert\widehat f(\xi)\rvert^2
\lvert\widehat f(-\lambda^{-1}\xi)\rvert^2
\geq 0.$$ As future research directions, it would be interesting to develop Fourier-free analogues of the following arguments:

1.  a proof of a polylogarithmic Roth bound of the form $r(n)\lesssim n(\log n)^{-c}$ for $c>0$;

2.  the energy-increment proof of Roth's theorem;

3.  Gowers' argument [@Gowers98] for $4$-term arithmetic progressions.
