---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-024-34-from-rouquier-complexes-to-khovanov-rozansky
section_title: "From Rouquier complexes to Khovanov-Rozansky homology"
section_number: 3.4
pages: 22-23
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.946
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:khr label="sub:khr"}

Since $\sigma_i=[B_i]-q^{-\frac 12}$, it is clear that $\sigma_i$ does not correspond to any Soergel bimodule. However, Rouquier showed that $\sigma_i$ can be realized in the homotopy category of complexes: $$K^b(\mathrm{SBim}_n)$$ where we use the variable $s$ to keep track of homological degree. Explicitly, objects in the homotopy category of complexes will be denoted by: $$\Big[s^k M_k \rightarrow ... \rightarrow s^{k'} M_{k'} \Big]$$ for some $k \leq k' \in \mathbb{Z}$. The variable $s$ may seem redundant when writing down chain complexes, but we keep track of it for two reasons: first of all, it will give rise to the equivariant parameter $t$ of Section [\[sec:flag\]](#sec:flag){reference-type="ref" reference="sec:flag"} via [\[eqn:matching\]](#eqn:matching){reference-type="eqref" reference="eqn:matching"}. Second of all, we think of the object: $$\left[M \rightarrow s M' \right] \in K^b(\mathrm{SBim}_n)$$ as the cone of a morphism between the objects $M$ and $s M'$, and thus the power of $s$ makes the homological degrees of our formulas manifest. Recall the Bott-Samuelson bimodules [\[eqn:bs\]](#eqn:bs){reference-type="eqref" reference="eqn:bs"} and consider the Rouquier complexes: $$\label{eqn:rouquier}
\sigma_i:= \left[ B_i \xrightarrow{1\otimes 1 \mapsto 1} \frac {sR}{q^{\frac 12}}  \right], \qquad \sigma_i^{-1} := \left[ \frac {q^{\frac 12}R}s \xrightarrow{1 \mapsto x_i \otimes 1 - 1 \otimes x_{i+1}} B_i \right]$$ They satisfy the following equations [@Kh; @Rou] (which can be deduced from [\[eqn:BS1\]](#eqn:BS1){reference-type="eqref" reference="eqn:BS1"} and [\[eqn:BS2\]](#eqn:BS2){reference-type="eqref" reference="eqn:BS2"}): $$\sigma_i\otimes \sigma_i^{-1} \cong \sigma_i^{-1} \otimes \sigma_i \cong \mathbf{1},$$ $$\sigma_i \otimes \sigma_j \cong \sigma_j \otimes \sigma_i \ \ \text{for }\ |i-j|>1,$$ $$\sigma_i \otimes \sigma_{i+1} \otimes \sigma_i \cong \sigma_{i+1} \otimes \sigma_i \otimes \sigma_{i+1},$$ and hence categorify the braid group. To any braid $\sigma=\prod_{i=1}^{n-1} \sigma_{i}^{a_i}$ (where $\alpha_{i} \in \{-1,0,1\}$) one can associate a complex of bimodules obtained by tensoring together the various complexes [\[eqn:rouquier\]](#eqn:rouquier){reference-type="eqref" reference="eqn:rouquier"}. We abuse notation and denote the resulting complex also by $\sigma$. Khovanov [@Kh] defined the HOMFLY-PT homology of a braid $\sigma$ as: $$\label{eqn:Khovanov}
\mathop{\mathrm{HHH}}(\sigma):=\mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1},\sigma).$$ The right hand side is a triply graded vector space, endowed with the internal grading $q$, the homological grading $s$ of the complexes [\[eqn:rouquier\]](#eqn:rouquier){reference-type="eqref" reference="eqn:rouquier"} and their coproducts, and the Hochschild grading $a$ given by taking the $\mathop{\mathrm{{RHom}}}$. The appropriate derived category formalism can be found in [@Hog]. With respect to these three gradings, Khovanov proved that [\[eqn:Khovanov\]](#eqn:Khovanov){reference-type="eqref" reference="eqn:Khovanov"} is a topological invariant of the closure of $\sigma$, after a certain renormalization.

::: corollary
[]{#cor:trace twisted identity label="cor:trace twisted identity"}

Let $\sigma,\sigma'$ be any two braids. Then: $$\mathop{\mathrm{HHH}}(\sigma\sigma') = \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1},\sigma \otimes \sigma') \quad \text{and} \quad \mathop{\mathrm{HHH}}(\sigma'\sigma) = \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\mathbf{1},\sigma' \otimes \sigma)$$ are isomorphic as $R$-modules, up to a twist by $w_{\sigma}$.
:::

The above formula follows from Corollary [\[cor:inv 2\]](#cor:inv 2){reference-type="ref" reference="cor:inv 2"}, which applies to all invertible objects in a monoidal category.

::: proposition
The Soergel bimodule $B_i$ is self biadjoint, for all $i$. The Rouquier complex $\sigma$ for a braid $\sigma$ is biadjoint to $\sigma^{-1}$.
:::

The second statement of the above Proposition also follows from Corollary [\[cor:inv 1\]](#cor:inv 1){reference-type="ref" reference="cor:inv 1"} below, which is quite general, and actually implies the following stronger result:

::: corollary
[]{#cor:twisting homs label="cor:twisting homs"} For any $A,A'\in \mathrm{SBim}_n$ and any braid $\sigma$ there are canonical isomorphisms: $$\mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(A\otimes \sigma,A' \otimes \sigma) \cong \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(A,A') \cong \mathop{\mathrm{{RHom}}}_{K^b(\mathrm{SBim}_n)}(\sigma \otimes A,\sigma\otimes A').$$
:::
