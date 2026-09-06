---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-031-42-notations-for-categories
section_title: "Notations for categories"
section_number: 4.2
pages: 34-35
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
algebra notations, deﬁnitions and assumptions which will be frequently used below. Let C be
an additive unital monoidal category with tensor product ⊗ and direct sum⊕. The monoidal
structure is not necessary symmetric. We will denote the unit object ofC by 1C, or 1 if the cate-
gory is clear from context. The endomorphism algebra End(1) is always commutative, and we
assume that it is Noetherian. For any objectA∈C , the morphism spaceHom(1,A ) is a module
over End(1), and we assume that it is ﬁnitely generated. We assume that all morphism spaces
are positively graded. We denote by Kb(C) the homotopy category of bounded complexes of
objects inC and byK−(C) the homotopy category of bounded above complexes. Unless stated
otherwise, we will work with bounded above complexes and abbreviateK−(C) toK(C).
We will consider two types of “semi-inﬁnite completions” of the categoryC. The ﬁrst type
is the homotopy category K−(C) of bounded above complexes of objects inC (which is well-
known to also be a monoidal category). The other type is the category of certain inﬁnite sums
of objects inC, as in the following deﬁnition.
Deﬁnition 4.3. Assume thatC is graded, and the grading shift is denoted by A↦→ A(1). We
deﬁne its graded completionC↑ as follows. The objects are given by countable direct sums:
Ob(C↑) =
{ N⨁
i=−∞
Ai(i) for someN∈ Z
}
and the morphismsφ :⊕Ai(i)→⊕Bj(j) are collections of arrows{φij :Ai(i)→Bj(j)} for
alli,j , such that for eachi there are only ﬁnitely manyj such thatφij⁄= 0.
One can check thatC↑ andK−(C↑) inherit the tensor product fromC. Note that K−(C↑) is
endowed with both the grading (1) and the homological degree [1].
Note that the categoryC may have multiple gradings, and the notion of completion depends
on a speciﬁc choice of grading among these. For example, if C is graded by Zr, this accounts
to choosing a one-dimensional direction in Zr. To clarify homological algebra over C↑, we
present some examples.
Example 4.4. LetC be the category of graded ﬁnitely generated C[x]-modules. Consider the
following two-term complex inK−(C↑):
FIGURE 7.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 35
We can introduce an auxilary variabley of degree(−1) and rewrite the complex as following:
C[x,y ]
1+xy
−−−→C[x,y ].
At ﬁrst glance, one could think that since all horizontal arrows in Figure 7 are isomorphisms,
the complex is contractible. However, this is not the case, since a homotopy would be:
C[x,y ]
H
← −C[x,y ] such thatH(1 +xy) = (1 +xy)H = 1
A natural choice forH would be:
H(x,y ) = 1
1 +xy = 1−xy +x2y2−x3y3 +...,
but this is not a valid morphism inC↑ since there would be non-zero arrows from the top-most
copy of C[x] to all inﬁnitely many copies below it.
Remark 4.5. One can check that the homology of the complex in Figure 7 is isomorphic to
C[x,y ]/(1 +xy) = C[x,x−1].
