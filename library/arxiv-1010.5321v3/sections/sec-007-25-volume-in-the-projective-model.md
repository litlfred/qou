---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-007-25-volume-in-the-projective-model
section_title: "Volume in the projective model"
section_number: 2.5
pages: 6-6
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.977
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
At the origin of the projective (Kayley-Clein) model we consider a Cartesian system of coordinates. Regarding the factor $k$ we assume that the radius of the sphere is $k$. The considered system is an orthogonal coordinate system both of the embedding Euclidean and the modeled hyperbolic space.

![Coordinates in the Cayley-Klein model](vol5.eps)

We connect the hyperbolic spherical coordinates and the euclidean spherical ones by the system of equations: $$r_n= k\tanh^{-1}\frac{R_n}{k}, \hspace{0,5cm}
\phi_i=\theta_i, \hspace{0,5cm} i=1,\cdots, n-1.$$ Since the Jacobian is $$\frac{1}{1-\left(\frac{R_n}{k}\right)^2},$$ and $$\left(\sinh \frac{ r_n}{k}\right)^{n-1}=\left(\sinh\left(\frac{1}{2}\ln\frac{1+\frac{R_n}{k}}{1-\frac{R_n}{k}} \right)\right)^{n-1} =\left(\frac{\frac{R_n}{k}}{\sqrt{1-\left(\frac{R_n}{k}\right)^2}}\right)^{n-1}$$ the volume is: $$v(D)=\int\limits_{D} \frac{ R_n^{n-1}}{\sqrt{1-\left(\frac{R_n}{k}\right)^2}^{n+1}}\sin^{n-2}\theta_{n-1}\cdots \sin\theta_{2}
\mathrm{d}\theta_1\cdots \mathrm{d}\theta_{n-1}\mathrm{d}R_n.$$ Transforming it into the usual Cartesian coordinates ($X_1,\cdots ,X_n$) the new formula is: $$v(D)=\int\limits_{D} \frac{ 1}{\left(1-\left(\sum\limits_{i=1}^{n}\left(\frac{X_i}{k}\right)^2\right)\right)^{\frac{n+1}{2}}} \mathrm{d}X_1\cdots \mathrm{d}X_{n-1}\mathrm{d}X_n.$$
