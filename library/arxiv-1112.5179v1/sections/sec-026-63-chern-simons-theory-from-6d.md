---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-026-63-chern-simons-theory-from-6d
section_title: "Chern-Simons theory from 6d"
section_number: 6.3
pages: 65-68
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.994
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:6d label="sec:6d"}

As we argued in [@DGG], a three-dimensional $\mathcal{N}=2$ theory $T_M$ labeled by a 3-manifold $M$ can be thought of as the result of compactification of the six-dimensional $(2,0)$ theory of type $A_1$ on a 3-manifold $M$. Therefore, a 3d $\mathcal{N}=2$ theory $T_M$ in the space-time $S^1 \times S^2$ relevant to the index computation can be equivalently approached by studying the $A_1$ 6d theory that describes two coincident M5-branes on $S^1 \times S^2 \times M$.

This configuration of two five-branes on $S^1 \times S^2 \times M$ fits in a large web of dualities that connects a number of closely related systems studied in the literature. Here, we briefly discuss some of these dualities, providing a further piece of evidence for the interpretation of 3d index in terms of the full $SL(2,{\mathbb C})$ Chern-Simons theory (not just a holomorphic half of it).

In general, putting a 3d $\mathcal{N}=2$ theory $\mathcal{T}$ in different space-times with an $\Omega$-background allows one to associate different quantities (partition functions) to $\mathcal{T}$. Below we list several examples of such partition functions and the corresponding 3d space-times, illustrating their concrete form in a basic example of the tetrahedron theory $\mathcal{T}= T_{\Delta}$, which basically consists of a single chiral multiplet:

$$\begin{aligned}
S^1 \times S^2 &\; : \qquad \mathcal{I}[T_{\Delta}]  \; = \;
\prod_{r=0}^\infty \frac{1- q^{r+1}z^{-1}}{1-q^{r}\bar z^{-1}} \notag \\
\text{``solid torus''} \quad S^1 \times {\mathbb R}^2_{\hbar} &\; : \qquad \mathcal{Z}_{\text{vortex}} [T_{\Delta}] \; = \;
\prod_{r=0}^{\infty} (1 - q^{r +1} z^{-1}) \label{ZZZ} \\
\text{``ellipsoid''} \quad S^3_b \quad & \; : \qquad \mathcal{Z}_b [T_{\Delta}] \; = \; \prod_{r=0}^{\infty}
\frac{1 - q^{r+1}\, z^{-1}}{1 - ({}^Lq)^r ({}^Lz)^{-1}} \notag
\end{aligned}$$

where, as usual, the $\Omega$-deformation parameter is proportional to $\hbar$, and in the case of $S^3_b$ there are dual deformations proportional to $\hbar=2\pi ib$ and ${}^L\hbar = 2\pi i b^{-1}$. In all cases, $z$ is related to a fugacity for the flavor $U(1)$ symmetry (and ${}^Lz = z^{\frac{2\pi i}{\hbar}}$).

By comparing the expressions of these partition functions for $\mathcal{T}= T_{\Delta}$, the reader will immediately notice that both the index $\mathcal{I}[\mathcal{T}]$ and the ellipsoid partition function $\mathcal{Z}_{b} [\mathcal{T}]$ roughly contain two copies of the vortex partition function $\mathcal{Z}_{\text{vortex}} [\mathcal{T}]$. This observation has a simple heuristic explanation based on the geometry of the three-dimensional space-times that lead to these partition functions. Indeed, both a 3-sphere and $S^1 \times S^2$ consist of two copies of the solid torus glued together either "back-to-back" or with a twist, *i.e.* in a way where the A-cycle on the boundary torus of one copy is glued to the A-cycle on the boundary of the second copy, or to the dual B-cycle. These two ways of gluing solid tori produce $S^1 \times S^2$ and $S^3$, respectively, which in turn lead to the partition functions [\[ZZZ\]](#ZZZ){reference-type="eqref" reference="ZZZ"}.

::: wrapfigure
r2in ![image](D4D62){height="2.3in"}
:::

Another intuitive explanation of the relation between different partition functions [\[ZZZ\]](#ZZZ){reference-type="eqref" reference="ZZZ"} and Chern-Simons theory with complex gauge group $SL(2,{\mathbb C})$ can be seen directly in the system of two M5-branes supported on $S^3_b \times M$ or $S^1 \times D \times M$, where $D = S^2$ leads to the superconformal index and $D = {\mathbb R}^2_{\hbar}$ leads to the vortex partition function. In each case, it is convenient to use a dual description of this five-brane configuration by reducing it on a circle down to type IIA string theory. There are several choices on can consider, which depend on the choice of the "M-theory circle," and all of which are supposed to provide equivalent descriptions of the same physical system. For example, if a 3-manifold $M$ admits a circle action, then one can find a dual description of the five-brane system in terms of D4-branes wrapped on the quotient space $M/U(1)$.

In our discussion, the 3-manifold $M$ is generic[^1] and since the $S^1$ part of the 3d space-time is used in the definition of the 3d index, our only choice is to take the M-theory circle be a part of the $D$ or $S^3$ geometry. Luckily, all our 3d space-times in [\[ZZZ\]](#ZZZ){reference-type="eqref" reference="ZZZ"} admit such circle actions (aside from obvious isometries arising from the $S^1$ factor). In particular, the sphere $D = S^2$ relevant for the 3d index can be represented as a circle fibration, $$\begin{matrix}
S^1_{\rm M} & \to & S^2 \\
& & \downarrow \\
& & I
\end{matrix}$$ with two degenerate fibers at the end-points of the interval $I = [0,1]$. Therefore, if we identify the M-theory circle with $S^1_{\rm M}$, we can relate the original five-brane system on $S^1 \times S^2 \times M$ with the system of D4-branes stretched between two D6-branes, as shown in Figure [\[D4D6\]](#D4D6){reference-type="ref" reference="D4D6"}. In other words, the 3d index (= partition function of the five-brane theory on $S^1 \times S^2 \times M$) can be equivalently computed in a gauge theory that lives on the world-volume of the D4-branes, $$S^1 \times I \times M \,,$$ with suitable boundary conditions associated with the D6-branes at the end-points of the interval $I$. Note, upon this reduction to type IIA theory the angular momentum for the $U(1)$ rotation symmetry of $D = S^2$ (similarly for $D = {\mathbb R}^2$) becomes the instanton charge $k_{\text{inst}} = \frac{1}{16 \pi^2} \int_{I \times M} {\rm Tr \,}F \wedge F$ in the D4-brane gauge theory. One quick way to see this is to note that instantons in the D4-brane theory can be interpreted as D0-branes which, in turn, are precisely the Kaluza-Klein modes for the reduction on $S^1_{\rm M}$.

The resulting configuration of D4-branes ending on the D6-branes essentially comprises two (interacting) copies of the D6-D4 brane system studied in [@Wfiveknots], where it was argued that its partition function equals the partition function of analytically continued Chern-Simons theory, see also [@DGH]. In the present case, we have two such systems coupled together. We claim that these are precisely the two sectors ("holomorphic" and "anti-holomorphic") of the full $SL(2,{\mathbb C})$ Chern-Simons theory discussed in Section [\[sec:k0\]](#sec:k0){reference-type="ref" reference="sec:k0"}.

Moreover, the coupling constants in these two sectors are related precisely as in Section [\[sec:k0\]](#sec:k0){reference-type="ref" reference="sec:k0"}. Indeed, in a single D6-D4 brane system the coupling constant of the analytically continued $SU(2)$ Chern-Simons theory is identified with the fugacity for the instanton charge $k_{\text{inst}}$. If we denote this fugacity by $q = e^{\hbar}$, then the fugacity of the second D6-D4 brane system is equal to $\tilde q = e^{- \hbar} = q^{-1}$ due to the opposite orientation. This is exactly the relation between coupling constants $t = - \tilde t = is$ that we encountered in Section [\[sec:k0\]](#sec:k0){reference-type="ref" reference="sec:k0"}, with the identification $\hbar = \frac{4 \pi}{s}$. In fact, we can even observe that the $\rho$ symmetry of Section [\[sec:kappa\]](#sec:kappa){reference-type="ref" reference="sec:kappa"}, lifted to the D6-D4 system, simply looks like a reflection of the geometry that exchanges the holomorphic and anti-holomorphic sectors, and the two fugacities $q$ and $\tilde q$.\
\

[^1]: *I.e.*, we do not make any special assumptions about isometries of $M$.
