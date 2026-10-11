---
doc_id: arxiv-math-ph-0012035v3
doc_title: "arXiv:math-ph/0012035v3 16 Jan 2002"
section_id: sec-017-31-two-dimensional-yang-mills-theory
section_title: "Two-dimensional Yang-Mills theory"
section_number: 3.1
pages: 35-41
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.98
---
There is a huge literature on the subject of the two-dimensional Yang-Mills theory approaching it from different points of view. One of the latest papers is \[AK00\], where a list of references to earlier papers is given. Two-dimensional Yang-Mills theory is a specific theory. From the dynamical point of view it is almost trivial---there are no local degrees of freedom, as a standard canonical analysis indicates. In fact it is "semi-topological" field theory, i.e. roughly it only describes combinatorial/topological phenomena and surface areas.

There are lot of important and interesting aspects in two-dimensional Yang-Mills theory. One of them is the issue of determination of "physical" observables---Wilson loops ([\[TrPexp\]](#TrPexp){reference-type="ref" reference="TrPexp"}). Calculation of the Wilson loops $W_R(C)$ in two-dimensional Yang-Mills theory can be facilitated by the use of the non-Abelian Stokes theorem.

A nice feature of (Euclidean) two-dimensional Yang-Mills gauge theory defined by the action $$S_{\rm 2dYM}(A)
    =\frac{1}{4}\int_M F_{AB}^a(A) F^{a\,AB}(A) \sqrt{g}\,d^2x,
    \qquad
    A,B=1,2,
    \label{YMS}$$ is the possibility to recast the action, and next, and more importantly, the whole partition function to the form $$Z=\int DF\,e^{-S_{\rm 2dYM}(F)},
    \label{YMZ}$$ where now $F$ is an independent field, and the action $S_{\rm 2dYM}$ is of the same form as the original Eq.[\[YMS\]](#YMS){reference-type="ref" reference="YMS"} but this time without $A$ dependence.

Let us now consider "physical" observables, i.e. Wilson loops. Confronting the partition function [\[YMZ\]](#YMZ){reference-type="ref" reference="YMZ"} with the form of the Wilson loop transformed by the non-Abelian Stokes theorem to a surface expression [\[op.NAST\]](#op.NAST){reference-type="ref" reference="op.NAST"} we can see that a kind of a Gaussian functional integral emerges. For an Abelian theory, we would exactly obtain an easy Gaussian functional integral, but in a non-Abelian case we should be more careful because $\cal F$ is a path-dependent object. The fact that $\cal F$ is path-dependent can be ignored in the case of a single loop due to the commutativity of the infinitesimal surface integrals (see below). Since, accordingly to the non-Abelian Stokes theorem $$W_R(C)={\rm Tr}_R{\cal P}\exp{\left(i\int_S
{\cal F}\sqrt{g}\,d^2x\right)},$$ where ${\cal F=F}_{12}$. For the expectation value $$\left<W_R(C)\right>
=Z^{-1}\int DF\exp{\left(-S_{\rm 2dYM}\right)}W_R(C),$$ we obtain (\[Bro90\]) $$\begin{aligned}
\left<W_R(C)\right>
&\propto&
\int DF\exp{\left(-\frac{1}{2}\int_M F^aF^a
\sqrt{g}\,d^2x\right)}
{\rm Tr}_R{\cal P}\exp{\left(i\int_S
F\sqrt{g}\,d^2x\right)}
\nonumber
\\
&=&
\int \prod_{x\in M\backslash S}
dF(x)\exp{\left(-\frac{1}{2}\int_{M\backslash S}
F^aF^a\sqrt{g}\,d^2x\right)}
\nonumber
\\
&&
\cdot{\rm Tr}_R{\cal P}\int \prod_{x\in S}dF(x)
\exp{\left[i\int_S \left(-\frac{1}{2}F^aF^a
+iF^aT^a\right)\sqrt{g}\,d^2x\right]}
\nonumber
\\
&\propto&
{\rm Tr}_R
\exp{\left(-\frac{1}{2}T^aT^a\int_S 
\sqrt{g}\,d^2x\right)}.
\nonumber
\end{aligned}$$ Thus, finally $$\left<W_R(C)\right>
={\rm Tr}_R\exp{\left[-\frac{1}{2}C_2(R)S\right]}
=\dim{R}\exp{\left[-\frac{1}{2}C_2(R)S\right]},$$ where $$S=\int_S\sqrt{g}\,d^2x,$$ and $$T^aT^a=C_2(R),\qquad
{\rm Tr}_RI=\dim{R}.$$ In the case of $n$ non-overlapping regions $\{S_i\}$, $i=1,\ldots,n$, $C_i=\partial S_i$, $S_i\cap S_j=\emptyset$ for $i\neq j$, and $n$ irreducible representations $R_i$ of the group $G$ with the generators $T_i$, we immediately obtain, literally repeating the last derivation, the formula for the expectation value of the product of the $n$ Wilson loops $$\left<\prod_{i=1}^n W_{R_i}(C_i)\right>
=\prod_{i=1}^n\dim{R_i}
\exp{\left[-\frac{1}{2}C_2(R_i)S_i\right]}.$$ The case of the overlapping regions $\{S_i\}$ is a bit more complicated \[Bro90\]. First of all, one has to decompose the union of all regions $\{S_i\}$, $\partial S_i=C_i$ into a disjoint union of connected, i.e. not intersected by the loops, regions $\{S_\alpha\}$. Each loop $C_i$ is next deformed into an equivalent loop $C_i'$, which is a product of "big" (not infinitesimal) lassos independently (a lasso per a region) covering each connected region $S_{\alpha_i}$, $S_{\alpha_i}=S_\alpha\cap S_i$ ($S_{\alpha_i}\in \{S_\alpha\}$). The lassos coming from the different loops $C_i'$ but covering the same connected region $S_\alpha$ should necessarily be arranged in such a way to enter the region $S_\alpha$ at the same base point $O_\alpha$. Consequently, the connected region $S_\alpha$, $S_\alpha\subset S_{i_1}\cap\ldots\cap S_{i_k}$, $i\leq k\leq n$, can be covered with the $k$ identical copies of the net of "small" (infinitesimal) lassos. Every Gaussian functional integration with respect to the infinitesimal area $\delta S$ enclosed by an infinitesimal lasso can be easily performed yielding $$\exp{\left(-\frac{1}{2}\delta S\,T_\alpha^2\right)},
    \label{YMexp}$$ where $$T_\alpha=\sum_{i\in\alpha} T_i,
\qquad
T_i=I\otimes\dots\otimes T_i\otimes\ldots\otimes I.$$ Integration with respect to the consecutive infinitesimal areas gives the terms of the form [\[YMexp\]](#YMexp){reference-type="ref" reference="YMexp"}. Since $T_\alpha$ is a generator of $\bf g$ in a product representation $R_\alpha$, $R_\alpha=R_{i_1}\otimes\ldots\otimes R_{i_k}$, $T_\alpha^2$ is a Casimir operator. Accordingly, [\[YMexp\]](#YMexp){reference-type="ref" reference="YMexp"} commutes with the product of the parallel-transport operators acting in the product representation $R_\alpha$. Since the products in the pairs connect every infinitesimal area $\delta S$ with the base point $O_\alpha$, they cancel each other. This fact means that the integral with respect to the whole region $S_\alpha$ is given only by the infinite product of the terms [\[YMexp\]](#YMexp){reference-type="ref" reference="YMexp"} and reads $$M_\alpha=\exp{\left(
    -\frac{1}{2}S_\alpha T_\alpha^2\right)}.
    \label{YMM}$$ The full expectation value of the $n$ loops $\{C_i\}$ consists of the trace of a product of $M_\alpha$-blocks [\[YMM\]](#YMM){reference-type="ref" reference="YMM"} joined with the parallel-transport operators, which are remnants of the primary decomposition of the loops. These joining curves enclose zero areas, and can be deformed into points (without destroying $M_\alpha$-blocks) giving some "linking" operators $L_\alpha$. An operator $L_\alpha$ is of a very simple form, namely it is a product of the Kronecker deltas, which contract indices belonging to the same representation but to different $M$'s. Thus, $L$ causes that the matrix multiplication of $M$'s is performed in a prescribed order in each representation sector independently. In other words, $M$ mixes, with some weights, indices of different representations (braiding), whereas $L$ sets the order of the matrix multiplications in a representation sector. $M$ depends on the metric (area of $S$) and group-theoretic quantities, whilts the concrete form of $L$ depends on the topology of the overlaps. Thus, the expectation value of the product of the $n$ Wilson loops is finally given by $$\left<\prod_{i=1}^n W_{R_i}(C_i)\right>
=\prod_\alpha L_\alpha M_\alpha.$$ This analysis is a bit simplified and shortened but gives the flavor of the power of the non-Abelian Stokes theorem in practical instances.

## Three-dimensional topological quantum field theory

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
