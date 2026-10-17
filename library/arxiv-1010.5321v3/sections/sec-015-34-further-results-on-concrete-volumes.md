---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-015-34-further-results-on-concrete-volumes
section_title: "Further results on concrete volumes"
section_number: 3.4
pages: 14-16
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.517
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
Here we mention some important results from the last few decades, which are calculate hyperbolic volumes. To investigate it we can see immediately that our formula on orthosceme has very simple building up. In this section the great latin letters mean the measures of the dihedral angles at the edges denoted by the corresponding small ones.

::: theorem
Opposite dihedral angles of ideal tetrahedron are equal to each other, $A+B+C=\pi$ and its volume $v$ is $$v=\Lambda (A)+\Lambda (B)+\Lambda (C),$$ where $\Lambda (x)=-\int \limits_{0}^x\ln|2\sin \zeta|{\mathrm d\zeta}$.
:::

::: theorem
Let $R$ be a Lambert cube with essential angles $w_k$, $0 \leq w_k \leq \frac{\pi}{2}, k = 0, 1, 2$. Then the volume $V(R)$ of $R$ is given by $$V(R)=\frac{1}{4}\left\{\sum\limits_0^2(\Lambda(w_i+\theta)-\Lambda(w_i-\theta))- \Lambda(2\theta)+2\Lambda\left(\frac{\pi}{2}-\theta\right)\right\}$$ with $$0<\theta=\tan ^{-1}\frac{\sqrt{\cosh^2V_1-\sin^2w_0\sin^2w_2}}{\cos w_0\cos w_2}\leq \frac{\pi}{2}.$$
:::

::: theorem
Let $O$ be an ideal symmetric octahedron with all vertices on the infinity. Then $C=\pi-A$, $D=\pi-B$, $F=\pi-E$ and the volume of $O$ is: $$v=2\left(\Lambda \left(\frac{\pi+A+B+E}{2}\right)+\Lambda \left(\frac{\pi-A-B+E}{2}\right)+\Lambda \left(\frac{\pi+A-B-E}{2}\right)+\right.$$ $$\left.+\Lambda \left(\frac{\pi-A+B-E}{2}\right)\right).$$
:::

::: theorem
The volume of the hyperbolic tetrahedron T = T (A,B,C,D,E,F) is equal to $$Vol(T) = \frac{-1}{4}\int\limits^{z_2}_{z_1}\log\frac{\cos\frac{ A+B+C+z}{2}\cos\frac{ A+E+F+z}{2}\cos\frac{B+D+F+z}{2}\cos\frac{C+D+E+z}{2}} {\sin\frac{A+B+D+E+z}{2}\sin\frac{A+C+D+F+z}{2}\sin\frac{ B+C+E+F+z}{2}\sin \frac{z}{2}}\mathrm{dz},$$ where $z_1$ and $z_2$ are the roots of the integrand, given by $$z_1 = \tan^{-1}\frac{ k_2}{k_1}-\tan^{-1}\frac{ k_4}{k_3} \mbox{ , } z_2 = \tan^{-1}\frac{ k_2}{k_1}+\tan^{-1}\frac{ k_4}{k_3}
,$$ with $$k_1 = -(\cos S + \cos (A + D) + \cos (B + E) + \cos (C + F) + \cos (D + E + F)
+$$ $$\cos(D + B + C)+
+ \cos(A + E + C) + \cos(A + B + F)),$$ $$k_2 = \sin S + \sin (A + D) + \sin (B + E) + \sin (C + F) + \sin (D + E + F) +$$ $$\sin (D + B + C)+ \sin (A + E + C) + \sin (A + B + F),$$ $$k_3 = 2(\sin A\sin D + \sin B \sin E + \sin C \sin F),$$ $$k_4 =\sqrt{k^2_1 + k_2^2- k_3^2},$$ and $S = A + B + C + D + E + F$.
:::

The above theorem implies the theorem of Murakami and Yano:

::: theorem
The volume of the simplex $T$ is $$v=\frac{1}{2}\Im \left(U(z_1,T)-U(z_2,T)\right),$$ where $$U(z,T)=\frac{1}{2}(l(z)+l(A+B+D+E+z)+l(A+C+D+F+z)+l(B+C+E++F+z)-$$ $$-l(\pi+A+B+C+z)-l(\pi+A+E+F+z)-l(\pi+B+D+F+z)-l(\pi+C+D+E+z),$$ and $l(z)=\mathrm{Li}_2(e^{iz})$ by the Dilogarithm function $$\mathrm{Li}_2(z)=-\int\limits_0^x\frac{\log (1-t)}{t}\mathrm{dt}.$$
:::

Here I mention the theorem of Y.Cho and H. Kim described the volume of a tetrahedron using Lobachevsky function, too. It is also very complicated formula the reader can find it in [@cho].
