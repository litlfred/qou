---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.869
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
---
Volume Conjectures relate the exponential growth rate of various quantum invariants of hyperbolic 3- manifolds at certain root of unity to the hyperbolic volume of the manifolds. In a series started from [@CZ23-1; @CZ23-2], we plan to prove various volume conjectures related to the twist knots.

In [@CZ23-1] and [@CZ23-2], we have proved the Detcherry-Kalfagianni-Yang's volume conjecture [@DKY18] and Kashaev-Murakami-Murakami's volume conjecture [@Kash97; @MuMu01] for the colored Jones polynomial of twist knot $\mathcal{K}_p$ with $p\geq 6$.

Furthermore, the volume conjecture [@CY18] relates the Reshetikhin-Turaev and the Turaev-Viro invariants of a hyperbolic 3-manifold at certain roots of unity to the hyperbolic volume of this hyperbolic 3-manifold. In [@Oht18], Ohtsuki proved the volume conjecture [@CY18] for the hyperbolic 3-manifolds obtained by doing integral surgery along the figure-8 knot. Later, in [@WongYang20-1], Wong and Yang proved volume conjecture [@CY18] for the hyperbolic 3-manifolds obtained by doing rational surgery along the figure-8 knot. The goal of this article is to prove the volume conjecture for Reshetikhin-Turaev invariants of the hyperbolic 3-manifolds $M_{p,q}$ obtained by doing integral $q$-surgery along the twist knot $\mathcal{K}_p$.

Let us state the main results of this paper precisely. First, we recall that the volume conjecture for Reshetikhin-Turaev invariant [@CY18]:

::: conjecture
[]{#conjecture-CY label="conjecture-CY"} Let $M$ be an oriented closed hyperbolic 3-manifold, for an odd integer $r$, let $RT_r(M)$ be its $r$-th Reshetikhin-Turaev invariant, then at the root of unity $t=e^{\frac{4\pi\sqrt{-1}}{r}}$, $$\begin{align}
\lim_{r\rightarrow \infty} \frac{4\pi}{r}RT_{r}(M)=Vol(M)+\sqrt{-1}CS(M) \mod \pi^2\mathbb{Z}.
\end{align}$$
:::

We define the subset $S\subset\mathbb{Z}_+\times \mathbb{Z}_+$ as follows: $$\begin{align}
S=\{(p,q)\in \mathbb{Z}_+\times \mathbb{Z}_+ |(p,q) \ \text{satisfies the condition} \ (\ref{formula-pqconditions})\}.
\end{align}$$

$$\begin{equation}
  \label{formula-pqconditions}
q\geq \left\{ \begin{aligned}
         & 27  &  \ ( \text{if} \ p=6) \\
         & 19 & \ ( \text{if} \ p=7)  \\ 
         & 17 & \ ( \text{if} \ p=8)  \\
         & 15 & \ ( \text{if} \ p=9, 10)  \\
         & 14 & \ ( \text{if} \ p=11, 12, 13)  \\
         & 13 & \ ( \text{if} \ 14 \leq p\leq 32)  \\ 
         & 12 & \ ( \text{if} \ p\geq 33).  \\ 
                          \end{aligned} \right.
\end{equation}$$

Let $\hat{V}(p,q,\theta_1,\theta_2,\theta_3)$ be the potential function of Reshetikhin-Turaev invariants of $M_{p,q}$ given by formula ([\[formula-PotentialV\]](#formula-PotentialV){reference-type="ref" reference="formula-PotentialV"}). By Proposition [\[prop-critical\]](#prop-critical){reference-type="ref" reference="prop-critical"}, there exists a unique critical point $(\theta_1^0,\theta_2^0,\theta_3^0)$ of $\hat{V}(p,q;\theta_1,\theta_2,\theta_3)$. Let $z_i^0=e^{2\pi\sqrt{-1}\theta_i^0}$ for $i=1,2,3$, we put $$\begin{align}
  \zeta(p,q)&=
\hat{V}(p,q;\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
&=\pi\sqrt{-1}\left(\frac{3q}{2}+(\frac{q}{2}-1)(\theta_1^0)^2-\theta_1^0+(2p+1)(\theta_3^0)^2-(2p+3)\theta_3^0-2\theta_2^0\right)\\\nonumber
&+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(z_2^0z_3^0)+\text{Li}_2\left(\frac{z_2^0}{z_3^0}\right)-\text{Li}_2(z_2^0z_1^0)-\text{Li}_2(z_2^0)-\text{Li}_2\left(\frac{z_2^0}{z_1^0}\right)\right).
\end{align}$$ and $$\begin{align}
 \label{formula-omegapq}
    \omega(p,q)=\frac{z_2^0(z_3^0-(z_3^0)^{-1})(\sqrt{z_1^0}-\frac{1}{\sqrt{z_1^0}})}{\sqrt{(1-z_2^0z_3^0)(1-z_2^0(z_{3}^0)^{-1})}\sqrt{H(p,q;z_1^0,z_2^0,z_3^0)}},
\end{align}$$ where $$\begin{align}
  &H(p,q;z_1^0,z_2^0,z_3^0)=4\frac{z_2^0}{z_1^0-z_2^0}\cdot \frac{z_1^0z_2^0}{1-z_1^0z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &-4\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0z_3^0}{1-z_2^0z_3^0}\cdot\frac{z_2^0}{z_3^0-z_2^0}+\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0}{1-z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &+(8p+4)\frac{z_2^0}{z_1^0-z_2^0}\cdot \frac{z_1^0z_2^0}{1-z_1^0z_2^0}+(2p+1)\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0}{1-z_2^0}\\\nonumber
  &-(2p+\frac{q}{2})\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)-(\frac{q}{2}-1)\frac{z_2^0}{1-z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &+4(\frac{q}{2}-1)\frac{z_2^0z_3^0}{1-z_2^0z_3^0}\cdot\frac{z_2^0}{z_3^0-z_2^0}-(2p+1)(\frac{q}{2}-1)\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}+\frac{z_2^0}{1-z_{2}^0}-\frac{z_2^0z_3^0}{1-z_2^0z_3^0}-\frac{z_2^0}{z_3^0-z_2^0}\right).
\end{align}$$

Then, we have

::: theorem
[]{#theorem-main label="theorem-main"} For $(p,q)\in S$, the asymptotic expansion of Reshetikhin-Turaev $RT_{r}(M_{p,q})$ is given by the following form $$\begin{align}
        RT_{r}(M_{p,q})&=(-1)^{p+1}\sqrt{-1}e^{\sigma((\mathcal{K}_{p})_q)\left(\frac{3}{r}+\frac{r+1}{4}\right)\pi\sqrt{-1}}\omega(p,q)e^{(N+\frac{1}{2})\zeta(p,q)}\\\nonumber
&\cdot\left(1+\sum_{i=1}^d\kappa_i(p,q)\left(\frac{4\pi\sqrt{-1}}{r}\right)^i+O\left(\frac{1}{r^{d+1}}\right)\right),
\end{align}$$ for $d\geq 1$, where $\omega(p,q)$ is given by formula ([\[formula-omegapq\]](#formula-omegapq){reference-type="ref" reference="formula-omegapq"}) and $\kappa_i(p,q)$ are constants determined by the 3-manifold $M_{p,q}$.
:::

By Theorem [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}, we know that $$\begin{align}
     2\pi \zeta(p,q)= Vol(M_{p,q})+\sqrt{-1}CS(M_{p,q}) \mod \pi^2\sqrt{-1}\mathbb{Z}.
\end{align}$$ It implies that

::: corollary
For $(p,q)\in S$, we have $$\begin{align}
        \lim_{r\rightarrow \infty}\frac{4\pi}{r}\log RT_r(M_{p,q};e^{\frac{4\pi \sqrt{-1}}{r}})=Vol(M_{p,q})+\sqrt{-1}CS(M_{p,q}) \mod \pi^2\sqrt{-1}\mathbb{Z}.
\end{align}$$
:::

Hence we proved Conjecture [\[conjecture-CY\]](#conjecture-CY){reference-type="ref" reference="conjecture-CY"} for $M_{p,q}$.

The rest of this article is organized as follows. In Section [\[Section-2RT\]](#Section-2RT){reference-type="ref" reference="Section-2RT"}, we fix the notations and review the related materials that will be used in this paper. In Section [\[Section-Potentialfunction\]](#Section-Potentialfunction){reference-type="ref" reference="Section-Potentialfunction"}, we compute the potential function for the Reshetikhin-Turaev invariant for the 3-manifold obtained by doing integral surgery along the twist knot $\mathcal{K}_p$. In Section [\[Section-Poissonsummation\]](#Section-Poissonsummation){reference-type="ref" reference="Section-Poissonsummation"}, we express the Reshetikhin-Turaev invariant as a summation of Fourier coefficients with the help of Poisson summation formula. In Section [\[Section-asympticexpansion\]](#Section-asympticexpansion){reference-type="ref" reference="Section-asympticexpansion"}, we first show that infinite terms of the Fourier coefficients can be neglected. Then we estimate the remained term of Fourier coefficients by using the saddle point method, we obtain that only four main Fourier coefficients will contribute to the final form of the asymptotic expansion. Hence we finish the proof of the main Theorem [\[theorem-main\]](#theorem-main){reference-type="ref" reference="theorem-main"}. The final Appendix Section [\[Section-Appendices\]](#Section-Appendices){reference-type="ref" reference="Section-Appendices"} is devoted to the proof of several results which will be used in previous sections.

**Acknowledgements.**

The first author would like to thank Nicolai Reshetikhin, Kefeng Liu and Weiping Zhang for bringing him to this area and a lot of discussions during his career, thank Francis Bonahon, Giovanni Felder and Shing-Tung Yau for their continuous encouragement, support and discussions, and thank Jun Murakami and Tomotada Ohtsuki for their helpful discussions and support. He also want to thank Jørgen Ellegaard Andersen, Sergei Gukov, Thang Le, Gregor Masbaum, Rinat Kashaev, Vladimir Turaev, Tian Yang and Hiraku Nakajima for their support, discussions and interests, and thank Yunlong Yao who built him solid analysis foundation twenty years ago. The second author would like to thank Kefeng Liu and Hao Xu for bringing him to this area when he was a graduate student at CMS of Zhejiang University, and for their constant encouragement and helpful discussions since then. Both of us thanks Ruifeng Qiu for his interests and supports.
