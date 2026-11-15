---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-006-24-coordinate-system-based-on-spherical-hyperbol
section_title: "Coordinate system based on spherical hyperbolic coordinates"
section_number: 2.4
pages: 5-6
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.919
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
![Spherical coordinates](vol4.eps)

From the hyperbolic orthogonal coordinates $x_1,x_2,\cdots, x_n$ we can get the spherical coordinates of a point $P$. Let the distance of $P=P_n$ from the origin is $r_n$ and denote by $\phi_i$ the angle between the $i^{th}$ coordinate axis and the segment $OP_{i+1}$ for $i=n-1,n-2,\cdots 1$. ( Here $P_{n-1}$ is the orthogonal projection of $P$ into the coordinate subspace of the axes $x_1, x_{n-2},x_n$, and so on\...) We have $$\sinh \frac{ x_{n-1}}{k}=\sinh \frac{ r_n}{k} \cos\phi_{n-1}$$ by the hyperbolic theorem of Sin. For general $i$, we get that $$\cosh \frac{ x_{n-1}}{k}\cdots \cosh \frac{x_{n-i+1}}{k}\sinh \frac {x_{n-i}}{k}=\sinh \frac{ r_n }{k}\sin\phi_{n-1}\cdots \sin\phi_{n-i+1}\cos\phi_{n-i},$$ and by the Pythagorean theorem we can get a last equation: $$\cosh \frac{ x_{n-1}}{k}\cdots \cosh \frac{x_{2}}{k}\sinh \frac{  x_{1}}{k}=\sinh \frac{ r_n }{k}\sin\phi_{n-1}\cdots \sin\phi_{2}\cos\phi_{1}.$$ Straightforward computation shows that:

$$v(D)=k^{n-1}\int\limits_{D} \left(\sinh\frac{r_n}{k}\right)^{n-1}\sin^{n-2}\phi_{n-1}\cdots \sin\phi_{2}
\mathrm{d}\phi_1\cdots \mathrm{d}\phi_{n-1}\mathrm{d}r_n.$$
