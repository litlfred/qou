---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI"
section_id: sec-006-3-volume-conjecture
section_title: "Volume conjecture"
section_number: 3
pages: 15-22
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
Figure 22. The label of the arc between the second bottom cross-
ing and the bottom-most crossing should be i + j− k. Note that
j− k≥ 0
Figure 23. The label k should coincide with i.
From Figure 14, we have
JN (E; q)
=
∑
0≤i≤N −1,0≤j≤N −1
0≤i+j≤N −1
Ri,0
0,i (R−1)i,j
i+j,0 R0,i+j
i,j (R−1)j,0
0,j (µ−1)i
i µj
j
=
∑
0≤i≤N −1,0≤j≤N −1
0≤i+j≤N −1
(−1)i {i + j}!{N− 1}!
{i}!{j}!{N− 1− i− j}! q−(N −1)i/2+(N −1)j/2−i2/4+j2/4−3i/4+3j/4.
16 HITOSHI MURAKAMI
Figure 24. The ﬁgure-eight knot can also regarded as the closure
of a (1 , 1)-tangle.
Putting k := i + j, we have
JN (E; q) =
N −1∑
k=0
{N− 1}!
{N− 1− k}! qk2/4+N k/2+k/4
( k∑
i=0
(−1)i {k}!
{i}!{k− i}! q−N i−ik/2−i/2
)
.
Using the formula (see [28, Lemma 3.2])
k∑
i=0
(−1)iqli/2 {k}!
{i}!{k− i}! =
k∏
g=1
(1− q(l+k+1)/2−g),
we have the following simple formula with only one summand, which is due t o
Habiro and Lˆ e (I learned this method from Lˆ e).
(2.5) JN (E; q) = 1
{N}
N −1∑
k=0
{N + k}!
{N− 1− k}! .
3. Volume conjecture
In this section we state the Volume Conjecture and then prove it fo r the ﬁgure-
eight knot. We also give supporting evidence for the conjecture.
3.1. Statement of the V olume Conjecture. In [15] Kashaev introduced a link
invariant⟨L⟩N∈ C for an integer N greater than one and a link L by using the quan-
tum dilogarithm. Then he observed in [16] that the limit 2 π limN →∞ log|⟨K⟩N|/N
is equal to the hyperbolic volume of the knot complement if a knot K is hyperbolic.
Here a knot in the three-sphere S3 is called hyperbolic if its complement possesses
a complete hyperbolic structure with ﬁnite volume. He also conjectu red this would
also hold for any hyperbolic knot.
In [28] J. Murakami and I proved that Kashaev’s invariant equals the N -dimensional
colored Jones polynomial evaluated at the N -th root of unity, that is, ⟨L⟩N =
JN (L; exp(2π√
−1/N)) and proposed that Kashaev’s conjecture would hold for any
knot by using the simplicial volume.
AN INTRODUCTION TO THE VOLUME CONJECTURE 17
Conjecture 3.1 (Volume Conjecture [16, 28]) . The following equality would hold
for any knot K.
2π lim
N →∞
log|JN (K; exp(2π√−1/N))|
N = Vol(S3\ K).
To deﬁne the simplicial volume (or Gromov norm), we introduce the Ja co–
Shalen–Johannson (JSJ) decomposition (or the torus decomposit ion) of a knot
complement.
Deﬁnition 3.2 (Jaco–Shalen–Johannson decomposition [11, 13]) . Let K be a knot.
Then its complement S3\ K can be uniquely decomposed into hyperbolic pieces
and Seifert ﬁbered pieces by a system of tori:
S3\ K =
( ⨆
Hi
)
⊔
( ⨆
Ej
)
with Hi hyperbolic and Ej Seifert-ﬁbered.
Then the simplicial volume of the knot complement is deﬁned to be the s um of
the hyperbolic volumes of the hyperbolic pieces.
Deﬁnition 3.3 (Simplicial volume (Gromov norm) [7]) . If a knot complement
S3\ K is decomposed as above, then its simplicial volume Vol( S3\ K) is deﬁned as
Vol(S3\ K) :=
∑
Hi:hyperbolic piece
Hyperbolic Volume of Hi.
Example 3.4. Let us consider the (2 , 1)-cable of the ﬁgure-eight knot as shown
in ﬁgure 25. Then its complement can be decomposed by a torus into t wo pieces
Figure 25. (2, 1)-cable of the ﬁgure-eight knot
(Figure 26), one hyperbolic and one Seifert ﬁbered. Therefore we have
Vol
































= Vol
































.
18 HITOSHI MURAKAMI
=
hyperbolic
⊔
Seifert ﬁbered
Figure 26. The JSJ decomposition of the (2 , 1)-cable of the
ﬁgure-eight knot
3.2. Proof of the V olume Conjecture for the ﬁgure-eight knot. We give a
proof of the Volume Conjecture for the ﬁgure-eight knot due to T . Ekholm.
3.2.1. Calculation of the limit. We use the formula (2.5) of the colored Jones poly-
nomial for the ﬁgure-eight knot E due to Habiro and Lˆ e. (See [8, 21] for Habiro’s
method.) By a simple calculation using it, we have
(3.1) JN (E; q) =
N −1∑
j=0
j∏
k=1
(
q(N −k)/2− q−(N −k)/2
)(
q(N +k)/2− q−(N +k)/2
)
.
Replacing q with exp(2 π√
−1/N), we have
JN
(
E; exp(2π
√
−1/N)
)
=
N −1∑
j=0
j∏
k=1
f (N ; k)
where we put f (N ; k) := 4 sin 2(kπ/N ). The graph of f (N ; k) is depicted in Fig-
ure 27.
Figure 27. Graph of f (N ; k)
Put g(N ; j) := ∏ j
k=1 f (N ; k) so that JN
(
E; exp(2π√
−1/N)
)
=∑ N −1
j=0 g(N ; j).
Then g(N ; j) decreases when 0 < j < N/ 6 and 5 N/6 < j , and increases when
AN INTRODUCTION TO THE VOLUME CONJECTURE 19
N/6 < j < 5N/6. Therefore g(N ; j) takes its maximum at j = 5 N/6. (To be
precise we need to take the integer part of 5 N/6.) See Table 1. Since there are N
j 0 ··· N/6 ··· 5N/6 ··· 1
f (N ; k) < 1 1 > 1 1 < 1
g(N ; j) 1 ց ր maximum ց
Table 1. table of f (N ; k) and g(N ; j)
positive terms in JN
(
E; exp(2π√−1/N)
)
=∑ N −1
j=0 g(N ; j) and g(N ; 5N/6) is the
maximum of these terms, we have
g(N ; 5N/6)≤ JN
(
E; exp(2π
√
−1/N)
)
≤ N× g(N ; 5N/6).
Noting that each side is positive, we take their logarithms and divide th em by N .
log g(N ; 5N/6)
N ≤ log JN
(
E; exp(2π√−1/N)
)
N ≤ log N
N + log g(N ; 5N/6)
N .
Since log N →∞(log N )/N = 0, we have
lim
N →∞
log g(N ; 5N/6)
N ≤ lim
N →∞
log JN
(
E; exp(2π√−1/N)
)
N ≤ lim
N →∞
log g(N ; 5N/6)
N .
Therefore we have
lim
N →∞
log JN
(
E; exp(2π√−1/N)
)
N = lim
N →∞
log g(N ; 5N/6)
N .
We can calculate the limit lim N →∞
(
log g(N ; 5N/6)
)
/N by integration. Since
g(N ; j) =∏ j
k=1 f (N ; k), we have
lim
N →∞
log g(N ; 5N/6)
N = lim
N →∞
1
N
5N/6∑
k=1
log f (N ; k)
= 2 lim
N →∞
1
N
5N/6∑
k=1
log
(
2 sin(kπ/N )
)
= 2
π
∫ 5π/6
0
log
(
2 sin x
)
dx.
(3.2)
What does this mean? I will explain a geometric interpretation of this in tegral.
3.2.2. Lobachevsky function. The function deﬁned by the integral in (3.2) is known
as the Lobachevsky function. More precisely, we deﬁne the Lobac hevsky function
Λ( θ) as
Λ( θ) :=−
∫ θ
0
log|2 sin x| dx
for θ∈ R. By using this function, we can express the limit of the colored Jones
polynomial as
(3.3) lim
N →∞
log JN
(
E; exp(2π√
−1/N)
)
N =− 2
π Λ(5 π/6)
We show some properties of the Lobachevsky function (see for ex ample [23]).
Lemma 3.5. The Lobachevsky function satisﬁes the following two proper ties.
20 HITOSHI MURAKAMI
(1) The Lobachevsky function is an odd function and has period π.
(2) We have Λ(2 θ) = 2Λ( θ) + 2Λ( θ + π/2). In general we have Λ( nθ) =
n∑ n−1
k=1 Λ( θ + kπ/n).
Proof. The ﬁrst property is easily shown by the periodicity of the sine funct ion.
To prove the second, we use the double angle formula of the sine fun ction:
sin(2x) = 2 sin x cos x. We have
log|2 sin(2x)| = log|2 sin x| + log|2 cos x| = log|2 sin x| + log|2 sin(x + π/2)|,
completing the proof. □
From (1) we have
Λ(5 π/6) = Λ(−π/6) =−Λ( π/6).
From (2) and (1) we also have
Λ( π/3) = 2Λ( π/6) + 2Λ(2 π/3) = 2Λ( π/6)− 2Λ( π/3).
Therefore we have
Λ(5 π/6) =− 3
2 Λ( π/3).
Returning to the limit of the Jones polynomial (3.3), we conclude that
2π lim
N →∞
log JN
(
E; exp(2π√−1/N)
)
N = 6Λ( π/3).
Next we show how the Lobachevsky function is related to hyperbolic geometry.
3.2.3. Hyperbolic geometry. It is well known that the complement of the ﬁgure-eight
knot can be decomposed into two ideal hyperbolic regular tetrahed ra.
Theorem 3.6 (W. Thurston [34]) . The complement of the ﬁgure-eight knot can be
obtained by gluing two ideal hyperbolic regular tetrahedra .
I will explain what is an ideal hyperbolic regular tetrahedron later. To pologically,
the theorem states that the complement of the ﬁgure-eight knot can be obtained
by gluing two truncated tetrahedra as in Figure 28 (see also [24]). In Figure 28 we
identify A with A′, B with B′, C with C′ and D with D′. Note that edges with
single arrows and edges with double arrows are also identiﬁed respec tively.
= ∪
A=A′,B=B′,
C=C ′,D=D′
Figure 28. The complement of the ﬁgure-eight knot is decom-
posed into two ideal hyperbolic regular tetrahedra. Shadowed tri-
angles make the boundary of the knot complement.
Here I give a short introduction to hyperbolic geometry.
First consider the upper half space {(x, y, z)∈ R3 | z > 0} with hyperbolic
metric ds :=
√
dx2 + dy2 + dz2/z and denote it by H3. It is known that a geodesic
AN INTRODUCTION TO THE VOLUME CONJECTURE 21
line in H3 is a semicircle or a straight line perpendicular to the xy-plane, and that
a geodesic plane is a hemisphere or a ﬂat plane perpendicular to the xy-plane.
An ideal hyperbolic tetrahedron is a tetrahedron in H3 with geodesic faces with
four vertices at inﬁnity, that is, on the xy-plain or at the point at inﬁnity ∞.
By isometry we may assume that one vertex is ∞ and the other three are on the
xy-plane. So its faces consist of three perpendicular planes and a hem isphere as
shown in Figure 29. If we see the tetrahedron from the top, it is a (E uclidean)
Figure 29. An ideal hyperbolic tetrahedron is the part above the
hemisphere surrounded by three perpendicular planes.
triangle with angles α, β, and γ. It is known that an ideal hyperbolic tetrahedron
Figure 30. A top view (right) of the ideal hyperbolic tetrahedron (left)
is deﬁned (up to isometry) by the similarity class of this triangle. Ther efore we
can parametrize an ideal hyperbolic tetrahedron by a triple of posit ive numbers
(α, β, γ) with α + β + γ = π. We denote it by ∆( α, β, γ).
The hyperbolic volume Vol(∆( α, β, γ)) can be expressed by using the Lobachevsky
function Λ( θ). In fact it can be shown that
Vol(∆( α, β, γ)) = Λ( α) + Λ( β) + Λ( γ).
For a proof, see for example [34, Chapter 7].
Now we return to the decomposition of the ﬁgure-eight knot comple ment. Fig-
ure 28 shows that after identiﬁcation we have two edges, edge with single arrow
and edge with double arrow, each of them is obtained by identifying six edges.
So if the ideal hyperbolic tetrahedra we are using are regular, that is, isometric
to ∆( π/3, π/3, π/3) then the sum of dihedral angles around each edge becomes
22 HITOSHI MURAKAMI
2π. This means that if we use two ideal hyperbolic regular tetrahedra, our glu-
ing is geometric, that is, the complement of the ﬁgure-eight knot is is ometric
to the union of two copies of ∆( π/3, π/3, π/3). In particular its volume equals
2 Vol(∆( π/3, π/3, π/3)) = 6Λ( π/3).
Thus we have proved
2π lim
N →∞
log JN
(
E; exp(2π√−1/N)
)
N = 6Λ( π/3) = Vol
(
S3\ E
)
,
which is the statement of the Volume Conjecture for the ﬁgure-eig ht knot.
3.3. Knots and links for which the V olume Conjecture is proved. As far
as I know the Volume Conjecture is proved for
(1) ﬁgure-eight knot by Ekholm,
(2) 5 2 knot by Kashaev and Yokota,
(3) Whitehead doubles of torus knots by Zheng [43],
(4) torus knots by Kashaev and Tirkkonen [17],
(5) torus links of type (2 , 2m) by Hikami [9],
(6) knots and links with volume zero by van der Veen [37],
(7) Borromean rings by Garoufalidis and Lˆ e [6],
(8) twisted Whitehead links by Zheng [43],
(9) Whitehead chains by van der Veen [38],
(10) a satellite link around the ﬁgure-eight knot with pattern the Wh itehead
link by Yamazaki and Yokota [39].
Note that (1) and (2) are for hyperbolic knots, (3) is for a knot wh ose JSJ decom-
position consists of a hyperbolic piece and a Seifert ﬁbered piece, (4 )–(6) are for
knots and links only with Seifert pieces, (7)–(9) are for hyperbolic lin ks, and (10)
is for a link whose JSJ decomposition consists of a hyperbolic piece and a Seifert
ﬁbered piece.
