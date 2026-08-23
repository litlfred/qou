---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-045-16-mod-z
section_title: "(mod Z),"
section_number: 16
pages: 52-60
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
CS(¯ρ1/4,−) = − 1
5 − cp
16 (mod Z).
This follows by using (C.5).
We have in the following appendices collected material of a technical n ature.
Appendix A Proofs of Lemma 1, Lemma 3 and (4.23)
Proof of Lemma 1 Let a> 0. Let ε = 1 if Im(ζ) ≥ 0 and let ε = −1 otherwise. Put
δ−
a = [ −a, √
−1εa] and δ+
a = [ √−1εa,a ]. (Here, as usual, [ z1,z 2] denotes the line
segment in C beginning at z1 and ending at z2.) We have
Sγ(ζ −γ)
Sγ(ζ +γ) = exp
(
− 1
2
∫
CR
eζz
sinh(πz)z dz
)
.
By an elementary argument one ﬁnds that the integrals
∫
δ±
a
eζz
sinh(πz)z dz converge to
zero as a → ∞. Therefore
∫
CR
eζz
sinh(πz)z dz =ε2π
√
−1
(
bε +
∞∑
n=1
Resz=ε√−1n
{ eζz
sinh(πz)z
})
,
where b1 = 0 and b−1 = Resz=0
{
eζz
sinh(πz)z
}
= ζ
π . For n ∈ Z \ {0} we have
Resz=√−1n
{ eζz
sinh(πz)z
}
= (−1)ne
√−1ζn
π√−1n ,
so ∫
CR
eζz
sinh(πz)z dz = −(1 −ε)
√
−1ζ − 2Log
(
1 +eε√−1ζ
)
giving the result.
To prove the identity (4.23) we use the power series expansion
Li2(z) =
∞∑
n=1
zn
n2 (A.1)
for the dilogarithm, valid for |z| ≤ 1. In the course of the following proof we will
establish the identity
ζ2
2 − π2
6 − Li2(−e−√−1ζ) = Li 2(−e
√−1ζ) (A.2)
valid for ζ = ±π and all ζ ∈ C with |Re(ζ)|<π .
Asymptotics of the quantum invariants for the ﬁgure 8 knot 53
Proof of (4.23) Note ﬁrst that the integral Aγ(ζ) := 1
4
∫
CR
eζz
sinh(πz)γz 2 dz is conver-
gent for all ζ ∈ C with |Re(ζ)| ≤ π since
∫ −R
−∞
eζt
sinh(πt)t2 dt = −
∫ ∞
R
e−ζt
sinh(πt)t2 dt
and ⏐
⏐
⏐
⏐
∫ ∞
R
eζt
sinh(πt)t2 dt
⏐
⏐
⏐
⏐ ≤ 2
1 −e−2πR
∫ ∞
R
e(Re(ζ)−π)t 1
t2 dt.
Let b = sign(Im(ζ)), where sign(0) can be put to both 1 and −1 in the following.
Moreover, leth be a positive parameter and let δ−
h (t) = (1+ib)ht+ibh fort ∈ [−1, 0]
and let δ+
h (t) = (1 −ib)ht +ibh for t ∈ [0, 1]. It is elementary to show that the
integrals
∫
δ±
h
eζz
sinh(πz)z2 dz converge to zero as h converges to inﬁnity for |Re(ζ)| ≤ π.
By the residue theorem we conclude that
Aγ(ζ) = 1
4γ 2πi
∞∑
n=1
Resz=in
{ eζz
sinh(πz)z2
}
for Im(ζ) ≥ 0 and |Re(ζ)| ≤ π and
Aγ(ζ) = − 1
4γ 2πi
∞∑
n=0
Resz=−in
{ eζz
sinh(πz)z2
}
for Im(ζ) ≤ 0 and |Re(ζ)| ≤ π. Using (A.1) this leads directly to
Aγ(ζ) =
{ 1
2√−1γ Li2(−e
√−1ζ ) , Im(ζ) ≥ 0,
1
2√−1γ
[
ζ2
2 − π2
6 − Li2(−e−√−1ζ)
]
, Im(ζ) ≤ 0.
for |Re(ζ)| ≤ π. Left is to prove the identity (A.2). To this end, let
g(ζ) = ζ2
2 − π2
6 − Li2(−e−iζ) − Li2(−eiζ)
for ζ ∈ Ω := {ζ ∈ C | |Re(ζ)|<π }. By (4.22) we have
g′(ζ) = ζ +i
(
Log(1 +eiζ ) − Log(1 +e−iζ)
)
and therefore eig′(ζ) = 1. Since Ω is connected, g is C1 and g′(0) = 0 we get that
g′ is identically zero on Ω so g is constant on Ω. Now g(0) = −π2
6 − 2Li2(−1) and
Li2(−1) =
∞∑
n=1
(−1)n
n2 = −π2
12
so g(0) = 0. Finally we note that g is well-deﬁned and continuous on Ω ∪ {±π} so
g(±π) = 0 by continuity.
54 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Note that the function g in the above proof is a well-deﬁned analytic function
on W = { ζ ∈ C | Re(ζ) /∈ π + 2πZ } and that g is continuous on W ∪ R. As
in the proof above we ﬁnd that g is constant on each connected component of W .
Moreover, we can on each of these connected components choos e a branch of the
dilogarithm such that g extends to a continuous (and hence a constant) function on
the connected set W ∪ R.
Proof of Lemma 3 The function 1 / sinh(w) has a simple pole at w = 0 with principal
part 1/w, i.e.
φ(w) = 1
sinh(w) − 1
w
is holomorphic in a neighborhood of zero, in fact on the open disk D(0,π ) with
centre 0 and radius π. Let a ≥ R, let CR;a = [ −a, −R] ∪ Υ R ∪ [a,R ], and write
Iγ(ζ) = Jγ(ζ) +Kγ(ζ), where
4Jγ(ζ) =
∫
CR;a
eζz
sinh(πz)zφ(γz )dz,
4Kγ(ζ) =
∫ −a
−∞
eζz
sinh(πz)zφ(γz )dz +
∫ ∞
a
eζz
sinh(πz)zφ(γz )dz.
To estimate Kγ(ζ) we simply use that
|φ(γt)| ≤ 1
sinh(γt) + 1
γt ≤ 2
γt
for t> 0 leading to the bound
|Kγ(ζ)| ≤ 1
2γ
∫ ∞
a
eRe(ζ)t +e−Re(ζ)t
sinh(πt)
1
t2 dt
≤ 1
γ(1 −e−2πa)
∫ ∞
a
(
e−(π−Re(ζ))t +e−(π+Re(ζ))t
) 1
t2 dt.
For |Re(ζ)| ≤ π we therefore get
|Kγ(ζ)| ≤ 2
γ(1 −e−2πa)
∫ ∞
a
1
t2 dt = 2
aγ(1 −e−2πa).
If |Re(ζ)|<π we ﬁnd that
|Kγ(ζ)| ≤ 1
γa2(1 −e−2πa)
∫ ∞
a
(e−(π−Re(ζ))t +e−(π+Re(ζ))t)dt
= 1
γa2(1 −e−2πa)
(
e−(π−Re(ζ))a
π − Re(ζ) + e−(π+Re(ζ))a
π + Re(ζ)
)
.
Next let us estimate Jγ(ζ). First we use the standard estimate
⏐
⏐
⏐
⏐
∫
Υ R
eζz
sinh(πz)zφ(γz )dz
⏐
⏐
⏐
⏐ ≤πRM (ζ,R ),
Asymptotics of the quantum invariants for the ﬁgure 8 knot 55
where M (ζ,R ) = maxz∈Υ R
⏐
⏐
⏐ eζz
sinh(πz)zφ(γz )
⏐
⏐
⏐. We have
|φ(w)| = sinh(w) −w
w sinh(w) .
Here sinh(w) −w = w3h(w) and w sinh(w) = w2k(w), where h and k are entire
functions. Note that k is diﬀerent from zero on D(0,π ). Since γ ∈]0, 1[ we get
M (ζ,R ) = 2γL(R)N (ζ,R ),
where L(R) = max |z|≤R |h(z)/k(z)| and N (ζ,R ) = max z∈Υ R
⏐
⏐
⏐ eζz
eπz −e−πz
⏐
⏐
⏐. We note
that
N (ζ,R ) ≤Q±(R) max
z∈Υ R
⏐
⏐
⏐e(ζ±π)z
⏐
⏐
⏐,
where Q±(R) = maxz∈Υ R
1
|1−e±2πz | . Put Q(R) = Q−(R) +Q+(R) and get
N (ζ,R ) ≤Q(R) min
µ=±1
(
max
z∈Υ R
⏐
⏐
⏐e(ζ+µπ)z
⏐
⏐
⏐
)
.
Since Re(z) ∈ [−R,R ] and Im(z) ∈ [0,R ] for z ∈ Υ R we ﬁnally get
N (ζ,R ) ≤Q(R)e2πR
(
1 +e−Im(ζ)R
)
.
We have thus obtained the estimate
⏐
⏐
⏐
⏐
1
4
∫
Υ R
eζz
sinh(πz)zφ(γz )dz
⏐
⏐
⏐
⏐ ≤γB
(
1 +e−Im(ζ)R
)
,
where B = π
2RL(R)Q(R)e2πR.
Finally we have to estimate ∫a
R
eζt −e−ζt
sinh(πt)tφ(γt)dt. First observe that
h(y) =
∞∑
n=0
y2n
(2n + 3)!
and
k(y) =
∞∑
n=0
y2n
(2n + 1)!
so h(y) ≤k(y)/6 for y ∈ R. Therefore
⏐
⏐
⏐
⏐
∫ a
R
eζt −e−ζt
sinh(πt)t φ(γt)dt
⏐
⏐
⏐
⏐ ≤ γ
3
∫ a
R
eRe(ζ)t +e−Re(ζ)t
eπt −e−πt dt
≤ γ
3(1 −e−2πR)
∫ a
R
(
e−(π−Re(ζ))t +e−(π+Re(ζ))t
)
dt.
For |Re(ζ)| ≤ π we get
⏐
⏐
⏐
⏐
∫ a
R
eζt −e−ζt
sinh(πt)t φ(γ(t)dt
⏐
⏐
⏐
⏐ ≤ 2aγ
3(1 −e−2πR).
56 Asymptotics of the quantum invariants for the ﬁgure 8 knot
If |Re(ζ)<π we get
⏐
⏐
⏐
⏐
∫ a
R
eζt −e−ζt
sinh(πt)t φ(γ(t)dt
⏐
⏐
⏐
⏐ ≤ γ
3(1 −e−2πR)
∫ a
0
(
e−(π−Re(ζ))t +e−(π+Re(ζ))t
)
dt
= γ
3(1 −e−2πR)
(
1 −e−(π−Re(ζ))a
π − Re(ζ) + 1 −e−(π+Re(ζ))a
π + Re(ζ)
)
.
The lemma now follows by putting a = 1/γ >1>R and A = 13
12(1−e−2πR ) .
Appendix B Proofs of the estimates (4.28) and (4.30)
Let
J
′
±(r,ε ) =
∫
C±(ε)
(exp (Iγ(π − 2πx) −Iγ(−π + 2πx)) − 1)erΦ(x)dx,
J
′′
±(r,ε ) =
∫
C±(ε)
(tan(πrx) ∓
√
−1)gr(x)dx,
where Φ is given by (4.29). Note ﬁrst that we are free to deform the contourC±(ε) as
long as we stay inside the domain of analyticity of the integrands. For the integrals
J
′
±(r,ε ) we will deform C±(ε) to ∓[ε, 1 −ε]. Since the integrands of the integrals
J
′′
±(r,ε ) are analytic on Ω 1
2r \ { (m + 1/2)/r |m = 0, 1,...,r − 1 }, we can deform
C±(ε) to C±(0) in these integrals without changing their sum, i.e.
J
′′
−(r,ε ) +J
′′
+(r,ε ) = J
′′
−(r) +J
′′
+(r),
where J
′′
±(r) = J
′′
±(r, 0). In the following calculations we will need the identity
Re (Φ(x)) = 2πRe(x)Im(x) −πIm(x) − 1
π Im
(
Li2
(
e−2πIm(x)e2πiRe(x)
))
(B.1)
valid for x ∈ Ω ∞ (see (3.20)). This identity is an immediate consequence of (A.2).
Proof of (4.28) Let us ﬁrst estimate J
′′
+(r). We partition C+(0) into the three
pieces C1
+ = [√−1, 0], C2
+ = [1 + √−1, √−1], and C3
+ = [1, 1 + √−1]. Put
Ii
+(r) =
∫
C i
+
(tan(πrx) −
√
−1)gr(x)dx.
By (4.26) we immediately get
|I 1
+(r)| ≤ 2
∫ 1
0
e−2πrt|gr(
√
−1t)|dt.
To be able to use (4.23) we introduce the positive parameter ε again. In fact, we
have by (4.23), Lemma 3 and Lebesgue’s dominated convergence th eorem that
|I 1
+(r)| ≤ 2 exp(2A + 2Bπ/r ) lim
ε→0+
∫ 1
0
e−2πrt
⏐
⏐
⏐erΦ(ε+√
−1t)
⏐
⏐
⏐dt.
Asymptotics of the quantum invariants for the ﬁgure 8 knot 57
By (B.1) we immediately get that
⏐
⏐
⏐erΦ(ε+√
−1t)
⏐
⏐
⏐ = exp
(
r
[
2πεt −πt − 1
π Im
(
Li2
(
e2π√−1εe−2πt
)) ])
.
Now by continuity of ( t,ε ) ↦→Li2
(
e2π√−1εe−2πt
)
on [0, 1] × [0, 1] we can remove
the parameter ε again by using Lebusgue’s dominated convergence theorem once
more. This gives us
lim
ε→0+
∫ 1
0
e−2πrt
⏐
⏐
⏐erΦ(ε+√
−1t)
⏐
⏐
⏐dt =
∫ 1
0
e−3πrt dt
leading to the estimate
|I 1
+(r)| ≤ 2
3πr exp(2A + 2Bπ/r )
(
1 −e−3πr)
.
Next we estimate I 2
+. By (4.26) we get
|I 2
+(r)| ≤ 4e−2πr
∫ 1
0
|gr(
√
−1 +t)|dt.
Similarly to the analysis of I 1
+ we introduce the parameter ε and get
|I 2
+(r)| ≤ 4 exp(2A + 2Bπ/r )e−2πr lim
ε→0+
∫ 1−ε
ε
|erΦ( √−1+t)|dt.
Here
|erΦ( √−1+t)| =e−πr(1−2t) exp
(
−r
π Im
(
Li2(e−2πe2π√−1t)
))
by (B.1), so by Lebesgue’s dominated convergence theorem we get
|I 2
+(r)| ≤ 4 exp(2A + 2Bπ/r )e−3πr
∫ 1
0
e2πrt exp
(
−r
π Im
(
Li2(e−2πe2π√−1t)
))
dt.
By deﬁnition of the dilogarithm we have
Im
(
Li2(e−2πe2π√−1t)
)
= −
∫ 1
0
Arg
(
1 −se−2πe2π√−1t
)
s ds,
which is non-negative for t ∈ [0, 1/2]. For t ∈ [1/2, 1] we use that
Im
(
Li2(e−2πe2π√−1t)
)
= Im
(
Li2(e2π√−1t)
)
+
∫ 1
1−e−2π
Arg
(
1 −se2π√−1t
)
s ds,
where the last integral is positive. The ﬁrst term is bounded from be low by
−∑ ∞
n=1
1
n2 = −π2
6 by (4.24). We therefore end up with
|I 2
+(r)| ≤ 4 exp(2A + 2Bπ/r )e−(3−1/6)πr
∫ 1
0
e2πrtdt
= 2
πr exp(2A + 2Bπ/r )e−(3−1/6)πr(
e2πr − 1
)
.
58 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Finally, we estimate I 3
+. Similarly to the other cases we get
|I 3
+(r)| ≤ 2 exp(2A + 2Bπ/r ) lim
ε→0+
∫ 1
0
e−2πrt
⏐
⏐
⏐erΦ(1 −ε+√
−1t)
⏐
⏐
⏐dt.
By (B.1) we have
⏐
⏐
⏐erΦ(1 −ε+√
−1t)
⏐
⏐
⏐ = exp
(
r
[
π(1 − 2ε)t − 1
π Im
(
Li2(e−2πte−2π√−1ε)
) ])
leading to
|I 3
+(r)| ≤ 2 exp(2A + 2Bπ/r )
∫ 1
0
e−πrtdt = 2
πr exp(2A + 2Bπ/r )
(
1 −e−πr)
.
By letting C1
− = [−√−1, 0], C2
− = [1 − √−1, −√−1], and C3
− = [1, 1 − √−1] and
Ii
−(r) =
∫
C i
−
(tan(πrx) +
√
−1)gr(x)dx
we ﬁnd (now by the use of (4.27)) an upper bound for |Ii
−(r)| identical with the
upper bound for |Ii
+(r)|,i = 1, 2, 3, with the exception that exp(2A+2Bπ/r ) should
be replaced by exp(2 A + 4Bπ/r ) in these bounds. To conclude we have shown that
there exists a constant K1 independent of r and ε such that
|J
′′
+(r,ε ) +J
′′
−(r,ε )| ≤
3∑
i=1
(
|Ii
+| + |Ii
−|
)
≤ K1
r
for all r ∈ Z≥2.
Proof of (4.30) By the remarks prior to the proof of (4.28) we have
J
′
±(r,ε ) = ∓
∫ 1−ε
ε
exp (rΦ(t))hγ(t)dt,
where
hγ(t) = exp (Iγ(π − 2πt) −Iγ(−π + 2πt)) − 1.
The integrand is continuous on [0 , 1]. Therefore
⏐
⏐
⏐J
′
±(r,ε )
⏐
⏐
⏐ ≤
∫ 1
0
exp (rRe (Φ(t))) |hγ(t)| dt
for all ε ∈]0, 1
4r [. By (4.24) and (4.25) and the remarks prior to (4.25) we have
Re (Φ(t)) = 1
2π Im
(
Li2(e−2π√−1t) − Li2(e2π√−1t)
)
= − 1
π Cl2(2πt) ≤ 1
2π Vol(K).
Therefore
|J
′
±(r,ε )| ≤ exp
(r
2π Vol(K)
) ∫ 1
0
|hγ(t)| dt.
Asymptotics of the quantum invariants for the ﬁgure 8 knot 59
By deﬁnition we have
hγ(t) =
∞∑
n=1
1
n! (Iγ(π − 2πt) −Iγ(−π + 2πt))n.
From Lemma 3 we get
|Iγ(π − 2πt) −Iγ(−π + 2πt)| ≤ (Cf (t) +D)γ
for t ∈]0, 1[, where C and D are positive constants independent of γ and t, and
f (t) = 1
t + 1
1 −t.
Since f :]0, 1[→ R is bigger than or equal to 4 we can choose C so big that
|Iγ(π − 2πt) −Iγ(−π + 2πt)| ≤ Cf (t)γ
for t ∈]0, 1[. From Lemma 3 we also have
|hγ(t)| ≤ exp (|Iγ(π − 2πt) −Iγ(−π + 2πt)|) ≤ exp(4A + 4Bπ/r )
fort ∈ [0, 1], where A andB are as in Lemma 3, so π
r exp(4A + 4Bπ/r ) is an upper
bound for both of the integrals
∫γ
0 |hγ(t)|dt and
∫ 1
1−γ |hγ(t)|dt (for r ≥ 4). Left is
to evaluate (for r ≥ 7)
∫ 1−γ
γ
|hγ(t)|dt ≤
∞∑
n=1
Cnγn
n!
∫ 1−γ
γ
f (t)ndt.
By using that
f (t)n =
n∑
k=0
(
n
k
) 1
tk
1
(1 −t)n−k
we get
∫ 1−γ
γ
f (t)ndt =
n∑
k=0
( n
k
) ∫ 1−γ
γ
1
tk
1
(1 −t)n−k dt
≤
n∑
k=0
(
n
k
) (
2n−k
∫ 1/2
γ
1
tk dt + 2k
∫ 1−γ
1/2
1
(1 −t)n−k dt
)
≤ 2n
n∑
k=0
( n
k
) (∫ 1/2
γ
1
tk dt +
∫ 1/2
γ
1
tn−k dt
)
≤ 2n+1
( n∑
k=0
( n
k
) ) ∫ 1/2
γ
1
tn dt = 2 2n+1
∫ 1/2
γ
1
tn dt.
Here ∫ 1/2
γ
1
t dt = −Log(2) − Log(γ) ≤ Log(r)
60 Asymptotics of the quantum invariants for the ﬁgure 8 knot
and ∫ 1/2
γ
1
tn dt = 1
n − 1
( 1
γn−1 − 2n−1
)
≤ 1
n − 1
1
γn−1
for n ≥ 2. Therefore
∫ 1−γ
γ
|hγ(t)|dt ≤ 2γ
(
4CLog(r) +
∞∑
n=2
(4C)n
(n − 1)n!
)
≤ 2π
r (4CLog(r) + exp(4C) − 4C − 1).
We conclude that there exists a constant K2 independent of r and ε such that
|J
′
+(r,ε ) +J
′
−(r,ε )| ≤ K2
Log(r)
r exp
(r
2π Vol(K)
)
,
for all r ∈ Z≥2.
Appendix C The case M0
The manifold M0 is the mapping torus of a torus with monodromy matrix
( 2 1
1 1
)
,
see [18, p. 366]. The invariant τr(M0) has been calculated by Jeﬀrey [13, Theorem
4.1]. This theorem gives the large r asymptotics of the invariant as well. In fact,
we have
τr(M0) = 1
2 − 1
2
√
5 − 1√
5
(
exp
(
2π
√
−1r
(
− 1
5
))
+ exp
(
2π
√
−1r 1
5
))
(C.1)
which at the same time can be taken as the large r asymptotics of the invariant.
Let us relate this result to our contour integral formula for the inv ariantτr(M0) =
¯τr(M0). By Lemma 2
τr(M0) = ri
4
∫
C 1r
cot(πrx)
(∫
C 2r
tan(πry)f0,r(x,y )dy
)
dx,
where
f0,r(x,y ) = sin(πx)e−2πirxySπ/r (−π + 2π(x −y))
Sπ/r (−π + 2π(x +y)).
Following the discussion in Sec. 4.3 the relevant (shifted) phase func tions to consider
are given by
Ψ a,b
