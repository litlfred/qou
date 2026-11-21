---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-020-58-products-of-trees
section_title: "Products of trees"
section_number: 5.8
pages: 29-30
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.955
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#SS:trees label="SS:trees"} A nonzero composition ${\mathbf v}=\mathbf{T}_k \cdots \mathbf{T}_2 \mathbf{T}_1$ is a if each $\mathbf{T}_i$ is a tree and each pair of trees has noncrossing supports. A forest is minimal, so that each pair of trees commute, and commuting them gives an equivalent operator.

::: theorem
[]{#main-theorem label="main-theorem"} Suppose that ${\mathbf v}$ is a forest. Let $u\in S_n$ and $k<n$ be such that ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u\neq{\mathbf 0}$. Then ${\mathbf v}$ is $(u,k)$-equivalent to a composition $\mathbf{R}\mathbf{C}$ of a row $\mathbf{R}$ and a column $\mathbf{C}$. Moreover, there exists $r \in {\mathbb N}$ such that $\mathfrak o^r(\mathbf{R}\mathbf{C})=\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$ is classical, and $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}\mathfrak o^r(u)\neq{\mathbf 0}$.
:::

The proof is split into two parts.

### The classical case

The case of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} in which all the operators are classical follows from the study of minimal permutations in [@BS-iso Sect. 6.2], and the discussion in Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}. Recall that ${\mathcal L}$ is the rank function in the Grassmannian--Bruhat order on $S_n$.

::: proposition
[]{#BS2002 label="BS2002"} If ${\mathbf v}$ is a composition of classical operators that is a forest, then it is equivalent to a composition $\mathbf{R}\mathbf{C}$ of a classical row and a classical column.
:::

::: proof
*Proof.* Suppose that $\zeta=(a_r,b_r)\dotsb(a_1,b_1)$ is the product of transpositions whose corresponding graph is a forest. Using that this graph is a forest, induction on $r$ shows that $\mathop{\mathrm{supp}}(\zeta)=\{a_r,b_r,\dotsc,a_1,b_1\}$. (*A priori*, it is only a subset.) The same induction shows that $\zeta$ is a product of disjoint cycles, with each cycle corresponding to a tree in the graph of $\zeta$.

Now suppose that ${\mathbf v}={\mathbf v}_{a_r,b_r}\dotsb{\mathbf v}_{a_1,b_1}$ is a nonzero tree with corresponding permutation $\zeta\vcentcolon=(a_r,b_r)\dotsb(a_1,b_1)$, which is a cycle--so $s(\zeta)=1$--and which satisfies ${\mathcal L}(\zeta)=r$. Since ${\mathbf v}$ is a tree, $\mathop{\mathrm{supp}}({\mathbf v})=\{a_r,b_r,\dotsc,a_1,b_1\}$, which equals $\mathop{\mathrm{supp}}(\zeta)$, has cardinality $r{+}1$. Thus ${\mathcal L}(\zeta)=\#\mathop{\mathrm{supp}}(\zeta)-s(\zeta)$, and we conclude that $\zeta$ is a minimal cycle.

When ${\mathbf v}$ is a forest, its corresponding permutation $\zeta$ is a noncrossing product of minimal cycles, and is therefore a minimal permutation. By Proposition [\[P:peaklessChains\]](#P:peaklessChains){reference-type="ref" reference="P:peaklessChains"}, the interval $[e,\zeta]_\preceq$ has a peakless chain. Under the identification of chains in $[e,\zeta]_\preceq$ with compositions equivalent to ${\mathbf v}$ from Proposition [\[Prop:monoid\]](#Prop:monoid){reference-type="ref" reference="Prop:monoid"}(*2*), this peakless chain corresponds to a composition $\mathbf{R}\mathbf{C}$ of a classical row and a classical column. ◻
:::
