---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-001-notation
section_title: "Notation"
section_number: null
pages: 3-4
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.965
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
In this paper we work over a base commutative, associative ring $R$ with unity. If not stated otherwise a fiber category will be a category fibered in groupoids over $\mathop{\mathrm{\textup{Aff}}}/R$, the category of affine schemes over $\mathop{\mathrm{\textup{Spec}}}R$, or, equivalently, the opposite of the category of $R$-algebras. An fpqc stack will be a stack for the fpqc topology.

A map $f\colon\stX'\arr\stX$ of fibered categories is called representable if for all maps $T\arr\stX$ from an affine scheme (or an algebraic space) the fiber product $T\times_{\stX}\stX'$ is (equivalent to) an algebraic space.

Given a flat and affine group scheme $G$ over $R$ we denote by $\mathop{\mathrm{\textup{B}}}_{R}G$ (or simply $\mathop{\mathrm{\textup{B}}}G$ when the base ring is clear) the stack of $G$-torsors for the *fpqc* topology, which is an fpqc stack with affine diagonal. When $G\arr\mathop{\mathrm{\textup{Spec}}}R$ is finitely presented (resp. smooth) then $\mathop{\mathrm{\textup{B}}}_{R}G$ coincides with the stack of $G$-torsors for the fppf (resp. �tale) topology.

By a "subcategory" of a given category we mean a "full subcategory" if not stated otherwise.

We assume the notations, definition and results of [@Tonini2014 Section 1]. In particular: the notion of pseudo-algebraic and quasi-compact fibered categories or maps between them; flat maps of fibered categories; quasi-coherent sheaves and their functoriality; quasi-coherent sheaves on a fibered category. In particular $\mathop{\mathrm{\textup{QCoh}}}(\stX)$ and $\mathop{\mathrm{\textup{QAlg}}}(\stX)$ denotes the category of quasi-coherent sheaves and quasi-coherent algebras on $\stX$ respectively.

If $\stY_{i}$ for $i\in I$ is a set of fibered categories over $R$ then $\sqcup_{i}\stY_{i}$ is defined as the fibered category over $R$ whose objects over an $R$-algebra $A$ are tuples consisting of a decomposition $\mathop{\mathrm{\textup{Spec}}}A=\sqcup_{i}U_{i}$ into open and closed subsets and $y_{i}\in\stY_{i}(U_{i})$. In particular if $\stX$ is a fibered category with maps $\stY_{i}\to\stX$ then a map $$\bigsqcup_{i\in I}\stY_{i}\to\stX$$ is well defined provided that $\stX$ is a Zariski stack.

If $\E$ is a vector bundle over a category fibered in groupoids $\stX$ then the locus $\stX_{n}\to\stX$ where $\E$ has rank $n$ is an open and closed immersion. Moreover there is a map $\stX\to\sqcup_{n}\stX_{n}$ (which is an equivalence if $\stX$ is a Zariski stack) and if $\stX$ is quasi-compact, then all $\stX_{n}$ are empty but finitely many.

If $\E$ is a vector bundle on a fibered category $\stX$ we can define $\det\E$ as $$\det\E=(\bigoplus_{n\in\N}\Lambda^{n}(\E_{|\stX_{n}}))_{|\stX}$$ which is compatible with the usual notion of determinant for vector bundles of fixed rank.
