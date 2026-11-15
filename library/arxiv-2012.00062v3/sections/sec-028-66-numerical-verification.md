---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-028-66-numerical-verification
section_title: "Numerical verification"
section_number: 6.6
pages: 61-62
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
jecture 26, which involves a richer resurgent structure than that of the 41 knot. We found
ample numerical evidence for the resurgent data (304a)–(304d). These numerical tests are
parallel to those performed for knot 41, so we will be sketchy here. Besides, we will mostly
focus on τ in the upper half plane, while the lower half plane is similar.
The ﬁrst test is the analysis of radial asymptotics of the left hand side of (226), which can
be easily done. The second test is to compute the Borel resummation sR(Φ′
σ)(x; τ) and by
comparing with the left hand side extract terms of MR(˜x, ˜q)σ,σ′ order by order. To expediate
the operation of extraction, instead of MR(˜x; ˜q) we consider
f
MR(˜x; ˜q) =


1
0
0
0
θ(−˜q−1/2˜x; ˜q)2
0
0
0
θ(−˜q1/2˜x; ˜q)2

MR(˜x; ˜q)
(318)
whose entries are ˜q-series with coeﬃcients in Z[˜x±1] instead of in Z(˜x). Using 180 terms of
Φσ(x; τ) at various values of x and τ, we ﬁnd entries of f
MI,II(x; q) up to O(q2) following
62
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARIÑO
results
f
MI(x; q)1,1 =1 −(x−1 + x)q −(x−1 −2 + x)q2 + O(q3) ,
f
MI(x; q)1,2 = −x−1 −x + (x−2 + 2 + x2)q + (x−2 −2x−1 + 1 −2x + x2)q2 + O(q3) ,
f
MI(x; q)1,3 = −1 + (x−1 −1 + x)q + (x−1 −2 + x)q2 + O(q3) ,
f
MI(x; q)2,1 =x2 −(x3 + x4)q −(x3 −x5)q2 + O(q3) ,
f
MI(x; q)2,2 = −x −x2 + (x2 + 2x3 + x4)q + (x2 + x3 −x4 −2x5)q2 + O(q3) ,
f
MI(x; q)2,3 = −x + x2q + (x2 −x4)q2 + O(q3) ,
f
MI(x; q)3,1 =x−2 −(x−4 + x−3)q + (x−5 −x−3)q2 + O(q3) ,
f
MI(x; q)3,2 = −x−2 −x−1 + (x−4 + 2x−3 + x−2)q −(2x−5 + x−4 −x−3 −x−2)q2 + O(q3) ,
f
MI(x; q)3,3 = −x−1 + x−2q −(x−4 −x−2)q2 + O(q3) .
(319)
and
f
MII(x; q)1,1 = −x −x−1 + (x2 + 2 + x−2)q + (x2 −2x + 1 −2x−1 + x−2)q2 + O(q3) ,
f
MII(x; q)1,2 =1 −(x + x−1)q −(x −2 + x−1)q2 + O(q3) ,
f
MII(x; q)1,3 = −1 + (x −1 + x−1)q + (x −2 + x−1)q2 + O(q3) ,
f
MII(x; q)2,1 = −x −1 + (1 + 2x−1 + x−2)q + (1 + x−1 −x−2 −2x−3)q2 + O(q3) ,
f
MII(x; q)2,2 =1 −(x−1 + x−2)q −(x−1 −x−3)q2 + O(q3) ,
f
MII(x; q)2,3 = −x + q + (1 −x−2)q2 + O(q3) ,
f
MII(x; q)3,1 = −1 −x−1 + (x2 + 2x + 1)q −(2x3 + x2 −x −1)q2 + O(q3) ,
f
MII(x; q)3,2 =1 −(x2 + x)q + (x3 −x)q2 + O(q3) ,
f
MII(x; q)3,3 = −x−1 + q −(x2 −1)q2 + O(q3) .
(320)
They are in agreement with (304a),(304b). More decisively, we can compare the numerical
evaluation of both sides of the equations of holomorphic lifts (317a),(317b). We ﬁnd the
relative diﬀerence between the two sides is always within the error margin of Borel-Padé
resummation, and much smaller than ˜q±1, ˜x±1, possible sources of additional corrections.
We illustrate this by one example with x = 6/5 and τ =
1
18e
πi
12, 1
18e
11πi
12
in regions I, II in
Table 2. Finally we can test the resurgent data by checking that in the x 7→1 limit the
Stokes matrices (305a), (305b) reduce properly to (95a), (95b). This is a non-trivial test as
W−1(x; q−1) (|q| < 1) in (305a), (305b) itself diverges in the limit x 7→1.
