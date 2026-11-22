---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-037-44-the-affine-case
section_title: "The affine case"
section_number: 4.4
pages: 36-37
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.857
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:aff label="sub:aff"}

Let $\mathcal{C}$ be an additive monoidal category. Suppose we are given a Noetherian commutative ring $A$ and a ring homomorphism $$\label{eqn:affine}
A \stackrel{f}\longrightarrow \mathrm{End}_\mathcal{C}(\mathbf{1})$$ satisfying $$(\#) \quad \mathop{\mathrm{Hom}}_\mathcal{C}(\mathbf{1},C) \text{ is finitely generated over }A$$ for any object $C$ of $\mathcal{C}$. Then there is a derived morphism: $$\label{eqn:affine0}
 \mathcal{C}\stackrel{\iota}\longrightarrow  \mathrm{Spec}\ A.$$ The functors $$K(\mathcal{C}) \xtofrom[\iota^*]{\iota_*} D(A\text{--mod})$$ are defined as follows. There is a functor $i: \mathcal{C}\to A \text{--mod}$ given by: $$\label{eqn:push0}
\iota_* (C) = \mathop{\mathrm{Hom}}_{\mathcal{C}}(\mathbf{1},C).$$ This extends in the obvious way to a functor $i: K(\mathcal{C}) \to K(A \text{--mod})$, and $\iota_*$ is defined to be the composition of $i_*$ with the natural inclusion $K(A \text{--mod}) \to D(A \text{--mod})$.

In the other direction, let $FA \text{--mod}$ be the category of finitely generated free $A$ modules. The inclusion $K(FA \text{--mod}) \to D(A \text{--mod})$ is an equivalence of categories, so we may as well give a functor $\iota_* : K(FA \text{--mod}) \to K(\mathcal{C})$. We define $\iota_*$ by setting $\iota_*(A) = \mathbf{1}$ and $\iota_*(a) = f(a)$ for $a \in A = \mathop{\mathrm{Hom}}(A,A)$. This extends to $K(FA \text{--mod})$ in the obvious way. If $M$ is an object of $D(A \text{--mod})$, we write $\iota_*(M) = M \otimes_A \mathbf{1}$.

Let us check that the functors $\iota^*$ and $\iota_*$ are adjoint, or equivalently, that $$\label{eqn:adj0}
\mathop{\mathrm{Hom}}_{K(\mathcal{C})}(M \otimes_A \mathbf{1}, C) = \mathop{\mathrm{Hom}}_{D(A\text{--mod})}(M, \mathop{\mathrm{Hom}}_{\mathcal{C}}(\mathbf{1},C))$$ for all $M \in D(A\text{--mod})$ and $C\in K(\mathcal{C})$. If $C \in \mathcal{C}$, the right-hand side is by definition $\mathop{\mathrm{Ext}}_A(M,\mathop{\mathrm{Hom}}_{\mathcal{C}}(1,C))$. The statement that it is equal to the left-hand side reduces to the well known fact that to compute $\mathop{\mathrm{Ext}}$ of two modules, it is enough to take a free resolution of one of them. Properties [\[eqn:projection\]](#eqn:projection){reference-type="eqref" reference="eqn:projection"} and [\[eqn:birational\]](#eqn:birational){reference-type="eqref" reference="eqn:birational"} also follow directly from the definitions.

::: example
Let $Y$ be an algebraic variety, and $\mathcal{C}=\mathrm{Coh}(Y)$. The unit in $Y$ is given by the structure sheaf $\mathcal{O}_Y$, and indeed $\mathcal{C}$ is a category over $\mathrm{Spec}\ \mathrm{End}_{\mathcal{C}}(\mathbf{1})=\mathrm{Spec}\ \Gamma(Y,\mathcal{O}_Y)$. This structure is precisely equivalent with the global section map: $$\iota : Y\to \mathrm{Spec}\ \Gamma(Y,\mathcal{O}_Y)$$ More generally, a ring homomorphism $A\stackrel{f}\rightarrow \Gamma(Y,\mathcal{O}_Y)$ corresponds to a map $\mathrm{Spec}\ \Gamma(Y,\mathcal{O}_Y)\to \mathrm{Spec}\ A$, and one can use the composed map from $Y$ to $\mathrm{Spec}\ A$ to define $\iota_*$ and $\iota^*$.
:::
