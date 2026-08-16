---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-050-334-asymptotic-behavior-in-diﬀerent-grading-conv
section_title: "Asymptotic behavior in diﬀerent grading conventions"
section_number: 3.3.4
pages: 46-49
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
It is instructive to study the asymptotic behavior of the col ored superpolynomial and its
specialization (3.11) in diﬀerent grading conventions. For example, another popular set of
grading conventions is the one where diﬀerentials dN <0 have degree ( −2, 2N, 2N − 1), see
(3.54). One important lesson of this exercise will be the fac t that the limit (2.5) has to be
– 45 –
slightly modiﬁed depending on which grading conventions on e chooses. Conceptually, and
also as a simple way to remember which limit to take, one wants
qβtγ =eℏ → 1, (3.181)
where the exponents β and γ represent the degree 11 of the colored diﬀerential, cf. (3.9),
deg(dcolored) = (0 ,β,γ ). (3.182)
Indeed, with the reﬁned volume conjectures (2.1) and (2.6) w e wish to probe the “large
volume” asymptotics of the homological knot invariantsPn(q,t ), asn goes to inﬁnity. On the
other hand, as we explained in section 3.1.3, the dependence of homological knot invariants
on the “color” R = Sn−1 is controlled by the colored diﬀerentials which (in the basic case)
change the value of n by one unit, see e.g. (3.87).
Therefore, in order to study the asymptotic behavior of the h omological knot invariants
under n → n + 1 for suﬃciently large n, one needs to take a limit in which discrete values
of n are replaced by a continuous variable x = eu and diﬀerent terms in the chain complex
(3.94) are clumped together in a continuous distribution, d escribed by S0(u,t ). Therefore,
this continuous limit is precisely the limit in whichdcolored changes gradings by a tiny amount,
i.e. the limit (3.181).
For example, in the grading conventions of [27], the ﬁrst col ored diﬀerential listed in
(3.54) has (a,q,t )-degree (0, 2, 2). Therefore, the right limit to take in this case is the limi t
(3.181) with β = 2 and γ = 2 or, more precisely,
q2t2 =eℏ → 1, t = ﬁxed, x ≡eu =enℏ = ﬁxed. (3.183)
In order to make this a little bit more concrete and to underst and the issue better, let
us illustrate how it all works in the large class of examples a ssociated with (2, 2p + 1) torus
knots. We already computed the colored superpolynomial (3.68) for these knots in the grading
conventions of [27], and now to study its asymptotic behavio r we will need a couple of useful
identities. First, applying the Euler-Maclaurin formula [ 60]:
N∑
m=M
f(m) =
∫ N
M
f(t)dt + 1
2(f(N) +f(M)) +
n∑
k=1
B2k
(2k)!
{
f (2k−1)(N)
}
−
∫ N
M
B2n(t)
(2n)! f (2n)(t)dt. (3.184)
to the function f(m) = log
(
1 −X(q2t2)m)
, we ﬁnd
log(X;q2t2)∞ = 1
ℏ +ǫLi2(X) + 1
2 log(1 −X) +
∞∑
k=1
B2k
(2k)!
U2k−1(X)
(1 −X)2k−1 (ℏ +ǫ)2k−1(3.185)
11For simplicity, here we assume that the a-degree of dcolored is equal to zero, as for the ﬁrst set of colored
diﬀerentials in (3.54).
– 46 –
where we temporarily introduced ǫ := logt. In particular for X =e
s
ℏ , one ﬁnds the following
expansion:
log(X;q2t2)∞ = −s
2 ℏ2 −iπsℏ + π2
3 + O(e−ℏs), (3.186)
which we can apply to our result for the superpolynomial (3.6 8) or, to be more precise, to its
specialization (3.91) at a =q2.
First, let us see what would happen if, instead of the correct limit (3.183) that comes
from the gradings of colored diﬀerentials, we naively used th e limit (2.5) (suitable for the
homological invariants in the grading conventions of [44], where deg(dcolored) = (0 , 1, 0)).
We would ﬁnd that the desired specialization of the colored s uperpolynomial (3.68) can be
approximated by an integral, much like in (3.166),
P Sn−1
DGR (T 2,2p+1;a =q2,q,t ) ∼
∫
dz e
1
ℏ 2 V DGR
(2,2p+1)(z,x;t)+O(ℏ−1), (3.187)
with a very simple potential function V DGR
T 2,2p+1(z,x ;t):
V DGR
(2,2p+1)(z,x ;t) = (2 p + 1)ǫ
(
(logx)2 − (logz)2)
. (3.188)
Clearly, the critical point of this potential is z0 = 1 and, therefore, the colored superpolyno-
mial in this grading and in the limit ℏ → 0 behaves as
P Sn−1
DGR (T 2,2p+1;a =q2,q,t ) ∼ e
1
ℏ 2 V DGR
(2,2p+1)(z0,x;t). (3.189)
This behavior is way too simple to learn anything non-trivial about the “large color” behavior
of the colored superpolynomial and is not even in the expecte d form (2.6a), which is yet
another signal that one needs to be very careful passing from one set of grading conventions
to another.
Now, let us consider the asymptotic behavior of the same obje ct in the correct limit
(3.183). Again, as in (3.166), we can write
P Sn−1
DGR (T 2,2p+1;a =q2,q ;t) ∼
∫
dz e
1
ℏ
(
V DGR
(2,2p+1)(z,x,t)+O(ℏ)
)
, (3.190)
with
V DGR
(2,2p+1)(z,x ;t) = Li2(−t−1) − Li2(x) + Li2(−xt−3) + Li2(xz−1) − Li2(−xt−1z−1)
+Li2(z) − Li2(zt−2) − Li2(−xzt−3) + Li2(xzt−2) − π2
6
+(2p + 1)
[
(log(−t−2)) · (logx) + (logx)2 − (logz)2
2 −πi logz
]
+(logt) · (logz). (3.191)
– 47 –
From this potential function, the saddle point condition (3 .168) and the ﬁrst line of (3.171)
we ﬁnd the equations for the saddle point that dominates the a bove integral:
1 = (t2 −z)z−1−2p(−x +z)(t3 +xz)
t(−1 +z)(x +tz)(t2 −xz) ,
y = −t−1−4p(−1 +x)x1+2p(x +tz)(t3 +xz)
(t3 +x)(x −z)(t2 −xz) . (3.192)
Eliminating the variable z, we ﬁnd the reﬁned A-polynomial ADGR
T 2,2p+1(x,y ;t). For p = 1,
the reﬁned A-polynomial will be described in Appendix C. For t = −1 we ﬁnd the same
behavior as in the analysis of (3.170) and (3.171): the ﬁrst e quation above only speciﬁes the
valuez2p+1
0 = 1, and the second one reduces to ordinary unreﬁned A-polynomial equation for
T 2,2p+1 knot y +x2p+1 = 0.
The algebraic equations (3.192) can be easily solved around t = −1:
zj = ξj +
ξj(1 +ξj)(−2x +ξj + 2xξj +x2ξj − 2xξ2
j )
(1 + 2p)(x −ξj)(−1 +ξj)(−1 +xξj) (1 +t)
+O((1 +t)2), (3.193)
with ξj = e
2πij
2p+1 . Plugging this solution into the second equation of (3.192) , we ﬁnd the
approximate solution for y (as a function of x and t):
y = −x2p+1
[
1 + (1 +t)(−3x − 4px + 4px2 + 2ξj + 4pξj +xξj − 4pxξj + 4x2ξj + 4px2ξj
−x3ξj − 4px3ξj − 3xξ2
j − 4pxξ2
j + 4px2ξ2
j )/(−1 +x)(x −ξj)(−1 +xξj)
+O(1 +t)2
]
. (3.194)
From (2.7), one can also ﬁnd the reﬁned classical action S0(u,t ):
S0(u,t ) = S0(u) +
∞∑
a=1
(1 +t)aS(a)
0 (u),
S0(u) = 1
2(2p + 1) log(−x2p+1)2,
S(1)
