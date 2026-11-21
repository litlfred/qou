---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-014-71-a-two-term-ladder-identity-for-the-plastic-ra
section_title: "A two-term ladder identity for the Plastic Ratio/Constant"
section_number: 7.1
pages: 21-23
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
We will derive a two-term cubic dilogarithm ladder identity where both terms are real. These are uncommon, compared to three-term and above series or series with 2 or more complex terms. Let: $$\begin{aligned}
- \operatorname{Li}_2((1-z)^2) + \frac{\pi^2}{6} - 2 \ln(1-z) \left( \ln(2-z) + \ln z \right) = \operatorname{Li}_2(2z - z^2)\\
\operatorname{Li}_2(2-z) + \operatorname{Li}_2(z) = \frac{1}{2} \operatorname{Li}_2(2z - z^2) + \frac{\pi^2}{4}\\
\operatorname{Li}_2(z) = \operatorname{Li}_2\left(\frac{z-1}{z}\right) + \frac{1}{2} \ln^2 \left( \frac{z}{1-z} \right) - \frac{1}{2} \ln^2(1-z) + \frac{\pi^2}{6}
\end{aligned}$$ Aplying elementary transformations twice, solving for $u,z$, we have that $$\begin{aligned}
\left\{
\begin{array}{l}
z=1-\frac{1}{\frac{1}{2} \left(-u + \sqrt{(4 - 3u) u} + 2 \right)} , \\
2 - z = \frac{1}{1 - \frac{1}{2} \left(-u - \sqrt{(4 - 3u) u} + 2 \right)}
\end{array}
\right.
\end{aligned}$$ We have, where $z$ is the real root of $z^3+z^2-1=0$ and $u=z$, that $$3 \operatorname{Li}_2(z^2) + 6 \operatorname{Li}_2(z) = - \ln^2(z - z^2) - 6 \ln(z) \ln(z + 1) + \pi^2$$ Note that $z=1/p$ where $p$ is the so-called *Plastic Constant* or ratio, given as the real root of $p^3-p-1=0$. It also obeys the following identities: $p-1=p^{-4}, p^{-5}=1-1/p,p^{3}=p+1,p^{2}=1+1/p$. Thus we have the following relations: $$\begin{aligned}
\mathrm{Li_2}(p^{-2}) + 2\mathrm{Li_2}(p^{-1}) &= -8\ln^2(p) + \frac{\pi^2}{3} \\
\mathrm{Li_2}(p^{-1}) + \mathrm{Li_2}(p^{-5}) &= \frac{\pi^2}{6} - 5\ln^2(p) \\ 
\mathrm{Li_2}(p^{-2}) - 2\mathrm{Li_2}(p^{-5}) &= 2\ln^2(p)\\
\operatorname{Li}_2(p^2) + \operatorname{Li}_2(p^3) = -\frac{1}{2} \ln^2(p) + \frac{\pi^2}{2}\\
\operatorname{Li}_2(-p^{-4}) - \operatorname{Li}_2(p^{-1}) = -\frac{\pi^2}{6} + \frac{9}{2} \ln^2(p)
\end{aligned}$$ This also leads to various ladder expressions: $$\begin{aligned}
\frac{5}{2} \mathrm{Li}_2(p^{-2}) + \mathrm{Li}_2(p^{-1}) - 4\mathrm{Li}_2(p^{-5}) = \frac{\pi^2}{6}\\
\mathrm{Li}_2\left(\frac{1}{p^{14}}\right) - 4\mathrm{Li}_2\left(\frac{1}{p^7}\right) + 6\mathrm{Li}_2\left(\frac{1}{p^5}\right) = \frac{\pi^2}{6}-8\ln^2(p)
\end{aligned}$$

::: example
Setting $u=1/2+i\mu$, it is possible to derive additional single-term dilogarithms by combining the first identity in Theorem [\[previously8p1\]](#previously8p1){reference-type="ref" reference="previously8p1"} with [\[previously7p5\]](#previously7p5){reference-type="eqref" reference="previously7p5"}. Define $\mu$ as an algebraic number given by the expression below. This is derived by setting solving for real $\mu$ for $u=1/2+i \mu$ , which has four possible solutions: $$\frac{1}{2} = \Re\left(\frac{4}{\pm\sqrt{12 \mu^2 + 4 i \mu + 5} - 2 i \mu + 3}\right)$$ The solutions are the real roots of $-256 c^8 + 96 c^4 + 544 c^2 - 125=0$, or: $$\mu_1\approx\pm1.1441...\mu_2 \approx \pm 0.4714...$$ Plugging $u=1/2+\mu_2i$ into the first identity in Theorem [\[previously8p1\]](#previously8p1){reference-type="ref" reference="previously8p1"} thus produces a single-term dilogarithm identity, and the same holds for $u=1/2+\mu_1i$. Moreover, we have that $\mu_1,\mu_2$ admit closed forms, with $$\mu_1^2=\frac{1}{32} 
 \sqrt{\frac{k_1+192}{3}} + \frac{1}{2} \sqrt{-\frac{k_1}{768}+\frac{1}{2} + 68 \sqrt{\frac{3}{k_1+192}}}$$ and $$\mu_2^2 = 
 \frac{1}{32} \sqrt{\frac{k_1+192}{3}} - \frac{1}{2} \sqrt{-\frac{k_1}{768}+\frac{1}{2} + 68 \sqrt{\frac{3}{k_1+192}}},$$ writing $$k_1=128 \cdot 2^{2/3} \cdot 3^{1/3} \left( (45 - \sqrt{1929})^{1/3} + (45 + \sqrt{1929})^{1/3} \right).$$ Using the two-term identity in Example [\[previously7p6\]](#previously7p6){reference-type="ref" reference="previously7p6"}, these are obtained by solving a system of equations, where $\theta=1$ corresponds to $\mu_1$ and $\theta=-1$ corresponds to $\mu_2$. $$\begin{aligned}
 \frac{3}{4} + \theta \frac{\sqrt{12 \mu^2 + 5 + \sqrt{144 \mu^4 + 136 \mu^2 + 25}}}{4 \sqrt{2}} = \frac{2}{4k^2+1} \\ 
 - \frac{\mu}{2}+\theta \frac{\sqrt{-12 \mu^2 -5 + \sqrt{144 \mu^4 + 136 \mu^2 + 25}}}{4 \sqrt{2}} = \frac{-4k}{4k^2+1} 
\end{aligned}$$ This allows us to produce the explicit identity such that $$\begin{gathered}
 -3 \Re\operatorname{Li}_2 \left( \frac{24 k^2 - 
 2 + 4 i (4 k^2 \mu - 4 k + \mu)}{4 k^2 (4 \mu^2 + 9) - 32 k \mu + 4 \mu^2 + 1} \right) = 
 -\frac{1}{8} \ln^2(k^2 + \frac{1}{4}) + \\ 
 \ln^2 \left( \frac{4 k \mu + 6 i k - 2 i \mu - 1}{4 k \mu + 2 i k - 2 i \mu - 3} \right) 
- \frac{5}{2} \arctan^{2}(2 k) 
- \arctan^{2}(2 \mu) 
+ \pi \arctan(2 \mu). 
\end{gathered}$$
:::
