---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-009-31-formulas-of-j-bolyai
section_title: "Formulas of J. Bolyai"
section_number: 3.1
pages: 6-8
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.967
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
In this section $k$ is a constant giving the curvature of the hyperbolic space and the value of our constant $v_n$ is $1$. The following formulas can be found in [@bolyai], [@bonola] and [@weszely]. Most of it can be easily determined using the results of the previous section. An important exception is the volume of the orthosceme, we will give a new formula for it in section 3.3.

Volume of the body determined by a disk of area p and the segments orthogonal to it with edge lengthes $t$, respectively:

$$v=\frac{1}{8}pk\left(e^{\frac{2q}{k}}-e^{-\frac{2q}{k}}\right) + \frac{1}{2}pq.$$

Volume of the sector of parallel half-lines intersecting orthogonally an paraspherical basic domain of area $p$: $$\frac{1}{2} pk.$$

Volume of the sphere of radious $x$:

$$\frac{1}{2}\pi k^3(e^{\frac{2x}{k}}-e^{\frac{-2x}{k}})-2\pi k^2x=\pi k^3\sinh\frac{2x}{k}-2\pi k^2x.$$

Volume of the set of those points of $\mathbb{H}^3$, which distances from a fixed segment $AB$ of length $p$ is not greater then $q$:

$$\frac{1}{4} \pi k^2p(e^{\frac{q}{k}}-e^{-\frac{q}{k}})^2.$$

Volume of a special tetrahedron. Two edges $a$ and $b$ are orthogonal to each other and a third one $c$ (skew with respect to $a$) is orthogonal to the plane of $a$ and $b$.

![Orthosceme](vol6.eps)

The dihedral angle at $a$ is $\alpha$, the angle opposite to $b$ of the triangle with edges $a$ and $b$ is $\beta$ and the angle opposite to the edge $c$ in the triangle with edges $c$ and $z$ is $\gamma$, respectively (see Fig.6). J.Bolyai gave two formulas:

$$v=\frac{\tan\gamma }{2\tan \beta}\int \limits_{0}^c\frac{z\sinh z}{\left(\frac{\cosh ^2z}{\cos ^2\alpha}-1\right)\sqrt{\frac{\cosh ^2z}{\cos ^2\gamma}-1}} {\mathrm dz},$$

and

$$v=\frac{1}{2}\int \limits_{0}^{\alpha}\left(-a+\frac{\sinh a\cos \phi}{2\sqrt{\tanh ^2b+\sinh ^2a\cos ^2\phi}\ln\frac{\cosh a\cos \phi +\sqrt{\tanh^2b+\sinh^2a\cos^2\phi}}{\cosh a\cos \phi -\sqrt{\tanh^2b+\sinh^2a\cos^2\phi}}}\right)
{\mathrm d\phi}$$

Volume of the orthosceme with ideal vertex (which is the common endpoint of the edges $a$, $x$ and $z$):

$$v=\frac{\sin 2\alpha}{4}\int \limits_{0}^c\frac{z}{\cosh ^2z-\cos^2\alpha} {\mathrm dz}$$

and

$$v=\frac{1}{2}\int \limits_{0}^a\ln\frac{\cos \phi}{\sqrt{\cos ^2\phi -\tanh ^2b}} {\mathrm d\phi}$$

Volume of a cone with a basic circle of radious $b$ and with half-angle $\beta$ at its apex.

$$v=\pi \int \limits_{0}^b\frac{\sinh ^2y}{\cosh y\sqrt{\frac{\cosh ^2y}{\cos ^2\beta}-1}} {\mathrm dy}.$$

The apex $B$ of a circular cone tends to an ideal point on its axis of rotation.

$$v=\pi \ln\cosh b.$$
