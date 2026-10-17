---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-005-24-the-polyanalytic-bergman-space-in-the-model-c
section_title: "The polyanalytic Bergman space in the model case of the unit disk with constant weight"
section_number: 2.4
pages: 4-4
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
For $q=1,2,3,\ldots$, we consider the spaces $\mathrm{PA}^2_q({\mathbb D}):=\mathrm{PA}^2_q({\mathbb D},\pi^{-1})$ where the domain is the unit disk ${\mathbb D}$ and the weight is $\omega(z)\equiv1/\pi$. The corresponding reproducing kernel $K_q$ was obtained Koshelev [@koselev]: $$K_q(z,w)=q\sum_{j=0}^{q-1}(-1)^j\binom{q}{j+1}\binom{q+j}{q}
\frac{(1-w\bar z)^{q-j-1}|z-w|^{2j}}{(1-z\bar w)^{q+j+1}}.
\label{eq-mcdisk1}$$ Its diagonal restriction is given by $$K_q(z,z)=\frac{q^2}{(1-|z|^2)^{2}}.$$ Based on [\[eq-mcdisk1\]](#eq-mcdisk1){reference-type="eqref" reference="eq-mcdisk1"}, the lift is $K_q$ is then easily calculated, $$\mathbf{E}_{\otimes2}[K_q](z,z';w,w')=
q\sum_{j=0}^{q-1}(-1)^j\binom{q}{j+1}\binom{q+j}{q}
\frac{(1-w'\bar z')^{q-j-1}(z-w')^j(\bar z'-\bar w)^{j}}{(1-z\bar w)^{q+j+1}}.$$ so that $$\begin{gathered}
\mathbf{E}_{\otimes2}[K_q](z,z';z,z')=
q\sum_{j=0}^{q-1}\binom{q}{j+1}\binom{q+j}{q}
\frac{(1-|z'|^2)^{q-j-1}|z-z'|^{2j}}{(1-|z|^2)^{q+j+1}}
\\
=q(1-|z|^2)^{-2}\sum_{j=0}^{q-1}\binom{q}{j+1}\binom{q+j}{q}
\bigg(\frac{1-|z'|^2}{1-|z|^2}\bigg)^{q-j-1}\bigg(\frac{|z-z'|}{1-|z|^2}
\bigg)^{2j}.
\end{gathered}$$
