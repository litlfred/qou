---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-021-61-the-tangent-complex
section_title: "The tangent complex"
section_number: 6.1
pages: 30-32
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In this subsection we recall the deﬁnition of the Yetter-Davydov cohomology of
a fusion category C [28, 29, 6]. Deﬁne the functor
Tn : C ⊠··· ⊠ C| {z }
n times
→ C
byTn(A1,...,A n) =A1⊗···⊗ An, parenthesized from left-to-right for deﬁnite-
ness, and deﬁne Cn = End(Tn), the vector space of natural endomorphisms of
Tn. For n = 0, set C 0 = C. In terms of representative simple objects Xi, i∈I,
we have
Cn =
⨁
i1,...,in
Hom(X1⊗···⊗ Xn, X1⊗···⊗ Xn).
30
In string diagrams, we can write the components of c∈Cn as
.
For instance, a 1-cochain c∈C 1 is simply a collection of scalars ci∈ C, i∈I.
A 2-cochain A∈C 2 is a collection of morphisms Aij :Xi⊗Xj→Xi⊗Xj; this
amounts to a collection of linear operators
Ai
jk : Hom(Xk,Xi⊗Xj)→ Hom(Xk,Xi⊗Xj). (40)
Deﬁnition 6.1. The tangent complex of a fusion category C is the sequence of
C-vector spaces and linear maps
C 0 d0
−→C 1 d1
−→C 2 d2
−→C 3→..., d n =
n+1∑
k=0
(−1)kfn
k
where the maps fn
k :Cn→Cn+1 are deﬁned by
=
 ,
 =
=
∑
k,α
(Note that for c∈C 0 = C, (f 0
0 (c))i = idXi = (f 0
1 (c))i so that d0 = 0.)
Lemma 6.2. The tangent complex is a complex, i.e. dn+1dn = 0.
Proof. Follows from the identity
fn+1
k fn
m =fn+1
m+1fn
k 0≤k≤m≤n + 1. (41)
Fork =m = 0 or k =m =n + 1, (41) is just the resolution of the identity (6).
Fork⁄=m, (41) is just the interchange law in a monoidal category. In the other
cases, (41) takes the following form (we do the case k =m = 1, n = 2):
∑
m,α,p,β
=
∑
n,δ,q,γ
(42)
31
Pre-composing both sides of (42) with
and inserting the associator expansion (4), the left and right sides become the
same expression, namely
∑
m,α,β
(Fs
ijk)βmα
θtω
 .
Example 6.3. A 1-cocycle c∈ Z 1(C) is a collection of numbers ci such that
ck =ci +cj wheneverXk is a summand of Xi⊗Xj. A 2-cocycle A∈Z 2(C) is
a collection of linear operators Ai
jk as in (40) such that
−
 +
∑
γ,m,δ
(Fs
ijk)γmδ
αtβ


−


= 0.
Expanded out fully, this is the equation
∑
α
(At
jk)αωFγ′m′δ′
θtα −
∑
β
(As
it)βθFγ′m′δ′
βtω +
∑
γ
(As
m′k)γ′γFγm′δ′
θtω −
∑
δ
(Am
ij )δ′δFγ′m′δ
θtω
(43)
for all values of the free indices, where F≡Fs
ijk.
Deﬁnition 6.4. The Yetter-Davydov cohomology Hi(C) of a fusion category
C is the cohomology of its tangent complex.
The low-dimensional cohomology groups have the following interpretations
[28, 29, 6, 16]. The groupH 1(C) classiﬁes ﬁrst-order deformations of Aut⊗(idC),
H 2(C) classiﬁes ﬁrst-order deformations of the tensor product functor, and
H 3(C) classiﬁes ﬁrst-order deformations of the associator.
