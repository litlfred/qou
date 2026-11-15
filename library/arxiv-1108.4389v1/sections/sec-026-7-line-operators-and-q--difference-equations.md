---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-026-7-line-operators-and-q--difference-equations
section_title: "Line operators and $q$--difference equations"
section_number: 7
pages: 52-58
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.609
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:lines label="sec:lines"}

In order to understand the meaning of operator identities [\[AZclaim\]](#AZclaim){reference-type="eqref" reference="AZclaim"} in 3d $\mathcal{N}=2$ theory, we need to incorporate line operators in our correspondence [\[MvsTM\]](#MvsTM){reference-type="eqref" reference="MvsTM"}.

Given a triangulated 3-manifold $M$ with nonempty boundary $\partial M$, each equation in [\[AZclaim\]](#AZclaim){reference-type="eqref" reference="AZclaim"} is written in terms of quantum holonomy operators

[^1]

that, from the viewpoint of Chern-Simons theory on $M$, are obtained by quantizing the space of flat $SL(2,{\mathbb C})$ connections $\mathcal{P}_{\partial M}$ on the boundary. These operators act on the Hilbert space [\[HdM\]](#HdM){reference-type="eqref" reference="HdM"}. We illustrate this with a simple example that plays a key role in this paper, namely with the $\mathcal{N}=2$ theory $T_{\Delta,\Pi_Z}$ that we associate with a single tetrahedron.

In particular, in the previous section we identified the $S^3_b$ partition function of this theory [\[ZDelta\]](#ZDelta){reference-type="eqref" reference="ZDelta"} with the wave function of the $SL(2)$ Chern-Simons theory on a tetrahedron. From the explicit form of the partition function [\[ZDelta\]](#ZDelta){reference-type="eqref" reference="ZDelta"}, it is easy to see that it satisfies the functional equation

[^2]

$$\mathcal{Z}(\tilde m_Z + ib \big) = \left( 1 - e^{-2\pi b \tilde m_Z} \right) \mathcal{Z}(\tilde m_Z ) \,.$$ Using $\hat Z''= ib\partial_{\tilde m_Z}$ and $\hat Z=2\pi b\tilde{m}_Z$, we can write this equation in a more convenient form: $$\left( e^{\hat Z''} + e^{-\hat Z} - 1 \right) \mathcal{Z}(\tilde m_Z) \; = \; 0 \,,
\label{psiAhat}$$ which is clearly reminiscent of the familiar equation [\[Aone\]](#Aone){reference-type="eqref" reference="Aone"} that describes the space of SUSY moduli in the theory $T_{\Delta, \Pi_{Z'}}$. Indeed, for reasons that we reviewed at the end of section [\[sec:S3b\]](#sec:S3b){reference-type="ref" reference="sec:S3b"}, in the semi-classical limit $\hbar \sim b^2 \to 0$ the equation [\[psiAhat\]](#psiAhat){reference-type="eqref" reference="psiAhat"} gives precisely [\[Aone\]](#Aone){reference-type="eqref" reference="Aone"}: $$\mathcal{M}_{{\rm SUSY}}
~:~ \quad
e^Z + e^{- Z'} - 1 \; = \; 0 \,.
\label{apoltetr}$$

In terms of geometry, we know from Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"} that $Z$ and $Z'$ are the complexified "shear coordinates" or edge parameters on the boundary $\partial\Delta$ of the tetrahedron; and indeed [\[psiAhat\]](#psiAhat){reference-type="eqref" reference="psiAhat"} is just the quantization of the tetrahedron's classical Lagrangian [\[LDelta\]](#LDelta){reference-type="eqref" reference="LDelta"} [@Dimofte-QRS]. More generally, if a 3-manifold $M$ has a triangulated geodesic boundary, it is the quantization of external edge coordinates $\exp(\hat X_E)$ on the boundary that appears in the operator equations [\[AZclaim\]](#AZclaim){reference-type="eqref" reference="AZclaim"}.

From a different perspective, the classical external edge coordinates $x_E=\exp(X_E)$ on a triangulated geodesic boundary $\mathcal{C}=\partial M$ also correspond to vevs of line operators in the *four-dimensional* $\mathcal{N}=2$ theory $T[\mathcal{C},\mathfrak{su}(2)]$; and the quantized $\hat x_E=\exp(\hat X_E)$ correspond to the quantum line operators themselves [@DMO; @AGGTV; @DGOT; @GMNIII]. To be more precise, it was shown in [@GMNII; @GMNIII] that every edge $E$ of $\mathcal{C}$ determines an IR line operator $\exp(\hat X_E)$ in the abelian $\mathcal{N}=2$ theory on the Coulomb branch of $T[\mathcal{C},\mathfrak{su}(2)]$. This operator carries the electric and magnetic charges associated to the edge $E$, exactly as described in Section [\[sec:gauge4d\]](#sec:gauge4d){reference-type="ref" reference="sec:gauge4d"}. Using this relation, we propose to interpret operator equations [\[AZclaim\]](#AZclaim){reference-type="eqref" reference="AZclaim"} as Ward identities for line operators in a 4d theory coupled to the 3d boundary theory $T_M$.

![Line operators in 4d becoming identified in the boundary theory $T_M$.](bdyop){#fig:bdyop width="2.5in"}

In the presence of boundary conditions, not all line operators of the bulk $\mathcal{N}=2$ gauge theory in four dimensions are independent. Indeed, one can start with a line operator $L$ (or, more generally, a collection of line operators $L_i$) in the 4d $\mathcal{N}=2$ gauge theory and then bring it to the three-dimensional boundary where the theory $T_M$ lives (Figure [1](#fig:bdyop){reference-type="ref" reference="fig:bdyop"}). Due to the boundary conditions (which *e.g.* may identify some of the 4d fields), vevs of line operators that were independent in the bulk become related on the boundary. This can be summarized in the form of Ward identities $$\sum c_i L_i \; = \; 0 \,.
\label{cLi}$$ For example, in our favorite example of the theory $T_{\Delta}$ the equation [\[psiAhat\]](#psiAhat){reference-type="eqref" reference="psiAhat"} can be written in the form [\[cLi\]](#cLi){reference-type="eqref" reference="cLi"} as $$W + H^{-1} - 1 \; \simeq \; 0
\label{WHinT1}$$ where we used the identification of $\hat Z$, $\hat Z'$, and $\hat Z''$ with the corresponding abelian Wilson / 't Hooft line operators:

$$\begin{array}{l@{\qquad}l}
\underline{\text{edge}} & \underline{\text{line operator}} \\[.1cm]
\hat z = e^{\hat Z} & W=\text{Wilson} \\[.1cm]
\hat z' = e^{\hat Z'} & \text{Wilson-'t Hooft} \\[.1cm]
\hat z'' = e^{\hat Z''} & H=\text{'t Hooft}
\end{array}
\label{whhlines}$$

(Thus, $\hat z^{-1}=H^{-1}$ denotes an 't Hooft operator of magnetic charge $-1$. Similarly, $W^0=H^0=1$ denotes a trivial line operator.) The above dictionary [\[whhlines\]](#whhlines){reference-type="eqref" reference="whhlines"} corresponds to the polarization $\Pi_{Z}$ for $T_\Delta$. The triality symmetry of $T_\Delta$ [\[STonT1\]](#STonT1){reference-type="eqref" reference="STonT1"}, generated by the $ST$ element of the 4d electric-magnetic duality group $SL(2,{\mathbb Z})$, permutes Wilson, 't Hooft, and Wilson-'t Hooft operators.

To explain the origin of Ward identities like [\[WHinT1\]](#WHinT1){reference-type="eqref" reference="WHinT1"}, it is instructive to simplify the theory $T_{\Delta}$ (which consists of a chiral multiplet and Chern-Simons coupling) even further and consider only the Chern-Simons part of the theory. As we discussed in section [\[sec:S3b\]](#sec:S3b){reference-type="ref" reference="sec:S3b"}, a supersymmetric Chern-Simons interaction at level $k$ for the background gauge field contributes to the partition function a factor [\[z3dCSk\]](#z3dCSk){reference-type="eqref" reference="z3dCSk"}: $$\mathcal{Z}_{CS_k} = e^{- i \pi k \tilde m^2} \,.$$ Much like the partition function of the theory $T_{\Delta}$, it obeys the following $q$-difference equation: $$\left( \hat z'' - q^{\frac k2} \, \hat z^k \right) \mathcal{Z}_{CS_k} =
\left( e^{ib \partial_{\tilde m}} - e^{i\pi b^2 k+2\pi bk\tilde m} \right) \mathcal{Z}_{CS_k} = 0 \,.$$ According to [\[whhlines\]](#whhlines){reference-type="eqref" reference="whhlines"}, this identity should be interpreted as a statement that at a 3d boundary with Chern-Simons term at level $k$ a 't Hooft operator with one unit of a magnetic flux is equivalent to a Wilson operator of electric charge $k$, $$H - e^{i\pi b^2 k} \, W^{k} \; \simeq \; 0 \,.$$ This is indeed correct, as one can easily verify by doing a direct path integral manipulation. Notice, it is important here that supersymmetric Chern-Simons theory lives on the boundary of the 4d space-time where Wilson and 't Hooft operators belong.

![Line operators in both $M$ and $T_M$.](bdyop2){#fig:MTMop width="5.2in"}

Most of our discussion in this section was based on interpreting $T_M$ as a boundary theory in the 4d $\mathcal{N}=2$ theory on the Coulomb branch of $T[\mathcal{C},\mathfrak{su}(2)]$, where $\mathcal{C}= \partial M$ is the geodesic boundary of $M$. This interpretation can be easily extended to 3-manifolds with "small" boundaries (*a.k.a.* cusps) and also to 3-manifolds with several boundary components. For example, in the latter case, each boundary component is a 2-dimensional Riemann surface $\mathcal{C}$ to which we associate either IR or UV limit of the 4d $\mathcal{N}= 2$ gauge theory $T[\mathcal{C}]$ depending on whether the boundary $\mathcal{C}$ is "big" or "small."

Within this framework, we could also look at a different class of line operators, corresponding to curves in a 3-manifold $M$ itself. In general, a 1-dimensional curve $\gamma_L$ inside a cobordism $M$ may have end-points on various boundary components of $M$, as shown in Figure [2](#fig:MTMop){reference-type="ref" reference="fig:MTMop"}. In order to find its interpretation in 3d $\mathcal{N}=2$ theory $T_M$, we recall that a point $p \in \mathcal{C}$ defines a surface operator in 4d $\mathcal{N}=2$ theory $T[\mathcal{C}]$, whereas the cobordism itself defines a domain wall between two different $\mathcal{N}=2$ theories in four dimensions (*cf.* Figure [\[fig:cobordism1\]](#fig:cobordism1){reference-type="ref" reference="fig:cobordism1"}). In four-dimensional space-time, a surface operator meets the domain wall over a 1-dimensional curve, which is precisely the line operator $L$ associated to $\gamma_L \subset M$, see Figure [2](#fig:MTMop){reference-type="ref" reference="fig:MTMop"}. In this description of $T_M$ as a theory on a duality wall, the line operator $L$ arises as an interface between two different surface operators.

The interplay between line operators on $M$ and line operators in 3d $\mathcal{N}=2$ theory $T_M$ can be easily motivated by thinking about $T_M$ as the effective theory $T[M,\mathfrak{su}(2)]$ obtained by reduction of the six-dimensional $(2,0)$ theory on a 3-manifold $M$. This is very similar to the correspondence between line operators in Liouville theory on $\mathcal{C}$ and line operators in 4d $\mathcal{N}=2$ theory $T[\mathcal{C},\mathfrak{su}(2)]$, where 6d theory again turns out to be very useful [@DMO; @AGGTV; @DGOT]. Indeed, six-dimensional $(2,0)$ theory contains two-dimensional surface operators. Upon compactification on a $d$-dimensional manifold $M_d$, the support of a surface operator can have the form $\gamma_L \times L$, where $\gamma_L \subset M_d$ is a 1-dimensional curve on $M_d$ and $L \subset {\mathbb R}^{6-d}$ is a line in the $(6-d)$ dimensional space-time where the theory $T[M_d,\mathfrak{su}(2)]$ lives. Surface operators of this form give rise to a large class of line operators in $T[M_d,\mathfrak{su}(2)]$ labeled by curves $\gamma_L$ on $M_d$.

[^1]: For example, in the context of knot complements, these operators are often denoted as $\hat m=e^{\hat u}$ and $\hat \ell=-e^{\hat v}$.

[^2]: We simply abbreviate $Z_{S^3_b}(T_{\Delta,\Pi_Z},\tilde m_Z)$ as $\mathcal{Z}(\tilde m_Z)$.
