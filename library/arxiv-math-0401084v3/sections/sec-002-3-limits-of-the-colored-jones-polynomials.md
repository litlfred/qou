---
doc_id: arxiv-math-0401084v3
doc_title: "THE COLORED JONES POL YNOMIALS OF THE"
section_id: sec-002-3-limits-of-the-colored-jones-polynomials
section_title: "Limits of the colored Jones polynomials"
section_number: 3
pages: 4-14
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
doc_brief: "THE COLORED JONES POLYNOMIALS OF THE — W e calculate limits of the colored Jones polynomials of the ﬁ gure- eight knot and conclude that in most cases they determine the volumes and the Chern–Simons"
---
K. Habiro [2] and T. Le showed that the colored Jones polynomial JN (E; t) of
the ﬁgure-eight knot E is given as follows (see also [6]).
(3.1) JN (E; t) =
N −1∑
n=0
n∏
k=1
tN(
1 − t−N −k)(
1 − t−N +k)
.
We will study the asymptotic behavior of JN (E; qr) with qr := exp(2 πr√−1/N)
for large N .
We approximate∏ n
k=1
(
1 − q−N ±k
r
)
by an integral. Note that
n∏
k=1
(
1 − q−N ±k
r
)
= exp
{
N
2π
n∑
k=1
2π
N log
(
1 − exp(±2πkr
√
−1/N − 2πr
√
−1)
)
}
.
Lemma 3.1. If r ⁄∈R then
log
⏐
⏐
⏐1 − e2πb/N
⏐
⏐
⏐ ≤ log
⏐
⏐1 − exp
(
sr
√
−1 − 2πr
√
−1
)⏐
⏐ ≤ log
(
1 + e2πb)
,
and
log
⏐
⏐1 − e2πb⏐
⏐ ≤ log
⏐
⏐1 − exp
(
−sr
√
−1 − 2πr
√
−1
)⏐
⏐ < log
(
1 + e4π |b|
)
where r = a + b√
−1 with a ∈ R, 0 ⁄= b ∈ R and 0 ≤ s ≤ 2π − 2π/N.
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 5
Proof. If we put r := a + b√−1 with b ⁄= 0, we have
exp
(
sr
√
−1 − 2πr
√
−1
)
= e−bs+2πb exp
(
(as − 2πa)
√
−1
)
.
Therefore
⏐
⏐1 − exp
(
sr√
−1 − 2πr√−1
)⏐
⏐ is smaller (greater, respectively) than or
equal to the longest (shortest, respectively) distance between 1 ∈ C and the circle
centered at 0 with radius e−bs+2πb . So if b > 0,
1 + e2πb ≥
⏐
⏐1 − exp
(
sr
√
−1 − 2πr
√
−1
)⏐
⏐ ≥ e−b(2π −2π/N )+2πb − 1 = e2πb/N − 1
and if b < 0,
1 + e2πb ≥
⏐
⏐1 − exp
(
sr
√
−1 − 2πr
√
−1
)⏐
⏐ ≥ 1 − e2πb/N .
Similarly if b > 0,
e2πb − 1 ≤
⏐
⏐1 − exp
(
−sr
√
−1 − 2πr
√
−1
)⏐
⏐ ≤ eb(2π −2π/N )+2πb + 1 < e 4πb + 1
and if b < 0,
1 − e2πb ≤
⏐
⏐1 − exp
(
−sr
√
−1 − 2πr
√
−1
)⏐
⏐ ≤ e4πb −2πb/N + 1 ≤ e2πb + 1.
□
We put
ϕN, ±(n) :=
n∑
k=1
2π
N log
(
1 − exp(±2πkr
√
−1/N − 2πr
√
−1)
)
−
∫ 2πn/N
0
log
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
ds.
Lemma 3.2. If r ⁄∈R, then there exist constants d ≥ 1 and δ > 0 such that
|Re ϕN, +(n)| < 2πd
N
{
log
(
1 + e2πb)
− log
(2π|b|δ
N
)}
and
|Re ϕN, −(n)| < 2πd
N
{
log
(
1 + e4π |b|
)
− log
⏐
⏐1 − e2πb⏐
⏐
}
for suﬃciently large N .
Proof. First we note that if a real continuous function g(s) (0 ≤ s ≤ A) has c
extremes, then
⏐
⏐
⏐
⏐
⏐
∫ nA/N
0
g(s) ds −
n∑
k=1
A
N g(kA/N)
⏐
⏐
⏐
⏐
⏐ ≤ (2c + 1) A
N
(
max
0≤s≤A
g(s) − min
0≤s≤A
g(s)
)
.
This is because if g is monotonic in [ jA/N, (j + l)A/N]
⏐
⏐
⏐
⏐
⏐
⏐
∫ (j+l)A/N
jA/N
g(s) ds −
j+l∑
k=j+1
A
N g(kA/N)
⏐
⏐
⏐
⏐
⏐
⏐
≤ A
N |g(jA/N ) − g((j + l)A/N)| ≤ A
N
(
max
0≤s≤A
g(s) − min
0≤s≤A
g(s)
)
and there are c + 1 such intervals. For other c intervals [jA/N, (j + 1)A/N] clearly
⏐
⏐
⏐
⏐
⏐
∫ (j+1)A/N
jA/N
g(s) ds − A
N g((j + 1)A/N)
⏐
⏐
⏐
⏐
⏐ ≤ A
N
(
max
0≤s≤A
g(s) − min
0≤s≤A
g(s)
)
holds.
6 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
Therefore from Lemma 3.1 there exists a constant d such that
|Re ϕN, +(n)| ≤ 2πd
N
{
log
(
1 + e2πb)
− log
⏐
⏐
⏐1 − e2πb/N
⏐
⏐
⏐
}
and
|Re ϕN, −(n)| < 2πd
N
{
log
(
1 + e4π |b|
)
− log
⏐
⏐1 − e2πb⏐
⏐
}
Since if b > 0,
e2πb/N − 1 = 2πb
N + (2πb)2
2N 2 + · · · > 2πb
N
for any N and if b < 0,
1 − e2πb/N = − 2πb
N − (2πb)2
2N 2 − · · · > − 2πbδ
N
for any 0 < δ < 1 if N is suﬃciently large. This completes the proof. □
Therefore we have
D−1N −d <
⏐
⏐
⏐
⏐exp
( N
2π ϕN, ±(n)
)⏐
⏐
⏐
⏐ < DN d
for some constants D > 0 and d ≥ 1 for suﬃcient large N .
We also have
Lemma 3.3. If r ⁄∈R, then for any positive number ε
|Im ϕN, ±(n)| < ε
for suﬃciently large N .
Proof. Clearly
max
2π/N ≤s≤2π −2π/N
arg
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
− min
2π/N ≤s≤2π −2π/N
arg
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
is bounded by a positive constant depending only r. So we can show as in the
previous lemma that
|Im ϕN, ±(n)| =
⏐
⏐
⏐
⏐
⏐
n∑
k=1
2π
N arg
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
−
∫ 2πn/N
0
arg
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
⏐
⏐
⏐
⏐
⏐
is bounded by a positive constant times 1 /N and the result follows. □
Putting
χN, ±(n) := exp
( N
2π ϕN, ±(n)
)
,
we have
n∏
k=1
(
1 − q−N ±k
r
)
= χN, ±(n) exp
{
N
2π
∫ 2πn/N
0
log
(
1 − exp(±sr
√
−1 − 2πr
√
−1)
)
ds
}
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 7
with D−1N −d < |χN, ±(n)| < DN d and | arg χN, ±(n)| < ε if r ⁄∈R. Therefore
n∏
k=1
(
1 − q−N ±k
r
)
= χN, ±(n) exp
{
±N
2πr√−1
∫ exp(±2πnr √−1/N −2πr √−1)
exp(−2πr √−1)
log(1 − u)
u du
}
= χN, ±(n) exp
{ ±N
2πr√−1
(
Li2
(
m−2)
− Li2
(
q±n
r m−2))}
.
Here we put
m := exp(πr
√
−1)
and
Li2(z) := −
∫ z
0
log(1 − u)
u du
is the dilogarithm function.
Thus we have
JN (E; qr)
=
N −1∑
n=0
qN n
r
n∏
k=1
(
1 − q−N +k
r
)(
1 − q−N −k
r
)
=
N −1∑
n=0
qN n
r χN, +(n) exp
{ N
2πr√−1
(
Li2
(
m−2)
− Li2
(
qn
r m−2))}
× χN, −(n) exp
{ −N
2πr√−1
(
Li2
(
m−2)
− Li2
(
q−n
r m−2))}
=
N −1∑
n=0
χN (n) exp
{ N
2πr√−1
(
Li2
(
q−n
r m−2)
− Li2
(
qn
r m−2)
+
(
log (−qn
r ) + π
√
−1
)
(log m2
)}
=
N −1∑
n=0
χN (n) exp
{ N
2πr√−1 H
(
qn
r , m2)}
,
where we put
H(ξ, η) := Li 2
(
ξ−1η−1)
− Li2
(
ξη −1)
+
(
log(−ξ) + π
√
−1
)
log η
and χN (n) := χN, +(n)χN, −(n). Note that D−2N −2d < |χ(n)| < D 2N 2d. Note also
that we use log( −ξ) + π√−1 instead of log ξ since we choose the branch of log as
(0, +∞) and that of Li 2 as (1 , +∞).
Let Ψ N (z) be an analytic function such that Ψ N
(
exp(2πn√−1/N)
)
= χN (n),
that P (N −1) < |Ψ N (z)| < Q (N ) with some polynomials P and Q, and that
| arg Ψ N (z)| < ε near C deﬁned below. Since the residue around z = exp(2πn√−1/N)
of 1 /
(
z(1 − z−N )
)
is 1 /N, we have from the residue theorem
JN (E; qr) = 1 + N
2π√−1
∫
C
Ψ N (z)
z(1 − z−N ) exp
( N
2πr√−1 H(zr, m2)
)
dz,
8 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
where C = C+∪C− is deﬁned by









C+ := {z ∈ C | |z| = 1 + κ, π/N ≤ arg z ≤ 2π − π/N}
∪
{
t exp(√
−1/N) ∈ C | 1 − κ ≤ t ≤ 1 + κ
}
∪
{
t exp(−√−1/N) ∈ C | 1 − κ ≤ t ≤ 1 + κ
}
C− := {z ∈ C | |z| = 1 − κ, π/N ≤ arg z ≤ 2π − π/N}
for small κ > 0. Now we have
JN (E; qr)
= 1 + N
2π√−1
∫
C+
Ψ N (z)
z exp
( N
2πr√−1 H(zr, m2)
)
dz
+ N
2π√−1
∫
C+
Ψ N (z)
z(1 − z−N ) exp
( N
2πr√−1
{
H(zr, m2) − 2π
√
−1 log zr})
dz
+ N
2π√−1
∫
C−
Ψ N (z)
z(zN − 1) exp
( N
2πr√−1
{
H(zr, m2) + 2π
√
−1 log zr})
dz.
Here we want to apply the steepest descent method (or the saddle point method,
see for example [5, Theorem 7.2.9])
Theorem 3.4 (Steepest Descent Method) . Let Γ : [ a, b] → C be a C1 curve. Let
h(z) be a continuous function on Γ that is analytic at z0 = Γ( t0), and gN (z) be
a continuous function on z ∈ Γ for each N = 1 , 2, 3, . . . with gN (z0) ⁄= 0 such
that |gN (z)| < N p for some p > 0. We also assume the following conditions: For
suﬃcient large integer N ,
(1)
∫
Γ gN (z) exp
(
N h(z)
)
dz converges absolutely.
(2) d h(z0)/dz = 0 and d2 h(z0)/dz2 ⁄= 0.
(3) Im
(
N h(z)
)
is constant for z on c in some neighborhood of z0.
(4) Re
(
N h(z)
)
takes its strict maximum along Γ at z0.
Then ∫
Γ
gN (z) exp
(
N h(z)
)
dz ∼
N →∞
√
2πgN (z0) exp
(
N h(z0)
)
√
N
√
−d2 h(z0)/dz2
for appropriate chosen square roots. Here ∼
N →∞
means the ratio of both hand sides
goes to 1 when N → ∞.
Remark 3.5. In [5, Theorem 7.2.9] it is assumed that gN (z) does not depend on
N but the result is also true if we assume that |gN (z)| grows polynomially. See
Exercises 8 and 10 in Section 7.3 of [5].
Putting h(z) := 1
2πr √−1 H(zr, m2), g(z) := Ψ N (z)/z, we can prove the following
proposition.
Proposition 3.6. We have
∫
C+
Ψ N (z)
z exp
( N
2πr√−1 H(zr, m2)
)
dz
∼
N →∞
√
2πΨ N (y1/r )
r
√
N
√
y − y−1 exp
( N
2πr√−1 H(y, m2)
)
with
y := m4 − m2 + 1 −
√
(m2 + m + 1)(m2 + m − 1)(m2 − m + 1)(m2 − m − 1)
2m2 ,
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 9
where the branch of the square root in the deﬁnition of y is taken so that if m = −1,
then y = exp(−π√−1/3). Note that y satisﬁes the following equality:
(3.2) y + y−1 = m2 − 1 + m−2.
Proof. First of all we calculate derivatives of H(zr, m2). We have
∂ H (zr, m2)
∂z = ∂ H (ξ, η)
∂ξ
d zr
dz
= rz r−1
zr
{
log(1 − z−rm−2) + log(1 − zrm−2) + log m2}
= r
z log
(
m2 − (zr + z−r) + m−2)
and
∂2 H(zr, m2)
∂z 2
= − r
z2 log
(
m2 − (zr + z−r) + m−2)
+ r
z × −rz r−1 + rz −r−1
m2 − (zr + z−r + m−2) .
Therefore y1/r gives a solution to ∂ H (zr, m2)/∂z = 0, and
∂2 H(zr, m2)
∂z 2
⏐
⏐
⏐
⏐
⏐
z=y1/r
= r2y−2/r (−y + y−1).
Now we will consider the case when r = 1 precisely. In this case y = exp(−π√
−1/3).
We change C+ to C′+ where
C′+ := {z ∈ C | |z| = 1, π/N ≤ arg z ≤ 2π − π/N}
∪
{
t exp(
√
−1/N) ∈ C | 1 − κ ≤ t ≤ 1
}
∪
{
t exp(−
√
−1/N) ∈ C | 1 − κ ≤ t ≤ 1
}
.
Then on the unit circle
H(exp(θ
√
−1), 1) = Li 2(exp(−θ
√
−1)) − Li2(exp(θ
√
−1))
=
{ π2
6 − 2π − θ
2
(
π − 2π − θ
2
)
+ 2
√
−1 L
(2π − θ
2
)}
−
{ π2
6 − θ
2
(
π − θ
2
)
+ 2
√
−1 L
(θ
2
)}
= −4
√
−1 L
(θ
2
)
.
(3.3)
Here we use the following formula:
(3.4) Li 2
(
exp(β
√
−1)
)
= π2
6 − β
2
(
π − β
2
)
+ 2
√
−1 L
(β
2
)
for 0 ≤ β ≤ 2π and the fact that L is an odd function with period π. (See for
example [9, p. 18].) So on C′+ Im H(z, 1) takes its maximum at y and near y
Re H(z, 1) = 0. Moreover in this case
∂2 H(z, 1)
∂z 2
⏐
⏐
⏐
⏐
⏐
z=y
= −3 −
√
3√−1
2 ⁄= 0.
Therefore we can apply the saddle point method and the proposition follows when
r = 1.
If r is near 1 we can also apply the saddle point method similarly from the
continuity of H(zr, m2) with respect to r, completing the proof. □
10 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
From Lemma 3.7 below we see
⏐
⏐
⏐
⏐
⏐
∫
C+
Ψ N (z)
z(1 − z−N ) exp
( N
2πr√−1
{
H(zr, m2) − 2π
√
−1 log zr})
dz
⏐
⏐
⏐
⏐
⏐
≤
∫
C+
|Ψ N (z)|
|z(1 − z−N )| exp
( N
2π Im
(H(zr, m2) − 2π√−1 log zr
r
))
|dz|
< exp
( N
2π Im
(H(y, m2)
r
))∫
C+
|Ψ N (z)|
|z(1 − z−N )| |dz|
≤ exp
( N
2π Im
(H(y, m2)
r
)) |C+|Q(N )
(1 + κ) (1 − (1 + κ)−N )
and
⏐
⏐
⏐
⏐
⏐
∫
C−
Ψ N (z)
z(zN − 1) exp
( N
2πr√−1
{
H(zr, m2) + 2π
√
−1 log zr})
dz
⏐
⏐
⏐
⏐
⏐
< exp
( N
2π Im
(H(y, m2)
r
)) |C−|Q(N )
(1 − κ) (1 − (1 − κ)N ) ,
where |C±| is the length of C±. Now we have
log
(
JN (E; qr)
)/
N − H(y, m2)
2πr√−1 − log
( √
2πΨ N (y1/r )
r
√
N
√
y − y−1
)/
N
= log
(
r
√
N
√
y − y−1
√
2πΨ N (y1/r ) exp
( −N
2πr√−1 H(y, m2)
)
+ N
2π√−1
∫
C+
Ψ N (z)
z exp
(
N
2πr √−1 H(zr, m2)
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
)
+ N
2π√−1
∫
C+
Ψ N (z)
z(1−z− N ) exp
(
N
2πr √−1 H(zr, m2) − 2π√−1 log zr
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
)
+ N
2π√−1
∫
C−
Ψ N (z)
z(zN −1) exp
(
N
2πr √−1 H(zr, m2) + 2π√−1 log zr
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
)
)/
N.
(3.5)
We will estimate each term in log. First we observe that
⏐
⏐
⏐
⏐
⏐
r
√
N
√
y − y−1
√
2πΨ N (y1/r ) exp
( −N
2πr√−1 H(y, m2)
)⏐
⏐
⏐
⏐
⏐
= |r|
√
N |
√
y − y−1|√
2π
⏐
⏐Ψ N (y1/r )
⏐
⏐ exp
(
−N Re
(H(y, m2)
2πr√−1
))
goes to 0. This is because P (N −1) < |Ψ N (y1/r )| < Q (N ) for polynomials P and
Q, and Re
(
H(y, m2)/2πr√−1
)
> 0 if r is near 1 since when r = 1
H(y, m2)
2πr√−1 = H(exp(−π√−1/3), 1)
2π√−1 = 2 L(π/6)
π > 0
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 11
from (3.3). Next we have
lim
N →∞
∫
C+
Ψ N (z)
z exp
(
N
2πr √−1 H(zr, m2)
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
) = 1,
⏐
⏐
⏐
⏐
⏐
⏐
⏐
N
2π√−1
∫
C+
Ψ N (z)
z(1−z− N ) exp
(
N
2πr √−1 H(zr, m2) − 2π√−1 log zr
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
< |rN 3/ 2√
y − y−1||C+|Q(N )
(2π)3/ 2|Ψ N (y1/r |)(1 + κ) (1 − (1 + κ)−N )
< |rN 3/ 2√
y − y−1||C+|Q(N )(1 + N κ)
(2π)3/ 2P (N −1))(1 + κ)N κ
and ⏐
⏐
⏐
⏐
⏐
⏐
⏐
N
2π√−1
∫
C−
Ψ N (z)
z(zN −1) exp
(
N
2πr √−1 H(zr, m2) + 2π√−1 log zr
)
dz
√
2π Ψ N (y1/r )
r
√
N
√
y−y− 1 exp
(
N
2πr √−1 H(y, m2)
)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
< |rN 3/ 2√
y − y−1||C−|Q(N )
(2π)3/ 2|Ψ N (y1/r |)(1 − κ) (1 − (1 − κ)N )
< |rN 3/ 2√
y − y−1||C−|Q(N )
(2π)3/ 2P (N −2)(1 − κ)(κ + (N − 1)κ2/2) .
So we see that the absolute values of the ﬁrst, third, and fourth t erms in log in
(3.5) are smaller than a polynomial in N . Therefore (3.5) goes to 0 when N → ∞
and so we have
lim
N →∞
log
(
JN (E; qr)
)
N
= H(y, m2)
2πr√−1 + lim
N →∞
log
( √
2πΨ N (y1/r )
r
√
N
√
y − y−1
)
/
N
= H(y, m2)
2πr√−1 + lim
N →∞
log
⏐
⏐Ψ N (y1/r )
⏐
⏐
N +
√
−1 lim
N →∞
arg Ψ N (y1/r )
N
= H(y, m2)
2πr√−1
since P (N −1) < |Ψ N (y1/r )| < Q(N ) and | arg Ψ N (y1/r )| < ε.
Lemma 3.7. There exists a neighborhood U ′ of 1 ∈ C such that if r∈U ′,
(3.6) Im
(
H
(
zr, m2)
∓ 2π√−1 log zr
r
)
< Im
(H(y, m2)
r
)
for z ∈ C±.
Proof. We will show that the inequality holds when r = 1. Then from the com-
pactness of C± and the continuity we see that there exists such a neighborhood U ′
of 1.
Put
h∓(z) := H(z, 1) ∓ 2π
√
−1 log z − H
(
exp(−π
√
−1/3), 1
)
= Li 2(1/z) − Li2(z) ∓ 2π
√
−1 log z − Li2
(
eπ √−1/ 3
)
+ Li2
(
e−π √−1/ 3
)
.
12 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
and we regard it as a function of ρ and θ with z = ρ exp(θ√
−1); that is
h∓(ρ, θ) = Li 2
(
ρ−1e−θ√−1
)
− Li2
(
ρeθ√−1
)
± 2πθ ∓ 2π
√
−1 log ρ
− Li2
(
eπ √−1/ 3
)
+ Li2
(
e−π √−1/ 3
)
.
We also put {
D+ := {z ∈ C | |z| ≥ 1},
D− := {z ∈ C | |z| ≤ 1}.
We will show that Im h∓(ρ, θ) on D± takes its unique maximum 0 at exp(−π√−1/3).
Since
∂ h∓(ρ, θ)
∂θ =
√
−1 log
(
1 − ρ−1e−θ√−1
)
+
√
−1 log
(
1 − ρeθ√−1
)
± 2π,
we have
∂ Im h∓(ρ, θ)
∂ θ = log
⏐
⏐
⏐
⏐
(
1 − ρ−1e−θ√
−1
)(
1 − ρeθ√−1
)⏐
⏐
⏐
⏐.
Since
⏐
⏐
⏐
(
1 − ρ−1e−θ√
−1
)(
1 − ρeθ√−1
)⏐
⏐
⏐
2
=
(
1 + ρ−2 − 2ρ−1 cos θ
)(
1 + ρ2 − 2ρ cos θ
)
=
(
ρ + ρ−1 − 2 cos θ
)2
,
Im h∓(ρ, θ) takes its maximum at θ = 2 π − arccos
(ρ + ρ−1 − 1
2
)
for a ﬁxed ρ if
(
3 −
√
5
)
/2 < ρ <
(
3 +
√
5
)
/2.
Now we put θ(ρ) := 2 π−arccos
(ρ + ρ−1 − 1
2
)
and denote h∓(ρ, θ(ρ)) by h∓(ρ).
Since
∂ h∓(ρ, θ)
dρ = 1
ρ
{
log
(
1 − ρ−1e−θ√−1
)
+ log
(
1 − ρeθ√−1
)
∓ 2π
√
−1
}
and
d θ(ρ)
dρ = 1 − ρ−2
2 sin θ(ρ)
we have
d h∓(ρ)
dρ =
{ 1
ρ +
√−1(1 − ρ−2)
2 sin θ(ρ)
}
×
{
log
((
1 − ρ−1e−θ(ρ)√−1
)(
1 − ρeθ(ρ)√−1
))
∓ 2π
√
−1
}
.
Therefore
d Im h∓(ρ)
dρ = 1
ρ
{
arg
((
1 − ρ−1e−θ(ρ)√−1
)(
1 − ρeθ(ρ)√−1
))
∓ 2π
}
+ 1 − ρ−2
2 sin θ(ρ)
{
log
⏐
⏐
⏐
⏐
(
1 − ρ−1e−θ(ρ)√
−1
)(
1 − ρeθ(ρ)√−1
)⏐
⏐
⏐
⏐
}
= 1
ρ
{
arg
((
1 − ρ−1e−θ(ρ)√−1
)(
1 − ρeθ(ρ)√−1
))
∓ 2π
}
since ⏐
⏐
⏐
⏐
(
1 − ρ−1e−θ(ρ)√
−1
)(
1 − ρeθ(ρ)√−1
)⏐
⏐
⏐
⏐ = 1.
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 13
Thus we have 






d Im h+(ρ)
dρ > 0,
d Im h−(ρ)
dρ < 0
and so Im h±(ρ) on D∓ takes maximum at ρ = 1.
Since θ(1) = −π/3, Im h∓(1) = 0. Therefore (3.6) holds when r = 1. □
Now we consider the case when r ∈ R. In this case m2 + m−2 = 2 cos(2πr) and
so
y = exp
(
−α(r)
√
−1
)
with α(r) := arccos(cos(2 πr) − 1/2) (0 ≤ arccos x ≤ π). From (3.4)
H(y, m2)
= Li 2(y−1m−2) − Li2(ym−2) +
(
log(−y) + π
√
−1
)
log m2
= Li 2
(
exp
(
α(r) − 2πr)
√
−1
))
− Li2
(
exp
(
−α(r) − 2πr)
√
−1
))
+ 2π(r − 1)(α(r) − 2π)
= π2
6 − 2π + α(r) − 2πr
2
(
π − 2π + α(r) − 2πr
2
)
+ 2
√
−1 L
(α(r) − 2πr
2
)
− π2
6 + 4π − α(r) − 2πr
2
(
π − 4π − α(r) − 2πr
2
)
− 2
√
−1 L
(−α(r) − 2πr
2
)
+ 2π(r − 1)(α(r) − 2π)
= −2π2(r − 1) + 2
√
−1
{
L
(
πr + α(r)/2
)
− L
(
πr − α(r)/2
)}
.
On the other hand from [13, Theorem 1.2]
2πr Re lim
N →∞
log JN
(
E; exp(2πr√−1/N)
)
N
= 2
{
L
(
πr + α(r)/2
)
− L
(
πr − α(r)/2
)}
if r ⁄∈Q and 5 /6 < r < 7/6, or r = 1. Moreover from its proof we see that the sign
of JN
(
E; exp(2πr√−1)/N
)
for large N is (−1)⌊N (1−r)/r ⌋, where ⌊x⌋ is the greatest
integer that does not exceed x. So
2πr Im lim
N →∞
log JN
(
E; exp(2πr√−1/N)
)
N = 2πr Im lim
N →∞
log
(
(−1)⌊N (1−r)/r ⌋)
N
= 2π2(1 − r).
Therefore we have
2πr
√
−1 lim
N →∞
log JN
(
E; exp(2πr√−1/N)
)
N = H(y, m2)
if 5 /6 < r < 7/6 and r ⁄∈Q \ {0}.
Putting
u := 2πr
√
−1 − 2π
√
−1
and
H(u) := H(y, m2),
we have proved the following theorem.
14 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
Theorem 3.8. Let E be the ﬁgure-eight knot. There exists a neighborhood U of 0
in C such that for any u ∈ (U \ π√
−1Q) ∪ {0},
(u + 2π
√
−1) lim
N →∞
log
(
JN
(
E; exp
(
u+2π √−1
N
)))
N = H(u).
