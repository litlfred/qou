---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-022-73-the-multiplicative-unitary
section_title: "The multiplicative unitary"
section_number: 7.3
pages: 61-66
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Given two locally compact quantum groups ( M1, ∆ 1) and (M2, ∆ 2), with a match-
ing m : M1⊗M2−→M1⊗M2, the multiplicative unitary for the double crossed
product is ﬁrst constructed in [1]. The quantum double group const ruction is a spe-
cial case given by ( M1, ∆ 1) = (A, ∆ op) and (M2, ∆ 2) = ( ˆA, ˆ∆), while the matching
m is given by m(x) = W (x)W ∗ as before [16]. Let us restrict to the quantum plane
case and describe the main ingredients needed.
Proposition 7.15. The multiplicative unitary operator is deﬁned by
Wm := W =W13Z ∗
34 ˆW24Z34∈B (H⊗ ˆH⊗H⊗ ˆH), (7.38)
whereZ∈B (H⊗ ˆH) is given by
Z =W ( ˆJ1J1⊗J2 ˆJ2)W ∗( ˆJ1J1⊗ ˆJ2J2) = W ( ˆJJ⊗ ˆJJ )W ∗( ˆJJ⊗J ˆJ), (7.39)
and ˆW = ΣW ∗Σ = W ∗
21.
61
The coproduct is given by
∆ m = (ι⊗σm⊗ι)(∆ op
1 ⊗ ∆ 2) = (ι⊗σm⊗ι)(∆ ⊗ ˆ∆) , (7.40)
wherem(z) = ZzZ ∗, and
∆ m(z) = W∗(1⊗z)W (7.41)
for z∈D (A).
The matching m satisﬁes
(∆ op⊗ 1)m =m23m13(∆ op⊗ 1), (7.42)
(1⊗ ˆ∆) m =m13m12(1⊗ ˆ∆) . (7.43)
First of all we note the diﬀerence in the deﬁnition of the matching m. In fact
they are the same.
Proposition 7.16. We actually have
m(x) = ZxZ ∗ =WxW ∗ (7.44)
for x∈A⊗ ˆA. In particular from the pentagon equation of W and ˆW =W ∗
21, the
matching satisﬁes the property (7.42) and (7.43).
Proof. Recall the conjugation properties from (5.46), (5.47):
( ˆJ⊗J)W ( ˆJ⊗J) = W ∗, (7.45)
(J⊗ ˆJ) ˆW (J⊗ ˆJ) = ˆW ∗. (7.46)
Using also (5.45), we have
W ( ˆJJ⊗ ˆJJ )W ∗( ˆJJ⊗J ˆJ )
= νi/4W (J⊗ ˆJ)( ˆJ⊗J)W ∗( ˆJ⊗J)(J⊗ ˆJ)
= νi/4W (J⊗ ˆJ)W (J⊗ ˆJ)
Hence using the deﬁnition (7.39) of Z, expanding ZxZ ∗ =WxW ∗ we have
W (J⊗ ˆJ)W (J⊗ ˆJ)x(J⊗ ˆJ)W ∗(J⊗ ˆJ)W ∗ =WxW ∗,
or
(J⊗ ˆJ)W (J⊗ ˆJ)x =x(J⊗ ˆJ)W (J⊗ ˆJ),
that is, (J⊗ ˆJ)W (J⊗ ˆJ) commutes with every x∈A⊗ ˆA⊂B (H⊗ ˆH) as operators.
However, since W∈A⊗ ˆA, from Corollary 6.11, it is clear that
(J⊗ ˆJ)W (J⊗ ˆJ) = g∗
b (q ˆB∗ ˆA−1
∗ ⊗B∗)e
i
2πb 2 log ˆA∗⊗log A∗
commutes with every x∈A⊗ ˆA.
62
For completeness, let us also reprove the coproduct formula.
Proof. Recall
W =W13Z ∗
34W ∗
42Z34,
∆( x) = W ∗(1⊗x)W,
ˆ∆( y) = ˆW ∗(1⊗y) ˆW =W21(1⊗y)W ∗
21.
Hence
W∗(1⊗z)W = Z ∗
34W42Z34W ∗
13(1⊗z)W13Z ∗
34W ∗
42Z34
= Z ∗
34W42Z34(∆ ⊗ι)(z)134Z ∗
34W ∗
42Z34
= Z ∗
34W42(ι⊗m)((∆ ⊗ι)(z))134W ∗
42Z34
= Z ∗
34((ι⊗ι⊗ ˆ∆)( ι⊗m)(∆ ⊗ι)(z))1324Z34
= Z ∗
34(m24m23(ι⊗ι⊗ ˆ∆)(∆ ⊗ι)(z))1324Z34
= Z ∗
34(Z24m23(ι⊗ι⊗ ˆ∆)(∆ ⊗ι)(z)Z ∗
24)1324Z34
= Z ∗
34Z34m32(ι⊗ι⊗ ˆ∆)(∆ ⊗ι)(z)Z ∗
34Z34
= ( σm)23(ι⊗ι⊗ ˆ∆)(∆ ⊗ι)(z)
= ∆ m(z).
It is proved in [1] for general matching m that Wm := W is a multiplicative
unitary. Here we present a direct proof using the fact that m is given by the
multiplicative unitary W .
Theorem 7.17. W is a multiplicative unitary, i.e. it satisﬁes
W3456W1234 = W1234W1256W3456.
Proof. It suﬃces to check that
W3456Z ∗
34 ˆW24Z34W∗
3456 =Z ∗
34Z ∗
56 ˆW24 ˆW26Z34Z56
and
W3456W13W∗
3456 =W35W13W ∗
35 =W13W15.
The second equation follows directly from the deﬁnition and the pent agon equa-
tion for W .
Let us write Z =VV ′ where V ∈B (H⊗ ˆH) and V ′ = (J⊗ ˆJ )V (J⊗ ˆJ) is the
copy of W based on diﬀerent spaces. Note that V,V ′ commute. Also V ′ commutes
with entries in A⊗ ˆA⊂B (H⊗ ˆH).
From the pentagon equation for W , but with its legs sitting on diﬀerent spaces,
we have the relations (cf. Corollary 2.20):
V23W12 =W12V13V23∈B (H⊗H⊗ ˆH), (7.47)
63
V13 ˆW23 = ˆW23V13V12∈B (H⊗ ˆH⊗ ˆH). (7.48)
Using also (7.45) and (7.46), we derive the relations
V ′
56W ∗
35 = ( J5⊗ ˆJ6)V56(J5⊗ ˆJ6)( ˆJ3⊗J5)W35( ˆJ3⊗J5)
= ( ˆJ3⊗J5⊗ ˆJ6)V56W35( ˆJ3⊗J5⊗ ˆJ6)
= ( ˆJ3⊗J5⊗ ˆJ6)W35V36V56( ˆJ3⊗J5⊗ ˆJ6)
= W ∗
35( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)(J5⊗ ˆJ6)V56(J5⊗ ˆJ6)
= W ∗
35( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)V ′
56,
ˆW ∗
46( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6) = ( J4⊗ ˆJ6) ˆW46(J4⊗ ˆJ6)( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)
= ( ˆJ3⊗J4⊗ ˆJ6) ˆW46V36( ˆJ3⊗J4⊗ ˆJ6)
= ( ˆJ3⊗J4⊗ ˆJ6)V36 ˆW46V ∗
34( ˆJ3⊗J4⊗ ˆJ6)
= ( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)(J4⊗ ˆJ6) ˆW46(J4⊗ ˆJ6)( ˆJ3⊗J4)V ∗
34( ˆJ3⊗J4)
= ( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6) ˆW ∗
46V34.
Hence
W3456Z ∗
34 ˆW24Z34W ∗
3456
= W35Z ∗
56 ˆW46Z56Z ∗
34 ˆW24Z34Z ∗
56 ˆW ∗
46Z56W ∗
35
= ( W35V ∗
56V ∗′
56 ˆW46V ∗
34V ∗′
34 ) ˆW24(V34V ′
34 ˆW ∗
46V56V ′
56W ∗
35).
Now the right hand bracket is
V34V ′
34 ˆW ∗
46V56V ′
56W ∗
35
= V34 ˆW ∗
46V56V ′
56W ∗
35V ′
34
= V ∗
36 ˆW ∗
46V36V56V ′
56W ∗
35V ′
34
= V ∗
36 ˆW ∗
46V36V56W ∗
35( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)V ′
56V ′
34
= V ∗
36 ˆW ∗
46W ∗
35V56( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)V ′
56V ′
34
= V ∗
36W ∗
35 ˆW ∗
46( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6)Z56V ′
34
= V ∗
36W ∗
35( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6) ˆW ∗
46V34Z56V ′
34
= V ∗
36W ∗
35( ˆJ3⊗ ˆJ6)V36( ˆJ3⊗ ˆJ6) ˆW ∗
46Z56Z34.
Combining, we see that the left most 3 terms will pass through ˆW24 and cancel
with the left hand inverses. Hence we obtain
W3456Z ∗
34 ˆW24Z34W ∗
3456
= Z ∗
34Z ∗
56 ˆW46 ˆW24 ˆW ∗
46Z56Z34
= Z ∗
34Z ∗
56 ˆW24 ˆW26Z56Z34
64
as desired.
Note that W is actually a composition of 6 dilogarithm functions. We can
simplify the expression to just 4 gb’s by applying the pentagon equation.
Proposition 7.18. We can rewrite W as
W =W13V ′′
32 ˆW24V ∗
32, (7.49)
where
V ′′ := ( J⊗J)V (J⊗J)
= e
i
2πb 2 log ˆA∗⊗log ˆA−1
g∗
b ( ˆB∗⊗ ˆB)
= e
i
2πb 2 log ˆA∗⊗log ˆA−1
∫
R+i0
ˆBib−1τ
∗ ⊗ ˆBib−1τeπiτ 2
Gb(−iτ )dτ.
Proof.
W = W13Z ∗
34 ˆW24Z34
= W13V ∗′
34V ∗
34 ˆW24V34V ′
34
= W13V ∗′
34 ˆW24V ∗
32V ′
34
= W13V ∗′
34 ˆW24V ′
34V ∗
32
= W13(J2⊗J3⊗ ˆJ4)V ∗
34 ˆW ∗
24V34(J2⊗J3⊗ ˆJ4)V ∗
32
= W13(J2⊗J3)V32(J2⊗J3) ˆW24V ∗
32.
The formula for V ′′ follows from the action of AdJ given in Proposition 5.17 on ˆH
and Proposition 6.10 on H.
Since W is a unitary operator on H⊗ ˆH⊗H⊗ ˆH, for completeness let us describe
its action.
Proposition 7.19. The action of W onHrep⊗H rep is given by
W =e
i
2πb 2 log A−1⊗log ˆAgb(B⊗q ˆB ˆA−1),
W :F⊗G↦→
∫
R+i0
F (s1 +τ,t 1)G(s2−s1−τ,t 2−s1) e2πiτ (s2−s1−τ )Gb( Q
2 +is2−it2)
Gb( Q
2 +is2−it2−iτ )Gb(Q +iτ )
dτ,
(7.50)
W ∗ :F⊗G↦→
∫
R+i0
F (s1 +τ,t 1)G(s2 +s1,t 2 +s1 +τ )e2πis2τGb( Q
2 +is2−it2)Gb(−iτ )
Gb( Q
2 +is2−it2−iτ )
dτ.
(7.51)
65
The action of ˆW on ˆH⊗ ˆHrep is given by
ˆW =e
i
2πb 2 log ˆA⊗log Ag∗
b ( ˆB⊗q−1BA−1),
ˆW24 :F⊗G ↦→
∫
R+i0
F (s1 +τ,t 1)G(s2−s1−τ,t 2−s1)e2πiτ (τ +s1−s2)
Gb( Q
2−is2 +it2 +iτ )Gb(−iτ )
Gb( Q
2−is2 +it2)
dτ, (7.52)
ˆW ∗
24 :F⊗G↦→
∫
R+i0
F (s1 +τ,t 1)G(s2 +s1,t 2 +s1 +τ )e−2πiτ s2Gb( Q
2−is2 +it2 +iτ )
Gb( Q
2−is2 +it2)Gb(Q +iτ )
dτ.
(7.53)
The action of V onHrep⊗ ˆHrep is given by
V :F⊗G↦→
∫
F (s1 +τ,t 1)G(s2 +τ,t 2)e2πis2(s1+τ )
Gb(Q +iτ )dτ, (7.54)
V ∗ :F⊗G↦→
∫
F (s1 +τ,t 1)G(s2 +τ,t 2)e−2πis1(s2+τ )Gb(−iτ )dτ, (7.55)
and the action of V ′′ onHrep⊗ ˆHrep is given by
V ′′ :F⊗G↦→
∫
R+i0
F (s1,t 1−τ )G(s2 +τ,t 2)e2πit1s2eπiτ 2
Gb(−iτ )dτ, (7.56)
V ′′∗ :F⊗G↦→
∫
R+i0
F (s1,t 1−τ )G(s2 +τ,t 2)e2πiτ (s2−t1)e−2πit1s2eπiτ 2
Gb(Q +iτ ) dτ.
(7.57)
Hence the action of W and W∗ are the compositions of the corresponding operators.
Proof. The actions follow directly from the closed form expression (Propos ition
4.19) for W , using Corollary 4.18 for the integral representations for gb, as well as
the action described in Section 6.2.
