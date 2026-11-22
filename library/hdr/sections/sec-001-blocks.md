---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-001-blocks
section_title: "Blocks"
section_number: null
pages: 16-16
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
toc_source: outline
doc_brief: "Hecke algebras, generalisations and representation theory — 31 sections: Front matter; Algebras of Finite Type; Blocks"
---
Blocks
We deﬁne the block-idempotents of A to be the primitive idempotents of the centre Z(A) of A. Let K be
a ﬁeld containing R such that the algebra KA is semisimple. Then KA is isomorphic to a direct product
of simple algebras,
KA ∼=
Y
V ∈Irr(KA)
MV ,
where MV is a simple K-algebra. For all V ∈Irr(KA), we denote by πV : KA ↠MV the projection
onto the V -factor and by eV the element of KA such that
πV ′(eV ) =
 1MV
if V = V ′,
0
if V̸ = V ′.
We have that the elements {eV }V ∈∈Irr(KA) are the block-idempotents of KA. Further, there exists a
unique partition Bl(A) of Irr(KA) that is the ﬁnest with respect to the property:
∀B ∈Bl(A),
eB :=
X
V ∈B
eV ∈A.
The elements {eB}B∈Bl(A) are the block-idempotents of A. We have A ∼= Q
B∈Bl(A) AeB. From now on,
we will refer to the parts of Bl(A) as the blocks of the algebra A.
Example 1.1 Let G be a ﬁnite group. The group algebra Z[G] has only one block, which contains all
the irreducible representations of C[G].
