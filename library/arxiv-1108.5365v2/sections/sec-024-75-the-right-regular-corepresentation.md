---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-024-75-the-right-regular-corepresentation
section_title: "The right regular corepresentation"
section_number: 7.5
pages: 72-75
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
In analogy to the left regular action, there is a notion of a right regu lar action.
First we consider the quantum plane.
Proposition 7.21. Given W that deﬁnes the left regular corepresentation,
WR := ( ˆJ⊗ ˆJ)W ∗
21( ˆJ⊗ ˆJ)∈B (H)⊗A (7.62)
is also a multiplicative unitary and satisﬁes
(1⊗ ∆) WR =WR,12WR,13, (7.63)
i.e. it deﬁnes a corepresentation, called the right-regula r corepresentation.
Using the realization of Ad ˆJ, we see that WR is given by
WR =e
i
2πb 2 log A∗⊗log Agb(B∗⊗B) = e
i
2πb 2 log A∗⊗log A
∫
R+i0
Bib−1τ
∗ ⊗Bib−1τ e−πiτ 2
Gb(Q +iτ )dτ,
(7.64)
where on the space Hcorep we have ˆJ =f (t,s ) so that
A∗ =e−2πbt, B ∗ =e−2πbpt. (7.65)
Therefore we see that the corepresentation is acting on the t-coordinate by:
f (s,t )↦→
∫
R+i0
f (s,t−τ ) e−πiτ 2
Gb(Q +iτ )A−ib−1tBib−1τdτ, (7.66)
in which under the pairing we have:
Xr =e−2πbt, Y r =e−2πbpt, (7.67)
~Xr =e−2πb−1t, ~Yr =e−2πb−1pt. (7.68)
In other words, under the transform t↦→−t, we conclude together with Proposition
6.16 that
Proposition 7.22. We have the equivalence
L2(A)≃H irr⊗H irr (7.69)
as representation ofBq~q,L⊗B q~q,R≃B q~q⊗B q~q, whereHirr :=L2(R) is the canonical
representation ofBq~q on L2(R). Hence this is an analogue to the classical “Peter-
Weyl” theorem on “functions on the quantum plane”.
72
Now let us look at the case for D(A). To deﬁne the right regular corepresenta-
tion, we need the corresponding multiplicative unitary WR. It is known that WR
is given by
WR = (U⊗ 1)W3412(U ∗⊗ 1), (7.70)
where
U = ˆJmJm = (J ˆJ⊗ ˆJJ )Z∈A⊗ ˆA. (7.71)
We simplify the expression and express WR in terms of 4 gb’s as before.
Proposition 7.23. WR is given by (cf. (7.49))
WR =V32WR,13V
′′∗
32 ˆWR,24, (7.72)
whereV
′′∗ = ( ˆJ⊗ ˆJ)V ∗( ˆJ⊗ ˆJ).
Proof. From ([25] Prop 2.15), we have:
ˆW = W ∗
21,
WR = ( ˆJ⊗ ˆJ)W ∗
21( ˆJ⊗ ˆJ)
= ( ˆJ⊗ ˆJ)(J⊗ ˆJ)W21(J⊗ ˆJ)( ˆJ⊗ ˆJ)
= ( ˆJJ⊗ 1)W21(J ˆJ⊗ 1),
ˆWR = ( J⊗J)W (J⊗J)
= ( J⊗J)( ˆJ⊗J)W ∗( ˆJ⊗J)(J⊗J)
= ( J ˆJ⊗ 1)W ∗( ˆJJ⊗ 1).
Hence we obtain (the indices indicate the legs in which the operators a re acting):
WR = (( J1 ˆJ1 ˆJ2J2)Z12)W31Z ∗
12 ˆW42Z12(Z ∗
12( ˆJ1J1J2 ˆJ2))
= ( J1 ˆJ1 ˆJ2J2)Z12W31Z ∗
12 ˆW42( ˆJ1J1J2 ˆJ2)
= ( J1 ˆJ1 ˆJ2J2)V12V ′
12W31V ∗′
12V ∗
12 ˆW42( ˆJ1J1J2 ˆJ2)
= ( J1 ˆJ1 ˆJ2J2)( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)V12W31V ∗
12 ˆW42( ˆJ1J1J2 ˆJ2)
= ( J1 ˆJ1 ˆJ2J2)( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)W31V32 ˆW42( ˆJ1J1J2 ˆJ2)
= ( J1 ˆJ1 ˆJ2J2)( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)W31V32(J1 ˆJ1J2 ˆJ2) ˆWR,24
= ( J1 ˆJ1 ˆJ2J2)( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)( ˆJ1J1)WR,13V32(J2 ˆJ2) ˆWR,24
= ( ˆJ2J2)( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)WR,13V32(J2 ˆJ2) ˆWR,24
= ( J2 ˆJ3)V ∗
32( ˆJ2 ˆJ3)WR,13V32( ˆJ2J2) ˆWR,24
= V32(J2 ˆJ3)( ˆJ2 ˆJ3)WR,13V32( ˆJ2J2) ˆWR,24
= V32WR,13(J2 ˆJ2)V32( ˆJ2J2) ˆWR,24
= V32WR,13(J2 ˆJ2)(J2 ˆJ3)V ∗
32(J2 ˆJ3)( ˆJ2J2) ˆWR,24
= V32WR,13( ˆJ2 ˆJ3)V ∗
32( ˆJ2 ˆJ3) ˆWR,24.
73
Now we can realize the action on Hcorep⊗ ˆHcorep as in previous section:
Proposition 7.24. The action of the components of WR is given by
ˆWR,24 = e− i
2πb 2 log ˆA∗⊗log ˆAg∗
b ( ˆB∗⊗ ˆB)
f (s1,t 1)g(s2,t 2) ↦→
∫
f (s1,t 1)g(s2,t 2−τ )e−2πiτ t2+πiτ 2
Gb(−iτ ) ˆBib−1τ ˆA−ib−1t2dτ,
WR,13 = e
i
2πb 2 log A∗⊗log Agb(B∗⊗B)
f (s1,t 1)g(s2,t 2) ↦→
∫
f (s1,t 1−τ )g(s2,t 2) e−πiτ 2
Gb(Q +iτ )A−ib−1t1Bib−1τdτ,
V32 = e
i
2πb 2 log ˆA−1⊗log A−1
gb(q ˆB ˆA−1⊗B)
f (s1,t 1)g(s2,t 2) ↦→
∫
R
∫
R+i0
∫
R
f (s1,t 1)g(s2 +α,t 2 +α +τ )
e2πi(αβ+ατ +βτ +s2τ )Gb( Q
2 +is2−it2)
Gb( Q
2 +is2−it2−iτ )Gb(Q +iτ )
Aib−1βBib−1τdαdτdβ,
V
′′∗
32 = e
i
2πb 2 log A∗⊗log Agb(B∗⊗B)
f (s1,t 1)g(s2,t 2) ↦→
∫
R
∫
R+i0
∫
R
g(s2 +α,t 2 +α +τ )
e2πiα(t2−s2−β)e−πiτ 2
Gb( Q
2 +is2−it2)
Gb( Q
2 +is2−it2−iτ )Gb(Q +iτ )
Aib−1βBib−1τdαdτdβ.
Theorem 7.25. The right regular corepresentation is given by
f (s1,t 1)g(s2,t 2) ↦→
∫
R+iǫτ
∫
R
∫
C
dσdαdτf (s1,t 1−σ)g(s2 +σ,t 2 +τ−α)
eπQ(−α+τ )+2πi(−σs2+ατ −αt2+σt2)
Gb(−iσ)Gb( Q
2 +is2−it2)Gb(iσ−iτ )Gb( Q
2−iσ +it1−it2)
Gb( Q
2 +is2−it2 +iσ−iτ )Gb(Q +iα)Gb( Q
2−iτ +it1−it2)
Aib−1(t2−t1−s2)Bib−1τ ˆBib−1α ˆA−ib−1(t2+τ )dαdτdσ,
where the contour C of σ goes above σ = 0 and below σ =τ .
We have to follow the transformations given in the left regular pictur e. So we
apply the transformations after Theorem 7.20 and an extra one th at does not aﬀect
74
the previous action:
s2 ↦→ s2−t1,
s1 ↦→ s1 + s2
2 ,
t1 ↦→ t1 + s2
2 ,
t2 ↦→ t2 + s2
2 ,
and obtain
f⊗g ↦→
∫
R+iǫτ
∫
R
∫
C
dσdαdτf (s1,t 1−σ)g(s2,t 2 +τ−α)
eπQ(−α+τ )+2πi(σt1+ατ −αt2+σt2)e−πiαs2
Gb(−iσ)Gb( Q
2−it1−it2)Gb(iσ−iτ )Gb( Q
2−iσ +it1−it2)
Gb( Q
2−it1−it2 +iσ−iτ )Gb(Q +iα)Gb( Q
2−iτ +it1−it2)
Aib−1(t2− s2
2 )Bib−1τ ˆBib−1α ˆAib−1(−t2−τ − s2
2 )dαdτdσ. (7.73)
