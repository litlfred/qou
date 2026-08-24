---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-012-43-resurgent-structure
section_title: "Resurgent structure"
section_number: 4.3
pages: 32-34
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41,S 3\52 with generic"
---
We collect the trans-series associated to the geometric and conjugate ﬂat connections in a
vector
Φ(k)
52 (x;τ) =


Φ(k,σ1)
52
Φ(k,σ2)
52
Φ(k,σ2)
53

 (x;τ). (4.33)
The singularities of the Borel transform of each component trans-series are located in Λ (k)
j
given in (2.63). In the case of level k = 1, we superimpose the Borel singularities of the
components of Φ(1)
52 (x;τ) and plot them in Fig. 5. At a generic level k≥ 1, the distrubtion
of the Borel plane singularities is the same and their actual locations are reduced by a
factor of 1/k according to (2.63).
As explained in Section 2, Stokes constants of individual Borel plane singularities
can be extracted from global Stokes automorphisms. The entire Borel plane is divided
by Stokes rays of components of Φ (k)
52 (x;τ) into inﬁnitely many cones. We label the four
cones above and below the positive and negative real axes by I,II,III,IV , ordered in
counter-clockwise direction, as illustrated in Fig. 5. We choose to calculate the global
Stokes automorphism S(k)
+ (˜x; ˜q) = S(k)
IV→II (˜x; ˜q) and S(k)
− (˜x; ˜q) = S(k)
II→IV (˜x; ˜q), both in
the anti-clockwise direction, which encode all the Stokes constants.
As in the previous section, in order to derive the Stokes automorphisms, we ﬁrst
calculate the Borel resummation of the trans-series. Following [31] and with numerical
evidence presented shortly after, We claim that the Borel resummation of trans-series can
be written as bilinear products of holomorphic blocks in q and ˜q. Concretely,
sI(Φ)(x;τ) =


0 1 1
0 1 0
−1 0 0

W−1(˜x; ˜q−1)∆(k)(τ)B(x;q), |˜q|< 1, (4.34a)
– 31 –
sII (Φ)(x;τ) =


0 1 0
0 1 1
−1 0 0

W−1(˜x−1; ˜q−1)∆(k)(τ)B(x;q), |˜q|< 1, (4.34b)
sIII (Φ)(x;τ) =


0 1 0
0 −s(˜x) 1
−1 0 0

W−1(˜x−1; ˜q−1)∆(k)(τ)B(x;q), |˜q|> 1, (4.34c)
sIV (Φ)(x;τ) =


0 −s(˜x) 1
0 1 0
−1 0 0

W−1(˜x; ˜q−1)∆(k)(τ)B(x;q), |˜q|> 1. (4.34d)
Here W−1(x,q ) is the Wronskian of holomorphic blocks deﬁned in (3.32), and
B(x;q) =


A0(x;q)
B0(x;q)
C0(x;q)

 (4.35)
∆(k)(τ) is the diagonal matrix deﬁned by
∆(k)(τ) = diag(e−πi
12 + 5πi
6k + 5πi
12k (τ+τ−1), e− 5
12πik+πi
6k + πi
12k (τ+τ−1), e− 5
12πik+πi
6k + πi
12k (τ+τ−1)).
(4.36)
As in the example of knot 41, we use (4.34a) and (4.34b) to derive Stokes automorphism
in the upper half plane, and use (4.34a) and (4.34d) to calculate Stokes constants for
Borel plane singularities in the positive axis, which involves analytic continuation of the
holomorphic blocks with the help of (4.32). Combining these results, we can write down
the global Stokes automorphism S(k)
+ from sectorIV to sectorII in anti-clockwise diretion.
Similar calculations can be done to write down S(k)
− from sector II to sector IV in anti-
clockwise direction.
S(k)
+ (˜x; ˜q) =


0 1 0
0 1 1
−1 0 0

W−1(˜x−1; ˜q−1)W−1(˜x; ˜q)T


0 0−1
1 1 0
0 1 0

, |˜q|< 1 (4.37a)
S(k)
− (˜x; ˜q) =


0 −s(˜x) 1
0 1 0
−1 0 0

W−1(˜x; ˜q)W−1(˜x−1; ˜q−1)T


0 0 −1
−s(˜x) 1 0
1 0 0

, |˜q|< 1.
(4.37b)
we notice that the Stokes automorphisms and therefore the Stokes constants do not depend
on the level k.
At level k = 1, the numerical evidences for the Borel plane singularities as well the
Borel resummation formulas (4.34a),(4.34b),(4.34c),(4.34d) were provided in detail in [31].
We verify these results numerically at level k = 2. We choose x = (−1)n 6
5 (n = 0, 1)
corresponding to u = 2 log 6/5,n = 0, 1 with power series truncated to N = 200 terms.
The Stokes plane is divided into four regions similar to Fig. 5. For example, the positions
of poles for the Pad´ e approximant Φ(k=2)
52 (x,τ ) at x = 6
5 are shown in Fig. 6. Finally we
– 32 –
present the numerical results in Tabs. 6 and 7 respectively. As we can see, the relative errors
between two sides of (4.34a),(4.34b),(4.34c),(4.34d) (the ﬁrst column) are always within
the precision of the Borel resummation (the second column), and in regionsI,II are always
far smaller than a potential ˜q (or 1/˜q in the lower half plane) or a ˜x±1 correction (the third
and the fourth columns). In region III , the relative error between two sides of (4.34b) is
relatively high, due to discrete singular points that break oﬀ from the branch cut of the
Borel transform of the truncated series Φ (k=2,σ2)
52 (x;τ) and stray into region III , as seen in
Fig. 6b. The relative error is still much smaller than a ˜x±1 correction, although it does not
preclude a potential ˜q−1 correction. The latter, however, is not possible. Fig. 6b indicates
that Φ(k=2,σ2)
52 (x;τ) in regions II and III must be related by a Stokes automorphism that
accounts for the three Borel plane singularities in the negative real axis. Indeed from
(4.34b),(4.34c) we ﬁnd that
sIII (Φ)(x;τ) = SII→III (˜x)sII (Φ)(x;τ), SII→III (˜x) =


1 0 0
−1−s(˜x) 1 0
0 0 1

 (4.38)
The (2, 1) entry of SII→III (˜x)
SII→III (˜x)2,1 =−˜x− 2− ˜x−1 (4.39)
should encode the Stokes constants of these three Borel plane singularities. Any cor-
rection to the right hand side of (4.34c) should involve a correction of the coeﬃcients of
SII→III (˜x)2,1 and thus must be of relative order at least ˜x±1. Likewise, from (4.34a),(4.34d)
we ﬁnd that
sI(Φ)(x;τ) = SIV→I(˜x)sIV (Φ)(x;τ), SIV→I(˜x) =


1 1 +s(˜x) 0
0 1 0
0 0 1

 (4.40)
The (1, 2) entry of SIV→I(˜x)
SIV→I(˜x)1,2 = ˜x + 2 + ˜x−1 (4.41)
accounts for the three singularities of the Borel transform of Φ (k=2,σ1)
52 (x;τ) in the positive
real axis shown in Fig. 6a. Any correction to the right hand side of (4.34d) should involve a
correction of the coeﬃcients of SIV→I(˜x)1,2 and thus must be of relative order ˜x±1, which
is also excluded in Tabs. 6, 7.
