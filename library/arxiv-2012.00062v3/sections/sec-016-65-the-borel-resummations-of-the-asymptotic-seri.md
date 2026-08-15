---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-016-65-the-borel-resummations-of-the-asymptotic-seri
section_title: "The Borel resummations of the asymptotic series"
section_number: 6.5
pages: 60-62
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
knot, Conjecture 26 identiﬁes the Borel resummations of the factorially divergent series
Φ(x;τ) with the descendant state-integrals, thus lifting the Borel resummation to holomor-
phic functions on the cut-planeC ′.
Corollary 27. (of Conjecture 26) We have
sI(Φ)(x;τ) =


0 1 1
0 1 0
−1 0 0

W−1(˜x; ˜q−1)∆(τ)B(x;q), (317a)
sII (Φ)(x;τ) =


0 1 0
0 1 1
−1 0 0

W−1(˜x−1; ˜q−1)∆(τ)B(x;q), (317b)
sIII (Φ)(x;τ) =


0 1 0
0 −s(˜x) 1
−1 0 0

W−1(˜x−1; ˜q−1)∆(τ)B(x;q), (317c)
sIV (Φ)(x;τ) =


0 −s(˜x) 1
0 1 0
−1 0 0

W−1(˜x, ˜q−1)∆(τ)B(x;q). (317d)
where the right hand side of (317a)–(317d) are holomorphic functions ofτ∈ C′, as they are
linear combinations of the descendants (243).
2Note that if we compare with the DGG indices computed in [BDP14] we have to modify the last line in
(315) slightly due to diﬀerent conventions for holomorphic blocks
(
W0(x−1;q−1)·W 0(x;q)T)
i+1,j+1 =q
3
2 (i2−j2)x−3(j−i)Indrot
52 (j−i,q −j+i
2 x−1;q), i,j = 0, 1, 2. (314)
The right hand side of (20) should be modiﬁed accordingly. This however does not aﬀect (21).
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 61
|sI(Φ)(x;τ)
PI(x;τ) − 1| |sI(Φ)(x;τ)
s′
I(Φ)(x;τ)− 1| | ˜q(τ)| | ˜x(x,τ )−1|
σ1 1.1× 10−38 1.1× 10−38
1.9× 10−13 0.042σ2 2.2× 10−63 1.7× 10−62
σ3 2.7× 10−48 2.5× 10−48
(a) Region I: τ = 1
18e
πi
12
|sII (Φ)(x;τ)
PII (x;τ) − 1| |sII (Φ)(x;τ)
s′
II (Φ)(x;τ)− 1| | ˜q(τ)| | ˜x(x,τ )|
σ1 2.2× 10−63 1.7× 10−62
1.9× 10−13 0.042σ2 1.1× 10−38 1.1× 10−38
σ3 2.7× 10−48 2.5× 10−48
(b) Region II: τ = 1
18e
11πi
12
Table 2. Numerical tests of holomorphic lifts of Borel sums of asymptotic
series for knot 52. We perform the Borel-Padé resummation onΦ(x;τ) with
180 terms atx = 6/5andτ in regionsI,II , and compute the relative diﬀerence
between them and the right hand side of (317a)–(317b), which we denote by
PR(x;τ). They are within the error margins of Borel-Padé resummation, which
are estimated by redo the resummation with 276 terms, denoted bys′
R(•) in
the tables. The relative errors are much smaller than |˜q±1|,|˜x±1|, possible
sources of additional corrections.
6.6. Numerical veriﬁcation.In this section we explain the numerical veriﬁcation of Con-
jecture 26, which involves a richer resurgent structure than that of the41 knot. We found
ample numerical evidence for the resurgent data (304a)–(304d). These numerical tests are
parallel to those performed for knot41, so we will be sketchy here. Besides, we will mostly
focus onτ in the upper half plane, while the lower half plane is similar.
The ﬁrst test is the analysis of radial asymptotics of the left hand side of (226), which can
be easily done. The second test is to compute the Borel resummationsR(Φ′
σ)(x;τ) and by
comparing with the left hand side extract terms ofMR(˜x, ˜q)σ,σ′ order by order. To expediate
the operation of extraction, instead ofMR(˜x; ˜q) we consider
~MR(˜x; ˜q) =


1 0 0
0 θ(−˜q−1/2˜x; ˜q)2 0
0 0 θ(−˜q1/2˜x; ˜q)2

MR(˜x; ˜q) (318)
whose entries are˜q-series with coeﬃcients inZ[˜x±1] instead of inZ(˜x). Using 180 terms of
Φσ(x;τ) at various values ofx and τ, we ﬁnd entries of~MI,II (x;q) up to O(q2) following
62 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
results
~MI(x;q)1,1 =1− (x−1 +x)q− (x−1− 2 +x)q2 +O(q3),
~MI(x;q)1,2 =−x−1−x + (x−2 + 2 +x2)q + (x−2− 2x−1 + 1− 2x +x2)q2 +O(q3),
~MI(x;q)1,3 =− 1 + (x−1− 1 +x)q + (x−1− 2 +x)q2 +O(q3),
~MI(x;q)2,1 =x2− (x3 +x4)q− (x3−x5)q2 +O(q3),
~MI(x;q)2,2 =−x−x2 + (x2 + 2x3 +x4)q + (x2 +x3−x4− 2x5)q2 +O(q3),
~MI(x;q)2,3 =−x +x2q + (x2−x4)q2 +O(q3),
~MI(x;q)3,1 =x−2− (x−4 +x−3)q + (x−5−x−3)q2 +O(q3),
~MI(x;q)3,2 =−x−2−x−1 + (x−4 + 2x−3 +x−2)q− (2x−5 +x−4−x−3−x−2)q2 +O(q3),
~MI(x;q)3,3 =−x−1 +x−2q− (x−4−x−2)q2 +O(q3). (319)
and
~MII (x;q)1,1 =−x−x−1 + (x2 + 2 +x−2)q + (x2− 2x + 1− 2x−1 +x−2)q2 +O(q3),
~MII (x;q)1,2 =1− (x +x−1)q− (x− 2 +x−1)q2 +O(q3),
~MII (x;q)1,3 =− 1 + (x− 1 +x−1)q + (x− 2 +x−1)q2 +O(q3),
~MII (x;q)2,1 =−x− 1 + (1 + 2x−1 +x−2)q + (1 +x−1−x−2− 2x−3)q2 +O(q3),
~MII (x;q)2,2 =1− (x−1 +x−2)q− (x−1−x−3)q2 +O(q3),
~MII (x;q)2,3 =−x +q + (1−x−2)q2 +O(q3),
~MII (x;q)3,1 =− 1−x−1 + (x2 + 2x + 1)q− (2x3 +x2−x− 1)q2 +O(q3),
~MII (x;q)3,2 =1− (x2 +x)q + (x3−x)q2 +O(q3),
~MII (x;q)3,3 =−x−1 +q− (x2− 1)q2 +O(q3). (320)
They are in agreement with (304a),(304b). More decisively, we can compare the numerical
evaluation of both sides of the equations of holomorphic lifts (317a),(317b). We ﬁnd the
relative diﬀerence between the two sides is always within the error margin of Borel-Padé
resummation, and much smaller than ˜q±1, ˜x±1, possible sources of additional corrections.
We illustrate this by one example withx = 6/5 and τ = 1
18e
πi
12, 1
18e
11πi
12 in regions I,II in
Table 2. Finally we can test the resurgent data by checking that in thex↦→ 1 limit the
Stokes matrices (305a), (305b) reduce properly to (95a), (95b). This is a non-trivial test as
W−1(x;q−1) (|q|< 1) in (305a), (305b) itself diverges in the limitx↦→ 1.
