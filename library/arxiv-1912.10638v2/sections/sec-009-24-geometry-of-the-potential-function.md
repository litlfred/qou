---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-009-24-geometry-of-the-potential-function
section_title: "Geometry of the potential function"
section_number: 2.4
pages: 16-32
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
---
To understand the critical values of the potential functions, we need to ﬁnd a concrete triangulation of
the link complement associated to the potential function. The triangulation is the one appeared in [21].
First of all, we prepare an ideal octahedra (Figure 3). The idea is to glue the two blue faces together and
the two red faces together (Figure 4) to form a cylinder.
Figure 3: ideal octahedron
Figure 4: glue the faces with the same color together
The following pictures illustrate how to obtain a cylinder from an ideal octahedron.
16
Figure 5: the faces B1 and B2 are glued to-
gether
Figure 6: deform the object so that it looks like
a cylinder
Figure 7: the faces D1 and D2 are glued to-
gether
 Figure 8: deform the object to obtain a
cylinder with a clasp removed
Next, we consider the curl face of the cylinder. The labels 1 , 2, 3, 4 refer to the truncated faces of the
ideal octahedron. If we glue the top of the cylinder to the bottom according to the rule C2→ C1 and
A2→A1, we will obtain a decomposition of the boundary torus into parallelograms. Note that this torus
is exactly the boundary torus of a tubular neighborhood of the belt component of the Whitehead link.
17
Figure 9: decomposition of the curl face into parallelograms
Next, we decompose the ideal octahedron into 5 ideal tetrahedra and assign shape parameters to
them (Figure 10). The parameters U,Z and W are related by U = (ZW )−1. The decomposition of the
truncated faces and the assignments of shape parameters to them are shown in Figure 11.
Figure 10: decomposition of the ideal octahedron into 5 ideal tetrahedra
18
Figure 11: assignment of shape parameters
After that, we slide the left edge down (Figure 12) to obtain the geometric triangulation of the curl
surface.
Figure 12: triangulation of the boundary torus of the belt component
Recall that for each triangle, the shape parameters are given in counter-clockwise by A, A′ = 1
1−A
and A′′ = 1− 1
A respectively. From direct computation, for the boundary torus of the belt component,
the edges equations are given by
• vertex (i):
[W′Z′′(B−1
2 W )′(B2U)′Z′′U′][(B−1
2 W )′′Z′U′W′′Z′(B2U)′′] =−1
W
−1
Z
−1
Z
−1
B−1
2 W
−1
B2U
−1
U = 1 (43)
19
• vertex (ii):
(WU′W′′)((B2U)′(B−1
2 W )′′(B2U)) =
(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)−1
=
B2
(
1− B2
W
)
(1−W )
(1−B2U)
(
1− 1
U
) (44)
• vertex (iii):
[W′Z′′(B−1
2 W )′(B2U)′Z′′U′][(B−1
2 W )′′Z′U′W′′Z′(B2U)′′] =−1
W
−1
Z
−1
Z
−1
B−1
2 W
−1
B2U
−1
U = 1 (45)
• vertex (iv):
(UW′U′′)((B−1
2 W )′(B2U)′′(B−1
2 W )) =
[(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)−1]−1
=
(1−B2U)
(
1− 1
U
)
B2
(
1− B2
W
)
(1−W )
(46)
For the top and bottom truncated faces, we have
Figure 13: triangulation of the boundary torus of the belt component
From direct computation, for the boundary torus of the clasp component, the edges equations are
given by
• vertex (v):
(W )(B2U)(B−1
2 W )′′(B2U)′(W )′′(U′) =
(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)−1
=
B2
(
1− B2
W
)
(1−W )
(1−B2U)
(
1− 1
U
) (47)
• vertex (vi):
(B−1
2 W )(B2U)′′(W′)(U)′′(B−1
2 W )′(U) =
[(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)−1]−1
=


B2
(
1− B2
W
)
(1−W )
(1−B2U)
(
1− 1
U
)


−1
(48)
Now we can explore the correspondence between the critical point equations of the potential function
and the edges equations of this triangulation. For Φ +(s1,s2)(z1,z 2), recall that the critical point equations
20
are given by



log(1−e2πi(s2−1)e−2πiz1−2πiz2) + log(1−e2πiz1+2πiz2)− log(1−e2πiz1)
= 2πi [−(s1− 1) + (s2− 1)]
log(1−e2πi(s2−1)e−2πiz1−2πiz2) + log(1−e2πiz1+2πiz2)− log(1−e2πi(s2−1)−2πiz2)
− log(1−e2πiz2)
= 2πi(s2− 1)
(49)
(50)
Put Z = e2πiz1, W = e2πiz2, U = (ZW )−1, B1 = e2πis1 and B2 = e2πis2. After taking exponential,
we have 


(1−B2U)
(
1− 1
U
)
(1−Z) =B−1
1 B2
(1−B2U)
(
1− 1
U
)
(1− B2
W )(1−W )
=B2
(51)
(52)
In particular, from (52) we have
(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)−1
= 1
i.e. the edge equations of the triangulation (44), (46), (47) and (48) are satisﬁed. Furthermore, by (51),
the holonomy of the meridian of the belt component (Figure 12) is given by
m1 = W′′U′
W′′Z′(B2U)′′ = B2 (1−Z)
(1−B2U)
(
1− 1
U
) =B1 (53)
By (52), the holonomy of the longitude of the clasp component (Figure 13) is given by
l2 = (B−1
2 W )′
(B2U)′ · U′′
W′′ =
(1−B2U)
(
1− 1
U
)
(
1− B2
W
)
(1−W )
×B2 =B2
2 (54)
Finally, for the potential function Φ−(s1,s2)(z1,z 2), by replacing B1 byB−1
1 in the above, we have the
same correspondence between critical point equations of the potential function and the hyperbolic gluing
equation for the triangulation of the link complement.
2.5 Diﬀerential formula for the potential function
After we associate a triangulation of the link complement to the potential functions, we need to prove
that the critical values of the potential functions Φ±(s1,s2)(z±(z1,z2)) are indeed the sum of the hyperbolic
volume of the tetrahedra. This can be done by using the following diﬀerential formula satisﬁed by the
potential functions.
Lemma 4. Writezk =xk +iyk fork = 1, 2. The real part of the potential function satisﬁes the following
diﬀerential equation:
Re Φ±(s1,s2)(z1,z 2) = 1
2πV±(s1,s2)(z1,z 2) +
2∑
k=1
yk
∂
∂yk
Re Φ±(s1,s2)(z1,z 2), (55)
where
V±(s1,s2)(z1,z 2) =D(e2πi(s2−1)−2πiz1−2πiz2)−D(e2πi(s2−1)−2πiz2) +D(e2πiz2)
−D(e2πiz1+2πiz2) +D(e2πiz1) (56)
and D(z) is the Bloch-Wigner function
D(z) = Im Li2(z) + log|z| Arg(1−z) (57)
21
Proof. First of all, for z =x +iy, since
d
dz
Li2(e2πiz)
2πi =− log(1−e2πiz)
we have
Im d
dz
Li2(e2πiz)
2πi =− Arg(1−e2πiz)
By the Cauchy Riemann equations, we have
∂
∂y Re Li2(e2πiz)
2πi = Arg(1−e2πiz)
Therefore,
Re Li2(e2πiz)
2πi = Im Li2(e2πiz)
2π
= D(e2πiz)− log|e2πiz| Arg(1−e2πiz)
2π
= D(e2πiz)
2π +y ∂
∂y Re Li2(e2πiz)
2πi
Following the same arguments, it is easy to show that
Re Li2(e−2πiz)
2πi = D(e−2πiz)
2π +y ∂
∂y Re Li2(e−2πiz)
2πi
Thus,
Re Li2(e2πi(s2−1)−2πiz1−2πiz2)
2πi = D(e2πi(s2−1)−2πiz1−2πiz2)
2π +
2∑
k=1
yk
∂
∂yk
Re Li2(e2πi(s2−1)−2πiz1−2πiz2))
2πi
Re Li2(e2πi(s2−1)−2πiz2)
2πi = D(e2πi(s2−1)−2πiz1−2πiz2)
2π +y2
∂
∂y2
Re Li2(e2πi(s2−1)−2πiz2))
2πi
Besides, for the linear terms in z1,z 2, it is straight forward to verify that
Re 1
2πi
[
± (2πi (s1− 1))
(
2πi
(
z1− 1
2
))]
=y1
∂
∂y1
Re 1
2πi
[
± (2πi (s1− 1))
(
2πi
(
z1− 1
2
))]
Re 1
2πi [−(2πi(s2− 1))(2πiz1 + 2πiz2)] =
2∑
k=1
yk
∂
∂yk
Re 1
2πi [−(2πi(s2− 1))(2πiz1 + 2πiz2)]
As a result, by direct computation, we get the diﬀerential formula.
Together with the discussion in previous subsection, we have
Re Φ±(s1,s2)(z±(z1,z2)) = 1
2πV±(s1,s2)(z±(z1,z2)) = 1
2π Vol
(
S3\WL,u 1 =±2πi(1−s1),v 2 = 4πi(1−s2)
)
By the Theorem 3 in [16], since v2 is even in u1 and the volume function is an even function in the
variableu1, we have
Vol
(
S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)
)
= Vol
(
S3\WL,u 1 =−2πi(1−s1),v 2 = 4πi(1−s2)
)
Thus we have
Re Φ±(s1,s2)(z±(z1,z2)) = 1
2π Vol
(
S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)
)
(58)
Next, from the deﬁnitions of the functions Φ±(s1,s2)(z±(z1,z2)), if we regards1,s 2 as complex variables,
then we get two holomorphic functions in s1,s 2. In particular, for each ﬁxed s2∈ R suﬃciently close to
1, we have two holomorphic functions for s1 suﬃciently close to 1 given by
N±(s1) = Φ±(s1,s2)(z+(z1,z2))
22
with the same real part
ReN±(s1) = 1
2π Vol
(
S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)
)
Besides, when s1 = 1, we have N+(1) =N−(1). As a result, N+(s1) =N−(s1) for all real s1∼ 1. Since
this is true for all s2∼ 1, we have
Φ+(s1,s2)(z+(z1,z2)) = Φ−(s1,s2)(z−(z1,z2)) (59)
for all s1,s 2∼ 1. This completes the proof of Theorem 3.
Finally, to prove Corollary 1, note that by Theorem 3, we have
lim
N→∞
1
N + 1
2
log
⏐⏐⏐⏐JM1,M2(WL,e
2πi
N + 1
2 )
⏐⏐⏐⏐ = Vol(S3\WL,u 1 = 2πi(1−s1),v 2 = 4πi(1−s2)) (60)
lim
N→∞
1
N + 1
2
log
⏐⏐⏐⏐JM2,M1(WL,e
2πi
N + 1
2 )
⏐⏐⏐⏐ = Vol(S3\WL,u 1 = 2πi(1−s2),v 2 = 4πi(1−s1)) (61)
By exchanging the components of the Whitehead link, we have
lim
N→∞
1
N + 1
2
log
⏐⏐⏐⏐JM1,M2(WL,e
2πi
N + 1
2 )
⏐⏐⏐⏐ = lim
N→∞
1
N + 1
2
log
⏐⏐⏐⏐JM2,M1(WL,e
2πi
N + 1
2 )
⏐⏐⏐⏐ (62)
This proves (1). Besides, recall that u2 = 0 if and only if v2 = 0. (2) follows from (1) by putting s2 = 1.
3 Generalization to JM1,M2(Wa,1,c,d, e
2πi
N+ 1
2 )
3.1 Potential functions for JM1,M2(Wa,1,c,d, e
2πi
N + 1
2 )
In this section, we compute the potential functions of the ˜JM1,M2(Wa,1,c,d,e
2πi
N + 1
2 ) with the belt colored
byM1 and all the other components colored by M2. First of all, recall from [22] that the unnormalized
JM1,M2(Wa,1,c,d) is given by 2
JM1,M2(Wa,1,c,d) = 1
t
1
2−t− 1
2
M2−1∑
n=0
(t
M1 (2n+1)
2 −t−M1 (2n+1)
2 )×tan(n+1)× ˜C(n,t ;M2)c× ˜C(n,t−1;M2)d
where
˜C(n,t ;M2) =t
M2 (M2−1)
2
M2−1−n∑
l=0
t−M2(l+n)
n∏
j=1
(1−tM2−l−j)(1−tl+j)
1−tj .
Note that the contribution of the twists is given by
tan(n+1) =e
a
(
N + 1
2
2πi
)[
2πi
(
n
N + 1
2
)][
2πi
(
n
N + 1
2
+ 1
N + 1
2
)]
=e
a
(
N + 1
2
2πi
)[
2πi
(
n
N + 1
2
− 1
2
)][
2πi
(
n
N + 1
2
− 1
2 + 1
N + 1
2
)]
×eaπi−a
4 (2πi)(N+ 1
2 )
= (−1)ae−a
4 (2πi)(N+ 1
2 )×e
a
(
N + 1
2
2πi
)[
2πi
(
n
N + 1
2
− 1
2
)][
2πi
(
n
N + 1
2
− 1
2 + 1
N + 1
2
)]
(63)
2when c + d = 1, there is an extra factor t
M 2
2−1
2 coming from the framing. Since it does not aﬀect the exponential
growth rate of the colored Jones polynomials, for simplicity we ignore this factor.
23
Besides, for the colored Jones polynomials of the mirror clasp, note that
n∏
j=1
(1−t−(M2−l−j)) =
n∏
j=1
(1−t−M2+(N+ 1
2 )+l+j)
=
n∏
j=1
(
1−e
2πi
(
−
(
M2
N + 1
2
−1
)
+ l
N + 1
2
+ j
N + 1
2
))
= exp

N + 1
2
2πi
n∑
j=1
(
ϕr
(
−π
( M2
N + 1
2
− 1
)
+ lπ
N + 1
2
+ (j− 1
2)π
N + 1
2
)
−ϕr
(
−π
( M2
N + 1
2
− 1
)
+ lπ
N + 1
2
+ (j + 1
2)π
N + 1
2
)))
= exp
(N + 1
2
2πi
(
ϕr
(
−π
( M2
N + 1
2
− 1
)
+ lπ
N + 1
2
+ π
2N + 1
)
−ϕr
(
−π
( M2
N + 1
2
− 1
)
+ lπ
N + 1
2
+ nπ
N + 1
2
+ π
2N + 1
)))
(64)
Besides,
n∏
j=1
(1−t−(l+j)) =
n∏
j=1
(
1−e
2πi
(
1− l
N + 1
2
− j
N + 1
2
))
= exp

N + 1
2
2πi
n∑
j=1
(
ϕr
(
π− lπ
N + 1
2
− (j + 1
2)π
N + 1
2
)
−ϕr
(
π− lπ
N + 1
2
− (j− 1
2)π
N + 1
2
))

= exp
(N + 1
2
2πi
(
ϕr
(
π− lπ
N + 1
2
− nπ
N + 1
2
− π
2N + 1
)
−ϕr
(
π− lπ
N + 1
2
− π
2N + 1
)))
(65)
n∏
j=1
(1−t−j) =
n∏
j=1
(
1−e
2πi
(
1− j
N + 1
2
))
= exp

N + 1
2
2πi
n∑
j=1
(
ϕr
(
π− (j + 1
2)π
N + 1
2
)
−ϕr
(
π− (j− 1
2)π
N + 1
2
))

= exp
(N + 1
2
2πi
(
ϕr
(
π− nπ
N + 1
2
− π
2N + 1
)
−ϕr
(
π− π
2N + 1
)))
(66)
For eachi = 1, 2,...,c , deﬁne the function ψ(s1,s2)
i,M1,M2(z1,zi+1) by
ψ(s1,s2)
i,M1,M2(z1,zi+1) = 1
2πi
{
−
(
2πi
( M2
N + 1
2
− 1
))
(2πiz1 + 2πizi+1)
+
[
ϕr
( M2π
N + 1
2
−πz1−πzi+1− π
2N + 1
)
−ϕr
( M2π
N + 1
2
−πzi+1− π
2N + 1
)
+ϕr
(
πzi+1 + π
2N + 1
)
−ϕr
(
πz1 +πzi+1 + π
2N + 1
)
+ϕr
(
πz1 + π
2N + 1
)]}
(67)
24
For eachi = 1, 2,...,d , deﬁne the function κ(s1,s2)
i,M1,M2(z1,zc+i+1) by
κ(s1,s2)
i,M1,M2(z1,zc+i+1) = 1
2πi
{(
2πi
( M2
N + 1
2
− 1
))
(2πiz1 + 2πizc+i+1)
−
[
ϕr
(
−π
( M2
N + 1
2
− 1
)
+πz1 +πzc+i+1 + π
2N + 1
)
−ϕr
(
−π
( M2
N + 1
2
− 1
)
+πzc+i+1 + π
2N + 1
)
+ϕr
(
π−πzc+i+1− π
2N + 1
)
−ϕr
(
π−πz1−πzc+i+1− π
2N + 1
)
+ϕr
(
π−πz1− π
2N + 1
)]}
(68)
Altogether, by (7) - (14) and (63) - (66), we have
JM1,M2(Wa,1,c,d,e
2πi
N + 1
2 ) = (−1)(M1−N+a)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
e−a
4 (2πi)(N+ 1
2 )e
2πi
N + 1
2
(c−d)M2 (M2−1)
2
2 sin( π
N+ 1
2
)
× exp
(
−ϕr
( π
2N + 1
))c
exp
(
ϕr
(
π− π
2N + 1
))d
× (I+ +I−) (69)
where
I± =
M2−1∑
n=0
M2−1−n∑
l1=0
···
M2−1−n∑
lc=0
M2−1−n∑
l′
1=0
···
M2−1−n∑
l′
d=0
exp
((
N + 1
2
)
Φ±(s1,s2);a,c,d
M1,M2
( n
N + 1
2
, l1
N + 1
2
,..., lc
N + 1
2
, l′
1
N + 1
2
,..., l′
d
N + 1
2
))
(70)
with
Φ±(s1,s2);a,c,d
M1,M2 (z1,z 2,...,z c+1,zc+2,...,z c+d+1)
= 1
2πi
{
±2πi
( M1
N + 1
2
− 1
)(
2πi
(
z1− 1
2
))
+a
[
2πi
(
z1− 1
2
)][
2πi
(
z1− 1
2 + 1
N + 1
2
)]}
+
c∑
i=1
ψ(s1,s2)
M1,M2,i(z1,zi+1) +
d∑
i=1
κ(s1,s2)
M1,M2,i(z1,zc+i+1)
TakeN→∞ , we have
ψ(s1,s2)
i (z1,zi+1) = 1
2πi [−2πi(s2− 1)(2πiz1 + 2πizi+1)
+ Li2
(
e2πi(s2−1)−2πiz1−2πizi+1
)
− Li2
(
e2πi(s2−1)−2πizi+1
)
+ Li2
(
e2πizi+1
)
− Li2
(
e2πiz1+2πizi+1
)
+ Li2
(
e2πiz1
)]
,
κ(s1,s2)
i (z1,zc+i+1) = 1
2πi [2πi(s2− 1)(2πiz1 + 2πizc+i+1)
− Li2
(
e−2πi(s2−1)+2πiz1+2πizc+i+1
)
+ Li2
(
e−2πi(s2−1)+2πizc+i+1
)
− Li2
(
e−2πizc+i+1
)
+ Li2
(
e−2πiz1−2πizc+i+1
)
− Li2
(
e−2πiz1
)
]
and
Φ±(s1,s2);a,c,d(z1,z 2,z 3,...,z c+1,zc+2,...,z c+d+1)
= 1
2πi
{
±2πi (s2− 1)
(
2πi
(
z1− 1
2
))
+a
[
2πi
(
z1− 1
2
)]2}
+
c∑
i=1
ψ(s1,s2)
i (z,zi+1) +
d∑
i=1
κ(s1,s2)
i (z1,zc+i+1)
25
As an analogue of Lemma 2, we let
RM2(z1,z 2) = 1
2
[
log
(
1−e
−2πi
(
M2
N + 1
2
−1
)
+2πiz1+2πiz2
)
− log
(
1−e
−2πi
(
M2
N + 1
2
−1
)
+2πiz2
)
− log
(
1−e−2πiz2
)
+ log
(
1−e−2πiz1−2πiz2
)
− log
(
1−e−2πiz1
)]
(71)
Following the proof of Lemma 2, we have
Lemma 5. On any compact subset of
{(z1,z 2,...,z c+d+1)∈ C| Rez1,..., Rezc+d+1 > 0, Rez1 + Rezk <s 2 for k = 2,...,c +d + 1},
we have
Φ±(s1,s2);a,c,d
M1,M2 (z1,z 2,z 3,...,z c+1,zc+2,...,z c+d+1)
= Φ±(s1,s2);a,c,d(z1,z 2,z 3,...,z c+1,zc+2,...,z c+d+1)
+ 1
N + 1
2
Ea,c,d
M2 (z1,z 2,z 3,...,z c+1,zc+2,...,z c+d+1) +O
(
1
(
N + 1
2
)2
)
, (72)
where
Ea,c,d
M2 (z1,z 2,z 3,...,z c+1,zc+2,...,z c+d+1)
=−4π2a
(
z1− 1
2
)
+
c∑
i=1
EM2(z1,zi + 1) +
d∑
i=1
RM2(z1,zc+i+1) (73)
Note that
∂
∂z1
ψi(z1,zi+1) = log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)− log(1−e2πiz1)
− 2πi(s2− 1) (74)
∂
∂zi+1
ψi(z1,zi+1) = log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)
− log(1−e2πi(s2−1)−2πizi+1)− log(1−e2πizi+1)− 2πi(s2− 1) (75)
∂
∂z1
κi(z1,zc+i+1) = log(1−e−2πi(s2−1)e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)
− log(1−e−2πiz1) + 2πi(s2− 1) (76)
∂
∂zc+i+1
κi(z1,zc+i+1) = log(1−e−2πi(s2−1)e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)
− log(1−e−2πi(s2−1)+2πizc+i+1)− log(1−e−2πizc+i+1) + 2πi(s2− 1) (77)
As a result, the critical point equations for the potential function Φ ±(s1,s2);a,c,d(z1,z 2,z 3,...,z c+d+1)
are given by
26



c∑
i=1
[
log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)− log(1−e2πiz1)
]
+
d∑
i=1
[
log(1−e−2πi(s2−1)e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)− log(1−e−2πiz1)
]
= 2πi
[
∓ (s1− 1) + (c−d)(s2− 1)− 2a
(
z1− 1
2
)]
log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)
− log(1−e2πi(s2−1)−2πizi+1)− log(1−e2πizi+1)
= 2πi(s2− 1) for i = 1, 2,...,c
log(1−e−2πi(s2−1)e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)
− log(1−e−2πi(s2−1)+2πizc+i+1)− log(1−e−2πizc+i+1)
=−2πi(s2− 1) for i = 1, 2,...,d
(78)
(79)
(80)
Put Zi = e2πizi, Ui = 1
Z1Zi+1
and Bl = e2πisl for i = 1, 2,...,c +d and l = 1, 2. After taking
exponential, we have





c∏
i=1
(1−B2Ui)
(
1− 1
Ui
)
B2 (1−Z1)




d∏
i=1
(
1−B−1
2 U−1
i+c
)
(
1− 1
U−1
i+c
)
B−1
2
(
1−Z−1
1
)


(Z2
1)a =B∓
1
(1−B2Ui)
(
1− 1
Ui
)
(1− B2
Zi+1
)(1−Zi+1)
=B2 for i = 1, 2,...,c
(1−B−1
2 U−1
c+i)
(
1− 1
U−1
c+i
)
(1− B−1
2
Z−1
c+i
)(1−Z−1
c+i)
=B−1
2 for i = 1, 2,...,d
(81)
(82)
(83)
3.2 Asymptotics of JN,N (Wa,1,c,d, e
2πi
N + 1
2 )
When M1 =M2 =N, the potential function becomes
Φ(1,1);a,c,d(z1,z 2,z 3,...,z c+d+1)
= 1
2πi
(
a
(
2πi
(
z1− 1
2
))2)
+
c∑
i=1
ψ(1,1)
i (z1,zi+1) +
d∑
i=1
κ(1,1)
i (z1,zc+i+1)
27
Besides, the critical point equations of the potential function are given by



c∑
i=1
[
log(1−e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)− log(1−e2πiz1)
]
−
d∑
i=1
[
log(1−e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)− log(1−e−2πiz1)
]
=−4πia(z1− 1
2)
log(1−e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)− log(1−e−2πizi+1)− log(1−e2πizi+1)
= 0 for i = 1, 2,...,c
log(1−e2πiz1+2πizc+i+1) + log(1−e−2πiz1−2πizc+i+1)− log(1−e2πizi+1)− log(1−e−2πizc+i+1)
= 0 for i = 1, 2,...,d
(84)
(85)
(86)
It is straightforward to verify that ( z1,z 2,...,z c,zc+1,...,z c+d+1) =
( 1
2, 1
4,..., 1
4
)
is a solution of equa-
tions (84) - (86). Besides, it is the unique maximum point on the region
D ={(z1,...,z c+d+1)∈ [0, 1]c+d+1|z1 +zi≤ 1 for i = 2,...,c +d + 1}
Moreover, since
ψ(1,1)
i
(1
2, 1
4
)
= 1
2πi [2 Li2(i)− 2 Li2(−i) + Li2(−1)] = 1
2π
[
8L
(π
4
)
+ π2i
12
]
(87)
κ(1,1)
i
(1
2, 1
4
)
= 1
2πi [2 Li2(i)− 2 Li2(−i)− Li2(−1)] = 1
2π
[
8L
(π
4
)
− π2i
12
]
(88)
the critical value is given by
Φ(1,1);a,c,d
(1
2, 1
4,..., 1
4
)
= 1
2πi
c∑
i=1
ψi
(1
2, 1
4
)
+ 1
2πi
d∑
i=1
κi
(1
2, 1
4
)
= 1
2π
[
8(c +d)L
(π
4
)
+ (c−d)π2i
12
]
Besides, by Lemma A.3 of [18], we have
exp
(
−φh
( π
2N + 1
))
∼
N→∞
e−πi
4 (N + 1
2)− 1
2 exp
(N + 1
2
2π
π2i
6
)
(89)
exp
(
φh
(
π− π
2N + 1
))
∼
N→∞
e
πi
4 (N + 1
2)− 1
2 exp
(N + 1
2
2π
(−π2i
6
))
(90)
Nevertheless, the Hessian of Φ (1,1);a,c,d( 1
2, 1
4,..., 1
4) is given by
Hess
(
Φ(1,1);a,c,d
(1
2, 1
4,..., 1
4
))
= 2πi


(c +d)i− c−d
2 + 2a i i i ... i
i 2i 0 0 ... 0
i 0 2 i 0 ... 0
...
i 0 0 ... 0 2 i


For anya1,a 2,a 3∈ C, one can verify that the determinant of the ( c +d + 1)× (c +d + 1) matrix


a1 a2 a2 a2 ... a 2
a2 a3 0 0 ... 0
a2 0 a3 0 ... 0
... ... ... ... ...
a2 0 0 0 ... 0
a2 0 0 0 ... a 3


28
is given by ⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
a1 a2 a2 a2 ... a 2
a2 a3 0 0 ... 0
a2 0 a3 0 ... 0
... ... ... ... ...
a2 0 0 0 ... 0
a2 0 0 0 ... a 3
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
=ac+d−1
3 [a1a3− (c +d)a2
2]
In particular, if we put a1 = (c +d)i− c−d
2 + 2a,a 2 =i and a3 = 2i, one can show that
det
(
− Hess
(
Φ(1,1);a,c,d
(1
2, 1
4,..., 1
4
)))
⁄= 0
for anya∈ Z,c,d ∈ N∪{0} withc+d≥ 1. Theorem 4 then follows by similar argument as in Section 2.2.
3.3 Triangulation of the S3\W0,1,c,0
The triangulation of S3\WL 0,1,c,0 is similar to that for the Whitehead link complement. First of all, we
prepare c ideal octahedra. Next, we glue the top of the cylinder to the bottom of the next cylinder by
the rule C2→C1 and A2→A1 (Figure 14), then we obtain a decomposition of the boundary torus into
paralleograms. Note that this torus is exactly the boundary torus of a tubular neighborhood of the belt
component of WL 0,1,c,0.
Figure 14: decomposition of the boundary torus into parallelograms
Originally, each tetrahedron has its own assignment of shape parameters Z1 = e2πiz1,Wi = e2πizi+1
and Ui = 1
Z1Wi
. If we put z1 = z2 =··· = zc+1 = z, w1 = w1 =··· = wc+1 = w and u1 = u2 =··· =
uc+1 = u, by similar calculation in Section 2.4, one can verify that the edges equations can be reduced
to a single equation
(U′
W′
)( (B2U)′′
(B−1
2 W )′′
)
= 1 (91)
29
On the other hand, the critical point equations for the potential function Φ(1,1);0,c,0(z1,z 2,z 3,...,z c+1)
are given by



c∑
i=1
[
log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)− log(1−e2πiz1)
]
= 2πi [− (s1− 1) +c(s2− 1)]
log(1−e2πi(s2−1)e−2πiz1−2πizi+1) + log(1−e2πiz1+2πizi+1)
− log(1−e2πi(s2−1)−2πizi+1)− log(1−e2πizi+1)
= 2πi(s2− 1) for i = 1, 2,...,c
(92)
(93)
By similar argument in Section 2.4, one can show that the holonomy of the meridian of the belt component
and the holonomy of the longitude of every clasps components are exactly B1 and B2 respectively.
Theorem 5 then follows from similar arguments in Section 2.3-2.4.
4 Volume conjecture for T Vr(Wa,b,c,d, e
2πi
r ) with b≥ 1
Let r = 2N + 1. Recall from Theorem 1 that the r-th Turaev-Viro invariants for the link complement
S3\L is related to the colored Jones polynomials of the link as follows:
TVr
(
S3\L,e
2πi
r
)
= 2n−1
(2 sin(2π
r )√r
)2 ∑
1≤⃗M≤r−1
2
⏐⏐⏐⏐J⃗M
(
L,e
2πi
N + 1
2
)⏐⏐⏐⏐
2
,
From the formula of J⃗M(Wa,b,c,d,e
2πi
N + 1
2 ), it is easy to see that the colored Jones polynomials of the belt
tangle and twist tangle grow at most polynomially. Thus, in order to ﬁnd an upper bound for the expo-
nential growth rate ofJ⃗M(Wa,b,c,d,e
2πi
N + 1
2 ), we only need to ﬁnd that for the clasp tangle ˜C(n,e
2πi
N + 1
2 ;M2).
Lemma 6. For any n∈{ 1, 2,...,M − 1}, l∈{ 1, 2,...,M − 1−n}, let
cM(n,l ;t) =
n∏
j=1
⏐⏐⏐⏐
(1−tM−l−j)(1−tl+j)
1−tj
⏐⏐⏐⏐
For each M, let nM∈{ 1, 2,...,M − 1} and lM∈{ 1, 2,...,M − 1−n} such that cM(nM,lM) achieves
the maximum among all cM(n,l ). Assume that M
N+ 1
2
→s∈ [0, 1], nM
N+ 1
2
→ns and lM
N+ 1
2
→ls. Then we
have
lim
N→∞
1
N + 1
2
log(cM(n,l ;e
2πi
N + 1
2 ))≤ Vol(S3\WL )
2π
Furthermore, the equality holds if and only if s = 1,ns = 1
2 and ls = 1
4.
Proof. Deﬁne
f(x,y,s ) = 1
π [Λ(πs−πx−πy)− Λ(πs−πy) + Λ(πy)− Λ(πx +πy) + Λ(πx)],
where ∆s ={(x,y,s )∈ R3| 0≤x,y≤π, 0≤x +y≤s,s∈ [0, 1]}. One can show that when
s = lim
N→∞
M
N + 1
2
,x = lim
N→∞
n
N + 1
2
and y = lim
N→∞
l
N + 1
2
,
we have
lim
N→∞
1
N + 1
2
log(cM(n,l ;e
2πi
N + 1
2 )) =f(x,y,s )
In order to ﬁnd out the maximum of f inside the region ∆s, we will ﬁrst ﬁnd out all the critical point of
f on ∆s, and then estimate the value of f along the boundary. Note that



fx = log|2 sin(πs−πx−πy)| + log|2 sin(πx +πy)|− log|2 sin(πx)|
fy = log|2 sin(πs−πx−πy)|− log|2 sin(πs−πy)|− log|2 sin(πy)| + log|2 sin(πx +πy)|
fs =− log|2 sin(πs−πx−πy)| + log|2 sin(πs−πy)|
(94)
(95)
(96)
30
1. To ﬁnd out the critical point of f, note that
fs = 0 =⇒ log|2 sin(πs−πx−πy)| = log|2 sin(πs−πy)| (97)
=⇒ x = 0 or x + 2y = 2s− 1 (98)
By putting (97) into the equation fy = 0, we get x = 0 or x + 2y = 1. As a result, fy = fs = 0
imply x = 0 or s = 1. In both cases, the critical point lies on the boundary.
2. To estimate the value of f along the boundary, note that
(a) on the boundary where s = 1, (x,y,s ) =
( 1
2, 1
4, 1
)
is a unique maximum point with maximum
valuef
( 1
2, 1
4, 1
)
= 1
2π Vol(S3\WL ).
(b) on the boundary where x = 0, we have f(0,y,s ) = 0.
(c) when y = 0 or x +y =s, the function f is given by



f(x, 0,s ) = 1
π [Λ(πs−πx)− Λ(πs)]
f(x,s−x,s ) = 1
π [Λ((πy)− Λ(πs)]
In both cases, we have
|f|≤ 1
π
[
2Λ
(π
3
)]
≤ 1
2π
[
6Λ
(π
3
)]
= 1
2π Vol(S3\41)< 1
2π Vol(S3\WL )
where the last inequality follows from the fact that the ﬁgure eight knot complement can be obtained
by doing surgery along the belt component of the Whitehead link. This completes the proof.
From Theorem 1 and Lemma 6, we can see that
lim sup
r→∞
r odd
2π
r log
(
TVr(S3\Wa,b,c,d,e
2πi
r )
)
≤ (c +d) Vol(S3\WL ) = Vol(S3\Wa,b,c,d) (99)
Besides, from Theorem 1 and Theorem 4, for r = 2N + 1, since
2π
r log
(
TVr(S3\Wa,b,c,d,e
2πi
N + 1
2 )
)
≥ 2π
r log
⏐⏐⏐J⃗N
(
(S3\Wa,1,c,d,e
2πi
r )
)⏐⏐⏐
2
(100)
and
lim
N→∞
2π
2N + 1 log
⏐⏐⏐⏐J⃗N
(
(S3\Wa,1,c,d,e
2πi
N + 1
2 )
)⏐⏐⏐⏐
2
= Vol(S3\Wa,1,c,d) =v3||S3\Wa,b,c,d||, (101)
Corollary 2 follows from squeeze theorem.
References
[1] J. E. Andersen and S. K. Hansen, ‘Asymptotics of the quantum invariants for surgeries on the ﬁgure
8 knot’, J. Knot Theory Ramiﬁcations 15 (2006) 479-548
[2] Q. Chen and T. Yang, ‘Volume conjectures for the Reshetikhin-Turaev and the Turaev-Viro invari-
ants’, Quantum Topology, 9 (2018) no. 3, 419-140.
[3] Francesco Costantino, ‘6j-symbols, hyperbolic structures and the volume conjecture’ Geom. Topol.,
Volume 11, Number 3 (2007), 1831-1854.
[4] Jinseok Cho, Jun Murakami, and Yoshiyuki Yokota, ‘The complex volumes of twist knots’ Pro-
ceedings of the American Mathematical Society, Volume 137, Number 10, October 2009, Pages
35333541
[5] R. Detcherry, E.Kalfagianni and T.Yang, ‘Turaev-Viro invariants, colored Jones polynomials and
volume’, Quantum Topol. 9 (2018) 775
31
[6] L. Faddeev, ‘Discrete Heisenberg-Weyl group and modular group’, Lett. Math. Phys. 34 (1995), no.
3, 249254.
[7] L. Faddeev, R. Kashaev and A. Volkov, ‘Strongly coupled quantum discrete Liouville theory, I’,
Algebraic approach and duality. Comm. Math. Phys. 219 (2001), no. 1, 199219.
[8] Sergei Gukov, ‘Three-dimensional quantum gravity, Chern-Simons theory, and the A polynomial’,
Commun.Math.Phys. 255 (2005), 577-627.
[9] Sergei Gukov, Hitoshi Murakami, ‘SL(2, C) Chern-Simons theory and the asymptotic behavior of
the colored Jones polynomial, H. Lett Math Phys (2008) 86: 79. https://doi.org/10.1007/s11005-
008-0282-3
[10] R. M. Kashaev, ‘The hyperbolic volume of knots from the quantum dilogarithm’, Lett. Math. Phys.
39(1997) 269-275
[11] F. Luo, T. Yang ‘Volume and rigidity of hyperbolic polyhedral 3-manifolds’, Journal of Topology,
11(2018) 1-29
[12] H. Murakami and Y. Yokota, ‘The colored Jones polynomials of the ﬁgure eight knot and its Dehn
surgery spaeces, J. reine angew. Math. 607 (2007) 47-68
[13] H. Murakami, ‘An introduction to the volume conjecture’, Interactions between hyperbolic geome-
try, quantum topology and number theory, Contemporary Mathematics 541 (American Mathemat-
ical Society, Providence, RI, 2011) I-40.
[14] H. Murakami, ‘The coloured Jones polynomial, the Chern-Simons invariant, and the Reidemeister
torsion of the ﬁgure-eight knot’, J. Topol. 6 (2013), no. 1, 193-216. MR 3029425
[15] H. Murakami and J. Murakami, ‘The colored Jones polynomials and the simplicial volume of a
knot’, Acta Math. 186 (2001) 85-104.
[16] W. Neumann and D. Zagier, ‘Volumes of hyperbolic three-manifolds’, Topology, Volume 24, Issue
3, 1985, Pages 307-332
[17] Koji Ohnuki, ‘The colored Jones polynomials of 2-bridge link and hyperbolicity equations of it’s
complements’, Journal of Knot Theory and Its Ramiﬁcations, Vol. 14, No. 6 (2005) 751771
[18] Tomotada Ohtsuki, ‘On the asymptotic expansion of the Kashaev invariant of the 5 2 knot’, Quan-
tum Topology. 7. 669-735.
[19] Tomotada Ohtsuki and Yoshiyuki Yokota, ‘On the asymptotic expansion of the Kashaev invariant
of the knots with 6 crossings’, Mathematical Proceedings of the Cambridge Philosophical Society,
165(2), 287-339. doi:10.1017/S0305004117000494
[20] Tomotada Ohtsuki, ‘On the asymptotic expansions of the Kashaev invariant of hyperbolic knots
with seven crossings’, International Journal of Mathematics, Vol. 28, No. 13, 1750096 (2017)
[21] William P. Thurston, ‘The geometry and topology of three-manifolds’, Princeton Univ. Math. Dept.
Notes, 1979, Available at http://www.msri.org/communications/books/gt3m.
[22] Roland Van Der Veen, ‘Proof of the volume conjecture for Whitehead chains’, ACTA MATHE-
MATICA VIETNAMICA, Volume 33, Number 3, 2008, pp. 421-431
[23] Ka Ho Wong and Thomas Kwok-Keung Au, ‘Asymptotic Behavior of the Colored Jones polynomials
and Turaev-Viro Invariants of the ﬁgure eight knot’, to appear in Algebraic & Geometric Topology
[24] Ka Ho Wong and Tian Yang, ‘On the Volume Conjecture for hyperbolic Dehn-ﬁlled 3-manifolds
along the ﬁgure-eight knot’, https://arxiv.org/pdf/2003.10053.pdf
[25] Hao Zheng, ‘Proof of the Volume Conjecture for Whitehead Doubles of a Family of Torus Knots’
Chinese Annals of Mathematics, Series B, 2007, 375-388
32
