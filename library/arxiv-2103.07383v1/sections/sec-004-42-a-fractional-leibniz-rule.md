---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-004-42-a-fractional-leibniz-rule
section_title: "A fractional Leibniz rule"
section_number: 4.2
pages: 10-18
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
The remainder termR(p) contains amongst others the factorΓ, which is basically given as a
product of two functions multiplied with a singular weight. By applying a Bessel potential space
norm, we obtain a sort of fractional Leibniz rule which will subsequently be discussed forΓ and
its derivatives.
10
We observe that thel-th derivative ofR(p) leads tok-th derivatives ofΓ, wherek≤l + 1.
Applying the generalized Leibniz rule to thek-th derivative ofΓ in the next step, we obtain
dk
duk Γ(u,v,w,s 1,s 2) = 1
|v|p−2|w|p−2|v−w|p
·
k∑
o=0
(k
o
{(
γ(k−o+1)(u +x1)−γ(k−o+1)(u +x2)
{
⊗
(
γ(o+1)(u +x3)−γ(o+1)(u +x4)
{
,
where we have the four cases
Case 1: (x1,x 2,x 3,x 4) = (s1w,s 1v,s 2w,s 2v),
Case 2: (x1,x 2) = (x3,x 4) = (s1w,s 2w),
Case 3: (x1,x 2) = (x3,x 4) = (s1v,s 2v),
Case 4: (x1,x 2) = (x3,x 4) = (v +s1(w−v),v +s2(w−v)).
The key observation here is thatΓ as well as its derivatives can be broken down into sums of
products of the form
(
γ(k−o+1)
i (u +x1)−γ(k−o+1)
i (u +x2)
{
·
(
γ(o+1)
j (u +x3)−γ(o+1)
j (u +x4)
{
,
where i,j = 1,...,n and o = 0,...,k. The diﬀerence in the component functions and the
additional factor|v|2−p|w|2−p|v−w|−p indicate a fractional derivative of the arising products.
This motivates to deduce the following general statement, which can therefore be interpreted as
fractional Leibniz rule.
Theorem 4.4. Let m > 1
2, s1,s 2∈[0, 1] and p∈( 7
3, 8
3). Then there exists a positive constant
CL =CL(m,p )<∞such that for allf,g ∈C∞(R/Z, R)

D
‖(f(·+x1)−f(·+x2)) (g(·+x3)−g(·+x4))‖H m
|v|p−2|w|p−2|v−w|p dv dw
≤CL(‖f‖H m+ 3
2 p−3‖g‖H m+ 3
2 p−3),
where
Case 1: (x1,x 2,x 3,x 4) = (s1w,s 1v,s 2w,s 2v),
Case 2: (x1,x 2) = (x3,x 4) = (s1w,s 2w),
Case 3: (x1,x 2) = (x3,x 4) = (s1v,s 2v),
Case 4: (x1,x 2) = (x3,x 4) = (v +s1(w−v),v +s2(w−v)).
Proof. We ﬁrst of all note thatHm is a Banach algebra due tom> 1
2 (see (3)), which implies

D
‖(f(·+x1)−f(·+x2)) (g(·+x3)−g(·+x4))‖H m
|v|p−2|w|p−2|v−w|p dv dw
≤C(m)

D
‖f(·+x1)−f(·+x2)‖H m‖g(·+x3)−g(·+x4)‖H m
|v|p−2|w|p−2|v−w|p dv dw
≤C(m)



D
‖f(·+x1)−f(·+x2)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
(
(
1
2



D
‖g(·+x3)−g(·+x4)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
(
(
1
2
11
for some positive constantC(m) only depending onm.
We start withCase 1. We ﬁrst see by the deﬁnition of the fractional Sobolev norm that

D
‖f(·+s1w)−f(·+s1v)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
=

D
∑
k∈Z
(1 +k2)m|( ˆf(·+s1w)−f(·+s1v))(k)|2 dv dw
|v|p−2|w|p−2|v−w|p.
By substitution and the periodicity off, we can rewrite the Fourier coeﬃcients to
| ˆ(f(·+s1w)−f(·+s1v))(k)|=
⏐⏐⏐⏐⏐⏐
1
0
(f(u +s1w)−f(u +s1v))e−2πikudu
⏐⏐⏐⏐⏐⏐
=
⏐⏐e2πiks1w⏐⏐
⏐⏐⏐⏐⏐⏐
1
0
(f(u)−f(u +s1(v−w)))e−2πikudu
⏐⏐⏐⏐⏐⏐
=|( ˆf(·+s1(v−w))−f(·))(k)|, (6)
which implies
‖f(·+s1w)−f(·+s1v)‖H m =‖f(·+s1(v−w))−f(·)‖H m.
Then, as in the proof of [BR15, Lemma 4.4], respectively [BR15, Lemma 1], we substitute with
Φ : ( v,w )↦→(t, ˜w) := ( v
v−w,s 1(v−w)),|detDΦ(v,w )|= s1
|v−w|, Φ(D)⊂[0, 1]×[−1, 0], such
that

D
‖f(·+s1w)−f(·+s1v)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
=

D
‖f(·+s1(v−w))−f(·)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
≤s−1
1
1
0
0
−1
‖f(·+ ˜w)−f(·)‖2
H m
|t ˜w
s1
|p−2|(t−1) ˜w
s1
|p−2|˜w
s1
|p−1 d ˜w dt
=s3p−6
1


0
−1
‖f(·+ ˜w)−f(·)‖2
H m
|˜w|3p−5 d ˜w
(
(


1
0
dt
|t(1−t)|p−2
(
(
/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
<∞
≤C(p)
0
−1
‖f(·+ ˜w)−f(·)‖2
H m
|˜w|3p−5 d ˜w.
Note that the positive constant C(p) in the previous estimate does not depend on s1 since
3p−6> 1 and by deﬁnition0≤s1≤1.
Now we ﬁnd again by the deﬁnition of the fractional Sobolev norm
0
−1
‖f(·+ ˜w)−f(·)‖2
H m
|˜w|3p−5 d ˜w =
0
−1
∑
k∈Z
(1 +k2)m|( ˆf(·+ ˜w)−f(·))(k)|2 d ˜w
|˜w|3p−5,
12
whose Fourier coeﬃcients have the form
⏐⏐⏐( ˆf(·+ ˜w)−f(·))(k)
⏐⏐⏐
2
=
⏐⏐⏐⏐⏐⏐
1
0
f(u + ˜w)e−2πikudu−
1
0
f(u)e−2πikudu
⏐⏐⏐⏐⏐⏐
2
=|e2πik˜w−1|2|ˆf(k)|2.
Since we get by Euler’s formula
0
−1
|e2πik˜w−1|2 d ˜w
|˜w|3p−5 = 2
1
0
(1−cos(2πk˜w)) d ˜w
˜w3p−5
≤2(2π|k|)3p−6
∞
0
1−cos( ¯w)
¯w3p−5 d ¯w
/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
<∞
≤⟨C(p)|k|3p−6,
(7)
for some positive constant⟨C(p) only depending onp, as well as the elementary inequality
|k|3p−6≤(1 +k2)
3p−6
2 , (8)
we obtain together with Beppo Levi’s monotone convergence theorem
0
−1
‖f(·+ ˜w)−f(·)‖2
H m
|˜w|3p−5 d ˜w =
0
−1
∑
k∈Z
(1 +k2)m|ˆf(k)|2|e2πikw−1|2 d ˜w
|w|3p−5
≤⟨C(p)
∑
k∈Z
(1 +k2)m+ 3
2p−3|ˆf(k)|2
= ⟨C(p)‖f‖2
H m+ 3
2 p−3.
After applying the same reasoning for the second factor, we ﬁnally achieve forCase 1

D
‖(f(·+s1w)−f(·+s1v)) (g(·+s2w)−g(·+s2v))‖H m
|v|p−2|w|p−2|v−w|p dv dw
≤C(m,p )‖f‖H m+ 3
2 p−3‖g‖H m+ 3
2 p−3,
for some new positive constantC(m,p ) depending onm and p.
13
In Case 2, we start by change of variables, cf. the proof of [BR15, Lemma 4.4], such that

D
‖f(·+s1w)−f(·+s2w)‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
≤
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
wp−2

)
2
3−w
0
1
vp−2(v +w)p dv
(
( dw
≤
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
wp−2


∞
0
1
(tw)p−2(w(t + 1))pw dt
(
( dw
≤
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
w3p−5


∞
0
1
tp−2(1 +t)p dt
(
(
/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
<∞
dw
≤C(p)
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
w3p−5 dw, (9)
whereC(p) is a positive constant depending onp. The deﬁnition of the fractional Sobolev norm
gives us
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
w3p−5 dw =
2
3
0
∑
k∈Z
(1 +k2)m|( ˆf(·+s1w)−f(·+s2w))(k)|2 dw
w3p−5.
We then observe for the Fourier coeﬃcients of the series, recalling of the periodicity off,
|( ˆf(·+s1w)−f(·+s2w))(k)|2 =
⏐⏐⏐⏐⏐⏐
1
0
f(u +s1w)e−2πikudu−
1
0
f(u +s2w)e−2πikudu
⏐⏐⏐⏐⏐⏐
2
=|e2πiks1w ˆf(k)−e2πiks2w ˆf(k)|2
=|e2πik(s1−s2)w−1|2|e2πiks2w|2|ˆf(k)|2,
and hence
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
w3p−5 dw =
2
3
0
∑
k∈Z
(1 +k2)m|ˆf(k)|2|e2πik(s1−s2)w−1|2 dw
w3p−5.
Now again by Euler’s formula and change of variables, we get similarly to (7)
2
3
0
|e2πik(s1−s2)w−1|2 dw
w3p−5 = 2
2
3
0
1−cos(2πk(s1−s2)w) dw
w3p−5≤⟨C(p)|k|3p−6
14
where ⟨C(p) is a positive constant depending onp and we used that|s1−s2|≤2. Therefore, we
obtain by (8) and Beppo Levi’s monotone convergence theorem
2
3
0
‖f(·+s1w)−f(·+s2w)‖2
H m
w3p−5 dw≤⟨C(p)
∑
k∈Z
(1 +k2)m+ 3
2p−3|ˆf(k)|2
= ⟨C(p)‖f‖2
H m+ 3
2 p−3. (10)
After applying the same arguments for the factor ofg, we conclude inCase 2

D
‖(f(·+s1w)−f(·+s2w)) (g(·+s1w)−g(·+s2w))‖H m
|v|p−2|w|p−2|v−w|p dv dw
≤C(m,p )‖f‖H m+ 3
2 p−3‖g‖H m+ 3
2 p−3
for some positive constantC(m,p ) depending onm and p.
Case 3directly follows fromCase 2.
Now onlyCase 4remains. Along the lines ofCase 1and Case 2, in particular (6) and (9), we
transform with respect of the Fourier coeﬃcients

D
‖f(·+v +s1(w−v))−f(·+v +s2(w−v))‖2
H m
|v|p−2|w|p−2|v−w|p dv dw
≤
2/3
0
2/3−w
0
‖f(·+s1(w +v))−f(·+s2(w +v))‖2
H m
|w|p−2
( 1
vp−2(v +w)p
{
dv dw
≤
2/3
0
‖f(·+s1 ˜w)−f(·+s2 ˜w)‖2
H m
˜w3p−5


∞
0
1
tp−2(1 +t)p dt
(
(
/∏⟨hti⨂u⨂l⟨⟩t/∏⟨hti⨂own∏ight/∏⟨hti⨂ownl⟨⟩t/∏⟨hti⨂u⨂∏ight
<∞
d ˜w.
We are now in the position to apply (10) and the statement forCase 4

D
‖(f(·+v +s1(w−v))−f(·+v +s1(w−v)))·
·(g(·+v +s1(w−v))−g(·+v +s1(w−v)))‖H m
dv dw
|v|p−2|w|p−2|v−w|p
≤C(m,p )‖f‖H m+ 3
2 p−3‖g‖H m+ 3
2 p−3
for some positive constantC(m,p ) only dependent onm and p follows.
4.3 Estimate of the remainder term ⟨R(p)
We may ﬁnd an estimate for of∂l⟨R(p)(γ) with respect to a fractional Sobolev norm.
15
Lemma 4.5. Letγ∈C∞(R/Z, Rn) be parametrized by arc-length andm> 1
2. Then there exist
constantsC =C(γ,m,n,p)> 0 and r =r(γ,m,n,p)> 0 such that
‖∂l⟨R(p)(γ)‖H m
≤C
∑
j1+...+jK−1=l+1
( l + 1
j1,...,jK−1
{
p(3n)
j1
({ (|α|+ 1)!
r|α|+1
}
|α|≤j1
,{‖γ(j+1)‖H m+ 3
2 p−3}j=1,...,j1
i=1,...,3n
(
·
K−1
i=2
‖γ(ji+1)‖H m+ 3
2 p−3.
Note that the second set of coeﬃcients ofp(3n)
j1 is independent ofi, we need that parameter only
for dimensional reasons.
Proof. First note thatG(p)◦|.|is an analytic function away from zero and by the fundamental
theorem of calculus
G(p)
(|∆ v,wγ|
|v−w|,|∆ v,0γ|
|v|,|∆ w,0γ|
|w|
{
= (G(p)◦|.|)


1
0
γ′(u +tw) dt,
1
0
γ′(u +tv) dt,
1
0
γ′(u +t(w−v)) dt
(
(.
Now by the generalized Leibniz formula and Faà di Bruno’s formula as in Lemma B.1, we observe
dl+1
dul+1gp
k(u,v,w ;s1,...,sK−2)
=
∑
k1+...+kK−2=l+1
( l + 1
k1,...,kK−2
{
·p(3n)
k1
(
}
∂α(G(p)◦|.|)


1
0
γ′(u +tw) dt,
1
0
γ′(u +tv) dt,
1
0
γ′(u +t(w−v)) dt
(
(


{
|α|≤k1
,

}

1
0
γ(j+1)
i (u +t(x−y)) dt


{
i=1,...,n,j=1,...,k1,
(x,y)=(v,w),(v,0),(w,0)
(
·dk2
duk2
Γ(u,v,w,s 1,s 2)
·
(K1⨂
i=3
γ(ki+1)(u +siv)
(
⊗
( K2⨂
i=K1+1
γ(ki+1)(u +siw)
(
⊗
( K−2⨂
i=K2+1
γ(ki+1)(u +v +si(w−v))
(
.
We then apply theHm-norm on∂l⟨R(p)(γ) for somem > 1
2 and obtain by the Banach algebra
16
property ofHm(R/Z, Rn), cf. (3), together with Lemma B.3 that
‖‖‖∂l⟨R(p)(γ)
‖‖‖
H m
≤c(m,n,p )
kmax∑
k=1

D

···

[0,1]K
‖‖∂l+1gp
k(·,v,w ;s1,...,sK−2)
‖‖
H m dθ1···dθK dv dw
≤˜c(m,n,p,K )
kmax∑
k=1

D

···

[0,1]K
∑
k1+...+kK−2=l+1
( l + 1
k1,...,kK−2
{
·p(3n)
k1
(
}
b|α|
‖‖‖‖‖‖
∂α(G(p)◦|.|)


1
0
γ′(·+tw) dt,
1
0
γ′(·+tv) dt,
1
0
γ′(·+t(w−v)) dt
(
(
‖‖‖‖‖‖
H m


{
|α|≤k1
,

}

‖‖‖‖‖‖
1
0
γ(j+1)
i (·+t(x−y)) dt
‖‖‖‖‖‖
H m


{
i=1,...,n,j=1,...,k1,
(x,y)=(v,w),(v,0),(w,0)
(
·
‖‖∂k2Γ(·,v,w,s 1,s 2)
‖‖
H m·
K−2
i=3
‖‖‖γ(ki+1)
‖‖‖
H m
dθ1···dθK dv dw
(11)
where b = b(m) := sup η1,η2∈H m(R/Z,R)
‖η1‖Hm‖η2‖Hm
‖η1η2‖Hm is a ﬁnite constant stemming from the
Banach algebra property andc(n,m,p ) is an upper bound for the operator norms of·⊗eo :
Hm(R/Z, Rn)→Hm(R/Z, Rn).
Since G(p)◦|.|is an analytic function away from the origin andγis smooth with bounded
bilipschitz constant [BR15, Proposition 2.1], we get from the proof of [BV19, Lemma 7.2] that
b|α|
‖‖‖‖‖‖
∂α(G(p)◦|.|)


1
0
γ′(·+tw) dt,
1
0
γ′(·+tv) dt,
1
0
γ′(·+t(w−v)) dt
(
(
‖‖‖‖‖‖
H m
≤CG
(|α|+ 1)!
r|α|+1
for some positive constants CG = CG(γ,m,n,p) and r = r(γ,m,n,p) which also absorb b.
Furthermore, we have by the triangle inequality
‖‖‖‖‖‖
1
0
γ(j+1)
i (·+t(x−y)) dt
‖‖‖‖‖‖
H m
≤‖γ(j+1)
i ‖H m≤‖γ(j+1)‖H m.
Note that these bounds are independent ofs3,...,sK−2.
To estimate the term

D

[0,1]2
‖‖∂k2Γ(·,v,w,s 1,s 2)
‖‖
H m dθ1 dθ2 dw dv, we ﬁrst observe by
the generalized Leibniz rule
dk2
duk2
Γ(u,v,w,s 1,s 2) = 1
|v|p−2|w|p−2|v−w|p
·
k2∑
o=0
(k2
o
{(
γ(k2−o+1)(u +x1)−γ(k2−o+1)(u +x2)
{
⊗
(
γ(o+1)(u +x3)−γ(o+1)(u +x4)
{
,
17
where we have the four cases
Case 1: (x1,x 2,x 3,x 4) = (s1w,s 1v,s 2w,s 2v),
Case 2: (x1,x 2) = (x3,x 4) = (s1w,s 2w),
Case 3: (x1,x 2) = (x3,x 4) = (s1v,s 2v),
Case 4: (x1,x 2) = (x3,x 4) = (v +s1(w−v),v +s2(w−v)).
Hence we get by Theorem 4.4

[0,1]2

D
‖‖∂k2Γ(·,v,w,s 1,s 2)
‖‖
H m dw dv dθ1 dθ2
≤C(m,n,p )
n∑
i=1
n∑
j=1
k2∑
o=0
(k2
o
{
[0,1]2

D
1
|v|p−2|w|p−2|v−w|p
·‖γ(k2−o+1)
i (·+x1)−γ(k2−o+1)
i (·+x2)‖H m‖γ(o+1)
j (·+x3)−γ(o+1)
j (·+x4)‖H m dw dv dθ1 dθ2
≤⟨C(m,n,p )
n∑
i=1
n∑
j=1
k2∑
o=0
(k2
o
{
[0,1]2
‖γ(k2−o+1)
i ‖H m+ 3
2 p−3‖γ(o+1)
j ‖H m+ 3
2 p−3 dθ1 dθ2
≤⟨C(m,n,p )
k2∑
o=0
(k2
o
{
‖γ(k2−o+1)‖H m+ 3
2 p−3‖γ(o+1)‖H m+ 3
2 p−3
where C(m,n,p ) is an upper bound for the operator norms ofei⊗ej on (Hm(R/Z, R))2. We
may combine the sum overo and the binomial coeﬃcient
(k2
o
{
with the sum overk1,...,kK−2
and the multinomial coeﬃcient
( l+1
k1,...,kK−2
{
from (11) into the sum overj1 +...+jK−1 and the
multinomial coeﬃcient
( l+1
j1,...,jK−1
{
by settingj2 :=o, jK−1 :=k2−o andji :=ki for all otheri.
This allows us to integrate the two derivatives ofγinto the bigger product.
Then, the statement follows from the embeddingHs(R/Z, Cn)⊆Ht(R/Z, Cn) for anys>t ,
s,t≥0. Since these estimates are uniform over allgk, we may use an additional factor ofkmax
in order to leave out the sum.
Note thatΓ is the only term for whose upper bound we need the higher-orderHm+ 3
2p−3-norms.
We estimated allHm-norms by these in order to get a simpler structure which will serve us in
the proof of the main theorem, especially in Lemma 5.2.
