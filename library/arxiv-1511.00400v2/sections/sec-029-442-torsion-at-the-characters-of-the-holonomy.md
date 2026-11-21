---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-029-442-torsion-at-the-characters-of-the-holonomy
section_title: "Torsion at the characters of the holonomy"
section_number: 4.4.2
pages: 33-34
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.718
latex_coverage_ratio: 0.97
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
::: prop
[]{#prop:propslift label="prop:propslift"} Let $\chi_\varrho$ be the character of a lift $\varrho$ of the holonomy representation

(a) []{#item:oddnonzero label="item:oddnonzero"} When $k_1+ k_2$ is odd, $\mathbb{T}_M^{k_1,k_2}(\chi_\varrho)\neq 0$.

    In particular, when $k$ is odd, $\mathbb{T}_M^{k}(\chi_\varrho)\neq 0$.

(b) []{#item:k1k2odd label="item:k1k2odd"} When $k_1\neq k_2$ are both odd, $\mathbb{T}_{M}^{k_1,k_2}(\chi_\varrho) = 0$.

(c) []{#item:k1k2even label="item:k1k2even"} When $k_1\neq k_2$ are both even and $k_1,k_2\neq 0$, for $0\neq\gamma\in H_1(T_2;\mathbb{Z})$, we have $\mathbb{T}_{M,\gamma}^{k_1,k_2}(\chi_\varrho) =0$.

(d) []{#item:ratiocurves label="item:ratiocurves"} For $k$ even and $0\neq\gamma\in H_1(T_2;\mathbb{Z})$, $\mathbb{T}_{M,\gamma}^{k}(\chi_\varrho) \neq 0$. In addition $$\frac{\mathbb{T}_{M,\gamma_2}^{k}(\chi_\varrho)}{\mathbb{T}_{M,\gamma_1}^{k}(\chi_\varrho)}= \operatorname{cs}(\gamma_2,\gamma_1),$$ where $0\neq\gamma_1,\gamma_2\in H_1(T_2;\mathbb{Z})$.
:::

::: proof
*Proof.* For item [\[item:oddnonzero\]](#item:oddnonzero){reference-type="eqref" reference="item:oddnonzero"}, Theorem [\[prop:dimatvarrho\]](#prop:dimatvarrho){reference-type="ref" reference="prop:dimatvarrho"} guarantees that the representation is acyclic and therefore $\mathbb{T}_M^{k_1,k_2}(\chi_\varrho)\neq 0$. For [\[item:k1k2odd\]](#item:k1k2odd){reference-type="eqref" reference="item:k1k2odd"}, the same theorem tells that the cohomology of $\varrho^{k_1,k_2}$ is nonzero in dimension 1 and 2. Since it is generically zero, what we have is a discontinuity in the dimension of the cohomology groups. On the other hand, the zeroth homology group of $\varrho^{k_1,k_2}$ vanishes, thus $\mathbb{T}_{M}^{k_1,k_2}(\chi_\varrho) = 0$. The proof of [\[item:k1k2even\]](#item:k1k2even){reference-type="eqref" reference="item:k1k2even"} is analogous, using the vanishing of the cup product in dimension one (not two) of the cap product in Proposition [\[prop:basis complete\]](#prop:basis complete){reference-type="ref" reference="prop:basis complete"}. The non-vanishing of the cup product of Proposition [\[prop:basis complete\]](#prop:basis complete){reference-type="ref" reference="prop:basis complete"} for $k_1$ even and $k_2=0$ yields the first part of item [\[item:ratiocurves\]](#item:ratiocurves){reference-type="eqref" reference="item:ratiocurves"}, the second part follows from Equation [\[eqn:cuspsh\]](#eqn:cuspsh){reference-type="eqref" reference="eqn:cuspsh"}. ◻
:::

::: thm
[]{#thm:MFP label="thm:MFP"} For any peripheral curve $\gamma$, $$\label{eqn:MFP}
    \lim_{k\to\infty} \frac{ \log\left\vert   \mathbb{T}_{M,\gamma}^{2k}(\chi_\varrho) \right\vert }{(2 k)^2} = 
    \lim_{k\to\infty} \frac{ \log\left\vert   \mathbb{T}_{M}^{2k+1}(\chi_\varrho) \right\vert }{(2 k+1)^2} = 
    \frac 1{4\pi}\operatorname{vol} (M^3)\, .$$
:::

Again, the sign convention is the opposite to [@MFP14]. This theorem is proved from Müller's Theorem [\[thm:Muller\]](#thm:Muller){reference-type="ref" reference="thm:Muller"} in the closed case, by using the approximation of the cusped manifolds by closed manifolds obtained by Dehn filling. Since Müller's proof uses Ruelle zeta functions, the key point is to understand geodesics (of bounded lengths) of the closed manifolds that approximate a cusped one.
