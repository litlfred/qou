---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-009-42-dirichlet-character
section_title: "Dirichlet character"
section_number: 4.2
pages: 9-10
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 0.98
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
The simplest example of a number field with a single complex place is an imaginary-quadratic field ${\bf Q}(\sqrt{-d})$, where $d$ is a square-free positive integer. When $d\equiv3$ (mod 4), the discriminant is $D=-d$; otherwise it is $D=-4d$.

It is proven in [@Berndt] that $$\frac{\zeta_K(2)}{\zeta(2)}=\sum_{n>0}\frac{\chi_K(n)}{n^2}\label{chi}$$ where $\chi_K$ is the real Dirichlet character of the group of units of the field ${\bf Z}/|D|$ and $D$ is the discriminant of the imaginary-quadratic field $K$. The Dirichlet character is related to the Jacobi (or Kronecker) symbol by $$\chi_K(n)=\left(\frac{D}{n}\right)\label{Jacobi}$$ which vanishes if ${\rm gcd}(D,n)>1$. When $D$ is odd, one may use the alternative form $\left(\frac{n}{|D|}\right)$.

Using ([\[chi\]](#chi){reference-type="ref" reference="chi"}) in ([\[ZK\]](#ZK){reference-type="ref" reference="ZK"}), at $n=2$, one happily disposes of powers of $\pi$. We dispose of $\sqrt{-D}$, by using the imaginary-quadratic result [@Berndt] $$\sum_{n>0}\frac{\chi_K(n)}{n^2}=
\frac{1}{\sqrt{-D}}\sum_{-D>k>0}\chi_K(k)
{\rm Cl}_2\left(\frac{2\pi k}{|D|}\right)\label{chik}$$ which yields a finite sum over the elements of the group of units. Finally, we dispose of a factor 2, via the reflection relations $\chi_K(k)=-\chi_K(|D|-k)$ and ${\rm Cl}_2(\theta)=-{\rm Cl}_2(2\pi-\theta)$, to obtain the readily computable result $$Z_K=Z_{|D|}:=D\sum_{-D>2k>0}\left(\frac{D}{k}\right)
{\rm Cl}_2\left(\frac{2\pi k}{D}\right)\label{ZKq}$$ with the magnitude of the discriminant identifying the imaginary-quadratic field.

Thanks to David Bailey [@TRANSMP], it is now a routine matter to evaluate ([\[ZKq\]](#ZKq){reference-type="ref" reference="ZKq"}) to high precision[^1], using [@Lewin] $$\frac{{\rm Cl}_2(\theta)}{\theta}
=1-\df12\log(\theta^2) +\sum_{n=1}^\infty\frac{\zeta(2n)}{2n^2+n}
\left(\frac{\theta}{2\pi}\right)^{2n}
\label{cl2}$$ which converges faster than $1/9^n$, for $\theta\in[0,2\pi/3]$. An angle in $[2\pi/3,\pi]$ may be transformed to a pair in $[0,2\pi/3]$, by rearrangement of the duplication formula $$\df12{\rm Cl}_2(2\theta)={\rm Cl}_2(\theta)-{\rm Cl}_2(\pi-\theta)
\label{dub}$$ Rather than compute $\zeta(2n)/(2\pi)^{2n}
=\frac12|B_{2n}|/(2n)!$ recursively, from the Bernoulli numbers, we used a FFT program written by David Bailey to evaluate $\{\zeta(2n)\mid 0\le n<2^{m}\}$, in one fell swoop, by a multi-dimensional generalization of Newton's method. With $m=11$, the initial outlay, to tabulate 2048 coefficients to 1800 digits, was 8 minutes; then 1800 good digits of any Clausen value in $\{{\rm Cl}_2(\theta)\mid 0<\theta<2\pi/3\}$ are obtainable in less than 2 seconds on a 533MHz machine. Low-precision results for $Z_{|D|}$ are given in Table 19.

It follows from ([\[ZKq\]](#ZKq){reference-type="ref" reference="ZKq"}) that every discovery of a rational Dedekind-zeta invariant for a quadratic link gives a relation between a set of Clausen values at angles whose tangents involve $\sqrt d$, and a set of Clausen values at angles which are multiples of $2\pi/|D|$. We have already seen this, rather strikingly, in the case $-D=d=7$ of ([\[todo\]](#todo){reference-type="ref" reference="todo"}), where the hyperbolic 6-crossing 3-component link[^2] $6^3_1$ mediates between Clausen values, and hence the Bloch--Wigner dilogarithms of ([\[modern\]](#modern){reference-type="ref" reference="modern"}), with very different types of argument on the left and right.

We now address the question: which links have volumes that link Clausen values?

[^1]: ` http://science.nas.nasa.gov/Groups/AAA/db.webpage/mpdist/mpdist.html`

[^2]: We use the notation of [@Rolfsen], whose appendix give drawings of links up to 9 crossings.
