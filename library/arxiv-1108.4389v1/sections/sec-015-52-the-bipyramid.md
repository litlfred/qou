---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-015-52-the-bipyramid
section_title: "The bipyramid"
section_number: 5.2
pages: 44-47
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.996
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

# $S^3_b$ partition functions {#sec:S3b}

In the previous section, the correspondence $(M,\Pi) \; \leftrightarrow \; T_{M,\Pi}$ was tested by comparing moduli spaces attached to each side of the correspondence. A more refined test could be obtained by associating certain functions to each side. For example, on the gauge theory side one can associate either an equivariant partition function or an index (an analog of the elliptic genus) to the 3d $\mathcal{N}=2$ theory $T_M$, by analogy with what was done in [@AGT] or [@Rastelli-2dQFT; @Rastelli-qYM] in the context of 4d $\mathcal{N}=2$ gauge theory. Then, these functions are expected to match the corresponding topological invariants of $M$.

In this section, we discuss one such test based on comparing the partition function of the 3d $\mathcal{N}=2$ theory $T_{M,\Pi}$ on a squashed three-sphere (or "ellipsoid") $S^3_b$ with the $SL(2)$ Chern-Simons partition function of the 3-manifold $M$:

$$\boxed{\phantom{\int}
Z^{SL(2)}_{\rm CS} (M) \; = \; Z_{S^3_b} (T_{M,\Pi})\,,
\phantom{\int}}
\label{ZZclaim}$$

where the squashing parameter $b$ is related to the Chern-Simons coupling coupling strength $\hbar$ as

$$\hbar = 2\pi ib^2\,.$$

This relation is a direct generalization of the AGT correspondence [@AGT] to three dimensions. In fact, it is fully consistent with the AGT correspondence, which corresponds to taking $M = {\mathbb R}\times \mathcal{C}$ to be a product of the "time" direction and a Riemann surface $\mathcal{C}$ (possibly with punctures), through a somewhat lengthy chain of correspondences [@DGG-defects], [@DG-Sdual], reviewed e.g. in [@Yamazaki-3d]

Various aspects of partition functions in $SL(2)$ Chern-Simons theory are discussed in [@gukov-2003; @DGLZ; @Wit-anal; @Dimofte-QRS]. Given a 3-manifold $M$ with boundary phase space $\mathcal{P}_{\partial M}$, as defined here in Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}, Chern-Simons theory should promote $\mathcal{P}_{\partial M}$ to a Hilbert space

$$\mathcal{P}_{\partial M}\;\leadsto\; \mathcal{H}_{\partial M}\,, \label{HdM}$$

and the partition function $Z^{SL(2)}_{\rm CS}(M)$ can be thought of as a distinguished wavefunction in $\mathcal{H}_{\partial M}$. In particular, $Z^{SL(2)}_{\rm CS}(M;X_1,X_2,...)$ is a function of half the coordinates on $\mathcal{P}_{\partial M}$, the "positions" in a given polarization $\Pi$. An affine $Sp(2N,{\mathbb Z})$ change of polarization acts on $Z^{SL(2)}_{\rm CS}(M;X_1,X_2,...)$ in the standard Weil representation [@Shale-rep; @Weil-rep]; for example, $S$-type elements act as Fourier transform, and $T$-type elements act as multiplication by quadratic exponentials $\sim \exp \frac{X_i^2}{2\hbar}$.

Similarly, the $S^3_b$ partition function of $T_{M,\Pi}$ depends on the twisted masses $m_\mathcal{O}$ of various chiral operators that transform under $U(1)$ flavor symmetries. These real masses are naturally complexified by the R-charge, due to the background curvature of the ellipsoid [@Kapustin-3dloc; @HHL]. Indeed, if we describe $S^3_b$ geometrically as

$$b^2|z_1|^2+b^{-2}|z_2|^2 = 1\,,\qquad z_1,z_2\in\mathcal{C}\,, \label{defS3b}$$

then $Z_{S^3_b}(T_{M,\Pi})$ depends holomorphically on the combinations $\tilde m_\mathcal{O}\equiv m_\mathcal{O}+\frac{iQ}{2}R_\mathcal{O}$, with $Q=b+b^{-1}$. These complexified masses become identified with the "positions" in $\mathcal{P}_{\partial M}$ or $\mathcal{H}_{\partial M}$, as

[^1]

$$\label{XmO}
X = 2\pi b\,
 \tilde m_{\mathcal{O}_X}= 2\pi b\,m_{\mathcal{O}_X}+\Big(i\pi+\frac\hbar2\Big)R_{\mathcal{O}_X}\,,$$

where $\mathcal{O}_X$ is (say) the operator we associated to a boundary position $X$ in Section [\[sec:defTM\]](#sec:defTM){reference-type="ref" reference="sec:defTM"}. We will see that the ellipsoid partition function $Z_{S^3_b}(T_{M,\Pi};\tilde m_{X_1},\tilde m_{X_2},...)$ transforms as a wavefunction under changes of the polarization $\Pi$, in exactly the same way as $Z^{SL(2)}_{\rm CS}(M;X_1,X_2,...)$.

Both sides of [\[ZZclaim\]](#ZZclaim){reference-type="eqref" reference="ZZclaim"} are eminently computable. In fact, [@Dimofte-QRS] developed a general state integral model for $SL(2)$ Chern-Simons theory that directly quantizes the semi-classical construction of flat connections from ideal tetrahedra, as described in Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}. Similarly, [@HHL] derived a prescription for ellipsoid partition functions of Chern-Simons-matter theories, using equivariant localization. It is not hard to see that the two constructions become equivalent when applied to our theories $T_{M,\Pi}$. We proceed to study a few aspects of this equivalence, starting with basic $T_\Delta$ building blocks and then forming more general theories/manifolds.

[^1]: Throughout this section, we work in units such that the "average" radius of the ellipsoid is $\rho=1$. Otherwise, it would appear on the right-hand side of [\[defS3b\]](#defS3b){reference-type="eqref" reference="defS3b"}, and would multiply $m_{\mathcal{O}_X}$ in [\[XmO\]](#XmO){reference-type="eqref" reference="XmO"}.
