---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-006-21-proof-of-the-basic-lemma-the-problem-is-that
section_title: "Proof of the Basic Lemma. The problem is that one cannot necessarily"
section_number: 2.1
pages: 4-6
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
deﬁne an algebraic intersection number between two properly embe dded surfaces,
since it might be possible to eliminate intersections by pushing them oﬀ t o inﬁnity.
We overcome this problem by proving the existence of an immersed clo sed surface
˜Σ 2(F ) which is equal to (1 − q)2(1 + qt) ˜Σ( F ) outside a small neighborhood of the
punctures.
Let F be a fork. Let the endpoints of T (F ) be pi and pj. Let ν(pi) and ν(pj)
be disjoint ǫ-neighborhoods of pi and pj respectively such that ν(pk) ∩ P = {pk}
for k = i, j. Let U be the set of {x, y} ∈ C such that at least one of x and y
lies in ν(pi) ∪ ν(pj). Fix a basepoint u0 = {u1, u2} ∈ U , where u1 ∈ ν(pi) and
u2 ∈ ν(pj). Let ˜U be the pre-image of U in ˜C. Choose a lift ˜ u0 of u0 to ˜C. We
start by analyzing π1(U, u0).
Using the arcs shown in Figure 2, we deﬁne the following elements of π1(U, u0).
a1 = {γ1, u2},
a2 = {u1, γ2},
b1 = {α1, β1β2β3}{α2α3, u1},
b2 = {α1α2α3, β1}{u2, β2β3}.
Note that b1 and b2 are homotopic in C, but not in U .
The following relations hold in π1(U ).
[a1, a2] = 1 ,(1)
[a1, b1a1b1] = 1 ,(2)
[a2, b2a2b2] = 1 .(3)
The ﬁrst of these is obvious. The second follows from the fact that b1a1b1 is equal
in π1(U ) to {u1, δ}, where δ is a curve based at u2 which passes counterclockwise
around p1 and u1. The third follows by a similar argument.
BRAID GROUPS ARE LINEAR 5
We now analyze π1( ˜U , ˜u0). Let i : U → C be the inclusion map and let i∗ be
the induced map on fundamental groups. Then π1( ˜U ) is the kernel of the map φi∗.
We deﬁne the following elements of π1( ˜U , ˜u0).
a = a−1
2 a1,
b = b−1
2 b1,
c = a−1
1 b−1
1 a1b1,
d = a−1
2 b−1
2 a2b2.
If x ∈ π1( ˜U , ˜u0) and y ∈ π1(U, u0) then the conjugate xy = y−1xy is also an element
of π1( ˜U , ˜u0). The following relations hold in π1( ˜U , ˜u0).
aa1 = a,(4)
cb1a1 c = 1 ,(5)
db2a2d = 1 ,(6)
dbab1 = aba1c.(7)
To see this, rewrite these relations in terms of a1, a2, b1 and b2. The ﬁrst three
translate into equations (1) to (3). The fourth translates into a t rivial identity.
If x ∈ π1( ˜U ), let [ x] denote the corresponding element of H1( ˜U ). Note that if
x ∈ π1( ˜U ) and y ∈ π1(U ) then [ xy] = φ(y)−1[x]. The relations given in equations
(4) to (7) give rise to the following relations in H1( ˜U ).
(q−1 − 1)[a] = 0 ,
(q−1t−1 + 1)[c] = 0 ,
(q−1t−1 + 1)[d] = 0 ,
(q−1 − 1)[b] = ( q−1 − 1)[a] − [c] + [d].
Combining these relations, we obtain the following.
(1 − q)2(1 + qt)[b] = 0 .
Let [ ˜Σ( F )] be the element of H2( ˜C, ˜U ) represented by ˜Σ( F ). The long exact
sequence of relative homology gives us the following exact sequence of Λ-modules
H2( ˜C)
j∗
→ H2( ˜C, ˜U )
∂
→ H1( ˜U ).
But ∂[ ˜Σ( F )] = [ b]. It follows that
(1 − q)2(1 + qt)[ ˜Σ( F )] = j∗[ ˜Σ 2(F )]
for some [ ˜Σ 2(F )] ∈ H2( ˜C) represented by some closed immersed surface ˜Σ 2(F ).
Let N be a noodle. Choose ν(pi) and ν(pj) small enough so as not to intersect
N . Then
(1 − q)2(1 + qt)⟨N, F ⟩ =
∑
a,b ∈Z
qatb(qatb ˜Σ( N ), ˜Σ 2(F )).
Now ( qatb ˜Σ( N ), ˜Σ 2(F )) is the algebraic intersection number between a properly
embedded surface and an immersed closed surface, so is well-deﬁne d.
Suppose σ is an element of the kernel of the Lawrence-Krammer representa tion.
Then σ( ˜Σ 2(F )) and ˜Σ 2(F ) represent the same element of homology, so have the
same algebraic intersection with any qatb ˜Σ( N ). Thus ⟨N, σ(F )⟩ = ⟨N, F ⟩.
