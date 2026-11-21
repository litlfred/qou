---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-017-91-derivation-of-the-loxton-lewin-four-term-frac
section_title: "Derivation of the Loxton-Lewin four-term $\frac{\pi}{9}$-identities"
section_number: 9.1
pages: 27-29
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
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
