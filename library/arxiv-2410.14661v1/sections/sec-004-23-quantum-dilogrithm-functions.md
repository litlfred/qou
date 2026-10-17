---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-004-23-quantum-dilogrithm-functions
section_title: "Quantum dilogrithm functions"
section_number: 2.3
pages: 7-7
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.919
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
For a positive integer $N$, we set $t=e^{\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}}$. We introduce the holomorphic function $\varphi_N(\theta)$ for $\{\theta\in
\mathbb{C}| 0< \text{Re}(\theta) < 1\}$, by the following integral $$\begin{aligned}
\varphi_N(\theta)=\int_{-\infty}^{+\infty}\frac{e^{(2\theta-1)x}dx}{4x \sinh x
\sinh\frac{x}{N+\frac{1}{2}}}.
\end{aligned}$$ Noting that this integrand has poles at $n\pi \sqrt{-1} (n\in
\mathbb{Z})$, where, to avoid the poles at $0$, we choose the following contour of the integral $$\begin{aligned}
\gamma=(-\infty,-1]\cup \{z\in \mathbb{C}||z|=1, \text{Im} z\geq 0\}
\cup [1,\infty).
\end{aligned}$$

::: lemma
[]{#lemma-varphixi label="lemma-varphixi"} The function $\varphi_N(\theta)$ satisfies $$\begin{aligned}
    (t)_n&=\exp \left(\varphi_N\left(\frac{1}{2N+1}\right)-\varphi_N\left(\frac{2n+1}{2N+1}\right)\right)   \  \   \left(0\leq n\leq N\right), \\
    (t)_n&=\exp \left(\varphi_N\left(\frac{1}{2N+1}\right)-\varphi_N\left(\frac{2n+1}{2N+1}-1\right)+\log 2\right)   \  \   \left(N< n\leq 2N\right).
\end{aligned}$$
:::

::: lemma
[]{#lemma-varphixi2 label="lemma-varphixi2"} We have the following identities: $$\begin{aligned}
    \varphi_N(\theta)+\varphi_N(1-\theta)&=2\pi \sqrt{-1}\left(-\frac{2N+1}{4}\left(\theta^2-\theta+\frac{1}{6}\right)+\frac{1}{12(2N+1)}\right),\\ 
    \varphi_N\left(\frac{1}{2N+1}\right)&=\frac{2N+1}{4\pi\sqrt{-1}}\frac{\pi^2}{6}+\frac{1}{2}\log \left(\frac{2N+1}{2}\right)+\frac{\pi \sqrt{-1}}{4}-\frac{\pi \sqrt{-1}}{6(2N+1)},\\
    \varphi_N\left(1-\frac{1}{2N+1}\right)&=\frac{2N+1}{4\pi\sqrt{-1}}\frac{\pi^2}{6}-\frac{1}{2}\log \left(\frac{2N+1}{2}\right)+\frac{\pi \sqrt{-1}}{4}-\frac{\pi \sqrt{-1}}{6(2N+1)}.
\end{aligned}$$
:::

The function $\varphi_N (\theta)$ is closely related to the dilogarithm function as follows.

::: lemma
[]{#lemma-varphixi3 label="lemma-varphixi3"} (1) For every $\theta$ with $0<\text{Re}(\theta)<1$, $$\begin{aligned}
        \varphi_N(\theta)=\frac{N+\frac{1}{2}}{2\pi \sqrt{-1}}\text{Li}_2(e^{2\pi\sqrt{-1}\theta})
 -\frac{\pi \sqrt{-1}e^{2\pi\sqrt{-1}\theta}}{6(1-e^{2\pi\sqrt{-1}\theta})}\frac{1}{2N+1}+O\left(\frac{1}{(N+\frac{1}{2})^3}\right).
    
\end{aligned}$$ (2) For every $\theta$ with $0<\text{Re}(\theta)<1$, $$\begin{aligned}
        \varphi_N'(\theta)=-\frac{2N+1}{2}\log(1-e^{2\pi\sqrt{-1}\theta})+O\left(\frac{1}{N+\frac{1}{2}}\right)
    
\end{aligned}$$ (3) As $N\rightarrow \infty$, $\frac{1}{N+\frac{1}{2}}\varphi_N(\theta)$ uniformly converges to $\frac{1}{2\pi\sqrt{-1}}\text{Li}_2(e^{2\pi\sqrt{-1}\theta})$ and $\frac{1}{N+\frac{1}{2}}\varphi'_N(\theta)$ uniformly converges to $-\log(1-e^{2\pi\sqrt{-1}\theta})$ on any compact subset of $\{\theta\in \mathbb{C}|0<\text{Re}(\theta)<1\}$.
:::

See the literature, such as [@Oht16; @CJ17; @WongYang20-1] for the proof of Lemma [\[lemma-varphixi\]](#lemma-varphixi){reference-type="ref" reference="lemma-varphixi"}, [\[lemma-varphixi2\]](#lemma-varphixi2){reference-type="ref" reference="lemma-varphixi2"}, [\[lemma-varphixi3\]](#lemma-varphixi3){reference-type="ref" reference="lemma-varphixi3"}.
