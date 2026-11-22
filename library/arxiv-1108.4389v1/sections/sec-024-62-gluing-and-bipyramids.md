---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-024-62-gluing-and-bipyramids
section_title: "Gluing and bipyramids"
section_number: 6.2
pages: 48-50
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.687
latex_coverage_ratio: 0.995
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
In Section [\[sec:MS\]](#sec:MS){reference-type="ref" reference="sec:MS"}, we derived $ST$-invariance of the tetrahedron theory $\mathcal{T}_1\simeq \mathcal{T}_{\Delta,\Pi_Z}$ by starting with $\mathcal{N}=4$ mirror symmetry, translating to $\mathcal{N}=2$ mirror symmetry for the XYZ model and SQED with $N_f=1$, and and then reducing further to the theories $\mathcal{T}_1$ and $ST\circ \mathcal{T}_1$ via a mass deformation. It is somewhat instructive to now do the same at the level of partition functions. In the process, we will see how gluing of partition functions should work.

Let's begin with the partition function of a hypermultiplet, with (complex) vector twisted mass denoted by $x$ and axial twisted mass by $y$: $$Z_{S^3_b} (\, \text{hypermultiplet} \, ) \; = \; s_b \big( \tfrac{iQ}{2} -x -y \big) s_b \big( \tfrac{iQ}{2} +x -y \big)\,.
\label{Zhyper}$$

The ${\cal N}=2$ R-charge and axial charge are a linear combination of the Cartan generators of the $SU(2)_H \times SU(2)_C$ R-charges of the ${\cal N}=4$ theory. We are using a convention where in the ${\cal N}=2$ language the R-symmetry of chiral multiplets in the standard hypermultiplet is absorbed in their axial twisted mass $y$. Then the scalar field in the vectormultiplet has "bare" R-charge $2$, and axial charge $-2$, i.e. complex twisted mass $i Q -2y$. This is also required for the basic superpotential coupling required by an ${\cal N}=4$ gauging.

Hence if we add a full $\mathcal{N}=4$ gauge multiplet to gauge the flavor symmetry, the chiral multiplet in it contributes a $s_b(2 y - i Q/2)$. The partition function is $$s_b(2 y - i Q/2) \int s_b(i Q/2-x -y) s_b(i Q/2+x -y) e^{- 2 i \pi z x } dx\,.$$

The basic $\mathcal{N}=4$ mirror symmetry should match this to the partition function of a twisted hypermultiplet, *i.e.* a hypermultiplet with the opposite axial charge [@IS]. The chiral fields in a twisted hypermutliplet have "bare" R-charge $1$ and axial charge $-1$, i.e. complex twisted mass $\tfrac{iQ}{2} -y$. Hence we should replace $y$ with $\tfrac{iQ}{2}-y$ in [\[Zhyper\]](#Zhyper){reference-type="eqref" reference="Zhyper"} and write the basic $\mathcal{N}=4$ mirror symmetry relation as

$$\label{twothree}
s_b(2 y - i Q/2) \int s_b(i Q/2-x -y) s_b(i Q/2+x -y) e^{- 2 i \pi z x } dx = s_b(y-z) s_b(y+z)$$

As a check, we are supposed to obtain either the partition functions of $\mathcal{N}=2$ SQED with $N_f=1$ flavor or the partition function of the XYZ model by acting with $S$ or with $F$ on the above relation. If we act with $S$, *i.e.* with the Fourier transform, we get

$$s_b(2 y - i Q/2)  s_b(i Q/2-x -y) s_b(i Q/2+x -y) \; = \; \int s_b(y-z) s_b(y+z) e^{- 2 i \pi z x }  dx \,. \label{ZXYZ}$$

The left-hand side is the partition function of the XYZ model. The real masses of the three chiral fields add to zero, and the R-charges to $2$, as it should be to allow the superpotential interaction $\mathcal{W}= \mu u\tilde u$, *cf.* Section [\[sec:MS\]](#sec:MS){reference-type="ref" reference="sec:MS"}. Equation [\[ZXYZ\]](#ZXYZ){reference-type="eqref" reference="ZXYZ"} happens to be another well known identity for quantum dilogarithm functions [@FKV; @PonsotTeschner].

Now, if we redefine $x\to x-y$, $z\to z+y-\tfrac{iQ}{2}$, and take $y$ to be large and positive in [\[twothree\]](#twothree){reference-type="eqref" reference="twothree"}, we replicate the mass deformation that reduces us to the theory $\mathcal{T}_1 \simeq \mathcal{T}_{\Delta,\Pi_Z}$. Expression [\[twothree\]](#twothree){reference-type="eqref" reference="twothree"} becomes

$$\int dx\, e^{-i\pi x\big(x+2(z-\frac{iQ}{2})\big)}\,e_b\big(\tfrac{iQ}{2}-x\big) = e_b\big(\tfrac{iQ}{2}-z\big)\,,$$

which is precisely [\[STZDelta\]](#STZDelta){reference-type="eqref" reference="STZDelta"}, expressing the mirror symmetry $\sigma\circ \mathcal{T}_1 \simeq  \mathcal{T}_1$.

We could also add Chern-Simons terms on both sides of [\[ZXYZ\]](#ZXYZ){reference-type="eqref" reference="ZXYZ"} in order to reproduce the exact partition function of the bipyramid theory, as discussed in Section [\[sec:gauge23\]](#sec:gauge23){reference-type="ref" reference="sec:gauge23"}. Namely, we find an identity

$$\begin{aligned}
 & e^{i\pi (i Q)\tilde m_3}e_b\big(\tfrac{iQ}{2}-\tilde m_1\big)e_b\big(\tfrac{iQ}{2}-\tilde m_2\big)e_b\big(\tfrac{iQ}{2}-\tilde m_3\big)\Big|_{\tilde m_3=iQ-\tilde m_1-\tilde m_2} \\
 &\hspace{1in} =\int d\sigma\, e^{-i\pi \sigma^2-2\pi i\sigma\big(\tilde m_2-\frac{iQ}{2}\big)}e_b\big(\tfrac{iQ}{2}+\sigma\big)e_b\big(\tfrac{iQ}{2}-\sigma+\tilde m_1\big)
\notag 
\end{aligned}$$

The two sides correspond to the theories of three and two tetrahedra, respectively, both in the equatorial polarization $\Pi_{\rm eq}$, with external edge positions $X_1 = 2\pi b\, \tilde m_1$ and $X_2=2\pi b\,\tilde m_2$. For the left-hand side, the superpotential $\mathcal{W}= \mathcal{O}_C = \phi_Z\phi_W\phi_Y$ [\[WXYZ\]](#WXYZ){reference-type="eqref" reference="WXYZ"} implements the constraint $\tilde m_1+\tilde m_2+\tilde m_3=iQ$.

More generally, the rules for constructing theories $T_{M,\Pi}$ in Section [\[sec:glue\]](#sec:glue){reference-type="ref" reference="sec:glue"} lead to the following rules for calculating the corresponding ellipsoid partition functions:

-   Multiply together partition functions $Z_{S^3_b}(T_{\Delta_i,\Pi_i};\tilde m_{Z_i}) = e_b\big(\tfrac{iQ}{2}-\tilde m_{Z_i}\big)$, one for each tetrahedron in the triangulation of $M$.

-   Act with $Sp(2N,{\mathbb Z})$ in the Weil representation (*i.e.* by generalizing the quadratic exponentials and Fourier transforms of [\[Z3T\]](#Z3T){reference-type="eqref" reference="Z3T"}--[\[Z3S\]](#Z3S){reference-type="eqref" reference="Z3S"}), to transform to the polarization $\tilde\Pi$ in which all internal edges are "positions."

-   Set the complex masses $\tilde m_I$ now associated to internal edges equal to $iQ$.

We note that the specialization in Step 3 is the only consequence of adding a superpotential $\mathcal{W}= \sum_I \mathcal{O}_I$ to the theory $T_{M,\Pi}$. Indeed, such a superpotential sets the real masses of the $\mathcal{O}_I$ to zero and the R-charges equal to $2$. Otherwise, the ellipsoid partition function is completely independent of superpotential terms, and cares only about gauge and matter content.

These rules for constructing $Z_{S^3_b}(T_{M,\Pi})$ are identical to the rules presented in [@Dimofte-QRS] for building the $SL(2)$ Chern-Simons partition function of $M$. One can see even subtle quantum effects matching in the two descriptions. For example, in quantum Chern-Simons theory, the classical internal edge constraints $C_I = 2\pi i$ become corrected to $C_I = 2\pi i+\hbar$, and this follows immediately from the dictionary [\[XmO\]](#XmO){reference-type="eqref" reference="XmO"} between edge parameters and complexified masses $\tilde m_I$.

## Figure-eight knot

We should be able to reproduce the well known Chern-Simons wavefunction for the figure-eight knot complement from the theory $T_{\mathbf{4_1},\Pi}$ described in Section [\[sec:gauge41\]](#sec:gauge41){reference-type="ref" reference="sec:gauge41"}. The definition of the actual theory, including internal edge operators, required a decomposition of the knot complement into six tetrahedra. However, since ellipsoid partition functions do not depend in a crucial way on superpotential terms, we might hope to get away with the simpler decomposition into two tetrahedra, also discussed in Section [\[sec:gauge41\]](#sec:gauge41){reference-type="ref" reference="sec:gauge41"}. Indeed, this turns out to work.

From the Lagrangian [\[41tet2\]](#41tet2){reference-type="eqref" reference="41tet2"}, we can immediately write down a partition function

$$Z_{S^3_b}(T_{\mathbf{4_1},\Pi};\tilde m_U) = \int d\sigma\, e^{i\pi\big(\tilde m_U^2+(2\tilde m_C-iQ+2\tilde m_U-\sigma)\sigma\big)}\,e_b\big(\tfrac{iQ}{2}-\sigma-\tilde m_U\big)e_b\big(\tfrac{iQ}{2}-\sigma\big)\,.$$

Now, there are no operators in the theory to force $\tilde m_{C_1}=iQ$, but we can put this in by hand. Up to a factor of due to a small change of polarization, the result is then identical to the figure-eight wavefunctions described in [@hikami-2006; @DGLZ; @Dimofte-QRS] (see also [@Yamazaki-layered; @SpirVar-knots]).

## Relation to moduli spaces on ${\mathbb R}^2\times S^1$

Finally, we point out that our tests of the proposed duality $(M,\Pi) \; \leftrightarrow \; T_{M,\Pi}$ here and in section [\[sec:moduli\]](#sec:moduli){reference-type="ref" reference="sec:moduli"} are not entirely unrelated. Indeed, in the semi-classical limit $\hbar = 2\pi i b^2 \to 0$, the partition function of the theory $T_M$ behaves exactly in the same way as the partition function of Chern-Simons theory on $M$, $$Z_{S^3_b} (T_M) \,\overset{\hbar\to0}{\sim}\, \exp\Big(\frac1\hbar \widetilde{\mathcal{W}}_{{\rm eff}} + \mathcal{O}(\log\hbar)\Big)\,,
\label{zscw}$$ where $\widetilde{\mathcal{W}}_{{\rm eff}}$ is the effective twisted superpotential of the theory $T_M$ on ${\mathbb R}^2 \times S^1$. Hence, if $\widetilde{\mathcal{W}}_{{\rm eff}}$ matches the classical $SL(2)$ Chern-Simons action on $M$, $$\widetilde{\mathcal{W}}_{{\rm eff}} (T_M) \; = \; S_0 (M) \,,$$ then the relation between moduli spaces [\[MMclaim\]](#MMclaim){reference-type="eqref" reference="MMclaim"} follows automatically. Indeed, the moduli space $\mathcal{M}_{{\rm flat}} (M,SL(2,{\mathbb C}))$ is a graph of $d S_0$ and, similarly, the moduli space $\mathcal{M}_{{\rm SUSY}} (T_M)$ is a graph of $d \widetilde{\mathcal{W}}_{{\rm eff}}$. In terms of gauge theory, the reason for [\[zscw\]](#zscw){reference-type="eqref" reference="zscw"} is that, in the limit $b \to 0$, the squashed 3-sphere $S^3_b$ degenerates into ${\mathbb R}^2 \times S^1$,

$$S^3_b \quad \leadsto \quad {\mathbb R}^2 \times S^1 \,.$$

The relation between moduli spaces $\mathcal{M}_{\rm flat}(M,SL(2,{\mathbb C})) = \mathcal{M}_{\rm SUSY}(T_M)$ of Section [\[sec:moduli\]](#sec:moduli){reference-type="ref" reference="sec:moduli"} has a "quantum" analog that does not require taking the limit $\hbar \to 0$. Indeed, the full quantum partition functions discussed here obey a set of $q$-difference equations: $$\boxed{\phantom{\int}
\widehat{A}_i \; Z \; = \; 0
\phantom{\int}}
\label{AZclaim}$$ for some operators $\widehat{A}_i$ that in the classical limit become defining polynomials of our moduli spaces. In Chern-Simons theory, [\[AZclaim\]](#AZclaim){reference-type="eqref" reference="AZclaim"} is known as the generalized / quantum volume conjecture [@gukov-2003] (sometimes also called the AJ-conjecture [@Gar-Le; @garoufalidis-2004] in the math literature), whereas in $\mathcal{N}=2$ gauge theory it expresses Ward identities for line operators. We consider these line operators next.
