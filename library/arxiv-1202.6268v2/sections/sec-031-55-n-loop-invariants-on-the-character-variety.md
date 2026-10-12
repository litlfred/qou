---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-031-55-n-loop-invariants-on-the-character-variety
section_title: "n-loop invariants on the character variety"
section_number: 5.5
pages: 35-37
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.955
---
[]{#sec.uSIM label="sec.uSIM"}

Just as we extended the torsion formula to general representations $\rho\in X_M$ in Section [\[sec.extensions\]](#sec.extensions){reference-type="ref" reference="sec.extensions"}, we may now generalize the entire state integral. The basic result for the higher invariants $S_{\mathcal{T},n}$ is that their formulas remain completely unchanged. The shapes $z_i$ simply become functions of the representation $\rho$, and satisfy deformed gluing equations [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"}--[\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"}. One must also make sure to use a generalized flattening whenever it occurs, just as in Section [\[sec.extensions\]](#sec.extensions){reference-type="ref" reference="sec.extensions"}.

We note that, for a hyperbolic knot complement $M=S^3\backslash K$, the generalized Chern-Simons state integral $\mathcal{Z}_M(u;\hbar)$ is expected to match the asymptotic expansion of the colored Jones polynomials $J_N(K;q)$. Specifically, one should consider the limit

$$N\to \infty\,,\quad \hbar\to 0\,,\qquad q^N=e^{N\hbar}=e^{2u}\quad\text{fixed}\,,$$

where $m=e^u$ is the meridian eigenvalue for a geometric representation $\rho_m$ in the neighborhood of the discrete faithful. This is the full *Generalized Volume Conjecture* of [@Gu].

To see how formulas for the generalized invariants $S_{\mathcal{T},n}$, $n\geq 0$, come about, consider the state integral at general meridian eigenvalue $m=e^u$. From [\[appSIM\]](#appSIM){reference-type="eqref" reference="appSIM"} of Appendix [\[app.SIM\]](#app.SIM){reference-type="ref" reference="app.SIM"}, we find

$$\begin{aligned}
 \notag
\mathcal{Z}_\mathcal{T}(u;\hbar) 
&=  \sqrt{\frac{8\pi}{\hbar^3\det\mathbf B}}\int \frac{d^N\!Z}{(2\pi \hbar)^{N/2}} \, \prod_{i=1}^N \psi_\hbar(Z_i)\,e^{-\tfrac1{2\hbar}Z\cdot \mathbf B^{-1}\mathbf A Z}\\
 &\hspace{1in} \times
e^{\tfrac1\hbar\Big[
2 \bm u\cdot \mathbf D\mathbf B^{-1}\bm u+(2\pi i+\hbar)f\cdot 
\mathbf B^{-1}\bm u
+\tfrac12\big(i\pi+\tfrac\hbar2\big)^2 f\cdot \mathbf B^{-1} \nu
- Z\cdot\mathbf B^{-1}\big(2\bm u+\big(i\pi+\tfrac\hbar2\big)\nu\big)\Big]}    \,,
 \label{uSIM}
\end{aligned}$$

where $\bm u:=(0,...,0,u)$ and $\mathbf D$ is the block appearing in any completion of the Neumann-Zagier matrices $(\mathbf A\;\mathbf B)$ to $\left(\begin{smallmatrix}\mathbf A&\mathbf B\\\mathbf C&\mathbf D\end{smallmatrix}\right)\in Sp(2N,\mathbb{Q})$, such that the bottom row $D$ of $\mathbf D$ appears in the longitude gluing equation $C\cdot Z+D\cdot Z''=v+2\pi i\nu_\lambda$ (Section [\[sec.uflat\]](#sec.uflat){reference-type="ref" reference="sec.uflat"}). Indeed, since we are contracting with $\bm u$, only this bottom row of $\mathbf D$ really matters in [\[uSIM\]](#uSIM){reference-type="eqref" reference="uSIM"}.

The critical points of the state integral are now given by

$$\label{ucrit} \mathbf A Z+\mathbf B Z''=2\bm u+i\pi\nu\,,$$

with $Z'':=-\widetilde{\rm Li}_1(e^{-Z})$. As expected, this is the logarithmic form of the deformed gluing equation [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"}. Thus, all critical points correspond to representations $\rho=\rho_m\in X_M$. The multivalued nature of this equation must be carefully studied to make sure desired solutions actually exist. However, for example, representations on the geometric component $X_M^{\rm geom}$ always exist in a neighborhood of the discrete faithful representation, if we choose $u=\log m$ to be close to zero (and use a regular triangulation).

We then start expanding the state integral around a critical point, setting

$$\mathcal{Z}_{\mathcal{T}}(u;\hbar) \sim \hbar^{-\frac32}\exp\Big[\frac1\hbar S_{\mathcal{T},0}(u)+S_{\mathcal{T},1}(u)+\hbar S_{\mathcal{T},2}(m)+\hbar^2 S_{\mathcal{T},3}(m)+...\Big]\,.$$

The leading contribution $S_{\mathcal{T},0}(\rho)$ is given, following some standard manipulations using the generalized flattening, by

$$\label{S0u}
S_{\mathcal{T},0}(u) =   u\,v(u)-\frac12 (Z-i\pi f)\cdot (Z''+i\pi f'') 
+ \sum_{i=1}^N\widetilde{\rm Li}_2(e^{-Z})\qquad \Big(\text{mod}\;\frac{\pi^2}{6}\Big)\,.$$

Here we write $S_{\mathcal{T},0}$ as a function of the logarithmic meridian eigenvalue $u$, though a fixed choice of representation $\rho$ will implicitly fix the choice of longitude eigenvalue $v=\log(-\ell)$ as well. Expression [\[S0u\]](#S0u){reference-type="eqref" reference="S0u"} is a holomorphic version of the complex volume of a cusped manifold with deformed cusp. Explicitly,

$$S_{\mathcal{T},0}(u) = i({\rm Vol}_M(u)+i{\rm CS}_M(u)) -2v\,\Re(u)\,.$$

This is the correct form of the complex volume to use in the Generalized Volume Conjecture, *cf.* [@GuM].

At first subleading order, we re-derive the generalized torsion formula. The calculation is identical to that of Section [\[sec.torsion2\]](#sec.torsion2){reference-type="ref" reference="sec.torsion2"}, with the exception of the correction [\[torcorr1\]](#torcorr1){reference-type="eqref" reference="torcorr1"} coming from the $\hbar^0$ part of the exponential. This correction now becomes

$$\exp\Big[ f\cdot \mathbf B^{-1}\bm u+\frac{i\pi}{2}f\cdot \mathbf B^{-1}\nu-\frac12Z\cdot \mathbf B^{-1}\nu\Big]\,. \label{utorcorr1}$$

To simplify this correction, we must use $\mathbf Af+\mathbf Bf''=\nu$ and a deformed gluing equation $\mathbf A Z+\mathbf B Z''=2\bm u+i\pi \nu$. The $\bm u$-dependent part of the gluing equation cancels the new $\bm u$-dependent term in [\[utorcorr1\]](#utorcorr1){reference-type="eqref" reference="utorcorr1"}, ultimately leading to the same result

$$\exp\Big[ f\cdot \mathbf B^{-1}\bm u+\frac{i\pi}{2}f\cdot \mathbf B^{-1}\nu-\frac12Z\cdot \mathbf B^{-1}\nu\Big] = \big(z{}^{f''}z''{}^{-f}\big)^{-1/2}\,, \notag$$

and therefore the same torsion

[^1]

$$\tau_\mathcal{T}= 4\pi e^{-2S_{\mathcal{T},1}} = \frac12\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1}\big)z^{f''}z''{}^{-f}\,.$$

Finally, we can produce a generalized version of the Feynman rules of Section [\[sec.diags\]](#sec.diags){reference-type="ref" reference="sec.diags"}. We note, however, that the $u$-dependent terms in [\[uSIM\]](#uSIM){reference-type="eqref" reference="uSIM"} do not contribute to either the vacuum energy $\Gamma^{(0)}$ (at order $\hbar^1$ or higher), the propagator, or the vertex factors $\Gamma^{(k)}_i$. Therefore, the Feynman rules must look exactly the same. The only difference is that the critical point equation [\[ucrit\]](#ucrit){reference-type="eqref" reference="ucrit"} requires us to use shape parameters that satisfy the generalized gluing equations.

## Example: $\mathbf{4_1}$ completed {#sec.41Sn}

We may demonstrate the power of the Feynman-diagram approach by computing the first two subleading corrections $S_{\mathcal{T},2}$ and $S_{\mathcal{T},3}$ for the figure-eight knot complement.

We can use the same Neumann-Zagier datum described in Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"}, along with the generalized flattening of Section [\[sec.utor41\]](#sec.utor41){reference-type="ref" reference="sec.utor41"}. Let us specialize to representations $\rho_m$ on the geometric component of the character variety. Then the two shapes $z,\,w$ are expressed as functions on the A-polynomial curve,

$$\label{zw412} z = -\frac{m^2-m^{-2}}{1+m^2\ell} \,,\qquad w= \frac{m^2+\ell}{m^2-m^{-2}}\,,$$

as in [\[zw41m\]](#zw41m){reference-type="eqref" reference="zw41m"}.

The 2-loop invariant is explicitly given in [\[2loopexplicit\]](#2loopexplicit){reference-type="eqref" reference="2loopexplicit"} of the Introduction. Evaluating this expression in `Mathematica`, we find

$$\notag S_{\mathbf{4_1},2}=-\frac{w^3 (z+1)+w^2 ((11-8 z) z-4)+w (z-1) (z (z+12)-5)+(z-2) (z-1)^2}{12 (w+z-1)^3}\,.$$

Upon using [\[zw412\]](#zw412){reference-type="eqref" reference="zw412"} to substitute rational functions for $z$ and $w$, the answer may be most simply expressed as

$$\widetilde S_{\mathbf{4_1},2}= \frac{S_{\mathbf{4_1},2}+1/8}{\tau_{\mathbf{4_1}}^3} = -\frac{1}{192}\big(m^{-6}-m^{-4}-2m^{-2}+15-2m^2-m^4+m^6\big)\,,$$

where we have divided by a power of the torsion as suggested in [\[tordivide\]](#tordivide){reference-type="eqref" reference="tordivide"} of the Introduction. (We have also absorbed a constant $1/8$, recalling that our formula is only well defined modulo $\mathbb Z/24$.

In a similar way, we may calculate the 3-loop invariant, finding unambiguously

$$\widetilde S_{\mathbf{4_1},3} = \frac{S_{\mathbf{4_1},3}}{\tau_{\mathbf{4_1}}^6}=\frac{1}{128}\big(m^{-6}-m^{-4}-2m^{-2}+5-2m^2-m^4+m^6\big)\,.$$

These answers agree perfectly with the findings of [@DGLZ], and the comparison there to the asymptotics of the colored Jones polynomials at general $u$. Moreover, at the discrete faithful representation we obtain

$$S_{\mathbf{4_1},2} = \frac{11i}{72\sqrt{3}}= -\frac{11}{192\,\tau_{\mathbf{4_1}}^{3}}\,,\qquad S_{\mathbf{4_1},3}=-\frac1{54} = \frac{1}{128\,\tau_{\mathbf{4_1}}^{6}}\,,$$

in agreement with known asymptotics of the Kashaev invariant.

[^1]: The normalization of the torsion here differs from the torsion at the discrete faithful by a factor of $\pi^2$. In fact, we intentionally changed the normalization of the entire state integral [\[uSIM\]](#uSIM){reference-type="eqref" reference="uSIM"} by $\pi^2$. This is because we wanted the state integral to match the asymptotics of the colored Jones polynomials exactly, and the asymptotics happen to jump by $\pi^2$ when $u\neq 0$, *cf.* [@GuM].
