---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-010-22-algebraic-quantum-groups
section_title: "Algebraic Quantum Groups"
section_number: 2.2
pages: 6-6
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
In this subsection we brieﬂy outline those aspects of the theory of aqg that will be needed in the sequel. For
the details and proofs, see the original references [35, 37].
Every algebra will be a (not necessarily unital) associative algebra ov er the complex ﬁeld C. The identity
map on a set V will be denoted by ι. If V and W are linear spaces, V ′ denotes the linear space of linear
functionals on V andV ⊗W denotes the linear space tensor product of V andW . The ﬂip map σ fromV ⊗W
to W ⊗V is the linear map sending v ⊗w onto w ⊗v, for all v ∈ V and w ∈ W . If V and W are Hilbert
spaces, V ⊗W denotes their Hilbert space tensor product; we denote by B(V ) and B0(V ) the C*-algebras of
bounded linear operators and compact operators on V , respectively. If V and W are algebras, V ⊗W denotes
their algebra tensor product. If V and W are C*-algebras, then V ⊗W will denote their C*-tensor product
with respect to the minimal C*-norm.
An algebra A is non-degenerate if for any a ∈A such that ab = 0 for all b ∈ A or ba = 0 for all b ∈A, we
havea = 0. Obviously, all unital algebras are non-degenerate. If A and B are non-degenerate algebras, so is
A ⊗B. From now on all algebras are assumed to be non-degenerate.
Let A be a ∗-algebra and denote by End A the unital algebra of linear maps from A to itself. Let
M (A) = {x ∈ EndA | ∃y ∈ EndA such that x(a)∗b =a∗y(b) ∀a,b ∈A}.
Then M (A) is a unital subalgebra of End A. The linear map y associated to a given x ∈ M (A) is uniquely
determined by non-degeneracy and we denote it by x∗. The unital algebra M (A) becomes a ∗-algebra when
endowed with the involution x ↦→x∗. This unital ∗-algebra is called the multiplier algebra of A.
Suppose that A is an ideal in a ∗-algebra B. For b ∈ B, deﬁne Lb ∈ M (A) by Lb(a) = ba, for all a ∈ A.
Then the map L : B → M (A), b ↦→Lb, is a homomorphism. If A is an essential ideal in B in the sense that
an element b of B is necessarily equal to zero if ba = 0, for all a ∈ A, or ab = 0, for all a ∈ A, then L is
injective. In particular, A is an essential ideal in itself (by non-degeneracy) and therefore w e have an injective
homomorphism L : A → M (A). We identify the image of A under L with A. Then A is an essential ideal of
M (A). (In fact, M (A) is the ‘largest’ algebra containing A as an essential ideal.) Obviously, M (A) = A iﬀ A
is unital.
IfA andB are ∗-algebras, then it is easily veriﬁed that A⊗B is an essential self-adjoint ideal in M (A)⊗M (B).
Hence, by the preceding remarks, there exists a canonical inject ive ∗-homomorphism from M (A) ⊗M (B) into
M (A ⊗B). We use this to identify M (A) ⊗M (B) as a unital ∗-subalgebra of M (A ⊗B). In general, these
algebras are not equal. A linear map π : A → B is said to be non-degenerate if π(A)B = B and Bπ(A) = B.
Here, as elsewhere, π(A)B denotes the linear span of {π(a)b |a ∈A, b ∈B}. Whenever π is non-degenerate
and multiplicative (resp. non-degenerate and antimultiplicative), th ere exists a unique extension to a unital
homomorphism (resp. antihomomorphism) π :M (A) →M (B). We shall henceforth use the same symbol π to
denote the original map and its extension π. A representation of a ∗-algebra is a non-degenerate homomorphism
π :A →B(K), where K is a Hilbert space.
If ω is a linear functional on A and x ∈M (A), we deﬁne the linear functionals xω and ωx on A by setting
(xω)(a) = ω(ax) and (ωx)(a) = ω(xa), for all a ∈A. We need the leg numbering notation. Take three ∗-algebras
A, B, C. It can be shown that there exists a non-degenerate ∗-homomorphism θ13 :A ⊗C →M (A ⊗B ⊗C)
such that θ13(a ⊗c) = a ⊗ 1 ⊗c, for all a ∈ A, c ∈ C. Thus, it has a unique extension to M (A ⊗C). Set
x13 =θ13(x), for all x ∈M (A ⊗C). The other variants of the leg numbering notation are deﬁned simila rly.
The triple product A ⊗A ⊗A is an essential ideal of both M (A ⊗A) ⊗A and A ⊗ M (A ⊗A), thus
M (M (A ⊗A) ⊗A) ⊂M (A ⊗A ⊗A) and M (A ⊗M (A ⊗A)) ⊂M (A ⊗A ⊗A).
Definition 2.3 A multiplier Hopf ∗-algebra (A, ∆) consists of a ∗-algebraA and a ∗-homomorphism ∆ from
A into M (A ⊗A) such that
1. (∆ ⊗ι)∆ = ( ι ⊗ ∆)∆ .
