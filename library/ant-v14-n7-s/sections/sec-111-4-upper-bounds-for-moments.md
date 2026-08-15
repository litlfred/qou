---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-111-4-upper-bounds-for-moments
section_title: "Upper bounds for moments"
section_number: 4
pages: 206-225
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1873
ﬁnd that
S(V⁄= 0)≪ q(X+Y)/2g11 ∑
c2≤Z
c1+2c2≤2g+1
∑
C1∈Mc1
C2∈Mc2
C1|1
τ(C)τ10(C)√|C|
≪ q(X+Y)/2g11 ∑
C2∈M≤Z
τ(C2)τ10(C2)√|g(C2)| ≪ q(X+Y+Z)/2g30,
which ﬁnishes the proof of Lemma 3.4. □
Proposition 3.1 follows upon combining the estimates and choosing Z= g−(X+ Y)/4.
4. Upper bounds for moments
The aim of this section is to bound the tails of the Dirichlet series in the approximate functional equations
in Lemmas 2.2 and 2.3. We start with the following upper bounds for moments.
Theorem 4.1. Let k> 0, u= eiθ,v= eiγ withθ,γ ∈[ 0, 2π] and let m= deg(L(E⊗χD,w)) . Then
∑
D∈H∗
2g+1
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐
k
≪ε q2ggε exp
(
kM(u,v, m)+ k2
2 V(u,v, m)
)
uniformly for|α|,|β|≤ 1/g, where M(u,v, m) and V(u,v, m) are given by (4-9) and (4-11) respectively.
Remark 4.2. Note that the same upper bound as above holds if we replace L(E⊗χD,w) with
L(E⊗χD𝓁,w) for a ﬁxed polynomial 𝓁 with (𝓁,1)= 1. Since the proof of the upper bound for
this twisted moment is the same as the proof of Theorem 4.1, we only focus on 𝓁= 1.
We ﬁrst need the following proposition, whose proof is similar to the proof of Theorem 3.3 in [Altu ˘g
and Tsimerman 2014].
Proposition 4.3. Let D∈ H∗
2g+1 and let m= deg(L(E⊗χD,w)) . Then for h≤ m and z withℜ(z)≥ 0
we have
log
⏐⏐L
(
E⊗χD, 1
2+ z
)⏐⏐≤ m
h+ 1
hℜ
( ∑
j≥1
deg(P j)≤h
χD(P j)(α( P) j+β( P) j) log qh− j deg(P)
|P| j(1/2+z+1/(h log q)) log q j
)
.
Proof. We write
L(E⊗χD, s)=
m∏
j=1
(1−α jq1/2−s),
where|α j|= 1 (see [Hall et al. 2017]). Then
L′
L(E⊗χD, s)= log q
(
−m
2+
m∑
j=1
( 1
1−α jq1/2−s− 1
2
))
. (4-1)
1874 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We put s=σ+ z and integrate (4-1) with respect toσ from 1
2 toσ0, whereσ0> 1
2. Taking real parts
gives
log
⏐⏐L
(
E⊗χD, 1
2+ z
)⏐⏐− log|L(E⊗χD,σ 0+ z)|
= m log q
2
(
σ0− 1
2
)
− 1
2 logq
m∑
j=1
log qσ0−1/2− 2q−ℜ(z) cos(θ j− log qℑ(z))+ q1/2−σ0−2ℜ(z)
1+ q−2ℜ(z)− 2q−ℜ(z) cos(θ j− log qℑ(z)) ,
whereα j= eiθ j . We use the inequality log(1+ x)≥ x/(1+ x) for x> 0 and get that
log
⏐⏐L
(
E⊗χD, 1
2+ z
)⏐⏐− log|L(E⊗χD,σ 0+ z)|
≤ m log q
2
(
σ0− 1
2
)
− 1
2 logq
m∑
j=1
(1− q1/2−σ0−2ℜ(z))(1− q1/2−σ0)
1− 2q1/2−σ0−ℜ(z) cos(θ j− log qℑ(z))+ q1−2σ0−2ℜ(z)
= m log q
2
(
σ0− 1
2
)
− Gz(σ0)(1− q1/2−σ0−2ℜ(z))(1− q1/2−σ0)
(1− q1−2σ0−2ℜ(z)) log q , (4-2)
where
Gz(σ)= 1− q1−2σ−2ℜ(z)
2
m∑
j=1
1
1− 2q1/2−σ−ℜ(z) cos(θ j− log qℑ(z))+ q1−2σ−2ℜ(z). (4-3)
Now similarly as in [Altu ˘g and Tsimerman 2014] we compute the integral
1
2πi
∫ 2+2πi/ log q
2
− L′
L(E⊗χD,σ+ z+w) qhwq−w
(1− q−w)2 dw
in two different ways. First we write
− L′
L(E⊗χD, s)=
∑
n≥0
λD(n)
qns ,
and integrate term by term. Secondly we continue analytically to the left and pick up the residues. We
integrate with respect toσ fromσ0 to∞ and take real parts, which gives
− 1
(log q)2ℜ
(∑
n≤h
λD(n) log qh−n
qn(σ0+z) log qn
)
=− h
log q log|L(E⊗χD,σ 0+ z)|− 1
(log q)2ℜ
( L′
L(E⊗χD,σ 0+ z)
)
+
m∑
j=1
ℜ
(∫ ∞
σ0
(α jq1/2−σ0−z)hα−1
j qσ+z−1/2
(1−α−1
j qσ+z−1/2)2 dσ
)
. (4-4)
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1875
Now we have
ℜ
(∫ ∞
σ0
(α jq1/2−σ0−z)hα−1
j qσ+z−1/2
(1−α−1
j qσ+z−1/2)2 dσ
)
≤
∫ ∞
σ0
q(1/2−σ−ℜ(z))hqσ+ℜ(z)−1/2
|1−α−1
j qσ+z−1/2|2 dσ
=
∫ ∞
σ0
q(1/2−σ−ℜ(z))hq1/2−σ−ℜ(z)
1−2q1/2−σ−ℜ(z) cos(θ j−log qℑ(z))+q1−2σ−2ℜ(z) dσ.
By taking the derivative of
f(x)= q−x
1− 2q1/2−x−ℜ(z) cos(θ j− log qℑ(z))+ q1−2x−2ℜ(z)
we can see that f is decreasing on[σ0,∞). Hence
m∑
j=1
ℜ
(∫ ∞
σ0
(α jq1/2−σ0−z)hα−1
j qσ+z−1/2
(1−α−1
j qσ+z−1/2)2 dσ
)
≤
m∑
j=1
q1/2−σ0−ℜ(z)
1− 2q1/2−σ0−ℜ(z) cos(θ j− log qℑ(z))+ q1−2σ0−2ℜ(z)
∫ ∞
σ0
q(1/2−σ−ℜ(z))h dσ
= 2Gz(σ0)q(1/2−σ0−ℜ(z))hq1/2−σ0−ℜ(z)
(1− q1−2σ0−2ℜ(z)) log qh
≤ 2Gz(σ0)q(1/2−σ0−ℜ(z))h
(σ0+ℜ(z)− 1/2) log q log qh,
with Gz(σ0) as in (4-3). Now from (4-1) note that
ℜ
( L′
L(E⊗χD,σ 0+ z)
)
= log q
(
−m
2+ Gz(σ0)
)
.
Combining the equations above and (4-4) gives
log|L(E⊗χD,σ 0+ z)|
≤ 1
log qhℜ
(∑
n≤h
λD(n) log qh−n
qn(σ0+z) log qn
)
+ 1
h
(m
2− Gz(σ0)
)
+ 2Gz(σ0)q(1/2−σ0−ℜ(z))h
h(σ0+ℜ(z)− 1/2) log qh.
This and (4-2) lead to
log
⏐⏐L
(
E⊗χD, 1
2+ z
)⏐⏐
≤ m
2h+ m log q
2
(
σ0− 1
2
)
+ 1
log qhℜ
(∑
n≤h
λD(n) log qh−n
qn(σ0+z) log qn
)
+ Gz(σ0)
(
− 1
h+ 2q(1/2−σ0−ℜ(z))h
h(σ0+ℜ(z)− 1/2) log qh−(1− q1/2−σ0−2ℜ(z))(1− q1/2−σ0)
(1− q1−2σ0−2ℜ(z)) log q
)
.
1876 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Choosingσ0= 1
2+ 1/ log qh ensures that the coefﬁcient of Gz(σ0) is negative. Since
λD(n)= log q
∑
j| n
∑
deg(P j)=n
deg(P)χD(P) j(α( P) j+β( P) j),
the conclusion follows. □
Before proving Theorem 4.1, we also need the following lemma (see Lemma 8.4 in [Florea 2017a]).
Lemma 4.4. Let h, l be integers such that 2hl≤ 2g+ 1. For any complex numbers a(P) we have
∑
D∈H∗
2g+1
⏐⏐⏐⏐
∑
deg(P)≤h
χD(P)a(P)
|P|1/2
⏐⏐⏐⏐
2l
≪ q2g(2l)!
l!2l
( ∑
deg(P)≤h
|a(P)|2
|P|
)l
.
Let
N(V, u,v)=
⏐⏐⏐⏐
{
D∈ H∗
2g+1: log
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐≥ V+ M(u,v, m)
}⏐⏐⏐⏐.
We will prove the following lemma.
Lemma 4.5. If
√
log m≤ V≤ V(u,v, m), then
N(V, u,v)≪ q2g+1 exp
(
− V 2
2V(u,v, m)
(
1− 8
log logm
))
;
if V(u,v, m)< V≤ 1
13 log logmV(u,v, m), then
N(V, u,v)≪ q2g+1 exp
(
− V 2
2V(u,v, m)
(
1− 8V
V(u,v, m) log logm
)2)
;
if V > 1
13 log logmV(u,v, m), then
N(V, u,v)≪ q2g+1 exp
(
− V log V
4500
)
.
Using Lemma 4.5 above we can prove Theorem 4.1 as follows.
Proof of Theorem 4.1. We have the following.
∑
D∈H∗
2g+1
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐
k
=−
∫ ∞
−∞
exp(kV+ kM(u,v, m)) d N(V, u,v)
= k
∫ ∞
−∞
exp(kV+ kM(u,v, m))N(V, u,v) dV.
In the equation above we use Lemma 4.5 in the form
N(V, u,v)≪
{q2g+1mo(1) exp(−V 2/2V(u,v, m)) if V≤ 8kV(u,v, m),
q2g+1mo(1) exp(−4kV) if V > 8kV(u,v, m),
which ﬁnishes the proof of Theorem 4.1. □
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1877
Proof of Lemma 4.5. We assume without loss of generality that α,β are positive and real. Indeed, notice
that if α∈ C, since|α|≤ 1/g, we have|ℜ(α)|≤ 1/g and|ℑ(α)|≤ 1/g. The proof that follows goes
through in exactly the same way, withα replaced byℜ(α) andθ replaced byθ−ℑ(α) log q. Once we
assumeα is real, we can also assume that α is positive, since by the functional equation we have
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)⏐⏐⏐⏐= q−α(n+2 deg(D))
⏐⏐⏐⏐L
(
E⊗χD, 1
q1/2−αu
)⏐⏐⏐⏐.
Let
m
h= V
A and h0= h
log m,
where
A=



1
2 log logm if V≤ V(u,v, m),
1
2V(log logm)V(u,v, m) if V(u,v, m)< V≤ 1
16 log logmV(u,v, m),
8 if V > 1
16 log logmV(u,v, m).
Using Proposition 4.3 gives
log
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐
≤ 2m
h+ 1
hℜ
( ∑
j≥1
deg(P j)≤h
χD(P j)(α( P) j+β( P) j) log qh− j deg(P)
|P|(1/2+1/h log q) j log q j (|P|−(α−iθ/ log q) j+|P|−(β−iγ/ log q) j)
)
. (4-5)
Note that the contribution of the terms with j≥ 3 is bounded by O(1).
The terms with j= 2 in (4-5) will contribute, up to a term of size O(log logm) coming from those P
with P| D,
1
2
∑
deg(P)≤h/2
(h− 2 deg(P))(λ(P2)− 1)
h|P|1+2/h log q
(cos(2θ deg(P))
|P|2α + cos(2γ deg(P))
|P|2β
)
.
Let
Fα(h,θ)=
h∑
n=1
cos(2nθ)
nq 2nα+n/h log q.
Similarly as in [Florea 2017a, Lemma 9.1], we can show that
Fα(h,θ)= log min
{
h, 1
2θ
}
+ O(1), (4-6)
where forθ∈[ 0, 2π] we denoteθ= min{θ, 2π−θ}. Now using the fact that
∑
deg(P)≤h
λ(P2) cos(2θ deg(P))
|P|1+1/h log q = O(log logh), (4-7)
1878 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
it follows that the contribution from j= 2 will be equal to
−1
2
∑
deg(P)≤ h
2
h− 2 deg(P)
h|P|1+2/h log q
(cos(2θ deg(P))
|P|2α + cos(2γ deg(P))
|P|2β
)
+ O(log logm)
=− 1
2
(
Fα
(h
2,θ
)
+ Fβ
(h
2,γ
))
+ O(log logm)
≤− 1
2(Fα(m,θ)+ Fβ(m,γ))+ 2m
h + O(log logm)= M(u,v, m)+ 2m
h + O(log logm), (4-8)
where
M(u,v, m)=− 1
2
(
log min
{
m, 1
2θ
}
+ log min
{
m, 1
2γ
})
(4-9)
by formula (4-6). Note that in the second line of the equation above we used the fact that
Fα(m,θ)− Fα
(h
2,θ
)
=
m∑
n=1
cos(2nθ)
nq 2nαen/m−
h/2∑
n=1
cos(2nθ)
nq 2nαe2n/h,
and since e−x= 1+ O(x), it follows that
Fα(m,θ)− Fα
(h
2,θ
)
=
m∑
n=h/2+1
cos(2nθ)
nq 2nα + O(1)≤ 2m
h + O(1).
Hence, using (4-8) in (4-5) we get
log
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐
≤ M(u,v, m)+ 5m
h +
∑
deg(P)≤h
(h− deg(P))χD(P)λ(P)
h|P|1/2+1/(h log q)
(cos(θ deg(P))
|P|α + cos(γ deg(P))
|P|β
)
.
Let S1 be the sum above truncated atdeg(P)≤ h0 and S2 be the sum over primes withh0< deg(P)≤ h.
If D is such that
log
⏐⏐⏐⏐L
(
E⊗χD, u
q1/2+α
)
L
(
E⊗χD, v
q1/2+β
)⏐⏐⏐⏐≥ M(u,v, m)+ V,
then
S1≥ V1:= V
(
1− 6
A
)
or S2≥ V
A.
Let
F1={ D∈ H∗
2g+1: S1≥ V1} and F2=
{
D∈ H∗
2g+1: S2≥ V
A
}
.
If D∈ F2, then by Markov’s inequality and Lemma 4.4 it follows that
|F2|≪ q2g(2l)!
l!2l
( A
V
)2l( ∑
h0<deg(P)≤h
|a(P)|2
|P|
)l
,
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1879
for any l≤ g/h where
a(P)=(h− deg(P))λ(P)
h|P|1/(h log q)
(cos(θ deg(P))
|P|α + cos(γ deg(P))
|P|β
)
.
Picking l=[ g/h] and noting that a(P)≪ 1 and m= 4g+ O(1), we get that
|F2|≪ q2g
(2l
e
)l( A
V
)2l
(log logm)l≪ q2g exp
(
− V log V
8A
)
. (4-10)
If D∈ F1 then for any l≤ g/h0, we have
|F1|≪ q2g(2l)!
l!2l
1
V 2l
1
( ∑
deg(P)≤h0
|a(P)|2
|P|
)l
.
Using the expression for a(P) and (4-7) we get that
|F1|≪ q2g (2l)!
l!2l V 2l
1
(V(u,v, m)+ O(log logm))l,
where
V(u,v, m)
= log m+ 1
2(Fα(m,θ)+Fβ(m,γ))+F(α+β)/2
(
m,θ+γ
2
)
+F(α+β)/2
(
m,θ−γ
2
)
= log m+ 1
2
(
log min
{
m, 1
2θ
}
+log min
{
m, 1
2γ
})
+log min
{
m, 1
θ+γ
}
+log min
{
m, 1
θ−γ
}
, (4-11)
and the last line of the equation above follows from (4-6). Then
|F1|≪ q2g
( 2l
eV 2
1
(V(u,v, m)+ O(log logm))
)l
.
If V≤ V(u,v, m)2, then we pick l=[ V 2
1/2V(u,v, m)], and if V > V(u,v, m)2, then we pick l=[ 10V].
In doing so we get
|F1|≪ q2g exp
(
− V 2
1
2V(u,v, m)
)
+ q2g exp(−V log V). (4-12)
Combining the bounds (4-12) and (4-10) ﬁnishes the proof of Lemma 4.5. □
The following is an immediate corollary of Theorem 4.1.
Corollary 4.6. Let u= eiθ andv= eiγ withθ,γ ∈[ 0, 2π]. Then
∑
D∈H∗
2g+1
⏐⏐⏐⏐L
(
E⊗χD, u√q
)
L
(
E⊗χD, v√q
)⏐⏐⏐⏐
≪ε q2gg1/2+ε min
{
g, 1
2θ
}−1/4
min
{
g, 1
2γ
}−1/4
min
{
g, 1
(θ−γ)
}1/2
min
{
g, 1
(θ+γ)
}1/2
.
1880 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
For N|1∞ and ﬁxed n∈ N, we deﬁne the truncated sums
E1,E(N, X, n):=
∑
X<deg( f)≤n+deg(D)
λ( f)χD(N f)√| f| (4-13)
and
E2,E(N, X, n):=
∑
X<deg( f)≤n+deg(D)
(n+ deg(D)− deg( f))λ( f)χD(N f)√| f| . (4-14)
We are now ready to prove the following upper bounds for Ei,E(N, X, n).
Proposition 4.7. For i= 1, 2 and any ﬁxed n∈ N we have
∑
D∈H∗
2g+1
|Ei,E(N, X, n)|2≪ε q2gg1/2+ε(2g− X)2i.
Proof. Using the Perron formula for the sum over f in (4-13), we get that
E1,E(N, X, n)=χD(N)
2πi
∮
|u|=1
L
(
E⊗χD, u√q
)( 1
un+deg(D)− 1
u X
) du
u(1− u).
Note that there is no pole at u= 1. So we need to bound the following expression
1
(2πi)2
∮
|u|=1
∮
|v|=1
∑
D∈H∗
2g+1
L
(
E⊗χD, u√q
)
L
(
E⊗χD, v√q
)
×
( 1
un+deg(D)− 1
u X
)( 1
vn+deg(D)− 1
v X
) dudv
uv(1− u)(1−v). (4-15)
We use Corollary 4.6 to bound the integral above and considerθ andγ on different arcs on the unit circle.
We bound the integral on these arcs and notice that we obtain the biggest upper bound when θ,γ are not
close to 0 (i.e., u andv are not close to 1) and whenθ is not close to γ or to 2π−γ (by close we mean
on an arc of length on the scale of 1/g).
For example, ifθ andγ are both on an arc C1 of length on the scale of 1/g around 0, then the double
integral in (4-15) over the arcs C1 is Oε(q2gg−1+ε) (since from the corollary we get a power of g which
gets multiplied by g−2, the product of the sizes of the arcs.)
Ifθ,γ are both on the complement of C1, but close to each other (i.e., θ is within 1/g ofγ ), we get
that the corresponding integral over the two arcs is Oε(q2ggε). We get a similar bound if θ is close to
2π−γ , under the same conditions.
We are left with the case whenθ,γ are on the complement of C1 andθ is far fromγ and from 2π−γ .
In this case the corresponding integral will be Oε(q2gg1/2+ε). This ﬁnishes the proof of the upper bound
when i= 1.
When i= 2, using the Perron formula for the sum over f in (4-14), we have
E2,E(N, X, n)=χD(N)
2πi
∮
|u|=1
L
(
E⊗χD, u√q
)( 1
un+deg(D)−(n+ deg(D)− X)(1− u)+ u
u X+1
) du
(1− u)2.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1881
Hence
E2,E(N, X, n)2= 1
(2πi)2
∮
|u|=1
∮
|v|=1
L
(
E⊗χD, u√q
)
L
(
E⊗χD, v√q
)
×
( 1
un+deg(D)−(n+ deg(D)− X)(1− u)+ u
u X+1
)
×
( 1
vn+deg(D)−(n+ deg(D)− X)(1−v)+v
v X+1
) dudv
(1− u)2(1−v)2.
We proceed as before and keeping in mind that|u|=| v|= 1, it follows that
∑
D∈H∗
2g+1
|E2,E(N, X, n)|2≪ε q2gg1/2+ε(2g− X)4,
as required. □
5. Proof of Theorem 1.1
For N|1∞, let
RE(N, X):=
∑
D∈H∗
2g+1
∑
f∈M≤X
λ( f)χD(N f)√| f| .
We will prove the following lemma.
Lemma 5.1. We have
RE(N, X)=| H2g+1|CE(N; 1)L(Sym2 E, 1)+ Oε(q2g−X/2+εg)+ Oε(q X/2+ϵg),
where the value CE(N; 1) is deﬁned in (5-2).
Proof. Note that
RE(N, X)= SE,E(N, X, 0; 0, 0),
where SE1,E2(N, X, Y;α,β) is deﬁned as in (3 -1). We proceed as in Section 3, see (3 -2), (3-3) and (3-7),
and write
RE(N, X)= SE,E(N, X, 0, g; 0, 0)= RE(N, X; V= 0)+ RE(N, X; V⁄= 0),
where RE(N, X; V⁄= 0)= SE,E(N, X, 0, g; 0, 0; V⁄= 0) and
RE(N, X; V= 0)= SE,E(N, X, 0, g; 0, 0; V= 0)
=| H2g+1|
∑
f∈M≤X
N f=□
λ( f)√| f|
∏
P|1f
(
1− 1
|P|
) ∑
C2|(1f)∞
deg(C2)≤g
1
|C2|2+ Oε(qεg).
1882 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We ﬁrst evaluate RE(N, X; V= 0). From (3-6) we have
∑
C2|(1f)∞
deg(C2)≤g
1
|C2|2=
∏
P|1f
(
1− 1
|P|2
)−1
+ Oε(q−2g+εg).
The contribution of the error term to RE(N, X; V= 0) is
≪ε qεg ∑
l∈M≤X/2
|λ(Nl 2)|
|l| ≪ε qεg.
Hence
RE(N, X; V= 0)=| H2g+1|
∑
f∈M≤X
N f=□
λ( f)√| f|
∏
P|1f
(
1+ 1
|P|
)−1
+ Oε(qεg).
Applying the Perron formula to the sum over f yields
RE(N, X; V= 0)=|H2g+1|
2πi
∮
|u|=r
BE(N; u) du
u X+1(1− u)+ Oε(qεg) (5-1)
for any r< 1, where
BE(N; u)=
∑
f∈M
N f=□
λ( f)udeg( f)
√| f|
∏
P|1f
(
1+ 1
|P|
)−1
.
We can write BE(N; u) in terms of its Euler product,
BE(N; u)=
∏
P ∤1
(
1+
(
1+ 1
|P|
)−1∑
i≥1
λ(P2i)u2i deg(P)
|P|i
)∏
P|1
((
1+ 1
|P|
)−1 ∑
i+ordP(N) even
λ(Pi)ui deg(P)
|P|i/2
)
= CE(N; u)L
(
Sym2 E, u2
q
)
, (5-2)
where CE(N; u) is some Euler product which is uniformly bounded for|u|≤ q1/2−ε. We shift the contour
in (5-1) to|u|= q1/2−ε, encountering a simple pole at u= 1. Then
RE(N, X; V= 0)=| H2g+1|CE(N; 1)L(Sym2 E, 1)+ Oε(q2g−X/2+εg). (5-3)
Now we will bound RE(N, X; V⁄= 0). As in Section 3D, see (3-12), it sufﬁces to bound the term
R(V⁄= 0)=q2g+1τ(q)
∑
f∈M≤X
deg(N f) odd
λ( f)
|N|| f|3/2
∑
C1|1
C2|(1f)∞
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f)
|C1||C2|2
∑
V∈Mdeg(N f)+deg(C1)+2 deg(C2)−2g−2
G(V, N f).
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1883
Using the fact that
∑
C2∈Mc2
C2|(1f)∞
1
|C2|2= q−2c2
2πi
∮
|w|=r
∏
P|1f
(1−wdeg(P))−1 dw
wc2+1
for r< 1, and writing V= V1V 2
2 with V1 a square-free polynomial, we have
R(V⁄= 0)= q2g+1τ(q)
|N|
∑
c1+2c2≤2g+1
q−2c2
∑
C1∈Mc1
C1|1
µ(C1)χC1(N)
|C1|
×
∑
n≤X
n+deg(N) odd
∑
j≤n+deg(N)+c1+2c2−2g−2
j+c1 odd
∑
V1∈H j
∑
V2∈M(n+deg(N)+c1− j)/2+c2−g−1
× 1
2πi
∮
|w|=r
∑
f∈Mn
χC1( f)λ( f)G(V1V 2
2, N f)
| f|3/2
∏
P|1f
(1−wdeg(P))−1 dw
wc2+1.
Now
∑
f∈M
χC1( f)λ( f)G(V1V 2
2, N f)
| f|3/2
∏
P|1f
(1−wdeg(P))−1udeg( f)
= H(V1; u,w) I(V1V 2
2, N; u,w) J(V1V 2
2; u,w),
where
H(V1; u,w)=
∏
P ∤V1
(
1+χC1V1(P)λ(P)udeg(P)
|P| (1−wdeg(P))−1
)
,
I(V1V 2
2, N; u,w)=
∏
P|1
(∑
j
χC1(P j)λ(P j)G(V1V 2
2, P j+n P)u j deg(P)
|P|3 j/2
)
(1−wdeg(P))−1
and
J(V1V 2
2; u,w)=
∏
P| V1V2
P ∤1
(
1+
∑
j≥1
χC1(P j)λ(P j)G(V1V 2
2, P j)u j deg(P)
|P|3 j/2 (1−wdeg(P))−1
)
×
∏
P ∤V1
P|1V2
(
1+χC1V1(P)λ(P)udeg(P)
|P| (1−wdeg(P))−1
)−1
.
1884 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We use the Perron formula for the sum over f and obtain
R(V⁄= 0)= q2g+1τ(q)
|N|
∑
c1+2c2≤2g+1
q−2c2
∑
C1∈Mc1
C1|1
µ(C1)χC1(N)
|C1|
×
∑
n≤X
n+deg(N) odd
∑
j≤n+deg(N)+c1+2c2−2g−2
j+c1 odd
∑
V1∈H j
∑
V2∈M(n+deg(N)+c1− j)/2+c2−g−1
× 1
(2πi)2
∮
|u|=r
∮
|w|=r
H(V1; u,w) I(V1V 2
2, N; u,w) J(V1V 2
2; u,w) du
un+1
dw
wc2+1. (5-4)
Let r1= q1/2−ε, r2= q−ε, and let k0 be minimal such that|r1r k0
2|< 1. Then we can write
H(V1; u,w)= L
(
E⊗χC1V1, u
q
)
L
(
E⊗χC1V1, uw
q
)
··· L
(
E⊗χC1V1, uwk0−1
q
)
K(V1; u,w), (5-5)
where
K(V1; u,w)≪ε|C1|ε
uniformly for|u|≤ r1 and|w|≤ r2. We also have
I(V1V 2
2, N; u,w)≪ε|V1V2|ε and J(V1V 2
2; u,w)≪ε|V2|ε
in this region. We now move the contours in (5 -4) to|u|= r1 and|w|= r2. We then use the Lindelöf
bound for each L-function and trivially bound the rest of the expression to obtain that
R(V⁄= 0)≪ε q X/2+εg.
Combining this with (5-3) ﬁnishes the proof of Lemma 5.1. □
To prove Theorem 1.1, note that from Lemma 2.2 we have
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
= RE(1,[n/2]+ 2g+ 1)+ϵ2g+1ϵ(E)RE(M,[(n+ 1)/2]+ 2g).
Using Lemma 5.1 and choosing X= g we have that
1
|H∗
2g+1|
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
= c1(M)L(Sym2 E, 1)+ Oε(q−g+εg),
where
c1(M)=(CE(1; 1)+ϵ2g+1ϵ(E)CE(M; 1))
∏
P|1
|P|+ 1
|P| . (5-6)
This ﬁnishes the proof of the theorem.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1885
6. Proof of Theorem 1.2
For N|1∞, let
RE(N, X;α):=
∑
D∈H∗
2g+1
∑
f∈M≤X
λ( f)χD(N f)
| f|1/2+α .
Note that RE(N, X; 0)= RE(N, X) with RE(N, X) as in Section 5. Similarly as in Section 5 and for
|α|≤ 1/g we get that
RE(N, X;α)=| H2g+1|CE(N; q−α)L(Sym2 E, 1+ 2α)+ Oε(q2g−X/2+ϵg)+ Oε(q X/2+ϵg). (6-1)
Using Lemma 2.3 we obtain
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
=(log q)([n/2]+ 2g+ 1)(RE(1,[n/2]+ 2g+ 1)−ϵ2g+1ϵ(E)RE(M,[n/2]+ 2g+ 1))
+ ∂
∂α(RE(1,[n/2]+ 2g+ 1;α)−ϵ2g+1ϵ(E)RE(M,[n/2]+ 2g+ 1;α))
⏐⏐
α=0.
From Lemma 5.1 and (6-1) it follows that
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
= c2(M)L(Sym2 E, 1)g+ c3(M)+ Oε(q−g+ϵg),
where
c2(M)= 2(log q)(CE(1; 1)−ϵ2g+1ϵ(E)CE(M; 1))
∏
P|1
|P|+ 1
|P| (6-2)
and
c3(M)=(((log q)([n/2]+ 1)L(Sym2 E, 1)+ 2L′(Sym2 E, 1))(CE(1; 1)−ϵ2g+1ϵ(E)CE(M; 1))
+ L(Sym2 E, 1)(C′
E(1; 1)−ϵ2g+1ϵ(E)C′
E(M; 1)))
∏
P|1
|P|+ 1
|P| . (6-3)
7. Proof of Theorem 1.3
Following Lemma 2.2, for X< 2g, we deﬁne
M1,E(X):=(1+ϵ)
∑
f∈M≤X
λ( f)χD( f)√| f| ,
so that
L
(
E⊗χD, 1
2
)
= M1,E(X)+ E1,E(1, X,[n/2])+ϵ2g+1ϵ(E)E1,E(M, X,[(n− 1)/2]), (7-1)
where recall expression (4-13) for E1,E(N, X, n). Hence
L
(
E⊗χD, 1
2
)2
= 2L(E⊗χD, 1
2)M1,E(X)− M1,E(X)2+(E1,E(1, X,[n/2])+ϵ2g+1ϵ(E)E1,E(M, X,[(n− 1)/2]))2.
1886 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
By Cauchy’s inequality and Proposition 4.7 we get
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)2= 2
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
M1,E(X)−
∑
D∈H∗
2g+1
M1,E(X)2
+ Oε(q2gg1/2+ε(2g− X)2).
Now using Lemma 2.2 again and expanding M1,E(X)2, the ﬁrst line of the equation above is
2(SE(1,[n/2]+ 2g+ 1, X)+ SE(1,[(n+ 1)/2]+ 2g, X)− SE(1, X, X))
+ 2ϵ2g+1ϵ(E)(SE(M,[n/2]+ 2g+ 1, X)+ SE(M,[(n+ 1)/2]+ 2g, X)− SE(M, X, X)),
where recall the deﬁnition of SE(M, X, Y) in Section 3. Using Proposition 3.1, this is equal to
|H∗
2g+1|c2(M)L(Sym2 E, 1)3X+ O(q2g)+ O(q2g−X/5g3)+ O(q5g/4+3X/8g30),
where
c2(M)= 2(CE(1; 1, 1, 1)+ϵ2g+1ϵ(E)CE(M; 1, 1, 1))
∏
P|1
|P|+ 1
|P| , (7-2)
and CE(N; 1, 1, 1) is deﬁned in (3-9). Thus
1
|H∗
2g+1|
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)2
= c4(M)L(Sym2 E, 1)3X+ O(q−X/5g3)+ O(q−3g/4+3X/8g30)+ Oε(g1/2+ε(2g− X)2).
Choosing X= 2g− 100 logg we obtain the theorem.
8. Proof of Theorem 1.4
Following Lemma 2.3, for X< 2g and ﬁxed n∈ N, we deﬁne
M2,E(X, n):=(1−ϵ)
∑
f∈M≤X
(n+ deg(D)− deg( f))λ( f)χD( f)√| f| ,
so that
ϵ−L′(
E⊗χD, 1
2
)
=(log q)M2,E(X,[n/2])+(log q)(E2,E(1, X,[n/2])−ϵ2g+1ϵ(E)E2,E(M, X,[n/2])), (8-1)
where recall that E2,E(M, X, n) is given in (4-14). Then we get that
ϵ−L′(
E⊗χD, 1
2
)2= 2(log q)ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])−(log q)2M2
2,E(X,[n/2])
+(log q)2(E2,E(1, X,[n/2])−ϵ2g+1ϵ(E)E2,E(M, X,[n/2]))2.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1887
By Cauchy’s inequality and Proposition 4.7 we get that
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)2= 2(log q)
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])
−(log q)2 ∑
D∈H∗
2g+1
M2,E(X,[n/2])2+ Oε(q2gg1/2+ϵ(2g− X)4).
Now by Lemma 2.3 we have
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])
= 2(log q)([n/2]+2g+1)2(SE(1,[n/2]+2g+1, X)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X))
+2([n/2]+2g+1) ∂
∂β(SE(1,[n/2]+2g+1, X; 0,β)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X; 0,β))
⏐⏐
β=0
+2([n/2]+2g+1) ∂
∂α(SE(1,[n/2]+2g+1, X;α, 0)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X;α, 0))
⏐⏐
α=0
+ 2
log q
∂2
∂α∂β(SE(1,[n/2]+2g+1, X;α,β)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X;α,β))
⏐⏐
α=β=0,
and similarly
∑
D∈H∗
2g+1
M2,E(X,[n/2])2
= 2([n/2]+ 2g+ 1)2(SE(1, X, X)−ϵ2g+1ϵ(E)SE(M, X, X))
+ 2
log q([n/2]+ 2g+ 1) ∂
∂β(SE(1, X, X; 0,β)−ϵ2g+1ϵ(E)SE(M, X, X; 0,β))
⏐⏐
β=0
+ 2
log q([n/2]+ 2g+ 1) ∂
∂α(SE(1, X, X;α, 0)−ϵ2g+1ϵ(E)SE(M, X, X;α, 0))
⏐⏐
α=0
+ 2
(log q)2
∂2
∂α∂β(SE(1, X, X;α,β)−ϵ2g+1ϵ(E)SE(M, X, X;α,β))
⏐⏐
α=β=0.
Choosing X= 2g− 100 logg and using Proposition 3.1, we obtain that
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)2= c5(M)L(Sym2 E, 1)3g3+ Oε(g2+ϵ),
where
c5(M)= 16(log q)2(CE(1; 1, 1, 1)−ϵ2g+1ϵ(E)CE(M; 1, 1, 1))
∏
P|1
|P|+ 1
|P| . (8-2)
1888 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
9. Proof of Theorem 1.5
By combining (7-1) and (8-1),
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=ϵ−
2 M1,E1(X)L′(
E2⊗χD, 1
2
)
+(log q)L
(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
−(log q)M1,E1(X)M2,E2(X,[n2/2])
+(log q)(E1,E1(1, X,[n1/2])+ϵ2g+1ϵ(E1)E1,E1(M1, X,[(n1− 1)/2]))
×(E2,E2(1, X,[n2/2])−ϵ2g+1ϵ(E2)E2,E2(M2, X,[n2/2])).
We bound the last term above using Cauchy’s inequality and Proposition 4.7. In doing so we get
∑
D∈H∗
2g+1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=
∑
D∈H∗
2g+1
ϵ−
2 M1,E1(X)L′(
E2⊗χD, 1
2
)
+(log q)
∑
D∈H∗
2g+1
L
(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
−(log q)
∑
D∈H∗
2g+1
M1,E1(X)M2,E2(X,[n2/2])+ Oε(q2gg1/2+ε(2g− X)3). (9-1)
We shall estimate the remaining three terms using Proposition 3.1. They all have similar forms. For the
ﬁrst term, by Lemma 2.3 again we have
∑
D∈H∗
2g+1
ϵ−
2 M1,E1(X)L′(
E2⊗χD, 1
2
)
=(log q)
∑
D∈H∗
2g+1
(1+ϵ1)(1−ϵ2)
∑
f∈M≤X
h∈M≤[n2/2]+2g+1
([n2/2]+ 2g+ 1− deg(h))λ1( f)λ2(h)χD( f h)√| f h| .
By expanding out, this equals
(log q)([n2/2]+ 2g+ 1)
(
SE1,E2(1,[n2/2]+ 2g+ 1, X; 0, 0)
+ϵ2g+1ϵ(E1)SE1,E2(M1,[n2/2]+ 2g+ 1, X; 0, 0)
−ϵ2g+1ϵ(E2)SE1,E2(M2,[n2/2]+ 2g+ 1, X; 0, 0)
−ϵ(E1)ϵ(E2)SE1,E2(M1M2,[n2/2]+ 2g+ 1, X; 0, 0)
)
+ ∂
∂β
(
SE1,E2(1,[n2/2]+ 2g+ 1, X; 0,β)
+ϵ2g+1ϵ(E1)SE1,E2(M1,[n2/2]+ 2g+ 1, X; 0,β)
−ϵ2g+1ϵ(E2)SE1,E2(M2,[n2/2]+ 2g+ 1, X; 0,β)
−ϵ(E1)ϵ(E2)SE1,E2(M1M2,[n2/2]+ 2g+ 1, X; 0,β)
)⏐⏐
β=0,
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1889
which is, by Proposition 3.1 and Cauchy’s residue theorem,
|H∗
2g+1|c6(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗ E2, 1)g+ O(q2g)+ O(q5g/4+3X/8g31),
where
c6(M1, M2)= 2(logq)
(
CE1,E2(1;1,1,1,0,0)+ϵ2g+1ϵ(E1)CE1,E2(M1;1,1,1,0,0)
−ϵ2g+1ϵ(E2)CE1,E2(M2;1,1,1,0,0)
−ϵ(E1)ϵ(E2)CE1,E2(M1M2;1,1,1,0,0)
)∏
P|1
|P|+1
|P| . (9-2)
The other two terms in (9-1) have the same asymptotics so we obtain
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=c6(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗E2, 1)g+O(q−3g/4+3X/8g31)+Oε(g1/2+ε(2g−X)3).
Choosing X= 2g− 100 logg we obtain the theorem.
10. Proof of Theorem 1.6
We argue as in the previous section. From (8-1) we have
ϵ−
1ϵ−
2 L′(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=(log q)
(
ϵ−
2 M2,E1(X,[n1/2])L′(
E2⊗χD, 1
2
)
+ϵ−
1 L′(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
)
−(log q)2M2,E1(X,[n1/2])M2,E2(X,[n2/2])
+(log q)2(E2,E1(1, X,[n1/2])−ϵ2g+1ϵ(E1)E2,E1(M1, X,[n1/2]))
×(E2,E2(1, X,[n2/2])−ϵ2g+1ϵ(E2)E2,E2(M2, X,[n2/2])).
Bounding the last term above using Cauchy’s inequality and Proposition 4.7 leads to
∑
D∈H∗
2g+1
ϵ−
1ϵ−
2 L′(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=(log q)
∑
D∈H∗
2g+1
ϵ−
2 M2,E1(X,[n1/2])L′(
E2⊗χD, 1
2
)
+(log q)
∑
D∈H∗
2g+1
ϵ−
1 L′(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
−(log q)2 ∑
D∈H∗
2g+1
M2,E1(X,[n1/2])M2,E2(X,[n2/2])+ Oε(q2gg1/2+ε(2g− X)4). (10-1)
1890 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We shall illustrate the evaluation of the third term using Proposition 3.1. The ﬁrst two terms can be
treated in the same way, and in fact they all have the same asymptotics. We have
(log q)2 ∑
D∈H∗
2g+1
M2,E1(X,[n1/2])M2,E2(X,[n2/2])=(log q)2 ∑
D∈H∗
2g+1
(1−ϵ1)(1−ϵ2)
∑
f,h∈M≤X
([n1/2]+ 2g+ 1− deg( f))([n2/2]+ 2g+ 1− deg(h))λ1( f)λ2(h)χD( f h)√| f h| .
By expanding out, this equals
(log q)2([n1/2]+ 2g+ 1)([n2/2]+ 2g+ 1)
(
SE1,E2(1, X, X; 0, 0)−ϵ2g+1ϵ(E1)SE1,E2(M1, X, X; 0, 0)
−ϵ2g+1ϵ(E2)SE1,E2(M2, X, X; 0, 0)+ϵ(E1)ϵ(E2)SE1,E2(M1M2, X, X; 0, 0)
)
+(log q)([n1/2]+ 2g+ 1) ∂
∂β
(
SE1,E2(1, X, X; 0,β)−ϵ2g+1ϵ(E1)SE1,E2(M1, X, X; 0,β)
−ϵ2g+1ϵ(E2)SE1,E2(M2, X, X; 0,β)+ϵ(E1)ϵ(E2)SE1,E2(M1M2, X, X; 0,β)
)⏐⏐
β=0
+(log q)([n2/2]+ 2g+ 1) ∂
∂α
(
SE1,E2(1, X, X;α, 0)−ϵ2g+1ϵ(E1)SE1,E2(M1, X, X;α, 0)
−ϵ2g+1ϵ(E2)SE1,E2(M2, X, X;α, 0)+ϵ(E1)ϵ(E2)SE1,E2(M1M2, X, X;α, 0)
)⏐⏐
α=0
+ ∂2
∂α∂β
(
SE1,E2(1, X, X;α,β)−ϵ2g+1ϵ(E1)SE1,E2(M1, X, X;α,β)
−ϵ2g+1ϵ(E2)SE1,E2(M2, X, X;α,β)+ϵ(E1)ϵ(E2)SE1,E2(M1M2, X, X;α,β)
)⏐⏐
α=β=0.
In view of Proposition 3.1 and Cauchy’s residue theorem, this is
|H∗
2g+1|c7(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗ E2, 1)g2+ O(q2gg)+ O(qg/2+3X/4g32),
where
c7(M1, M2)= 4(log q)2(
CE1,E2(1; 1, 1, 1, 0, 0)−ϵ2g+1ϵ(E1)CE1,E2(M1; 1, 1, 1, 0, 0)
−ϵ2g+1ϵ(E2)CE1,E2(M2; 1, 1, 1, 0, 0)
+ϵ(E1)ϵ(E2)CE1,E2(M1M2; 1, 1, 1, 0, 0)
)∏
P|1
|P|+ 1
|P| . (10-2)
The other two terms in (10-1) have the same asymptotics so we obtain
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−
1ϵ−
2 L′(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
= c7(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1E2, 1)g2
+ O(g)+ O(q−3g/2+3X/4g32)+ Oε(g1/2+ε(2g− X)4).
Choosing X= 2g− 100 logg we obtain the theorem.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1891
11. Proof of Corollary 1.7
The results in Section 4 imply that
∑
D∈H∗
2g+1
L(E⊗χD, 1
2)4≪ε q2gg6+ε. (11-1)
We next obtain some upper bounds for moments of the derivatives. We have
L(l)(
E⊗χD, 1
2
)k=
( l!
2πi
)k∮
···
∮ L(E⊗χD, 1/2+α1)··· L(E⊗χD, 1/2+αk)
αl+1
1 ··· αl+1
k
dα1··· dαk,
where we are integrating along small circles of radii r around the origin. Then using Hölder’s inequality
leads to ∑
D∈H∗
2g+1
⏐⏐L(l)(
E⊗χD, 1
2
)⏐⏐k≪ (l!)k
rlk+1
∮
|α|=r
∑
D∈H∗
2g+1
⏐⏐L
(
E⊗χD, 1
2+α
)⏐⏐kdα.
Choosing r= 1/g and using upper bounds for moments of L-functions we get that
∑
D∈H∗
2g+1
⏐⏐L(l)(
E⊗χD, 1
2
)⏐⏐k≪ε q2g(l!)kglk+k(k−1)/2+ε.
In particular, with l= 1 and k= 4, we have
∑
D∈H∗
2g+1
L′(
E⊗χD, 1
2
)4≪ε q2gg10+ε. (11-2)
Now from Hölder’s inequality we have
( ∑
D∈H2g+1
(D,11)=1
L
(
E1⊗χD, 1
2
)4
)( ∑
D∈H2g+1
(D,12)=1
L′(
E2⊗χD, 1
2
)4
)( ∑
D∈H2g+1, (D,1112)=1
ϵ−
2 L(E1⊗χD,1/2)L′(E2⊗χD,1/2)⁄=0
1
)2
≥
( ∑
D∈H2g+1
(D,1112)=1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
))4
.
Combining (11-1) and (11-2) with Theorem 1.5 we get
#
{
D∈ H∗
2g+1:ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
⁄= 0
}
≫ε
q2g
g6+ε,
which implies the ﬁrst statement. The second statement can be obtained similarly.
