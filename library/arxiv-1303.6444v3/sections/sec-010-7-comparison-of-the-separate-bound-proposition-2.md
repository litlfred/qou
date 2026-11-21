---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-010-7-comparison-of-the-separate-bound-proposition-2
section_title: "Comparison of the Separate Bound: Proposition 2.4"
section_number: 7
pages: 12-13
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.974
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
[]{#sec: comparison label="sec: comparison"} This approach would be better for potentials where $\zeta R(\beta) < C(\beta)$, for some $\zeta$ representing the quotient of the coefficients $\frac{f_1}{f_2}$, where: $$\begin{aligned}
 f_1&:=e^{-4\beta B}\frac{\left(W\left(\frac{e}{1+e^{2\beta B}}\right)-1\right)^2}{W\left(\frac{e}{1+e^{2\beta B}}\right)} \label{f1} \\
f_2&:=\frac{\left(W\left(\frac{e^{\beta B+1}}{1+e^{\beta B}}\right)-1\right)^2}{W\left(\frac{e^{\beta B+1}}{1+e^{\beta B}}\right)} \label{f2}
\end{aligned}$$ $f_2$ is actually smaller than $f_1$, as detailed in Figure [1](#fig:quotient){reference-type="ref" reference="fig:quotient"}. This would only be an improvement if the $R(\beta)$ factor compensates. In the case of a hard-core contribution, both $R(\beta)$ and $C(\beta)$ are the same, and so are the $f_i$ factors. The use of the integrand $\beta |U(y)|$ rather than $|e^{-\beta U(y)}-1|$ is better for potentials with attractive parts. For $\beta=0$, the coefficients $f_1$ and $f_2$ are precisely the same.

The comparison between the optimised bound in [\[f1\]](#f1){reference-type="eqref" reference="f1"} and the bound achieved from these different cluster coefficient bounds based on tree graph identities ($f_2$) is shown in Figure [1](#fig:quotient){reference-type="ref" reference="fig:quotient"}. This gives us that as soon as $1.6 R(\beta) < C(\beta)$ this other version of bounds is better. This is due to the fact that $$\frac{C(\beta)}{R(\beta)}> 1.6> \frac{f_1}{f_2} \label{compare2}$$ and so $$f_2 R(\beta)^{-1} > f_1 C(\beta)^{-1}$$

We also note that $R(\beta)$ should be a better bound, for large $\beta$ or small temperature, since it is linear in $\beta$, whereas $C(\beta)$ is exponential in $\beta$ and that this $\zeta(\beta)$ could be understood better to explore the comparison of these two bounds. It also only depends on the potential $\Phi$ through the stability parameter $B$.

![Quotient $\frac{f_1}{f_2}$ [\[compare2\]](#compare2){reference-type="eqref" reference="compare2"} of the Optimised Penrose-Lebowitz Bound ($f_1$) [\[f1\]](#f1){reference-type="eqref" reference="f1"} over the New Bound ($f_2$) [\[f2\]](#f2){reference-type="eqref" reference="f2"} ](quotient.pdf){#fig:quotient}
