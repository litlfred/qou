---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-002-12-main-result
section_title: "Main result"
section_number: 1.2
pages: 4-5
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
quotient Hilb f ree
1,n = ﬁHilb
f ree
1,n /B, where
ﬁHilb
f ree
1,n ={(X,Y,v )∈ b× n×V| C⟨X,Y⟩v =V}
is an open subset of the product n×b×V (n, b⊂ gln(V ) being the nilpotent radial and Borel subalgebra), the
Borel subgroupB⊂ GLn acts on the ﬁrst two factors by conjugation and V is its fundamental representation.
Denote a ﬂag V• = (V1⊂···⊂ Vn−1⊂ Vn = V )∈ Fl and denote a point in the cotangent bundle T ∗Fl
as a pair ( Y,V •), where Y is a nilpotent matrix preserving the ﬂag: YV i⊂Vi−1.
In order to avoid a quotient by a non-reductive group B we can deﬁne Hilb f ree
1,n equivalently as a GIT
GLn-quotient of the space of quadruples ( X,Y,V •,v )∈ g×T ∗Fl×V such that C⟨X,Y⟩v =V andXV •⊂V•.
The fact that these deﬁnitions match follows from covering ﬁHilb1,n by aﬃne charts with free B-action, for
details see proposition 13.1. The aﬃne cover also provides a ”hands o n” description of the algebraic structure
of the quotient manifold.
Let us denote by B∨ the trivial vector bundle over ﬁHilb
f ree
1,n with the ﬁber V , we use the same notation
for its descent to the B-quotient. Respectively,B is the vector bundle dual to B∨.
The two-dimensional torus Tsc = C∗× C∗ acts on Hilb f ree
1,n by scaling X,Y : an element ( λ,µ )∈Tsc turns
a pair of matrices (X,Y ) into (λ−2X,λ 2µ2Y ). We refer to the weights of this action as q-degree and t-degree.
The torus Tsc acts on the space V by (λ,µ )·v =λv, that is the vectors of V have degree t. We use notation
qktl for the shift of the Tsc-action:
(λ,µ )(qktl·x) = λkµl(λ,µ )·x.
4
We denote by Dper
Tsc (Hilbf ree
1,n ) the derived category of two-periodic complexes on Hilb f ree
1,n which are Tsc-
equivariant. Let Brn denote a braid group with n strands and let wr( β) denote the writhe of a braid β
deﬁned as the diﬀerence between the positive and negative crossin gs. Our main result is the construction of
the object
Sβ∈Dper
Tsc (Hilbf ree
1,n ),
such that the hypercohomology of the complex
Hk(β) := H(Sβ⊗∧ kB)
deﬁnes an isotopy invariant of L(β). To simplify notations we assume Hk(... ) = 0 for k /∈{ 0, 1,...,n }.
Theorem 1.1. For any β∈ Brn the triply graded space:
H(β) :=⊕k∈ZHk(β),
withHk(β) doubly graded deﬁned by
Hk(β) := q−wr(β)+n· H(k−wr(β)+n−1)/2(β),
is an isotopy invariant of the braid closure L(β).
Let us also introduce a notation for the graded pieces of Hk:Hi,j,k⊂H k is the subspace of vectors that
are of weight qitj. We show that our invariant categoriﬁes HOMFLY-PT polynomial.
Theorem 1.2. The bi-graded Euler characteristic of Hk(β) is equal to the HOMFLY-PT polynomial of the
link L(β):
P ( L(β)) =
∑
i,j,k∈Z
(−1)jqiak dimHi,j,k(β).
The ﬁrst categoriﬁcation of HOMFLY-PT polynomial was discovered by Khovanov and Rozansky [27]
and it is natural to expect that the homology theory from this pape r coincides with one from [27]. We do
not have a proof for a match of these theories.
