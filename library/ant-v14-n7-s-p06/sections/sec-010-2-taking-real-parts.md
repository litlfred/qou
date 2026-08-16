---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-010-2-taking-real-parts
section_title: "Taking real parts"
section_number: 2
pages: 22-29
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
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
