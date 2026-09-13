---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-018-25-propagator
section_title: "Propagator"
section_number: 2.5
pages: 42-45
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Eﬃciently sampling the imaginary time propagator e−H∆τ by using a short-time
approximated propagator U(∆τ) is important for PIMC. Due to the fact that the
local chiral N2LO interaction contains the spin-orbit term vLS(rij) in Eq.(2.24), the
approximated short-time propagator U(∆τ) for e−H∆τ is calculated as,
U(∆τ)≡e−V†
2 ∆τGe−T ∆τe−V
2 ∆τ =e−H∆τ +O(∆τ 2), (2.61)
32
whereV is the NN potential only with the ﬁrst 6 operators in Eq.(2.19) plus the EM
force in Eq.(2.25),
V =
∑
i<j
[ 6∑
p=1
vp(rij)Op
ij +VEM
ij (rij)
]
≡
∑
i<j
Vij. (2.62)
Fore−V
2 ∆τ, we pick an order of each ij pair and calculate it using the following
approximation,
e−V
2 ∆τ =e
−VA−1A∆t
2 e
−VA−2A∆t
2 ...e
−V13∆t
2 e
−V12∆t
2 +O(∆τ)2, (2.63)
where theO(∆τ)2 terms are due toVij do not commute with each other for diﬀerent
ij pairs, and e−V†
2 ∆τ is the Hermitian conjugate of the e−V
2 ∆τ approximation which is
the reverse order of Eq.(2.63). Note that the ﬁrst 6 operators in VNN
ij in Eq.(2.19),
VNN
ij commutes with the VEM
ij , so we have,
e−
Vij
2 ∆τ =e−
∑6
p=1vp(rij)Op
ij
2 ∆τe−
VEM
ij
2 ∆τ. (2.64)
The ﬁrst 6 operators in VNN
ij are the same AV6’ operators and they form a group.
e− ∑6
p=1vp(rij)Op
ij∆τ in Eq.(2.64) can be linearized by the original 6 operators Op
ij in the
following way,
e− ∑6
p=1vp(rij)Op
ij∆τ =
6∑
p=1
up
ij(rij)Op
ij, (2.65)
where the six coeﬃcients up
ij(rij) can be solved once rij is given 4 .
The symbolG is the approximated short-time propagator for the spin-orbit term
e−VLS∆τ to the linear order 5 ,
G≡ 1−
∑
i<j
vLS(ˆrij)∆τ =e−VLS∆τ +O(∆τ 2). (2.67)
4See Appendix D for details about linearizing the AV6’ operators in the propagator. In order
to save time, in the code all the up(r) are tabulated for the relevant range of r before performing
the Monte Carlo simulations. And the interpolations of the table are done by Lagrange 4-point
interpolation polynomials.
5The three body interaction V3b =∑
i<j<kVijk may be added in the same way as the spin-orbit
33
The approximated short-time propagator U(∆τ) in our basis is calculated as,
⟨R′S′|U(∆τ)|RS⟩
=
⟨
R′
⏐⏐⏐⊗
⟨
S′
⏐⏐⏐e−V†
2 ∆τGe−T ∆τe−V
2 ∆τ
⏐⏐⏐R
⟩
⊗
⏐⏐⏐S
⟩
=
⟨
S′
⏐⏐⏐⏐⏐e−V†(R′)
2 ∆τ
{[
1−
∑
i<j
v7(r′
ij)Lij·Sij∆τ
]
⟨
R′⏐⏐e−T ∆τ⏐⏐R
⟩
}
e−V(R)
2 ∆τ
⏐⏐⏐⏐⏐S
⟩
=
⟨
S′
⏐⏐⏐⏐e−V†(R′)
2 ∆τ Ge−V(R)
2 ∆τ
⏐⏐⏐⏐S
⟩
×Gf
R′R. (2.68)
The symbol Gf
R′R in Eq.(2.68) means the products of the free particle propagator
of each particle in the system,
Gf
R′R≡⟨R′|e−T ∆τ|R⟩ =
A∏
i=1
⟨r′
i|e−
p2
i ∆τ
2m|ri⟩≡
( m
2π∆τ ℏ2
) 3A
2
e
− (R′−R)2
2∆τ ℏ2
m , (2.69)
and (R′−R)2 is calculated as,
(R′−R)2 =
A∑
i=1
(r′
i−ri)2 =
A∑
i=1
[
(x′
i−xi)2+(y′
i−yi)2+(z′
i−zi)2]
. (2.70)
The symbol G in Eq.(2.68) is the eﬀective G which is written as,
G = 1−
(−m
4iℏ2
)∑
i<j
v7(r′
ij)
[
r′
ij× ∆rR′,R
ij
∆τ · (σi +σj)
]
∆τ, (2.71)
wherer′
ij is the distance between particlei andj in conﬁgurationR′,r′
ij≡ri−rj inR′,
and ∆rR′,R
ij ≡ ∆rR′,R
i − ∆rR′,R
j where ∆rR′,R
i ≡rR′
i −rR
i and ∆rR′,R
j ≡rR′
j −rR
j , and
the symbolrR′(R)
i(j) simply means the ri(j) in conﬁguration R′(R). Note that Eq.(2.71)
does not explicitly contain ∆τ anymore. However, as will be shown in chapter 3,
∆rR′,R
ij will essentially have the order of ∆τ becauserR′
j will be eﬀectively sampled
aroundrR
j from a gaussian function whose variance is the order of ∆ τ.
term in Eq.(2.61) to the linear order, such that
G≡ 1−
∑
i<j
vLS(ˆrij)∆τ−
∑
i<j<k
Vijk∆τ. (2.66)
For light nuclei this linear approximation may be suﬃcient because the three-body force and the spin-
orbit force usually have opposite sign and similar strength, soG is close to 1 and the ﬂuctuation in the
propagator will not be too big. Better approximations for the 3-body propagator are straightforward
since they do not contain derivatives.
34
