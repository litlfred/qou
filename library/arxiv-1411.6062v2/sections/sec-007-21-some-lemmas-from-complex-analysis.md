---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-007-21-some-lemmas-from-complex-analysis
section_title: "Some lemmas from complex analysis"
section_number: 2.1
pages: 7-10
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
Lemma 2.1. Let f :U→ C be an analytic function satisfying the functional equation
(26) f( z− a) f(z + a) = f( z)2,
with some ﬁxed a∈ C\{ 0}, the domain U⊂ C being a translationally invariant open set,
U = a +U, and C⊂U an oriented path such that f( z)(f(z)− f(z + a))⁄= 0 for all z∈C .
Then
(27)
∫
C
f(z) dz =
(∫
C
−
∫
a+C
) f(z)
1− f(z + a)/ f(z) dz.
Proof. We have
(28)
(∫
C
−
∫
a+C
) f(z)
1− f(z + a)/ f(z) dz =
∫
C
f(z)
1− f(z + a)/ f(z) dz
−
∫
a+C
f(z)
1− f(z)/ f(z− a) dz =
∫
C
f(z)− f(z + a)
1− f(z + a)/ f(z) dz =
∫
C
f(z) dz.
□
Given a rational function r( z)∈ C(z), a nonzero complex number q∈ C\{ 0} and an
integer k we deﬁne r k(z; q)∈ C(z), k∈ Z, by:
(29) rk+1(z; q)
rk(z; q) = r(zq k), r0(z; q) = 1 .
Note that
(30) r 1(z; q) = r( z)
and
(31) r k+l(z; q) = r k(zq l; q) rl(z; q) = r l(zq k; q) rk(z; q) ,
for all integers k, l . In particular, in the case of roots of unity this implies a quasi-period icity
property:
(32) r k+N (z; q) = r k(z; q) rN (z; q), if qN = 1,
8 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
and the invariance property
(33) r N (zq; q) = r N (z; q), if qN = 1.
Let ( M, N ) be an admissible pair, and recall b and s from Equation (
11). Choose two
integers P and Q which satisfy the equation M P + N Q = 1. Let f( z) be a meromorphic
function and g ±(z)∈ C(z) two rational functions such that
(34) f(z + b±1i)
f(z) = g ±
(
e2πb±1z
)
.
Then, for k∈ /CI we have
(35) g ±
k
(
e2πb±1z; q±
)
= f(z + b±1ik)
f(z) ,
and, in particular,
(36) g +
N
(
e2πbz; q+
)
= f(z + biN)
f(z) = f(z + si)
f(z) = f(z + b−1iM)
f(z) = g –
M
(
e2πb−1z; q−
)
.
Deﬁne
g(x) = g +
N
(
x
1
N ; q+
)
= g –
M
(
x
1
M ; q−
)
(37)
S(x, y ) =
s2−1∑
k=0
g+
kP (x; q+) g–
kQ(y; q−)(38)
Lemma 2.2. (a) We have g( x)∈ C(x) and S( x, y )∈ C(x, y ).
(b) The function S( x, y ) is independent of P and Q provided xN = yM .
Proof. Since
(39) g +
N (xq+; q+) = g +
N (x; q+) , g–
M (xq−; q−) = g –
M (x; q−) ,
it follows that g( x)∈ C(x), and consequently, S( x, y )∈ C(x, y ).
For (b), let P ′, Q ′ be another pair satisfying the equation M P′ + N Q′ = 1. Then there
exists an integer R such that P ′ = P + RN and Q′ = Q− RM . Denoting the function (
38)
with P and Q replaced by P ′ and Q′ as S ′(x, y ), we have
S′(x, y ) =
s2−1∑
k=0
g+
kP ′(x; q+) g–
kQ′(y; q−) =
s2−1∑
k=0
g+
kP +kRN (x; q+) g–
kQ−kRM (y; q−)
=
s2−1∑
k=0
g+
kP (x; q+) g+
N (x; q+)kR g–
kQ(y; q−) g–
M (y; q−)−kR
=
s2−1∑
k=0
g+
kP (x; q+)
(g+
N (x; q+)
g– M (y; q−)
) kR
g–
kQ(y; q−) =
s2−1∑
k=0
g+
kP (x; q+) g–
kQ(y; q−)
= S(x, y )
where we used the second equality in ( 37). □
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 9
For a complex number x, we denote Cx = xi/ s + R⊂ /BV .
Lemma 2.3. Let f( z), g( z), S( x, y ) be as above and λ a real number in general position
such that the form f( z) dz is absolutely integrable along Cλ,
(40) lim
x→±∞
sup
y∈[ λ
s , λ
s +s]
| f(x + iy)| = 0,
and
(41) g(0) ⁄= 1⁄= g(∞) .
Then the following equalities hold
∫
Cλ
f(z) dz =
(∫
Cλ
−
∫
Cλ +1
) f(z) S
(
e2πbz, e 2πb−1z
)
1− g(e2πsz) dz(42)
= 2πi
∑
0<sImα−λ<1
Resz=α
f(z) S
(
e2πbz, e 2πb−1z
)
1− g(e2πsz) .
Proof. Let us derive the ﬁrst equality. We denote
(43) q± = e2πib±2
,
so that we have
(44) q+ = e2πi M
N , q − = e2πi N
M .
We also have
(45) f( z + kb±1i) = f( z) g±
k
(
e2πb±1z; q±
)
, ∀k∈ Z.
In particular,
(46) f( z + si) = f( z + Nbi) = f( z + Mb−1i) = f( z) g
(
e2πsz)
.
The function
(47) h( z) = f
( z
2πs
)
has the properties
(48) h(z + k2πi)
h(z) = g +
P k
(
ez/N; q+
)
g–
Qk
(
ez/M ; q−
)
, ∀k∈ Z.
From equation ( 48), it follows that
(49)
s2−1∑
k=0
h(z + k2πi)
h(z) = S
(
ez/N , e z/M)
.
10 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
As λ is generic, the contour Cλ satisﬁes the conditions of Lemma
2.1 with a = si. Thus, we
write
(50)
∫
Cλ
f(z) dz =
(∫
Cλ
−
∫
si+Cλ
) f(z)
1− g(e2πsz) dz
=
(∫
Cλ 2π s
−
∫
C(λ +s2)2π s
)
h(z)
1− g(ez)
dz
2πs
=
s2−1∑
k=0
(∫
C(λ +k)2π s
−
∫
C(λ +k+1)2π s
)
h(z)
1− g(ez)
dz
2πs
=
s2−1∑
k=0
(∫
Cλ 2π s
−
∫
C(λ +1)2π s
)
h(z + k2πi)
1− g(ez)
dz
2πs
=
(∫
Cλ 2π s
−
∫
C(λ +1)2π s
)
h(z) S
(
ez/N, e z/M)
1− g(ez)
dz
2πs
=
(∫
Cλ
−
∫
Cλ +1
) f(z) S
(
e2πbz, e 2πb−1z
)
1− g(e2πsz) dz.
The second equality in Equation ( 42) follows from the residue theorem. To justify its
application note that Cλ−C λ+1 union two vertical segments is the boundary of a disk.
Conditions ( 40), ( 41) imply that for suﬃciently large negative or positive x the integrand in
last part of ( 50) is regular on the vertical segment C′ = x + i[λ, λ + 1]/ s and the following
estimate holds⏐
⏐
⏐
⏐
⏐
⏐
∫
C′
f(z) S
(
e2πbz, e 2πb−1z
)
1− g(e2πsz) dz
⏐
⏐
⏐
⏐
⏐
⏐
≤
s2−1∑
k=0
∫ λ+1
λ
⏐
⏐
⏐
⏐
⏐
f
(
x + i y+k
s
)
1− g(e2π(sx+iy))
⏐
⏐
⏐
⏐
⏐
dy
s
≤ 1
s
s2−1∑
k=0
sup
y∈[λ,λ+1]
⏐
⏐
⏐
⏐
⏐
f
(
x + i y+k
s
)
1− g(e2π(sx+iy))
⏐
⏐
⏐
⏐
⏐
≤ 1
s sup
y∈[λ,λ+1]
1
|1− g(e2π(sx+iy))|
s2−1∑
k=0
sup
t∈[λ,λ+1]
⏐
⏐
⏐
⏐f
(
x + i t + k
s
) ⏐
⏐
⏐
⏐
≤ s
supz∈x+i[ λ
s , λ
s +s]|f(z)|
inf |w|=e2π sx|1− g(w)|
|x|→∞
−−−−→0
□
