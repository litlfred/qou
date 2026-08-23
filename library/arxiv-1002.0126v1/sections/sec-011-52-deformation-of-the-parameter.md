---
doc_id: arxiv-1002.0126v1
doc_title: "An introduction to the volume conjecture"
section_id: sec-011-52-deformation-of-the-parameter
section_title: "Deformation of the parameter"
section_number: 5.2
pages: 29-38
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "An introduction to the volume conjecture — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
and its complexiﬁcation (Conjecture 5.1), the (possible) limit corres ponds to the
complete hyperbolic structure of S3\ K for a hyperbolic knot K. As described in
[34, Chapter 4] the complete structure can be deformed to incomp lete ones.
How can we perform this deformation in the colored Jones polynomial? If we
deform the parameter 2 π√−1 in the Volume Conjecture, is the corresponding limits
related to incomplete hyperbolic structures?
Let us consider the limit
lim
N →∞
log JN
(
K; exp
(
(u + 2π√−1)/N
) )
N .
Note that when u = 0, this limit is considered in the (complexiﬁed) Volume Con-
jecture.
5.2.1. Figure-eight knot. Before stating a conjecture for general knots, I will explain
what happens in the case of the ﬁgure-eight knot.
Theorem 5.3 ([30]). Let E be the ﬁgure-eight knot. There exists a neighborhood
O⊂ C of 0 such that if u∈ (O\ π√
−1Q)∪{ 0}, then the following limit exists:
lim
N →∞
log JN (E; exp
(
(u + 2π√−1)/N
)
)
N .
Moreover if we put
H(u) := ( u + 2π
√
−1)× (the limit above ),
30 HITOSHI MURAKAMI
and
v := 2 d H(u)
d u − 2π
√
−1
then we have
Vol(Eu) +
√
−1 CS(Eu)
≡−
√
−1H(u)− πu + u v
√
−1/4− πκ(γu)/2 (mod π2√
−1Z).
Here Eu is the closed hyperbolic three-manifold associated with th e following
representation of π1
(
S3\ E
)
→ SL(2; C):
µ↦→
( exp(u/2) ∗
0 exp( −u/2)
)
,
λ↦→
(
exp(v/2) ∗
0 exp( −v/2)
)
.
(5.1)
Here µ is the meridian of E (a loop in S3\ E that goes around the knot, which
generates H1(S3\ E)∼
= Z), λ is the longitude (a loop in S3\ E that goes along the
knot such that it is homologous to 0 in H1(S3\ E)), and γu is the loop attached to
S3\E when we complete the hyperbolic structure deﬁned by u. We also put κ(γu) :=
length(γu) +√
−1 torsion(γu), where length(γu) is the length of the attached loop
γu, and torsion is its torsion, which is deﬁned modulo 2π as the rotation angle when
one travels along γu. See [31] for details (see also [24]).
We will give a sketch of the proof in the following two subsections.
5.2.2. Calculation of the limit. First we calculate the limit. Note that here I give
just a sketch of the calculation but it can be done rigorously. For de tails see [30].
From (3.1) we have
JN (E; q) =
N −1∑
j=0
qjN
j∏
k=1
(
1− q−N −k)(
1− q−N +k)
.
Put q := exp(θ/N) for θ near 2 π√−1. If θ is not a rational multiple of π√−1 (but
it can be 2 π√−1), we have
log
( j∏
k=1
(
1− q−N ±k)
)
=
j∑
k=1
log
(
1− exp(±kθ/N− θ)
)
≈
N →∞
N
∫ j/N
0
log(1− exp(±θs− θ)) ds
=±N
θ
∫ exp(±jθ/N −θ)
exp(−θ)
log(1− t)
t dt
=±N
θ
(
Li2
(
exp(−θ)
)
− Li2
(
exp(±jθ/N− θ)
))
.
AN INTRODUCTION TO THE VOLUME CONJECTURE 31
So we have
JN
(
E; exp(θ/N)
)
≈
N →∞
N −1∑
j=0
exp(jθ) exp
[ N
θ
(
Li2
(
exp(−jθ/N− θ)
)
− Li2
(
exp(jθ/N− θ)
)) ]
=
N −1∑
j=0
exp
[ N
θ H
(
exp(jθ/N ), exp(θ)
) ]
≈
N →∞
∫
C
exp
[ N
θ H
(
x, exp(θ)
) ]
dx
for a suitable contour C. Here we put
(5.2) H(ζ, η) := Li 2(1/(ζη ))− Li2(ζ/η ) + log ζ log η.
To apply the steepest descent method (Theorem 4.2), we ﬁnd the m aximum of
Re
(
H
(
x, exp(θ)
)
/θ
)
over x. To do that we will ﬁnd a solution y to the equation
d H
(
x, exp(θ)
)
/d x = 0, which is
log
[
exp(θ) + exp(−θ)− x− x−1]
x = 0.
We can show that appropriately chosen y gives the maximum and from the steepest
descent method we have
JN
(
E; exp(θ/N)
)
≈
N →∞
exp
[ N
θ H
(
y, exp(θ)
) ]
,
that is,
(5.3) θ lim
N →∞
JN
(
E; exp(θ/N)
)
N = H
(
y, exp(θ)
)
,
where y satisﬁes
y + y−1 = exp(θ) + exp(−θ)− 1.
5.2.3. Calculation of the volume. Next we will relate the limit to the volume of a
three-manifold obtained by S3\ E.
As described in § 3.2.3, S3\ E is obtained by gluing two ideal hyperbolic tetra-
hedra as in Figure 28. Here we assume that they are parametrized b y complex
numbers z and w. When z = w = (1 +√−3)/2, S3\ E has a complete hyperbolic
structure as described in § 3.2.3. We assume that the left tetrahedron (with faces
labeled with A, B, C and D) and the right tetrahedron (with faces labeled with
A′, B′, C′ and D′) in Figure 28 are ∆( z) and ∆( w) respectively.
The boundary torus, which is obtained from the shadowed triangles in Figure 28,
looks like Figure 35. Here the leftmost triangle is the one in the center of the picture
of ∆( z) and the second leftmost one is the one in the center of the picture of ∆( w).
Let α, β and γ be the dihedral angle between B and C, A and B, and C and A
respectively. Let α′, β′ and γ′ be the dihedral angle between B′ and D′, A′ and B′,
and D′ and A′ respectively. As described in § 3.2.3, the sum of the dihedral angles
32 HITOSHI MURAKAMI
Figure 35. Identifying the sides as indicated by the circles, we
get a triangulation of the boundary torus. Here the single circles
denote the arrow head of the single arrow, the double circles denot e
the arrow head of the double arrow, the circles with − denote the
arrow tail of the single arrow, and the circles with + denote the
arrow tail of the double arrow in Figure 28. Note that we view this
torus from outside of S3\ E.
around each edge should be 2 π. So from Figure 35, we have
β + 2γ + β′ + 2γ′ = 2π from the single circles ,
2α + β + 2α′ + β′ = 2π from the double circles ,
β + 2γ + β′ + 2γ′ = 2π from the circles with −,
2α + β + 2α′ + β′ = 2π from the circles with + ,
which is equivalent to a single equation
2α + β + 2α′ + β′ = 2π
since α + β + γ = α′ + β′ + γ′ = π.
Assume that α = arg z and α′ = arg w. Since β = arg(1 − 1/z) and β′ =
arg(1− 1/w) (see Figures 30 and 31) this turns out to be
2 arg z + arg(1− 1/z) + 2 arg w + arg(1− 1/w) = 2 π.
So we have
(5.4) zw(z− 1)(w− 1) = 1 .
Remark 5.4. This is just a condition that S3\ E is hyperbolic. To make the metric
complete we need to add the condition that the upper side and the low er side of
the parallelogram in Figure 35 are parallel.
Now we introduce parameters x and y as
x := w(1− z),
y :=−zw.(5.5)
Note that the following equality holds from (5.4):
(5.6) y + y−1 = x + x−1− 1.
Since ∆( z) and ∆( w) can also be parametrized as ∆(1 − 1/z) and ∆(1 − 1/w),
we have
Vol(∆( z)) + Vol(∆( w))
= Im Li2(w′) + Im Li2(z′) + log|w′| arg(1− w′) + log|z′| arg(1− z′),
AN INTRODUCTION TO THE VOLUME CONJECTURE 33
from (4.10), where we put z′ := 1− 1/z and w′ := 1− 1/w. Using the equation
Li2(z′) + Li2(z′−1) =− π2
6 − 1
2
(
log(−z′)
) 2
(see for example [42, § 1.2]), we have
Vol(∆( z)) + Vol(∆( w))
= Im Li2(w′)− Im Li2(z′−1) + log|w′| arg(1− w′)− log|z′−1| arg(1− z′−1)
(since w′ = 1/(yx) and z′−1 = y/x)
= Im Li2(1/(yx))− Im Li2(y/x) + log|1/(yx)| arg(1− 1/(yx))− log|y/x| arg(1− y/x)
(from (5.6))
= Im Li2(1/(yx))− Im Li2(y/x) + log|y| arg x + log|x| arg 1− y/x
1− 1/(yx)
(from (5.5) and (5.4))
= Im Li2(1/(yx))− Im Li2(y/x) + log|y| arg x + log|x| arg y
z(z− 1)
(from (5.2))
= Im H(y, x)− log|x| arg(z(z− 1)).
(5.7)
Putting
u := log x = log(w(1− z)),
v := 2 log(z(1− z)),
H(u) := H(y, x),
we have
(5.8) Vol(∆( z)) + Vol(∆( w)) = Im H(u)− π Re u− 1
2 Re u Im v.
Moreover from (5.3), we have
(u + 2π
√
−1) lim
N →∞
log JN
(
E; exp((u + 2π√−1)/N)
)
N = H(u)
if we put θ = u + 2π√−1 since x = exp( u) = exp( θ). Note that z, w, x, y and v
are functions of u. Note also that v is given as
v = 2 d H(u)
d u − 2π
√
−1
since d H(u)
d u = log(z(z− 1)).
Remark 5.5. We need to be more careful about the arguments of variables. For
details see [30].
I will give geometrical interpretation of u and v to relate the term Re u Im v in
(5.8) to the length of γu.
We ﬁrst calculate H1(S3\ E) = H1(∆( z)∪ ∆( w)). Since the interiors of three-
simplices do not matter to the ﬁrst homology, we can calculate it from the boundary
34 HITOSHI MURAKAMI
torus, the edges of ∆( z) and ∆( w), and the faces A = A′, B = B′, C = C′, and
D = D′ (see Figures 28 and 35). From Figures 28, 35 and 36 one reads
∂A = ∂A′ = →− e7 + ։+ e10− ։− e5,
∂B = ∂B ′ =−→− e11− ։+ e6 + ։− e9,
∂C = ∂C ′ = ։+ e4 +→+ e8−→+ e1,
∂D = ∂D ′ = →+ e3− ։+ e2−→+ e12,
where → and ։ mean the single arrowed edge and the double arrowed edge in
Figure 28 respectively, and the ei are the edges of the boundary torus as indicated
in Figure 36. Since
e7 = e6 + e2,
e10 = e6,
e5 = e1 + e6,
e11 = e4 + e12 = e4 + e6,
e9 = e3 + e10 = e3 + e6,
e8 = e6,
e12 = e6
in the ﬁrst homology group, we have
→− e1− e2− e6 = 0,
−→− e3− e4− e6 = 0,
։+ e1 + e4 + e6 = 0,
− ։+ e2 + e3 + e6 = 0.
So if we put µ := e6, λ := e1 + e2 + e3 + e4 + 2µ, then we see that the ﬁrst homology
group of the boundary torus is generated by µ and λ, that H1(S3\ E)∼
= Z is
generated by µ, and that λ = 0 in H1(S3\ E). Therefore µ is the meridian and λ
is the longitude.
Figure 36. The cycle e6 is the meridian and the cycle e1 + e6 +
e2 + e8 + e3 + e4 is the longitude.
Now let us consider the universal cover ~S3\ E of S3\ E = ∆( z)∪ ∆( w) which
is H3. We can construct it by developing ∆( z) and ∆( w) isometrically in H3.
Then each loop in S3\ E is regarded as a covering translation of ~S3\ E and it
deﬁnes an isometric translation of H3. This deﬁnes a representation (holonomy
AN INTRODUCTION TO THE VOLUME CONJECTURE 35
representation) of π1
(
S3\ E) at P SL(2; C). Taking a lift to SL(2; C), we can
deﬁne a representation ρ : π1
(
S3\ E)→ SL(2; C).
We consider how ρ(µ) and ρ(λ) act on ∂H3 = S2 = C∪{∞} . The image of the
meridian ρ(µ) sends the top side to the bottom side. So it is the composition of
a−α-rotation around the circle with + in the top (between e1 and e2) and a γ′-
rotation around the single circle in the bottom (between e2 and e3), which means
a multiplication by 1 /z× 1/(1− w)) = w(1− z) plus a translation from (5.4).
Similarly ρ(λ) acts as a multiplication by z2(1− z)2 plus a translation.
Therefore u = log( w(1− z)) and v = 2 log( z(1− z)) can be regarded as the
logarithms of the actions by the meridian µ and the longitude λ, respectively.
Since the meridian and the longitude commute in π1(S3\ E), their images can
be simultaneously triangularizable. Recalling that µ and λ deﬁne multiplications
by exp( u) and exp( v) plus translations on ∂H3, we may assume
ρ(µ) =
( exp(u/2) ∗
0 exp( −u/2)
)
,
ρ(λ) =
( exp(v/2) ∗
0 exp( −v/2)
)
,
which is (5.1). This is a geometric interpretation of u and v.
Since u determines z and w, it deﬁnes a hyperbolic structure of S3\ E as the
union of ∆( z) and ∆( w). When u⁄= 0 this hyperbolic structure is incomplete. We
can complete this incomplete structure by attaching either a point o r a circle.
Since v is not a real multiple of u when u is small, there exists a pair ( p, q)∈ R2
such that pu + qv = 2π√−1. The pair ( p, q) is called the generalized Dehn surgery
coeﬃcient [34]. If p and q are coprime integers, then the completion is given by
attaching a circle γu and the result is a closed hyperbolic three-manifold which we
denote by Eu. (For other cases the completion is given by adding either a point
or a circle. In the former case the regular neighborhood of the att ached point is a
cone over a torus, and in the latter case the regular neighborhood of the attached
circle is topologically a solid torus but geometrically the angle around th e core is
not 2 π.)
If p and q are coprime integers, the completion is nothing but the ( p, q)-Dehn
surgery along the knot, that is, we attach a solid torus D to S3\ Int(N (E)) so
that the meridian of D coincides with the loop on the boundary of the regular
neighborhood N (E) of E⊂ S3 presenting pµ + qλ∈ H1(S3\ Int(N (E))), where
Int denotes the interior (Figure 37). Then the circle γu can be regarded as the core
of D.
To complete the proof of Theorem 5.3, we want to describe the lengt h of the
attached circle γu in terms of u and v. We will show
(5.9) length γu =− 1
2π Im (uv) .
When u is small and non-zero, we can assume that exp( u)⁄= 1 and exp( v)⁄= 1.
So we can also assume that ρ(µ) and ρ(λ) are both diagonal. This means that the
image of µ is a multiplication by exp( u) and that the image of λ is a multiplication
by exp(v) (with no translations). Note that now ~S3\ E is identiﬁed with H3 minus
the z-axis, and the completion is given by adding the z-axis.
Since p and q are coprime, we can choose integers r and s so that ps− qr = 1.
We push γu∈ D to the boundary of the solid torus ∂D and denote the resulting
36 HITOSHI MURAKAMI
∪
Figure 37. (2, 1)-Dehn surgery along the ﬁgure-eight knot
circle by ˜γu. Then we see that [˜ γu] = rµ + sλ∈ H1(∂(S3\ Int(N (E))); Z) since the
meridian of D is identiﬁed with pµ + qλ, and the images of the meridian and ˜ γu
make a basis of H1(∂(S3\ Int(N (E))); Z).
Remark 5.6. Even if we use another pair ( r′, s′) such that ps′− qr′ = 1, we get the
same manifold. This is because changing ( r, s) corresponds to changing of ˜γu∈ ∂D.
Observe that ambiguity of the choice of ˜γu is given by a twist of D and that it does
not matter to the resulting manifold.
Therefore ρ(γu) corresponds to a multiplication by exp(±(ru + sv)). This means
that if we identify the completion of ~S3\ E with H3, a fundamental domain of the
lift of γu is identiﬁed with the segment [1 , exp
(
± Re(ru + sv)
)
] in the z-axis. Since
the metric is given by
√
dx2 + dy2 + dz2/z, the length of γu is given by
length(γu) =
∫ exp
(
± Re(ru+sv)
)
1
dz
z
=± Re(ru + sv)
=±
( ps− 1
q Re(u) + s Re(v)
)
=±
( s
q (p Re(u) + q Re(v))− 1
q Re(u)
)
=∓ Re(u)
q
=∓1
2π (Re u Im v− Im u Re v)
=±1
2π Im(uv),
where the fourth and the sixth equalities follow from
( Re(u) Re( v)
Im(u) Im( v)
)( p
q
)
=
( 0
2π
)
.
Since v = u×|v|2
uv and the orientation of ( u, v) should be positive on C, we see that
Im(uv) is negative (see [31] for details) and so (5.9) follows.
AN INTRODUCTION TO THE VOLUME CONJECTURE 37
Therefore from (5.8) we ﬁnally have
Vol(Eu) = Re
(
−
√
−1H(u)− πu + 1
4 uv
√
−1− π
2 κ(γu)
)
.
The Chern–Simons invariant is obtained by Yoshida’s formula [41]. See [3 0] for
details.
5.2.4. General knots. Here I propose a generalization of the Volume Conjecture for
general knots.
Conjecture 5.7 ([26]). For any knot K, there exists an open set U∈ C such that
if u∈ U , then the following limit exists:
lim
N →∞
log JN (K; exp
(
(u + 2π√
−1)/N
)
)
N .
Moreover if we put
H(K; u) := ( u + 2π
√
−1)× (the limit above ),
and
v := 2 d H(K; u)
d u − 2π
√
−1,
then we have
Vol(K; u) = Im H(K; u)− π Re u− 1
2 Re u Im v.
Here Vol(K; u) is the volume function corresponding to the representation of π1(S3\
K) to SL(2; C) as in Theorem 5.3.
Remark 5.8. In the case of a hyperbolic knot, we can also propose a similar conjec -
ture with the imaginary part as in the case of the ﬁgure-eight knot. For a general
knot, a relation to the Chern–Simons invariant is also expected by us ing a combi-
natorial description of the Chern–Simons invariant by Zickert [44].
Remark 5.9. Conjecture 5.7 is known to be true for the ﬁgure-eight knot [30] a nd for
torus knots [26]. See also [27] and [10] for a possible relation to the Ch ern–Simons
invariant.
Finally note that Garoufalidis and Lˆ e proved the following result, whic h should
be compared with Conjecture 5.7. (See also [25] for the case of the ﬁgure-eight
knot.)
Theorem 5.10 (S. Garoufalidis and T. Lˆ e [5]). For any K, there exists ε > 0 such
that if |θ| < ε, we have
lim
N →∞
JN (K; exp(θ/N)) = 1
∆( K; exp θ) ,
where ∆( K; t) is the Alexander polynomial of K.
38 HITOSHI MURAKAMI
