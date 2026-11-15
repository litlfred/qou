---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-018-32-three-dimensional-topological-quantum-field-t
section_title: "Three-dimensional topological quantum field theory"
section_number: 3.2
pages: 38-41
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.975
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
Topological quantum field theory has recently become a fascinating and fashionable subject in mathematical physics. At present, main applications of topological field theory are in mathematics (topology of low-dimensional manifolds) rather than in physics. Its application to the issue of classification of knots and links is one of the most interesting. To approach this problem one usually tries to somehow encode the topology of a knot/link . As was first noted by Witten \[Wit89\], the problem can be attacked by means of standard theoretical physics techniques of quantum field theory. In particular, using three-dimensional Chern-Simons gauge theory one can derive not only all the well-known polynomial invariants of knots and links but many of their generalizations as well. Most authors working in the topological field theory description of polynomial invariants follow Witten's original approach, which relies heavily on the underlying conformal-field-theory structure. There is also a genuinely three-dimensional covariant approach advocated in its perturbative version in \[Smo89\] and \[CGM90\] using the non-Abelian Stokes theorem in its operator formulation. We shall sketch an application of the non-Abelian Stokes theorem to a genuinely three-dimensional, non-perturbative, covariant path-integral approach to *polynomial invariants* of knots and links in the framework of (topological) quantum Chern-Simons gauge field theory.

To begin with, we introduce the classical topological Chern-Simons action on the three-dimensional sphere $S^3$ $$\begin{aligned}
    S_{\rm CS}
    &=&
    {k\over4\pi}\int_{S^3}{\rm Tr}\left(A\wedge
    dA+{2\over3}A\wedge A\wedge
    A\right)
    \nonumber\\
    &=&
    {k\over4\pi}\int_{S^3}d^3x\,
    \varepsilon^{ijk}{\rm Tr}\left(A_i\partial_j
    A_k+{2\over3}A_i A_j A_k\right),
    \label{CSS}
\end{aligned}$$ where $k\in{\bf Z}^\pm$. The use of Eq.[\[CSS\]](#CSS){reference-type="ref" reference="CSS"} is not obligatory. One could as well choose the action of the so-called $BF$-theory $$S_{\rm BF}={k\over4\pi}\int_{{S}^3}d^3x\,
    \varepsilon^{ijk}{\rm Tr}(B_i F_{jk}),
    \label{SBF}$$ where $B_i=B_i^a(x)T^a$ is an auxiliary gauge field, and now $k\in{\bf R}^\pm$.

To encode the topology of a link ${\cal L}=\{C_i\}$ into a path integral we introduce an auxiliary one-dimensional topological field theory (topological quantum mechanics) in an external gauge field $A$, living on the corresponding loop $C_i$. The classical action of this theory is chosen in the form (see, Eq.[\[clas.L\]](#clas.L){reference-type="ref" reference="clas.L"}) $$S_{C_i}(A)
    =i\oint_{C_i}dt\,\bar{z}_iD_t z_i,
    \label{CSo}$$ where the multiplet of scalar fields $\bar{z}_i$, $z_i$ transforms in a irreducible representation $R_i$. The partition function corresponding to [\[CSo\]](#CSo){reference-type="ref" reference="CSo"} has the following standard form $$Z_i(A)=\int D^2z_i\exp\left[iS_{C_i}(A)\right].$$ It is obvious that the observables $S_{C_i}(A)$ are akin to the Wilson loops.

We define the topological invariant of the link ${\cal
L}$ as the (normalized) expectation value $$\left<\prod_iZ_i(A)\right>
    \equiv\left[\int d\mu\exp(iS)\right]^{-1}
    \int d\mu\exp(iS)\prod_iZ_i(A),
    \label{CSvac}$$ where $S$ consists of $S_{\rm CS}$ plus quantum terms, and the measure should also contain the auxiliary fields. We can calculate [\[CSvac\]](#CSvac){reference-type="ref" reference="CSvac"} recursively, using the so-called *skein relations*. Thus, our present task reduces to the derivation of the corresponding skein relation. To this end, we consider a pair of loops, say $C_1$ and $C_2$, where a part of $C_1$, forming a small loop $\ell$ ($\ell=\partial N$), is wrapped round $C_2$. In other words, $C_2$ pierces $N$ at a point $P$.

Such an arrangement can be interpreted as a preliminary step towards finding the corresponding monodromy matrix **M**. Having given the loop $\ell$ we can utilize the non-Abelian Stokes theorem (actually the Abelian Stokes theorem for [\[CSo\]](#CSo){reference-type="ref" reference="CSo"}) in its holomorphic version, obtaining Eq.[\[top.act.\]](#top.act.){reference-type="ref" reference="top.act."}. In general position, $N$ and $C_2$ can intersect in a finite number of points, and the contribution to the path-integral coming from these points can be explicitly calculated. We replace the curvature in [\[top.act.\]](#top.act.){reference-type="ref" reference="top.act."} by the functional derivative operator $$F_{ij}^a(x)\longrightarrow{4\pi\over
ik}\varepsilon_{ijk}{\delta\over\delta
A_k^a(x)}.$$ This substitution yields an equivalent expression provided the order of terms in [\[CSvac\]](#CSvac){reference-type="ref" reference="CSvac"} is such that the functional derivative can act on $S_{\rm CS}$ producing $F$. Using formal translational invariance of the product measure $DA$, and functionally integrating by parts in [\[CSvac\]](#CSvac){reference-type="ref" reference="CSvac"} with respect to $A$, we obtain, for each intersection point $P$, the *monodromy operator* $$M=\exp\left[{4\pi\over ik}(\bar z_1T_1^a z_1)
    (\bar z_2 T_2^a z_2)(P)\right].
    \label{CSM}$$ To calculate the *matrix elements* of [\[CSM\]](#CSM){reference-type="ref" reference="CSM"} one utilizes the following scalar product $$(f,g)={1\over2\pi i}\int
fg\exp(\bar z z)d\bar z dz.$$ This kind of the scalar product is implicit in our derivations of the path integral. Expanding [\[CSM\]](#CSM){reference-type="ref" reference="CSM"} in a power series, multiplying with respect to this scalar product, and re-summing, we get the *monodromy matrix* $${\bf M}=(\bar z_1\bar z_2, M\,z_2z_1)
=\exp\left({4\pi\over ik}T_1^a\otimes T_2^a\right).$$ The square root of the monodromy matrix gives rise to the, so-called, braiding matrix $\bf B$ resposible for a proper form of skein relations, yielding knot/link invariants.
