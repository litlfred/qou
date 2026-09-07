---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-006-23-sums-of-cotangents
section_title: "Sums of cotangents"
section_number: 2.3
pages: 14-19
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
of the LandauO-symbol. Let D1⊂D2⊂ C be two sets given by the context, andg :D2→ R+.
We will write
(2.20) f(z) =Oz
(p1,p2,... )(g(z)) ( z∈D1)
whenever, for any ﬁxed choice of the parameters p1,p 2,... , there exists a function ϕ holo-
morphic on D2, which satisﬁes ϕ(z) = f(z) for z∈ D1, and |ϕ(z)|≪ g(z) for z∈ D2, the
implied constant being uniform in the parameters p1,p 2,... . The additional information is
the holomorphic behaviour inz, which may become useful when studying knots other than 41.
However we stress that, in the present work, a later obstacle (possible cancellation of main
terms) imposes the restriction K = 41, and in this case, we do not require holomorphicity of
error terms.
Lemma 5. For 0<α< 1
2, we have
cot(πα) tan(παx)≤x (0<x ≤ 1),(2.21)
x(1− (2α)2)< cot(πα) tan(παx)≤Oε(x) (0 <x ≤ 1
α( 1
2−ε)).(2.22)
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 15
Proof. Assume 0 < x≤ 1
α( 1
2−ε). The function x ↦→ tan(xλ)
x is increasing on (0 , π
2λ) for
all λ >0. It follows that πα≤ tan(παx)/x≤ Oε(α), while tan(παx)/x≤ tan(πα) if x≤ 1.
Thus, it suﬃces to show the bounds
1− (2α)2<πα cot(πα), tan(πα) cot(πα)≤ 1, α cot(πα)≪ 1.
The second is trivial, while the third follows from elementary properties of cot. For the ﬁrst,
we note that by the Taylor expansion of cot [19, 1.411.7], we have φ(α) := 1−πα cot(πα)
α2 =∑
j≥0cjα2j for α ∈ (0, 1), where cj > 0. In particular φ is increasing, and we conclude
byφ( 1
2) = 4. □
Lemma 6. Letε> 0. For 0<α ≤ 1
2−ε and| Re(αz)|≤ 1
2−ε we have
1− cot(πα) tan(παz) = (1−z)
(
1 +Oε(α2(|z|2 +|z|))
)
.
Proof. If|z|≤ 1/2, expanding in Taylor series we obtain
cot(πα) tan(παz) = cot(πα)παz(1 +O(α2|z|2)) =z(1 +O(α2))(1 +O(α2|z|2))
and the claimed result follows. If |z|≥ 1/2, we observe that the left hand side is equal to
cot(πα)(tan(πα)− tan(παz)) and so, since cot(πα)πα = 1 +Oε(α2), we are required to show
that
(2.23) tan(παz)− tan(πα)
πα(z− 1) = 1
αz−α
∫ αz
α
dv
cos(πv)2 = 1 +Oε(|αz|2).
This follows for |Im(αz)|≤ 1 by the estimate cos( πv)2 = exp{Oε(|v|2)} for| Re(v)|≤ 1
2−ε
and|Im(v)|≤ 1. If |Im(αz)| > 1, then both the ratio 1
αz−α and the integral are bounded,
since|cos(πv)|≫ eπ| Im(v)|, so that (2.23) holds in this case as well. □
Lemma 7. Letα∈ R with 0<|α|< 1/2, and
Dα :={z∈ C| −1
3|α| < Re(z)< 1}.
Then, taking the determination of the logarithm which is real on the real axis, the function
given by
ψα(z) := log(1− cot(πα) tan(παz)) + cot(πα) tan(παz) (2.24)
is holomorphic on Dα, where it satisﬁes
ψα(z)≪|z|2 +|z|| log(1−z)|, Im(ψα(z))≪|z|2,(2.25)
ψα(z) = log(1−z) +z +Oε((|z|2 +|z|3)|α|2) if|α|≤ 1
2−ε.(2.26)
Proof. We can assume α∈ (0, 1/2), since ψα is even in α. For |Re(z)| < 1
2α, let gα(z) :=
cot(πα) tan(παz). Since, for z =x +iy, we have
tan(παz) = tan(παx)(1− tanh2(παy)) +i tanh(παy)(1 + tan2(παx))
1 + tan2(παx) tanh2(παy) ,(2.27)
we deduce, for x,y real and|x|≤ 1,
|Re(gα(z))|≤| cot(πα) tan(παx)|≤| x|.(2.28)
by Lemma 5. Moreover, ifx≤ 0, then Re(gα(z))≤ 0. Using (2.27) and the lower bound (2.22),
we obtain|Re(gα(z))|≫ cot(πα) tan(πα|x|)≫ε|x|. Thus, there exists cε> 0 such that
(2.29) Re(1 −gα(z))≥ min(1−x, 1−cεx).
16 S. BETTIN AND S. DRAPPEAU
In particular, the function z↦→ψα(z) = log(1−gα(z))+gα(z) is well-deﬁned and holomorphic
in Dα, and moreover Im(log(1−gα(z)))<π/ 2.
We observe that if αy→±∞ (and so z→∞ ), then gα(z)∼± i cot(πα) uniformly in x,
so that ψα(z)≪ 1/α≪| z| and (2.25)-(2.26) follow trivially. Thus, we can assume αy≪ 1.
Also, by (2.27) and Lemma 5 we obtain
| Im(gα(z))|≪| cot(πα)|
(
| tan(πxα)| +| tanh(παy)|)≪|x| +|y|≪| z|.(2.30)
In particular, recalling (2.28), we have gα(z)≪|z|.
Now, assume α≤ 1
2−ε. By (2.27), and since αy≪ 1, we have
| Im(gα(z))|≥| cot(πα) tanh(παy)|≫ ε|y|.
By (2.29), it then follows that |1−gα(z)|≫ ε min(1−x, 1−cεx) +|y|≫ ε|1−z|, and so
|uα(z)|≫ ε 1 for uα(z) := 1−gα(z)
1−z . Thus,
log(uα(z)) =uα(z)− 1 +Oε(|uα(z)− 1|2) =z−gα(z) +z(uα(z)− 1) +Oε(|uα(z)− 1|2)
and so (2.26) follows since uα(z)− 1 =Oε(α2(|z|2 +|z|)) by Lemma 6 (and since αz≪ 1).
We now move to (2.25). Since gα(z)≪| z|, then if |z| < δ with δ > 0 suﬃciently small,
then by Taylor expansion one trivially has that (2.25) holds for |z| < δ. By the assumption
|αy|≪ 1 we have that (2.26) implies (2.25) for |z|≥ δ and α≤ 1
2−ε. It follows that we can
also assume α≫ 1 (and so also |z|≪ α|z|≪ 1).
Finally, we observe that under the above assumptions we have that (2.27) implies also
Re(1−gα(z))≥ 1−x(1− tanh2(παy))≫ 1−x +y2≫| 1−z|2 (x≥ 0),
which inequality Re(1−gα(z))≫| 1−z|2 is also trivially true if x <0. The bound (2.26)
follows since gα(z)≪| z|, Im(log(1−gα(z))) < π/2, and log(1 −w) +w≪ min{|w|2,|w| +
log|1−w|} for w∈ C r [1,∞). □
Lemma 8. Let γ≤ δ and let a∈ N with γ≤ a− 1
2 ≤ δ. Let g(z) be holomorphic on a
neighborhood ofγ≤ Re(z)≤δ, where it satisﬁes|g(z)|≤ C1|z|m +C2 for some m,C 1,C 2≥ 0.
Then, with z =r, we have
r∑
n=a
g(n) =Or
(g,a)(C1((|a| +|z|)m+1 + 1) +C2(|a| +|z| + 1)), (r∈ Z∩ [a,δ ])
using the notation (2.20) with D2 ={z, γ + 1
2≤ Re(z)≤δ}.
Proof. We apply Lemma 1 with α =a− 1
2, β =r− 1
2, we ﬁnd
r−1∑
n=a
g(n) =
∫ r− 1
2
a− 1
2
g(z)dz−i
∫ ∞
0
g(a− 1
2 +it)−g(a− 1
2−it)−g(r− 1
2 +it) +g(r− 1
2−it)
e2πt + 1 dt,
Denoting byϕ(r)−g(r) the right hand side, we immediately see thatϕ extend to a holomorphic
function in γ + 1
2≤ Re(z)≤ δ and that ϕ(z)≪ C1((|a| +|z|)m+1 + 1) +C2(|a| +|z| + 1) in
this strip. □
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 17
Lemma 9. Let (h,k ) = 1 , 3≤ h < kand r0∈ Z/hZ. Then for all 0≤ r < kwith r≡
r0 (mod h), writing z =r/k, we have
∑
0≤n≤r
h∤n
(
log
(
1− cot
(πnk
h
)
tan
(πn
hk
))
+ cot
(πnk
h
)
tan
(πn
hk
))
= k
h
(πi(z2−z)
2 + L(z) +πi
12 +z log(2πz/e)
)
+Oz
(h,k,r0)((1 +|log(1−z)| +|z|4)(1 +k/h2 + log(k/h))),
using the notation (2.20) withD2 ={z∈ C, 0≤ Re(z)< 1}. Moreover, the error term|log(1−z)|
can be omitted if z∈ [0, 1− h
k (1−{ r0−k
h })].
Proof. In this proof, the notationO will stand forOz
(k,h,r0) relative to the setD2 ={z, Re(z)∈
[0, 1)}. We divide the sum into congruence classes n≡𝓁k (modh),|𝓁|<h/ 2, where the possi-
ble term𝓁 =h/2 is excluded since the summand is zero in this case. With the notation (2.24),
we write the sum to be computed as
∑
0<|𝓁|<h/2
S(𝓁), S (𝓁) :=
∑
0<n≤r
n≡𝓁k (mod h)
ψ𝓁/h
(n
k𝓁
)
.
We consider each 𝓁 separately. We ﬁrst consider 𝓁⁄= 1. Let δ𝓁 :={r0−k𝓁
h }, and
α𝓁 =
⌈−k𝓁
h
⌉
− 1
2, β 𝓁(r) :=
⌊r−k𝓁
h
⌋
+ 1
2 = r−k𝓁
h + 1
2−δ𝓁.
Then by Lemma 1, we have
S(𝓁) =
∑
α𝓁<m≤β𝓁(r)
ψ𝓁/h(1 + hm
k𝓁 ) =I +C(α𝓁)−C(β𝓁(r)),
where
I :=
∫ β𝓁(r)
α𝓁
ψ𝓁/h(1 + ht
k𝓁)dt, C (γ) := 2
∫ ∞
0
Im(ψ𝓁/h(1 + h
k𝓁(γ +it)))dt
e2πt + 1 .
Note that β𝓁(r) = r−r0
h +β𝓁(r0), the right-hand side of which depends holomorphically on r.
Splitting the integral as
∫ (z−𝓁)k/h
−k𝓁/h +
∫−k𝓁/h
α𝓁
+
∫β𝓁(r)
(z−𝓁)k/h with z =r/k, we get
I = k
h
∫ z
0
ψ𝓁/h(t/𝓁)dt +
∫ 0
α𝓁+k𝓁
h
ψ𝓁/h(ht
k𝓁)dt +
∫ 1
2−δ𝓁
0
ψ𝓁/h(z
𝓁 + ht
k𝓁)dt
= k
h
∫ z
0
ψ𝓁/h(t/𝓁)dt +O
( 1+|z|2
𝓁2
)
,
by Lemma 7.
Next, we have
C(β𝓁(r)) = 1
2i
∑
±
±
∫ ∞
0
ψ𝓁/h
(z
𝓁 + h
k𝓁
(1
2−δ𝓁
)
±ith
k𝓁
) dt
e2πt + 1.
This also deﬁnes a holomorphic function of z for Re(z)∈ [0, 1), by Lemma 7. Since 𝓁⁄= 1, it
is bounded byO(|z|2+1
𝓁2 ).
18 S. BETTIN AND S. DRAPPEAU
Grouping the above discussion, we deduce for 𝓁⁄= 1 the estimate
(2.31) S(𝓁) = k
h
∫ z
0
ψ𝓁/h(t/𝓁)dt +O
(1 +|z|2
𝓁2
)
.
Consider now the case 𝓁 = 1. We recall the notation δ𝓁 from above. Since h≥ 3, by (2.26)
and Lemma 8 we have
(2.32) S(1) =O( k
h3 (|z|4 + 1)) +
∑
0<n≤r
n≡k (mod h)
(n
k + log
(
1− n
k
))
.
Leta∈{ 1,...,h } satisfya≡k (mod h),q = k−a
h andg =
⌊r−a
h
⌋
= r−a
h −δ1. In the sum, the
integerm = k−n
h runs through Z∩ [q−g,q ], so that
∑
0<n≤r
n≡k (mod h)
log
(
1− n
k
)
= (g + 1) log
(h
k
)
+ log Γ(q + 1)
Γ(q−g)
=
∫ g+1
0
(
log
(h
k
)
+ Γ′
Γ (q + 1−v)
)
dv
=
∫ g+1
0
(
log
(h
k (q + 1−v)
)
− 1
q + 1−v−
∫ ∞
0
{s}ds
(s +q + 1−v)2
)
dv
by Stirling’s formula [38, Theorem II.0.12]. First, setting t = (v−1)h+a
k , we have
∫ g+1
0
log
(h
k (q + 1−v)
)
dv = k
h
∫ z
0
log(1−t)dt + k
h
[∫ 0
a−h
k
+
∫ z−h
kδ1
z
]
log(1−t)dt
= k
h
∫ z
0
log(1−t)dt +O(|log(1−z)| + log(1 +k/h)).
Secondly, we have
∫ g+1
0
dv
q + 1−v = log
(
1−z + h
kδ1
)
− log
(
1 +h−a
k
)
=O(|log(1−z)| + log(1 +k/h)).
Note that in both cases, as well as in the following computations, the error term |log(1−z)|
can be omitted if z∈ [0, 1− h
k (1−δ1)] (which is the case when z =r/k). Finally,
∫ g+1
0
∫ ∞
0
{s}ds
(s +q + 1−v)2 dv =
∫ ∞
0
{s}(g + 1)ds
(s +q−g)(s +q + 1)
=
∫ ∞
0
{s} 1 + k
hz− a
h−δ1
(s + k
h(1−z) +δ1)(s + k−a
h + 1)ds
=O(log(1 +k/h) + log(1 +|z|)).
We turn to the contribution of the term n/k in (2.32). By a direct computation, we ﬁnd
∑
0<n≤r
n≡k (mod h)
n
k− k
h
∫ z
0
tdt =z( 1
2−δ1) + 1− h
2k(a
h +δ1)(a
h + 1−δ1) =O(|z| + 1).
On the other hand, we note that by (2.26),
∫ z
0
(t + log(1−t))dt =
∫ z
0
ψ1/h(t)dt +O
(1 +|z|4
h2
)
.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 19
Grouping the above estimates, we deduce
(2.33) S(1) = k
h
∫ z
0
ψ1/h(t)dt +O
(
(1 + k
h3 + log(k/h))(1 +|z|4 +|log(1−z)|)
)
.
We now sum the estimates (2.31), (2.33) over 𝓁, getting
∑
0<|𝓁|<h/2
S(𝓁) = k
h
∫ z
0
∑
0<|𝓁|<h2/3
ψ𝓁/h(t/𝓁)dt +O((1 + k
h3 + log(k/h))(1 +|z|4 +|log(1−z)|)).
The main term is evaluated by (2.26) (for |𝓁|≤ h/3) and (2.25) (for h/3<|𝓁|<h/ 2) as
∑
0<|𝓁|≤h/2
∫ z
0
ψ𝓁/h(t/𝓁)dt =
∑
0<|𝓁|≤h/3
(∫ z
0
(log(1−t/𝓁) +t/𝓁)dt +O
(1 +|z|4
h2
))
+O
(1 +|z|3
h
)
=
∑
0<𝓁<h/3
∫ z
0
log(1−t2/𝓁2)dt +O
(1 +|z|4
h
)
=
∑
𝓁>0
∫ z
0
log(1−t2/𝓁2)dt +O
(1 +|z|4
h
)
.
For−1≤t≤ 1 we have∏∞
𝓁=1(1−t2/𝓁2) = sin(πt)
πt . Moreover, for 0 ≤z <1 we have
∫ z
0
log(2 sin(πt))dt =
∫ z
0
log(−ieπit(1− e−2πit))dt = πi(z2−z)
2 +
∫ z
0
log(1− e−2πit)dt
= πi(z2−z)
2 + L(z) +πi
12,
by (2.10). Collecting the previous estimates, we conclude that
∑
0<|𝓁|<h/2
S(𝓁) = k
h
(πi(z2−z)
2 + L(z) +πi
12 +z log(2πz/e)
)
+O
((
1 + k
h2 + log(k/h)
)
(1 +|z|4 +|log(1−z)|)
)
,
as claimed. □
