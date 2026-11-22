---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-004-3-calculation-by-the-saddle-point-method
section_title: "Calculation by the saddle point method"
section_number: 3
pages: 10-19
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Calculation by the saddle point method
In this section, we calculate Gaussian integrals by the saddle point method. We calculate
a Gaussian integral in Proposition 3.1, a Gaussian integral with perturbative terms in
Proposition 3.2, and multi-variable cases in Propositions 3.4 and 3.5. We use Proposition
3.5 in the proof of Theorem 1.1 in Section 5. For the saddle point method, see e.g. [39].
10
Proposition 3.1. For a non-zero a ∈C, the domain {z ∈C | Re az2 < 0} has two
connected components. We choose z0, z1 from the two components respectively. Let C be
a path from z0 to z1 in C. (See Figure 2.) Then, there exists ε > 0 such that
∫
C
eN·az2dz =
√π
√−a ·
√
N
+ O
(
e−εN)
,
where we choose the sign of √−a such that Re z1
√−a > 0.
We note that ε depends on z0, z1 and a.
z0
z1
−
1
√−a
1
√−a
C
Figure 2: The domain {z ∈C | Re az2 < 0} is shaded.
Proof. By replacing z with z/√−a, we can reduce the proof to the case where a = −1.
Putting a = −1, we show that
∫z1
z0
e−Nz2dz =
√π
√
N
+ O(e−εN).
Since
∫∞
−∞e−Nz2dz = √π/
√
N, it is suﬃcient to show that
∫z0
−∞
e−Nz2dz = O(e−εN),
∫∞
z1
e−Nz2dz = O(e−εN).
We show the latter formula. (The former formula can be shown similarly.) The latter
formula is calculated,
∫∞
z1
e−Nz2dz =
∫Re z1
z1
e−Nz2dz +
∫∞
Re z1
e−Nz2dz,
and the two terms of the right-hand side are estimated,

∫Re z1
z1
e−Nz2dz

 ≤
∫Re z1
z1
|e−Nz2| · |dz| ≤
∫Re z1
z1
e−NRe z2|dz|
≤
∫Re z1
z1
e−NRe z2
1|dz| = |Im z1| · e−NRe z2
1 = O(e−εN),
11
0 ≤
∫∞
Re z1
e−Nz2dz ≤
∫∞
Re z1
e−N(Re z1)zdz = e−N(Re z1)2
N · Re z1
= O(e−εN)
for some ε > 0. Hence, we obtain the required formula.
We generalize Proposition 3.1 to the case where there are perturbative terms in the
exponential of the integrand.
Proposition 3.2. Let a be a non-zero complex number, and let ψ(z) and r(z) be holo-
morphic functions of the forms,
ψ(z) = az2 + r(z),
r(z) = b3z3 + b4z4 + · · · ,
deﬁned in a neighborhood of 0. The domain
{
z ∈C

 Re ψ(z) < 0
}
(15)
has two connected components in a neighborhood of 0. We choose z0, z1 from these two
components respectively. Let C be a path from z0 to z1 in C. (See Figure 3.) Then,
∫
C
eN ψ(z)dz =
√π
√−a ·
√
N
(
1 +
d
∑
k=1
λk
N k + O
(
1
N d+1
))
,
for any d, where we choose the sign of √−a similarly as in Proposition 3.1, and λk’s
are constants given by using coeﬃcients of the expansion of ψ(z); such presentations are
obtained by formally expanding the following formula,
1 +
∞
∑
k=1
λk
N k = exp
(
N r
( ∂
∂u
))
exp
(
−u2
4Na
)

u=0 .
(16)
In particular, λ1 is given by
λ1 = −15b2
3
16a3 + 3b4
4a2 .
z0
z1
C
Figure 3: The domain {z ∈C | Re ψ(z) < 0} is shaded.
12
Proof. We show the proposition modifying a proof of the saddle point method written
in [39].5
We show the proposition, for simplicity, putting a = −1 as in the proof of
Proposition 3.1. We put ˆr(z) = r(z)/z2. Since ˆr(z) is analytic in a neighborhood of 0,
there exists a suﬃciently small δ1 > 0 such that
ˆr(z) =
∞
∑
i=1
bk+2 zk
for |z| < δ1. Let w be a non-negative real parameter. For each ﬁxed w, we have that
ew ˆr(z) =
∞
∑
k=0
Pk(w) zk
for |z| < δ1, where Pk(w) is a polynomial in w of degree ≤k. Since ˆr(0) = 0, there exist
small δ2 > 0 and ε1 > 0 such that |ˆr(x)| ≤ε1 for −δ2 ≤x ≤δ2; we can further assume
that ε1 < 1 and δ2 ≤δ1. For each ﬁxed integer m > 0, we can put
ew ˆr(x) =
m
∑
k=0
Pk(w) xk + Rm xm+1
(17)
for −δ2 ≤x ≤δ2 and any w ≥0, where Rmxm+1 is the error term, which is estimated by
|Re Rm| ≤
max
|x| ≤δ2

 Re dm+1
dxm+1 ew ˆr(x) 

 ,
|Im Rm| ≤
max
|x| ≤δ2

 Im dm+1
dxm+1 ew ˆr(x) 

 .
Further, since
dm+1
dxm+1 ew ˆr(x) = ew ˆr(x) ·
(
polynomial in w and diﬀerentials of ˆr(x) of degree ≤m+1
)
,
we have that
|Rm| ≤eε1wK1(wm+1 + 1) ≤K2 eε2w
(18)
for some K1, K2 > 0 and ε2 < 1, which are independent of x and w (noting that m is
bounded by using d later). Further, we replace the path C with the union of a path C1
from z0 to −δ, a path C2 from −δ to δ along the real axis, and a path C3 from δ to z1.
We can assume that there exist suﬃciently small δ, ε3 > 0 such that δ ≤δ2 and C1 and
C3 are in the domain
{
z ∈C

 Re ψ(z) ≤−ε3
}
.
(19)
Then, the integral of the proposition is given by
∫
C
eN ψ(z)dz =
∫
C1
eN ψ(z)dz +
∫
C2
eN ψ(z)dz +
∫
C3
eN ψ(z)dz.
(20)
5As for the 1-variable case, a proof of a more general statement of the saddle point method is written in [39], though
the multi-variable case is not written in [39]. We review (a simpler modiﬁcation of) the proof of [39], in order to generalize
it to the multi-variable case later (Proposition 3.5).
13
Since C1 and C3 are in the domain (19), we have that
∫
C1
eN ψ(z)dz = O(e−Nε3)
and
∫
C3
eN ψ(z)dz = O(e−Nε3).
(21)
Hence, it is suﬃcient to show that the integral along C2 gives the required formula.
The integral along C2 is calculated as
∫
C2
eN ψ(z)dz =
∫δ
−δ
eN ψ(x)dx =
∫δ
−δ
e−Nx2eNx2ˆr(x)dx
=
2d+1
∑
k=0
∫δ
−δ
Pk(Nx2) xke−Nx2dx +
∫δ
−δ
R2d+1 x2d+2e−Nx2dx,
(22)
by (17), putting w = Nx2 and m = 2d + 1. When k is odd, the summand of the ﬁrst
term of (22) is equal to 0, since the integrand is an odd function. When k is even, the
summand of the ﬁrst term of (22) is given by a sum of integrals of the following form,
∫δ
−δ
(Nx2)l xke−Nx2dx =
∫∞
−∞
N lx2l+ke−Nx2dx + O(e−Nε4)
=
1
N k/2√
N
∫∞
−∞
y2l+ke−y2dx + O(e−Nε4)
= (2l + k −1)!! · √π
2l+k/2N k/2√
N
+ O(e−Nε4),
for some ε4 > 0, where we obtain the ﬁrst equality in a similar way as in the proof of
Proposition 3.1, and obtain the second equality putting y =
√
Nx. Hence, the ﬁrst term
of (22) is given by the following form,
√π
√
N
(
1 +
d
∑
k=1
λk
N k
)
+ O(e−Nε4).
Further, by (18) putting w = Nx2, the second term of (22) is estimated by

∫δ
−δ
R2d+1 x2d+2e−Nx2dx

 ≤
∫δ
−δ
|R2d+1| x2d+2e−Nx2dx
≤K2
∫δ
−δ
x2d+2e−(1−ε2)Nx2dx = O
(
1
N d+ 3
2
)
,
where we obtain the last equality in a similar way as the above calculation. Hence, by
(22),
∫
C2
eN ψ(z)dz =
√π
√
N
(
1 +
d
∑
k=1
λk
N k + O
(
1
N d+1
))
.
Therefore, by (20) and (21), the integral of the proposition is given by the following form,
∫
C
eN ψ(z)dz =
√π
√
N
(
1 +
d
∑
k=1
λk
N k + O
(
1
N d+1
))
.
14
In particular, λ1 is concretely calculated by reﬁning the above calculation, as follows.
Since
ˆr(z) = b3z + b4z2 + · · · ,
we have that
ew ˆr(z) = 1 + wˆr(z) + 1
2w2ˆr(z)2 + · · · = 1 + b3wz +
(b3
2 w2 + b4w)z2 + · · · .
Hence,
∫
C
eN ψ(z)dz =
∫∞
−∞
e−Nx2(
1 + b3Nx2 · x +
(b2
3
2 (Nx2)2 + b4Nx2)
x2 + · · ·
)
dx
=
√π
√
N
(
1 +
(15
16b2
3 + 3
4b4
) 1
N + O
( 1
N 2
))
.
This is the required formula for d = 1 when a = −1.
We obtain a concrete presentation of any λk by the following formal calculation. Noting
that
zm =
( ∂
∂u
)m euz

u=0 ,
we have that
∫
eNaz2zmdz =
∫( ∂
∂u
)m eNaz2+uz

u=0 dz
=
∫( ∂
∂u
)m exp
(
Naw2 −u2
4Na
)

u=0 dw
=
√π
√−a ·
√
N
·
( ∂
∂u
)m exp
(
−u2
4Na
)

u=0 ,
which can be justiﬁed by a similar calculation as above, to be precise. Hence, putting
exp
(
N r(z)
)
= ∑
m ˜bmzm,
∫
eN ψ(z)dz =
∫
eNaz2 exp
(
N r(z)
)
dz
=
∫
eNaz2( ∑
m
˜bmzm)
dz
=
√π
√−a ·
√
N
·
∑
m
˜bm
( ∂
∂u
)m exp
(
−u2
4Na
)

u=0
=
√π
√−a ·
√
N
· exp
(
N r
( ∂
∂u
))
exp
(
−u2
4Na
)

u=0 ,
and this gives (16). By expanding this formula formally, we obtain concrete presentations
of λk’s in terms of coeﬃcients of the expansion of ψ(z).
15
Remark 3.3. We can extend Proposition 3.2 to the case where ψ(z) depends on N in
such a way that ψ(z) is of the form
ψ(z) = ψ0(z) + ψ1(z) 1
N + ψ2(z) 1
N 2 + · · · + ψm(z) 1
N m + rm(z)
1
N m+1 ,
(23)
where ψi(z)’s are holomorphic functions independent of N, and we assume that ψ0(z)
satisﬁes the assumption of the proposition and |rm(z)| is bounded by a constant which is
independent of N. Then, eNψ(z) = ϕ(z)eNψ0(z), where we put
ϕ(z) = exp
(
ψ1(z) + ψ2(z) 1
N + · · · + ψm(z)
1
N m−1 + rm(z) 1
N m
)
= ϕ0(z) + ϕ1(z) 1
N + ϕ2(z) 1
N 2 + · · · + ϕm−1(z)
1
N m−1 + ˜rm(z) 1
N m.
Here, ˜rm(z) is the error term such that |˜rm(z)| is bounded by a constant which is indepen-
dent of N. As written in [39], in the same way as in the proof of Proposition 3.2, we can
show the asymptotic expansion of
∫
ϕi(z)eNψ0(z)dz by expanding ϕi(z) at z = 0. Further,
we can estimate
∫
˜rm(z)eNψ0(z)dz similarly as in the proof of Proposition 3.2, noting that
only values of ˜rm(z) in a suﬃciently small neighborhood of 0 contribute to the resulting
expansion. In this way, we can justify the statement of Proposition 3.2 in the case where
ψ(z) depends on N as in the form (23).
We generalize Proposition 3.1 to the case of n variables.
Let A be a non-singular
symmetric complex n×n matrix, and let z be a column vector (z1, · · · , zn)T ∈Cn. The
domain
{
z ∈Cn 

 Re zTA z < 0
}
(24)
is homotopy equivalent to Sn−1. Let D be an oriented n-ball embedded in Cn such that
∂D is included in the domain (24), whose inclusion is homotopy equivalent. There exists
a matrix P such that −A = P TP; we note that det P = ±
√
det(−A). We choose an
n-ball as a neighborhood of the origin in Rn ⊂Cn. The matrix P −1 takes this n-ball
to an n-ball satisfying the above assumption of D. We choose the sign of
√
det(−A) by
setting it to be det P if P takes the orientation of D to the standard orientation of Rn,
and −det P otherwise.
Proposition 3.4. Let A, D be as above. Then, there exists ε > 0 such that
∫
D
eN·zTA zdz =
πn/2
N n/2√
det(−A)
+ O
(
e−εN)
,
where we put dz = dz1 · · · dzn, and we choose the sign of
√
det(−A) as above.
Proof. By changing the coordinate of z linearly, we can reduce the proof to the case where
A is a diagonal matrix. Further, since d(eN·zTA zdz) = 0, we can move the domain D in
Cn by Stokes’ theorem; we can also move ∂D in the domain (24) ignoring error terms of
order e−Nε for some ε > 0 as in the proof of Proposition 3.1. In this way, we can move D
into Rn ⊂Cn, which means that we can reduce the proof to the product of copies of the
formula of Proposition 3.1.
16
We generalize Proposition 3.4 to the case where there are perturbative terms in the
exponential of the integrand.
Proposition 3.5. Let A be a non-singular symmetric complex n×n matrix, and let ψ(z)
and r(z) be holomorphic functions of the forms,
ψ(z) = zTA z + r(z),
r(z) = r(z1, · · · , zn) = ∑
i,j,k bijkzizjzk + ∑
i,j,k,l cijklzizjzkzl + · · · ,
(25)
deﬁned in a neighborhood of 0 ∈Cn. The restriction of the domain
{
z ∈Cn 

 Re ψ(z) < 0
}
(26)
to a neighborhood of 0 ∈Cn is homotopy equivalent to Sn−1. Let D be an oriented n-ball
embedded in Cn such that ∂D is included in the domain (26) whose inclusion is homotopic
to a homotopy equivalence to the above Sn−1 in the domain (26). Then,
∫
D
eN ψ(z)dz =
πn/2
N n/2√
det(−A)
(
1 +
d
∑
i=1
λi
N i + O
(
1
N d+1
))
,
for any d, where we choose the sign of
√
det(−A) as in Proposition 3.4, and λi’s are
constants given by using coeﬃcients of the expansion of ψ(z); such presentations are
obtained by formally expanding the following formula,
1 +
∞
∑
i=1
λi
N i = exp
(
N r
( ∂
∂u1
, · · · , ∂
∂un
))
exp
(
−1
4N uTA−1u
)

u=0 .
(27)
In particular, λ1 is given by
λ1 =
−1
28 · 3
∑
i1,i2,··· ,i6
σ∈S6
bi1i2i3bi4i5i6aiσ(1)iσ(2)aiσ(3)iσ(4)aiσ(5)iσ(6) + 1
32
∑
i1,i2,i3,i4
τ∈S4
ci1i2i3i4aiτ(1)iτ(2)aiτ(3)iτ(4) ,
where Sn is the nth symmetric group, and we put
(
aij
)
i,j = A−1.
Proof. Similarly as in the proof of Proposition 3.4, we can reduce the proof to the case
where A = −E, where E denotes the identity matrix of size n. Then, the integral of the
problem is rewritten,
∫
D
eN·zT z exp
(
N r(z)
)
dz,
(28)
where we can let D be a suﬃciently small neighborhood of 0 in Rn as in the proof of
Proposition 3.4. The second exponential in the integrand of (28) is calculated as
exp
(
N r(z)
)
= 1 + N r(z) + 1
2N 2r(z)2 + · · ·
= 1 + N
∑
i,j,k
bijkzizjzk + N
∑
i,j,k,l
cijklzizjzkzl
+ 1
2N 2 ∑
i1,i2,··· ,i6
bi1i2i3bi4i5i6zi1zi2zi3zi4zi5zi6 + · · · .
17
Hence, we can calculate the asymptotic expansion of the integral (28) similarly as the
calculation of λ1 in the proof of Proposition 3.2, and we can show that the asymptotic
expansion of (28) is given by the following form,
∫
D
eN ψ(z)dz =
πn/2
N n/2
(
1 + λ1
N + λ2
N 2 + · · ·
)
.
We estimate the remaining part “· · · ” of the above formula as in the proof of Propo-
sition 3.2, as follows. We can put
r(z) =
∑
i,j
zizjˆrij(z)
for some ˆrij(z) which satisﬁes that ˆrij(z) = ˆrji(z). Let wij be non-negative real parameters,
and put w = (wij). For each ﬁxed w, we have that
exp
( ∑
i,j
wijˆrij(z)
)
=
∞
∑
k=0
∑
i1,··· ,ik
Pi1···ik(w) zi1 · · · zik
for suﬃciently small z, where Pi1···ik(w) is a polynomial in wij’s of degree ≤k. Further,
for each ﬁxed integer m > 0, we can put
exp
( ∑
i,j
wijˆrij(x)
)
=
m
∑
k=0
∑
i1,··· ,ik
Pi1···ik(x) xi1 · · · xik +
∑
j1,··· ,jm+1
Rj1···jm+1xj1 · · · xjm+1
where Rj1···jm+1xj1 · · · xjm+1 is the error term. Similarly as in the proof of Proposition 3.2,
we can estimate it by
|Rj1···jm+1| ≤K exp
( ∑
i,j
εijwij
)
for some K > 0 and εij > 0 which satisﬁes that εij = εji and E−(εij) is positive deﬁnite.
Further, similarly as in the proof of Proposition 3.2, putting m = 2d + 1, we can show
that the error term is of order O(1/N n/2+d+1). Hence, we can show that the integral of
the problem has the asymptotic expansion of the required formula.
We obtain concrete presentations of λk’s by the following formal calculation. Noting
that
zi1 · · · zim =
∂
∂ui1
· · ·
∂
∂uim
euT z

u=0
we have that
∫
eN·zTA zzi1 · · ·zimdz =
∫
∂
∂ui1
· · ·
∂
∂uim
eN·zTA z + uT z

u=0 dz
=
∫
∂
∂ui1
· · ·
∂
∂uim
exp
(
N · wTA w −1
4N uTA−1u
)

u=0 dw
=
πn/2
N n/2√
det(−A)
·
∂
∂ui1
· · ·
∂
∂uim
exp
(
−1
4N uTA−1u
)

u=0 .
18
Hence, we obtain (27) from this formula similarly as in the proof of Proposition 3.2.
The above expansion is concretely calculated as
∂
∂ui1
· · ·
∂
∂ui2k
exp
(
−1
4N uTA−1u
)

u=0 =
∂
∂ui1
· · ·
∂
∂ui2k
1
k!
(
−1
4N uTA−1u
)k
=
(−1)k
k! 4kN k
∑
σ∈S2k
aiσ(1)iσ(2) · · · aiσ(2k−1)iσ(2k).
In particular, we obtain the presentation of λ1 from such calculation.
Remark 3.6. Similarly as Remark 3.3, we can extend Proposition 3.5 to the case where
ψ(z) depends on N in such a way that ψ(z) is of the form
ψ(z) = ψ0(z) + ψ1(z) 1
N + ψ2(z) 1
N 2 + · · · + ψm(z) 1
N m + rm(z)
1
N m+1 ,
(29)
where ψi(z)’s are holomorphic functions independent of N, and we assume that ψ0(z)
satisﬁes the assumption of the proposition and |rm(z)| is bounded by a constant which is
independent of N.
