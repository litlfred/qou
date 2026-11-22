---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three"
section_id: sec-005-physical-applications
section_title: "Physical applications"
section_number: null
pages: 23-25
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.991
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three — We classify connected ´etale algebras A’s in pre-modular fusion categories B with rank(B) ≤3 including"
---
In this section, we discuss physical applications of the classification results.

Consider a two-dimensional $\mathcal C$-symmetric gapped phase (an existence of braiding is not assumed at this level). It is known [@TW19; @HLS21] that such phases stand in bijection with $\mathcal C$-module categories $$\{\text{2d }\mathcal C\text{-symmetric gapped phases}\}\cong\{\mathcal C\text{-module categories }\mathcal M\}.\label{1to1}$$ In particular, ground state degeneracy (GSD) in the LHS is given by $\text{rank}(\mathcal M)$ of a module category $\mathcal M$ in the RHS. Therefore, we can translate physical problems in the LHS to mathematical problems in the RHS. One of the most important physical problems is whether the $\mathcal C$ symmetry is spontaneously broken or not. In this setup, a spontaneous symmetry breaking (SSB) in the LHS is defined as follows:

**Definition.** [@KK23GSD] Let $\mathcal C$ be a fusion category and $\mathcal M$ be a (left) $\mathcal C$-module category describing a $\mathcal C$-symmetric gapped phase. A symmetry $c\in\mathcal C$ is called *spontaneously broken* if $\exists m\in\mathcal M$ such that $c\triangleright m\not\cong m$. We also say $\mathcal C$ *is spontaneously broken* if there exists a spontaneously broken object $c\in\mathcal C$. A categorical symmetry $\mathcal C$ is called *preserved* (i.e., not spontaneously broken) if all objects act trivially.

With the definition, we can show a

**Lemma.** [@KK23GSD] *Let $\mathcal C$ be a fusion category and $\mathcal M$ be an indecomposable (left) $\mathcal C$-module category. Then, $\text{rank}(\mathcal M)>1$ implies SSB of $\mathcal C$ (i.e., $\mathcal C$ is spontaneously broken).*

Therefore, in two-dimensional gapped phases, we can mathematically prove SSB of a (categorical) symmetry $\mathcal C$ by classifying $\mathcal C$-module categories. In particular, if $\mathcal M$ is finite, it is known [@O01; @EGNO15] that $\exists A\in\mathcal C$ such that $\mathcal M\simeq\mathcal C_A$. In classifying such module categories, it is natural to assume $A$ be connected étale. (Note that we also assume ambient categories be pre-modular at this point. There are infinitely many examples in this class, relevant deformations of rational conformal field theories.) Then, our classification results can be translated to physics side. We arrive the

**Theorem.** *Let $\mathcal B$ be a pre-modular fusion category and $A\in\mathcal B$ a connected étale algebra. Suppose two-dimensional $\mathcal B$-symmetric gapped phases are described by indecomposable $\mathcal B_A$'s. Then, the gapped phases have* $$\text{GSD}\in\begin{cases}\{1\}&(\mathcal B\simeq\text{Vect}_{\mathbb C}),\\\{1,2\}&(\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^1\ (\text{two with }(\ref{Z2etale}))),\\\{2\}&(\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha\text{ (the other 14)}),\\\{2\}&(\mathcal B\simeq\text{Fib}),\\\{1,3\}&(\mathcal B\simeq\text{Vec}_{\mathbb Z/3\mathbb Z}^1\text{ with }h_X=h_Y=0),\\\{3\}&(\mathcal B\simeq\text{Vec}_{\mathbb Z/3\mathbb Z}^1\text{ with }h_X=h_Y=\pm\frac13),\\\{3\}&(\mathcal B\simeq\text{Ising}),\\\{1,2,3\}&(\mathcal B\simeq\text{Rep}(S_3)\ (\text{two with }(d_Y,h_Y)=(2,0)),\\\{3\}&(\mathcal B\simeq\text{Rep}(S_3)\ (\text{the other six})),\\\{3\}&(\mathcal B\simeq psu(2)_5).\end{cases}$$ *In particular, categorical symmetries $\mathcal B$'s are spontaneously broken for* $$\mathcal B\simeq\begin{cases}\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha\text{ with }(d_X,h_X)\neq(1,0),\\\text{Fib},\\\text{Vec}_{\mathbb Z/3\mathbb Z}^1\text{ with }h_X=h_Y=\pm\frac13,\\\text{Ising},\\\text{Non-symmetric }\text{Rep}(S_3),\\\text{Symmetric }\text{Rep}(S_3)\text{ with }d_Y=-1,\\psu(2)_5.\end{cases}$$

**Remark.** As noted in [@KK23GSD] Example 6, commutativity of an algebra seems too strong; a numerical computation suggests an existence of two-dimensional $\mathcal B$-symmetric gapped phase described by $\mathcal B_A$ with non-commutative connected separable algebra $A\in\mathcal B$.
