---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-005-22-first-reciprocity-formula-for-the-q-pochhamme
section_title: "First reciprocity formula for the q-Pochhammer symbol"
section_number: 2.2
pages: 9-14
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
as follows. Let N,d ≥ 1 be coprime. Let α = p/q in reduced form, and γ =
(
p−q
q p
)
for
some (p,q) satisfying pp +qq = 1. Throughout the rest of Section 2.2, all error terms will be
allowed to depend on d and γ (but not on N). We write h =Np−dq, k =Nq +dp, so that
x = N
d, γ (x) = Np−dq
Nq +dp = h
k
and notice that this implies that ( h,k ) = 1 (since (h,k ) divides qh−pk =d and (d, (h,k )) =
(p,q ) = 1) and
h
k = p
q− d
kq,(2.2)
d
kq + k
dq = N
d − h
k + p +p
q .(2.3)
We also recall from [21, p.45] that the Dedekind sum s( α) is deﬁned by
(2.4) s(α) =s(p,q ) :=
q−1∑
n=1
n
q
((pn
q
))
, where ( (x) ) ={x}− 1
2,
Forz∈ (C\ R)∪ (0, 1), we let
(2.5) f(z) := log(1− e(z))
taking the determination which is real on the positive imaginary axis. Notice that with this
choice we have
f(z) = f(1−z) +πi(2z− 1); (2.6)
f(1 +z) = f(z), if Im(z)> 0; f(1 +z)− f(z) = 2πi, if Im(z)< 0;(2.7)
f(z) = log(2 sin(πz)) +iπ(z− 1
2) if z∈ (0, 1).(2.8)
Moreover, if t∈ (0, 1), expanding the logarithm in its Taylor series
(2.9)
q∑
g=1
f
(g−t
q
)
=−
q∑
g=1
∞∑
m=1
e(−tm/q) e(mg/q)
m =
∞∑
m=1
e(−mt)
m = f(1−t)
10 S. BETTIN AND S. DRAPPEAU
and the same formula holds for t∈ (C\ R)∪ (0, 1) by analytic continuation. Finally, for λ∈
(C\ R)∪ (0, 1), we let
(2.10) L(λ) =
∫ λ
0
f(1−t)dt− πi
12.
The function L is holomorphic in ( C\ R)∪ (0, 1). Note that Li 2(1) = π2/6, so that when-
ever Im(λ)< 0,
L(λ) =
∫ λ
0
f(1−t)dt− πi
12 = 1
2πi
∫ 1
e(−λ)
log(1−z)dz
z + Li2(1)
2πi = Li2(e(−λ))
2πi .
Before stating the main theorem of this section, we deﬁne
(2.11) Hκ(u,v ) := lim
ε→0+
(
i
∫
γε
f(u−itκ)dt
e(v)e2πt− 1−i
∫
γε
f(u +itκ)dt
e(−v)e2πt− 1
)
for κ> 0,u∈ [0, 1],v∈ R/Z. Notice that if v⁄∈ Z we have
(2.12) Hκ(u,v ) =i
∫ ∞
0
( f(u−itκ)
e(v)e2πt− 1− f(u +itκ)
e(−v)e2πt− 1
)
dt,
whereas if v∈ Z and 0 <u< 1 then
(2.13) Hκ(u, 0) =−1
2 f(u) +i
∫ ∞
0
f(u−itκ)− f(u +itκ)
e2πt− 1 dt,
as can seen by isolating the contribution of the two circular paths, which are both πi/2 times
the residue at 0.
Theorem 6. For 1≤r<k , letting L :=⌊rd/k⌋, and λ ={rd/k}, we have
(e(γx))r e(γx
24 )
(e(x))L e( x
24) = exp
(πi(p +p)
12q −πi s(p,q )− πi
4 + 1
2 logk
d + k
qd L(λ) +Er(λ,d/k )
)
,
where s is the Dedekind sum [21, p.45] and for λ∈ [0, 1), κ> 0 and, for s∈ Z/qZ,
Es(λ,κ ) :=−Hκ
(⟨ps⟩− λ
q , 0
)
−
q∑
g=1
g⁄≡ps (mod q)
i
∫ ∞
0
( f(g−λ
q −itκ)
e(gp−s
q )e2πt− 1
−
f(g−λ
q +itκ)
e(−gp−s
q )e2πt− 1
)
dt,
(2.14)
with⟨n⟩ indicating the representative of n (mod q) in [1,q ]. Moreover, for all s (mod q)
and κ∈ (0, 1], the function λ↦→E s(λ,κ ) is deﬁned and holomorphic in the strip {Re(λ)∈
[0, 1)}, and
Es(λ,κ )≪| log|1−λ|| + log(1/κ) (2.15)
uniformly for Re(λ)∈ [0, 1) and Im(λ)≪ 1.
Remark 4. If λ∈ (0, 1) or if s⁄≡ 0 (mod q) by (2.13) we can write Eλ as
Es(λ,κ ) := 1
2f
(⟨ps⟩− λ
q
)
−
q∑
g=1
i
∫ ∞
0
( f(g−λ
q −itκ)
e(gp−s
q )e2πt− 1
−
f(g−λ
q +itκ)
e(−gp−s
q )e2πt− 1
)
dt.(2.16)
We remark that if (q,d ) = 1 (i.e. (k,d ) = 1), one cannot have{rd/k} = 0.
Remark 5. Notice that by (2.3) we have e( γx
24 )/e( x
24)· exp(−πi(p+p)
12q ) = exp(−πi
12( d
kq + k
dq)).
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 11
In order to prove Theorem 6, we require some properties of the function Hκ(u,v ).
Lemma 3. We have :
(1) Hκ(1−u,−v) +Hκ(u,v ) =−2πiB1(u) ˜B1(v) +πiκ ˜B2(v) for v /∈ Z,
(2) Hκ(1,v )−Hκ(0,v ) = f({−v}) for v /∈ Z,
(3) Hκ(1, 0) =− log(κ)
2 − πi
4 + πiκ
12 .
Proof. Let v /∈ Z. By (2.6), Lemma 2 and (2.8) we have
Hκ(1−u,−v) +Hκ(u,v ) =i
∫ ∞
0
( f(1−u−itκ)
e(−v)e2πt− 1− f(1−u +itκ)
e(v)e2πt− 1
)
dt +
+i
∫ ∞
0
( f(u−itκ)
e(v)e2πt− 1− f(u +itκ)
e(−v)e2πt− 1
)
dt
=−
∫ ∞
0
((1− 2u)π− 2πitκ
e(−v)e2πt− 1 − (1− 2u)π + 2πitκ
e(v)e2πt− 1
)
dt
= 2πi(1− 2u) Im
∫ ∞
0
dt
e(v)e2πt− 1− 4πiκ Im
∫ ∞
0
−itdt
e(v)e2πt− 1
=−2πiB1(u) ˜B1(v) +πiκ ˜B2(v).
Also, by (2.7), we have
Hκ(1,v )−Hκ(0,v ) =i
∫ ∞
0
( f(1−itκ)
e(v)e2πt− 1− f(1 +itκ)
e(−v)e2πt− 1
)
dt +
+i
∫ ∞
0
( f(−itκ)
e(v)e2πt− 1− f(itκ)
e(−v)e2πt− 1
)
dt
=−
∫ ∞
0
2π
e(v)e2πt− 1dt = f({−v}).
Finally, by (2.6) and (2.7) as ε→ 0+ we have
i
∫
γε
f(1−itκ)dt
e2πt− 1 −i
∫
γε
f(1 +itκ)dt
e2πt− 1
=i
∫
γε
f(itκ)dt
e2πt− 1−i
∫
γε
f(itκ)dt
e2πt− 1−
∫
γε
πdt
e2πt− 1 +
∫ ∞
0
2πitκdt
e2πt− 1 +o(1).
The last two integrals can be easily computed and contribute−iπ
4 + log(2πε)
2 and πiκ
12 respectively.
The contributions of the interval ( ε,∞) in the ﬁrst two integral cancel out. Thus, since
f(itκ) = log(2πtκ) +o(1) as |t|→ 0 with −π/2 < argt < π/2, we have that the ﬁrst two
integral contribute
i
∫
Cε
log(2πtκ)dt
e2πt− 1 =−log(2πεκ)
2 +o(1)
where Cε is the semicircle centered at the origin going from −iε to iε counter-clockwise. We
then have
Hκ(1, 0) =−logκ
2 − iπ
4 + πiκ
12 .
□
Lemma 4. Let 0<κ ≤ 1, Re(u)∈ [0, 1],v∈ R/Z with u⁄= 0, 1, and A≥ 1. Then
Hκ(u,v ) =− log|u| +Ov,A(log(2/κ))
12 S. BETTIN AND S. DRAPPEAU
uniformly in u,κ with Im(u)≤A.
Proof. The case v /∈ Z, Re(u)∈ [0, 1] is an easy consequence of the bound
f(x +it)≪|t| +| log|t||, (x∈ [0, 1],t∈ R⁄=0).(2.17)
Now assume v∈ Z and Re(u)∈ (0, 1/2]. We recall (2.13). By (2.17) the contribution to the
integral from the interval [2A,∞) is O(log(2/κ)). Next, we write
I(u,κ ) :=i
∫ 2A
0
f(u−itκ)− f(u +itκ)
e2πt− 1 dt =−πi
∫ 2A
0
∫ u+itκ
u−itκ
(cot(πz) +i)dz dt
e2πt− 1.
Note that cot(πz) = 1/(πz)+O(1) uniformly for Re(z)∈ [0, 1/2], and that 1
e2πt−1 = 1
2πt +O(1)
for t> 0. Therefore,
I(u,κ ) = 1
2πi
∫ 2A
0
∫ u+itκ
u−itκ
dz
z
dt
t +OA(log(2/κ)).
Changing variables z←|u|z and t←t|u|/κ, we get
I(u,κ ) = 1
2πi
∫ 2Aκ/|u|
0
∫ u′+it
u′−it
dz
z
dt
t +OA(log(2/κ)),
where|u′| = 1. For t≤ 1/2, we may bound the z-integral by O(t), while for t≥ 2, we
have
∫u′+it
u′−it
dz
z =πi +O(1/t). We deduce
I(u,κ ) = 1
2πi
∫ 2
1/2
∫ u′+it
u′−it
dz
z
dt
t +OA(log(2/κ))− 1
2 log|u|.
The double integral here is bounded independently of u′, and so ﬁnally
I(u,κ ) =OA(log(2/κ))− 1
2 log|u|.
We deduce Hκ(u, 0) = − log|u| +OA(log(2/κ)) for 0 ≤ Re(u)≤ 1/2, u⁄= 0. On the other
hand, by computations similar to Lemma 3, we get
Hκ(1−u, 0) +Hκ(u, 0) =−f(u)− πi
2 (2u− 1)− πiκ
6 ,
from which we get the claimed behaviour for all u. □
Proof of Theorem 6. For 0≤𝓁≤L, let r𝓁 =𝓁k/d. We split (e(γx))r as (e(γx))r =∏L
𝓁=0PL
𝓁 ,
where for 0≤𝓁<L ,
PL
𝓁 =
∏
r𝓁<n≤r𝓁+1
(
1− e
(nh
k
))
and PL
L =
∏
r𝓁<n≤r
(
1− e
(nh
k
))
.
First we focus on the case 0 ≤𝓁<L . By (2.2) and by periodicity we have
PL
𝓁 =
∏
r𝓁<n≤r𝓁+1
(
1− e
(np
q − nd
kq
))
=
q∏
a=1
∏
r𝓁−a
q <m≤
r𝓁+1−a
q
(
1− e
(ap
q − d(a +mq)
kq
))
=
q∏
a=1
∏
r𝓁−a
q <m≤
r𝓁+1−a
q
(
1− e
(ga
q − d(a +mq)
kq
))
,
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 13
wherega is the representative of the class pa (mod q) contained in [𝓁 + 1,𝓁 +q], so that in the
last line each e( ) is computed at a number in (0 , 1). It follows that we can write
PL
𝓁 = exp
( q∑
a=1
∑
r𝓁−a
q <m≤
r𝓁+1−a
q
f
(ga
q − d(a +mq)
kq
))
and that 0 < ga
q − dr𝓁+1
kq < 1 whenever r𝓁+1−a
q is an integer. We can then apply Abel-Plana
formula in the form of Lemma 1. Note that
q∑
a=1
∫ r𝓁+1−a
q
r𝓁−a
q
f
(ga
q − d(a +tq)
kq
)
dt = k
qd
q∑
a=1
∫ 𝓁+1
𝓁
f
(ga
q − t
q
)
dt
= k
qd
q∑
g=1
∫ 1
0
f
(g−t
q
)
dt = k
qd
∫ 1
0
f(1−t)dt = 0
by (2.9). Therefore, by Lemma 1, equation (2.11) and the deﬁnition of r𝓁,
PL
𝓁 = exp
( q∑
a=1
Hd/k
(ga
q − 𝓁
q,a
q− 𝓁k
qd
)
−
q∑
a=1
Hd/k
(ga
q − 𝓁 + 1
q ,a
q− (𝓁 + 1)k
qd
))
.
Now, k
qd = N
d + p
q and 1≤ga−𝓁≤q with pa≡ga (mod q), thus by a change of variable and
multiplying this equality over 0≤𝓁<L , we get
L−1∏
𝓁=0
PL
𝓁 = exp
(L−1∑
𝓁=0
( q∑
g=1
Hd/k
(g
q,gp
q − 𝓁N
d
)
−
q−1∑
g=0
Hd/k
(g
q,gp
q − (𝓁 + 1)N
d
)))
= exp
(L−1∑
𝓁=0
(
Hd/k
(
1,−𝓁N
d
)
−Hd/k
(
0,−(𝓁 + 1)N
d
))
(2.18)
+
q−1∑
g=1
(
Hd/k
(g
q,gp
q
)
−Hd/k
(g
q,gp
q − LN
d
)))
.
We treatPL
L in the same way. First,
PL
L = exp
( q∑
a=1
∑
rL−a
q <m≤r−a
q
f
(ga
q − d(a +mq)
kq
))
.
Note that by (2.9) and (2.10)
q∑
a=1
∫ (r−a)/q
(rL−a)/q
f
(ga
q − d(a +qt)
kq
)
dt = k
qd
q∑
a=1
∫ L+λ
L
f
(ga
q − t
q
)
dt
= k
qd
∫ λ
0
f(1−t)dt = k
qd L(λ) + πik
12qd
where we recall that λ ={rd/k}. Applying Lemma 1, we therefore ﬁnd
(2.19) PL
L = exp
( k
qd L(λ) + πik
12qd +
q∑
g=1
(
Hd/k
(g
q,gp
q − LN
d
)
−Hd/k
(g−λ
q ,gp−r
q
)))
.
14 S. BETTIN AND S. DRAPPEAU
Multiplying the equalities (2.18) and (2.19) and recalling that (e(γx))r =∏L
𝓁=0PL
𝓁 , we obtain
(e(γx))r = exp
( k
qd L(λ) + πik
12qd +
q−1∑
g=1
Hd/k
(g
q,gp
q
)
−
q∑
g=1
Hd/k
(g−λ
q ,gp−r
q
)
+
+Hd/k(1, 0) +
∑
1≤𝓁≤L
(
Hd/k(1,−𝓁N
d )−Hd/k(0,−𝓁N
d )
))
.
By Lemma 3 (1) we have
q−1∑
g=1
Hd/k
(g
q,gp
q
)
=−πi
q−1∑
g=1
˜B1
(g
q
)
˜B1
(gp
q
)
+ πid
2k
q−1∑
g=1
˜B2
(g
q
)
=−πi s(p,q ) + πid
12kq− πid
12k
since∑q−1
g=0B2(g/q) = 1
6q andB2(0) = 1/6. Also, by Lemma 3 (3) and (2) we haveHd/k(1, 0) =
log(k/d)
2 − πi
4 + πid
12k and
∑
1≤𝓁≤L
(
Hd/k(1,−𝓁N
d )−Hd/k(0,−𝓁N
d )
)
=
∑
1≤𝓁≤L
f({𝓁N/d}).
Thus,
(e(γx))r = (e(N/d))L exp
( k
qd L(λ) + 1
2 logk
d−
q∑
g=1
Hd/k
(g−λ
q ,gp−r
q
)
+
−πi s(p,q )− πi
4 + πid
12kq + πik
12qd
)
.
By (2.3) and (2.12) we then obtain the claimed result. The bound (2.15) follows by Lemma 4.
□
