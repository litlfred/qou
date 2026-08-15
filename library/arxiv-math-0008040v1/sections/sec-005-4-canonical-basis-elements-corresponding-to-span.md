---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh"
section_id: sec-005-4-canonical-basis-elements-corresponding-to-span
section_title: "Canonical basis elements corresponding to spanning vecto rs"
section_number: 4
pages: 8-9
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh — Let U be the quantum group associated to a Lie algebra g of type An."
---
Recall that for i, i′ ∈ χ n, the map T i′
i is deﬁned by T i′
i (a) = ψ i′ψ −1
i (a), for a ∈ Yi. Deﬁne T2 :
Z2 → Z2 byT2(a,b ) := (b,a ), and T3 : Z3 → Z3 byT3(a,b,c ) := (max(c,b −a),a +c, min(a,b −c)).
The maps T i′
i satisfy the following:
Proposition 4.1 (Berenstein and Zelevinsky)
(a) Suppose i, i′ ∈ χ n and that i = i′ except that (is,i s+1) = (i,j ) and (i′
s,i ′
s+1) = (j,i ) for some
index s and i,j ∈ [1,n ] with |i −j|> 1. Let a ∈ Nk and write a′ =T i′
i (a). Then we have a′
r =ar
for r<s or r>s + 1 and (a′
s,a ′
s+1) = T2(as,a s+1).
(b) Suppose i, i′ ∈χ n, and that i = i′ except that (is,i s+1,i s+2) = (i,j,i ) and (i′
s,i ′
s+1,i ′
s+2) = (j,i,j )
for some index s and i,j ∈ [1,n ] with |i −j| = 1. Let a ∈ Nk and write a′ =T i′
i (a). Then we have
a′
r =ar for r<s or r>s + 2 and (a′
s,a ′
s+1,a ′
s+2) = T3(as,a s+1,a s+2).
Proof: See [3, §§2.6, 2.7]. □
We need the following Lemma, which will help us to understand how spanning vectors of Lusztig
cones are related.
Lemma 4.2 (a) Suppose i, i′ ∈χ n and that i = i′ except that (is,i s+1) = (i,j ) and (i′
s,i ′
s+1) = (j,i )
for some index s and i,j ∈ [1,n ] with |i −j|> 1. Let a =a(c, i), respectively a(j, i), be a spanning
vector of Ci, and let a′ = a(c′, i′), respectively (j, i′), be the corresponding spanning vector of Ci′.
Here (c′, i′) is the chamber that (c, i) becomes when the commutation relation (i,j ) → (j,i ) is applied
to i. Then a′
r =ar for all r<s or r>s + 1, while (a′
s,a ′
s+1) = T2(as,a s+1).
(b) Suppose i, i′ ∈χ n and that i = i′ except that (is,i s+1,i s+2) = (i,j,i ) and (i′
s,i ′
s+1,i ′
s+2) = (j,i,j )
for some index s and i,j ∈ [1,n ] with |i −j| = 1. Let a =a(c, i), respectively a(j, i), be a spanning
vector of Ci. In this case, we suppose further that (c, i) is not the chamber of CD (i) involving
the substring (i,j,i ), so that there is a chamber (c′, i′) with P (c, i) = P (c′, i′). Let a′ = a(c′, i′),
respectively (j, i′). Then a′
r =ar for all r<s orr>s +1, while (a′
s,a ′
s+1,a ′
s+2) = T3(as,a s+1,a s+2).
Proof: Recall that the spanning vectors of Ci are obtained by inverting the deﬁning matrix Pi ofCi.
Part (a) follows immediately from the deﬁnition of Pi. Suppose we are in situation (b). Consider
the case where a =a(c, i). Since ( c, i) is not the chamber corresponding to ( i,j,i ) = (is,i s+1,i s+2),
we must have that a is perpendicular to the row of Pi corresponding to this chamber. In the case
where a =a(j, i), this is also true. So, in either case, we see that as+1 =as +as+2. It follows from
the deﬁnition of T3 that T3(as,a s+1,a s+2) = ( as+2,a s+1,a s). Since the ordering on the positive
roots induced by i agrees with that induced by i′ except that the roots in positions s ands + 2 are
exchanged, the fact that a′ is as claimed in the statement above follows from Theorem 3.1 (a) and
(b). □
Using Proposition 4.1 and Lemma 4.2 we have:
Corollary 4.3 Let i, i′ ∈ χ n, and let (c, i), (c′, i′) be chambers with P (c, i) = P (c′, i′). Then
T i′
i (a(c, i)) = a(c′, i′). Also, for j ∈ [1,n ], T i′
i (a(j, i)) = a(j, i′).
8
a
.
. 2
1
2 .
.
.
n + 2 −b.
.
n +a−
b + 1
.
.
.
.......................................................................................................................................................................................................... .................................................................................................................................................................................................................................................. .......................................................................................................................................................................................................... ..................................................................................................................................................................................................................................................
Type L
b − 1
b − 2
.
.b −a.
.
.
.
n + 1 −a
.
.
.
n
.
.
.
.
.......................................................................................................................................................................................................... .................................................................................................................................................................................................................................................. .......................................................................................................................................................................................................... ..................................................................................................................................................................................................................................................
Type R
