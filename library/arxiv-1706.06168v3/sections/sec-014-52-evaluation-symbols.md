---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-014-52-evaluation-symbols
section_title: "Evaluation Symbols"
section_number: 5.2
pages: 16-17
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.98
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
One way to interpret the stability properties of a given polynomial is via the stability-preservation properties of a particular type of linear operator: the evaluation map. That is, the map which evaluates a polynomial $p(x,y)$ at $(a,b) \neq (0,0)$ preserves strong $\{(a:b)\}$-stability, where $\{(a:b)\}$ is a subset of $\mathbb{CP}^1$ consisting of a single point. Further, given $\lambda \in \mathbb{N}_0^m$ and $(a,b) = (a_1,b_1,\ldots,a_m,b_m) \in \mathbb{C}^{2m}$ (with $(a_j,b_j) \neq 0$ for all $j$), we can define the corresponding evaluation map as an element of $\mathop{\mathrm{Hom}}(V(\lambda),V(0))$ since $V(0) \cong \mathbb{C}$. This allows us to obtain symbols for evaluation maps, and these play an important role in our linear operator characterization.

::: definition
[]{#ev_def label="ev_def"} Fix $\lambda \in \mathbb{N}_0^m$ and $(a,b) = (a_1,b_1,\ldots,a_m,b_m) \in \mathbb{C}^{2m}$ such that $(a_j,b_j) \neq (0,0)$ for all $j \in [m]$. Let $\mathop{\mathrm{ev}}_{(a,b)}: V(\lambda) \rightarrow V(0) \cong \mathbb{C}$ be the evaluation operator which maps $p$ to $p(a,b) = p(a_1,b_1,\ldots,a_m,b_m)$. We call $\mathop{\mathrm{Symb}}(\mathop{\mathrm{ev}}_{(a,b)}) \in V(\lambda)$ the *evaluation symbol with root $(a,b)$*. Further: $$\mathop{\mathrm{Symb}}(\mathop{\mathrm{ev}}_{(a,b)}) = \prod_{j=1}^m (b_jx_j - a_jy_j)^{\lambda_j} =: (bx - ay)^\lambda$$
:::

The main significance of this notion comes from the following result, which is essentially just a restatement of the symbol lemma (Lemma [\[symb_lemma\]](#symb_lemma){reference-type="ref" reference="symb_lemma"}) for evaluation symbols.

::: lemma
[]{#ev_lemma label="ev_lemma"} Fix $\lambda \in \mathbb{N}_0^m$, $p \in V(\lambda)$, and $(a,b) = (a_1,b_1,\ldots,a_m,b_m) \in \mathbb{C}^{2m}$ such that $(a_j,b_j) \neq (0,0)$ for all $j \in [m]$. Considering $(bx-ay)^\lambda$, the evaluation symbol with root $(a,b)$, we have: $$D^\lambda((bx-ay)^\lambda \otimes p) = (\lambda!)^2 p(a,b) \otimes 1 = (\lambda!)^2 p(a,b)$$
:::

In what follows, we will extend Grace's theorem in a number of ways, mainly relying on the previous lemma and the symbol lemma itself. As we will see, the representation theoretic mentality combined with repeated use of the symbol lemma will yield many of the results of this paper with surprising simplicity.

We now obtain an interesting corollary of Grace's theorem, making use of the notion of a disjoint Grace pair. This particular formulation of the theorem will serve as a model for our linear operator characterization in §[\[str_Cstab_subsect\]](#str_Cstab_subsect){reference-type="ref" reference="str_Cstab_subsect"}.

::: corollary
[]{#ev_graces label="ev_graces"} Fix $\lambda \in \mathbb{N}_0^m$, $q \in V(\lambda)$, and any disjoint Grace pair $(C_1 \times \cdots \times C_m, B_1 \times \cdots \times B_m)$. Then the following are equivalent.

1.  $D^\lambda(p \otimes q) \neq 0$ for all $(C_1 \times \cdots \times C_m)$-stable $p \in V(\lambda)$.

2.  $D^\lambda(p \otimes q) \neq 0$ for all $(C_1 \times \cdots \times C_m)$-stable evaluation symbols $p \in V(\lambda)$.

3.  $q$ is $(B_1 \times \cdots \times B_m)$-stable.
:::

::: proof
*Proof.* $(i) \Rightarrow (ii)$ Immediate.

$(ii) \Rightarrow (iii)$ Fix any $(a,b) = (a_1,b_1,\ldots,a_m,b_m) \in \mathbb{C}^{2m}$ such that $(a_k:b_k) \in B_k$ for all $k \in [m]$. Since $B_k$ and $C_k$ are disjoint, we have that $(a_k:b_k) \not\in C_k$ for all $k$, and therefore $\mathop{\mathrm{Symb}}(\mathop{\mathrm{ev}}_{(a,b)}) = (bx-ay)^\lambda$ is an evaluation symbol which is $(C_1 \times \cdots \times C_m)$-stable. The evaluation symbol lemma given above then implies: $$0 \neq D^\lambda(\mathop{\mathrm{Symb}}(\mathop{\mathrm{ev}}_{(a:b)}) \otimes q) = (\lambda!)^2 q(a,b) \otimes 1 = (\lambda!)^2 q(a,b)$$ That is, $q(a,b) \neq 0$ for any $(a,b) \in \mathbb{C}^{2m}$ such that $(a:b) \in B_1 \times \cdots \times B_m$, and this implies $q$ is $(B_1 \times \cdots \times B_m)$-stable.

$(iii) \Rightarrow (i)$ This follows immediately from the definition of Grace pair (Definition [\[grace_pair_def\]](#grace_pair_def){reference-type="ref" reference="grace_pair_def"}). ◻
:::
