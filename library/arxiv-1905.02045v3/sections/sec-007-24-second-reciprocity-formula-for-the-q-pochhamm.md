---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-007-24-second-reciprocity-formula-for-the-q-pochhamm
section_title: "Second reciprocity formula for the q-Pochhammer symbol"
section_number: 2.4
pages: 19-38
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
Theorem 7. Let 4≤ h < kwith (h,k ) = 1 and r0∈{ 0,...,h − 1}. Let 0≤ r < kwith
r≡r0 (mod h). We have
(e(−h/k))r e(− h
24k)
(e(k/h))r0 e( k
24h) = exp
(k
h L(r/k)− π
k
∑
1≤n≤r0
cot
(
πnk
h
)n
h + π
k
⌊r
h
⌋
c0
(k
h
)
+Oz
h,k,r0
(
(1 +|z|4 +|log(z(1−z))|)
(
1 + log
(k
h
)
+ k
h2
)))
wherez =r/k, using the notation (2.20) with domain D2 ={z⁄= 0, Re(z)∈ [0, 1)}. Moreover,
the term|log(z(1−z))| can be omitted if z∈ [r0
k, 1− h
k (1−{ r0−k
h })].
20 S. BETTIN AND S. DRAPPEAU
Proof. In this proof, the notation O will stand for Oz
h,k,r0 with respect to the domain D2 =
{z⁄= 0, Re(z)∈ [0, 1)}. Applying the identity h
k + k
h≡ 1
hk (mod 1) we have
(e
(
−h/k
)
)r =
r∏
n=1
(
1− e
(nk
h − n
hk
))
=P·
r∏
n=1
h∤n
(
1− e
(nk
h − n
hk
))
whereP :=∏⌊r/h⌋
n=1
(
1− e(−n
k )
)
. Note that for x,y∈ C, we have
1− e(y−x) = 1
2(1 + e(−x))
(
1− e(y)
)
(1− tan(πx) cot(πy)).
Thus, since∏h−1
n=1(1− e(nk
h )) =h, we have
(e
(
−h/k
)
)r = (e
(
k/h
)
)r0h⌊r/h⌋·P·M·L ,(2.34)
where
M =
r∏
n=1
h∤n
1 + e(− n
hk)
2 , L =
r∏
n=1
h∤n
(
1− cot
(πnk
h
)
tan
(πn
hk
))
.
First, we examineM. We have
M = exp
(
−
r∑
n=1
h∤n
πin
hk +
r∑
n=1
h∤n
log
(
cos
(πn
hk
)))
.
We split the second sum as∑
1≤n≤r−∑
1≤n≤r−r0,h|n. For any ε> 0 we have log(cos(πw
hk ))≪ε
(|w|
hk )2 for|Re(w/(hk))|≤ (1−ε)/2 and so applying Lemma 8 we obtain, with z =r/k,
M = exp
(
−
r∑
n=1
h∤n
πin
hk + k
h2O(|z|3 + 1)
))
= exp
(
− πi(r2 +r)
2hk + k
h2O(|z|3 + 1)
)
.(2.35)
We then move toP = exp(logP). Taking the determination which is real on the negative
imaginary axis, we have that log( 1−e(−w)
2πiw ) is holomorphic and Oε(|w|) for |Re(w)| < 1−ε.
Thus, by Lemma 8,
P = exp
( ∑
1≤n≤(r−r0)/h
log
(
2πin
k
)
+ k
h2O(|z|2 + 1)
)
= exp
(
log Γ
(
1 +r−r0
h
)
+ r−r0
h log 2πi
k + k
h2O(|z|2 + 1)
)
.
Write log(Γ(1+w)) = (w+1/2) log(w+1)−w+E1(w) withE1 holomorphic andO(| log(w+1)|)
on Re(w)>−1. Abbreviating temporarily q = r−r0
h , it follows that
P = exp
((1
2 +q
)
log(1 +q) +q log 2πi
ke +E1(1 +q) + k
h2O(|z|2 + 1)
)
= exp
(r
h log
(2πir
ke
)
−
⌊r
h
⌋
logh +O((1 + log(k/h) + k
h2 )(1 +|z|2 +|log(z)|)
)
,(2.36)
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 21
since
(1
2− r0
h
)
log
(kz +h−r0
h
)
+ kz
h log
(
1 +h−r0
kz
)
+
− r0
h log 2πih
ke +E1
(kz +h−r0
h
)
=O(|z| +|log(z)|).
Note that the terms |log(z)| can be omitted if z∈ [r0
k, 1).
It remains to study L. By Lemma 5 we have | tan(πn
hk ) cot(πnk
h )| < 1 and so we can write
L = exp(logL) with the principal determination. First, we consider
∑
1≤n≤r
h∤n
tan
(
π n
hk
)
cot
(
πnk
h
)
=
∑
1≤n≤r
h∤n
πn
hk cot
(
πnk
h
)
+
∑
1≤n≤r
h∤n
E2
( n
hk
)
cot
(
πnk
h
)
,
whereE2(z) := tan(πz)−πz. Clearly,E2(z) is holomorphic andOε(|z|2) in| Re(z)|< (1−ε)/2.
Thus, dividing in congruence classes modulo h, the second summand above is
O
(
(1 +|z|3)
h∑
𝓁=1
1
𝓁
k
h2
)
=O
(
(1 +|z|3)k logh
h2
)
.
Also,
∑
1≤n≤r
h∤n
cot
(
πnk
h
)πn
hk =
∑
1≤n≤r0
cot
(
πnk
h
)πn
hk +
⌊r/h⌋∑
𝓁=1
∑
1≤n<h
cot
(
πnk
h
)π(n +𝓁h)
hk
= π
k
∑
1≤n≤r0
cot
(
πnk
h
)n
h−
⌊r
h
⌋π
kc0
(k
h
)
since∑h−1
n=1 cot(πn
h) = 0. Thus, by Lemma 9 we have
L = exp
(πi(r2−rk)
2kh + k
h
(
L(r/k) +πi
12 + r
k log
(2πr
ke
))
+
+ π
k
∑
1≤n≤r0
cot
(
πnk
h
)n
h− π
k
⌊r
h
⌋
c0
(k
h
)
+O
((
1 + k
h2 + log(k/h)
)
(1 +|z|4 +| log(1−z)|)
))
,
where the error term |log(1−z)| can be omitted if z∈ [0, 1− h
k (1−{ r0−k
h })]. The theorem
then follows by (2.34), (2.35) and (2.36), since h
24k =O(1). □
3. Proof of Theorem 1
Throughout the rest of the section, K will denote any hyperbolic knot K⁄= 72 with at most
7 crossings.
We will use the same notation as in Section 2.2. In particular, all error terms will be allowed
to depend on d and γ.
Forn∈ N≥0 and α = h
k∈ Q, with (h,k ) = 1, we let
[α]n :=k−1/2(e(α))n′,(3.1)
22 S. BETTIN AND S. DRAPPEAU
where n′≡n (mod k), 0≤n′<k .
There exist m,m 1,...,m 4∈ N, ι,υ ∈ Z and linear functions 𝓁i,j(r) =∑m
u=1κi,j(u)ru with
κi,j∈{ 0,±1} such that
JK(x) = denom(x)ι e(υx)
∑*
0≤r1,...,rm<k
∏m1
j=1[x]𝓁1,j (r)
∏m2
j=1 [x]𝓁2,i(r)
∏m3
j=1[x]𝓁3,j (r)
∏m4
j=1 [x]𝓁4,j (r)
(3.2)
= denom(x)ι e(υx)
∑*
0≤r1,...,rm<k
ΠK
(
[x]𝓁i,j (r)
)
,
where∑* indicates that the sum is restricted to the terms with 0 ≤𝓁i,j(r)<k and, here and
what follows, we put
ΠK
(
zi,j
)
=
∏m1
j=1z1,j
∏m2
j=1z2,j
∏m3
j=1z3,j
∏m4
j=1z4,j
.
The Kashaev invariants for the knots under consideration has been given for example in [32,
34, 33]. In all these cases, m + 3 coincides with the number of crossings of K, moreover
ι = 3−m
2 , m 1 +m2 +m3 +m4 = 3m− 1,
and the values of mi,𝓁i,j are as in Figure 3, where we used the formula [ α]n[α]denom(α)−n = 1
to write the Kashaev invariants given in [32, 34, 33] as in (3.2). Finally, diﬀerent variants of
the deﬁnition of the Kashaev invariant lead to slightly diﬀerent values for υ (cf. [32, p.677
footnote 4] and [41]). In the context of the modularity conjecture it is natural to always take
υ = 0, which we shall do in the following. This choice will lead to the expression (1.3) for
the reciprocity formula, as conjectured by Zagier. Using (2.3) one can then easily deduce the
suitable modiﬁed reciprocity formula corresponding to other choices of υ.
We divide the sum overr restricting theri into congruence classes moduloq and in intervals
of length k/d:
JK(γx) = denom(γx)
3−m
2
∑
L∈{0,...,d−1}m
∑
s (mod q)
JK(γ,x ;L,s)(3.3)
where, for L = (L1,...,L m)∈ Zm
≥0,s = (s1,...,s m)∈ (Z/qZ)m we write
JK(γ,x ;L,s) =
∑*
0≤r1,...,rm<k,
⌊rid/k⌋=Li,∀i
ri≡si (mod q),∀i
ΠK
(
[γx]𝓁i,j (r)
)
.
By Theorem 6 and Remark 5, we have
[γx]r = [x]⌊rd/k⌋A(p,q )Φr({rd/k}),
where for s∈ Z/qZ, λ∈ [0, 1), we deﬁne
A(p,q ) = e
(
− s(p,q )
2 − 1
8
)
,
Φs(λ) = exp
( k
qd
(
L(λ) +πi
12
)
+ πid
12kq +Es(λ,d/k )
)
.(3.4)
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 23
K (mj)1≤j≤4 𝓁i,j =𝓁i,j(r)
41 (1, 1, 0, 0) 𝓁1,1 =𝓁2,1 =r
52 (0, 1, 2, 2) 𝓁2,1 =r1 +r2, 𝓁 3,1 =r1 +r2
𝓁3,2 =𝓁4,1 =r2, 𝓁 4,2 =r1
61 (0, 2, 3, 3)
𝓁2,1 =r1 +r2, 𝓁 2,2 =r1 +r2 +r3
𝓁3,1 =r1, 𝓁 3,2 =r1 +r2, 𝓁 3,3 =r1 +r2 +r3
𝓁4,1 =r1, 𝓁 4,2 =r2, 𝓁 4,3 =r3
62 (2, 1, 2, 3) 𝓁1,1 =r1, 𝓁 1,2 =r2 +r3, 𝓁 2,1 =r1
𝓁3,1 =𝓁4,1 =r2, 𝓁 3,2 =r3, 𝓁 4,2 =r1−r2, 𝓁 4,3 =r2 +r3
63 (1, 1, 3, 3) 𝓁1,1 =𝓁2,1 =r2, 𝓁 3,1 =𝓁4,1 =r1
𝓁3,2 =𝓁4,2 =r3, 𝓁 3,3 =r2−r3, 𝓁 4,3 =r2−r1
73 (2, 3, 3, 3)
𝓁1,1 =𝓁2,1 =r2, 𝓁 1,2 =r2−r1
𝓁2,2 =𝓁3,1 =r2−r3, 𝓁 2,3 =𝓁3,2 =r2−r3−r4, 𝓁 3,3 =r1
𝓁4,1 =r2−r1, 𝓁 4,2 =r3, 𝓁 4,3 =r4
74 (3, 0, 4, 4)
𝓁1,1 =𝓁4,1 =r1 +r2, 𝓁 1,2 =r2 +r3
𝓁1,3 =𝓁4,2 =r3 +r4
𝓁3,1 =r1, 𝓁 3,2 =𝓁4,3 =r2
𝓁3,3 =𝓁4,4 =r3, 𝓁 3,4 =r4
75 (2, 2, 3, 4)
𝓁1,1 =𝓁2,1 =r3, 𝓁 1,2 =𝓁4,1 =r3−r4
𝓁2,2 =𝓁3,1 =r2, 𝓁 3,2 =𝓁4,2 =r1, 𝓁 3,3 =r4
𝓁4,3 =r2−r1
𝓁4,4 =r3−r2
76 (2, 1, 4, 4)
𝓁1,1 =𝓁4,1 =r2, 𝓁 1,2 =r3 +r4
𝓁2,1 =r2 +r3, 𝓁 3,1 =𝓁4,2 =r1, 𝓁 3,2 =r2−r1
𝓁3,3 =𝓁4,3 =r3, 𝓁 3,4 =𝓁4,4 =r4.
77 (2, 1, 4, 4) 𝓁1,1 =r1 +r2, 𝓁 1,2 =r3 +r4
𝓁2,1 =r2 +r3, ∀j∈{ 1, 2, 3, 4}, 𝓁3,j =𝓁4,j =rj
Figure 3. Parameters of the Kashaev invariants
It follows that
JK(γ,x ;L,s) =A(p,q )m1+m4−m2−m3
∑*
0≤r1,...,rm<k,
⌊rid/k⌋=Li,∀i
ri≡si (mod q),∀i
ΠK
(
[x]⌊𝓁i,j (r)d/k⌋Φ𝓁i,j (s)({𝓁i,j(r)d/k})
)
.
Now, let λi ={rid/k}. The next lemma shows that the contribution of the terms for which
𝓁i,j(λ) /∈ [0, 1) for some i,j is negligible.
Lemma 10. There exists δ >0 such that
⏐⏐⏐⏐ΠK
(
exp
(
L(𝓁i,j(λ))
))⏐⏐⏐⏐≤ exp
(Vol(K)
2π −δ
)
whenever 𝓁i,j(λ) /∈ [0, 1) for some i,j .
24 S. BETTIN AND S. DRAPPEAU
We postpone the proof of Lemma 10 to Section 3.1. Since [ x]r ≍ 1 for 0 ≤ r < d,
applying (2.15) and the above lemma we obtain
JK(γ,x ;L,s) =A(p,q )m1+m4−m2−m3ΠK
(
[x]𝓁i,j (L)
)
J∗
K(γ,x ;L,s) +
+O
(
kO(1) exp
((Vol(K)
2π −δ
) k
qd
))
,
(3.5)
where
J∗
K(γ,x ;L,s) =
∑*
0≤r1,...,rm<k,
⌊rid/k⌋=Li,∀i
ri≡si (mod q),∀i,
𝓁i,j (λ)∈[0,1)∀i,j
ΠK
(
Φ𝓁i,j (s)({𝓁i,j(r)d/k})
)
.
We notice that the condition 0 ≤ 𝓁i,j(r) < k, which is implicit in the summation ∑∗, can
be written as 0 ≤ 𝓁i,j(L) + 𝓁i,j(λ) < d and so, since 𝓁i,j(λ) ∈ [0, 1), it is equivalent to
0≤𝓁i,j(L)<d . Assuming that L satisﬁes this condition,J∗
K(γ,x ;L,s) can be then rewritten
as
J∗
K(γ,x ;L,s) =
∑
0≤ri−Lik/d<k/d∀i,
ri≡si (mod q),∀i,
0≤𝓁i,j (r−kL/d)<k/d∀i,j
ΠK
(
Φ𝓁i,j (s)({𝓁i,j(r)d/k})
)
where we used{𝓁i,j(r)d/k} =𝓁i,j(rd/k−L) to rewrite the summation conditions. This sum
is essentially the same sum which arises when taking d = 1, γ = ( 0 1
−1 0 ), i.e. the conjugate
of the sum arising in the volume conjecture. The only diﬀerence in the general case is that
r is summed over a box with sides of length k/d and along arithmetic progressions modulo
q. For ﬁxed d,q these restrictions are negligible from the analytical point of view, and the
works [32, 34, 33] can be adapted. For z∈ (C r R)∪ (0, 1), deﬁne
ψ1(z) := f(z), ψ 2(z) := f(1−z), ψ 3(z) :=−f(z), ψ 4(z) :=−f(1−z),
and let µ = (µ1,...,µ m) be the solution described in [32, §5.1], [34, §3.3,§4.3,§5.3] [33,
§3.3,§4.3,§5.3,§6.3,§7.3] (conjugated to agree with our deﬁnition of JK) to the system of
equations
4∑
i=1
m1∑
j=1
κi,j(u)ψi(1−𝓁i,j(µ)) = 0, ∀u∈{ 1,...,m }(3.6)
satisfying 0 < Re(𝓁i,j(µ))< 1 for all i,j . We write
νi := exp(µi), ν 1/q
i := exp(µi/q).
It is known [32, 34, 33] that Q(ν) =FK, the trace ﬁeld of K. It will be useful to denote
FK,q := Q(e(1/q),ν), ˜FK,q := Q(e(1/q),ν1/q).
The following lemma will be proven in Section 3.2.
Lemma 11. LetL∈{ 0,...,d − 1}m,s∈ (Z/qZ)m with 0≤𝓁i,j(L)<d for all i,j . Then for
all N≥ 0, we have
J∗
K(x;L,s) = 1
D1/2
(2πik
qd
)m/2
exp
(Vol(K)−i cs(K)
2π
k
qd +C(s)
)( N∑
n=0
ωs,n
(2πiqd
k
)n
+O
(qd
k
)N +1)
,
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 25
where 0⁄= D∈FK, ωs,0 := 1 and
C(s) :=
4∑
i=1
mi∑
j=1
Ci,j(s), C i,j(s) :=
q∑
g=1
B1
(⟨gp−𝓁i,j(s)⟩
q
)
ψi
(g−𝓁i,j(µ)
q
)
(3.7)
where B1 is the 1-st Bernoulli polynomial. Moreover, for all n≥ 1, ωs,n∈ ˜FK,q, and for
all σ∈ Gal( ˜FK,q/FK,q), we have σ(ωs,n) =ωs−pu,n if σ is given by
σ(ν1/q
i ) =ν1/q
i e(ui/q) (1 ≤i≤m) (3.8)
for some u1,...,u m∈ Z.
Applying Lemma 11, by (3.3) and (3.5), and recalling the condition 0 ≤ 𝓁i,j(L) < d for
all i,j , we obtain
JK(γx)
JK(x) = A(p,q )m1+m4−m2−m3
D1/2
(k
d
) 3
2
e(−m/8)q−m/2 exp
(Vol(K)−i cs(K)
2π
k
qd
)
×
∑
s (mod q)
exp(C(s))
( N∑
n=0
ωs,n
(2πiqd
k
)n
+O
(1
k
)N +1)
,
for all N≥ 0.
Now, 6q s(p,q ) is an integer, so A(p,q ) is a 24q root of unity, and letting νK =−m1−m4 +
m2 +m3, we have νK≡m + 1 (mod 2). We deduce
e
(νK
2 s(p,q ) +ν−m
8
)
=±e
(νK
2 s(p,q ) + 1
8
)
ω,
where ω∈{ 1,i} is independent of α and νK is as in the following table.
K 41 51 61 62 63 73 74 75 76 77
νK 0 1 2 −2 0 1 −3 −1 −1 −1
Figure 4. Values ofνK
Keeping track of the factor i implicit in 2π
ℏ =−i k
dq, the proof of Theorem 1 follows from
the following lemma, upon possibly multiplying the value of D by−1.
Lemma 12. There exists 0⁄=U∈FK such that deﬁning
Sn :=U 1/2 ∑
s (mod q)
exp(C(s))ωs,n, n ∈ N≥0,
we have Sq
n∈ FK,q for all n≥ 0. If moreover Sn⁄= 0, then for all n′≥ 0 we have S−1
n Sn′∈
FK,q.
Note that in Theorems 2.2 and 2.6 of [14], similar computations are carried out for coeﬃ-
cients of power series constructed by a diﬀerent process, which are conjectured to match those
in the modularity conjecture.
26 S. BETTIN AND S. DRAPPEAU
Proof. Forx∈ (−1, 1) we have B1(⟨x⟩) =x− 1
2 + 1x≤0. Thus,
Ci,j(s) =
q∑
g=1
B1
(⟨g−𝓁i,j(s)⟩
q
)
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)
=
⟨𝓁i,j (s)⟩∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)
+
q∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)(g
q−⟨𝓁i,j(s)⟩
q − 1
2
)
=
⟨𝓁i,j (s)⟩∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)
+
q∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)g
q−ψi(1−𝓁i,j(µ))
(⟨𝓁i,j(s)⟩
q + 1
2
)
where in the last equality we used (2.9). Then,
Ci,j(s) =Di,j(s) + 1
qD′
i,j−ψi(1−𝓁i,j(µ))
(𝓁i,j(s)
q + 1
2
)
,(3.9)
with
Di,j(s) :=
⟨𝓁i,j (s)⟩∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)
+ψi(1−𝓁i,j(µ))𝓁i,j(s)−⟨𝓁i,j(s)⟩
q ,(3.10)
D′
i,j :=
q∑
g=1
ψi
(⟨gp⟩− 𝓁i,j(µ)
q
)
g.(3.11)
It follows that
∑
s (mod q)
exp(C(s))ωs,n = exp
(1
q
4∑
i=1
mi∑
j=1
D′
i,j− 1
2E
) ∑
s (mod q)
exp
( 4∑
i=1
mi∑
j=1
Di,j(s)
)
ωs,n
(3.12)
where we used that, by (3.6),
E = 2
4∑
i=1
mi∑
j=1
ψi(1−𝓁i,j(µ))
(𝓁i,j(s)
q + 1
2
)
=
4∑
i=1
mi∑
j=1
ψi(1−𝓁i,j(µ))
is independent of s. In particular, writing U = exp(E), by the deﬁnition of ψi, (3.10)-(3.11)
and Lemma 11, we have Sq
n∈ ˜FK,q. The extension ˜FK,q/FK,q is Galois and Gal( ˜FK,q/FK,q)
consists of automorphisms of the form (3.8). Thus, it suﬃces to show that Sq
n is invariant
under any such automorphism σ. Now, by Lemma 11,
σ
(
Sq
n
)
= exp
(1
q
4∑
i=1
mi∑
j=1
D′σ
i,j
) ∑
s (mod q)
exp
( 4∑
i=1
mi∑
j=1
Dσ
i,j(s)
)
ωs−pu,n
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 27
where
Dσ
i,j(s) :=
⟨𝓁i,j (s)⟩∑
g=1
ψi
(⟨gp−𝓁i,j(u)⟩− 𝓁i,j(µ)
q
)
−ψi(1−𝓁i,j(µ))𝓁i,j(s)−⟨𝓁i,j(s)⟩
q ,(3.13)
(D′
i,j)σ :=
q∑
g=1
ψi
(⟨gp−𝓁i,j(u)⟩− 𝓁i,j(µ)
q
)
g.
The same computation as above gives
Dσ
i,j(s) + 1
qD′σ
i,j−ψi(1−𝓁i,j(µ))
(𝓁i,j(s)
q + 1
2
)
=Cσ
i,j(s) (3.14)
where
Cσ
i,j(s) :=
q∑
g=1
B1
(⟨g−𝓁i,j(s)⟩
q
)
ψi
(⟨gp−𝓁i,j(u)⟩− 𝓁i,j(µ)
q
)
(3.15)
so that one ﬁnds
σ
(
Sq
n
)
= exp(−qE/2)
( ∑
s (mod q)
exp
( 4∑
i=1
mi∑
j=1
Cσ
i,j(s)
)
ωs−pu,n
)q
.
By the change of variables g→ g +p𝓁i,j(u) one obtains Cσ
i,j(s) = C(s−pu), so that, after
the change of variables s→s +pu, one obtains σ(Sq
n) =Sq
n, and so Sq
n∈FK,q, as desired.
Now, assume Sn′⁄= 0. By (3.12) we have
S−1
n Sn′ =
( ∑
s (mod q)
exp
( 4∑
i=1
mi∑
j=1
Di,j(s)
)
ωs,n
)−1 ∑
s (mod q)
exp
( 4∑
i=1
mi∑
j=1
Di,j(s)
)
ωs,n′.
and so S−1
n Sn′∈ ˜FK,q. Moreover, given an automorphism σ as in (3.8), one shows as above
that σ(S−1
n Sn′) =S−1
n Sn′ and so S−1
n Sn′∈FK,q. □
Remark 6. The constant term in Theorem 1 can be worked out from the arguments above
as an explicit product of algebraic numbers. In the case K = 41, we obtain
C41(α)D41,0(α) =cδ−1/2
41 Λ1/c
41,α,
δ41 =i
√
3,
Λ1/c
41,α =
( c∏
g=1
|ωg|2g/c
) c∑
r=1
r∏
g=1
|ωg|2,
whereωg = 1− e(gα− 5
6c). In the case of K = 52, let τ≈ 0.665 + 0.562i solveτ 3−τ + 1 = 0,
and letµ1≈ 0.224+0.045i andµ2≈ 0.164−0.067i be such that e(µ1) =τ 2 and e(µ2) =τ 2+τ.
28 S. BETTIN AND S. DRAPPEAU
Then
C52(α)D52,0(α) = e
(s(α)
2
)
c1/2δ−1/2
52 Λ1/c
52,α,
δ52 = 3τ− 2τ 2,
Λ1/c
52,α = e
(
µ1
c + 1
2c
)( c∏
g=1
ω−g/c
g χ−2g/c
g
)
×
×
c∑
r1,r2=1
e
(µ1(r1 +r2) +µ2r1
c + r1
2 − α
2r1(1 +r1 + 2r2)
)( r1∏
g=1
ω−1
g
)( r2∏
g=1
χ−2
g
)
,
where ωg = 1− e(−gα + µ1
c ) and χg = 1− e(gα− µ2
c ), and the logarithms are taken with
principal determination. Note that F52 = Q(τ) (see [32]).
3.1. Proof of Lemma 10. Forλ∈ R, let Λ denote the Lobachevsky function
Λ(λ) :=− Re
(
L(λ)
)
=−
∫ {λ}
0
log(2 sin(πt))dt.
where the last equality follows by (2.8) and (2.10). Note that Λ is 1-periodic and odd. We
need to bound
WK(λ) :=−
2∑
i=1
mi∑
j=1
Λ(𝓁i,j(λ)) +
4∑
i=3
mi∑
j=1
Λ(𝓁i,j(λ))
for all λ∈ [0, 1)m such that 𝓁i,j(λ)⁄∈ [0, 1) for some (i,j ). Deﬁne
M = Λ(1/6)∈ [0.16, 0.162].
We will require the following simple inequalities: for α,β ∈ [0, 1],
|Λ(α)|≤ M,(3.16)
Λ(α)≤ 0, (α≥ 1
2),(3.17)
2(Λ(α) + Λ(β))− Λ(α +β)≤ 4Λ( 1
4)< 0.59, (α +β≤ 1),(3.18)
2(Λ(α) + Λ(β))− Λ(α +β)≤M, (α +β≥ 1).(3.19)
2(Λ(α) + Λ(β))− Λ(α +β)≤ 0.45, (α +β≤ 1, and α≥ 1
2).(3.20)
Λ(α)− Λ(β)≤ 0.23, (α≤ 1
2≤β, and β≤ 2α),(3.21)
The bound (3.21) is proved by optimizing at β = min( 5
6, 2α). The maximum is achieved at
a point α where ρ = sin(πα) solves ρ(1−ρ2) = 1
8. Similarly, the bound (3.20) is proved by
maximizing at α for which ρ = cos(πα) solves ρ = 2(1−ρ2).
We consider the situation case by case; in each case, we work under the extra assumption
that for some (i,j ), we have 𝓁i,j(λ)⁄∈ [0, 1).
• Case K = 52. We have
WK(λ) = Λ(λ1) + 2Λ(λ2).
A bound of 2 M≤ Vol(K)
2π − 0.12 is enough. Assume λ1 +λ2≥ 1. Then λi≥ 1
2 for
some i∈{ 1, 2}, so that using (3.16) and (3.17), we get
WK(λ)≤ 2M
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 29
• Case K = 61. We have
WK(λ) = 2Λ(λ1) + Λ(λ2) + Λ(λ3).
A bound of 3 M≤ Vol(K)
2π − 0.01 is enough. Thus, by (3.17), we may assume λi≤ 1
2
for all i∈{ 1, 2, 3}. Assume λ1 +λ2 +λ3 ≥ 1. Then by concavity of Λ on [0 , 1
2],
we have WK(λ)≤ 2Λ(λ1) + 2Λ(1
2(λ2 +λ3)). The bound (3.21) can then be applied
with (α,β ) = ( 1
2(λ2 +λ3), 1−λ1), and yields WK(λ)≤ 0.46≤ 3M. We ﬁnd in all
cases
WK(λ)≤ 3M.
• Case K = 62. We have
WK(λ) =−2Λ(λ1) + 2Λ(λ2) + Λ(λ3) + Λ(λ1−λ2).
A bound of 4M≤ Vol(K)
2π − 0.05 is enough. Because of (3.17), we may assume λ1 > 1
2
and λ2≤ 1
2. Then the case λ1≤ λ2 is excluded, and we may assume λ2 +λ3≥ 1.
Then λ3 ≥ 1
2, and so by (3.17) and (3.18) (with ( α,β ) = (1 − λ1,λ 2)), we ob-
tain WK(λ)≤ 4Λ( 1
4). We obtain in all cases
WK(λ)≤ 4M.
• Case K = 63. We have
WK(λ) =−2Λ(λ2) + 2Λ(λ1) + 2Λ(λ3) + Λ(λ2−λ3) + Λ(λ2−λ1).
A bound of 5 M≤ Vol(K)
2π − 0.09 is enough. By symmetry, we may assume λ2≤ λ3.
Suppose ﬁrstλ2≥ 1
2. Then λ2−λ3∈ [− 1
2, 0], so by (3.17), Λ(λ2−λ3)≤ 0 and Λ(λ3)≤
0. We deduceWK(λ)≤ 5M by (3.16). Suppose on the other hand thatλ2< 1
2. If λ3≥
1
2, then by (3.18)-(3.19) with (α,β ) = (λ1, 1−λ2), we ﬁndWK(λ)≤ 4Λ( 1
4)+M≤ 5M.
If, ﬁnally, λ3 < 1
2, then by (3.17) we have Λ( λ2−λ3)≤ 0, so that WK(λ)≤ 5M. In
all cases, we ﬁnd
WK(λ)≤ 5M.
• Case K = 73. We have
WK(λ) =−2Λ(λ2) + Λ(λ1) + Λ(λ3) + Λ(λ4).
A bound of 4M≤ Vol(K)
2π − 0.08 is enough. Thus, by (3.17), we may assume λj < 1
2 for
all j∈{ 1, 3, 4}, and λ2 > 1
2. Assume that λ2≤λ3 +λ4. By (3.17) and the concavity
of Λ on [0, 1
2], we have
WK(λ)≤− 2Λ(λ2) + Λ(λ3) + Λ(λ4) +M≤ 2
(
Λ
(λ3 +λ4
2
)
− Λ(λ2)
)
+M.
By (3.21) with β = 1
2(λ3 +λ4), we obtain WK(λ)≤ 0.46 +M≤ 4M. We deduce that
in all cases,
WK(λ)≤ 4M.
• Case K = 74. We have
WK(λ) =−Λ(λ2 +λ3) + Λ(λ1) + 2Λ(λ2) + 2Λ(λ3) + Λ(λ4).
A bound of 5 M ≤ Vol(K)
2π − 0.01 is enough. By (3.17) and (3.16) we may assume
without loss of generality λ2,λ 3 < 1
2. Moreover, by (3.18) (note that 0 .59≤ 4M), we
always haveWK(λ)≤ 4M + Λ(λ1) + Λ(λ4), and so we may assume λ1,λ 4< 1
2 as well.
30 S. BETTIN AND S. DRAPPEAU
But then, neither of the cases λi +λj≥ 1 can occur for ( i,j )∈{ (1, 2), (2, 3), (3, 4)}.
We ﬁnd in all cases that
WK(λ)≤ 5M.
• Case K = 75. We have
WK(λ) =−2Λ(λ3) + 2Λ(λ1) + Λ(λ4) + Λ(λ2−λ1) + Λ(λ3−λ2).
A bound of 6 M≤ Vol(K)
2π − 0.05 is enough. We may assume λ3 > 1
2 and λ1,λ 4 < 1
2.
Then the case λ3≤λ4 is excluded. Assume next λ2≤λ1. Then λ2−λ1∈ (− 1
2, 0], so
that Λ(λ2−λ1)≤ 0. Similarly, if λ3≤ λ2, then λ2 > 1
2, and Λ(λ3−λ2)≤ 0. In all
cases, we ﬁnd by (3.16) and (3.17) that
WK(λ)≤ 6M.
• Case K = 76. We have
WK(λ) =−Λ(λ3 +λ4)− Λ(λ2 +λ3) + 2Λ(λ1) + Λ(λ2−λ1) + 2Λ(λ3) + 2Λ(λ4).
A bound of 0.45 + 4M≤ Vol(K)
2π − 0.03 is enough; note that 0 .59 + 3M <0.45 + 4M.
In particular, we may assume that λ1 < 1
2, since otherwise, by (3.17) and (3.18)-
(3.19), we get WK(λ)≤ 0.59 + 2M. Assume ﬁrst λ3 +λ4≥ 1. Then by (3.19), we
obtain WK(λ)≤ 5M, which is acceptable. Next, assume that λ2 +λ3≥ 1. If λ3≤ 1
2,
then λ2 +λ3∈ [1, 3
2] and by (3.19) we have WK(λ)≤ 0.59 + 3M. If on the other
handλ3> 1
2, then by (3.20), we getWK(λ)≤ 0.45+4M. Both bounds are acceptable.
Finally, assume that λ2≤λ1. Then λ2−λ1∈ (− 1
2, 0], and so Λ(λ2−λ1)≤ 0, and we
again obtain WK(λ)≤ 0.59 + 3M. We ﬁnd in all cases that
WK(λ)≤ 0.45 + 4M.
• Case K = 77. We have
WK(λ) = 2(Λ(λ1) + Λ(λ2) + Λ(λ3) + Λ(λ4))− Λ(λ1 +λ2)− Λ(λ2 +λ3)− Λ(λ3 +λ4).
Assume λi +λj≥ 1 for some (i,j )∈{ (1, 2), (2, 3), (3, 4)}. Then by (3.19) and (3.16),
we have
WK(λ)≤ 7M≤ Vol(K)
2π − 0.08.
Summarizing the above, we ﬁnd that in all cases considered for K, there holds
(3.22) EK := sup{WK(λ)|λ∈ [0, 1)n, ∃i,j, 𝓁i,j(λ) /∈ [0, 1)}≤ VolK
2π − 0.01.
This proves Lemma 10.
Remark 7. The analogue of Lemma 10 for the knot 7 2 is false as stated. It is likely that
this obstacle can be lifted by processing the contour integral arguments underlying Lemma 11
more carefully (see [33, Remark 8.1]). For sake of clarity, and since our main point is rather
to stress how the modularity conjecture can be reduced to the arithmeticity conjecture, we
chose to omit the case K = 72.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 31
3.2. Proof of Lemma 11.
Remark 8. We have L(λ) =− L(1−λ) forλ∈ [0, 1) and f(z) = f(1−z) forz∈ (C\R)∪(0, 1).
In particular we can write the conjugates of Φ r(λ) and gd(λ) given in (3.4) and (2.16) ((2.14)
if λ = 0) as
Φr(λ) = exp
(
− k
qd
(
L(1−λ) +πi
12
)
− πid
12kq +E∗
r (λ,d/k )
)
E∗
r (λ,d/k ) := 1
2f
(q−⟨pr⟩ +λ
q
)
+
q∑
g=1
i
∫ ∞
0
( f(q−g+λ
q −idt
k )
e(−gp−r
q )e2πt− 1
−
f(q−g+λ
q +idt
k )
e(gp−r
q )e2πt− 1
)
dt, (λ⁄= 0)
andE∗
r (0,d/k ) = Er(0,d/k ). In particular, we can extend Φr(λ) to a holomorphic function
of λ in the strip 0 < Re(λ)< 1.
In the following lemmas we give some properties of the expansion of Er andE∗
r .
Lemma 13. Assume Re(λ)∈ (ε, 1−ε) with ε∈ (0, 1/2) and let s∈ Z/qZ. Then, for all
M≥ 0 uniformly in λ we have
Es(λ,d/k ) =
M∑
𝓁=0
(qd
k
)𝓁
Es,𝓁(λ) +Oε
(qd
k
)M +1
, E∗
s (λ,d/k ) =
M∑
𝓁=0
(qd
k
)𝓁
E∗
s,𝓁(λ) +Oε
(qd
k
)M +1
,
(3.23)
where
E0,𝓁(λ) :=
q∑
g=1
f
(g−λ
q
)
B1
(⟨gp−s⟩
q
)
, E∗
0,𝓁(λ) :=
q∑
g=1
f
(g−λ
q
)
B1
(⟨gp−s⟩
q
)
,
Es,𝓁(λ) := (−1)𝓁
q𝓁(𝓁 + 1)!
q∑
g=1
f(𝓁)
(g−λ
q
)
˜B𝓁+1
(gp−s
q
)
, 𝓁 ≥ 1,
E∗
s,𝓁(λ) := (−1)𝓁
q𝓁(𝓁 + 1)!
q∑
g=1
f(𝓁)
(1−g +λ
q
)
˜B𝓁+1
(gp−s
q
)
, 𝓁 ≥ 1.
Proof. For Re(λ)∈ (ε, 1−ε) we have infg∈Z‖g−λ
q ‖≫ ε 1. Thus, since
f′(z) =π(cot(πz) +i), f(ν)(z) = (−1)ν−1(ν− 1)!
∑
n∈Z
1
(z−n)ν, (z /∈ Z, ν≥ 2),
we have that f(ν)(g−λ+it
q )≪q,ν,ε (1 +|t|ε) for all ν ≥ 0, t∈ R. The Lemma then follows
immediately by expanding in Taylor series and applying Lemma 2. □
Lemma 14. Assume Re(˜λ)∈ (0, 1) and let s∈ Z/qZ. Let hs,𝓁 be eitherEs,𝓁 orE∗
s,𝓁. Then,
for all 𝓁,M ≥ 0, and all λ in a neighborhood of ˜λ, we have
hs,𝓁(λ) =
M∑
v=0
(2πi)𝓁+vCs,𝓁,v(˜λ)(λ− ˜λ)v +O(|λ− ˜λ|M +1),(3.24)
32 S. BETTIN AND S. DRAPPEAU
where, for (v,𝓁 ) = (0, 0),
C0,0(˜λ) =
q∑
g=1
f
(g− ˜λ
q
)
B1
(⟨gp−s⟩
q
)
, if hs,𝓁 =Es,𝓁(3.25)
C0,0(˜λ) =
q∑
g=1
f
(q−g + ˜λ
q
)
B1
(⟨gp−s⟩
q
)
, if hs,𝓁 =E∗
s,𝓁.(3.26)
Moreover, for (v,𝓁 )⁄= (0, 0) we have Cs,𝓁,v(˜λ)∈ Q(e( 1
q ), e(
˜λ
q )); also if
σ∈ Gal
(
Q(e( 1
q ), e(
˜λ
q ))/Q(e( 1
q ), e(˜λ))
)
is such that σ(e(˜λ/q)) = e(˜(λ +u)/q) for some u∈{ 0,...,q − 1}, then
σ(Cs,𝓁,v(˜λ)) =Cs−up,𝓁,v(˜λ).(3.27)
Proof. The equations (3.24)-(3.26) follow immediately by Taylor expansion. Moreover, if𝓁≥ 1,
v≥ 0 and hr,𝓁 =Er,𝓁 then
Cr,𝓁,v(˜λ) = (−1)𝓁
q𝓁(𝓁 + 1)!
1
qvv!
q∑
g=1
(2πi)𝓁+vf(𝓁+v)
(g− ˜λ
q
)
˜B𝓁+1
(gp−r
q
)
,
so that Cr,𝓁,v(˜λ)∈ Q(e( 1
q ), e(
˜λ
q )) since f′(z) = π(cot(πz) +i) = 2i
1−e(−z) and (3.27) follows by
the change of variables g→g +j. The case 𝓁 = 0, v≥ 1 and the analogous property for ˜Er,𝓁
can be proven in the same way. □
Proof of Lemma 11. As mentioned in the introduction, for the knots under consideration,
the asymptotic expansion stated in Lemma 11 will be essentially reduced to a proof of the
asymptotic expansion in the volume conjecture for those knots. Thus, we shall frequently refer
to [32, 34, 33] where this asymptotic expansion was proven for hyperbolic knots with 5 , 6 and
7 crossings. The case of the knot 4 1 is easier, since there is a dominant critical point on (0, 1),
and the method of stationary phase can be applied, similarly as in the proof of Theorem 2
below. Thus, we will focus here on the case K⁄= 41. Recall also that we assume K⁄= 72.
By Remark 8, for 0 ≤𝓁i,j(L)<d we can write J∗
K as
J∗
K(x;L,s) =
∑
rd/k−L∈D,
ri≡si (mod q),∀i
exp
( k
qdVs,d/k(dr/k−L)
)
,
whereD ={n∈ [0, 1)m|𝓁i,j(n)∈ [0, 1)∀i,j},
Vs,κ(n) := ˆV (n) +qκ
(
Us,κ(n) +πi(m1 +m4−m2−m3)
12q κ
)
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 33
and
ˆV (n) =
m1∑
j=1
(
L(𝓁1,j(n)) +πi
12
)
−
m2∑
j=1
(
L(1−𝓁2,j(n)) +πi
12
)
−
m3∑
j=1
(
L(𝓁3,j(n)) +πi
12
)
+
m4∑
j=1
(
L(1−𝓁4,j(n)) +πi
12
)
,
Us,κ(n) =
m1∑
j=1
Es(𝓁1,j(n),κ ) +
m2∑
j=1
E∗
s(𝓁2,j(n),κ )−
m3∑
j=1
Es(𝓁3,j(n),κ )−
m4∑
j=1
E∗
s(𝓁4,j(n),κ ).
The function ˆV (n) coincides, up to conjugation, with the limiting value of the potential
function of the hyperbolic structure of the knot complement given in [32, (10)], [34, p.297,
p.308, p.322] and [33, p.12, p.26, p.38, p.50, p.63]. We remark that the expressions for ˆV
given there diﬀer from the one we have here, however it is easy to see that the two expressions
actually coincide upon using the dilogarithm identity (or the formula (2.6))
L(1−λ) + L(λ) =−πiB2(λ).
In [32, Lemma 2.1], [34,§3.2,§4.2,§5.2] and [33,§3.2,§4.2,§5.2,§6.2,§7.2] it was shown that
for all knots under consideration Re( ˆV ) is smaller than Vol(K)
2π on the boundary of D. More
precisely, there exists a domainD′⊂D with dist(D′,∂D)> 0 such that Re(ˆV (n))< Vol(K)
2π −δ′
for all n∈D\D ′ and some δ′> 0. Thus, by (2.15), we have
J∗
K(γ,x ;L,s) =
∑
rd/k−L∈D′,
ri≡si (mod q),∀i
exp
( k
qdVs,d/k(dr/k−L)
)
+O
(
km exp
((Vol(K)
2π −δ′
) k
qd
))
.
We now apply Poisson summation formula in the form of [32, Proposition 4.6] (with k/d
playing the role of N of [32]). Note that our sum are restricted to arithmetic progressions
modulo q; since q is ﬁxed, this does not aﬀect the argument. By [32, Lemma 5.1], [34, Lemma
3.4, 4.3 and 5.2] and [33, Lemma 3.2, 4.2, 5.2, 6.2 and 7.2] we have that ˆV (n)− Vol(K)
2π satisﬁes
the conditions (41)-(42) of [32, Proposition 4.6] and by [32, Remark 4.8] and Lemma 13 we
can apply Proposition 4.6 of [32] to Vs,L,d/k(n) rather than ˆV (n). We ﬁnd
J∗
K(γ,x ;L,s) =
( k
qd
)m∫∫
D′
exp
( k
qdVs,d/k(z)
)
dz +O
(
exp
((Vol(K)
2π −δ′′
) k
qd
))
,(3.28)
for some δ′′ > 0, where the extra factor q−m comes from the restriction to the congruence
classes. One can then apply the saddle point method in the form of [32, Proposition 3.5 and
Remark 3.6] as done in [32, p.705-706 and §5.2] (cf. also [42]), [34, p.297 and §3.5; p.309 and
§4.5; p.47 and §5.5] and [33, p.13 and §3.5; p.26 and §4.5; p.39 and §5.5; p.50 and §6.5; p.64
and§7.5]. Notice that both Vs,d/k(z) and the corresponding functions studied in these papers
converge uniformly to ˆV , so the same computations apply. We then ﬁnd that for all N≥ 1
the ﬁrst summand on the right of (3.28) is equal to
(2πk
qd
)m/2 1
det(− Hess)1/2 exp
( k
qd
ˆV (µ) +C(s)
)(
1 +
N∑
n=1
ωs,n
(2πiqd
k
)n
+O
( 1
kN +1
))
34 S. BETTIN AND S. DRAPPEAU
where µ is a critical point of ˆV (z) (and thus satisﬁes (3.6)) with 0 < Re(𝓁i,j(µ)) < 1 for
alli,j , such that ˆV (µ) = Vol(K)−i cs(K)
2π and Hess is the Hesse matrix of ˆV atµ. In particular,
det(− Hess)∈ (πi)mFK. By Lemma 14 the coeﬃcients ωs,n are in ˜FK,q for all n≥ 1 and if
σ is as in (3.8), then σ(ωs,n) = ωs−pu,n. Finally, by (3.25)-(3.26) we have that C(s) is as
in (3.7). □
4. Proof of Theorems 2
We proceed in a similar way as in the proof of Theorem 1. For x =h/k, with (h,k ) = 1 and
1≤h<k , we writeJ41(x) as in (3.2) and we divide the sum into congruence classes modulo
h, that is we write
J41(h/k) =k
3−m
2
∑
0≤s≤h−1
J41(h/k;s) (4.1)
where, for 0≤s≤h− 1, we write
J41(h/k;s) =
∑
0≤r<k,
r≡s (mod h)
|[h/k]r|2.(4.2)
with [·]r as in (3.1). We apply Theorem 7, which for 0 ≤s<h , s≡r (mod h), gives
|[h/k]r|2 =|[k/h]s|2Φ†
s(r/k) exp
(
− 2πr
hk c0(k/h) +E†
s(r/k)
)
(4.3)
for someE†
s(r/k) satisfying|E†
s(r/k)|≪ E(h,k ) for all 0≤r<k , where
E(h,k ) := 1 + logk
h + k
h2 + max
r′=0,...,h−1
⏐⏐⏐
∑
1≤n≤r′
cot
(
πnk
h
) n
hk
⏐⏐⏐,
(note that if 0≤r0<h withr0≡r (mod q), then r
k∈ [r0
k, 1− h
k (1−{ r0−k
h })]), and where for
λ∈ [0, 1], we deﬁne
Φ†
s(λ) = exp
(
2k
h Re
(
L(λ)
))
= exp
(k
h
∫ λ
0
log(4 sin(πt)2)dt
)
,
by (2.8) and (2.10). By positivity, it follows that
J41(h/k;s) = exp
(
O(E(h,k ) +|c0(k/h)|/h)
)
|[k/h]s|2 ∑
0≤r<k
r≡s (mod h)
Φ†
s(r/k).(4.4)
Now, the functionλ→
∫λ
0 log(4 sin(πt)2)dt is continuous on [0, 1] and it has a unique maximum
in this interval, located at λ = 5/6. Moreover, it can be expanded in a neighborhood of this
point as
∫ λ
0
log(4 sin(πt)2)dt = Vol(41)
2π −π
√
3(λ− 5
6)2 +O(|λ− 5
6|3).(4.5)
since
∫ 5/6
0 log(4 sin(πt)2)dt = Vol(41)
2π . It follows that
∑
0≤r<k
r≡s (mod h)
Φ†
s(r/k) =
√
k
h
√
3 exp
(Vol(41)
2π
k
h
)
(1 +O(h/k)) = exp
(Vol(41)
2π
k
h +O(log(1 +k/h))
)
,
(4.6)
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 35
where the ﬁrst step is justiﬁed in a standard way [16, p.517], e.g. by smoothly restricting the
sum to the terms where r/k is in a neighborhood of 5/6, using (4.5) and applying the Poisson
summation formula. The second step instead follows immediately by positivity.
By (4.1), (4.4) and (4.6) we then ﬁnd
J41(h/k) =J41(k/h) exp(O(E(h,k ) +|c0(k/h)|/h)),(4.7)
as desired.
With a similar argument we can prove the following theorem, which deals with the case
where the dominating term on the right hand side of (4.3) is exp( − 2πr
hkc0(k/h)).
Theorem 8. Let 1≤h≤k with (h,k ) = 1 and assume c0(k/h)< 0. Then,
log|J41,0
(
e
(
h/k
))
| = log|J41,0
(
e
(
k/h
))
|− 2π
h c0
(
k/h
)
+O
(k
h + max
0≤r′<h
⏐⏐⏐
∑
1≤n≤r′
cot
(
πnk
h
) n
hk
⏐⏐⏐
)
.
(4.8)
To prove (4.8) ﬁrst we observe we can assume k >2h since otherwise the result is trivial.
Also, we observe that, bounding trivially Φ†
s, one can write (4.3) as
|[h/k]r|2 =|[k/h]s|2 exp
(
− 2πr
hk c0(k/h) +O(E(h,k ) +k/h)
)
and so
J41(h/k;s) = exp
(
O(E(h,k ) +k/h)
)
|[k/h]s|2 ∑
0≤r<k
r≡s (mod h)
exp
(
− 2πr
hk c0(k/h)
)
.
Now, if x≥ 0, we have ∑
0≤n≤m enx = emx+O(m), and thus if x is large the sum is roughly
dominated by the last term. Then for c0(k/h)< 0, we have
∑
0≤r<k
r≡s (mod h)
exp
(
− 2πr
hk c0(k/h)
)
= exp
(
− 2πr′
hk c0(k/h) +O(k/h)
)
where r′ is the maximum integer satisfying 0 ≤ r′ < kwith r′≡ s (mod h). Then, k−h≤
r′<k and so in particular r′
hkc0(k/h) = 1
hc0(k/h) +O( 1
k|c0(k/h)|) and the result follows.
5. Proof of Theorem 3
Before starting, we state some basic properties of continued fractions (see [26] for a ref-
erence). Given h/k∈ Q∩ (0, 1) with h,k ∈ N, (h,k ) = 1, we denote by [0; b1,...,b r] the
continued fraction expansion of h/k. Then for 0 ≤ s≤ r the convergents of h/k are the
fractions [0;b1,...,b s] = us
vs with (us,vs) = 1 (as usual u0/v0 = 0/1, v−1 := 0, u−1 := 1);
the vs are called the partial quotients. The partial quotients satisfy the bounds vs≪ 2−s/2,
vr−s≪ k2−s/2 for 0≤ s≤ r, and vs/vs−1≤ bs + 1 for 1 ≤ s≤ r. Also, r≪ logk. For all
1≤s≤r we have vsus−1−vs−1us = (−1)s and so vs−1
vs ≡ (−1)s+1us
vs (mod 1). Moreover, if
1≤h′≤k is such that h′≡ (−1)r+1h (mod k), then the Euclid algorithm on h′ andk can be
written as
(5.1) vr =k, v r−1 =h′,
v𝓁+1 =b𝓁+1v𝓁 +v𝓁−1, 𝓁 = 0,...,r − 1.
The following technical result, proved in [11], will be needed in the proof of Theorem 3.
36 S. BETTIN AND S. DRAPPEAU
Lemma 15 ([11, Theorem 1]) . Let 1≤ h < kwith (h,k ) = 1 . Let v0,...,v r be the partial
quotients of h/k. Then uniformly for 1≤c≤k, we have
∑
1≤n≤c
cot
(
πnh
k
)n
k≪
r−1∑
m=0
vm log(vm+1/vm) +k.
Proof of Theorem 3. Since J is even, applying repeatedly the reciprocity formula (1.7) and
the recurrence relation (5.1), we see that for all 0 ≤s≤r
logJ41,0(e(h/k)) = logJ41,0(e(vr−1/vr)) =C
r∑
𝓁=s+1
( v𝓁
v𝓁−1
+E(v𝓁−1/v𝓁)
)
+ logJ41,0(e(vs−1/vs)),
with C = Vol(41)
2π and E satisfying (1.8). Now, by Lemma 15
r∑
𝓁=1
max
r′=0,...,v𝓁−1−1
⏐⏐⏐
∑
1≤n≤r′
cot
(
πnv𝓁−2
v𝓁−1
) n
v2
𝓁−1
⏐⏐⏐≪
r∑
𝓁=1
𝓁−2∑
m=0
vm
v𝓁−1
log(vm+1/vm) +
r∑
𝓁=1
1/v𝓁−1,
since v𝓁−2
v𝓁−1
= (−1)𝓁u𝓁−1
v𝓁−1
(mod 1) and so its partial quotients are v0...,v 𝓁−1. The second sum
is O(1), whereas changing the order of summation and using v𝓁−1−n≪v𝓁−12−n/2, for n≥ 0,
we obtain
r∑
𝓁=1
𝓁−2∑
m=0
vm
v𝓁−1
log(vm+1/vm)≪
r−2∑
m=0
r∑
𝓁=m+2
2(m−𝓁)/2 log(vm+1/vm)≪
r−2∑
m=0
log(vm+1/vm).
Now, we ﬁx an ε> 1/k and we take s to be the least integer in {1,...,r } such that vs≥ 1/ε
and notice that, sincevm≫ 2m/2, we haves =Oε(1). Then, the above computations and (1.8)
give
logJ41,0(e(h/k)) =
r∑
𝓁=s+1
v𝓁
v𝓁−1
(C +O(√ε)) +
r∑
𝓁=1
O(log(v𝓁/v𝓁−1)) + logJ41,0(e(±us/vs)).
since vs−1
vs =±us
vs (mod 1) for ±1 := (−1)s−1. Now, if s≥ 1, we have±us/vs =γ(bs), where
γ := (±us−1 us−2
±vs−1 vs−2 )∈ SL(2, Z). Notice that by deﬁnition of s all entries of γ are bounded by
1/ε. Thus, by Theorem 1, we have
logJ41,0(e(±us/vs)) =Cbs +O(logbs) +Oε(1) =C
s∑
𝓁=1
b𝓁 +O(logbs) +Oε(1),
sinces,v𝓁−1 =Oε(1) and so also b𝓁 =Oε(1) for all 𝓁≤s− 1. Then, since v𝓁/v𝓁−1 =b𝓁 +O(1)
we ﬁnd
logJ41,0(e(h/k)) = (C +O(√ε))
r∑
𝓁=1
(b𝓁 +O(logb𝓁)) +O(r) +Oε(1).
Finally, we observe that b𝓁 +O(logb𝓁) =b𝓁(1 +O(√ε)) +O(1/ε). Thus,
logJ41,0(e(h/k)) = (C +O(√ε))
r∑
𝓁=1
b𝓁 +Oε(r) = Σ(h/k)
(
C +O(√ε) +Oε
(r(h/k)
Σ(h/k)
))
.
By hypothesis r(h/k)/Σ(h/k)→ 0 and so (1.9) follows by letting ε→ 0+ suﬃciently slowly.
Equation (1.10) then follows immediately from [10, Corollary 1.4]. □
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 37
Proof of Theorem 4. We extendHK to a function onR>0 by settingHK(x) := limy→x,y∈QHK(y)
for all x⁄∈ R>0\ Q. By hypothesis HK(x) is well deﬁned and it is easy to prove that HK is
continuous on R\ Q. Then, setting ψ(x) := HK(x)− Vol(K)
2π
1
x− 3
2 log(1/x), for x >0, and
ψ(0) = 0, we have that ψ(x) is bounded and continuous almost everywhere on [0 , 1]. Thus,
by Lebesgue’s integrability condition, ψ is Riemann-integrable on [0, 1]. In particular, for all
ε> 0 there exist a diﬀerentiable function ψε : [0, 1]→ R such that‖ψ−ψε‖∞,[0,1]≤ε.
By deﬁnition logJK,0(e(h/k))− logJ41,0(e(k/h)) = ψ(h/k) + Vol(K)
2π
k
h + 3
2 log(k/h). Thus,
proceeding as in the proof of Theorem 3 using this formula instead of Theorem 2, we obtain
logJ41,0(e
(
h/k
)
) =
r∑
𝓁=1
(Vol(K)
2π
v𝓁
v𝓁−1
+ 3
2 log(v𝓁/v𝓁−1) +ψ(v𝓁−1/v𝓁)
)
=φε(h/k) +O(ε logk),
where
φε(h/k) :=
r∑
𝓁=1
(Vol(K)
2π
v𝓁
v𝓁−1
+ 3
2 log(v𝓁/v𝓁−1) +ψε(v𝓁−1/v𝓁)
)
.
Letting T (x) ={1/x} for x∈ (0, 1], we note that for 2 ≤s≤r, we have vs−1
vs =Tr−s(h′/k),
whereas v0
v1
=Tr−1(h′/k) + 1b1=1 (the contribution of 1b1=1 being negligible). We apply [10]
(Theorem 1.3 with λ = 1, complemented by Theorem 1.2 with γ(x) = {1/x}), and obtain
that the estimate (1.11) holds with log J41,0(e(h/k)) replaced by φε(h/k) and
DK = 1−γ0− log 2
12/π2 + 3π
Vol(K) + 24
πVol(K)
∫ 1
0
ψε(1/x)dx
1 +x ,
and with an error term oε(N 2). The result then follows by letting ε→ 0+ suﬃciently slowly
with respect to N, and making the change of variables h/k→ h′/k on the left hand side
of (1.11). □
Proof of Corollary 5. We prove the result in the case where x∈ [0, 1]\ Q and for y→x−, the
other cases being analogous. Let x = [0;b1,b 2,... ] and let h/k = [0;b1,b 2,...,b 2n,X,Y ] for
some X,Y ∈ N>0. Then, h/k→ x− as n→∞ , uniformly in X > b2n+1 and Y . We have
k/h≡ [0;b2,...,b 2n,X,Y ] (mod 1) and so by [8, (1.2)-(1.3) and Lemma 4]
1
h c0(k/h) = 1
π
2n+1∑
𝓁=1
(−1)𝓁 log(v𝓁−1/v𝓁)
v𝓁−1
+O(n)
uniformly in X,Y , where vi denotes the partial quotient of [0; b2,...,b 2n,X,Y ]. Now, let
B = 2 + max1≤i≤2nbi. Then, for 𝓁< 2n, we havev𝓁/v𝓁−1<B , whereasv2n/v2n−1 =X +O(1)
and v2n+1/v2n = Y +O(1). Also, v2n = Xv 2n−1 +v2n−2 and v2n−2≤ v2n−1≤ B2n−1. It
follows, that
π
h c0(k/h) = logY
Xv 2n−1 +v2n−2
− logX
v2n−1
+O(n logB) =−logX
v2n−1
(1 +o(1))
as n,X,Y →∞ under the constraint YnB 2n = o(logX). By (4.8) and [11, Theorem 1] we
then have
H∗
41(h/k) =−logX
v2n−1
(1 +o(1))(1 +O(1/Y )) +O
(
Y + logX
Yv 2n−1
)
and this goes to −∞ as n,X,Y →∞ with YnB 2n =o(logX). □
38 S. BETTIN AND S. DRAPPEAU
