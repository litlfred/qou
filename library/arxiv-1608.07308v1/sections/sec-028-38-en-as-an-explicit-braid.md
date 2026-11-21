---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-028-38-en-as-an-explicit-braid
section_title: "En as an explicit braid"
section_number: 3.8
pages: 26-27
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.843
latex_coverage_ratio: 0.882
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:explicit braid label="sub:explicit braid"}

The object $E_n = \mathop{\mathrm{Tr}}(L_{n+1}) \in K^b(\mathrm{SBim}_n[x_{n+1}])$ has a simple topological meaning, represented below.

<figure>

<figcaption>The braid <span class="math inline"><em>L</em><sub>4</sub></span> and its partial trace <span class="math inline"><em>E</em><sub>3</sub></span>.</figcaption>
</figure>

The relation between the tangle $E_n$ and the complex $\mathcal{E}_n$ is expected to categorify the classical formula for $E_n$ (e.g. [@Morton]) in the skein algebra. Specifically, skein relations are topological equalities between knots which only differ near a crossing:

<figure id="fig:skein def">

<figcaption>Skein relation</figcaption>
</figure>

In $K^b(\mathrm{SBim}_n)$ such equalities must be replaced with exact sequences. For example, consider the skein relation applied to the bottom right crossing of the braid $L_{n+1}$.

<figure id="fig:skein">

<figcaption>Skein relation for <span class="math inline"><em>L</em><sub><em>n</em> + 1</sub></span></figcaption>
</figure>

If one closes the last strand in Figure [2](#fig:skein){reference-type="ref" reference="fig:skein"} and applies a Markov move, one gets the following formula in the Grothendieck group of $\mathrm{SBim}_n$ (which is isomorphic to the Hecke algebra): $$\label{eqn:explicit0}
\langle E_n\rangle - \langle I(E_{n-1})\rangle = (1-q)\langle L_{n} \rangle$$ In the category $K^b(\mathrm{SBim}_n[x_{n+1}])$, the above equality is lifted to an exact sequence: $$\label{eqn:explicit}
\left[ qt L_{n}\xrightarrow{(0,x_n-x_{n+1})} \underline{q L_{n}\oplus t L_{n}} \xrightarrow{(x_n-x_{n+1},0)}L_{n} \right] \cong \left[ E_n \longrightarrow \widetilde{I(E_{n-1})} \right]$$ where $t = s^2/q$ and $\widetilde{I(E_{n-1})}$ refers to the same braid as $I(E_{n-1})$, but with the variables on the last two strands switched (compare with [\[eqn:ind\]](#eqn:ind){reference-type="eqref" reference="eqn:ind"}). This is a crucial feature of the category $\mathrm{SBim}_n[x_{n+1}]$, where the variables $x_n$ and $x_{n+1}$ play different roles. Also note that [\[eqn:explicit\]](#eqn:explicit){reference-type="eqref" reference="eqn:explicit"} consists of 4 copies of $L_n$ instead of the two of [\[eqn:explicit0\]](#eqn:explicit0){reference-type="eqref" reference="eqn:explicit0"}, due to the modified Markov move [\[eqn: R1 upgraded\]](#eqn: R1 upgraded){reference-type="eqref" reference="eqn: R1 upgraded"}.
