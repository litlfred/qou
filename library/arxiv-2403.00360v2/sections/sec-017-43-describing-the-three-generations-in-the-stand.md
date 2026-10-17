---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-017-43-describing-the-three-generations-in-the-stand
section_title: "Describing the Three Generations in the Standard Model"
section_number: 4.3
pages: 19-21
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.987
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
[]{#secthreegen label="secthreegen"} We now explain and compare how the three generations of elementary particles (like $e$, $\mu$ and $\tau$) come up in the different approaches.

### Octonionic Approaches

Although existing division algebraic approaches provide an elegant construction of the internal space of a single generation of leptons and quarks, a comprehensive algebraic explanation for the existence of three generations remains to be found[^1].

In [@manogue1999dimensional] three generations of leptons are described in terms of the three $\mathbb{H}$ subalgebras of $\mathbb{O}$ that contain a particular imaginary octonion unit.

Furey identifies three generations of color states directly from the 64 complex dimensional algebra $\mathbb{C}\ell(6)$ [@furey2014generations]. Constructing two representations of the Lie algebra $\mathfrak{su}(3)$, the remaining 48 degrees of freedom transform under the action of the ${\rm{SU}}(3)$ as three generations of leptons and quarks. However, the inclusion of ${\rm{U}}(1)_{em}$ via the number operator, which works in the context of a one-generation model, fails to assign the correct electric charges to states in this three-generation model. A generalized action that leads to a generator that produces the correct electric charges for all states is introduced in [@furey2018three].

Dixon instead describes three generations in terms of the algebra $\mathbb{T}^6=\mathbb{C}\otimes\mathbb{H}^2\otimes\mathbb{O}^3$, with a single generation being described by $\mathbb{T}^2$, a complexified (hyper) spinor in 1+9D spacetime [@dixon2004division]. The choice $\mathbb{T}^6$, as opposed to any other $\mathbb{T}^{2n}$ appears rather arbitrary however, although can be motivated from the Leech lattice.

One intriguing idea is that the triality automorphism of $\mathop{\mathrm{Spin}}(8)$, may be responsible for the existence of three generations. Triality corresponds to an outer automorphism of $\mathop{\mathrm{Spin}}(8)$ that permutes between the vectors and two spinor representations, all of which are of dimension eight. It is known that there exist three conjugacy classes of $\mathop{\mathrm{Spin}}(7)$ subgroups in $\mathop{\mathrm{Spin}}(8)$ which are permuted by triality [@varadarajan2001spin]. Furthermore, there exists a unique way to choose one $\mathop{\mathrm{Spin}}(7)$ subgroup from each conjugacy class such that the common intersection of these subgroups is $G_2$. This suggests it may be possible to represent three generations of color states (since $G_2$ contains ${\rm{SU}}(3)$ as one of its maximal subgroups) in terms of $\mathop{\mathrm{Spin}}(8)$, with each generation corresponding to a $\mathop{\mathrm{Spin}}(7)$ subgroup. $\mathop{\mathrm{Spin}}(8)$ corresponds to the spin group of $\mathbb{C}\ell(8)$, whose bi-vectors generate $\mathfrak{spin}(8)$. One way to generate $\mathbb{C}\ell(8)$ is to consider the left or right associative multiplication algebra of a column vector of two octonions [@schray1994octonions].

An alternative way to generate $\mathbb{C}\ell(8)$ is to instead consider the left or right associative multiplication algebra generated from sedenions $\mathbb{S}$, which may be generated from the octonions[^2]. It has recently been advocated that $\mathbb{S}$, constitutes a natural mathematical object which exhibits the required algebraic structure necessary to describe three generations of color states [@gillard2019three; @gresnigt2019sedenions; @gresnigt2023three]. In this construction, one generation of leptons and quarks is represented in terms of two minimal left ideals of $\mathbb{C}\ell(6)\subset \mathbb{C}\ell(8)$, in what corresponds to a direct generalization of the octonionic construction in [@furey2016standard], reviewed in Subsection [\[Furey\]](#Furey){reference-type="ref" reference="Furey"}. Subsequently the $S_3$ automorphism of order three, which is an automorphism of $\mathbb{S}$ but not of $\mathbb{O}$ can be used to generate two additional pairs of minimal $\mathbb{C}\ell(6)$ ideals to represent exactly two additional generations of color states. Exactly how the $S_3$ automorphisms of $\mathbb{S}$ are related to the $S_3$ outer automorphisms corresponding to triality remains to be worked out, as does a possible link between this sedenionic construction and the three conjugacy classes of $\mathop{\mathrm{Spin}}(7)$ subgroups of $\mathop{\mathrm{Spin}}(8)$ mentioned above.

Finally, numerous authors have encoded three generations within the exceptional Jordan algebra $J_3(\mathbb{O})$ consisting of three by three matrices over $\mathbb{O}$ [@dubois2016exceptional; @dubois2019exceptional; @todorov2018octonions; @todorov2018deducing; @boyle2020standard2; @boyle2020standard]. In these models, the three octonions in $J_3(\mathbb{O})$ are related via triality. Each octonion is associated with one generation via the three canonical $J_2(\mathbb{O})$ subalgebras of $J_3(\mathbb{O})$. The automorphism group of $J_3(\mathbb{O})$ is the exceptional group $F_4$. The standard model gauge group emerges as the intersection of two subgroups of $F_4$, the first being the subgroup that preserves the representation of the octonions occurring in the elements of $J_3(\mathbb{O})$ as elements of $\mathbb{C}\oplus\mathbb{C}^3$, and the second being $\mathop{\mathrm{Spin}}(9)$, the automorphism group of each $J_2(\mathbb{O})$ subgroup of $J_3(\mathbb{O})$.

### Causal Fermion Systems

In the ansatz [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"}, [\[PC\]](#PC){reference-type="eqref" reference="PC"} and [\[massneutrino\]](#massneutrino){reference-type="eqref" reference="massneutrino"} the three generations of elementary particles are built in ad hoc via the $\beta$-sum. At this stage, one can just as well choose a different number of generations $g \in \mathbb{N}$ by summing instead over $\beta=1,\ldots, g$. However, the analysis of the continuum limit reveals that one gets field equations with a well-posed Cauchy problem if the number of generations is three. In simple terms, in the case $g<3$ the resulting equations are overdetermined (meaning that they do not admit non-trivial solutions), whereas in the case $g>3$ they are under-determined (meaning that, given initial data the solution is not unique). The details of this analysis and a discussion of there results can be found in [@cfs Section 3.7].

### Discussion

In order to make a connection between causal fermion systems and octonionic approaches, it is preferable to write out the direct sum over the generation index in [\[Paux\]](#Paux){reference-type="eqref" reference="Paux"} as a matrix, $$\bigoplus_{\beta=1}^3 
{P^\text{sea}_{m_\beta}} = \begin{pmatrix} P^\text{sea}_{m_1} & 0 & 0 \\
0 & P^\text{sea}_{m_1} & 0 \\ 0 & 0 & P^\text{sea}_{m_3} \end{pmatrix} \:,$$ giving a $3 \times 3$-matrix with octonionic entries. The form of the interaction poses constraints on the form of these matrices. The interesting connection with octonionic theories is that specific algebras arising in this context, like the exceptional Jordan algebra $J_3(\mathbb{O})$ in the approach [@singh-jordan; @singh-octo3], give concrete proposals for how these constraints could look like. The hope is that studying the causal action principle for these proposals will give a better understanding of why the gauge groups of the standard model appear in nature and why the gauge fields couple to matter in the way observed in experiments. This will be discussed in more detail in Section [\[sece68\]](#sece68){reference-type="ref" reference="sece68"}.

[^1]: It is worth noting that most GUTs likewise inherently correspond to single generation models, lacking any theoretical basis for three generations, which ultimately has to be imposed by hand.

[^2]: Starting with $\mathbb{R}$, the remaining three division algebras can be generated via what is called the Cayley-Dickson process. This process does not terminate with $\mathbb{O}$ however, but continues indefinitely to produce a series of $2^n$-dimensional algebras.
