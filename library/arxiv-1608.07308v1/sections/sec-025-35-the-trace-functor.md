---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-025-35-the-trace-functor
section_title: "The trace functor"
section_number: 3.5
pages: 23-24
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.924
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:trace label="sub:trace"}

We will henceforth write $R_n = \mathbb{C}[x_1,...,x_n]$ to avoid confusion as to which number $n$ we are considering. For an extra variable $x_{n+1}$, we consider the category: $$\label{eqn:upgrade}
\mathrm{SBim}_n[x_{n+1}]$$ of Soergel bimodules which are equipped with an additional endomorphism denoted by $x_{n+1}$ that commutes with the action of $R_n$. In other words, $\mathrm{SBim}_n[x_{n+1}]$ is the Karoubian envelope of the smallest full subcategory of $R_{n+1}\text{--mod--}R_{n+1}$ that contains the modules $B_1,\ldots B_{n-1}$ and is closed under $\otimes_{R_{n+1}}$ and grading shifts. It is easy to see that the functors: $$\mathrm{SBim}_n[x_{n+1}] \xtofrom{} \mathrm{SBim}_n$$ that forget the action of $x_{n+1}$, respectively tensor with $\mathbb{C}[x_{n+1}]$, are adjoint with respect to each other. We will now recall the functors $I$ and $\mathop{\mathrm{Tr}}$ defined in [@Hog], upgraded to the level of the category [\[eqn:upgrade\]](#eqn:upgrade){reference-type="eqref" reference="eqn:upgrade"}. At the level of additive categories, these functors are quite simple: $$I: \mathrm{SBim}_n[x_{n+1}] \longrightarrow \mathrm{SBim}_{n+1}$$ is the full embedding. Meanwhile: $$\mathop{\mathrm{Tr}}: \mathrm{SBim}_{n+1} \longrightarrow \mathrm{SBim}_n[x_{n+1}], \qquad M \mapsto \text{Ker} \left(M \xrightarrow{x_{n+1} \otimes 1 - 1 \otimes x_{n+1}}  M \right)$$ As shown in [@Hog], these functors can be upgraded to the derived categories: $$D^b\left(\mathrm{SBim}_n[x_{n+1}]\right) \xtofrom[I]{\mathop{\mathrm{Tr}}}  D^b\left(\mathrm{SBim}_{n+1}\right)$$ where the trace functor now encodes the full operation of multiplication by $x_{n+1} \otimes 1 - 1 \otimes x_{n+1}$, instead of simply the kernel: $$\mathop{\mathrm{Tr}}(M) = \left[ M \xrightarrow{x_{n+1} \otimes 1 - 1 \otimes x_{n+1}}  M \right].$$

::: remark
When working in the upgraded category [\[eqn:upgrade\]](#eqn:upgrade){reference-type="eqref" reference="eqn:upgrade"} rather than $\mathrm{SBim}_n$, one must be careful with Markov invariance, i.e. the statement ([@Kh]) that for $M\in \mathrm{SBim}_{n+1}$ one has: $$\mathop{\mathrm{Tr}}(M \otimes \sigma_n^{\pm 1})\simeq M \ \in \mathrm{SBim}_n$$ In the upgraded category, this equation becomes: $$\label{eqn: R1 upgraded}
\mathop{\mathrm{Tr}}(M \otimes \sigma_n^{\pm 1})\simeq \left[M\otimes \mathbb{C}[x_{n+1}] \xrightarrow{x_n\otimes 1- 1 \otimes x_{n+1}} M\otimes \mathbb{C}[x_{n+1}] \right] \ \in \mathrm{SBim}_n[x_{n+1}]$$ The proof is straightforward and we leave it to the reader. Remark that in the category $\mathrm{SBim}_n$ the complex [\[eqn: R1 upgraded\]](#eqn: R1 upgraded){reference-type="eqref" reference="eqn: R1 upgraded"} is quasi-isomorphic to $M$, but this is no longer true in $\mathrm{SBim}_n[x_{n+1}]$.

<figure id="fig:R1">

<figcaption>Markov move in <span class="math inline">SBim<sub><em>n</em></sub>[<em>x</em><sub><em>n</em> + 1</sub>]</span></figcaption>
</figure>
:::
