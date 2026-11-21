---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-003-22-the-chern-weil-homomorphism
section_title: "The Chern-Weil homomorphism"
section_number: 2.2
pages: 5-6
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.988
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let ${\mathfrak{g}}$ be a Lie algebra and ${\mathfrak{h}}\subset{\mathfrak{g}}$ be a subalgebra of ${\mathfrak{g}}$. Suppose that there is an ${\mathfrak{h}}$-equivariant projection $pr\,:\,{\mathfrak{g}}\mapsto {\mathfrak{h}}$, that is a map commuting with the adjoint action of ${\mathfrak{h}}$ and satisfying the property $\displaystyle pr\, |_{{\mathfrak{h}}} = Id_{{\mathfrak{h}}}\,.$ The amount by which $pr$ fails to be a Lie algebra homomorphism is measured by the "curvature" $C\in Hom(\wedge^2 {\mathfrak{g}}, {\mathfrak{h}})$ $$\label{curvature}
C(v,w)= [pr(v), pr(w)]- pr ([v,w])\,,
\qquad v,w \in {\mathfrak{g}}\,.$$

Given the "curvature" ([\[curvature\]](#curvature){reference-type="ref" reference="curvature"}) of the ${\mathfrak{h}}$-equivariant projection $pr$, it is not hard to see that for any adjoint invariant form $Q\in ((S^j{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ the formula $$\label{Ch-W}
\chi(Q)(v_1, \dots, v_{2j}) =
\frac1{(2j)!} \sum_{\nu\in S_{2j}}
(-)^{\nu} Q(C(v_{\nu(1)}, v_{\nu(2)}), \dots,
C(v_{\nu(2j-1)}, v_{\nu(2j)}))$$ defines a relative Lie algebra cocycle $\chi(Q)\in C^{2j}({\mathfrak{g}},{\mathfrak{h}})$. The standard argument of the theory of characteristic classes shows that the cohomology class $[\chi(Q)]$ of the cocycle $\chi(Q)$ does not depend on the choice of the projection $pr$. Thus ([\[Ch-W\]](#Ch-W){reference-type="ref" reference="Ch-W"}) induces a map from the vector space $((S^j{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ to $H^{2j}({\mathfrak{g}}, {\mathfrak{h}})$. The latter map is called the *Chern-Weil homomorphism*.

In our case we set ${\mathfrak{g}}={\mathfrak{gl}}_N({\cal W})$, ${\mathfrak{h}}={\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ and define the projection $pr$ from ${\mathfrak{g}}$ to ${\mathfrak{h}}$ by the formula $$\label{pr}
pr(v)= pr_0(v) + pr_2 (v)\,,$$ $$pr_0(v)= v\Big|_{y=0}\,, \qquad
pr_2(v)= \frac1{N}{\sigma}_2(tr (v)) I_{N}\,,$$ where ${\sigma}_2$ denotes the projection onto the monomials of the second degree in $y$'s, $tr$ is the ordinary matrix trace, $I_N$ is the identity matrix of size $N\times N$, and the Lie algebra ${\mathfrak{sp}}_{2n}$ is realized as a subalgebra of scalar matrices in ${\mathfrak{gl}}_N({\cal W})$ with values in quadratic monomials in ${\cal W}$ .

Due to [@FFS] we have the following

::: teo
The Lie algebra cocycle $\Theta^N_{2n}\in
C^{2n}({\mathfrak{g}},{\mathfrak{g}}^*)$ is relative with respect to the subalgebra ${\mathfrak{h}}={\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$. The evaluation of ([\[Te\]](#Te){reference-type="ref" reference="Te"}) on the identity matrix $I_N\in {\mathfrak{g}}$ gives a relative Lie algebra cocycle $${\varphi}\in C^{2n}({\mathfrak{g}}, {\mathfrak{h}})$$ $${\varphi}= \Theta^N_{2n}(\cdot ,\dots, \cdot, I_N)\,:\,
\wedge^{2n}({\mathfrak{g}}) \mapsto {\Bbb C}(({\hbar}))$$ whose cohomology class $$\label{FFS}
[{\varphi}\,]=[\chi (Q_n)]\,,$$ coincides with the image of the $n$-th component $Q_n\in ((S^n{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ of the adjoint invariant form $Q\in ((S{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ $$\label{Qn}
Q(X,\dots, X)= \det\Big( \frac{X_1/2{\hbar}}{sinh\,(X_1/2{\hbar})}
\Big)^{1/2} tr\, \exp\left(\frac{X_2}{{\hbar}}\right)\,,$$ $$X= X_1\oplus X_2 \in {\mathfrak{sp}}_{2n} \oplus {\mathfrak{gl}}_N$$ under the Chern-Weil homomorphism ([\[Ch-W\]](#Ch-W){reference-type="ref" reference="Ch-W"}).
:::
