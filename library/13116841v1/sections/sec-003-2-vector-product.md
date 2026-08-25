---
doc_id: 13116841v1
doc_title: "Observables in Loop Quantum Gravity with a cosmological constant"
section_id: sec-003-2-vector-product
section_title: "Vector product"
section_number: 2
pages: 9-24
source_pdf: 1311.6841v1.pdf
source_sha256: ca65879d80b1e1c3
doc_brief: "Observables in Loop Quantum Gravity with a cosmological constant — 5 sections: Introduction; Contents; Scalar product"
---
1. Scalar product
We call “scalar product” of two tensor operators, the projection of these operators on the trivial representation.
Indeed, considering two tensor operators tj1 and ˜tj2, we can combine them using the CG coeﬃcients to build a tensor
operator of rank 0, i.e. a scalar operator.
tj1· ˜tj2≡
√
[2j1 + 1]
∑
m1+m2=0
qC j1 j2 0
m1m20 tj1
m1
˜tj2
m2 =δj1,j2
∑
m
(−1)j1−mq
m
2 tj1
m ˜tj1
−m, (27)
In this sense, we can interpret these quantum Clebsch-Gordan coeﬃcients as encoding a (non-degenerated) bilinear
formB(j) deﬁning a scalar product.
B(j)(v,w ) =g(j)
mnvmwn =v·w, g (j)
mn =
√
[2j1 + 1]qC j j0
mn0 = δm,−n (−1)j−mq
m
2 ⁄=g(j)
nm. (28)
To have a scalar product out from a bilinear formB, we usually demand that the bilinear form is symmetricB(v,w ) =
B(ψ(v,w )), where ψ is the permutation. However due to the non-cocommutativity of the coproduct, we have a non
trivial tensor product structure. Thus we have to discuss the symmetry with respect to the deformed permutation
ψR =ψ◦R . We have then
v·w =B(v,w ) = (−1)2jq−j(j+1)B(ψR(v,w )) = (−1)2jq−j(j+1)w·v. (29)
We notice therefore that, modulo the factor q−j(j+1), if j is integer we have a (deformed) symmetric bilinear form,
whereas in the half integer case, it is (deformed) antisymmetric. This is consistent with the construction when q→ 1.
Unlike in the classical case there is an extra factorq−j(j+1) that comes into play. Since we have deﬁned a bilinear form,
we can introduce the contravariant and covariant notions. If |u⟩ =∑
mum|jm⟩ is a vector (covariant object), then
⟨u|≡ ∑
mu−m(−1)j−mq
m
2⟨jm| will be the covector (contravariant object). This notion can be naturally extended
to tensor operators. We have deﬁned earlier the covariant tensor operators since they transform as vectors. We can
introduce the contravariant tensor operators as
tm
j ≡ (−1)j−mq
m
2
(
tj
−m
)†
, (30)
where† is here the standard combination of transpose and complex conjugation. This contravariant notion of tensor
operators was actually proposed by Quesne [36].
Finally, given a bilinear form, we can construct the associated notion of adjoint †B of an operator A, from
B(A†Bv,w )) = B(v,Aw ). We recall that 3 gmn = δm,−n (−1)j−mq
m
2 is antidiagonal and not symmetric, so that
we need to be careful. We note gmn = (−1)−j−mq
m
2δ−m,n its inverse. Following the adjoint deﬁnition, given a
bilinear form gmn, we have, for a given operator A,
(A†B)m
n =gmaAd
agdn =
(
(−1)m−nq−m−n
2
)
A−n
−m. (31)
3 We omit the j upper index for simplicity.
10
2. Vector product
The notion of “vector product” is deﬁned by associating a vector operator ˆt1 to two vector operators t1, ˜t1 using
the CG coeﬃcients,
ˆt1
m = (t1∧ ˜t1)m≡
∑
m1,m2
qC 1 1 1
m1m2m t1
m1
˜t1
m2. (32)
Using their value (recalled in the appendix B), we obtain explicitly
ˆt1 =
√
[2]
[4]
(
q1/2t1
1˜t1
0−q−1/2t1
0˜t1
1
)
, ˆt−1 =
√
[2]
[4]
(
q1/2t1
0˜t1
−1−q−1/2t1
−1˜t1
0
)
,
ˆt0 =
√
[2]
[4]
(
t1
1˜t1
−1− t1
−1˜t1
1 +
(
q
1
2−q− 1
2
)
t1
0˜t1
0
)
.
As we shall see when giving a realization of the vector operators, this vector product is related to the commutation
relations of the su(2) algebra (whenq = 1) and to Witten’s proposal describing the q-deformation of the su(2) algebra
[44]. Combining the scalar product with the wedge product, we obtain the generalization of the triple product.
(t1∧ t1)· t1≡
∑
mi
(−1)1−m3q
m3
2 qC 1 1 1
m1m2m3
t1
m1 t1
m2t1
−m3. (33)
This is nothing else than the image of trivalent intertwiner (15) when restricted toj1 =j2 =j3 = 1. The generalization
to any ji is then
(tj1∧ tj2)· tj3≡
∑
mi
(−1)j3−m3q
m3
2 qC j1 j2 j3
m1m2m3
tj1
m1 tj2
m2tj3
−m3. (34)
In general, given a set of tensor operators, we can use the relevant intertwiner coeﬃcients, to construct a scalar
operator out of them. Observables for an intertwiner will be the generalization of this construction.
C. Tensor products of tensor operators
The tensor product of tensor operators necessitates more attention. Indeed if t∈L(W ) and ˜t∈L(W′) are tensor
operators forUq(su(2)), then in general t⊗ ˜t will not be a tensor operator for Uq(su(2)). To see this, ﬁrst we recall
that we need the coproduct to deﬁne the action of the generators Jα on|j1m1,j 2m2⟩. For example,
∆J+|j1m1,j 2m2⟩ =
(
J+⊗K +K−1⊗J+
)
|j1m1,j 2m2⟩, K ≡q
Jz
2 . (35)
If t⊗ ˜t is a (linear) module homomorphism, we have then
(
t⊗ ˜t
)
(∆J+|j1m1,j 2m2⟩) =
(
t⊗ ˜t
)
(J+⊗K +K−1⊗J+|j1m1,j 2m2⟩)
= (J+⊿ tj1
m1)⊗ (K⊿ ˜tj2
m2) + (K−1⊿ tj1
m1)⊗ (J+⊿ ˜tj2
m2). (36)
On the other hand this is must be equal to the action of J+ on t⊗ ˜t seen as a linear map V⊗V′→W⊗W′, so that
J+⊿ (t⊗ ˜t) = (J+)V⊗V′ (t⊗ ˜t)
(
K−1)
W⊗W′−q
1
2
(
K−1)
V⊗V′ (t⊗ ˜t) (J+)W⊗W′. (37)
We recall that by deﬁnition we have
(
K±1)
W⊗W′ = ∆K±1 =
(
K±1)
W⊗
(
K±1)
W′ (38)
(J+)W⊗W′ = ∆J+ = (J+)W⊗ (K)W′ +
(
K−1)
W⊗ (J+)W′. (39)
If t⊗ ˜t is a tensor operator, we must have (36) = (37), which gives (we omit for simplicity the indices)
(J+tK−1−q
1
2K−1tJ+)⊗ (K˜tK−1) + (K−1tK)⊗ (J+˜tK−1−q
1
2K−1˜tJ+) = (40)
J+tK−1⊗K˜tK−1 +K−1tK−1⊗J+˜tK−1−q
1
2
(
K−1tJ+⊗K−1˜tK +K−1tK−1⊗K−1˜tJ+
)
.
11
If ˜t = 1, then (40) is satisﬁed for any t but when t = 1 and ˜t⁄= 1, the constraint (40) is not satisﬁed in general 4. The
problem can be identiﬁed with the non-commutativity of the coproduct [34]. Indeed, the operator 1⊗ t can be seen
as obtained from the permutation of t⊗ 1, but since we are dealing now with a non-commutative tensor product, we
need to consider the deformed permutation ψR instead of ψ.
Lemma II.4. [34] If t is a tensor operator of rank j then (1)t = t⊗ 1 and (2)t =ψR(t⊗ 1)ψ−1
R =R21(1⊗ t)R−1
21
are tensor operators of rank j
We extend the construction to an arbitrary number of tensor products 5.
(i)t =Rii−1Rii−2..Ri 1(1⊗ 1⊗..⊗ 1⊗ t)R−1
i 1..R−1
ii−2R−1
ii−1⊗ 1⊗..⊗ 1. (41)
By abuse of notation, we say that (i)t acts on the ith Hilbert space, even though it is not really the case when q⁄= 1.
Note also that if q = 1, tensor operators which act on diﬀerent Hilbert spaces will commute, but when q⁄= 1, this will
not be the case in general due to the presence of the R-matrices.
When we consider the scalar product of tensor operators living acting on the same Hilbert space, the R-matrices
disappear which simpliﬁes the calculations.
Lemma II.5. The scalar product of the tensor operators (i)tj1 and (i)˜tj2 can be reduced to
(i)tj1· (i)˜tj2 = 1⊗..1⊗ tj1· ˜tj2⊗ 1⊗..⊗ 1. (42)
This lemma simply follows from (41).
III. REALIZATION OF TENSOR OPERATORS OF RANK 1/2 AND 1 FOR Uq(su(2))
The abstract theory of tensor operators has been summarized above. We want to illustrate the construction by
giving some realization of these tensor operators. We know that any representation Vj ofUq(su(2)) can be recovered
from the fundamental spinor representation 1
2 and the CG coeﬃcients. In the same way, the most important operators
to identify are the spinor operators. If we know them, we can concatenate them using the CG coeﬃcients to obtain
any other tensor operators. We ﬁrst present the realization of the spinor operators using q-harmonic oscillators and
then present the vector operators realized in terms of either the q-harmonic oscillators or the Uq(su(2)) generators.
A. Rank 1/2 tensor operators
Rank 1
2 tensor operators ( i.e. spinor operators) t
1
2
m should be solution of the following constraints.
J±⊿ t
1
2
∓ = t
1
2
±, J ±⊿ t
1
2
± = 0, J z⊿ t
1
2
± =±1
2t
1
2
±. (43)
Using the Schwinger-Jordan realization ofUq(su(2)) generators given in (19), we can solve these equations and we get
two solutions T
1
2 and ˜T
1
2 satisfying (43).
T
1
2 =
(
A†
B†
)
=
(
a†qNa/4
b†q(2Na+Nb)/4
)
, ˜T
1
2 =
(
˜B
˜A
)
=
(
q(2Na+Nb+1)/4b
−q(Na−1)/4a
)
. (44)
We recall thata andb areq-harmonic oscillators which satisfy the modiﬁed commutation relations (16). We can check
that T
1
2 and ˜T
1
2 are Hermitian conjugate to each other, according to the modiﬁed bilinear form we have deﬁned in
Section II B 1 (see (30)). When looking at the limit q→ 1, we have
T
1
2 → τ
1
2 =
(
a†
b†
)
, ˜T
1
2→ ˜τ
1
2 =
(
b
−a
)
. (45)
4 Note that in the limit q→ 1, this would be satisﬁed. Hence 1⊗ ˜t is a tensor operator for su(2).
5Rms = 1s−1⊗R 2⊗ 1m−s−1⊗R 1, using notations of (6).
12
This explicit realization of the tensor operators allows to check explicitly the Wigner-Eckart theorem, and to identify
the normalization of the operators through this realization. In particular, for the q-deformed spinor operator matrix
elements, we have
⟨j1,m 1|T
1
2
m|j2,m 2⟩ = δj1,j2+1/2N
1
2
j2 qC1/2j2j1
mm 2m1, with N
1
2
j2 =
(
([dj2])1/2q
j2
2
)
,
⟨j1,m 1| ˜T
1
2
m|j2,m 2⟩ = δj1,j2−1/2 ˜N
1
2
j2 qC1/2j2j1
mm 2m1, with ˜N
1
2
j2 =
(
([dj2])1/2q
1
4 (2j2−1)
)
, (46)
where m =±1/2 and dj = 2j + 1. We have therefore the two possible realizations of spinor operators in terms of
rectangular matrices. Note that the above choice of normalization N
1
2
j2 and ˜N
1
2
j2 can be modiﬁed because the spinor
operators T
1
2 and ˜T
1
2 are deﬁned up to a multiplicative function of Na +Nb. Therefore, N
1
2
j2 and ˜N
1
2
j2 can be any
function of j2.
To form observables for a N-valent intertwiner, we need to deﬁne spinor operators built from the tensor product
of N spinor operators. The explicit realization of the tensor product of spinor operators has been discussed in details
by Quesne [36]. The calculation amounts to calculate (41) for an arbitrary number N of tensor products, in the case
of the spinor operators t
1
2 .
We outline now the outcome of this calculation and give the expression of these spinor operators in terms of the q-
deformed harmonic oscillatorsa†
i, ai, Nai, b†
i, bi, Nbi ∈Fi∼Fai⊗Fbi where theFi (i = 1,··· ,N ) areN independent
q-Fock spaces. Let us deﬁne the tensor operators (i)T
1
2 and (i) ˜T
1
2 living inF≡ (⊗N
i=1Fai)(⊗N
i=1Fbi) which “act” on
the ith Hilbert space.
(i)T
1
2 =
(
A†
i
B†
i
)
, (i) ˜T
1
2 =
(
˜Bi
˜Ai
)
, for i∈{ 1,··· ,N}, (47)
where
(i)T
1
2
+ :=A†
i = (⊗i−1
k=1q
Nak−Nbk
4 )a†
iq
Nai
4 ,
(i)T
1
2
− :=B†
i = (⊗i−1
k=1q
−Nak +Nbk
4 )b†
iq
2Nai+Nbi
4 + (q
1
4−q− 3
4 )
[i−1∑
l=1
(⊗l−1
k=1q
−Nak +Nbk
4 )alb†
l (⊗i−1
k=l+1q
Nak−Nbk
4 )
]
a†
iq
Nai
4 ,
(i) ˜T
1
2
+ := ˜Bi = (⊗i−1
k=1q
Nak−Nbk
4 )q
2Nai+Nbi+1
4 bi,
(i) ˜T
1
2
− := ˜Ai = (⊗i−1
k=1q
−Nak +Nbk
4 ) (−q
Nai−1
4 ai) + (q
1
4−q− 3
4 )
[i−1∑
l=1
(⊗l−1
k=1q
−Nak +Nbk
4 )alb†
l (⊗i−1
k=l+1q
Nak−Nbk
4 )
]
q
2Nai+Nbi+1
4 bi.
These operators will be the building blocks of our construction of Uq(su(2))-observables presented in the following
section. It will be necessary to have their explicit form in terms of the harmonic oscillators in order to recover the
Uq(u(n)) structure in Section IV B.
Note that if i⁄= 1, the two spinor operators (i)T
1
2 and (i) ˜T
1
2 are no more Hermitian conjugated to each other.
Indeed, (A†
i)†⁄=−q1/4 ˜Ai, (B†
i )†⁄=q−1/4 ˜Bi, i∈{ 2,··· ,N}. To emphasize this lack of Hermiticity, we introduce the
notation,
Ci≡−q1/4 ˜Ai, Di≡q−1/4 ˜Bi, ∀i∈{ 1,··· ,N}. (48)
That is, we can rewrite the spinor operators (i) ˜T
1
2 as (i) ˜T
1
2 =
(
q
1
4Di
−q− 1
4Ci
)
. Quesne has calculated all possible
commutation relations between the components of (i)T
1
2
± , (j) ˜T
1
2
± for any i, j∈{ 1,··· ,N} [36]. First let us give the
commutation relations when 1≤i =j≤N.
B†
iA†
i =q1/2A†
iB†
i, CiDi =q1/2DiCi, DiA†
i =q1/2A†
iDi, CiB†
i =q1/2B†
iCi, CiA†
i =qA†
iCi + 1,
DiB†
i =qB†
iDi + (q− 1)A†
iCi + 1. (49)
13
When 1≤i<j ≤N, we have
A†
iA†
j =q−1/4A†
jA†
i, A†
iB†
j =q1/4B†
jA†
i− (q3/4−q−1/4)A†
jB†
i, B†
iA†
j =q1/4A†
jB†
i, B†
iB†
j =q−1/4B†
jB†
i,
DiDj =q−1/4DjDi, DiCj =q1/4CjDi− (q3/4−q−1/4)DjCi, CiDj =q1/4DjCi, CiCj =q−1/4CjCi,
A†
iDj =q−1/4DjA†
j, DiA†
j =q−1/4A†
jDi, B†
iCj =q−1/4CjB†
i, CiB†
j =q−1/4B†
jCi, B†
iDj =q1/4DjB†
i,
DiB†
j =q1/4
(
B†
jDi + (1−q−1)A†
jCi
)
, A†
iCj =q1/4
(
CjA†
i + (q− 1)DjB†
i
)
, CiA†
j =q1/4A†
jCi. (50)
These commutation relations are quite cumbersome and they illustrate that the components of operators acting on
diﬀerent Hilbert spaces do not commute when q⁄= 1. Obviously, when q = 1, they simplify a lot.
B. Rank 1 tensor operators
Rank 1 tensor operators (i.e. vector operator) forUq(su(2)) have been identiﬁed [34]. These operators are important
as in the LQG context, they will encode the notion of ﬂux operator. We explicitly construct them and provide their
commutation relations, when they act on diﬀerent legs, or not.
We can construct them using the spinor operators T
1
2 , ˜T
1
2 and the CG coeﬃcients.
t1
m =
∑
m1,m2
qC
1
2
1
2 1
m1m2mT
1
2
m1
˜T
1
2
m2. (51)
Using the explicit non-zero CG coeﬃcients given in the appendix B, we have that
t1
±1 =T
1
2
± ˜T
1
2
±, t1
0 = 1√
[2]
(
q− 1
4T
1
2
+ ˜T
1
2
− +q
1
4T
1
2
− ˜T
1
2
+
)
. (52)
Explicitly, we obtain that
t1
1 = q− 1
2 q
(3Na+Nb)
4 a†b =q−1/2q
1
2 (Na+Nb)q
Jz
2 J+, (53)
t1
0 = − 1
[2]
1
2
(
q−1qNa/2[Na]−qNa+Nb/2[Nb]
)
=−q−1/2
[2]
1
2
q
1
2 (Na+Nb)(q−1/2J+J−−q1/2J−J+), (54)
t1
−1 = −q− 1
2 q(3Na+Nb)/4b†a =−q− 1
2q
1
2 (Na+Nb)q
Jz
2 J−. (55)
Once again, we can check that the Wigner-Eckart is satisﬁed,
⟨j1,m 1|t1
l|j2,m 2⟩ =δj1,j2N1
j2 qC 1j2 j1
lm2m1
with N1
j2 =−qj2− 1
2
(([2j2][2j2 + 2])
[2]
) 1
2
, (56)
andl∈{− 1, 0, 1}. In this realization, the vector operator is realized as a square matrix. Note that the normalization
N1
j2 comes here from the chosen spinor normalization (46). For a given vector operator, we can always consider an
arbitrary normalization N1
j2.
An important remark is that in the limit q→ 1, the components of the vector operator become proportional to the
components of the su(2)-generators,
t1→τ 1 =


J+
−
√
2Jz
−J−

. (57)
That is the su(2) generators are very simply related to vector operators. Let us now go back to our deﬁnition of
generalized scalar product (27) and generalized vector product (32). In the q = 1-case, theq-deformed CG coeﬃcients
of equations (27) and (32) are simply replaced by the standard su(2) CG coeﬃcients. In particular the scalar
14
product is still the projection on the trivial rank and we can deﬁne the “norm” of the vector operator τ 1, given by
τ 1·τ 1≡∑
m1+m2=0 C 1 1 0
m1m2 0τ 1
m1τ 1
m2. This simpliﬁes into
τ 1·τ 1 =−2⃗J· ⃗J (58)
where the su(2) set of generators ⃗J is seen as a 3-vector with components Jx = 1
2(J+ +J−), Jy = 1
2i(J+−J−) and
Jz = Jz and the · of the left-hand side of (58) denotes the standard scalar product of 3-vectors. That is, in the
non-deformed case, the norm of the vector operator is proportional to the quadratic Casimir of su(2),C = ⃗J· ⃗J. The
norm of theUq(su(2)) vector operator is by deﬁnition aUq(su(2))-invariant but it is not proportional to|⃗J|2 anymore.
Indeed,
t1·t1∝ (q
1
2−q− 1
2 )2J2
−J2
+ + ([2Jz + 4]− [2Jz])J−J+ + [2Jz + 2][2Jz] (59)
where the proportionality coeﬃcient is a function of q
Na+Nb
2 .
The “vector product” operation in the case q = 1 can be understood as the commutator of the su(2) generators,
which is also the natural way to encode the notion of vector product, as used in LQG. Indeed
(τ 1∧τ 1)1 = 1√
2
(
τ 1
1τ 1
0−τ 1
0τ 1
1
)
= [Jz,J +] =J+ =τ 1
1,
(τ 1∧τ 1)−1 = 1√
2
(
τ 1
0τ 1
−1−τ 1
−1τ 1
0
)
= [Jz,J−] =−J− =τ 1
−1,
(τ 1∧τ 1)0 = 1√
2
(
τ 1
1τ 1
−1−τ 1
−1τ 1
1
)
= 1√
2[J−,J +] =−
√
2Jz =τ 1
0. (60)
We see therefore that this vector product can be understood as the commutator of the su(2) generators, which is also
the natural way to encode the notion of vector product, as used in LQG.
One can check explicitly using the above realization of the vector operators when q⁄= 1 that
(t1∧ t1)1 =
√
[2]
[4]
(
q1/2t1
1t1
0−q−1/2t1
0t1
1
)
, (t1∧ t1)−1 =
√
[2]
[4]
(
q1/2t1
0t1
−1−q−1/2t1
−1t1
0
)
,
(t1∧ t1)0 =
√
[2]
[4]
(
t1
1t1
−1− t1
−1t1
1 +
(
q
1
2−q− 1
2
)
t1
0t1
0
)
. (61)
Thus, in the quantum group case, the vector product of vector operators is diﬀerent than the commutation relations
deﬁningUq(su(2)). The matrix elements of this new vector operator can be expressed in terms of the matrix elements
of t1,
⟨j, m1|(t1∧ t1)α|j, m2⟩ = [2j− 1]− [2j + 3]
[2]([4])
1
2
qj− 1
2⟨j, m1|t1
α|j, m2⟩ (62)
We see therefore that in the classical case when q = 1, the generators are related to vector operators and diﬀerent
structures, such as the adjoint action, the commutator and vector product are encoded in the same way. When q⁄= 1,
all these diﬀerent degeneracies are actually lifted. Let us summarize in the table below all the possible relations in
the cases of su(2) andUq(su(2)).
15
su(2) Uq(su(2))
Generators Jσ, σ =±,z Jσ, σ =±,z
with commutation relations with commutation relations
[J+,J−] = 2Jz [J+,J−] = qJz−q−Jz
q
1
2−q− 1
2
[J±,Jz] =∓J± [J±,Jz] =∓J±
Vector operators τ 1 =


J+
−
√
2Jz
−J−

 t1∝


q
Jz
2 J+
− 1√
[2]
(q−1/2J+J−−q1/2J−J+)
−q
Jz
2 J−


Adjoint action Jσ⊿O = [Jσ,O] for σ =±, z J±⊿O =J±Oq−Jz
2 −q± 1
2q−Jz
2OJ±, Jz⊿O = [Jz,O]
“Scalar product” τ 1·τ 1 =−2C =−2|⃗J|2 t1· t1 =I where I is aUq(su(2))-invariant;
(· deﬁned by (27)) whereC is the quadratic Casimir of su(2). |⃗J|2 is not a Casimir for Uq(su(2)).
“Vector product” (τ 1∧τ 1)±1 = [Jz,J±], (t1∧ t1)α = ˆt1
α = vector operator; not simply related to
(∧ deﬁned by (32)) (τ 1∧τ 1)z = 1√
2[J−,J +]. the commutators between generators of Uq(su(2)).
The extension of t1 to (i)t1, for i∈{ 1,··· ,N}, can be done either through (41) or by using the spinor operators
(i)T
1
2
m1 and (i) ˜T
1
2
m2 given in (47).
(i)t1
m =
∑
m1,m2
qC
1
2
1
2 1
m1m2m
(i)T
1
2
m1
(i) ˜T
1
2
m2→



(i)t1
1 =q
1
4A†
iDi =A†
i ˜Bi
(i)t1
0 = 1√
[2]
(
q
1
2B†
iDi−q− 1
2A†
iDi
)
= 1√
[2]
(
q
1
4B†
i ˜Bi +q− 1
4A†
i ˜Ai
)
(i)t1
−1 =−q− 1
4B†
iCi =B†
i ˜Ai
(63)
Explicitly, in terms of theUq(su(2))-generators, we have,
(i)t1
1 = q
∑i−1
k=1
(k)Jz (i)J+q
(i)Jz
2 q
Nai+Nbi
2 ,
(i)t1
0 = 1√
[2]
[−q− 1
2 (q− 1
2 (i)J+
(i)J−−q
1
2 (i)J−
(i)J+)q
Nai+Nbi
2
+(q
1
2−q− 1
2 )(1 +q− 1
2 )
i−1∑
l=1
[q(
(l)Jz
2 +∑i−1
k=l+1
(k)Jz) (l)J−] (i)J+q
(i)Jz
2 q
Nai+Nbi
2 ]
(i)t1
−1 = −q−1q− ∑i−1
k=1( (k)Jz) (i)J−q
(i)Jz
2 q
Nai+Nbi
2
−q−1(q
1
2−q− 1
2 )
i−1∑
l=1
(
q− ∑l−1
k=1( (k)Jz+
(l)Jz
2 ) (l)J−
)
(q− 1
2 (i)J+
(i)J−−q
1
2 (i)J−
(i)J+)q
Nai+Nbi
2
+q−1(q
1
2−q− 1
2 )2
(i−1∑
l=1
q− ∑l−1
k=1
(k)Jz
2 (l)J−q
∑i−1
k=l+1
(k)Jz
2
)2
(i)J+q
(i)Jz
2 q
Nai+Nbi
2
With this choice of normalization inherited from (56), the commutation relations between the (i)t1
m are quite
16
complicated. For 1≤i<j ≤N,
(i)t1
1
(j)t1
1 =q−1 (j)t1
1
(i)t1
1
(i)t1
1
(j)t1
0 = (j)t1
0
(i)t1
1 + (q−1−q) (j)t1
1
(i)t1
0
(i)t1
1
(j)t1
−1 =q (j)t1
−1
(i)t1
1− (q− 1)[2] (j)t1
0
(i)t1
0 + (q2− 1)(1−q−1) (j)t1
1
(i)t1
−1
(i)t1
0
(j)t1
1 = (j)t1
1
(i)t1
0
(i)t1
0
(j)t1
0 = (j)t1
0
(i)t1
0− (q
1
2−q− 1
2 )(q + 1)(1 +q−1) (j)t1
1
(i)t1
−1 (64)
(i)t1
0
(j)t1
−1 = (j)t1
−1
(i)t1
0 + (q−1−q) (j)t1
0
(i)t1
−1
(i)t1
−1
(j)t1
1 =q (j)t1
1
(i)t1
−1
(i)t1
−1
(j)t1
0 = (j)t1
0
(i)t1
−1
(i)t1
−1
(j)t1
−1 =q−1 (j)t1
−1
(i)t1
−1
Fori =j∈{ 1,··· ,N},
(i)t1
1
(i)t1
0 =q−1 (i)t1
0
(i)t1
1 + q
1
2−q− 1
2
√
[2]
Eii
(i)t1
1 +q−1√
[2] (i)t1
1,
(i)t1
1
(i)t1
−1 =q−1 (i)t1
−1
(i)t1
1 + (q−1− 1)
[2] ( (i)t1
0)2 + 2(q
1
2−q− 1
2 )
[2]
3
2
(i)t1
0Eii + 2q−1
√
[2]
(i)t1
0− q−1(q
1
2−q− 1
2 )
[2] Eii (65)
(i)t1
0
(i)t1
−1 =q−1 (i)t1
−1
(i)t1
0 + q
1
2−q− 1
2
[2] Eii +q−1√
[2] (i)t1
−1, (66)
whereEii :=−q
1
4A†
i ˜Ai +q− 1
4B†
i ˜Bi is aUq(su(2))-invariant (see section IV B) and it commutes with any (i)t1
α, (α =
±,z ).
IV. OBSERVABLES FOR THE INTERTWINER SPACE
As emphasized in the introduction, we focus on the quantum group Uq(su(2)) with q real, which is relevant for 3d
Euclidian gravity with Λ < 0 and the physical case, i.e. 4d Lorentzian gravity with Λ > 0.
A. General construction and properties of intertwiner observables
From now on, we consider the space of N-valent intertwiners with N legs ordered from 1 to N. Let’s consider n
tensor operators (α)tJα of respective rank Jα, associated with the αth leg of the vertex, built from (41). To construct
an observable, i.e. a scalar operator, we can use the same combination that would appear in the deﬁnition of an
intertwiner built out from the vectors |Jα,mα⟩. Indeed, if |ιJ1..Jn⟩ =∑
mcJ1..Jn
m1..mn|J1m1,..Jnmn⟩, then,
IJ1..Jn =
∑
mi
cJ1..Jn
m1..mn
(1)tJ1
m1.. (n)tJn
mn (67)
will be a scalar operator. Like for intertwiners, the bivalent and trivalent ones are the simplest and we can write them
explicitly,
IJαJβ≡ (α)tJα· (β)tJβ =δJα,Jβ
∑
m
(−1)Jα−mq
m
2 (α)tJα
m
(β)tJβ
−m≡IJα
αβ, (68)
IJαJβJγ≡ ( (α)tJα∧ (β)tJβ)· (γ)tJγ =
∑
mi
(−1)Jγ−m3q
m3
2 qC JαJβ Jγ
m1m2m3
(α)tJα
m1
(β)tJβ
m2
(γ)tJγ
−m3. (69)
We recognize the generalized notions of respectively the scalar product and the triple product.
This construction works well for operators acting on an intertwiner, however in the general LQG context, we need
to deal with spin networks, so we need to consider the tensor product of such intertwiners |ιj1..jN⟩⊗| ι′
j1′..jN′⟩⊗ ....
Although the tensor product is not commutative, we do not need to use the deformed permutation to deﬁne an
operator acting on any intertwiner of the tensor product. Indeed, since an intertwiner is a Uq(su(2))-invariant vector,
the tensor product involving such invariant vectors is commutative.
More explicitly, we have seen earlier that ift is a tensor operator, then 1⊗t will not be in general a tensor operator.
However if 1⊗ t is restricted to act on some invariant vectors |ι⟩⊗| ι′⟩, then 1⊗ t will still be a tensor operator.
17
To see this, let us consider the invariant vectors|ι⟩⊗| ι′⟩∈ W⊗W′. We recall that an invariant vector means that
J±|ι⟩ = 0, K ±1|ι⟩ =|ι⟩. (70)
Let us ﬁrst determine the transformation of 1⊗ t as a representation of Uq(su(2)), that is (36), when acting on the
vectors|ι⟩⊗| ι′⟩
(
(J+K−1−q
1
2K−1J+)⊗K˜tK−1 + 1⊗ (J+˜tK−1−q
1
2K−1˜tJ+)
)
|ι⟩⊗| ι′⟩ = 1⊗ (J+⊿ ˜t)|ι⟩⊗| ι′⟩ (71)
If 1⊗ t transforms well when restricted to the invariant vectors |ι⟩⊗| ι′⟩, we must recover the same outcome as (71)
when considering 1⊗ t transforming as an operator, that is (37).
(
J+K−1⊗K˜tK−1 + 1⊗J+˜tK−1−q
1
2
(
K−1J+⊗K−1˜tK +K−2⊗K−1˜tJ+
))
|ι⟩⊗| ι′⟩
= 1⊗ (J+⊿ ˜t)|ι⟩⊗| ι′⟩. (72)
In the right hand side of the two above equations, we have used (70) to recover 1⊗ (J+ ⊿ ˜t)|ι⟩⊗| ι′⟩. A similar
calculation can be made for the action of J− and K. Hence, the operator 1⊗ ˜t transforms as a tensor operator of
same rank as ˜t when restricted to act on an invariant state |ι⟩⊗| ι′⟩. This means that we can just focus on the
observables associated to one intertwiner, and if we look at another intertwiner a priori we do not need to order the
vertices, unless we look at observables that live on both intertwiners at the same time.
If we have many legs in our intertwiner, it might cumbersome to calculate the terms (i)tJ and (j)tJ and then
calculate the observable IJ
ij, since we have to use extensively the deformed permutations and a lot of CG coeﬃcients
(orR matrices) appear then. If we know the matrix elements of IJ
12 and IJ
21, we can construct by induction all the
other terms. We know that by deﬁnition
IJ
12 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20 (tJ
m1⊗ 1)R21(1⊗ tJ
m2)R−1
21, (73)
IJ
13 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20 (tJ
m1⊗ 1⊗ 1)R32R31(1⊗ 1⊗ tJ
m2)R−1
31R−1
32, (74)
IJ
23 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R−1
21R32R31(1⊗ tJ
m2)R−1
31R−1
32. (75)
We can construct the observable IJ
13 from IJ
12, by permuting 2 with 3, using the braided permutation ψ23 deﬁned in
(7). Upon this permutation, we have in particular that R21 becomesR31.
ψ23IJ
12ψ−1
23 =
√
[2J + 1]
∑
mi
R32qC J J 0
m1m20 (tJ
m1⊗ 1⊗ 1)R31(1⊗ 1⊗ tJ
m2)R−1
31R−1
32
=
√
[2J + 1]
∑
mi
qC J J 0
m1m20 (tJ
m1⊗ 1⊗ 1)R32R31(1⊗ 1⊗ tJ
m2)R−1
31R−1
32
= IJ
13. (76)
We have used the fact thatR23 and tJ
m1⊗ 1⊗ 1 commute. This can be extended to arbitrary IJ
1j. Now we would like
to consider the construction of IJ
23 from IJ
12. As a matter of fact, we can start from IJ
13 and permute 1 and 2 using
the deformed permutation ψ12.
ψ12IJ
13ψ−1
12 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R31R32(1⊗ 1⊗ tJ
m2)R−1
32R−1
31R−1
21. (77)
To simplify this expression, we use the Yang-Baxter equation,
RdcRdbRcb =RcbRdbRdc, (78)
18
with c = 2, b= 1,d = 3. We have then
ψ12IJ
13ψ−1
12 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R31R32(1⊗ 1⊗ tJ
m2)R−1
21R−1
31R−1
32.
=
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R31R32R−1
21 (1⊗ 1⊗ tJ
m2)R−1
31R−1
32 (79)
where we used that R−1
21 commutes with 1⊗ 1⊗ tJ
m2. We use again the Yang-Baxter equation (80), for the product
ofR matrices in the middle of the above expression.
R−1
21R32R31R21 =R31R32. (80)
ψ12IJ
13ψ−1
12 =
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R−1
21R32R31R21v−1
21 (1⊗ 1⊗ tJ
m2)R−1
31R−1
32
=
√
[2J + 1]
∑
mi
qC J J 0
m1m20R21(1⊗ tJ
m1⊗ 1)R−1
21R32R31(1⊗ 1⊗ tJ
m2)R−1
31R−1
32
= IJ
23. (81)
This is the relevant expression for IJ
23. Hence, we can obtain any IJ
ij with i < j, using the braided permutation,
starting fromIJ
12. A similar argument applies to construct the terms IJ
ji withi<j . We can obtain them by induction
on the braided permutation starting from the ﬁrst term IJ
21.
Now that we have provided a general rule and some tricks to construct observables, it is natural to answer the
following questions.
• Can we generate any observables from a fundamental algebra of observables?
• What is the physical meaning and implications of some of the key-observables deﬁned in the Uq(su(2)) context?
We explore these questions now.
B. Uq(u(n)) formalism for LQG deﬁned over Uq(su(2))
We want to construct the ”smallest” observables. It is therefore natural to consider the observables built from
the scalar product of spinor operators (47). Since we have two types of spinor operators, we have diﬀerent possible
combinations.
Eαβ≡− (α)T
1
2·(β) ˜T
1
2, G†
αβ≡−(α)T
1
2·(β)T
1
2 Fαβ≡−(α) ˜T
1
2·(β) ˜T
1
2. (82)
Note that since the operators on diﬀerent legs do not commute, we could a priori choose a diﬀerent order of T and ˜T
in the deﬁnition ofEαβ. One can show however that choosing the order leads to the same operator modulo a constant
factor. This factor comes from the (deformed) symmetry of the scalar product as well as the commutation relations
between the spinor operators acting on diﬀerent legs.
Let us focus on the operators Eαβ. Consider ﬁrst the spinor operators which act on the same leg α =β =i.
Eii :=− (i)T
1
2· (i) ˜T
1
2 =−q
1
4A†
i ˜Ai +q− 1
4B†
i ˜Bi. (83)
Having in mind Lemma II.5, we can forget about the tensor product, and the only relevant action is on the leg i so
Eii|ιj1...jN⟩ = [2ji]|ιj1...jN⟩. (84)
Consider now the spinor operators which act on diﬀerent legs i and j.
Eij =A†
iCj +B†
iDj. (85)
19
The action ofE12 =A†
1C2 +B†
1D2 on a trivalent intertwiner is given by
E12|ιj1j2j3⟩ = − ˜N
1
2
j2N
1
2
j1(−1)j1+j2+j3−1q− 3
4j1
√
[2j1 + 2][2j2]
{
j2− 1
2
1
2 j2
j1 j3 j1 + 1
2
}
|ij1+ 1
2j2− 1
2j3⟩ (86)
with the normalization choice
N
1
2
j = [dj]
1
2q
j
2, ˜N
1
2
j = [dj]
1
2q
j
2− 1
4.
The other operators Eij (i, j∈{ 1, 2, 3}) can be constructed using the tricks described in the previous section. In a
similar way, we get
q
3
4F12|ij1j2j3⟩ = − ˜N
1
2
j2
˜N
1
2
j1(−1)j1+j2+j3q
1
2 (j2+1)√
[2j1][2j2]
{
j2− 1
2
1
2 j2
j1 j3 j1− 1
2
}
|ij1− 1
2j2− 1
2j3⟩
q
1
4G†
12|ij1j2j3⟩ = −N
1
2
j2N
1
2
j1(−1)j1+j2+j3q− 1
2 (j1+ 3
4 )√
[2j1 + 2][2j2 + 2]
{
j2 + 1
2
1
2 j2
j1 j3 j1 + 1
2
}
|ij1+ 1
2j2+ 1
2j3⟩
(87)
When we perform the limit q→ 1, the operators A†
i,B†
i ,Ci,Di become respectively a†
i, b†
i, ai and bi, that is
the standard harmonic oscillators operators. Hence in this limit, the operators Eij become a†
iaj +b†
ibj which are
the generators Eij of a u(n) Lie algebra, written using the Schwinger-Jordan representation. In a similar way, the
operatorsFij,Gij become respectively Fij and F†
ij deﬁned as follows
G†
ij
q→1
→ a†
ib†
j−b†
ia†
j =F†
ij, Fij
q→1
→ aibj−biaj =Fij. (88)
We recognize the operators E,F,F † which are the basis of the U( N) formalism [27–29]. They appear very naturally
in our framework.
It is then natural to demand if the operators Eij are the generators Uq(u(n)). First, let us recall the deﬁnition of
Uq(u(n)) Cartan Weyl generators [37]. We have respectively the raising, diagonal, lowering operators Eii+1, Ei, Ei−1i,
with the following commutation relations
[Eii, Ejj] = 0, [Eii, Ejj+1] = (δij−δij+1)Ejj+1, [Eii, Ej−1j] = (δij+1−δij)Ej−1j, [Eii+1, Ej−1j] =δij(Ei− Ei+1).
The other generators are constructed by induction.
Eij = q
1
2 Ej−1
(
Eij−1Ej−1j−q
1
2 Ej−1,jEij−1
)
, j >i + 1 (89)
Eji = q− 1
2 Ej−1
(
Ejj−1Ej−1i−q− 1
2 Ej−1,iEjj−1
)
, j >i + 1. (90)
Note that Eij is not necessarily the adjoint of Eji due to the presence of q. The coproduct is deﬁned as follows
∆Ei = Ei⊗ 1 + 1⊗ Ei, ∆Eii+1 = Eii+1⊗qEi+Ei+1 +qEi+Ei+1⊗ Eii+1, . (91)
The coproduct for the other generators are obtained by induction.
The Schwinger-Jordan map allows to express these generators in terms of N q-harmonic oscillators ai.
Eij =aia†
j, Ei = 1
2(Ni−Ni+1) (92)
To have the representation of these generators in terms of N pairs of q-harmonic oscillators ( ai,bi), we use the
20
coproduct:
Eii :=Nai +Nbi, (93)
Ei,i+p :=a†
iai+pq
Nbi+2(∑p−1
l=1 Nbi+l)−Nbi+p
4 +q
−Nai+2(∑p−1
l=1 Nai+l)+Nai+p
4 b†
ibi+p
+(q− 1
4−q
3
4 )
p−1∑
k=1
(
q
Nai+k +2(∑p−1
l=k+1Nai+l)+Nai+p
4 a†
iai+kq
Nbi+2(∑k−1
l=1 Nbi+l)+Nbi+k
4 b†
i+kbi+p
)
, (94)
Ei+p,i :=aia†
i+pq
Nbi−2(∑p−1
l=1 Nbi+l)−Nbi+p
4 +q
−Nai−2(∑p−1
l=1 Nai+l)+Nai+p
4 bib†
i+p
+(q
1
4−q− 3
4 )
p−1∑
k=1
(
q
−Nai−2(∑k−1
l=1 Nai+l)−Nai+k
4 a†
i+pai+kq
−Nbi+k−2(∑p−1
l=k+1Nbi+l)−Nbi+p
4 b†
i+kbi
)
. (95)
Using the deﬁnition of the Eij in terms of the q-harmonic oscillators (ai,bi) deduced from the expression of the spinor
operators, we can identify a non linear relationship between these Eij and theEij.
Eii =q− 1
2q
Eii
2 [Eii], Ei,i+1 =q
Ei+1,i+1
4 Ei,i+1, Ei+1,i =q
Eii
2 Ei+1,iq
Ei+1,i+1
4 , Ei,i+p =q
− ∑p−1
l=1 Ei+l,i+l+Ei+p,i+p
4 Ei,i+p,
Ei+p,i =q
2Eii+∑p−1
l=1 Ei+l,i+l
4 Ei+p,iq
Ei+p,i+p
4 . (96)
To have a non-linear redeﬁnition of the generators is something common when dealing with quantum groups. For
example, there exists diﬀerent realizations ofUq(su(2)), all related with a non-linear redeﬁnition of the generators [45].
Biedenharn recalls also diﬀerent deﬁnitions of the generators of Uq(u(n)) related by nonlinear transformations in [37].
For some choice of generators, the commutation relation might take a simpler shape but the coproduct would be more
complicated, and vice-versa. The key point is here that we have found that the intertwiner carries a representation
ofUq(u(n)), and this generalizes the results of [27, 29].
In the classical case, when q = 1, it was shown that the intertwiner carries an irreducible u(n) representation [28].
We can wonder whether a similar result also holds here. The answer is positive. A cumbersome proof can probably
be obtained by looking at the Casimirs of Uq(u(n)). We do not want to follow this route. Instead we would like to
recall the seminal results by Jimbo, Rosso and Lustzig [46–48] which essentially state that all the ﬁnite dimensional
representations of the deformation Uq(g) of the enveloping algebra U(g), where g is any complex simple Lie algebra,
are completely reducible. The irreducible representations can be classiﬁed in terms of highest weights and in particular
they are deformations of the irreducible representations of U(g), when q is not root of unity. We can extend this
result to the semi-simple case and to Uq(u(n)) in particular (see Section 2.5 of [37] for example). Now we know
that when q = 1, the intertwiner is an irreducible representation of u(n), hence by deforming the enveloping algebra,
the representation of Uq(u(n)) carried by the Uq(su(2)) intertwiner must stay an irreducible representation. As a
consequence, the Uq(su(2)) intertwiner must carry an irreducible representation of Uq(u(n)), just as in the classical
case.
Finally, we can discuss the hermiticity property of the scalar operators we have constructed. Indeed, we expect an
observable to be self-adjoint. The operators Eij are not self-adjoint, but this should not come as a surprise. Indeed
the classical operators Eij are not hermitian either. However, the adjoint (Eij)† =Eji is still a generator. This means
that we can do a linear change of basis Eij → Eij + (Eij)† in the u(n) basis to construct self-adjoint generators.
This is actually how the formalism was initially introduced in [27]. The Cartan Weyl generators Eij when expressed
in terms of the harmonic oscillators satisfy a similar property, namely E†
ij = Eji [37]. As a consequence, from the
Eij, we can do a (non-linear) change of basis and construct the relevant hermitian Uq(u(n)) generators which will be
Uq(su(2)) invariant, using the maps (96).
V. GEOMETRIC INTERPRETATION OF SOME OBSERVABLES IN THE LQG CONTEXT
In LQG with Λ = 0, the intertwiner is understood as the fundamental chunk of quantum space. For a 2d space, it is
dual to a face, whereas in 3d it is dual to a polyhedron. The intertwiner is invariant under the action of su(2), hence
the observables should be invariant under the adjoint action of su(2). We see that the use of tensor operators allows
to construct in a direct manner such observables: we need to construct operators which transform as a scalar under
the adjoint action of su(2). We have seen in the previous section how this formalism can be extended to the quantum
21
group caseUq(su(2)) in a direct manner. When Λ = 0, some observables have a clear geometrical meaning. We have
for example the quantum version of the angle, the length... We now explore the generalization of these geometric
operators in 3 dimensions, in the Euclidian case with Λ < 0.
For simplicity we are going to focus on the three-leg intertwiner. When Λ = 0, we know that it encodes the quantum
state of a triangle. Let us recall quickly the main geometric features of a triangle, either ﬂat or hyperbolic.
Classically a ﬂat triangle can be described by the normals ⃗ ni, i = a,b,c to its edges, such that |⃗ ni| = 𝓁i is the
edge length. To have a triangle, the normals need to sum up to zero, this is the closure constraint. All the geometric
information of the triangle can then be expressed in terms of these normals, as recalled in the table below.
FIG. 1: The hyperbolic triangle is represented in the Poincar´ e disc. The (outgoing) normals ˆni are deﬁned in the tangent plane
at the vertex of the triangle, as the orthogonal vectors to the tangent vectors ˆ ui.
Let us consider now an hyperbolic triangle. Its edges are geodesics in the 2d hyperboloid of radius R. Unlike the ﬂat
triangle, an hyperbolic triangle can be characterized by its three angles θi or the three lengths 𝓁i of its edges. The
hyperbolic cosine laws relate the edge lengths and the angles (see the table below). The area A of the triangle is given
in terms of the angles.
A = (π− (θa +θb +θc))R2. (97)
In order to make easier the limit to the ﬂat case, we can encode all this information in terms of the normals. Note
however that due to the curvature, we have a diﬀerent tangent space at each point of the edge. The tangent vectors
and their normal are therefore not living in the same vector space for diﬀerent points. In the curved case, we shall
consider the normals ⃗ ni at each vertex of the triangle. As a direct consequence, the closure constraint in the curved
case is subtler than in the ﬂat case. We postpone the study of this constraint to a detailed analysis of the relevant
phase space in [49]. We recall in the following table the main geometric features of the ﬂat and hyperbolic triangles,
in terms of the normals. We use the notation s = 1
2(𝓁a +𝓁b +𝓁c).
Flat case, Λ = 0 Hyperbolic case, Λ < 0, R =|Λ|− 1
2
Closure constraint: ∑
i⃗ ni = 0 To be determined [49]
Edge length: |⃗ ni| =𝓁i |⃗ ni| = sinh 𝓁i
R
Cosine law: cosθa =−ˆnb· ˆnc =−𝓁2
a−𝓁2
b−𝓁2
c
2𝓁b𝓁c
cosθa =−ˆnb· ˆnc = − cosh 𝓁a
R +cosh
𝓁b
R cosh 𝓁c
R
sinh
𝓁b
R sinh 𝓁c
R
Area: A2 = 1
4 (s(s−𝓁a)(s−𝓁b)(s−𝓁c)) sin2 A
2R2 = sinh( s
2R ) sinh(s−𝓁a
2R ) sinh(
s−𝓁b
2R ) sinh(s−𝓁c
2R )
cosh2 𝓁a
2R cosh2 𝓁b
2R cosh2 𝓁c
2R
22
The quantization of the ﬂat triangle can be done very naturally. The quantum state is given by the three-leg SU(2)
intertwiner. We associate to normalized normals⃗ ni to the ﬂux operators (i)⃗J, which we know now to be related to the
SU(2) vector operators (i)τ 1 (cf section III B). This provides a direct quantization of all the geometric data: closure
constraint, length, angles, area (see [38] for a recent review of these results).
We consider now a Uq(su(2)) three-leg intertwiner |ιjbjcja⟩. The ordering we choose for the legs is ﬁxed as we
have already emphasized before. We would like to check whether it encodes the quantum state of an hyperbolic
triangle. We use the Uq(su(2)) tensor operators to probe the geometry of this state of geometry. Since we are in the
3d framework with a negative cosmological constant, we take q =eλ, with λ = 𝓁p
R , and Λ =−R2.
Angle operator. Since we know that the angles specify completely the hyperbolic triangle, we can focus ﬁrst on
operators characterizing angles. By analogy with the non-deformed case, we deﬁne the scalar product of the vector
operators (i)ˆt1 and (j)ˆt1, with chosen normalization ˆN1
ji = 1 and i⁄=j. We look at the action of this operator on the
three-leg intertwiner|ιjbjcja⟩. For simplicity we focus on (b)ˆt1· (c)ˆt1, since we know how to recover the other types of
operators from this one using tricks developed in Section IV A.
(b)ˆt1· (c)ˆt1|ιjbjcja⟩ = −q cosh λ
2 cosh((ja + 1
2)λ)− cosh((jb + 1
2)λ) cosh((jc + 1
2)λ))√
(sinh(jbλ))(sinh((jb + 1)λ))(sinh(jcλ))(sinh((jc + 1)λ))
|ιjbjcja⟩,
= −q cosh λ
2 cosh((ja + 1
2)λ)− cosh((jb + 1
2)λ) cosh((jc + 1
2)λ))√
(sinh2((jb + 1
2)λ)− sinh2 λ
2 )(sinh2((jc + 1
2)λ)− sinh2 λ
2 )
|ιjbjcja⟩, (98)
where we have used q = eλ and sinh(jλ))(sinh((j + 1)λ)) = sinh 2((j + 1
2)λ)− sinh2 λ
2 . We recognize in (98) a
quantization of the hyperbolic cosine law, provided we consider the quantization of the length edge given by 𝓁→
(j + 1
2)𝓁p. Note that the factors sinh2 λ
2 in the denominator and coshλ
2 in the numerator can be interpreted as ordering
ambiguity factors, arising from the respective quantization of sinh 𝓁i
R and cosh 𝓁i
R .
In the limit q→ 1, we recover the quantized cosine law for a ﬂat triangle [41] expressed in terms of the quantized
normals, modulo an overall sign and a factor 1
2.
(b)ˆτ 1· (c)ˆτ 1|ιjajbjc⟩ = −
(
ja(ja + 1)−jb(jb + 1)−jc(jc + 1)√
jb(jb + 1)jc(jc + 1)
+O
(
λ2)
)
|ιjbjcja⟩. (99)
From the construction of the vector operators, in section III B, we know that
(b)ˆτ 1· (c)ˆτ 1|ιjajbjc⟩ =− 2√
jb(jb + 1)jc(jc + 1)
(b)⃗J· (c)⃗J|ιjajbjc⟩.
This allows to identify the source of the discrepancy for the 1
2 and the overall sign. In particular, the global minus
sign in (98) and (99) with respect to the ﬂat/hyperbolic cosine law comes simply from the deﬁnition of the scalar
product we have used.
Since (i)⃗J is interpreted in the LQG formalism as the quantized normal to the edge of the triangle, in the deformed
case, we interpret (b)ˆt1 and (c)ˆt1 as the quantized normals respectively of the edges AC and AB, at the vertex A of
the hyperbolic triangle.
We can play with the normalization of the vector operators to have a better deﬁned hyperbolic law. Indeed, we
notice that both (98) and (99) diverge when j = 0. Instead of taking the vector operator (i)ˆt1 with normalization
N1
ji = 1, we can consider (i)˜t1 with normalization
˜N1
j ≡
√
sinh(jλ) sinh((j + 1)λ)
sinh((j + 1
2)λ)
q→1
→
√
j(j + 1)
j + 1
2
. (100)
In this case the cosine laws become well behaved for small j.
(b)˜t1· (c)˜t1|ιjbjcja⟩ =q
cosh 𝓁p
2𝓁c
cosh((ja + 1
2)λ)− cosh((jb + 1
2)λ) cosh((jc + 1
2)λ))
sinh((jb + 1
2)λ) sinh((jc + 1
2)λ) |ιjbjcja⟩. (101)
When dealing with a non-zero cosmological constant and the Planck length, by dimensional analysis, one can expect
to have a minimum angle [50]. This can now be explicitly checked. Setting ja = 0, we must havejb =jc =j since we
23
deal with an intertwiner, and the quantum cosine law (98) gives
θmin
a (j) = arccos
(
q cosh2 λ
2− cosh2((j + 1
2)λ)
sinh2((j + 1
2)λ)− sinh2 λ
2
)
, (102)
which means that there is a non-zero minimum angle. When 𝓁p→ 0 (classical limit) or R→∞ (ﬂat quantum limit),
(102) tends to 1, so we recover that the triangle is degenerated.
As expected, the angle observables can be expressed in terms of the Uq(su(2)) generators.
i>j, (i)ˆt1· (j)ˆt1 =
(
q− 3
2 (−EijEji +Eii) + 1
[2]EiiEjj
)
, i<j, (i)ˆt1· (j)ˆt1 =
(
q
1
2 (−EijEji +Eii) + q2
[2]EiiEjj
)
.
Length operator. The length operator is obtained by looking at the norm of the unnormalized vector operator
(i)t1 with normalization Ni
j.
(i)t1·(i) t1|ιjbjcja⟩ =
(
N1
ji
)2
|ιjbjcja⟩, i =a,b,c. (103)
Keeping in mind that (i)t1 encodes the quantization of the normal, by inspection of the classical and quantum
hyperbolic cosine law, it is natural to take
N1
j =
√
sinh2((j + 1
2)λ)− sinh2(λ
2 ) or ˜N1
j = sinh((j + 1
2)λ). (104)
The normalization ˜N1
j leads to the regularized hyperbolic cosine law (101). We note therefore that the norm of the
vector operator corresponds to a function of the length operator. The length is quantized, with eigenvalue ( j + 1
2)𝓁p
as we have argued previously. The norm of the vector operator can be expressed in terms of the E operators.
(i)t1· (i)t1 = 1
[2](−qE2
i− (1 +q−1)Ei). (105)
”Area” operator. In the ﬂat case, one expresses the square of the area of the triangle in terms of a cosine and the
norm of the normals so that the operator is easy to quantize, using vector operators [51].
A2 = 1
4
(
|⃗ nb|2|⃗ nc|2− (⃗ nc·⃗ nc)2)
(106)
We proceed in the same manner in the hyperbolic case. We do not consider the square of the area but instead the
square of the sine of the area. Indeed, the area of an hyperbolic triangle is given in terms of the triangle angles (97).
There are various ways to express functions of the area in terms of the edge lengths [52]. A convenient one will be
sin2 A
2R2 = sinh( s
2R) sinh(s−𝓁a
2R ) sinh(s−𝓁b
2R ) sinh(s−𝓁c
2R )
cosh2 𝓁a
2R cosh2 𝓁b
2R cosh2 𝓁c
2R
, (107)
where s = 1
2(𝓁a +𝓁b +𝓁c). Of course, in the ﬂat limit, R→∞ , we recover Heron’s formula (see the above table).
Playing with the cosine laws, we can express sin 2 A
2R2 only in terms of the normals.
sin2 A
2R2 = 1
4
sinh2 𝓁b
R sinh2 𝓁c
R (1− cos2θa)
(cosh2 𝓁a
2R cosh2 𝓁b
2R cosh2 𝓁c
2R) = 2 |⃗ nb|2|⃗ nc|2− (⃗ nb·⃗ nc)2
(1 +
√
1 +|⃗ na|2)(1 +
√
1 +|⃗ nb|2)(1 +
√
1 +|⃗ nc|2)
. (108)
There is no diﬃculty in quantizing this expression since it only involves scalar products and norms of nromals, which
upon quantization become operators that are diagonal and functions of the Casimir operator. There is therefore no
ordering issue anywhere. The area has also a discrete spectrum.
24
