---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-009-53-the-52-knot
section_title: "The 52 knot"
section_number: 5.3
pages: 16-20
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
series ϕσj(τ) (j = 1, 2, 3) of the 5 2 knot is shown in Fig. 3. Points in each vertical line are
2πi are apart, while the six points ιij surrounding the origin are given by
ιij = V (σi)
2π − V (σj)
2π , 1≤i⁄=j≤ 3, (81)
whereV (σi) are given in (21). The structure of Stokes rays is shown in Fig. 4. There is also
an inﬁnite dense set of rays accumulating towards the imaginary axis.
s21
s31
ϕσ1(τ )
s12
s32
ϕσ2(τ )
s23s13
ϕσ3(τ )
Figure 3. The singularities in the Borel plane for the series ϕσj(τ) of the 5 2
knot for j = 1, 2, 3.
The q-series H±
k,0 for (k = 0, 1, 2), which are analogues of G0
0,G 1
0 of the 4 1 knot, have
similarly interesting radial asymptotics. We use small letters for the corresponding functions,
i.e.
hk(τ) =
{
H +
k,0(e2πiτ), ℑ(τ)> 0
H−
k,0(e−2πiτ), ℑ(τ)< 0, k = 0, 1, 2. (82)
Then the exact expression of the radial asymptotics reads
e3πi/4


τ−1h0(τ)
h1(τ)
τh 2(τ)

 =MR(˜q)sR(Φ)(τ), (83)
where the index R labels a sector in the τ-plane. The entries of the matrix MR(˜q) are power
series in ˜q in the upper half plane, and power series in 1 /˜q in the lower half-plane.
With more than 200 terms of Φ(τ), we are able to compute ﬁrst few terms in MR(˜q). For
instance, in region I+ we are able to compute ﬁrst six terms in each entry of MI+(˜q). We
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 17
I+
II +
IV +
III +
I−
II −
IV −
III −
s21s12
s23
s31
s13
s32
Figure 4. Stokes rays in the τ-plane for Φσj(τ) of the 5 2 knot for j = 1, 2, 3.
Note that the points s23,s 31 happen to have the same real part, and so do
s13,s 32. The dots are not shown in scale for aesthetic purpose.
display some of the results here
MI+(q) =


−1−q2 2 + 3q2 1 +q + 3q2
−1 + 3q + 3q2 1− 6q− 3q2 −q
− 5
6 + 5q− 53
6q2 − 4
3− 4q + 77
2q2 − 1
6 + 29
6q + 55
2q2

 +O(q3). (84)
Following Conjecture 1, we can express it in terms of solutions to the linear q-diﬀerence
equation (23)
MI+(q) =W−1(q)T


0 0 1
−1 3 0
0 −1 0

, (85)
18 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
where the Wronskian is deﬁned in (25). Note that this expression is exact. By inverting the
matrix MI+(q), we can express the Borel resummation of Φ σj for j = 1, 2, 3 in the sector I+
in terms of the descendants of the state integal introduced in Equation (39). Let us again
introduce the “reduced” descendant
~Iλ,µ(τ) =τH +
2,λ(q)H−
0,µ(˜q)− 2H +
1,λ(q)H−
1,µ(˜q) +τ−1H +
0,λ(q)H−
2,µ(˜q), (86)
which diﬀers from the descendant (111) in a manifestly holomorphic factor. We ﬁnd in region
I+
sI+(Φ)(τ) = 1
2e3πi/4


−1 −1 0
0 −1 0
0 0 1




~I0,−1
~I0,0
~I0,1

 (τ). (87)
In other regions, the results for MR(q) are as follows:
• In the upper half-plane
MII +(q) =W−1(q)T


0 −3 1
−1 3 0
0 −1 0

, (88)
MIII +(q) =


1 0 0
0 −1 0
0 0 1

W−1(q)T


−3 0 1
3 −1 0
−1 0 0

, (89)
MIV +(q) =


1 0 0
0 −1 0
0 0 1

W−1(q)T


0 0 1
3 −1 0
−1 0 0

, |q|< 1. (90)
• In the lower half-plane:
MI−(q) =


1 0 0
0 −1 0
0 0 1

W−1(q)T


0 0 1
−1 −1 0
0 −1 0

, (91)
MII−(q) =


1 0 0
0 −1 0
0 0 1

W−1(q)T


0 0 1
−1 −1 −3
0 −1 0

, (92)
MIII−(q) =W−1(q)T


0 0 1
−1 −1 −3
−1 0 0

, (93)
MIV−(q) =W−1(q)T


0 0 1
−1 −1 0
−1 0 0

, |q|> 1. (94)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 19
From these values one can deduce the Stokes automorphism, in the anticlockwise direction
sIII +(Φ) = SII +→III +(˜q)sII +(Φ), s II−(Φ) = SIII−→II−(˜q−1)sIII−(Φ),
sII +(Φ) = SI+→II +sI+(Φ), s I−(Φ) = SII−→I−sII−(Φ),
sIV +(Φ) = SIII +→IV +sIII +(Φ), s III−(Φ) = SIV−→III−sIV−(Φ),
sI+(Φ) = SI−→I+sI−(Φ), s IV−(Φ) = SIV +→IV−sIV +(Φ), (95)
where
SII +→III +(q) =1
2


0 −1 0
0 −1 −1
1 −3 0

·W−1(q−1)·


0 0 1
0 −2 0
1 0 0

·W−1(q)·


0 −3 1
−1 3 0
0 −1 0

,
(96)
S−1
III−→II−(q) =1
2


0 −1 0
−3 3 −1
1 0 0

·W−1(q)·


0 0 1
0 −2 0
1 0 0

·W−1(q−1)T·


0 0 1
−1 −1 −3
0 −1 0

,
(97)
and SI−→I+,SI+→II +,SIII +→IV +,SIV +→IV−,SIV−→III−,SII−→I− are given in (100a),(100b).
The matrices S±(q) are simply
S+(q) =SIII +→IV +SII +→III +(q)SI+→II +SI−→I+, (98)
S−(q) =SII−→I−SIII−→II−(q)SIV−→III−SIV +→IV−, (99)
and we obtain (29a),(29b).
In the q↦→ 0 limit, the Stokes matrices factorize
S+(0) =Sσ3,σ1Sσ3,σ2Sσ1,σ2 =


1 0 0
0 1 0
−3 0 1




1 0 0
0 1 0
0 3 1




1 4 0
0 1 0
0 0 1

, (100a)
S−(0) =Sσ1,σ3Sσ2,σ3Sσ2,σ1 =


1 0 3
0 1 0
0 0 1




1 0 0
0 1 −3
0 0 1




1 0 0
−4 1 0
0 0 1

. (100b)
The non-vanishing oﬀ-diagonal entry of Sσi,σj is the Stokes constant associated to the Borel
singularityιi,j. Assembling these Stokes constants in a matrix we obtain


0 4 3
−4 0 −3
−3 3 0

 (101)
which is what was found numerically in [GZc, Sec.3.3]. Note that the Stokes matrices S±(q)
can also be factorized according to (67) in order to extract all the other Stokes constants.
This will be studied in detail in [GGMn20a].
We note that
S+
σ1σ1(q) = 2H +
1,0(q)H−
1,0(q) = 1− 12q + 3q2 + 74q3 + 90q4 +O(q5) = Indrot
52 (q), (102)
in agreement with Conjecture 2.
20 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
