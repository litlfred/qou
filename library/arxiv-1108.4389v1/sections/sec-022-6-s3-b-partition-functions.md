---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-022-6-s3-b-partition-functions
section_title: "$S^3_b$ partition functions"
section_number: 6
pages: 45-47
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:S3b label="sec:S3b"}

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
