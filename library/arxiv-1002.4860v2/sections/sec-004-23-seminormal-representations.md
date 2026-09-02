---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-004-23-seminormal-representations
section_title: "Seminormal representations"
section_number: 2.3
pages: 3-3
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
---
the results were originally worked out in [6]. For a new point of view and s ubstantial
generalization, see [2, section 5].
Let Par(n) denote the set of all integer partitions of n. To the partition λ = (λ1 ≥
λ2 ≥ · · · ), associate its Young diagram , that is, the left-justiﬁed diagram with λ1
boxes on the ﬁrst row, λ2 boxes on the second row, etc.
Let Tab(λ) denote the set of λ-tableaux. These are ﬁllings of the boxes in the Young
diagramλ by the numbers 1,...,n . Let Std(λ) denote the set of standardλ-tableaux,
namely those that increase across rows and down columns. The sym metric group Sn
acts on Tab( λ) via its natural action on the entries, although Std( λ) is not stable
under this action. For a tableau T ∈ Tab(λ), its residue sequence (i1,...,i n) ∈ Zn
is deﬁned by setting ir = b −a where the box labeled r in T appears in row a and
column b.
λ = T = 1 2
3
4 s2T = 1 3
2
4
Figure 1. The partition λ = (3, 1) ∈ Par(4) and standard tableaux T
and s2T. Here, T has residue sequence (0 , 1, −1, 2).
Fix a partition λ ∈ Par(n) and let S(λ) be the C(v)-vector space on basis {xT | T ∈
Std(λ)}. Let ( i1,...,i n) be the residue sequence of T and deﬁne ar(T),b r(T) ∈ C(v)
to be
(3) ar(T) = v −v−1
1 −v2(ir−ir+1), b r(T) = v−1 +ar(T).
Deﬁne actions of the generators H1,...,H n−1 of Hn on S(λ) by
(4) HrxT =ar(T)xT +br(T)xsrT,
where we interpret xsrT = 0 if srT is not a standard tableau.
Theorem 2.4 (Semi-normal representations). This action extends to make S(λ) into
a well-deﬁned Hn-module. Furthermore, the modules {S(λ) |λ ∈ Par(n)} constitute
a complete set of pairwise non-isomorphic irreducible modu les for Hn.
