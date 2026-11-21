---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-018-47-mutation-invariance-from-gauge-theory
section_title: "Mutation invariance from gauge theory"
section_number: 4.7
pages: 42-46
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:mutant label="sec:mutant"}

In this section, we begin to test the strength of the index as a topological invariant of 3-manifolds --- *i.e.* its ability to distinguish 3-manifolds from one another. We will specialize to the case of knot complements $M$, either in $S^3$ or in some closed 3-manifold $\overline M$, and consider the operation of mutation [@Conway-mutation]. To perform a mutation, the knot complement $M$ is cut along an $S^2$ that is punctured exactly four times by the knot, separating $M$ into two halves

[^1]

$M_1$ and $M_2$; then the halves are glued back together with a "$180^\circ$ rotation" along some axis of $S^2$, forming a new manifold $M_\mu$. More precisely, the rotation of $S^2$ interchanges two pairs of punctures. This is illustrated in Figure [1](#fig:mutation){reference-type="ref" reference="fig:mutation"} for the simplest topologically distinct mutant pair of knot complements.

![The Kinoshita-Terasaka (left) and Conway (right) knots, related by a nontrivial mutation operation.](mutation){#fig:mutation width="4.8in"}

It is famously known that mutation acts trivially on colored Jones polynomials, the $SU(2)$ Chern-Simons wavefunctions of knot complements [@MortonTraczyk] (see also [@StoimenowTanaka]). We have also mentioned several times that the index should correspond to a complex $SL(2,{\mathbb C})$ Chern-Simons wavefunction. Thus a natural expectation might be that the index is mutation invariant. We will prove this physically below, by using the $6d$ realization of theories $T_M$, and also by arguing that mutation is implemented by a 3d superpotential deformation that leaves the index untouched. First, however, we can do a simple check. The triangulations of the KT and Conway knot complements in Figure [1](#fig:mutation){reference-type="ref" reference="fig:mutation"} are easily found with the program `SnapPy` [@SnapPy]. In their simplest (non-univalent) form, they have 12 tetrahedra each, leading to an expression for the corresponding indices as 11-dimensional sums. Then we find, for example, that

[^2]

$$\mathcal{I}_{\rm KT}(0,0;q) = \mathcal{I}_{\rm Con}(0,0;q) = 1 + 6 q - 32 q^2 + O(q^3)\,. \label{ConKT}$$

If the indices $\mathcal{I}_{\rm KT}$ and $\mathcal{I}_{\rm Con}$ were to differ, they could only do so by a finite number of $q$-dependent normalizations --- since the colored Jones polynomial determines operators $\hat \mathcal{L}_M$, and these in turn fix the index up to $q$-dependent boundary conditions. Thus, evaluating the index even at $(m,e)=(0,0)$ as in [\[ConKT\]](#ConKT){reference-type="eqref" reference="ConKT"} is quite a nontrivial check of mutation invariance.

::: wrapfigure
r2.6in ![image](Mstretch){width="2.7in"}
:::

Now, let us proceed to the six-dimensional argument. Consider the six-dimensional $A_1$ theory on a three-manifold $M$, and identify a two-sphere $C=S^2$ in $M$ that intersects exactly four strands of codimension 2 regular defects. We will denote as $M_1$ and $M_2$ the two halves of $M$ joined along $C$. We can put a metric on $M$ that elongates a neighborhood of $C$ into a long cylinder of cross-section $C$ (Figure [\[fig:Mstretch\]](#fig:Mstretch){reference-type="ref" reference="fig:Mstretch"}). At low energy, the six-dimensional setup admits a simple four-dimensional description, as a four-dimensional $\mathcal{N}=2$ gauge theory on a segment, with boundary conditions $\mathcal{B}_1$ and $\mathcal{B}_2$ at the endpoints that are determined by the geometry of $M_1$ and $M_2$. The four-dimensional theory is $SU(2)$ gauge theory with $N_f=4$ fundamental hypermultiplets. In the far IR, the four-dimensional setup will flow back to $T_M$.

This cutting construction, of course, can be done for any surface $C$, but the four-punctured sphere is special. While for generic $C$ the four-dimensional theory has an $SU(2)$ flavor symmetry for each puncture, inherited from the flavor symmetry of codimension-$2$ defects in the six-dimensional theory, the $SU(2)$ $N_f=4$ theory has an $SO(8)$ flavor symmetry. The flavor symmetries with a six-dimensional origin compose an $SO(4) \times SO(4)$ block-diagonal subgroup of $SO(8)$. The remaining $16$ generators of $SO(8)$ are accidental IR symmetries that appear in the four-dimensional limit. As $T_M$ can be defined by the four-dimensional setup, the enhanced $SO(8)$ flavor symmetry has important consequences for $T_M$.

One important consequence is that any boundary condition $\mathcal{B}$ for $SU(2)$ $N_f=4$ theory sits in an $SO(8)$ orbit of boundary conditions $g\circ \mathcal{B}$, $g \in SO(8)$. In principle it is possible to imagine an $SO(8)$-invariant boundary condition. For example: set Dirichlet boundary conditions for the gauge fields, split the $16$ chiral fields in the hypermultiplets into sets $X^i$, $Y^i$, each in a vector representation of $SO(8)$ ($X^i$ and $Y^i$ are the top and bottom components respectively of the $8$ $SU(2)$ doublets), and then give Dirichlet b.c. to $X^i$ and Neumann b.c. to $Y^i$. However, we are not aware of a geometric realization for such a boundary condition. Boundary conditions $\mathcal{B}$ obtained from a generic six-dimensional configuration will typically break $SO(8)$ down to $SU(2)^4$, or even a smaller subgroup $H_\mathcal{B}$, and hence will sit in a non-trivial continuous family $SO(8)/H_{\mathcal{B}}$ of boundary conditions.

Although it will not be too important for us, it is simple to show that these exactly marginal deformations of an $\mathcal{N}=2$ supersymmetric boundary condition $\mathcal{B}$ are actually superpotential deformations. Indeed, they correspond to deformations of the boundary conditions for the hypermultiplets only, and can be implemented by adding superpotential terms at the boundary. The true space of exactly marginal deformations of $\mathcal{B}$ will be some complex manifold that locally is the complexification of $SO(8)/H_{\mathcal{B}}$. We do not have a good handle over the full space of exactly marginal deformations, but for our purpose $SO(8)/H_{\mathcal{B}}$ is sufficient.

Notice that even if $\mathcal{B}$ has a six-dimensional realization as some cobordism with a single non-empty boundary $C\,(\times {\mathbb R}^3)$, generically the boundary condition $g \circ \mathcal{B}$ may not have such a realization. There is an exception, though: if $g$ is an $SO(8)$ rotation that permutes the four $SU(2)$'s among themselves, then $g \circ \mathcal{B}$ can be also realized by the same cobordism as $\mathcal{B}$, with the four punctures suitably permuted. There is an obvious example: the diagonal matrix $(1,1,1,-1,1,1,1,-1)$ acts as a reflection in each $SO(4)$, and therefore permutes the two $SU(2)$'s in each $SO(4)$. Thus we can find an $SO(8)$ rotation $\mu$ that simultaneously permutes any two distinct pairs of punctures. Then $\mathcal{B}$ and $\mu \circ \mathcal{B}$ are defined by two possibly inequivalent six-dimensional cobordisms, but are related by a continuous family of deformations that do not admit a simple six-dimensional definition.

Now, we can define a deformation $T^\mu_M$ of the 3d theory $T_M$ by taking four-dimensional $SU(2)$ $N_f=4$ gauge theory on the segment, with modified boundary conditions $\mathcal{B}_1$ and $\mu\circ \mathcal{B}_2$ at the endpoints. Clearly $T^\mu_M$ is the theory associated to a new three-manifold $M_\mu$, obtained by permuting the two pairs of strands across $C$. This is the definition of a mutation of $M$. But the theories $T_M$ and $T^\mu_M$ are related by a continuous family of exactly marginal deformations, hence must have the same index!

This is the main conclusion of this section. Next, we would like to recast it in a language that makes use only of the definition of $T_M$ through the gluing of tetrahedra, with no reference to the six-dimensional setup. We are after a continuous family of exactly marginal deformations of $T_M$, possibly including a subset $H_{\mathcal{B}_1} \backslash SO(8)/H_{\mathcal{B}_2}$ and modeled locally on the complexification of that locus. If $H_{\mathcal{B}_1}$ and $H_{\mathcal{B}_2}$ are $SU(2)^4$, the exactly marginal locus should be four-dimensional. Notice that in concrete examples, such exactly marginal deformations may be directly visible in the index, as chiral operators of $R$-charge $2$ and specific flavor charges under the flavor symmetries associated to the codimension two defects.

![Splitting $M = M_1\cup_C M_2$ along a 2-sphere $C$ to form two new geodesic boundaries, triangulated by faces of tetrahedra.](mutMC){#fig:mutMC width="5.7in"}

In order to proceed, we will assume that $M$ admits a triangulation that can be split along $C$ without cutting any tetrahedra. If we split along $C$, we will get triangulated versions of $M_1$ and $M_2$, each with a triangulated $C$ boundary component, $C_1$ and $C_2$; see Figure [2](#fig:mutMC){reference-type="ref" reference="fig:mutMC"}.

[^3]

Clearly, $C_1$ and $C_2$ are triangulated in the same way, and gluing $M_1$ and $M_2$ back along $C$ can be done by imposing a standard gluing constraint for each edge in the triangulation of $C$. So we can start from the theories $T_{M_1}$ and $T_{M_2}$ and implement the gluing constraints by adding superpotential terms $\mathcal{O}_E$, one for each edge $E$ of $C$. In a polarization where the images $E_1$ and $E_2$ of $E$ in $C_1$ and $C_2$ carry position edge variables, we can write $$\mathcal{O}_E =  \mathcal{O}_{E_1} \mathcal{O}_{E_2}$$ for operators $\mathcal{O}_{E_1}$ and $\mathcal{O}_{E_2}$ in the theories $T_{M_1}$ and $T_{M_2}$ respectively.

Again, this is true for a generic $C$, but if $C$ is a four-punctured sphere something special happens. Consider any of the many triangulations with the topology of a tetrahedron (not to be confused with the tetrahedra we use for gluing!). Then any pair of opposite edges $E$, $\tilde E$ have the same gauge charges, and only differ by the flavor charges associates with the punctures. This means that in any polarization where the $E$ edge coordinate and the meridians of defects are positions, the edge coordinate of $\tilde E$ is also a position.

Thus we can simultaneously decompose

$$\label{mutO}
\mathcal{O}_E =  \mathcal{O}_{E_1} \mathcal{O}_{E_2}\,,  \qquad   \mathcal{O}_{\tilde E} =  \mathcal{O}_{\tilde E_1} \mathcal{O}_{\tilde E_2}\,.$$

Now, $\mathcal{O}_{E_1}$ and $\mathcal{O}_{\tilde E_1}$ have the same gauge charges, and different flavor charges. The same is true for $\mathcal{O}_{E_2}$ and $\mathcal{O}_{\tilde E_2}$. Thus we can also build two new gauge-invariant operators

$$\label{mutOmixed}
\mathcal{O}_{12} =  \mathcal{O}_{E_1} \mathcal{O}_{\tilde E_2}\,,  \qquad   \mathcal{O}_{21} =  \mathcal{O}_{\tilde E_1} \mathcal{O}_{E_2}\,.$$

We can repeat the analysis for all the pairs of edges in the triangulation of $C$. This gives us a total of six new gauge-invariant marginal operators of "mixed" type [\[mutOmixed\]](#mutOmixed){reference-type="eqref" reference="mutOmixed"} in addition to the six operators of type [\[mutO\]](#mutO){reference-type="eqref" reference="mutO"}. It should be clear that a mutation $M \to M_\mu$ simply modifies the geometric gluing by permuting two opposite pairs of edges in, say, $C_2$. In field theory, this corresponds to a different choice of gluing superpotential, replacing four of the standard operators with four of the new operators. This has no effect on the index. In particular, either configuration breaks exactly the same set of global $U(1)$ symmetries.

We can even try to see part of the space of exactly marginal deformations of $T_M$: consider the most general superpotential, a linear combination of the six standard operators and the six new operators. There is a choice of R-charges that makes all the twelve operators marginal. The general superpotential breaks many flavor symmetries of the product theory $T_{M_1} \times T_{M_2}$. The standard superpotential forces the meridians (puncture eigenvalues) of $C_1$ to be equal to the meridians of $C_2$. The general superpotential forces all meridians to be equal . The number of flavor symmetries broken by the general superpotential is strictly smaller than $12$, but there are $12$ marginal operators. By the results of [@GKSTW], this indicates that at least one linear combination of the $12$ operators is exactly marginal.

We can try to be more precise. Assume that $T_{M_1} \times T_{M_2}$ has $SU(2)^8$ flavor symmetry associated to the defects, broken to $SU(2)^4$ by the standard gluing superpotential. Then the $6$ new operators have charges $\pm (\frac12,\frac12,-\frac12,-\frac12)$, $\pm (\frac12,\frac12,-\frac12,-\frac12)$, $\pm (\frac12,-\frac12,-\frac12,\frac12)$, $\pm (\frac12,-\frac12,\frac12,-\frac12)$ respectively. Because of the $SU(2)^4$ flavor symmetry, the operators must really be part of a set of $16$ marginal operators in the tensor product of the four doublet representations of the four $SU(2)$ flavor groups. By the results of [@GKSTW], the space of exactly marginal deformations is locally the Kähler quotient of ${\mathbb C}^{16}$ by $SU(2)^4$, which is indeed a local complexification of the expected $SU(2)^4 \backslash SO(8)/SU(2)^4$. Thus we recovered the full space of exactly marginal deformations predicted in the UV.

[^1]: It is perfectly possible that $S^2$ does not split $M$ in two, but rather into a manifold $\tilde M$ with two $S^2$ boundaries. Everything we say in this section will go through with very minor modifications in that case.

[^2]: As per the linear/quadratic behavior of the index explained in Section [\[sec:tent\]](#sec:tent){reference-type="ref" reference="sec:tent"}, evaluating these indices to order $q^n$ requires summing over an 11-dimensional cube with sides approximately of length $2n$. This is feasible for low order. The computation in [\[ConKT\]](#ConKT){reference-type="eqref" reference="ConKT"}, done naively, required $11^7$ terms and took 28 hours per knot.

[^3]: The triangulations of $M_1$ and $M_2$ contain annular cusps, and are of the "hybrid" type discussed in Section 2 of [@DGG]. Such triangulations will be a major focus of [@DGGV-hybrid].
