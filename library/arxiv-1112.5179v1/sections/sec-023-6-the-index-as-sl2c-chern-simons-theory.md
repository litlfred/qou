---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-023-6-the-index-as-sl2c-chern-simons-theory
section_title: "The index as SL(2,C) Chern-Simons theory"
section_number: 6
pages: 56-58
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:CS label="sec:CS"}

Throughout the preceding sections, there have been various hints that the index $\mathcal{I}_M(m,e;q)$ of a theory $T_M$ may have some relation to complex Chern-Simons theory on $M$ itself, *i.e.* Chern-Simons theory with complex gauge group $SL(2,{\mathbb C})$. For example, the constructions of $T_M$ and $\mathcal{I}_M$ involve choosing a polarization on the phase space $\mathcal{P}_{\partial M}$, and this is precisely the phase space of complex Chern-Simons theory on a 3-manifold $M$ with boundary [@Wit-Jones; @Witten-cx]. In addition, the flat $SL(2,{\mathbb C})$ connections in the bulk of $M$, which project to the Lagrangian submanifold $\mathcal{L}_M$,

$$\begin{aligned}
 \mathcal{L}_M &\;=\;\{\text{flat $SL(2,{\mathbb C})$ connections on $\partial M$ that extend to $M$}\} \notag \\
\cap\;\; & \notag \\
\mathcal{P}_{\partial M} &\;=\;\{\text{flat $SL(2,{\mathbb C})$ connections on $\partial M$}\}\,, \notag
\end{aligned}$$

correspond to spaces of SUSY vacua for $T_M$ [@DGH; @DGG]; and these flat connections on $M$ are the classical solutions to Chern-Simons theory. Moreover, we saw in Sections [\[sec:TM\]](#sec:TM){reference-type="ref" reference="sec:TM"} and [\[sec:3d4d\]](#sec:3d4d){reference-type="ref" reference="sec:3d4d"} that a quantization of the Lagrangian's defining equations, $\hat\mathcal{L}_M$, provides difference operators that annihilate the index. This again is an expected property of Chern-Simons wavefunctions: the constraints describing classical solutions $(\mathcal{L}_M)$ become promoted to quantum operators $(\hat\mathcal{L}_M)$ that annihilate the quantum wavefunctions [@gukov-2003].

To be even more suggestive, consider the tetrahedron index in the electric fugacity basis [\[Iztet2\]](#Iztet2){reference-type="eqref" reference="Iztet2"}. Note that in the definition of the index as a partition function on $S^2\times S^1$, the parameter $q=e^\hbar$ is real, while $\zeta = e^{i\theta}$ is a pure phase. We can then recombine $m$ and $\theta$ into complex variables, as in Section [\[sec:T1\]](#sec:T1){reference-type="ref" reference="sec:T1"} :

$$Z = \frac{m}{2}\hbar+i\theta\,,\qquad \overline Z = \frac{m}{2}\hbar-i\theta\,, \label{tmZ}$$

or

$$z = e^Z = q^{\frac m2}\zeta\,,\qquad \overline z = e^{\overline Z}=q^{\frac m2}\zeta^{-1}\,; \label{tmz}$$

so that the tetrahedron index takes the form

$$\mathcal{I}_\Delta(m;q,\zeta) = \mathcal{I}_\Delta(z,\overline z;q) = \prod_{r=0}^\infty \frac{1-q^{r+1}z^{-1}}{1-q^r\,\overline{z}^{-1}}\,.$$

If we define $\mathcal{Z}_\Delta(z;q)\equiv\prod_{r\geq 1} (1-q^r z^{-1})$ for $|q|<1$, and allow ourselves the "Fock space reorganization" $\prod_{r\geq 1}(1-q^{-r}z)=\prod_{r\geq 0}(1-q^{r}z)^{-1}$, we would then have an index

$$\mathcal{I}_\Delta(z,\overline z;q) \;\text{``}\!=\!\text{''}\; \mathcal{Z}_\Delta(z;q)\,\mathcal{Z}_\Delta(\overline z;q^{-1})\,, \label{Dfact}$$

factorized into identical holomorphic and antiholomorphic pieces.

Such a factorization is familiar from the studies of $SL(2,{\mathbb C})$ Chern-Simons partition functions in [@gukov-2003; @DGLZ; @Wit-anal]. More generally, the physical Chern-Simons partition function on a 3-manifold $M$ would be a sum over classical flat connections $\alpha$ with fixed boundary conditions $x$,

$$\mathcal{Z}^{\rm CS}_M(x,\overline x;q)\; = \; \sum_{\alpha}n_{\alpha\bar\alpha}\,\mathcal{Z}_M^\alpha(x;q)\,\mathcal{Z}_M^{\bar \alpha}(\overline x;q^{-1})\,, \label{CSfact}$$

and with $n_{\alpha\bar\alpha}$ real and diagonal.

[^1] In the case of the tetrahedron, there is a unique flat connection at fixed boundary condition $x=z$, and so a single term in [\[CSfact\]](#CSfact){reference-type="eqref" reference="CSfact"}. Note that [\[CSfact\]](#CSfact){reference-type="eqref" reference="CSfact"} has a symmetry under complex conjugation and exchange of $q$ and $q^{-1}$, which looks like $\rho$ symmetry [\[kind\]](#kind){reference-type="eqref" reference="kind"} for the index.

Our goal in this section is to make the relation between $SL(2,{\mathbb C})$ Chern-Simons theory and the index as precise as possible. There actually exist several inequivalent quantizations of complex Chern-Simons theory --- corresponding to different real symplectic structures on the complex phase space $\mathcal{P}_{\partial M}$ --- and we will see that one special choice is related to the generalized index $\mathcal{I}_M(m;q,\zeta)$. An interesting open question is to understand what the other quantizations might mean. In Section [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}, we will give a "top-down," qualitative view of the equivalence between Chern-Simons theory and the index by considering the theory of M5-branes in the geometry $S^1\times S^2\times M$ and applying various known dualities.

[^1]: Explicit expansions of this type, not for indices but for the closely related ellipsoid partition functions of some theories in class $\mathcal{R}$, have recently appeared in [@Pasquetti-fact].
