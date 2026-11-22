---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-034-52-volume
section_title: "Volume"
section_number: 5.2
pages: 32-33
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.8
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.vol label="sec.vol"}

By substituting a solution to [\[crit\]](#crit){reference-type="eqref" reference="crit"} back into the $\hbar^{-1}$ (leading order) part of the integrand, we obtain the following formula for the complex volume of a representation:

$$S_{\mathcal{T},0} = -\frac{\pi^2}{2}f\cdot \mathbf B^{-1}\nu
-i\pi Z\cdot\mathbf B^{-1}\nu+\frac1{2}Z\cdot\mathbf{B}^{-1}\mathbf A Z 
+\sum_i\widetilde{{\rm Li}}_2(e^{-Z_i}) \qquad \Big({\rm mod} \;\;\frac{\pi^2}{6}\Big)\,.$$

Some manipulation involving the flattening can be used to recast this as

$$\label{vol}
\boxed{ S_{\mathcal{T},0} = -\frac12 (Z-i\pi f)\cdot (Z''+i\pi f'')
+\sum_i\widetilde{\rm Li}_2(e^{-Z_i})} \qquad \Big({\rm mod} \;\;\frac{\pi^2}{6}\Big)\,,$$

where $Z_i'' := -\widetilde{\rm Li}_1(e^{-Z_i})$. It is straightforward to verify that this formula is independent of the choice of quad type, choice of edge of $\mathcal{T}$, choice of meridian loop, choice of flattening, and 2--3 moves defines a topological invariant, which agrees with the complex Chern-Simons invariant of $M$. Since the complex volume in this form has already been studied at length in the literature, we suppress the details here.

At the discrete faithful representation, we can remove the "tildes" from the logarithm and dilogarithm. If we consider the discrete faithful solution to $z^{\mathbf A}(1-z^{-1})^{\mathbf B}=(-1)^n$, and take standard logarithms $Z_i=\log z_i$, $Z_i''=\log(1-z_i^{-1})$ (with $0\leq {\rm Im}\,Z,\,{\rm Im}\,Z''\leq \pi$), we find

$$\begin{aligned}
S_{\mathcal{T},0} &= \,i({\rm Vol}(M)-i\,{\rm CS}(M)) \notag \\ &= 
-\frac12 (Z-i\pi f)\cdot (Z''+i\pi f'')+\sum_i{\rm Li}_2(e^{-Z_i}) 
\qquad \Big({\rm mod} \;\;\frac{\pi^2}{6}\Big)\,.
\end{aligned}$$

This is a version of the simple formula for the complex volume given in [@Neumann-combi]. It is known that the ambiguity in the volume can be lifted from $\pi^2/6$ to $2\pi^2$ using more refined methods [@N; @DuZi; @GoZi; @Zickert-rep].
