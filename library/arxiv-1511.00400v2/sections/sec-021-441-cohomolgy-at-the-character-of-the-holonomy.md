---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-021-441-cohomolgy-at-the-character-of-the-holonomy
section_title: "Cohomolgy at the character of the holonomy"
section_number: 4.4.1
pages: 32-35
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.965
---
In order to evaluate the torsion functions at the lift of the holonomy, some results on the cohomology for this representation are required. Again the proofs are postponed to Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}.

::: thm
[]{#prop:dimatvarrho label="prop:dimatvarrho"} Let $\varrho\colon\pi_1 M^3\to\mathrm{SL}_2(\mathbb{C})$ be a lift of the holonomy.

(a) If $k_1+k_2$ is odd, then $\varrho^{k_1,k_2}$ is acyclic.

(b) If $k_1+k_2$ is even, $k_1\neq k_2$, then $$\dim H_i(M^3;    \varrho^{k_1,k_2})= \begin{cases}
                                        1 & \textrm{if } i=1,2\, ,\\
                                        0 & \textrm{otherwise.}
                                       \end{cases}$$
:::

Notice that when both $k_1$ and $k_2$ are odd, the homology of $\varrho^{k_1,k_2}$ differs from the generic homology of $\operatorname{Sym}^{k_1,k_2}$ on $X_0(M^3)$, there is a discontinuity in the dimension of the cohomology, which is generically trivial.

We also need to discuss the basis. Let $i\colon T^2\to M^3$ denote the inclusion.

::: prop
[]{#prop:basis complete label="prop:basis complete"} Let $\varrho\colon\pi_1 M^3\to\mathrm{SL}_2(\mathbb{C})$ be a lift of the holonomy. Assume that $k_1+k_2$ is even.

(a) $\dim  H^0(T^2;\varrho)=1$.

(b) For $0\neq a\in H^0(T^2;\varrho)$, $\langle i_*(a\cap [T^2]) \rangle = H_2(M^3;    \varrho^{k_1,k_2})$.

(c) For $0\neq a\in H^0(T^2;\varrho)$ and $0\neq\gamma\in H_1(T_2;\mathbb{Z})$:

    (i) $\langle i_*(a\cap \gamma) \rangle = H_1(M^3;    \varrho^{k_1,k_2})$ if $k_1=0$ or $k_2=0$; in addition $$\label{eqn:cuspsh}
             i_*(a\cap \gamma_1)=\operatorname{cs}(\gamma_1,\gamma_2) \, i_*(a\cap \gamma_2)$$ where $\operatorname{cs}(\gamma_1,\gamma_2)$ is the cusp shape (Definition [\[def:cs\]](#def:cs){reference-type="ref" reference="def:cs"}).

    (ii) $i_*(a\cap \gamma ) = 0$ if $k_1\neq 0$ and $k_2\neq 0$.
:::

### Torsion at the characters of the holonomy

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

### Dehn filling

The following is a generalization to other representations of the formula for Dehn filling in Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}. In particular the same context and notation is used.

::: prop
[]{#prop:SFh label="prop:SFh"} Let $M^3$ be as above. For $\vert p\vert +\vert q\vert$ sufficiently large:

(a) For $k_1$ or $k_2$ odd, $$\tau^{k_1,k_2}(M_{p/q}^3,\sigma)=  
     {\mathbb{T}_M^{k_1,k_2}(\chi_{p/q,\sigma} )}{ 
    \prod_{i_1=0}^{k_1}\prod_{i_2=0}^{k_2}  
     \frac 1{ 1-(\lambda_{p/q})^{2 i_1-k_1} (\overline {\lambda}_{p/q})^{2 i_2-k_2} 
    } } \, .$$

(b) For $k_1$ and $k_2$ even, $k_1\neq k_2$, $$\tau^{k_1,k_2}(M_{p/q}^3)=  
     {\mathbb{T}_{M,pm+ql}^{k_1,k_2}(\chi_{p,q} )}{ 
        \prod_{(i_1,i_2)\in \mathcal I}
     \frac 1{ 1-(\lambda_{p/q})^{2 i_1-k_1} (\overline {\lambda}_{p/q})^{2 i_2-k_2} 
    } } \, ,$$ where $(i_1,i_2)\in \mathcal I$ if $0\leq i_1 \leq {k_1}$, $0\leq i_2\leq {k_2}$, and $i_1\neq \frac{k_1}{2}$ or $i_2\neq \frac{k_2}{2}$.
:::

::: cor
$$\lim_{p^2+q^2} \vert \tau^{2k}(M_{p/q}^3,\sigma)\vert =+\infty \, .$$
:::

::: proof
*Proof.* Use first Proposition [\[prop:propslift\]](#prop:propslift){reference-type="ref" reference="prop:propslift"} [\[item:ratiocurves\]](#item:ratiocurves){reference-type="eqref" reference="item:ratiocurves"} . Since the character $\chi_{p,q}$ converges to $\chi_\varrho$, $\mathbb{T}_{M,m}^{2k}(\chi_\varrho)\neq 0$, and $\vert\operatorname{cs}(pm+ql ,m )\vert=\vert p+q\,\operatorname{cs}(l,m)\vert\to\infty$, one has $$\vert {\mathbb{T}_{M,pm+ql}^{2 k}(\chi_{p,q} )}\vert \to\infty \, .$$ As $\vert\lambda_{p/q}\vert\to 1$, the surgery formula in Proposition [\[prop:SFh\]](#prop:SFh){reference-type="ref" reference="prop:SFh"} yields the result. ◻
:::

The same proof as Corollary [\[cor:dense\]](#cor:dense){reference-type="ref" reference="cor:dense"} yields:

::: cor
[]{#cor:denseh label="cor:denseh"} Given a spin structure, The set of modules of the torsions $\vert \tau^{2k_1+1,k_2}(M_{p/q}^3,\sigma)\vert$ obtained by Dehn filling on $M^3$, so that $\sigma$ can be extended, is dense in $$\left[ \frac14{\left\vert \tau^{2k_1+1,k_2} (M^3,\sigma)\right\vert},+\infty\right).$$
:::

When $k_1+k_2$ is even and $k_1 k_2\neq 0$, then $\mathbb{T}^{k_1,k_2}_M(\chi_\varrho)=0$ (for $k_i$ odd) and $\mathbb{T}^{k_1,k_2}_{M,\gamma}(\chi_\varrho)=0$ (for $k_i$ even). In this case, we cannot get conclusions from the surgery formula.
