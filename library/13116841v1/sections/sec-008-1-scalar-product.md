---
doc_id: 13116841v1
doc_title: "Observables in Loop Quantum Gravity with a cosmological constant"
section_id: sec-008-1-scalar-product
section_title: "Scalar product"
section_number: 1
pages: 9-10
source_pdf: 1311.6841v1.pdf
source_sha256: ca65879d80b1e1c3
toc_source: outline
doc_brief: "Observables in Loop Quantum Gravity with a cosmological constant — 22 sections: Front matter; Contents; Introduction"
---
1.
Scalar product
We call “scalar product” of two tensor operators, the projection of these operators on the trivial representation.
Indeed, considering two tensor operators tj1 and ˜tj2, we can combine them using the CG coeﬃcients to build a tensor
operator of rank 0, i.e. a scalar operator.
tj1 · ˜tj2 ≡
p
[2j1 + 1]
X
m1+m2=0
qC j1 j2 0
m1m20 tj1
m1 ˜tj2
m2 = δj1,j2
X
m
(−1)j1−mq
m
2 tj1
m ˜tj1
−m,
(27)
In this sense, we can interpret these quantum Clebsch-Gordan coeﬃcients as encoding a (non-degenerated) bilinear
form B(j) deﬁning a scalar product.
B(j)(v, w) = g(j)
mnvmwn = v · w,
g(j)
mn =
p
[2j1 + 1] qC j j0
mn0 = δm,−n (−1)j−mq
m
2̸ = g(j)
nm.
(28)
To have a scalar product out from a bilinear form B, we usually demand that the bilinear form is symmetric B(v, w) =
B(ψ(v, w)), where ψ is the permutation. However due to the non-cocommutativity of the coproduct, we have a non
trivial tensor product structure. Thus we have to discuss the symmetry with respect to the deformed permutation
ψR = ψ ◦R. We have then
v · w = B(v, w) = (−1)2jq−j(j+1)B(ψR(v, w)) = (−1)2jq−j(j+1)w · v.
(29)
We notice therefore that, modulo the factor q−j(j+1), if j is integer we have a (deformed) symmetric bilinear form,
whereas in the half integer case, it is (deformed) antisymmetric. This is consistent with the construction when q →1.
Unlike in the classical case there is an extra factor q−j(j+1) that comes into play. Since we have deﬁned a bilinear form,
we can introduce the contravariant and covariant notions. If |u⟩= P
m um|jm⟩is a vector (covariant object), then
⟨u| ≡P
m u−m(−1)j−mq
m
2 ⟨jm| will be the covector (contravariant object). This notion can be naturally extended
to tensor operators. We have deﬁned earlier the covariant tensor operators since they transform as vectors. We can
introduce the contravariant tensor operators as
tm
j ≡(−1)j−mq
m
2

tj
−m
†
,
(30)
where † is here the standard combination of transpose and complex conjugation. This contravariant notion of tensor
operators was actually proposed by Quesne [36].
Finally, given a bilinear form, we can construct the associated notion of adjoint †B of an operator A, from
B(A†Bv, w)) = B(v, Aw).
We recall that3 gmn = δm,−n (−1)j−mq
m
2 is antidiagonal and not symmetric, so that
we need to be careful. We note gmn = (−1)−j−mq
m
2 δ−m,n its inverse.
Following the adjoint deﬁnition, given a
bilinear form gmn, we have, for a given operator A,
(A†B)m
n = gmaAd
agdn =

(−1)m−nq−m−n
2

A−n
−m.
(31)
3 We omit the j upper index for simplicity.
