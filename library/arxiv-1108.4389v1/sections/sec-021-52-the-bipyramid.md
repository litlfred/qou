---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-021-52-the-bipyramid
section_title: "The bipyramid"
section_number: 5.2
pages: 44-45
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.99
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
To find the moduli space for the bipyramid theory, let us work in the equatorial polarization $\Pi_{\rm eq}$, as discussed in Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"} and Section [\[sec:gauge23\]](#sec:gauge23){reference-type="ref" reference="sec:gauge23"}. We closely follow the notation in those sections. We can start with the decomposition into two tetrahedra, and use the Lagrangian description [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"} of $T_{M,\Pi_{\rm eq}}$ as $N_f=1$ SQED, with a shift $V\to V-V_{X_1}/2$, to obtain a twisted superpotential

$$\widetilde\mathcal{W}(X_1,X_2;\sigma) = {\rm Li}_2(e^{\sigma})+{\rm Li}_2(e^{-\sigma+X_1})+\frac12\sigma^2+(X_2-i\pi)\sigma\,.$$

Here we have extended the symplectic transformation [\[gbip2\]](#gbip2){reference-type="eqref" reference="gbip2"} with an affine shift by $-i\pi$ for the twisted mass $X_2$. By requiring $\partial\widetilde\mathcal{W}/\partial\sigma =0$ (because $\sigma$ is the vev of a dynamical field), and setting $P_1=\partial\widetilde\mathcal{W}/\partial X_1$ and $\partial\widetilde\mathcal{W}/\partial X_2$, it is straightforward to derive the moduli space

$$\hspace{-.2in}\mathcal{M}_{\rm SUSY}^{(\rm param)}(T_{M,\Pi_{\rm eq}})\;: \quad\;\; p_1+\frac{p_2}{x_1}-1=0\,,\qquad p_2+\frac{p_1}{x_2}-1 = 0\,.
\label{SUSYbipeq}$$

This is the same as the Lagrangian $\mathcal{L}_M$ appearing in [\[Lbipeq\]](#Lbipeq){reference-type="eqref" reference="Lbipeq"}. An easier way to derive [\[SUSYbipeq\]](#SUSYbipeq){reference-type="eqref" reference="SUSYbipeq"} would be to begin with the product of moduli spaces for two tetrahedra

$$r''+r^{-1}-1=0\,,\qquad s'+s''^{-1}-1=0\,,$$

and simply apply the affine $Sp(4,{\mathbb Z})$ transformation $r\to\frac{x_1}{p_2},\, r''\to p_1,\, s_2\to p_2,\, s_1\to-\frac{p_1}{x_2p_2}$ .

Equivalently, we can take the decomposition of the bipyramid into three tetrahedra, and the corresponding XYZ model. The twisted superpotential corresponding to the Lagrangian [\[XYZbip\]](#XYZbip){reference-type="eqref" reference="XYZbip"} is

$$\widetilde\mathcal{W}_{\rm eff}(X_1,X_2,C) = {\rm Li}_2(e^{-X_1})+{\rm Li}_2(e^{-X_2})+{\rm Li}_2(e^{C-X_1-X_2})+i\pi(X_1+X_2-C)\,.$$

Note that, according to the shifts in the symplectic transformation [\[Spbip3\]](#Spbip3){reference-type="eqref" reference="Spbip3"}, we have turned on a half-integral theta angle for the combination $\Sigma_{X_1}+\Sigma_{X_2}-\Sigma_C$. Setting $P_1=\partial\widetilde\mathcal{W}/\partial X_1,\,P_2=\partial\widetilde\mathcal{W}/\partial X_2,\, \Gamma=\partial\widetilde\mathcal{W}/\partial C$ and exponentiating, we find equations

$$\gamma p_1+\frac1{x_1}-1=0\,,\qquad \gamma p_2+\frac{1}{x_2}-1=0\,,\qquad -\frac{\gamma x_1x_2}{c}+\frac{x_1x_2}{c}-1=0\,. \label{preL3}$$

Now, however, the (ordinary) cubic superpotential of the XYZ model tells us that we must set the twisted mass $C=0$ (modulo $2\pi i$), or $c=e^C=1$. By appending this to equations [\[preL3\]](#preL3){reference-type="eqref" reference="preL3"} and eliminating $\gamma$, we then obtain

$$(x_1-1)\Big(p_1+\frac{p_2}{x_1}-1\Big)=0\,,\qquad (x_2-1)\Big(p_2+\frac{p_1}{x_2}-1\Big)=0\,. \label{SUSYbipeq3}$$

These are equivalent to [\[SUSYbipeq\]](#SUSYbipeq){reference-type="eqref" reference="SUSYbipeq"} as long as $x_1\neq 1$ and $x_2\neq 1$. We recall, however, that $x_{1,2}=1$ (or $X_{1,2}=0$) are precisely the analogues of the singular points in moduli space discussed below [\[Aone\]](#Aone){reference-type="eqref" reference="Aone"}. There, either supersymmetry is broken or new Higgs branches of dynamical vacua open up. Away from this singular locus, equations [\[SUSYbipeq3\]](#SUSYbipeq3){reference-type="eqref" reference="SUSYbipeq3"} reduce to [\[SUSYbipeq\]](#SUSYbipeq){reference-type="eqref" reference="SUSYbipeq"}.
