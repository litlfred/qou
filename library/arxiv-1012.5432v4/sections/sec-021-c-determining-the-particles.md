---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-021-c-determining-the-particles
section_title: "C Determining the Particles"
section_number: null
pages: 18-19
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
Note that there is spin-charge separation in the system as the flux and the charge can be measured independently (and there are both charged particles with no magnetic flux and magnetic fluxes with no electric charge). A specific particle type is determined by a conjugacy class A of the symmetry group H and a representation $\alpha$ of the centralizer of a representative of that conjugacy class. (The centralizers of each element of the conjugacy class are isomorphic, so the representation thus defined is independent of the particular representative chosen.) In particular, label the elements of each conjugacy class $^A C = \{^A h_1, ^A h_2, ..., ^A h_k \}$. Let $^A N$ denote the subgroup of H that is the centralizer for $^A h_1$. Choose a set of representatives of $H/^A N = \{^{\alpha}v_1,...,^{\alpha}v_k\}$. The states $$\{ |^A h_i, ^{\alpha}v_j \rangle \}$$ then constitute a basis for the internal Hilbert space $V_{\alpha}^A$.

A bit more formally, given the flux values take values in a group H, then quantum mechanically we should consider complex combinations $\mathbb{C}[H]$. The electric charge takes values in the dual $\textit{F}(H)$. The particles thus correspond to representations of Drinfeld's quantum double construction applied to the Abelian algebra $\textit{F}(H)$ of functions on a finite group $H$. Generators are given by combinations $\{P_h g\}_{h,g \in H}$, where $P_h$ is the operator projecting the flux $h \in H$ and $g \in H$ corresponds to the global symmetry transformation. The operators $P_h$ are projections as $P_h P_{h'} = \delta_{h, h'}P_h$. We demonstrated earlier that the action of the global symmetry transformations does not commute with the flux projection operators, and in fact: $g P_h = P_{g h g^{-1}} g$ due to flux metamorphosis. Combining these two relations we obtain the multiplication rule for two elements of the quantum double: $P_h g \cdot P_{h'}g' = \delta_{h, g h' g^{-1} P_h g g}$. The particles permitted by a discrete gauge theory are given by unitary irreducible representations of the quantum double. Note that since the quantum double is an algebra, not a group, representations $\Pi$ here are defined not only to respect the multiplicative structure, but are also required to be linear, i.e. addition and scalar multiplication are preserved. Each unitary irreducible representation of $D(H)$ is labeled uniquely by fixing a conjugacy class of the underlying group H and specifying the representation of the centralizer of a representative element in that conjugacy class. The algebra is semisimple, i.e. it can be decomposed into a direct sum. Thus the sum of squares of internal Hilbert spaces = the dimension of the quantum double. (This will be used as a consistency check to confirm the explicit dimensions obtained in future sections.)
