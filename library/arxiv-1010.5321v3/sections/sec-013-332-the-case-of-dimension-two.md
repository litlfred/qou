---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-013-332-the-case-of-dimension-two
section_title: "The case of dimension two"
section_number: 3.3.2
pages: 13-13
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.9
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
The following calculation shows that area of a rectangular triangle also can be get with our method. $$\int\limits_{0}^{a}\int\limits_{0}^{\phi(x)}(\cosh y)\mathrm{d}y\mathrm{d}x=\int\limits_{0}^{a}\frac{\frac{\tanh b}{\sinh a}\sinh x}{\sqrt{1-\left(\frac{\tanh b}{\sinh a}\sinh x\right)^2}}\mathrm{d}x=$$ $$=\frac{1}{2}\frac{\sinh a}{\tanh b}\int\limits_{0}^{(\tanh b)^2}\frac{1}{\sqrt{1+\left(\left(\frac{\sinh a}{\tanh b}\right)^2-1\right)t-\left(\frac{\sinh a}{\tanh b}\right)^2t^2}}\mathrm{d}t$$

At this point we can use the following result on antiderivative: if $y=ax^2+bx+c$ and $a<0$ then $\int\frac{1}{\sqrt{y}}\mathrm{d}t=\frac{1}{\sqrt{-a}} \sin^{-1}\frac{-y'}{\sqrt{b^2-4ac}}$. Thus the required area is: $$\frac{1}{2}\left[\sin^{-1}\frac{(2\sinh^2a)t-\sinh^2a+\tanh ^2b}{\sinh^2a+\tanh ^2b}\right]^{\tanh ^2b}_0=
\frac{1}{2}\left[\sin^{-1}(2\sin^2\beta\sinh^2a-\cos2\beta)- \sin^{-1}(-\cos2\beta)\right].$$ Using now the equalities $\sin \beta=\frac{\sinh b}{\sinh c}$, $\sin\alpha=\frac{\sinh a}{\sinh c}$ we get that $\frac{-\sinh^2a+\tanh ^2b}{\sinh^2a+\tanh ^2b}=-\cos(2\beta)$, $\frac{(2\sinh^2a)\tanh ^2b}{\sinh^2a+\tanh ^2b}=2\sin ^2\beta\sinh^2a=2\frac{\sinh ^2b}{\sinh ^2c}\sinh^2a$ and $1=\frac{\sinh ^2b\sinh^2a}{\sinh ^2c}+\frac{\sinh ^2b+\sinh^2a}{\sinh ^2c}$. Now our formula simplified into the form $$\frac{1}{2}\left[\sin^{-1}(2-2\frac{\sinh ^2b+\sinh^2a}{\sinh ^2c}+\sin^2\beta-\cos^2\beta)+(\frac{\pi}{2}-2\beta)\right]=\pi-\left(\alpha +\beta +\frac{\pi}{2}\right),$$ as we stated.
