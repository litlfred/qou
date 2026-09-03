---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-005-3-the-diagonal-contour-integral-method
section_title: "The diagonal (contour integral) method"
section_number: 3
pages: 8-12
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
We now apply the diagonal method, based on a complex contour integ ral. Firstly, we obtain
∮
C(0;1)
β
(
w, xξ, y
ξ
) dξ
2πiξ = α(w,xy ), (42)
for suﬃciently small x, y and w. To state it again with the detailed formula, we have
α(w,xy ) =
∮
C(0;1)
1
(
(1− (xξ +yξ −1))2− 4xy
)1/2
−w
· dξ
2πiξ . (43)
For simplicity, we will specialize this to y =x. That gives
α(w,x 2) =
∮
C(0;1)
1
(
(1−x· (ξ +ξ−1))2− 4x2
)1/2
−w
· dξ
2πiξ . (44)
This may then be further simpliﬁed as
α(w,x 2) =
∮
C(0;1)
1
((
1−x· (ξ + 2 +ξ−1)
)(
1−x· (ξ− 2 +ξ−1)
))1/2
−w
· dξ
2πiξ . (45)
8
c1 c2
a1 a2
d1 d2
b1 b2
>
Figure 2: A schematic picture – it is not to scale but it does accurately depict the order of points – for the
branch cuts and poles of the integral in (72). The conﬁgurati on of points and branch cuts is shown assuming
u,t ∈ (0, 1) are suﬃciently small. The poles are at a1(x,w ), a2(x,w ), b1(x,w ) and b2(x,w ). The branch cuts
are the intervals [c1(x),c 2(x)] and [d1(x),d 2(x)].
We will do a contour integral for ξ as in Figure 2, which requires analytically continuing this function from
ξ∈C (0; 1). The argument of the square-root in equation (45) is closely connected to the quartic function of ξ
Q1(x;ξ) =
(
ξ−x· (ξ2 + 1)
)2
− 4x2ξ2
=
(
x· (ξ2 + 1)− (1 + 2x)ξ
)(
x· (ξ2 + 1)− (1− 2x)ξ
)
.
(46)
More precisely, we can rewrite equation (45) as
α(w,x 2) =
∮
C(0;1)
1
(
Q1(x;ξ)/ξ2)1/2
−w
· dξ
2πiξ , (47)
because, for ξ⁄= 0 we have
(
1−x· (ξ + 2 +ξ−1)
)(
1−x· (ξ− 2 +ξ−1)
)
= Q1(x;ξ)
ξ2 . (48)
We will want to rationalize the denominator of the integrand. Theref ore, let us also introduce another quartic
function of ξ,
Q2(x,w ;ξ) = Q1(x;ξ)−w2ξ2
=
(
ξ−x· (ξ2 + 1)
)2
− (4x2 +w2)ξ2.
(49)
If we assume that x and w are both in [0 ,∞), then we may rewrite this as
Q2(x,w ;ξ) =
(
x· (ξ2 + 1)−
(
1 +
√
4x2 +w2
)
ξ
)(
x· (ξ2 + 1)−
(
1−
√
4x2 +w2
)
ξ
)
. (50)
Now we will begin to simplify the polynomials Q2(x;·) andQ2(x,w ;·). First we may a quick deﬁnition to set
notation.
Deﬁnition 3.1 LetU(z0;r) denote the open unit disk in the complex plane {z :|z−z0|<r}. Let
U(z0;r)
denote its closure {z :|z−z0|≤ r}.
The following four lemmas will be proved in in Appendix F. They all rely on t he quadratic formula for roots
of 1-variable quadratic equations.
9
Lemma 3.2 Suppose that we have a number x∈ (0, 1/4). Then, deﬁning
c1(x) = 1 + 2x−√1 + 4x
2x , c 2(x) = 1− 2x−√1− 4x
2x ,
d1(x) = 1− 2x +√1− 4x
2x , d 2(x) = 1 + 2x +√1 + 4x
2x ,
(51)
we have
Q1(x;ξ) = x2(
ξ−c1(x)
)(
ξ−c2(x)
)(
ξ−d1(x)
)(
ξ−d2(x)
)
. (52)
Note in particular that
c1(x)·d2(x) = c2(x)·d1(x) = 1 , (53)
which can also be seen since they are the roots of the self-inversive quadratic polynomials of ξ in the ultimate
formula in (46).
Lemma 3.3 Suppose that we have a number x∈ (0, 1/4) and another number w satisfying
0≤ w≤
√
1− 4x. (54)
Then, deﬁning
a1(x,w ) = 1 +
√
4x2 +w2−
√
1 +w2 + 2
√
4x2 +w2
2x ,
a2(x,w ) = 1−
√
4x2 +w2−
√
1 +w2− 2
√
4x2 +w2
2x ,
b1(x,w ) = 1−
√
4x2 +w2 +
√
1 +w2− 2
√
4x2 +w2
2x ,
b2(x,w ) = 1 +
√
4x2 +w2 +
√
1 +w2 + 2
√
4x2 +w2
2x ,
(55)
we have
Q2(x,w ;ξ) = x2·
(
ξ−a1(x,w )
)(
ξ−a2(x,w )
)(
ξ−b1(x,w )
)(
ξ−b2(x,w )
)
. (56)
Of course, we also have
a1(x,w )·b2(x,w ) = a2(x,w )·b1(x,w ) = 1 , (57)
because these are the roots of the self-inversive quadratic polyn omials of ξ in (49). Let us note the following
ordering of the roots for the two quartic equations, as in Figure 2.
Lemma 3.4 If we have x∈ (0, 1/4) and w∈ (0,√
1− 4x) then we have
0<a 1(x,w )<c 1(x)<c 2(x)<a 2(x,w )< 1<b 1(x,w )<d 1(x)<d 2(x)<b 2(x,w ). (58)
Let us introduce an analytic continuation of the function from (48) ,
((
1−xξ−xξ−1)
− 4x2)1/2
.
Lemma 3.5 Assume we have x∈ (0, 1/4). Deﬁne the domain D2(x) as
D2(x) = U(0;d1(x))\U(0;c1(x)). (59)
Then for all ξ∈D 2(x), we have Q1(x;ξ)/ξ2 is in D1 from Remark 2.3. So, deﬁning the function,
f (x;·) :D2(x)→ C, (60)
by the formula
f (x;ξ) =
√
Q2(x;ξ)/ξ2 =
((
1−x· (ξ +ξ−1)
)2
− 4x2)1/2
, (61)
we have that f (x;·) is analytic.
10
c1
> c2
<a1
Γ 1(δ)
>
a2
Γ 2(δ)
>
Γ 3(δ)
Figure 3: A schematic of the contours after deformation as used in the p roof of Lemma 4.1. The positively
oriented circular contours Γ 1(δ) and Γ 2(δ) are of radius δ, centered at the poles a1(x,w ) and a2(x,w ). The
branch cut along the real axis interval from c1(x) toc2(x) is enclosed by the contour Γ 3(δ) which is the rectangle
traversing the vertices: c1(x)−iδ, c2(x)−iδ, c2(x) +iδ and c1(x) +iδ, in that order.
We will prove Lemmas 3.2, 3.3, 3.4 and 3.5 in Appendix F. They are all eleme ntary, and essentially follow by
applying the quadratic formula.
We want to deform the contour from the integral in (47) as in Figure 3. For equation (47) we rationalize
the denominator. From equation (50) and Lemma 3.5, we may rewrite that equation as
α(w,x 2) =
∮
C(0;1)
ξ·f (x;ξ) +w·ξ
Q2(x,w ;ξ) · dξ
2πi. (62)
We multiplied numerator and denominator of the ﬁrst fraction by ξ2, and then canceled one power from the
numerator with the ξ that had been in the denominator of dξ/(2πiξ), which is now absent.
To deform this as in as in Figure 3, we need a more optimal analytic cont inuation of the function f (x;·).
We start with the domain as in the right-hand picture in Figure 4.
Lemma 3.6 Assume we have x∈ (0, 1/4). Deﬁne the domain D3(x) as
D3(x) = C\
(
(−∞,c 2(x)]∪ [d1(x),∞)
)
. (63)
Then deﬁne the function
g(x,·) :D3(x)→ C, (64)
by the formula
g(x;ξ) = x·
√
ξ−c1(x)·
√
ξ−c2(x)·
√
d1(x)−ξ·
√
d2(x)−ξ, (65)
where the square-root is as in Remark 2.3. Then g(x;·) is analytic and
∀ξ∈D 2(x)∩D 3(x) =
(
U(0;d1(x))\U(0;c1(x))
)
\ [−d1(x),−c1(x)], we have g(x;ξ) = ξ·f (x;ξ). (66)
Lemma 3.7 Assume we have x∈ (0, 1/4). Deﬁne the domain D4(x) as
D4(x) = C\
(
[c1(x),c 2(x)]∪ [d1(x),d 2(x)]
)
. (67)
Then deﬁne the function
~g(x;·) :D4(x)→ C, (68)
such that
∀ξ∈D 3(x) =
(
C\
(
(−∞,c 2(x)]∪ [d1(x),∞)
))
, we have ~g(x;ξ) = g(x;ξ), (69)
and
∀ξ∈ (−∞,c 1(x))∪ (d2(x),∞), we have ~g(x;ξ) = lim
ζ→ξ
ζ∈C\R
g(x;ζ). (70)
Then~g(x;·) is analytic and
∀ξ∈D 2(x), we have ~g(x;ξ) = ξ·f (x;ξ). (71)
11
c1 c2 d1 d2 c1 c2 d2d1
Figure 4: The branch cuts for the function ~g(x;·) are shown on the left, which is an analytic continuation of
the function f (x;ξ) =
√
Q1(ξ)/ξ2 deﬁned in a neighborhood of C(0; 1). In the ﬁgure on the right we show the
a priori overlapping branch-cuts of the original analytic continua tion g(x;·).
The domain for the function ~g(x;·) is as in the left-hand picture in Figure 4. We prove Lemmas 3.6 and
3.7 in Appendix G. Then equation (62) may be rewritten as
α(w,x 2) =
∮
C(0;1)
~g(x;ξ) +w·ξ
Q2(x,w ;ξ) · dξ
2πi , (72)
where the roots of Q2(x,w ;·) are a1(x;w), a2(x;w), b1(x;w) and b2(x;w), and where the domain of ~g(x;·) is
all of C except for the union of the two intervals [ c1(x),c 2(x)] and [d1(x),d 2(x)]. Thus we obtain the region
as in Figure 2. This is the region where we may deform the contour C(0; 1).
