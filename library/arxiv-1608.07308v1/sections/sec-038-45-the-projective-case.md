---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-038-45-the-projective-case
section_title: "The projective case"
section_number: 4.5
pages: 37-38
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.944
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:proj label="sub:proj"}

In the previous Subsection, we showed that any category can be realized over the spectrum of the endomorphism ring of its unit. We may upgrade this construction if we are given an **invertible** object $F \in K(\mathcal{C})$, i.e. one which is endowed with isomorphisms: $$\label{eqn:def invertible}
F \otimes F^{-1} \cong F^{-1} \otimes F \cong \mathbf{1}$$

::: assumption
[]{#ass:commute label="ass:commute"} We assume that the graded algebra: $$\label{eqn:commalg}
\mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^{\bullet}) := \bigoplus_{k=0}^\infty \mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^k)$$ is commutative.
:::

::: remark
Recall that $\mathcal{C}$ was a graded category, so for every $k$ the space $\mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^k)$ is graded. The algebra $\mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^{\bullet})$ has an extra grading which equals $k$ on $\mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^k)$.
:::

In this setting, there exists a tautological derived map: $$\label{eqn:projective0}
\mathcal{C}\stackrel{\iota}\longrightarrow (\mathrm{Spec}\ R )/\mathbb{C}^*$$ for any Noetherian graded commutative ring $R$ and graded ring homomorphism: $$\label{eqn:projective}
R \stackrel{f}\longrightarrow  \mathop{\mathrm{Hom}}_{K(\mathcal{C})}(\mathbf{1},F^{\bullet})$$ The functors [\[eqn:functors\]](#eqn:functors){reference-type="eqref" reference="eqn:functors"} are explicitly given by: $$\label{eqn:functors1}
\iota_*(C) = \mathop{\mathrm{Hom}}_{K(\mathcal{C})} \left(\mathbf{1}, F^{\bullet} \otimes C \right)$$ $$\label{eqn:functors2}
{\iota}^*(M) = \left( M \otimes_R \bigoplus_{k=-\infty}^{\infty} F^k \right)^0$$ for all graded $R-$modules $M$ and all $C \in K(\mathcal{C})$. The Hom space in [\[eqn:functors1\]](#eqn:functors1){reference-type="eqref" reference="eqn:functors1"} is an $R-$module via [\[eqn:projective\]](#eqn:projective){reference-type="eqref" reference="eqn:projective"}. It is straightforward to show that the analogue of [\[eqn:adj0\]](#eqn:adj0){reference-type="eqref" reference="eqn:adj0"} holds, and that the above datum makes $\mathcal{C}$ into a category over the stack $(\mathrm{Spec}\ R )/\mathbb{C}^*$: $$\label{eqn:yoy}
K(\mathcal{C}) \xtofrom[\iota^*]{\iota_*}D(R\text{--grmod})$$ Note that one needs the analogue of condition $(\#)$ on the category $\mathcal{C}$ to ensure that the above functors are well-defined (in particular, that the right hand side of [\[eqn:functors1\]](#eqn:functors1){reference-type="eqref" reference="eqn:functors1"} is a finitely generated $R$-module). But given this, the map $\iota$ is birational if and only if the map $f$ of [\[eqn:projective\]](#eqn:projective){reference-type="eqref" reference="eqn:projective"} is an isomorphism.

::: example
[]{#ex:projective label="ex:projective"}

Let us consider the case where $R = A[z_0,...,z_n]$, for a ring $A$ equipped with a homomorphism $A \rightarrow \mathrm{End}_\mathcal{C}(\mathbf{1})$. Then the datum of the homomorphism [\[eqn:projective\]](#eqn:projective){reference-type="eqref" reference="eqn:projective"} boils down to giving $n+1$ morphisms: $$z_i \quad \rightsquigarrow \quad \Big\{ \mathbf{1} \xrightarrow{\alpha_i} F \Big\}_{i=0,...,n}$$ This makes $\mathcal{C}$ into a category over the stack: $\mathcal{C}\xrightarrow{\iota} \mathbb{A}^{n+1}_A/\mathbb{C}^*.$ The natural question is when does $\iota$ factor through projective space: $$\includegraphics{before_4_21.png}$$ which amounts to factoring [\[eqn:yoy\]](#eqn:yoy){reference-type="eqref" reference="eqn:yoy"} through functors: $$\label{eqn:func}
K(\mathcal{C}) \xtofrom[{\iota'}^*]{\iota'_*} D(\mathrm{Coh}(\mathbb{P}^n_A))$$ It is clear that ${\iota'}^*$ and $\iota'_*$ must be given by the same formulas as in [\[eqn:functors1\]](#eqn:functors1){reference-type="eqref" reference="eqn:functors1"}--[\[eqn:functors2\]](#eqn:functors2){reference-type="eqref" reference="eqn:functors2"}, but one needs to impose a certain relation. Because the zero section of $\mathbb{A}^{n+1}_A/\mathbb{C}^*$ is removed when defining projective space, the structure sheaf of the zero section becomes quasi-isomorphic to 0. Since this structure sheaf can be expressed via the following Koszul complex: $$\left[ ... \longrightarrow \mathcal{O}(-2)^{\oplus \binom{n+1}{2}} \longrightarrow \mathcal{O}(-1)^{\oplus \binom{n+1}{1}} \xrightarrow{(z_0,...,z_n)} \mathcal{O}\right] = \bigotimes_{i=0}^n \left[\mathcal{O}(-1) \xrightarrow{z_i} \mathcal{O}\right]$$ we conclude that the functors [\[eqn:func\]](#eqn:func){reference-type="eqref" reference="eqn:func"} are well-defined only if: $$\label{eqn:conecondition}
\left[ \mathbf{1} \xrightarrow{\alpha_0}  F \right] \otimes ... \otimes \left[ \mathbf{1} \xrightarrow{\alpha_n} F \right] \stackrel{\text{h.e.}}\cong 0 \ \in K(\mathcal{C}).$$

It is not hard to see that this condition is also sufficient, by invoking Beilinson's description [@Be; @BGG] of the derived category of projective space as equivalent to the homotopy category of complexes of finite direct sums of free $A[x_0,...,x_n]$--modules with degree shifts $\in \{0,...,n\}$.
:::

::: remark
If $F = \mathcal{L}$ is a line bundle in $\mathcal{C}=\mathrm{Coh}(X)$, then $\alpha_i$ are nothing but sections of $\mathcal{L}$. By Remark [\[rem:prod cones\]](#rem:prod cones){reference-type="ref" reference="rem:prod cones"}, equation [\[eqn:conecondition\]](#eqn:conecondition){reference-type="eqref" reference="eqn:conecondition"} is equivalent to the fact that $\alpha_i$ generate $\mathcal{L}$, and indeed this is a necessary and sufficient condition for the existence of $X \rightarrow \mathbb{P}^n$, as we saw in Subsection [\[sub:linear\]](#sub:linear){reference-type="ref" reference="sub:linear"}.
:::
