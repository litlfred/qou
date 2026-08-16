---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗"
section_id: sec-030-2-partial-wave-decomposition
section_title: "Partial wave decomposition"
section_number: 2
pages: 26-28
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗ — 35 sections: Scattering equation . . . . . . . ; R-matrix and partial wave decompos; Phase shifts . . ."
---
The potential is decomposed into partial waves according to
⟨λ′
1λ′
2|V J(q′,q )|λ1λ2⟩= 2π
∫ +1
−1
d(cosθ)dJ
λ 1−λ 2,λ ′
1−λ ′
2
(θ)⟨q′λ′
1λ′
2|V |qλ1λ2⟩
(B10)
where θ is the angle between q and q′ and dJ
m,m ′(θ) are the conventional reduced rotation
matrices which can be expressed in terms of Legendre polynom inalsPJ (cosθ). The following
types of integrals occur:
I (0)
J ≡
∫ +1
−1
dt PJ (t)
(q′ − q)2 +m2
α
= QJ (zα )
q′q , (B11)
I (1)
J ≡
∫ +1
−1
dt tPJ (t)
(q′ − q)2 +m2
α
= Q(1)
J (zα )
q′q , (B12)
I (2)
J ≡ 1
J + 1
∫ +1
−1
dt JtP J (t) +PJ−1(t)
(q′ − q)2 +m2
α
= Q(2)
J (zα )
q′q , (B13)
26
I (3)
J ≡
√
J
J + 1
∫ +1
−1
dt tPJ (t) −PJ−1(t)
(q′ − q)2 +m2
α
= Q(3)
J (zα )
q′q , (B14)
I (4)
J ≡
∫ +1
−1
dt t2PJ (t)
(q′ − q)2 +m2
α
= Q(4)
J (zα )
q′q , (B15)
I (5)
J ≡ 1
J + 1
∫ +1
−1
dt Jt 2PJ (t) +tPJ−1(t)
(q′ − q)2 +m2
α
= Q(5)
J (zα )
q′q , (B16)
I (6)
J ≡
√
J
J + 1
∫ +1
−1
dt t2PJ (t) −tPJ−1(t)
(q′ − q)2 +m2
α
= Q(6)
J (zα )
q′q , (B17)
with t ≡ cosθ and zα ≡ (q′2 +q2 +m2
α )/2q′q where our notation for momenta is q′ ≡ | q′|,
and q ≡ |q| which we will use throughout the remainder of the appendices .
The QJ (z) are the Legendre functions of the second kind [105]; e. g., Q0(z) = 1
2 ln[(z +
1)/(z − 1)]. The combinations needed above are deﬁned by:
Q(1)
J (z) ≡zQJ −δJ0, (B18)
Q(2)
J (z) ≡ 1
J + 1 (JzQ J +QJ−1), (B19)
Q(3)
J (z) ≡
√
J
J + 1 (zQJ −QJ−1), (B20)
Q(4)
J (z) ≡zQ(1)
J − 1
3δJ1, (B21)
Q(5)
J (z) ≡zQ(2)
J − 2
3δJ1, (B22)
Q(6)
J (z) ≡zQ(3)
J + 1
3
√
2δJ1. (B23)
(B24)
The integrals Eqs. (B11)-(B17) can be evaluated either nume rically or analytically by us-
ing the Legendre functions of the second kind. The latter met hod is better if the correct
threshold behavior of V J (q′,q ) for q′,q → 0 is important.
The above expressions still ignore the cutoﬀ which is includ ed by replacing
1
(q′ − q)2 +m2
α
− → F 2
α [(q′ − q)2]
(q′ − q)2 +m2
α
(B25)
in Eqs. (B11)-(B17). If the Legendre functions of the second kind are used, then the product
of propagator and cutoﬀ must be decomposed according to
F 2
α [(q′ − q)2]
(q′ − q)2 +m2
α
= 1
(q′ − q)2 +m2
α
−
(
Λ 2
α 2 −m2
α
Λ 2
α 2 − Λ 2
α 1
)
1
(q′ − q)2 + Λ 2
α 1
+
(
Λ 2
α 1 −m2
α
Λ 2
α 2 − Λ 2
α 1
)
1
(q′ − q)2 + Λ 2
α 2
(B26)
27
where Λ α 1/ 2 ≡ Λ α ±ǫ with ǫ → 0; i. e., ǫ ≪ Λ α , e. g., ǫ ≈ 1 MeV. To give an example, I (0)
J
with cutoﬀ is given by
I (0)
J =
∫ +1
−1
dt PJ (t)F 2
α [(q′ − q)2]
(q′ − q)2 +m2
α
(B27)
= QJ (mα )
q′q −
(
Λ 2
α 2 −m2
α
Λ 2
α 2 − Λ 2
α 1
)
QJ (Λ α 1)
q′q +
(
Λ 2
α 1 −m2
α
Λ 2
α 2 − Λ 2
α 1
)
QJ (Λ α 2)
q′q , (B28)
and similarly for the other I (i)
J . Notice that the I (i)
J are functions of q′, q, mα , and Λ α even
though our notation does not indicate this.
