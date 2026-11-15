---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-011-31-proof-of-theorem-for-links
section_title: "Proof of Theorem ?? for links"
section_number: 3.1
pages: 10-13
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
We will formulate and prove an analog of Theorem 1 (see Theorem 3 below)
for colored links. Our proof will use a state-sum deﬁnition of the colored Jones
function, coming from a representation of the quantum group Uq(sl2), as was
discovered by Reshetikhin and Turaev in [29, 32].
Suppose L is a framed, oriented link of p components. Then the colored Jones
function JL : Np →Z[q±1/4] = Z[v±1/2] can be deﬁned using the representa-
tions of braid groups coming from the quantum group Uq(sl2).
Theorem 3 The colored Jones function JL is q–holonomic.
Proof We will present the deﬁnition of JL in the form most suitable for us.
Let V (n) be the n–dimensional vector space over the ﬁeld Q(v1/2) with basis
{e0, e1, . . . , en−1}, with V (0) the zero vector space.
Fix a positive integer m. A linear operator
A: V (n1) ⊗· · · ⊗V (nm) →V (n′
1) ⊗· · · ⊗V (n′
m)
can be described by the collection
Ab1,...,bm
a1,...,am ∈Q(v1/2),
where
A(ea1 ⊗· · · ⊗eam) =
X
b1<n′
1,...,bm<n′m
Ab1,...,bm
a1,...,am eb1 ⊗· · · ⊗ejm.
We will call (a1, . . . , am, b1, . . . , bm) the coordinates of the matrix entry Ab1,...,bm
a1,...,am
of A, with respect to the given basis.
The building block of our construction is a pair of functions f±: Z5 →Z[v±1/2],
given by
f+(n1, n2;a, b, k)
:= (−1)kv−((n1−1−2a)(n2−1−2b)+k(k−1))/2
 b + k
k

{n1 −1 + k −a}k,
f−(n1, n2;a, b, k)
:= v((n1−1−2a−2k)(n2−1−2b+2k)+k(k−1))/2
 a + k
k

{n2 −1 + k −b}k.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1263
The reader should not focus on the actual, cumbersome formulas. The main
point is that:
Fact 1
•
f+ and f−are q–proper hypergeometric and thus q–holonomic in all
variables.
For each pair (n1, n2) ∈N2 we deﬁne two operators
B+(n1, n2), B−(n1, n2): V (n1) ⊗V (n2) →V (n2) ⊗V (n1)
by
(B+(n1, n2))c,d
a,b
:=
f+(n1, n2; a, b, c −b) δc−b,a−d,
(B−(n1, n2))c,d
a,b
:=
f+(n1, n2; a, b, b −c) δc−b,a−d,
where δx,y is Kronecker’s delta function. Although the coordinates (a, b, c, d)
of the entry B±(n1, n2))c,d
a,b of the operators B±(n1, n2) are deﬁned for 0 ≤
a, b ≤n1 and 0 ≤c, d ≤n2, the above formula makes sense for all non-negative
integers a, b, c, d. This will be important for us. The following lemma is obvious.
Lemma 3.1 The discrete functions B±(n1, n2)c,d
a,b are q–holonomic with re-
spect to the variables (n1, n2, a, b, c, d).
If we identify V (n) with the simple n–dimensional Uq(sl2)–module, with ei, i =
0, . . . , n −1 being the standard basis, then B+(n1, n2), B−(n1, n2) are respec-
tively the braiding operator and its inverse acting on V (n1) ⊗V (n2). This fact
follows from the formula of the R–matrix, say, in [17, Chapter 3]. In particular,
B−(n1, n2) is the inverse of B+(n1, n2). If one allows a, b, c, d in B±(n1, n2)c,d
a,b to
run the set N, then B±(n1, n2)c,d
a,b deﬁne the braid action on the Verma module
corresponding to V (n1), V (n2).
Let Bm be the braid group on m strands, with standard generators σ1, ..., σm−1:
σi =
...
...
i+1
1
m
i
For each braid β ∈Bm and (n1, . . . , nm) ∈Nm, we will deﬁne an operator
τ(β) = τ(β)(n1, . . . , nm),
τ(β): V (n1) ⊗· · · ⊗V (nm) →V (n ¯β(1)) ⊗· · · ⊗V (n ¯β(m)),
Geometry & Topology, Volume 9 (2005)
1264
Stavros Garoufalidis and Thang T Q Lˆe
where ¯β is the permutation of {1, . . . , m} corresponding to β. The operator
τ(β) is uniquely determined by the following properties: For an elementary
braid σi, we have:
τ(σ±1
i
) = id⊗i−1 ⊗B±(ni, ni+1) id⊗m−i−1 .
In addition, if β = β′β′′, then τ(β) := τ(β′)τ(β′′). It is well-known that τ(β)
is well-deﬁned.
From Fact 0 and Lemma 3.1 it follows that
Lemma 3.2 For any braid β ∈Bm, the discrete function τ(β)(n1, . . . , nm),
considered as a function with variables n1, . . . , nm and all the coordinates of
the matrix entry, is q–holonomic.
Let K be the linear endomorphism of V (n1) ⊗· · · ⊗V (nm) deﬁned by
K(ei1 ⊗· · · ⊗eim) = vn1+···+nm−2i1−···−2im−m ei1 ⊗· · · ⊗eim.
The inverse operator K−1 is well-deﬁned.
Corollary 3.3 For any braid β ∈Bm, the discrete function
˜τ(β) := τ(β)(n1, . . . , nm) × K−1
is q–holonomic in n1, . . . , nm all all of the coordinates of the matrix entry.
In general, the trace of ˜τ(β) is called the quantum trace of τ(β). Although the
target space and source space maybe diﬀerent, let us deﬁne the quantum trace
of τ(β)(n1, . . . , nm)) by
trq(β)(n1, . . . , nm) :=
X
1≤i≤m
X
0≤ai<ni
˜τ(β)(n1, . . . , nm)a1,...,am
a1,...,am.
It follows from Fact 0 that trq(β)(n1, . . . , nm) is q–holonomic in n1, . . . , nm.
Restricting this function on the diagonal deﬁned by ni = n ¯βi, i = 1, . . . , m, we
get a new function Jβ of p variables, where p is the number of cycles of the
permutation ¯β.
Suppose a framed link L can be obtained by closing the braid β. Then the
colored Jones polynomial JL is exactly Jβ . Hence Theorem 1 follows.
Remark 3.4 In general, JK(n) contains the fractional power q1/4. If K has
framing 0, then JK′(n) := JK(n)/[n] ∈Z[q±1]. See [20].
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1265
Remark 3.5 There is a variant of the colored Jones function JL′ of a colored
link L′ where one of the components is broken. If β is a braid as above, let us
deﬁne the broken quantum trace tr′
β by
tr′
q(β)(n1, . . . , nm) :=
X
2≤i≤m
X
0≤ai<ni
˜τ(β)(n1, . . . , nm)a1,...,am
a1,...,am|a1=0.
Restricting this function on the diagonal deﬁned by ni = n ¯βi, i = 1, . . . , m, we
get a new function Jβ′ of p variables, where p is the number of cycles of the
permutation ¯β.
If L′ denotes the broken link which is the closure of all but the ﬁrst strand of
β, then the colored Jones function JL′ of L′ satisﬁes JL′ = Jβ′ .
If L denotes the closure of the broken link L′, then we have:
JL = JL′ × [λ]
where λ is the color of the broken component of L′.
