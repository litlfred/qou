---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-049-87-poincare-series
section_title: "Poincare series"
section_number: 8.7
pages: 66-67
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
Proposition 8.12. For any standard Young tableau of size n, the bigraded Poincar´e series of
graded algebras ˚AT (∗) are given by the following formulas:
(8.21) P ( ˚AT (C2)) = (1−q)−n(1−t)−n
n∏
i=1
1
1−z−1
i
∏
1≤i<j≤n
ζ
(zi
zj
)
(8.22) P ( ˚AT (C)) = (1−q)−n
n∏
i=1
1
1−z−1
i
∏
1≤i<j≤n
ζ
(zi
zj
)
(8.23) P ( ˚AT (point)) =
n∏
i=1
1
1−z−1
i
n∏
i=2
1
1−qtzi/zi+1
∏
1≤i<j≤n
ζ
(zi
zj
)
where
ζ(x) = (1−x)(1−qtx)
(1−qx)(1−tx)
andzi denotes the weight of theith box in the standard Young tableauT .
Proof. We will prove (8.21), and leave the other two formulas as exercises for the interested
reader. In order to prove the formula by induction, one needs to compute the following quotient
for any standard Young tableauT of sizen and an inner corner□∈T :
P ( ˚AT∪□(C2))
P ( ˚AT (C2))
= 1
(1−q)(1−t)(1−z−1
□ )
n∏
i=1
ζ
(zi
z□
)
SinceT is a Young tableau, it is easy to show that the product ofζ’s can be simpliﬁed to:
P ( ˚AT∪□(C2))
P ( ˚AT (C2))
= 1
(1−q)(1−t)·
∏■⁄=□
■inner corner ofT (1−z■/z□)∏
■outer corner ofT (1−z■/z□)
The above formula follows from (8.5) and the relation (8.7) for the weights. □
If we pass to the decategoriﬁed setting by substituting t = q−1, we see that the Poincar ´e
series depends only on the Young diagram ofT :
Corollary 8.13. P ( ˚AT (C))|t=q−1 = 1∏
□∈λ(1−qh(□)).
Proof. If we letζq,q−1(x) =ζ(x)|t=q−1, then clearlyζq,q−1(x) =ζq,q−1(x−1). It follows that the
function∏
i<jζq,q−1(zi/zj) is actually symmetric inzi, hence depends only of the shape of the
Young diagram. Let us choose the permutation ofzi such that
(z1,...,z n) = (1,q,...,q λ1−1,q−1,...,q λ1−2,... ),
Given zi on the vertical boundary of λ and zj on the horizonal boundary such that i < j,
one can consider the box □ in the same row as zi and in the same column as zj. We get
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 67
(1−qzi/zj) = (1−qh(□)), whereh(□) denotes the hook-length of□. One can check after all
telescopic cancellations
∏
i<j
ζq,q−1(zi/zj) =
(1−q)n∏
j>1(1−z−1
i )∏
□∈λ(1−qh(□)) ,
so
P ( ˚AT ) =
n∏
i=1
1
(1−q)(1−z−1
i )
∏
i<j
ζq,q−1(zi/zj) = 1∏
□∈λ(1−qh(□)).
□
To compute the full endomorphism ring of the projector PT , we should tensor with ∧•T∨
n .
When we restrict to the afﬁne chart FHilbT⊂ FHilbn the vector space Cn is endowed with a
preferred basise1,...,e n, which more abstractly means that the tautological bundle is trivialized:
Tn|FHilbT
∼=O· e1⊕...⊕O· en
The basis vectors are indexed by boxes□ in the Young diagram of T , and the torus C∗× C∗
acts on the basis vector e□ by the character z□ = qatb for any box□ = (a,b ). We conclude
that:
∧•T∨
n|FHilbT
∼=∧(ξ1,...,ξ n)
where the equivariant weights of the symbols ξ□ are given by z−1
□ = q−at−b. In particular,
Conjecture 1.9 implies that End(PT ) should be the tensor product of the homology on the
“bottom row” with an exterior algebra.
The theorems stated in the introduction can be easily deduced from the results above.
Proof. (Of Theorem 1.10 ) The observations in Examples 8.9 and 8.10, together with the re-
mark above, show that the expressions on the right-hand side of equations (1.27) and (1.28)
agree withAT (C)⊗
(
∧•T∨
n| ˚FHilbT (C)
)
. On the other hand, these expressions agree with the
known homology of the symmetric projector (computed by Hogancamp in [36]) and the anti-
symmetric projector (computed by Abel and Hogancamp in [1].) □
Proof. (of Theorem 1.11). From Corollary 8.13, we see that
P
(
˚AT (C)⊗
(
∧•T∨
n| ˚FHilbT (C)
))
=
∏
□∈λ
1−aqb(□)−a(□)
(1−qh(□)) .
This right-hand side is a well-known formula for the λ-colored HOMFLY-PT polynomial of
the unknot, which is by deﬁnition the Markov trace of the Jones-Wenzl projectorpλ∈Hn.
□
9. D IFFERENTIALS AND glN HOMOLOGY
