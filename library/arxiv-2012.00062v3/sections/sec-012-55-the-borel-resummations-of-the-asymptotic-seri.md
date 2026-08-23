---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-012-55-the-borel-resummations-of-the-asymptotic-seri
section_title: "The Borel resummations of the asymptotic series"
section_number: 5.5
pages: 39-45
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
plain how Conjecture 19 identiﬁes the Borel resummations of the factorially divergent series
Φ(x;τ) with the descendant state-integrals, thus lifting the Borel resummation to holomor-
phic functions on the cut-planeC ′. This is interesting theoretically, but also practically in
the numerical computation of Borel resummations.
After multiplying the inverse ofMR(˜x, ˜q) from the left on both sides of (15), we can
also express the Borel sumssR(Φ)(x;τ) in each region in terms of holomorphic functions of
τ∈ C\R as follows
Corollary 20. (of Conjecture 19) We have
sI(Φ)(x;τ) =
(
−˜x 1 + ˜x−1
0 1
)
W−1(˜x; ˜q−1)∆(τ)B(x;q), (201a)
sII (Φ)(x;τ) =
(
0 −˜x
1 −˜x− ˜x2
)
W−1(˜x−1; ˜q−1)
(
1 0
0 −1
)
∆(τ)B(x;q), (201b)
sIII (Φ)(x;τ) =
(
0 −˜x
1 1
)
W−1(˜x−1; ˜q−1)
(
1 0
0 −1
)
∆(τ)B(x;q), (201c)
sIV (Φ)(x;τ) =
(
−˜x −˜x
0 1
)
W−1(˜x, ˜q−1)∆(τ)B(x;q). (201d)
1Note that because the form of the state integral in [BDP14] is slightly diﬀerent from that in [AK14],
which we adopt, our convention for holomorphic blocks is also diﬀerent from [BDP14]. As a result, the
entries of (198) equate the DGG indices computed in [BDP14] up to a prefactor
(
W0(x−1;q−1)·W 0(x;q)T)
i+1,j+1 = (−q1/2)j−iIndrot
41 (j−i,q
j+i
2 x;q), i,j = 0, 1. (199)
If we take this into account, Conjecture 4 should be modiﬁed slightly by stating the accompanying matrices
on the left and on the right are inGL(2, Z(x,q 1/2)).
40 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
where the right hand side of (201a)–(201d) are holomorphic functions ofτ∈ C′, as they are
linear combinations of the descendants (129).
The asymptotic series of the41 knot have the symmetry (122) due to the fact that it is
an amphichiral knot. This gives a symmetry of the state-integral.
Proposition 21. (Assuming Conjecture 19) We have:
Z41(u;τ) =e2π(b+b−1)uZ41(−u;τ). (202)
Proof. The second line of (201a) indicates that in regionI
Z41(u;τ) =sI(Φ2)(x;τ). (203)
Recall the structure ofΦ2(x;τ) from (120)
Φ2(x;τ) = exp
(V (x,y 2(x))
2πiτ
) 1√
iδ(x,y 2(x))
√
iδϕ(x,y 2(x);τ). (204)
Here
√
iδϕ2(x;τ) :=
√
iδϕ(x,y 2(x);τ) is an asymptotic series inτ with
√
iδϕ2(x; 0) = 1. The
coeﬃcients of the series
√
iδϕ2(x;τ) are invariant under the transformationx↦→ 1/x (see for
instance (123); this is also true for
√
iδϕ1(x;τ) =
√
iδϕ(x,y 1(x);τ)), and thus
s(
√
iδϕ2)(1/x;τ) =s(
√
iδϕ2)(x;τ). (205)
On the other hand, from deﬁnition (121) ofδ2(x) :=δ(x,y 2(x)), it is clear that
δ2(1/x) =x2δ2(x). (206)
Finally, to study the behavior ofV2(x) :=V (x,y 2(x)) under the transformationx↦→ 1/x, it
is convenient to do the change of variablesy =x−1 + ˜y, so that the Equation (116) satisﬁed
byy becomes
1− (1−x−x−1)˜y + ˜y2 = 0 (207)
which is manifestly invariant under this transformation, and thus˜y(1/x) = ˜y(x). Expressed
in terms of this variable
V2(x) =− Li2(−x−1˜y2)− Li2(−x˜y2)− π
3− 1
2 log2(x˜y−1
2 )
+ log(1 +x˜y−1
2 ) log(−x˜y−1
2 )− log(1 +x˜y2) log(−x˜y2)
− 1
2 log2(−1−x˜y−1
2 ) + 1
2 log2(−x−1− ˜y2) + 2 logx log(−x−1− ˜y2), (208)
and it has the property that
V2(x−1) =V2(x)− 2πix (209)
This can be proven by diﬀerentiating both sides with respect tox, and reducing it to an
identity of rational functions on the curveS. Combining (205),(206),(209), we have
sI(Φ2)(x−1;τ) =x−1˜x−1sI(Φ2)(x;τ) (210)
which implies (202). We comment in the passing that the identity (210) is true for both
s(Φ1,2)(x;τ) for anyτ∈ C whenever the asymptotic series is Borel summable.
Once we have established the identity (202) in regionI, it can be extended toτ∈ C′ by
the holomorphicity of (129). □
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 41
5.6. Stokes matrices for realu. In Section 5.4 we only considered the resurgent structure
for x near 1, or equivalently,u = logx near 0. Whenx is arbitrary, the resurgent structure
of the vectorΦσ(x;τ) could be very diﬀerent. According to the Picard–Lefschetz theory (for
review, see for instance [Wit11]), when a set of asymptotic series originates from a (path)
integral, the Borel sum of each asymptotic series is the evaluation of the integral along a
Lefschetz thimble anchored to a critical point. In thex-plane, there are walls of marginal
stability which start from the roots to the discriminant (119) and which end at inﬁnity.
When we cross such a Stokes line, Lefschetz thimbles jump leading to linear transformations
of the Borel summed asymptotic series. In this section we extend slightly the discussion
of Section 5.4 by considering the resurgent structure ofΦσ(x;τ) for generic positivex (see
[BDP14] for a similar discussion in complex Chern-Simons theory). The positive real axis is
divided by the two real solutions to (119)
x± = 1
2(3±
√
5) (211)
to three intervals
(0,x−), (x−,x +), (x+,∞). (212)
The middle interval is covered by Section 5.4, while the ﬁrst (labeled by<) and third (labeled
by>) intervals are discussed below.
ϕσ1(τ )
ϕσ2(τ )
Figure 8. The singularities in the Borel plane for the seriesϕσj(u;τ) with
j = 1, 2 of knot41 forx = e2πbu in the ﬁrst or the third interval of the positive
axis.
First of all, we notice that the ﬁrst and third intervals are related by the reﬂectionx↦→x−1.
In fact, due to the property (205) of the asymptotic series, the Borel plane singularities for
Φσ(x;τ) and Φσ(x−1;τ) are identical, and we illustrate them uniformly in Figure 8. The
positionsofsingularitiesarestilldescribedby (14). However, thediﬀerenceofaction (V (σ1)−
V (σ2))/(2πi) is now imaginary and it describes the vertical spacing between neighoring
42 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
III
III IV
Figure 9. Four diﬀerent sectors in theτ-plane for Φ(u;τ) of knot 41 with
x = e2πbu in the ﬁrst or the third interval of the positive axis.
singularities. The shortest horizontal spacing islogx. Finally all singularities are repeated
vertically by the spacing2πi. Similar to the discussion in Section 5.4, we label in theτ-plane
by I,II,III,IV the four sectors which separate the 12 singularities close to the real axis
and other singularities along the imaginary axis or away from the real axis, as in Figure 9.
In each of the four sectors, the Borel summed vectors≷
R(Φ)(x;τ) is a linear transformation
of the Borel summed vectorsR(Φ)(x;τ) in the middle interval, as per the Picard-Lefschetz
theory
s≷
R(Φ)(x;τ) =T≷
R (˜x)·sR(Φ)(x;τ). (213)
It is most convenient to compute the transformation matrixT≷
R by comparing the left hand
side with the holomorphic lifts ofsR(Φ)(x;τ) summarized in Corollary 20. By doing so, we
ﬁnd in the ﬁrst interval
T<
I (˜x) =
(
˜x 0
−˜x 1
)
, T <
II (˜x) =
(
0 1
−˜x 1
)
(214)
T<
III (˜x) =
(
˜x 1
−˜x 0
)
, T <
IV (˜x) =
(
˜x 1
0 1
)
, (215)
while in the third interval
T>
I (˜x) =
(
˜x−1 0
−˜x−1 1
)
, T >
II (˜x) =
(
0 1
−˜x−1 1
)
(216)
T>
III (˜x) =
(
˜x−1 1
−˜x−1 0
)
, T >
IV (˜x) =
(
˜x−1 1
0 1
)
. (217)
They are indeed related by
T<
R (˜x) =T>
R (˜x−1). (218)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 43
Once the linear combinations are known, the Stokes matrices can be computed using the
Stokes matrices in the middle interval given in Section 5.4
S≷
R→R′(x;q) =T≷
R′(x)· SR→R′(x;q)·
(
T≷
R (x)
)−1
. (219)
We ﬁnd
S>
I→II (x;q) =
(
0 1
−x−1 1
)
· SI→II (x;q)·
(
x 0
1 1
)
(220)
S>
II→III (x) =
(
1−x−x2 x +x2
−x−x2 1 +x +x2
)
(221)
S>
III→IV (x;q) =
(
x−1 1
−x−1 0
)
· SIII→IV (x;q)·
(
x −x
0 1
)
(222)
S>
IV→I(x) =
(
1 +x−1 +x−2 x−1 +x−2
−x−1−x−2 1−x−1−x−2
)
, (223)
and thanks to (218),
S<
R→R′(x;q) = S>
R→R′(x−1;q). (224)
Note that S>
III→I(x) and S>
II→IV (x) encode all the 12 singularities near the real axis
illustrated in Figure 9, as well as the Stokes constants associated to them. Furthermore, the
Stokes matrices also have the property
S>
IV→III (x−1;q)−1 = S>
I→II (x;q)T, (225)
in accord with Conjecture 5.
5.7. Numerical veriﬁcation.In this section we explain the numerical veriﬁcation of Con-
jecture 19. This involves, on the one hand, a numerical computation of the asymptotics of
the holomorphic blocks and on the other hand, a numerical computation of the Borel re-
summation by the Laplace integral of a Padé approximation. Taking the two computations
into account, we found out numerically, integers appearing at two exponentially small scales,
namely ˜q and ˜x, and guessing these integers eventually led to Conjecture 19.
We found ample numerical evidence for the resurgent data (186a)–(186d). First of all,
due to the symmetryΦ1(x;−τ) =−iΦ2(x;τ), Φ2(x;−τ) = iΦ1(x;τ), the resurgent behavior
of s(Φ)(x;τ) for τ in the lower half-plane can be deduced from that forτ in the upper
half-plane. We only have to numerically test the resurgent data forτ in regionsI,II in the
upper-half plane.
The ﬁrst piece of evidence comes from analysing the radial asymptotics of the left hand
side of (15). Note that the matrix∆(τ) = diag(∆σ(τ)) is always diagonal, and each row of
(15) is
∆σ(τ)Bσ(x;q) =
∑
σ′
MR(˜x, ˜q)σ,σ′sR(Φσ′)(x;τ). (226)
If we takeτ = e iα/k with the argumentα depending on a ray in the regionR and k a
very large integer, the diﬀerence betweenexp
(
V (σ′)
2πiτ
)
associated to diﬀerent critical points is
greatly magniﬁed, and the right hand side of (226) is dominated by a single series. Further-
more, whenτ is in the upper (lower) half plane,˜q (1/˜q) is exponentially suppressed and the
44 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
|sI(Φ)(x;τ)
PI(x;τ) − 1| |sI(Φ)(x;τ)
s′
I(Φ)(x;τ)− 1| | ˜q(τ)| | ˜x(x,τ )|
σ1 3.2× 10−66 9.7× 10−66
8.3× 10−33 0.05σ2 1.9× 10−94 5.2× 10−94
(a) Region I: τ = 1
20e
πi
5
|sII (Φ)(x;τ)
PII (x;τ) − 1| |sII (Φ)(x;τ)
s′
II (Φ)(x;τ)− 1| | ˜q(τ)| | ˜x(x,τ )−1|
σ1 1.9× 10−94 5.2× 10−94
8.3× 10−33 0.05σ2 3.2× 10−66 9.7× 10−66
(b) Region II: τ = 1
20e
4πi
5
|sIV (Φ)(x;τ)
PIV (x;τ) − 1| |sIV (Φ)(x;τ)
s′
IV (Φ)(x;τ)− 1| | ˜q(τ)−1| | ˜x(x,τ )|
σ1 1.9× 10−94 5.2× 10−94
8.3× 10−33 0.05σ2 3.2× 10−66 9.7× 10−66
(c) Region III: τ = 1
20e− 4πi
5
|sIII (Φ)(x;τ)
PIII (x;τ) − 1| |sIII (Φ)(x;τ)
s′
III (Φ)(x;τ)− 1| | ˜q(τ)−1| | ˜x(x,τ )−1|
σ1 3.2× 10−66 9.7× 10−66
8.3× 10−33 0.05σ2 1.9× 10−94 5.2× 10−94
(d) Region IV : τ = 1
20e−πi
5
Table 1. Numerical tests of holomorphic lifts of Borel sums of asymptotic
series for knot 41. We perform the Borel-Padé resummation onΦ(x;τ) with
280 terms atx = 6/5 andτ in four diﬀerent regions, and compute the relative
diﬀerence between them and the right hand side of (201a)–(201d), which we
denote byPR(x;τ). They are within the error margins of Borel-Padé resum-
mation, which are estimated by redo the resummation with 276 terms, denoted
bys′
R(•) in the tables. The relative errors are much smaller than|˜q±1|,|˜x±1|,
possible sources of additional corrections.
correction MR(˜x, ˜q)σ,σ′ as a series in˜q (1/˜q) is dominated by the leading term. (226) thus
becomes
∆σ(τ)Bσ(x;q)∼ exp
(
V (ˆσ) +ωˆσ
2πieiα k− log(iδ(x,y ˆσ)) +
∞∑
n=1
Sn(x,y ˆσ)eniαk−n
)
, k ≫ 1,
(227)
whereωˆσ is possible contribution from the leading term ofMR(˜x, ˜q)σ,ˆs, and the series ink−1
is logϕ(x,y ˆσ;τ). As pointed out in [GZa], this equation can be tested numerically with the
help of Richardson transformations (see for instance [BO99]).
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 45
Next, we can test (226) directly. One way of doing this is to compute Borel-Padé re-
summation sR(Φσ′)(x;τ) for various values ofx∈ R and τ in the same regionR, and by
comparing with the left hand side extract terms ofMR(˜x, ˜q)σ,σ′ order by order. To facilitate
this operation, instead ofMR(˜x; ˜q) we consider
~MR(˜x; ˜q) =
(
θ(−˜q−1/2˜x; ˜q)2 0
0 θ(−˜q1/2˜x; ˜q)−1
)
MR(˜x; ˜q) (228)
whose entries are˜q-series with coeﬃcients inZ[˜x±1] instead of inZ(˜x). Using 280 terms of
Φσ(x;τ), we ﬁnd the results forτ in the upper half plane
~MI(x;q) =
(
−x + (x2 +x3)q + (x2 +x3)q2 1− (x +x2 +x3)q− (x +x2)q2
−1 + (x−1 +x)q + (x−1 +x)q2 1− (x−1 + 1 +x)q− (x−1 +x)q2
)
+O(q3)
(229a)
~MII (x;q) =
(
−x + (1 +x−1 +x−2)q + (1 +x−1)q2 1− (x−1 +x−2)q− (x−1 +x−2)q2
−1 + (x + 1 +x−1)q + (x +x−1)q2 1− (x +x−1)q− (x +x−1)q2
)
+O(q3)
(229b)
and they agree with (186a), (186b). Another more decisive way is to compute both sides of
(226)numericallyassuming (186a), (186b)andcomparethem. Alternatively, wecancompare
two sides of the equations of holomoprhic lift (201a), (201b). We ﬁnd that the diﬀerence
between the two sides is always within the error margin of Borel-Paé resummation, and much
smaller than ˜q±1, ˜x±1, i.e. possible additional corrections. We illustrate this comparison by
one example withx = 6/5 and τ = 1
20e±πi
5, 1
20e± 4πi
5 in four regions in Table 1.
A ﬁnal way to test these results is to see that in thex↦→ 1 limit, the resurgent data as well
as the Stokes matrices (187a)–(187b) are compatible with the results in section 3.1 where
x = 1. This is a non-trivial test since the matrixW−1(x−1;q−1) (|q|< 1) in (187a)–(187b) is
divergent in the limitx↦→ 1.
