---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-023-61-chirals-and-tetrahedra
section_title: "Chirals and tetrahedra"
section_number: 6.1
pages: 47-48
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:S3tet label="sec:S3tet"}

Consider a free chiral multiplet $\phi_Z$ with twisted mass $m_Z$ for a $U(1)$ flavor symmetry, and R-charge $R_Z$. This R-charge assignment enters in a fundamental way when putting the chiral on an ellipsoid. We set $\tilde m_Z = m_Z+\frac{iQ}{2}R_Z$, and find a partition function

[^1]

[@HHL]

$$Z_{S^3_b}(\text{chiral multiplet}) = s_b\big(\tfrac{iQ}{2}-\tilde m_Z\big)\,, \label{Zchiral}$$

where

$$s_b(x) = \prod_{m,n \in {\mathbb Z}_{\ge 0}} \frac{mb + nb^{-1} + \tfrac{Q}{2}-ix}{mb + nb^{-1} + \tfrac{Q}{2}+ix} = e^{-\frac{i\pi}{2}x^2}\prod_{r=1}^\infty\frac{1+e^{2\pi bx+2\pi i b^2(r-\tfrac12)}}
 {1+e^{2\pi b^{-1}x+2\pi ib^{-2}(\tfrac12-r)}}
\label{sbdef}$$

is a variant of the noncompact quantum dilogarithm function [@Barnes-QDL; @Fad-modular] commonly used in Liouville theory.

Two of the properties enjoyed by the function $s_b(x)$ are

$$\begin{equation}
s_b(x) s_b(-x) \; = \; 1\,,
\label{sbsb1}
\end{equation}
\begin{equation}
s_b(x) \sim
\begin{cases}
e^{i \pi x^2/2} & \mbox{as } x \to + \infty \\
e^{-i \pi x^2/2} & \mbox{as } x \to - \infty\,,
\end{cases}
\label{sbasympt}
\end{equation}$$

which have a nice interpretation in 3d $\mathcal{N}=2$ gauge theory. According to [\[Zchiral\]](#Zchiral){reference-type="eqref" reference="Zchiral"}, the first property [\[sbsb1\]](#sbsb1){reference-type="eqref" reference="sbsb1"} implies that the partition function of two chiral fields $\phi$, $\phi'$ of opposite flavor charge and R-charge adding to 2 is trivial. Indeed, this R-charge assignment allows one to add a marginal superpotential

$$\mathcal{W}\; = \; M \phi \phi'$$

which makes both fields arbitrarily massive and decouples them. The second property [\[sbasympt\]](#sbasympt){reference-type="eqref" reference="sbasympt"} agrees with an important fact: a Chern-Simons action of level $k$ for the background gauge field gives a contribution

$$e^{- i \pi k \tilde m^2}
\label{z3dCSk}$$

to the partition function. Therefore, we see that at large positive $\sigma$ the chiral multiplet contributes as a Chern-Simons coupling of level $+\tfrac{1}{2}$, while at large negative $\sigma$ as a Chern-Simons coupling of level $-\tfrac{1}{2}$, as expected [@AHISS] (*cf.* our discussion of such couplings in Section [\[sec:MS\]](#sec:MS){reference-type="ref" reference="sec:MS"}). In a similar way, many beautiful identities obeyed by the special function [\[sbdef\]](#sbdef){reference-type="eqref" reference="sbdef"} --- in turn related to the combinatorics of 3-manifolds triangulations --- find physical interpretation as dualities among 3d $\mathcal{N}=2$ gauge theories.

The actual theory $T_{\Delta,\Pi_Z}$ associated to a tetrahedron has an extra level $-\tfrac12$ Chern-Simons coupling for the background gauge field, leading to a partition function

$$\boxed{ Z_{S^3_b}(T_{\Delta,\Pi_Z};\tilde m_Z) = e_b\big(\tfrac{iQ}{2}-\tilde m_Z\big) \equiv e^{\frac{i\pi}{2}\big(\frac{iQ}2-\tilde m_Z\big)^2}s_b\big(\tfrac{iQ}{2}-\tilde m_Z\big) \,.}
\label{ZDelta}$$

With the identification [\[XmO\]](#XmO){reference-type="eqref" reference="XmO"}, this is equivalent to the Chern-Simons partition function of a single tetrahedron, found in [@Dimofte-QRS].

In order to consider other polarizations for $T_{\Delta}$, we should analyze how the $SL(2,{\mathbb Z})$ action on gauge theories affects partition functions. It is already clear from [\[z3dCSk\]](#z3dCSk){reference-type="eqref" reference="z3dCSk"} that the $T$-move sends

$$T\;:\quad Z_{S^3_b}(\tilde m)\;\mapsto\; Z_{S^3_b}'(\tilde m)= e^{-i\pi \tilde m^2}Z_{S^3_b}(\tilde m)\,. \label{Z3T}$$

Similarly, the $S$-move adds a factor $e^{-2\pi i \tilde m\tilde m'}$ to the partition function, and dictates that we integrate over the vev $m$, since its gauge multiplet has become dynamical. In other words, $S$ acts as a Fourier transform:

$$S\;:\quad Z_{S^3_b}(\tilde m)\;\mapsto\; Z_{S^3_b}'(\tilde m')=\int d\tilde m\, e^{-2\pi i \tilde m\tilde m'}\, Z_{S^3_b}(\tilde m)\,. \label{Z3S}$$

Note that this an integral along the real line, which could be deformed to a contour in the complex plane. In addition to $S$ and $T$, affine shifts in polarization also act nontrivially on the ellipsoid, by redefining the R-charge used to couple a theory to background curvature. For example, a classical shift by $\pm i\pi$ in a position coordinate $Z$ corresponds to sending $R_Z\mapsto R_Z\pm 1$, or $\tilde m_Z\mapsto \tilde m_Z\pm \tfrac{iQ}{2}$.

The above action of the affine symplectic group shows that the ellipsoid partition function transforms as a wavefunction under changes of polarization, precisely as claimed. In particular, the above transformations are identical to those that appear in $SL(2)$ Chern-Simons theory. As a simple example, we can consider the affine $ST$ action that sends the polarization $\Pi_Z$ to $\Pi_{Z'}$ for the tetrahedron theory. This affine action was called $\sigma$ in [\[sST\]](#sST){reference-type="eqref" reference="sST"}. We find

$$\begin{aligned}
 Z_{S^3_b}(T_{\Delta,\Pi_{Z'}};\tilde m_{Z'}) &=\sigma \circ Z_{S^3_b}(T_{\Delta,\Pi_Z}) \notag \\ &= \int\, dm_Z\,e^{-i\pi \tilde m_Z(\tilde m_Z+2\tilde m_{Z'}-iQ)}\,
e_b\big(\tfrac{iQ}{2}-\tilde m_Z\big)  \notag \\
&= e_b\big(\tfrac{iQ}{2}-\tilde m_{Z'}\big)\,, \label{STZDelta}
\end{aligned}$$

up to a constant factor. The last equality follows from a standard functional identity for $e_b(x)$ [@FKV], and verifies the prediction from mirror symmetry that the transformation $\sigma$ leaves the tetrahedron theory invariant.

[^1]: Here and in the following, we will ignore overall numerical constants in front of the partition function.
