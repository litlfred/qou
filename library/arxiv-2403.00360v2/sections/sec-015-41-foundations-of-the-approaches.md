---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-015-41-foundations-of-the-approaches
section_title: "Foundations of the Approaches"
section_number: 4.1
pages: 16-18
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.98
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
[]{#sec:foundations label="sec:foundations"} We begin with a discussion of the basic ideas and the mathematical structures of the theories.

### Octonionic Approaches

Octonionic (division algebraic) approaches to the standard model remain an active research program, with different approaches considered in the literature. The underlying goal of these approaches is to find the correct algebraic structures, often in the form of tensor products of the division algebras, from which the gauge groups and particle content of the standard model may be derived, as well as the Lorentz group for the gravitational sector. An example of how the left associative multiplication algebra of the (complex) octonions may be used to represent one generation of standard model fermions with unbroken $SU(3)\times U(1)$ symmetry was given in [\[Furey\]](#Furey){reference-type="ref" reference="Furey"}. By further including the quaternion algebra $\mathbb{H}$ into this approach, it is possible to describe also the chiral weak interaction and the Lorentz spacetime symmetries [@dixon1990derivation; @dixon2013division; @furey2018demonstration; @furey231]

Although such algebraic proposals provide an elegant derivation of the gauge symmetries and particle multiplets of the standard model, what is currently still lacking is a description of spacetime in which these particles live, as well as a dynamical framework. In the absence of a dynamical framework, these kinematic algebraic models cannot be rigorously tested against experimental data. For a review of an ongoing attempt to incorporate spacetime and dynamics see [@singh-octo4].

### Causal Fermion Systems

Causal fermion systems are formulated on a set of operators ${\mathscr{F}}^{\text{reg}}$ on a Hilbert space. The measure $\rho$ on ${\mathscr{F}}^{\text{reg}}$ is the only "dynamical" degree of freedom in the theory. However, the fact that the support of the measure is typically restricted to a proper, lower dimensional subset of the operator manifold together with the intrinsic causal structures allows for the measure to encode a plethora of physical systems. In contrast to GR, for example, the operator manifold on which the variational principle is formulated does not fix the topology of the spacetime described by a minimizing measure.

To describe a classical spacetime in terms of a causal fermion system we need to construct the fermionic projector $P(x,y)$ which is a bi-distribution. In the coincidence limit this gives rise to the so-called local correlation map $F: \mathcal{M}\rightarrow {\mathscr{F}}$ that allows us to identify points in classical spacetime with operators in ${\mathscr{F}}$. The fermionic projector then allows us to calculate the causal action for a classical spacetime. An important observation for the following discussion is the fact that for every point $x$, the spin space $S_x$ is a $2n$ dimensional vector space. Intuitively one can think of this vector space as a fiber space attached to a point $x$ in ${\mathscr{F}}$ that goes over to a fiber space of the classical spacetime in the continuum limit.

### Discussion

In the following we will provide a first example of how octonions can be integrated in the mathematical structures of causal fermion systems and which conceptual lessons we can draw from this with respect to octonion based approaches and quantum gravity more generally.

In view of [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"} and [\[PC\]](#PC){reference-type="eqref" reference="PC"} the vacuum is formed of eight direct summands. In order to get a connection to the octonions, we replace the direct sum [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"} by the octonion-valued ordinary sum $$P(x,y) = P^N(x,y) \, e_0 + \sum_{i=1}^7 P^C_i(x,y)\: e_i \:. \label{PvacO}$$ Here the index $i$ at the factors $P^C_i$ clarifies that these factors could be different, describing the charged leptons and the quarks of different colors and isospin. In the vacuum, the index $i$ can be left out because, as in [\[PC\]](#PC){reference-type="eqref" reference="PC"}, all these factors are identical. We note that the octonionic symmetry is broken, because $e_0$ is distinguished (as it is multiplied by $P^N$, which is different from the factors $P^C$).

We point out that the descriptions [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"} and [\[PvacO\]](#PvacO){reference-type="eqref" reference="PvacO"} are equivalent, because the octonions simply serve as labels for the components of the direct sum in [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"}. Therefore, the crucial question is whether the formulation with octonions carries over and has benefits in the description of interacting systems.

Before addressing this question in the next section, we point out that, with the above construction, we implemented octonions into the causal fermion system *of the vacuum*. Once this has been done, the interaction and the resulting dynamics are described by the causal action principle. In this way, octonions should be helpful for getting a better understanding of and giving an explanation for the choice of the vacuum configuration in causal fermion systems.

In interacting causal fermion systems obtained from an octonionic vacuum like [\[PvacO\]](#PvacO){reference-type="eqref" reference="PvacO"} (using the methods outlined in Sections [\[seccfssm\]](#seccfssm){reference-type="ref" reference="seccfssm"} and [\[secqft\]](#secqft){reference-type="ref" reference="secqft"}), the octonionic structures are still present in the *local* form of the causal fermion system. More precisely, the octonionic structures describe the internal degrees of freedom contained in the fibers of vector bundles (like the spin space $S_x$, linear operators thereon like the kernel of the fermionic projector $P(x,y) : S_y \rightarrow S_x$, etc.). Since octonionic theories by themselves do not provide spacetime structures and dynamical equations, this is the best we can hope for without imposing additional structures. It is interesting to note that in [@singh-octo2; @singh-td] it was proposed to use Adler's trace dynamics [@adler-trace] and Connes' spectral action principle [@connes] in the octonionic setting. In an upcoming paper [@tracedynamics] we will show that the causal action principle reduces to trace dynamics on the diagonal (i.e. if only local contributions ${\mathcal{L}}(x,x)$ are considered). This further strengthens the above claim that octonion based algebraic structures are suitable to describe physics locally, i.e. in fibers of corresponding vector bundles.
