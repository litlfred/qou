---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-009-71-a-two-term-ladder-identity-for-the-plastic-ra
section_title: "A two-term ladder identity for the Plastic Ratio/Constant"
section_number: 7.1
pages: 21-29
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 1.0
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

# Applications of Roger's identity

Our below applications of Roger's identity are useful in the construction of new dilogarithm ladder relations, as we later demonstrate.

::: lemma
[]{#previously10p1 label="previously10p1"} The equality of $$\begin{gathered}
 3 \operatorname{Li}_2\left(\frac{-2u^2 + 3u + \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + 
 3 \operatorname{Li}_2\left(\frac{-2u^2 + 3u - \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + \\ 
 3 \operatorname{Li}_2(u) + 3 \operatorname{Li}_2((u - 1)^2) 
\end{gathered}$$ and $$\begin{gathered}
 \text{ {\footnotesize $ - \frac{3}{2} \ln^2\left(\frac{2}{u - \sqrt{(4 - 3u) u} - 2}\right) 
 - \frac{3}{2} \ln^2\left(\frac{2}{u + \sqrt{(4 - 3u) u} - 2}\right) 
 + \ln^2\left(1 - \frac{2}{u + \sqrt{(4 - 3u) u}}\right) $ } } \\ 
 \text{ { \footnotesize $ + \ln^2\left(1 + \frac{2}{\sqrt{(4 - 3u) u} - u}\right) 
 - 3 \ln\left(\frac{u - \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) 
 \ln\left(\frac{u + \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + $ } } \\ 
 \text{ { \footnotesize $ \ln^2(1 - u) - \frac{\ln^2(-u)}{2} - 2 \ln(-u) \ln(1 - u) - \frac{3 \pi^2 }{2}$. } } 
 
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* By setting $$w = \frac{-u - \sqrt{(4 - 3u)u} + 2}{2} \ \ \ \text{and} \ \ \ z = \frac{-u + \sqrt{(4 - 3u)u} + 2}{2},$$ the desired result follows from the application of Roger's identity to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}. ◻
:::

::: lemma
[]{#previously10p2 label="previously10p2"} The equality of $$\begin{gathered}
 \operatorname{Li}_2 \left( \frac{2 u^2 - 3 u - \sqrt{u(4-3u)}}{2 (u-1)^2} \right) 
 + \operatorname{Li}_2 \left( \frac{(u - 1) \left(2 u^3 - 4 u^2 + 3 u - \sqrt{u(4 - 
 3 u)} \right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) \\ 
 + \operatorname{Li}_2 \left( \frac{u \left( u^2 - u + (u - 1) \sqrt{u(4-3u)} + 
 2 \right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) 
 + \operatorname{Li}_2 \left( \frac{u \left(2 u^2 - 3 u + \sqrt{u(4-3u)}\right)}{2 (u-1)^2} \right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
 \text{ { \footnotesize $ - \ln \left( \frac{u^2 - u + (u - 
 1) \sqrt{u(4 - 3 u)} + 2}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) 
 \ln \left( \frac{(u - 1) \left(2 u^3 - 5 u^2 - u \sqrt{(4 - 3 u) u} + 4 u - 2\right)}{2 \left(u^4 - 3 u^3 + 
 4 u^2 - 2 u + 1\right)} \right) - $ } } \\ 
 \text{ { \footnotesize $ \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{u(4-3u)}}{2(u-1)} \right) - 
 \frac{1}{2} \ln^2 (1 - u)$. } }
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* Setting $w = u$ and $$z = \frac{2u^2-3u \pm \sqrt{(4 - 3u)u} + 2}{2(u-1)^2},$$ the desired result follows from the application of Roger's identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}. ◻
:::

::: lemma
[]{#previously10p3 label="previously10p3"} The equality of $$\begin{gathered}
 \operatorname{Li}_2\left(\frac{u - \sqrt{u(4 - 3u)}}{4u - 2u^2}\right) + 
 \operatorname{Li}_2\left(\frac{u + \sqrt{u(4 - 3u)}}{4u - 2u^2}\right) + \\ 
 \operatorname{Li}_2\left(\frac{1}{(u - 1)^2}\right) + \operatorname{Li}_2\left(\frac{u}{u - 1}\right) - \frac{\pi^2}{3} 
\end{gathered}$$ and the closed form $$\begin{gathered}
 \text{ { \footnotesize $ \frac{3}{2} \ln^2 \left(\frac{u - \sqrt{-u (3 u - 4)} - 2}{2 (u - 1)}\right) 
 - \ln \left(\frac{-2 u^2 + 3 u + \sqrt{-u (3 u - 4)}}{4 u - 2 u^2}\right) \ln \left(\frac{2 
 u^2 - 3 u + \sqrt{-u (3 u - 4)}}{2 (u - 2) u}\right) $ } } \\ 
 \text{ { \footnotesize $ - \ln \left(\frac{-u + \sqrt{(4-3 u) u} + 2}{2 (u - 
 1)^2}\right) \ln \left(\frac{2 u^2 - 3 u - \sqrt{-u (3u-4)}}{2(u-1)^2}\right) - $}} \\ 
 \text{ { \footnotesize $ \ln \left(\frac{-u - \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right) \ln \left(\frac{2 
 u^2 - 3 u + \sqrt{-u (3 u - 4)}}{2(u-1)^2}\right)$ } }
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* Setting $$w = \frac{-u + \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2} \ \ \ \text{and} \ \ \ z = \frac{-u - \sqrt{-u (3 u - 4)} + 2}{2 (u - 
 1)^2},$$ the desired result follows through an application of Euler's identity and then Roger's identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}. ◻
:::

::: lemma
[]{#previously10p4 label="previously10p4"} The equality of $$\begin{gathered}
 \operatorname{Li}_2(k) - \operatorname{Li}_2(k^2) 
 - \operatorname{Li}_2\left(\frac{-2k^2 + k - \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}\right) - \\ 
 \operatorname{Li}_2\left(\frac{-2k^2 + k + \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}\right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
\frac{1}{2} \ln^2\left(\frac{-2}{-\sqrt{-3k^2 + 2k + 1} + k + 1}\right) 
+ \frac{1}{2} \ln^2\left(\frac{-2}{\sqrt{-3k^2 + 2k + 1} + k + 1}\right)\\ 
- \frac{1}{3} \ln^2\left(1 - \frac{2}{\sqrt{-3k^2 + 2k + 1} - k + 1}\right)
- \frac{1}{3} \ln^2\left(\frac{2}{\sqrt{-3k^2 + 2k + 1} + k - 1} + 1\right) \\
+ \ln\left(\frac{\sqrt{-3k^2 + 2k + 1} - k + 1}{2 - 2k^2}\right) 
\ln\left(\frac{\sqrt{-3k^2 + 2k + 1} + k - 1}{2k^2 - 2}\right)\\
+ \frac{1}{2} \pi^2 + \frac{1}{6} \ln^2(1 - k) - \frac{1}{3} \ln(1 - k) \ln k - \frac{1}{3} \ln^2 k
\end{gathered}$$ holds for complex $k$.
:::

::: proof
*Proof.* This follows from the application of Roger's identity to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, with $$w=\left(\frac{-u + 
 \sqrt{(4 - 3u)u} + 2}{2}\right) \ \ \ 
 \text{and} \ \ \ 
 z=\left(\frac{-u - \sqrt{(4 - 3u)u} + 2}{2}\right),$$ and by enforcing the substituion $u=1-k$. ◻
:::

::: lemma
[]{#previously10p5 label="previously10p5"} The equality of $$\begin{gathered}
 - \operatorname{Li}_2 \left( (u - 1) u \right) 
 + \operatorname{Li}_2 \left( \frac{-u^3 + 5u^2 + \sqrt{u(4 - 3u)} (u^2 - u - 1) - 5u}{2(u - 1)^2} \right) 
 - \operatorname{Li}_2 \left( \frac{u}{u - 1} \right)\\ 
 + \operatorname{Li}_2 \left( \frac{-u^3 + 5u^2 - \sqrt{u(4 - 3u)} (u^2 - u - 1) - 5u}{2(u - 1)^2} \right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
 - \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{u(4 - 3u)}}{2(u - 1)} \right)\\ 
 + \ln \left( \frac{-u + \sqrt{-u(3u - 4)} + 2}{2(u - 1)^2} \right) 
 \ln \left( \frac{-(u + \sqrt{-u(3u - 4)} - 2)}{2(u - 1)^2} \right) 
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* This follows form the application of Abel's five-term identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} where $w = \frac{-u + \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2}, z = \frac{-u - \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2}$. ◻
:::

# Derivation of the Loxton--Lewin $\frac{\pi}{9}$-identities

In this section, we derive an elementary proof to the trio of three and four-term Loxton-Lewin dilogarithm $\frac{\pi}{9}$-identities. For reference, the three-term is identity given by, where $h = \frac{1}{2} \sec\left(\frac{\pi}{9}\right)$: $$\begin{aligned}
 \left( \operatorname{Li}_2(h) + \frac{1}{2} \ln(h) \ln(1 - h) \right) 
 + \left( \operatorname{Li}_2(h^2) + \frac{1}{2} \ln(h^2) \ln(1 - h^2) \right) - \\ 
 \frac{1}{3} \left( \operatorname{Li}_2(h^3) + \frac{1}{2} \ln(h^3) \ln(1 - h^3) \right)=7\pi^2/54, 
\end{aligned}$$ Using the latter identity in Theorem [\[previously8p1\]](#previously8p1){reference-type="ref" reference="previously8p1"} and applying the Euler reflection identity in [\[Eulerreflectionidentity\]](#Eulerreflectionidentity){reference-type="eqref" reference="Eulerreflectionidentity"} and then letting $u=1-k$, we have to show that the expression below yields the sought three-term relation in terms of $h$: $$\begin{gathered}
 - \operatorname{Li}_2\left(\frac{2 k^2 - k - \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right) - \\ 
 \operatorname{Li}_2\left(\frac{2 k^2 - k + \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right) 
 - \operatorname{Li}_2(1-k). 
\end{gathered}$$ We then set $$\begin{aligned}
\frac{\sqrt{-3 k^2 + 2 k + 1}}{2 k^2 - k - 1} = -i \sqrt{3}
\end{aligned}$$ This gives the polynomial $3 k^3 - 3 k^1 - 1 =0$, which has the solution: $k=\frac{-2}{\sqrt{3}} \sin\left(\frac{\pi}{9}\right)$.

With reference to the polylogarithm multiplication formula $$\label{previously11p4}
\begin{aligned}
 \sum_{m=0}^{p-1} \operatorname{Li}_s(z e^{2\pi i m/p}) = p^{1-s} \operatorname{Li}_s(z^p), 
\end{aligned}$$ we may obtain that $$\label{previously11p5}
\begin{aligned}
 -\operatorname{Li}_2(r) + \frac{1}{3} \operatorname{Li}_2(r^3) = 
 \operatorname{Li}_2\left(r e^{2\pi i / 3}\right)+\operatorname{Li}_2\left(r e^{4\pi i / 3}\right) 
\end{aligned}$$ So now we derive $r$, which is the radius/norm, given by: $$\frac{\sqrt{(2 k^2 - k - 1)^2 - (-3 k^2 + 2 k + 1)}}{2 k^2} = \sqrt{\frac{k - 1}{k}}=\frac{1}{h}$$ To prove this, make a substitution $3 (1/(1-x^2))^3 - 3 (1/(1-x^2))^1 - 1 =0$. Here, $k= (1/(1-x^2))$ This factors as $(x^3 - 3 x - 1) (x^3 - 3 x + 1) = 0$. We choose the polynomial $(x^3 - 3 x - 1)$, which has a root $1.87...$ which is $1/h$. Using the dilogarithm relation in [\[sigmasumLi\]](#sigmasumLi){reference-type="eqref" reference="sigmasumLi"}, we find that $$\label{previously11p7}
 - \operatorname{Li}_2\left(\frac{2 k^2 - k- \sqrt{-3 k^2 + 2 k + 1} + 1}{2 k^2}\right) 
 - \operatorname{Li}_2\left(\frac{2 k^2 - k + \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right)$$ reduces to $$-\frac{1}{3} \operatorname{Li}_2(h^{-3}) + \operatorname{Li}_2(h^{-1}).$$ We then use the Landen identity in [\[Landenformula\]](#Landenformula){reference-type="eqref" reference="Landenformula"}, with $\operatorname{Li}_2(1-k)$. By inspection, $\frac{k-1}{k} = h^{-2}$, which is the squared term of the ladder, completing the proof, in so far that we have proven the existence of the identity. Additional simplifications of log terms are required to bring it to the familiar form. This is done in the second proof below.

## Derivation of the Loxton-Lewin four-term $\frac{\pi}{9}$-identities

To derive a four-term dilogarithm involving $2\cos\big(\frac{4\pi}{9}\big)$ as the base, we apply Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} and set $$\frac{\sqrt{u (4-3u)}}{2 u^2 - 3 u} = i \sqrt{3}.$$ This has the solution $u=1 - \frac{2}{\sqrt{3}} \sin\left(\frac{4\pi}{9}\right)$ within the unit circle, so Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} can be applied. The radius, in this case, is $r=\sqrt{\frac{u}{u - 1}} = 2\cos\left(\frac{4\pi}{9}\right)$. Consequently, we obtain that $$\frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{(4 - 3 u) u}}{2 (u-1)} \right) 
 - \operatorname{Li_2} (r^2) = \operatorname{Li}_2 (-r) - \frac{1}{3} \operatorname{Li}_2 (-r^3).$$ For the logarithm on the left-hand side, split it into the complex and real parts. (Note that because $u=-.137...$ is negative that $\sqrt{(4 - 3 u)u}$ is a complex number.) Also note that $\sqrt{1 - \left( \frac{2(u - 1) - u}{2(u - 1)} \right)^2} = \sqrt{1 - 
 \left(\frac{(u - 2)}{2 (u - 1)}\right)^2} = \pm \frac{\sqrt{3u^2 - 4u}}{2(u - 1)}$, so therefore given the constraints that it is a primitive root of unity. Performing the same process as in [\[previously11p4\]](#previously11p4){reference-type="eqref" reference="previously11p4"}, we observe that $\frac{(u - 2)}{2 (u - 1)}$ is a root of $8 x^3 - 6 x - 
 1=0$, or exactly $\cos(\frac{\pi}{9})$. So we have $3/2 \ln^2(e^{-i\frac{\pi}{9}})$ (the negative $-\pi i/9$ sign arises because we choose the positive value of $\pm \frac{\sqrt{3u^2 - 4u}}{2(u - 1)}$ , as $u-1$ is negative), which gives the sought $-\pi^2/54$ value. Using the duplication formula for $\operatorname{Li_2}$ and elementary manipulations, we obtain the desired final form.

Mappings of the form $\frac{u}{u-1} \mapsto \frac{a+bx}{cx+d}$ provide all possible solutions that satisfy $(x^3 - 3 x - 1) (x^3 - 
 3 x + 1) = 0$. For our purposes, we only require that the ladder is composed of roots of the above polynomial, provided valid solutions are chosen for Roger's identity, as not all will be applicable. For the third identity, the solution $2\cos\big(4\frac{\pi}{9} \big)$ is chosen. It just so happens the solutions are trigonometric values.

Lewin and Loxton sought an analytic proof to the third and most difficult of the $\frac{\pi}{9}$-identities. It appears that the above proof is the closest proof for this identity in terms of being closest to a purely analytic proof. In contrast, a proof due to Kirillov [@Kirillov1995] relies on the assembly of the identity from various relations of trigonometric components and elementary dilogarithm identities, whereas the radius method sidesteps this assembly process.

To derive the second four-term ladder that involves $\frac{1}{2} \sec(\frac{2\pi}{9})$, we again apply the latter identity in Theorem [\[previously8p1\]](#previously8p1){reference-type="ref" reference="previously8p1"} and applying the Euler reflection identity, and we again set $u = 1 -k$, but now we set $$\begin{aligned}
\frac{\sqrt{-3 k^2 + 2 k + 1}}{2 k^2 - k - 1} = i \sqrt{3}. 
\end{aligned}$$ The solution $k=\frac{-2}{\sqrt{3}} \sin\left(\frac{2\pi}{9}\right)$ and the radius is $r=1+\frac{1}{2} \sec\left(\frac{\pi}{9}\right)$. We can show that $\frac{1}{r} = \frac{1}{2} \sec\left(\frac{2\pi}{9}\right)$, by mimicking the derivation of [\[previously11p5\]](#previously11p5){reference-type="eqref" reference="previously11p5"}, and by changing the sign from $h$ to $-h$, completes the proof. By analogy with the reduction of [\[previously11p7\]](#previously11p7){reference-type="eqref" reference="previously11p7"}, the additional transformation $\operatorname{Li_2}(z) + \operatorname{Li_2}(-z)=1/2\operatorname{Li_2}(z^2)$ is needed to convert it to the four-term ladder form.

Alternatively, all three can be proven at once with Roger's five-term identity, with the following substitutions, which are chosen in such a way that Landen's identity can be applied: $$n = \frac{\sqrt{-3a^2 + 2a + 1} + a + 1}{2a},z = -\frac{n}{(n - 1)^2}, \quad w = n - n^2.$$ Written out, this the equality of the three-term dilogarithm combination $$\begin{gathered}
 - \operatorname{Li}_2 \left( \frac{a}{a - 1} \right) 
 - \operatorname{Li}_2 \left( \frac{2a^2 - a - \sqrt{-3a^2 + 2a + 1} - 1}{2a^2} \right) \\ 
 - \operatorname{Li}_2 \left( \frac{2a^2 - a + \sqrt{2a - 3a^2 + 1} - 1}{2a^2} \right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
 \frac{\pi^2}{6} 
 + \frac{1}{2} \ln^2 \left( \frac{-2a^2 + \sqrt{-3a^2 + 2a + 1} + a + 1}{2(a - 1)a} \right) + \\ 
 \frac{3}{2} \ln^2 \left( 1 - \frac{\sqrt{-3a^2 + 2a + 1} + a + 1}{2a} \right). 
\end{gathered}$$ By setting $$\frac{\sqrt{(2 - 3a)a + 1}}{a(2a - 1) - 1} = \pm\sqrt{3}i,$$ we obtain the radius $\sqrt{\frac{a - 1}{a}}$.

A third proof relies on the application of Hill's five-term identity $$\operatorname{Li}_2(zw) - \operatorname{Li}_2(w) - \operatorname{Li}_2(z) - \operatorname{Li}_2\left(\frac{z(w - 1)}{1 - z}\right) - \operatorname{Li}_2\left(\frac{w(z - 1)}{1 - w}\right) - \frac{1}{2} \ln^2\left(\frac{1 - w}{1 - z}\right) = 0$$ Letting $w=r e^{\frac{2\pi i}{3}},z=r e^{\frac{4\pi i}{3}}$ or $w=r e^{\frac{\pi i}{3}},z=r e^{\frac{5\pi i}{3}}$.

After simplifying, note: $\frac{r (r^2 + 4r + 1)}{2 (r^2 + r + 1)} \pm \frac{i \sqrt{3} \, r (r^2 - 1)}{2 (r^2 + r + 1)}$. So, we need to solve $$\frac{r (r^2 + 4r + 1)}{2 (r^2 + r + 1)} = \frac{1}{2}$$

The solutions are $r=\frac{1}{2} \sec\left(\frac{\pi}{9}\right), \quad \frac{-1}{2} \sec\left(\frac{2\pi}{9}\right), \quad 
 \frac{-1}{2} \sec\left(\frac{4\pi}{9}\right)$. Then we use [\[previously7p5\]](#previously7p5){reference-type="eqref" reference="previously7p5"} to find the closed-form value of the real part, which when combined with additional simplifications, thus gives the value of $k$ and proving the identities, using [\[previously11p5\]](#previously11p5){reference-type="eqref" reference="previously11p5"}. Note: $\frac{1}{2} \sec\left(\frac{4\pi}{9}\right)$ will not work, as it is outside of the convergence.

Observe that the latter two proofs use five-term identities once, whereas the first proof uses the cubic integral. As a consequence of the connection between the integral, the hypergeometric series, and the dilogarithm identity, we also have that $$\cos\left(\frac{\pi}{9}\right) \sum_{n=0}^{\infty} \left( \frac{-8\cos\left(\frac{\pi}{9}\right)}{9} \right)^n 
 \frac{ \left( \frac{3}{2} \right)_n (1)_n^2 }{ \left( \frac{5}{3} \right)_n \left( \frac{4}{3} \right)_n 
 (2)_n } = \ln^2\left(2 \cos\left(\frac{4\pi}{9}\right)\right) - \frac{\pi^2}{27}$$ The $2\cos(\frac{4\pi}{9})$ identity is regarded as the most difficult of the three. In this case, this identity is the easiest, as it requires the least simplification of log terms due to $u$ lying within the unit circle, so Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} can be immediately used.
