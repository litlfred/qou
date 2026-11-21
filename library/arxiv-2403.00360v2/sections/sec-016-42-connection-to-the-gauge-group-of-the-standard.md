---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-016-42-connection-to-the-gauge-group-of-the-standard
section_title: "Connection to the Gauge Group of the Standard Model"
section_number: 4.2
pages: 18-19
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
[]{#sec:gaugegroup label="sec:gaugegroup"} Obtaining the gauge group of the standard model is a key objective for any fundamental physical theory. Here we summarize the current status of this quest in both approaches and discuss what we can learn from a comparison.

### Octonionic Approaches

Algebraic approaches based on the octonions (or more generally the division algebras) attempt to recover the standard model gauge groups as those groups that preserve certain subspaces of the underlying algebraic structure. These subspaces are identified by means of projectors, as discussed in [\[historical\]](#historical){reference-type="ref" reference="historical"}.

Different constructions are possible. Dixon takes as the spinor space the algebra  $\mathbb{T}=\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$ [@dixon2013division]. Such spinors are acted upon from the left or right by the algebra itself, with these linear maps generating the associative multiplication algebra. In this construction it is the nontrivial algebraic structure of the spinor space itself that provides the algebraic source of the internal symmetries needed to replicate the structure of the standard model. The projectors that may be identified within  $\mathbb{T}$ simultaneously decompose the spinor space into mutually orthogonal subspaces, as well as the associative multiplication algebra into subalgebras whose actions preserve these subspaces.

Furey's approach is similar, but identifies the algebraic spinors are the minimal left ideals of the left associative multiplication algebra of $\mathbb{C}\otimes\mathbb{O}$ (see [\[Furey\]](#Furey){reference-type="ref" reference="Furey"}) and $\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$ [@furey2016standard; @furey231]. The dimensionality of these minimal left ideals then tells one the number of distinct physical states, whereas the gauge symmetries are those symmetries that preserve the minimal ideals.

### Causal Fermion Systems

Assuming the fermionic projector $P(x,y)$ in vacuum to be given by expression [\[Pvac\]](#Pvac){reference-type="eqref" reference="Pvac"} with eight direct summands, one can prove that the Minkowski vacuum is a minimizer of the causal action principle in the limit where $\varepsilon \searrow 0$. In this case $P(x,y)$ satisfies the Dirac equation [\[dirvac\]](#dirvac){reference-type="eqref" reference="dirvac"}. If we perturb the fermionic projector to satisfy the Dirac equation with a bosonic potential [\[Dinteract\]](#Dinteract){reference-type="eqref" reference="Dinteract"} we find that this perturbation only corresponds to a minimizer of the causal action if the vector potential $B$ has the right transformation property under the gauge group of the standard model.

### Discussion

We start the discussion in this section with the question how the octonionic vacuum [\[PvacO\]](#PvacO){reference-type="eqref" reference="PvacO"} can be perturbed. The auxiliary fermionic projector can be defined again by replacing direct sums by sums and inserting the octonions as factors, i.e. $$P^\text{aux} := P^N_\text{aux} \: e_0 + \bigg( \bigoplus_{\beta=1}^3 P^\text{vac}_{m_\beta} \bigg)
\big( e_1 + \cdots + e_7 \big) \:.$$ Now the vacuum Dirac equation [\[dirvac\]](#dirvac){reference-type="eqref" reference="dirvac"} holds if the matrix $Y$ is represented by a linear operator acting on the octonions. The interaction can again be described by inserting an operator ${\mathscr{B}}$ into the Dirac equation [\[Dinteract\]](#Dinteract){reference-type="eqref" reference="Dinteract"}. Now we observe that for the equation [\[Dinteract\]](#Dinteract){reference-type="eqref" reference="Dinteract"} to be well defined, the operator ${\mathscr{B}}(x)$ involves operations on the octonions. This leads us to choose the matrix elements of ${\mathscr{B}}$ as being composed of elements of the algebra of endomorphisms acting on the octonions. This algebra is the left associative multiplication algebra $\mathbb{O}_L\cong \mathbb{C}\ell(6)$. This algebra is associative. Moreover, this algebra acts on the octonions by left multiplication, giving a mapping $$\mathbb{O}_L \times \mathbb{O} \rightarrow \mathbb{O} \:.$$ In summary, when integrating octonions in the construction of the fermionic projector one is naturally lead to look for the standard model in the left associative multiplicative algebra. This is one of the key insights in this paper as it provides a clear motivation as for why one would consider this algebra instead of the octonions themselves. Furthermore, integrating the octonions in the fermionic projector provides a clear road map of how to get to the standard model. On the other hand, working with octonions provides a clear motivation for the choice of the vacuum in causal fermion systems which otherwise might appear arbitrary.
