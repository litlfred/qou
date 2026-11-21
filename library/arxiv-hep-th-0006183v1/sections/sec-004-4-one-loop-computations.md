---
doc_id: arxiv-hep-th-0006183v1
doc_title: "Fine-tuning and the Wilson renormalization group"
section_id: sec-004-4-one-loop-computations
section_title: "One-loop computations"
section_number: 4
pages: 5-15
source_pdf: 0006183v1.pdf
source_sha256: 2c9c4d97ce4f71a3
toc_source: inferred
doc_brief: "Fine-tuning and the Wilson renormalization group — We use the Wilson renormalization group (RG) formulation to solve the ﬁne-tuning proce- dure needed in renormalization schemes breaking the gauge"
---
At one-loop and at Λ = Λ0, the ﬁne-tuning equation (6) reduces to
SΠ(0) Π(1)(Λ0) = −ˆ∆(1)
Γ (Λ0) ,
(8)
4
where the local functional Π(1)(Λ0) ≡Π(1)[Φ, γ; Λ0] contains the relevant monomials given
in (5) (as discussed in the previous section its irrelevant contributions vanish as Λ0 →∞
and therefore can be omitted in the calculations performed in this section). This functional
can be split into two contributions 2
Π(Λ0) = Πinv(Λ0) + ˜Π(Λ0) ,
(9)
where Πinv satisﬁes the ST identity i.e. SΠinv Πinv = 0. The explicit form of Πinv is
Πinv(Λ0) =
Z
d4x

−1
4 z1 Fµν · F µν + z2 z3
 1
g z3
wµ · Dµc −1
2 v · c ∧c
 
,
with Fµν = ∂µAν −∂νAµ + g z3 Aµ ∧Aν and the covariant derivative given by Dµc =
∂µc + g z3 Aµ ∧c. The remaining monomials contribute to ˜Π which can be written as
˜Π(Λ0) ≡
Z
d4x
n
σ1 Λ2
0
1
2A2
µ + σ2
1
2(∂µAµ)2 + σ3 wµ · c ∧Aµ + σ4
1
2v · c ∧c
+ σ5
g2
4 (Aµ ∧Aν)2 + σ6
g2
4 (Aµ · Aν)2o
.
(10)
The functional Π(Λ0) is equal to the UV action SΛ0[Φ, γ] with the UV wave function
constants and UV couplings given by
zi = zi(g, µ/Λ0) ,
σi = σi(g, µ/Λ0) .
Notice that the ﬁne-tuning equation (8) allows to compute the couplings in Π(1)(Λ0) since
ˆ∆(1)
Γ (Λ0) depends only on Π(0) = SBRS. As a matter of fact only the couplings σi are
tuned with this procedure. On the contrary the couplings zi are not involved in the ﬁne-
tuning. They are free parameters which can be ﬁxed setting the ﬁeld normalization and
the gauge coupling at the subtraction point µ equal to their physical values at Λ = 0,
i.e. zi(Λ = 0) = 1.
In the standard language this corresponds to the renormalization
prescriptions. In the following subsections we will determine the expression for the couplings
σi in term of the Yang-Mills coupling g and the cutoﬀfunction. The values of these couplings
corresponding to three diﬀerent choices of the cutoﬀfunction are collected in the tables 1-3
given below.
Using the parameterization given in (9) and (10), the l.h.s. of (8) becomes
SΠ(0) Π(1)(Λ0) =
Z
d4x
n
δ1Λ2
0 Aµ · ∂µc + δ2 Aµ · ∂2∂µc + δ3 Aµ · (∂2Aµ) ∧c
+ δ4 Aµ · (∂µ∂νAν) ∧c + 1
2δ5 (∂µwµ) · c ∧c + 1
2δ6 (wµ ∧Aµ) · (c ∧c)
+ δ7 ((∂µAµ) · Aν)(Aν · c) + δ8 ((∂µAµ) · c)(Aν · Aν) + δ9 ((∂νAµ) · Aν)(Aµ · c)
+ δ10 ((∂νAµ) · Aµ)(Aν · c) + δ11 ((∂νAµ) · c)(Aµ · Aν)
o
where
δ1 = −i
gσ1 ,
δ2 = i
gσ2 ,
δ3 = −iσ3 ,
δ4 = −i(σ2 −σ3) ,
δ5 = 1
g δ6 = i
g(σ3 −σ4) ,
δ7 = δ9 = δ11 = ig(σ3 + σ6 −σ5) ,
δ8 = 1
2δ10 = ig(σ5 −σ3) .
(11)
2For the sake of simplicity the loop order index will be sometimes understood.
The system of equations obtained by imposing δi to be equal to the coeﬃcient of the
corresponding monomials in −ˆ∆Γ overdetermines the couplings σi (eleven equations and ﬁve
unknown couplings) therefore it can be solved if one has only ﬁve independent equations.
The necessary six relations among the parameters δi are automatically obtained from the
anticommutativity of the BRS operator SΠ, as can be seen in (11). Though it is not evident
that the same relations hold for the coeﬃcients of ˆ∆Γ, the direct calculation given in the
following subsections will shown that this is true.
At one-loop oder ˆ∆Γ can be evaluated taking the integrand in (7) at tree level and
noticing that Π(0) = SBRS and then the sum over ΦJ is restricted to the (A, c)−ﬁelds. At
Λ = Λ0, ˆ∆(1)
Γ
is given by
ˆ∆(1)
Γ (Λ0) =
Z
p,q
K0Λ0(p)(−)δi
DΛ0∞(q) ¯Γ(0)[−q, −p; Λ0]

ji
δ2
δΦj(q)δγi(p)

SBRS −1
g
Z
x
uµ∂µc

,
(12)
where the functional ¯Γ(0) originating from the inversion of
δ2Γ[Φ,γ;Λ]
δΦ(−q)δΦ(−p) is recursively deﬁned
as
¯Γ(0)
IJ [−q, −p; Φ, γ; Λ0] = (−)δJ

Sint
BRS(−q, −p)

IJ
−
Z
q′

DΛ0∞(q′) ¯Γ(0)[−q′, −p; Φ, γ; Λ0]

LJ

Sint
BRS(−q, q′)

IL ,
(13)
with Sint
BRS the interaction part of SBRS and

Sint
BRS(p, q)

IJ =
δ
δΦJ(q)
δ
δΦI(p)Sint
BRS .
For instance when ΦI and ΦJ are vector ﬁelds one has

Sint
BRS(p, q)

Abν Aaµ
= −igǫabc tµνρ(p, q) Ac
ρ(−p −q) −g2 tabcd
µνρσ
Z
k
Ac
ρ(k) Ad
σ(−p −q −k) , (14)
where
tµνρ(p, q) = (p −q)ρgµν + (2q + p)µgνρ −(2p + q)νgµρ
and
ta1···a4
µ1···µ4 = (ǫa1a2cǫca3a4 −ǫa1a4cǫca2a3) gµ1µ3gµ2µ4 + (ǫa1a3cǫca2a4 −ǫa1a4cǫca3a2) gµ1µ2gµ3µ4
+ (ǫa1a3cǫca4a2 −ǫa1a2cǫca3a4) gµ1µ4gµ2µ3
are the three and four-vector elementary vertices, respectively.
In the following subsections we compute the coeﬃcients of the various ﬁeld monomials
in ˆ∆Γ.
4.1
Ac-vertex
There are three contributions 3 to the Aµ·c−vertex which are obtained inserting in (12) the
ﬁrst term of (13) and setting (γi = wν , Φj = Aν), (γi = wν , Φj = c) and (γi = v , Φj = c).
Figure 1: Graphical contribution to the A-c-vertex of ˆ∆Γ. The curly and dashed line denotes the
gluon and ghost ﬁeld respectively; the double lines represent the BRS source associated to the
ﬁeld depicted by the top line. All momenta are incoming.
The corresponding graphs are given in Fig 1.
Using the vertices of SBRS one obtains
Z
p
Aµ(p) · c(−p) ˆ∆(Ac)
Γ µ (p; Λ0)
with
ˆ∆(Ac)
Γ µ (p; Λ0) = −2ig
Z
q

tνµν(q, p) −2qµ
KΛ0∞(q)
q2
K0Λ0(q + p) .
The presence of the two cutoﬀfunctions having almost non-intersecting supports (i.e.
q2 ≳Λ2
0, (q + p)2 ≲Λ2
0) ensures that this vertex is quadratically divergent in the Λ0 →∞
limit but without logarithmic divergences. In this limit one gets
ˆ∆(Ac)
Γ µ (p; Λ0) = i pµ [ˆδ1 Λ2
0 −ˆδ2 p2 + O(p4/Λ2
0)]
with
ˆδ1 = 2g
Λ2
0
Z
q
(1 −K)(3K + 2K′q2)
q2
,
(15)
and
ˆδ2 = −2g
Z
q
(1 −K)(18K′ + 21K′′q2 + 4K′′′q4)
6q2
,
(16)
where K ≡K0Λ0(q) and the ′ denotes the derivative with respect to q2 and we have used
the identity KΛ0∞(q) = 1−K0Λ0(q). The coeﬃcients ˆδ1 and ˆδ2 are ﬁnite and cutoﬀfunction
dependent. Recalling that K0Λ0(0) = 1 and that K0Λ0(q) →0 rapidly enough for q2 →∞,
(15) and (16) can be rewritten as
ˆδ1 = 2g
Λ2
0
Z
q
(1 −2K)K
q2
(17)
and
ˆδ2 = g
5r
6 −3
Z
q
K′2
,
(18)
3This computation can be found in [7] and is repeated here for completeness.
where r = i/(16π2) (the factor i comes from the q-integration). The ﬁne-tuning equation
(8) for the Ac-vertex becomes
δ1 = −ˆδ1 ,
δ2 = −ˆδ2 .
Then from (11) one ﬁnds that σ1 and σ2 are given by
σ(1)
1
= −2ig2
Λ2
0
Z
q
(1 −2K)K
q2
,
(19)
σ(1)
2
= ig2 5r
6 −3
Z
q
K′2
(20)
and their values depend, as shown in table 1, on the cutoﬀfunction.
K0Λ0(p)
e−p2/Λ2
0
Λ4
0
(p2+Λ2
0)2
Λ2n
0
p2n+Λ2n
0
σ1
0
- 2ig2r
3
2πig2r(n−2)
n2sin(π/n)
σ2
ig2r
12
7ig2r
30
ig2r(5−3n)
6
Table 1: One-loop values of the couplings σ1 and σ2 for three diﬀerent cutoﬀfunctions (r =
i
16π2
and n ≥1).
4.2
AAc-vertex
In order to ﬁnd the AAc-vertex one has to insert in (12) the functional ¯Γ(0) obtained from
the ﬁrst iteration in (13), i.e.
−(−)δJ
Z
q′

DΛ0∞(q′) Sint
BRS(−q′, −p)

LJ

Sint
BRS(−q, q′)

IL .
(21)
One ﬁnds one contribution for (γi = wν , Φj = Aν), two for (γi = wν , Φj = c) and one for
(γi = v , Φj = c) (plus the terms obtained from the permutation of the two vectors). The
corresponding graphs are given in Fig 2. Using the vertices of SBRS one obtains
1
2
Z
p1p2
Aµ1(p1) · Aµ2(p2) ∧c(−p1 −p2) ˆ∆(AAc)
Γ µ1µ2(p1, p2; Λ0)
with
ˆ∆(AAc)
Γ µ1µ2(p1, p2; Λ0)
Figure 2: Graphical contribution to the A-A-c-vertex of ˆ∆Γ.
= −g2
2
Z
q

tρµ1ν(q, p1) tνµ2ρ(q + p1, p2)KΛ0∞(q)KΛ0∞(q + p1)
q2(q + p1)2
K0Λ0(q + p1 + p2)
−(q + p1 + p2)νtνµ1µ2(q, p1)KΛ0∞(q)KΛ0∞(q + p1 + p2)
q2(q + p1 + p2)2
K0Λ0(q + p1)
−qµ1(q + p1)µ2
KΛ0∞(q)KΛ0∞(q + p1)
q2(q + p1)2
(K0Λ0(q −p2) + K0Λ0(q + p1 + p2))
−(1 ↔2)

.
In the Λ0 →∞limit one gets
ˆ∆(AAc)
Γ µ1µ2(p1, p2; Λ0) = gµ1µ2(p2
1 −p2
2) ˆδ3 + (p1µ1 p1µ2 −p2µ1 p2µ2)ˆδ4 + O(P 4/Λ2
0) ,
where P is a combination of the external momenta p1 and p2,
ˆδ3 = −g2
Z
q
(1 −K)
6q4
[13K2−2q2(11K′+8K′2q2 +K′′q2)+K(−13+15K′q2 −8K′′q4)] (22)
and
ˆδ4 = g2
Z
q
(1 −K)
6q4
[13K2+2q2(−8K′+10K′2q2−K′′q2)+K(−13+45K′q2+10K′′q4)] . (23)
The ﬁne-tuning equation (8) for the AAc-vertex allows to ﬁnd the value of σ3 in term of g
and the cutoﬀfunction. From δ3 = ˆδ3 and (11) one ﬁnds
σ(1)
3
= −ig2 37r
36 −
Z
q
13K(1 −K)2 + 10q4K′2
6q4

(24)
K0Λ0(p)
e−p2/Λ2
0
Λ4
0
(p2+Λ2
0)2
Λ2n
0
p2n+Λ2n
0
σ3
-
ig2r(39 ln 4
3 +11)
18
49igr
360
- igr(10n2−37n+39)
36n
Table 2: One-loop values of the coupling σ3 for three diﬀerent cutoﬀfunctions (r =
i
16π2 and
n ≥1).
and its value for diﬀerent choices of the cutoﬀfunction is given in table 2.
In order to check the consistency of our computation the ﬁne-tuning equation δ4 ≡
−i(σ2 −σ3) = ˆδ4 must be automatically satisﬁed with the couplings σ2 and σ3 previously
determined and given in (20) and (24), respectively. Alternatively one has to prove the
consistency condition ˆδ3 + ˆδ4 = −gˆδ2. From (22) and (23) one ﬁnds
−1
g(ˆδ4 + ˆδ3) = −g
Z
q
1 −K
q2
(K′ + 5KK′ + 6K′2q2 + 3KK′′q2)
which becomes equal to (18) after integration by parts.
4.3
AAAc-vertex
The AAAc-vertex receives contribution from (21) and the term originating from the second
iteration of (13) i.e.
(−)δJ
Z
q′q′′

DΛ0∞(q′′) Sint
BRS(−q′′, −p)

HJ

DΛ0∞(q′) Sint
BRS(−q′, q′′)

LH

Sint
BRS(−q, q′)

IL .
(25)
The corresponding graphs are shown in ﬁgs. 5-7 and the various contributions are computed
in Appendix A. After performing the trace over the gauge indices this vertex can be written
as
1
3!
Z
p1p2p3

Aµ1(p1) · Aµ2(p2)

Aµ3(p3) · c(−p1 −p2 −p3)

ˆ∆(AAAc)
Γ µ1µ2µ3(p1, p2, p3; Λ0) .
In the Λ0 →∞limit one obtains
ˆ∆(AAAc)
Γ µ1µ2µ3(p1, p2, p3; Λ0) = −3i[ˆδ7(p1µ1gµ2µ3 + p2µ2gµ1µ3) + 2ˆδ8p3µ3gµ1µ2
+ˆδ9(p1µ2gµ1µ3 + p2µ1gµ2µ3) + ˆδ10(p1µ3 + p2µ3)gµ1µ2 + ˆδ11(p3µ2gµ1µ3 + p3µ1gµ2µ3)]
+ O(P 4/Λ2
0) ,
(26)
where
ˆδ7 = ˆδ9 = ˆδ11 = −g3
Z
q
(1 −K)
6q4
[31K3+K2(124K′q2−47)+K(16−111K′q2)+14K′q2] (27)
and
ˆδ8 = 1
2
ˆδ10 = −g3
Z
q
(1 −K)
6q4
[23K3 + K2(56K′q2 −25) + K(2 −48K′q2) + K′q2] .
(28)
By using the ﬁne-tuning equation (8), together with the results (11) and (24), the couplings
σ5 and σ6 are given by
σ(1)
5
= −ig23r
2 +
Z
q
K(1 −K)(23K2 −12K −11) −10K′2q4
6q4

,
σ(1)
6
= −ig2 2r
3 +
Z
q
(1 −K)(9K3 + 12K2 + 3K)
q4

and their values for diﬀerent cutoﬀfunctions are given in table 3.
K0Λ0(p)
e−p2/Λ2
0
Λ4
0
(p2+Λ2
0)2
Λ2n
0
p2n+Λ2n
0
σ5
- ig2r(13+94 ln 2−70 ln 3)
12
47ig2r
630
ig2(5n2−27n+28)
18n
σ6
- ig2r(2−63 ln 3+99 ln 2)
3
- 58ig2r
105
- 2ig2
3
Table 3: One-loop values of the couplings σ5 and σ6 for three diﬀerent cutoﬀfunctions (r =
i
16π2
and n ≥1).
4.4
wcc-vertex
The wcc-vertex is obtained inserting (21) in (12) and is given by the three graphs depicted
in Fig. 3. Using the vertices of SBRS one gets
1
2
Z
p1p2
wµ(−p1 −p2) · c(p1) ∧c(p2) ˆ∆(wcc)
Γ µ (p1, p2; Λ0)
with
ˆ∆(wcc)
Γ µ (p1, p2; Λ0)
= g
Z
q

(q −p1 −p2)µ
KΛ0∞(q)KΛ0∞(q −p1 −p2)K0Λ0(q −p2)
q2(q −p1 −p2)2
−qµ
KΛ0∞(q)KΛ0∞(q + p2)[K0Λ0(q + p1 + p2) + K0Λ0(q −p1)]
q2(q + p2)2
+(1 ↔2)

.
Figure 3: Graphical contribution to the w-c-c-vertex of ˆ∆Γ.
In the Λ0 →∞limit one obtains
ˆ∆(wcc)
Γ µ (p1, p2; Λ0) = i(p1 + p2)µ [ˆδ5 + O(P 2/Λ2
0)] ,
where
ˆδ5 = g
Z
q
(−1 + 4K −3K2)K′
q2
= 0
as integration by parts can show. Thus from (11) the one-loop value of the coupling σ4 is
given by (24).
4.5
wccA-vertex
The ﬁne-tuning equation for this vertex is directly obtained form the the relation between
δ5 and δ6 in (11), thus this vertex must vanish.
The graphs which contribute to this vertex are obtained inserting (25) in (12) and are
given in ﬁg. 4. All the terms can be collected in the following monomial
Z
p1p2p3
(Aµ(p3) · c(p2) )(wν(−p1 −p2 −p3) · c(p1) ) ˆ∆(Accw)
Γ µν
(p3, p2, p1, p3; Λ0) .
The complete expression of ˆ∆(Accw)
Γ µν
is not needed since
ˆ∆(Accw)
Γ µν
(p3, p2, p1, p3; Λ0) = gµνˆδ6 + O(P 2/Λ2
0)
and therefore in the Λ0 →∞limit one can set to zero all the external momenta. In this
limit one obtains
gµνˆδ6 = g2
Z
q
(1 −K)3K
q6
[−q2gµν + qµqν + qρtρνµ(q, 0)] ,
which vanishes.
Figure 4: Graphical contribution to the w-c-c-A-vertex of ˆ∆Γ.
