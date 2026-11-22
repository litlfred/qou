---
doc_id: 13116841v1
doc_title: "Observables in Loop Quantum Gravity with a cosmological constant"
section_id: sec-012-a-rank-12-tensor-operators
section_title: "A Rank 1/2 tensor operators"
section_number: null
pages: 11-13
source_pdf: 1311.6841v1.pdf
source_sha256: ca65879d80b1e1c3
toc_source: outline
doc_brief: "Observables in Loop Quantum Gravity with a cosmological constant — 22 sections: Front matter; Contents; Introduction"
---
Rank 1
2 tensor operators (i.e. spinor operators) t
1
2m should be solution of the following constraints.
J± ▷t
1
2
∓= t
1
2
±,
J± ▷t
1
2
± = 0,
Jz ▷t
1
2
± = ±1
2t
1
2
±.
(43)
Using the Schwinger-Jordan realization of Uq(su(2)) generators given in (19), we can solve these equations and we get
two solutions T
1
2 and ˜T
1
2 satisfying (43).
T
1
2 =
 
A†
B†
!
=
 
a†qNa/4
b†q(2Na+Nb)/4
!
,
˜T
1
2 =
 
˜B
˜A
!
=
 
q(2Na+Nb+1)/4b
−q(Na−1)/4a
!
.
(44)
We recall that a and b are q-harmonic oscillators which satisfy the modiﬁed commutation relations (16). We can check
that T
1
2 and ˜T
1
2 are Hermitian conjugate to each other, according to the modiﬁed bilinear form we have deﬁned in
Section II B 1 (see (30)). When looking at the limit q →1, we have
T
1
2 →τ
1
2 =
 
a†
b†
!
,
˜T
1
2 →˜τ
1
2 =
 
b
−a
!
.
(45)
4 Note that in the limit q →1, this would be satisﬁed. Hence 1 ⊗˜t is a tensor operator for su(2).
5 Rms = 1s−1 ⊗R2 ⊗1m−s−1 ⊗R1, using notations of (6).
This explicit realization of the tensor operators allows to check explicitly the Wigner-Eckart theorem, and to identify
the normalization of the operators through this realization. In particular, for the q-deformed spinor operator matrix
elements, we have
⟨j1, m1|T
1
2
m|j2, m2⟩= δj1,j2+1/2 N
1
2
j2 qC1/2 j2 j1
m m2 m1, with N
1
2
j2 =

([dj2])1/2q
j2
2

,
⟨j1, m1| ˜T
1
2
m|j2, m2⟩= δj1,j2−1/2 ˜N
1
2
j2 qC1/2 j2 j1
m m2 m1, with ˜N
1
2
j2 =

([dj2])1/2q
1
4 (2j2−1)
,
(46)
where m = ±1/2 and dj = 2j + 1. We have therefore the two possible realizations of spinor operators in terms of
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
2 are deﬁned up to a multiplicative function of Na + Nb. Therefore, N
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
deformed harmonic oscillators a†
i, ai, Nai, b†
i, bi, Nbi ∈Fi ∼Fai ⊗Fbi where the Fi (i = 1, · · · , N) are N independent
q-Fock spaces. Let us deﬁne the tensor operators (i)T
1
2 and (i) ˜T
1
2 living in F ≡(⊗N
i=1Fai)(⊗N
i=1Fbi) which “act” on
the ith Hilbert space.
(i)T
1
2 =
 
A†
i
B†
i
!
,
(i) ˜T
1
2 =
 
˜Bi
˜
Ai
!
,
for i ∈{1, · · · , N},
(47)
where
(i)T
1
2
+ := A†
i = (⊗i−1
k=1q
Nak −Nbk
4
) a†
iq
Nai
4 ,
(i)T
1
2
−:= B†
i = (⊗i−1
k=1q
−Nak +Nbk
4
) b†
iq
2Nai +Nbi
4
+ (q
1
4 −q−3
4 )
"i−1
X
l=1
(⊗l−1
k=1q
−Nak +Nbk
4
) alb†
l (⊗i−1
k=l+1q
Nak −Nbk
4
)
#
a†
iq
Nai
4 ,
(i) ˜T
1
2
+ := ˜Bi = (⊗i−1
k=1q
Nak −Nbk
4
) q
2Nai +Nbi +1
4
bi,
(i) ˜T
1
2
−:= ˜
Ai = (⊗i−1
k=1q
−Nak +Nbk
4
) (−q
Nai −1
4
ai) + (q
1
4 −q−3
4 )
"i−1
X
l=1
(⊗l−1
k=1q
−Nak +Nbk
4
) alb†
l (⊗i−1
k=l+1q
Nak −Nbk
4
)
#
q
2Nai +Nbi +1
4
bi.
These operators will be the building blocks of our construction of Uq(su(2))-observables presented in the following
section. It will be necessary to have their explicit form in terms of the harmonic oscillators in order to recover the
Uq(u(n)) structure in Section IV B.
Note that if i̸ = 1, the two spinor operators (i)T
1
2 and (i) ˜T
1
2 are no more Hermitian conjugated to each other.
Indeed, (A†
i)†̸ = −q1/4 ˜
Ai, (B†
i )†̸ = q−1/4 ˜Bi, i ∈{2, · · · , N}. To emphasize this lack of Hermiticity, we introduce the
notation,
Ci ≡−q1/4 ˜
Ai,
Di ≡q−1/4 ˜Bi,
∀i ∈{1, · · · , N}.
(48)
That is, we can rewrite the spinor operators (i) ˜T
1
2 as (i) ˜T
1
2 =
 
q
1
4 Di
−q−1
4 Ci
!
.
Quesne has calculated all possible
commutation relations between the components of (i)T
1
2
±, (j) ˜T
1
2
± for any i, j ∈{1, · · · , N} [36]. First let us give the
commutation relations when 1 ≤i = j ≤N.
B†
i A†
i = q1/2A†
iB†
i ,
CiDi = q1/2DiCi,
DiA†
i = q1/2A†
iDi,
CiB†
i = q1/2B†
i Ci,
CiA†
i = qA†
iCi + 1,
DiB†
i = qB†
i Di + (q −1)A†
iCi + 1.
(49)
When 1 ≤i < j ≤N, we have
A†
iA†
j = q−1/4A†
jA†
i,
A†
iB†
j = q1/4B†
jA†
i −(q3/4 −q−1/4)A†
jB†
i ,
B†
i A†
j = q1/4A†
jB†
i ,
B†
i B†
j = q−1/4B†
jB†
i ,
DiDj = q−1/4DjDi,
DiCj = q1/4CjDi −(q3/4 −q−1/4)DjCi,
CiDj = q1/4DjCi,
CiCj = q−1/4CjCi,
A†
iDj = q−1/4DjA†
j,
DiA†
j = q−1/4A†
jDi,
B†
i Cj = q−1/4CjB†
i ,
CiB†
j = q−1/4B†
jCi,
B†
i Dj = q1/4DjB†
i ,
DiB†
j = q1/4 
B†
jDi + (1 −q−1)A†
jCi

,
A†
iCj = q1/4 
CjA†
i + (q −1)DjB†
i

,
CiA†
j = q1/4A†
jCi.
(50)
These commutation relations are quite cumbersome and they illustrate that the components of operators acting on
diﬀerent Hilbert spaces do not commute when q̸ = 1. Obviously, when q = 1, they simplify a lot.
B.
