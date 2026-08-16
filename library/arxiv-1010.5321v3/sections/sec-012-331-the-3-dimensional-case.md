---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗ ´A.G.Horv´ ath Department of Geometry"
section_id: sec-012-331-the-3-dimensional-case
section_title: "The 3-dimensional case"
section_number: 3.3.1
pages: 9-13
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
doc_brief: "Formulas on hyperbolic volume ∗ Á.G.Horváth Department of Geometry — This paper collects some important formulas on hyperbolic volume."
---
We now follow another way for computation, we will determine the integral
v(D) =
∫
D
(coshz)2(coshy)dydzdy =
a∫
0
φ(x)∫
0
ψ(x,y)∫
0
(coshz)2(coshy)dydzdx,
getting it from hyperbolic orthogonal coordinates using th e parameter valuek = 1. The functions
φ(x) and ψ (x,y ) can be determined as follows. Consider the orthosceme on Fi g.7. In the
a b
c
x=x
y=x
z=x
O Q
Q
,
P
P2
P1
3
1
2
b,
c,
y
zmax
Figure 7: Orthosceme and orthogonal coordinates
rectangular triangle △OP2P1 the tangent of the angle P2OP1∠ is:
tanP2OP1∠ = tanhb
sinha = tanhy1
sinhx .
So
tanhymax = tanhb
sinha sinhx,
9
hence
0 ≤y ≤φ(x) = tanh −1
(tanhb
sinha sinhx
)
=:λ.
Consider now the triangle △P1P2P3. The line O(x,y, 0) intersects that point Q for which |P1Q| =
b′, and let denote the point of the segment PP 1 aboveQ be Q′. Thus we get the equality
tanhc′ = tanhc
sinhb sinhb′.
Take into consideration again the equality
tanhb′ = tanhy
sinhx sinha,
and using the hyperbolic Pythagorean theorem, from the tria ngle △OQQ′ we get that
tanhzmax = tanhc′ sinh
(
cosh−1(coshx coshy)
)
sinh
(
cosh−1(cosha coshb′)
)= tanhc
sinhb sinhb′
√
cosh2x cosh2y − 1√
cosh2a cosh2b′ − 1
=
= tanhc
sinhb sinhb′
√
sinh2y + sinh2x cosh2y√
sinh2b′ + sinh2a cosh2b′
= tanhc
sinhb sinhy
√
1 + sinh2x coth2y√
1 + sinh2a coth2b′
=
= tanhc
sinhb sinhy.
Hence the assumption
0 ≤z ≤ψ (x,y ) = tanh −1
(tanhc
sinhb sinhy
)
=:ν
holds if we ﬁxed the ﬁrst two variables. Thus the required vol ume is:
v =
a∫
0
λ∫
0
ν∫
0
(coshz)2(coshy)dzdydx =
=
a∫
0
λ∫
0
1
2
[
z + 1
2 (sinh 2z)
] ν
0
(coshy)dydx.
Using now the equality
ν = 1
2 ln sinhb + tanhc sinhy
sinhb − tanhc sinhy,
we get that
v = 1
4



a∫
0


λ∫
0
ln sinhb + tanhc sinhy
sinhb − tanhc sinhy coshydy+
+
λ∫
0
sinh
(
ln sinhb + tanhc sinhy
sinhb − tanhc sinhy
)
coshydy

 dx


.
To determine the second integral we use that sinh x = ex−e−x
2 . Now
λ∫
0
sinh
(
ln sinhb + tanhc sinhy
sinhb − tanhc sinhy
)
coshydy =
10
= 1
2
λ∫
0
(sinhb + tanhc sinhy
sinhb − tanhc sinhy − sinhb − tanhc sinhy
sinhb + tanhc sinhy
)
coshydy =
= 2
λ∫
0
sinhy coshy
sinhb
tanhc − tanhc
sinhb sinh2y dy = 2
λ∫
0
sinh 2y
2 sinhb
tanhc − tanhc
sinhb cosh 2y + tanhc
sinhb
dy =
= − sinhb
tanhc
[
ln
(
2 sinhb
tanhc − tanhc
sinhb cosh 2y + tanhc
sinhb
)] λ
0
=
= − sinhb
tanhc ln
(
2 sinhb
tanhc − tanhc
sinhb cosh 2λ + tanhc
sinhb
)
+ sinhb
tanhc ln
(
2 sinhb
tanhc
)
.
From the deﬁnition of λ we can calculate cosh 2 λ and get:
cosh 2λ = 1
2
(sinha + tanhb sinhx
sinha − tanhb sinhx + sinha − tanhb sinhx
sinha + tanhb sinhx
)
,
thus the value of the second integral (denoted by II) is:
II := − sinhb
tanhc ln
(
1 − tanh2c sinh2x
cosh2b(sinh2a − tanh2b sinh2x)
)
.
The ﬁrst part can be integrated as follows:
λ∫
0
ln sinhb + tanhc sinhy
sinhb − tanhc sinhy coshydy =
{[
ln sinhb + tanhc sinhy
sinhb − tanhc sinhy sinhy
] λ
0
−
−
λ∫
0
tanhc coshy[(sinhb − tanhc sinhy) + (sinhb + tanhc sinhy)]
sinh2b − tanh2c sinh2y sinhydy


 =
=


sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ −
λ∫
0
2 tanhc sinhb coshy sinhy
sinh2b − tanh2c cosh2y + tanh2c dy


 =
=
{
sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ + sinhb
tanhc
[
ln(sinh2b − tanh2c cosh2y + tanh2c)
] λ
0
}
=
=
{
sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ + sinhb
tanhc
(
ln(sinh2b − tanh2c sinh2λ) − ln(sinh2b)
)}
.
Since
sinh2λ = tanh2b sinh2x
sinh2a − tanh2b sinh2x,
the ﬁrst integral is:
{
sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ + sinhb
tanhc ln
(
1 − tanh2c sinh2x
cosh2b(sinh2a − tanh2b sinh2x)
)}
=
= sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ − II.
The sum of the two parts is:
sinhλ ln sinhb + tanhc sinhλ
sinhb − tanhc sinhλ.
11
Fromλ = tanh −1(tanhb
sinha sinhx
)
follows
x = sinh −1
(tanhλ sinha
sinhb
)
= ln tanhλ sinha +
√
tanh2λ sinh2a + tanh2b
tanhb
and we get that
v = 1
4
b∫
0
tanhλ sinha√
tanh2b cosh2λ + sinh2a sinh2λ
ln
(sinhb + tanhc sinhλ
sinhb − tanhc sinhλ
)
dλ,
proving the theorem:
Theorem 1 Let the edges of an orthosceme be a,b,c , respectively where a⊥b and (a,b )⊥c. If
k = 1 then the volume of it is:
v = 1
4
b∫
0
tanhλ sinha√
tanh2b cosh2λ + sinh2a sinh2λ
ln
(sinhb + tanhc sinhλ
sinhb − tanhc sinhλ
)
dλ.
Corollary: This formula can be simpliﬁed in the case of asymptotic ortho scemes. If the edge-
length a tends to inﬁnity, the function tanhλ sinha√
tanh2b cosh2λ+sinh2a sinh2λ
tends to 1
coshλ showing that
the volume of the orthosceme with one ideal vertex is
v = 1
4
b∫
0
1
coshλ ln
(sinhb + tanhc sinhλ
sinhb − tanhc sinhλ
)
dλ.
If now the length of the edge c also grows to inﬁnity, then this formula simpliﬁed into:
v = 1
4
b∫
0
1
coshλ ln
(sinhb + sinhλ
sinhb − sinhλ
)
dλ,
which is the volume of an orthosceme with two ideal vertices. If now we reﬂect it in the face
containing the edges b and c then we get a tetrahedron with three ideal vertices. If than w e
reﬂect the getting tetrahedron in the face containing the ed gesb anda we get another one with
four ideal vertices. The volume of it is
v =
b∫
0
1
coshλ ln
(sinhb + sinhλ
sinhb − sinhλ
)
dλ.
Of this tetrahedron there are two edges ( a and c) which are skew and orthogonal to each other
(its common normal transversal is b). Since the reﬂection in the line of b is a symmetry of this
ideal tetrahedron, we can see that there are two types of its d ihedral angles, two opposite (at
the edges a and c) are equal to each other, ( say A); and the other four ones are also equal to
each other ( say B). Then we have A + 2B =π , and its volume by Milnor’s formula is equal to
v′ = Λ(π − 2B) + 2Λ(B) = Λ(2 B) + 2Λ(B) = 4Λ( B) + 2Λ
(
B + π
2
)
.
(We used that the Lobachevsky function is odd, periodic of pe riod π , and satisﬁes the identity
Λ(2B) = 2Λ( B) + 2Λ(B + π
2 ). ) We have the following connection between the two integrals :
0 =
b∫
0
1
coshλ ln
(sinhb + sinhλ
sinhb − sinhλ
)
dλ + 2
B+ π
2∫
0
ln |2 sinζ|dζ + 4
B∫
0
ln |2 sinζ|dζ.
12
Remark: If we substitute to this formula the ﬁrst-order terms of the T aylor series of the
functions in the integrand, respectively, we get that
v = 1
4
b∫
0
tanhλ sinha√
tanh2b cosh2λ + sinh2a sinh2λ
ln
(sinhb + tanhc sinhλ
sinhb − tanhc sinhλ
)
dλ =
= 1
2
b∫
0
λa√
b2 +a2λ 2
cλ
b dλ = ac
2b2
b∫
0
λ 2
√
1 dλ = abc
6 .
This shows that our formula for little values gives back the e uclidean one.
