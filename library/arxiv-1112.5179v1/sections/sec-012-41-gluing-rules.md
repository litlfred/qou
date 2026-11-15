---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-012-41-gluing-rules
section_title: "Gluing rules"
section_number: 4.1
pages: 22-25
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.997
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:rules label="sec:rules"}

Let's begin by recalling the gluing rules of [@DGG] for theories $T_M$. To construct $T_M$, we must choose an oriented 3-manifold $M$, an ideal triangulation $M = \bigcup_{i=1}^N\Delta_i$ of $M$ (which doesn't matter in the end), and a polarization $\Pi$ for the symplectic space $\mathcal{P}_{\partial M}$ of flat connections on the boundary $\partial M$ (which does matter).

The choice of polarization was described carefully in Section 2 of [@DGG], and we recall a few facts about it here. Physically, if we think of $T_M$ as a 3d boundary condition for a 4d $\mathcal{N}=2$ SCFT $T[\partial M]$, the polarization specifies how to couple $T_M$ to bulk 4d degrees of freedom. In practice, for components of $\partial M$ that are triangulated by faces of tetrahedra $\Delta_i$, the polarization $\Pi$ involves a choice of independent external edges to which are associated canonically conjugate "position" and "momentum" coordinates on $\mathcal{P}_{\partial M}$. For components of $\partial M$ that are torus cusps, coming from vertices of ideal tetrahedra, a polarization corresponds to a basis of canonically conjugate "A and B cycles" on the torus. We will see both of these cases appearing in examples later on.

Suppose then that we are given $M$, $\{\Delta_i\}_{i=1}^N$, and $\Pi$. To find $T_M$:

1.  The semi-classical phase space $\mathcal{P}_{\partial\Delta_i}$ of each tetrahedron $\Delta_i$ is described by three logarithmic edge parameters $Z_i,Z_i',Z_i''$ as in Figure [\[fig:tet\]](#fig:tet){reference-type="ref" reference="fig:tet"}, with a (quantum-corrected) constraint

    $$Z_i + Z_i'+Z_i'' = i\pi + \hbar/2\, \label{Phbar}$$

    and a symplectic structure $\Omega_i = \frac{1}{\hbar} dZ_i\wedge dZ_i'$. To each tetrahedron $\Delta_i$, in its "canonical" polarization $\Pi_i\equiv \Pi_{Z_i}$ with position and momentum $(X_i;P_i)=(Z_i;Z_i'')$, associate the tetrahedron theory $T_{\Delta_i,\Pi_i}$ as in [\[tetthy\]](#tetthy){reference-type="eqref" reference="tetthy"}. It has a $U(1)$ flavor symmetry, whose twisted mass parameter should be thought of as the position $Z_i$.

2.  Form a product theory $T_{\{\Delta_i\},\{\Pi_i\}}=T_{\Delta_1,\Pi_1}\otimes\cdots\otimes T_{\Delta_N,\Pi_N}$. This corresponds to the collection of tetrahedra $\{\Delta_i\}$ with the natural product polarization $\Pi_1\times\cdots \times \Pi_N$ on the product phase space $\mathcal{P}_{\partial\Delta_1}\times\cdots\times \mathcal{P}_{\partial\Delta_N}$. The theory has $U(1)^N$ flavor symmetry, with each independent twisted mass corresponding to a position coordinate $Z_i$.

3.  []{#step3 label="step3"} Choose a new polarization $\widetilde\Pi$ on the product phase space $\mathcal{P}_{\partial\Delta_1}\times\cdots\times \mathcal{P}_{\partial\Delta_N}$ such that

    -   it is compatible with the final desired polarization $\Pi$ for $\partial M$ (*i.e.* the positions and momenta in $\Pi$ are also positions and momenta in $\widetilde\Pi$); and

    -   the edge coordinates $C_I$ for all internal edges in the triangulation of $M$ are positions in $\widetilde\Pi$.

        [^1]

    This is possible by a classic result of [@NZ].

4.  Write $\widetilde\Pi = g\cdot \{\Pi_i\}$, where $g$ is an affine symplectic transformation,

    $$g\;\in\; Sp(2N,{\mathbb Z})\ltimes \big[(i\pi{\mathbb Z})^{2N}\times (\tfrac\hbar2{\mathbb Z})^{2N}\big]\,, \label{ggen}$$

    and act on the product theory $T_{{\Delta_i},\{\Pi_i\}}$ with $g$ as in Sections [\[sec:Sp\]](#sec:Sp){reference-type="ref" reference="sec:Sp"}--[\[sec:aff\]](#sec:aff){reference-type="ref" reference="sec:aff"} to obtain

    $$T_{\{\Delta_i\},\tilde\Pi}\,=\,g\circ T_{\{\Delta_i\},\{\Pi_i\}}\,.$$

    This theory still has a $U(1)^N$ flavor symmetry, but the twisted mass parameters now correspond to position coordinates on $\mathcal{P}_{\partial M}$ and to internal edge coordinates $C_I$.

5.  []{#step5 label="step5"} Add a superpotential $\mathcal{W}= \sum_I \mathcal{O}_I$ to $T_{\{\Delta_i\},\tilde\Pi}$ that breaks the $U(1)$ symmetries associated to the internal edges $I$. This operation is the gauge-theory equivalent of symplectic reduction. We obtain a UV Lagrangian description of the theory $T_M$, which has a global symmetry group $U(1)^{\frac12\dim \mathcal{P}_{\partial M}}$ left over. The twisted mass of each $U(1)$ is a position coordinate in the polarization $\Pi$ for $\mathcal{P}_{\partial M}$.

Two points here deserve further clarification. First, for defining a theory $T_M$ on ${\mathbb R}^3$, the affine shifts in [\[ggen\]](#ggen){reference-type="eqref" reference="ggen"} were irrelevant. In the context of the index, however, the theory is put on an $S^2\times S^1$ geometry, in the presence of magnetic flux. Then the affine shifts by $i\pi$ and $\hbar/2$ are related to $F$ and $R$ assignments, respectively, as discussed in Section [\[sec:aff\]](#sec:aff){reference-type="ref" reference="sec:aff"}. In order to see both shifts by $i\pi$ and $\hbar/2$ in the geometric description of phase spaces such as $\mathcal{P}_{\partial\Delta_i}$ and $\mathcal{P}_{\partial M}$, one must include a few $\hbar$ corrections in the relations among classical coordinates, as in [\[Phbar\]](#Phbar){reference-type="eqref" reference="Phbar"}. In the closely related context of analytically continued Chern-Simons theory, these semi-classical corrections were studied systematically in [@Dimofte-QRS]. The basic rule--of--thumb is that every $i\pi$ must be accompanied by an $\hbar/2$. Hence for gauge theory on $S^2\times S^1$ this means that every shift of R-charge $\sigma^R$ is coupled to a shift of fermion number $\sigma^F$.

Second, one might recall from [@DGG] that it was sometimes necessary to refine a given triangulation of $M$ in order to properly define the theory $T_M$. This is because the operators $\mathcal{O}_I$ that one adds to the superpotential may not exist when triangulations are too coarse. (For example, the theory of the figure-eight knot complement built from two tetrahedra suffered from this problem.) For purposes of calculating the index $\mathcal{I}_M$, such refinements of triangulation are not necessary. The index is insensitive to superpotential terms, aside from the simple fact that they break some flavor symmetry. Thus, when computing an index, we can often use unrefined, "hard" triangulations and just break flavor symmetries by hand, following the rules of Section [\[sec:W\]](#sec:W){reference-type="ref" reference="sec:W"}.

Now, translating the gluing rules for $T_M$ to gluing rules for the index, and taking into account the preceding remarks, we arrive at the following combinatorial construction of $\mathcal{I}_M$. Let's again suppose that we have a manifold $M$, a triangulation $\{\Delta_i\}$, and a polarization $\Pi$ for $\mathcal{P}_{\partial M}$. Then:

1.  To each tetrahedron $\Delta_i$ with polarization $\Pi_i$, associate a tetrahedron index $\mathcal{I}_{\Delta_i}(m_i,e_i)$ defined by [\[Imetet\]](#Imetet){reference-type="eqref" reference="Imetet"}. (We work in a charge basis, and also suppress the dependence on $q$.)

2.  Form the product

    $$\mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}(m,e) = \mathcal{I}_{\Delta_1}(m_1,e_1)\times\cdots\times \mathcal{I}_{\Delta_N}(m_N,e_N)\,.$$

    Now $m$ and $e$ are charge vectors of length $N$, and we can set $\gamma = {m \choose e}$.

3.  Choose a polarization $\widetilde\Pi$ for the product phase space $\mathcal{P}_{\partial\Delta_1}\times\cdots\times\mathcal{P}_{\partial\Delta_N}$ as in Step [\[step3\]](#step3){reference-type="ref" reference="step3"} above. It is related to the obvious product polarization via an affine symplectic transformation $g$. Decompose $g$ as a product $g = \sigma(\alpha)\,g_{Sp}$, where $g_{Sp}\in Sp(2N,{\mathbb Z})$ and $\sigma(\alpha) =\sigma^R(\alpha)\sigma^F(\alpha)$, $\alpha\in {\mathbb Z}^{2N}$, is an affine shift of position and momentum coordinates by $(i\pi+\tfrac\hbar2)\alpha$. (As noted above, shifts by $i\pi$ will always be coupled with shifts by $\hbar/2$.)

4.  Apply the above affine symplectic transformation to the product index, following Sections [\[sec:Sp\]](#sec:Sp){reference-type="ref" reference="sec:Sp"}--[\[sec:aff\]](#sec:aff){reference-type="ref" reference="sec:aff"}. Using the notation $\gamma = {m\choose e}$, we obtain

    $$\begin{aligned}
     \mathcal{I}_{{\Delta_i},\tilde\Pi}(m,e) &= \big[\sigma^R(\alpha)\,\sigma^F(\alpha)\,g_{Sp}\big]\circ \mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}(m,e) \notag \\
     &= \big(-q^{\frac12}\big)^{\langle \alpha,\gamma\rangle} \mathcal{I}_{\{\Delta_i\},\{\Pi_i\}}\big(g_{Sp}^{-1}\,\gamma\big)\,. \label{Iprod2}
     
    \end{aligned}$$

5.  Finally, break the flavor symmetries corresponding to internal edges of the triangulation. In the polarization $\widetilde\Pi$, each independent internal edge coordinate $C_I$ corresponds to a distinct electric charge $e_I$. Then, according to Section [\[sec:W\]](#sec:W){reference-type="ref" reference="sec:W"}, we find

    $$\mathcal{I}_{M,\Pi}(m',e')\,=\, \sum_{e_I\in {\mathbb Z}} q^{\Sigma_Ie_I}\, \mathcal{I}_{{\Delta_i},\tilde\Pi}(m,e)\Big|_{m_I\,=\,0}\,, \label{indsum}$$

    where the sum is over all internal-edge charges $e_I$, and we set all conjugate magnetic charges $m_I$ to zero. The extra factor of $q^{\Sigma_Ie_I}$ comes from the R-charge correction discussed in Section [\[sec:W\]](#sec:W){reference-type="ref" reference="sec:W"}, using the fact that our R-charge assignment for tetrahedron theories was $R_\phi = R_{\rm vac} = 0$.

In the end, we obtain an index $\mathcal{I}_M$ that depends on $\tfrac12\dim \mathcal{P}_{\partial M}$ electric charges $e'$ and $\tfrac12\dim \mathcal{P}_{\partial M}$ magnetic charges $m'$. They correspond directly to the $\tfrac12\dim\mathcal{P}_{\partial M}$ $U(1)$ flavor symmetries of the theory $T_M$.

The sum [\[indsum\]](#indsum){reference-type="eqref" reference="indsum"} typically converges, in the sense that only finitely many terms are necessary for calculating $\mathcal{I}_{M,\Pi}(m',e')$ to any desired order in $q$. Physically, the convergence of the sum is directly related to the existence of unconstrained chiral operators $\mathcal{O}_I$ that can be added to the superpotential of $T_{\{\Delta_i\},\tilde\Pi}$ to obtain $T_M$. (This statement will become clearer in Section [\[sec:tent\]](#sec:tent){reference-type="ref" reference="sec:tent"}.) In particular, when using a refined, "easy" triangulation so that all operators $\mathcal{O}_I$ exist, the sum should always converge. In practice, for an index computation, it actually appears that the only triangulations to be avoided are those with univalent internal edges --- *e.g.* edges resulting from gluing two adjacent sides of a single tetrahedron together. Such triangulations are automatically "hard"; but more seriously, they fail to describe the moduli space of flat connections on $M$ (*cf.* [@Dunfield-Mahler], Sec. 10.3, and [@Segerman-def; @DunGar]), and should never be expected to produce the correct theory $T_M$ or its index.

[^1]: It may be useful to recall here that these internal edge coordinates are sums of edge coordinates $Z_i,Z_i',Z_i''$ of individual tetrahedra that come together to form an internal edge (the same holds for external edges); and all internal edge coordinates commute with all external coordinates on $\mathcal{P}_{\partial M}$.
