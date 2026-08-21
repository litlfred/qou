---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-046-0-xy-ax-by-xy-1
section_title: "(x,y ) = ax +by −xy + 1"
section_number: 0
pages: 60-62
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
4π2
(
Li2(e2πi(x+y)) −Li2(e2πi(x−y))
)
,
Asymptotics of the quantum invariants for the ﬁgure 8 knot 61
wherea,b are certain integers. If we put Ψ = Ψ a,b
0 , then by (4.40) ( x,y ) is a critical
point of Ψ if and only if
0 = 2 πi(a −y) + Log(1 −zw) − Log(1 −zw −1),
0 = 2 πi(b −x) + Log(1 −zw) + Log(1 −zw −1), (C.2)
where z =e2πix and w =e2πiy as usual, and this set of equations implies that
w −z = 1 −zw,
(1 −zw)(w −z) = zw, (C.3)
compare with (4.41) and (4.42). We note that the ﬁrst of these equ ations is equiv-
alent to
w − 1 = z(1 −w)
so w = 1 or z = −1. For z = −1 we get w2 + 3w + 1 = 0 so w = −3±
√
5
2 .
Forw = 1 we ﬁnd that z2 − 3z + 1 = 0 so z = 3±
√
5
2 . However, only the point
(z,w ) = ((3 −
√
5)/2, 1) satisﬁes that zw,zw −1 /∈ [1, ∞[. For this point we ﬁnd that
y ∈ Z and from (C.2) we get that y =a. But then
Ψ(x,y ) = ax +by −xy + 1
4π2 (Li2(z) − Li2(z)) = yx +ba −xy =ba ∈ Z.
Let ¯ρθ,ε be the nonabelian SU(2)–representations of π from Proposition 2, where
θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and ε ∈ {±} . Here ¯ρθ,ε and ¯ρ−θ,ε are conjugate. By
(5.65) ¯ρθ,ε extends to a representation of π1(M0) if and only if
Lε(θ) = 1.
But this happens if and only if θ = ±1/4 for both ε = + and ε = −, i.e. the
set of conjugacy classes of nonabelian representations of π1(M0) into SU(2) is{
[ ¯ρ1/4,−], [ ¯ρ1/4,+]
}
.
By (5.77) the ﬂat reducible SU(2)–connections on M0 all have a Chern–Simons
invariant equal to zero, so we conclude that the image set of the SU (2) Chern–
Simons functional on M0 has at most three elements. By [18, Theorem 5.6 and
precedent text] we can therefore conclude that the set of Cher n–Simons invariants
of ﬂat SU(2)–connections on M0 is
{
0 mod Z, − 1
5 mod Z, 1
5 mod Z
}
. (C.4)
In particular, the set of Chern–Simons invariants of [ ¯ ρ1/4,+] and [ ¯ρ1/4,−] is equal
to
{
− 1
5 mod Z, 1
5 mod Z
}
. We note that (C.1) and (C.4) prove the AEC for the
invariantsτr(M0).
By (5.70) and (5.71) we have β±(1/4) = f±, where f− = 0 and f+ = 1. By
Proposition 4 and (5.71) we ﬁnd
CS(¯ρ1/4,±) = ± 1
6 − 1
π
∫ 1/4
1/6
Arg(L±(t))dt (mod Z),
62 Asymptotics of the quantum invariants for the ﬁgure 8 knot
where we use that L±(t) ∈S1. By (5.90) we have
∫ 1/4
1/6
Arg(L−(t))dt = −
∫ 1/4
1/6
Arg(L+(t))dt
so we ﬁnally get
CS(¯ρ1/4,±) = ±
(
1
6 − 1
π
∫ 1/4
1/6
Arg(L+(t))dt
)
(mod Z).
Note that Im(L+(t))< 0 on ]1/6, 1/4[ so
− 1
12 = 1
π (−π)(1/4 − 1/6)< 1
π
∫ 1/4
1/6
Arg(L+(t))dt< 0.
Therefore
1/6 − 1
π
∫ 1/4
1/6
Arg(L+(t))dt ∈] 1
6, 1
4 [.
Since this value mod Z belongs to the set {±1/5 mod Z} we conclude that it is equal
to 1/5 so
1
π
∫ 1/4
1/6
Arg(L−(t))dt = − 1
π
∫ 1/4
1/6
Arg(L+(t))dt = 1
