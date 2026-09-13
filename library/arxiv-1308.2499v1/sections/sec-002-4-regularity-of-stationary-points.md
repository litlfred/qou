---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-002-4-regularity-of-stationary-points
section_title: "Regularity of stationary points"
section_number: 4
pages: 19-26
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
doc_brief: "Towards a regularity theory for integral Menger curvature — We generalize the notion of integral Menger curvature introduced by Gonzalez and Maddocks [14] by decoupling the powers in the integrand."
---
For the rest of this section, let us restrict to the case thatγ is parametrized by arc-length.
Then we get using Lemma 3.1
δintM(p,q)(γ; h) := 6q ˜Qp,q(γ, h) + 6Rp,q
1 (γh)
where
˜Qp,q(γ, h) :=
$
R/Z×D
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q−2
⟨∆w,0γ∧∆ v,0γ,∆w,0h∧∆ v,0γ +∆w,0γ∧∆ v,0h⟩
|∆w,0γ|p|∆v,0γ|p|∆v,wγ|p dw dv du
19
and
R1(γ, h) :=
$
R/Z×D
(
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p+2|∆v,0γ|p|∆v,wγ|p· ⟨∆w,0γ,∆w,0h⟩
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p|∆v,0γ|p+2|∆v,wγ|p· ⟨∆v,0γ,∆v,0h⟩
− p
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐q
|∆w,0γ|p|∆v,0γ|p|∆v,wγ|p+2· ⟨∆v,wγ,∆v,wh⟩
+ Rp,q(u, u +w, u +v)⟨γ′(u), h′(u)⟩
+ Rp,q(u, u +w, u +v)⟨γ′(u +v), h′(u +v)⟩
+ Rp,q(u, u +w, u +v)⟨γ′(u +w), h′(u +w)⟩)
dw dv du.
For q = 2 will see that ˜Qp := ˜Qp,2 contains the highest order term of the Euler-Lagrange
operator. To see this we use
⟨a∧ b, c∧ d⟩ = det
(⟨a, c⟩ ⟨a, d⟩
⟨b, c⟩ ⟨b, d⟩
)
to get
⟨a∧ b, a∧ c⟩ =⟨a, a⟩⟨ c, b⟩−⟨a, c⟩⟨ a, b⟩ =|a|2 ⟨
P⊥
a b, c
⟩
. (4.1)
Hence,
˜Qp(γ; h) =
$
R/Z×D
( ⟨
P⊥
∆v,0γ∆w,0γ,∆w,0h
⟩
⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2 ⏐⏐⏐∆w,0γ
⏐⏐⏐p +
⟨
P⊥
∆w,0γ∆v,0γ,∆v,0h
⟩
⏐⏐⏐∆w,vγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p ⏐⏐⏐∆w,0γ
⏐⏐⏐p−2
)
dw dv du
=
$
R/Z×D
(⟨
P⊥
∆v,0γ∆w,0γ,∆w,0h
⟩
|v−w|p|v|p−2|w|p +
⟨
P⊥
∆w,0γ∆v,0γ,∆v,0h
⟩
|v−w|p|v|p|w|p−2
)
dw dv du + R2(γ; h)
=
$
R/Z×D
(⟨
P⊥
∆v,0γ
(∆w,0γ
w − ∆v,0γ
v
)
,∆w,0h
w
⟩
|v−w|p|v|p−2|w|p−2 −
⟨
P⊥
∆w,0γ
(∆w,0γ
w − ∆v,0γ
v
)
,∆v,0h
v
⟩
|v−w|p|v|p−2|w|p−2
)
dw dv du + R2(γ; h)
=
$
R/Z×D
(⟨∆w,0γ
w − ∆v,0γ
v ,∆w,0h
w − ∆v,0h
v
⟩
|v−w|p|v|p−2|w|p−2
)
dw dv du + R2(γ; h)− R3(γ; h)
where
R2(γ; h) :=
$
R/Z×D
(⟨
P⊥
∆v,0γ∆w,0γ,∆w,0h
⟩
1⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2 ⏐⏐⏐∆w,0γ
⏐⏐⏐p− 1
|v−w|p|v|p−2|w|p

+
⟨
P⊥
∆w,0γ∆v,0γ,∆v,0h
⟩
1⏐⏐⏐∆w,vγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p ⏐⏐⏐∆w,0γ
⏐⏐⏐p−2− 1
|v−w|p|v|p|w|p−2

)
dw dv du
and
R3(γ; h) :=
$
R/Z×D
(⟨
P⊤
∆v,0γ
(∆w,0γ
w − ∆v,0γ
v
)
,∆w,0h
w
⟩
|v−w|p|v|p−2|w|p−2 +
⟨
P⊤
∆w,0γ
(∆v,0γ
v − ∆w,0γ
w
)
,∆v,0h
v
⟩
|v−w|p|v|p−2|w|p−2
)
dw dv du.
20
Using
Q(p)(γ; h) :=
$
R/Z×D
(⟨∆w,0γ
w − ∆v,0γ
v ,∆w,0h
w − ∆v,0h
v
⟩
|v−w|p|v|p−2|w|p−2
)
dw dv du
we hence get
δM p,2 = 12
(
Q(p) + 1
2R1 + R2 + R3
)
. (4.2)
Proposition 4.1. The functional Q(p) is bilinear on
(
W3p/2−2,2
)2
, more precisely
Q(p)( f,g ) =
∑
k∈Z
ϱk
⟨ ˆfk, ˆgk
⟩
Cd whereϱk = c|k|3p−4 + o
(
|k|3p−4)
as|k|↗∞
and c> 0. Here ˆ·k denotes the k-th Fourier coeﬃcient
ˆfk :=
∫ 1
0
f (x)e−2πikx dx.
Proof. Testing with the basis e l· e2πikx of L2, l = 1, 2, 3, k∈ Z, where e 1, e2, e3 is the
standard basis of R3, we get
Q(p)( f,g ) =
∑
k∈Z
⟨ ˆfk, ˆgk
⟩
Cdϱk
where
ϱk :=
"
D
⏐⏐⏐⏐ e2πikw−1
w − e2πikv−1
v
⏐⏐⏐⏐
2
|v|p−2|w|p−2|v−w|p dw dv.
A simple substitution leads to
ϱk =|k|3p−4
"
Dk
⏐⏐⏐⏐ e2πiw−1
w − e2πiv−1
v
⏐⏐⏐⏐
2
|v|p−2|w|p−2|v−w|p dw dv
where Dk := k· D. We use the fundamental thorem of calculus and Jensen’s inequality
to get
⏐⏐⏐⏐ e2πiw−1
w − e2πiv−1
v
⏐⏐⏐⏐
2
|v|p−2|w|p−2|v−w|p≤ 4π2
∫ 1
0
|e2πiθw− e2πiθv|2
|w|p−2|v|p−2|v−w|p dθ
= 4π2
∫ 1
0
|e2πiθ(v−w)− 1|2
|w|p−2|v|p−2|v−w|p dθ.
Hence,
"
v<0,w>0
⏐⏐⏐⏐ e2πikw−1
w − e2πikv−1
v
⏐⏐⏐⏐
2
|v|p−2|w|p−2|v−w|p≤ C
"
v<0,w>0
∫ 1
0
|e2πiθ(v−w)− 1|2
|w|p−2|v|p−2|v−w|p dθ dw dv
21
= C
(∫ 1
0
θ3p−6 dθ
) "
v<0,w>0
|e2πi(v−w)− 1|2
|w|p−2|v|p−2|v−w|p dw dv
≤ C
"
v<0,w>0
|e2πi(v−w)− 1|2
|w|p−2|v|p−2|v−w|p dw dv
= C
∫ ∞
0
∫ ˜w
0
|e−2πi ˜w− 1|2
| ˜w−v|p−2|v|p−2| ˜w|p dv d ˜w
= C
∫ ∞
0
∫ 1
0
|e−2πi ˜w− 1|2
|1− t|p−2|t|p−2| ˜w|3p−5 dt d ˜w
≤ C
∫ ∞
0
1− cos 2π ˜w
| ˜w|3p−5 d ˜w< ∞.
Thus, we have shown that
ϱk
|k|3k−4
|k|→∞
−−−−→
"
v<0,w>0
⏐⏐⏐⏐ e2πikw−1
w − e2πikv−1
v
⏐⏐⏐⏐
2
|v|p−2|w|p−2|v−w|p dw dv∈ (0,∞). □
In the following statement, we use the symbol⊗ to denote any kind of product structure,
such as cross product, dot product, scalar or matrix multiplication.
Lemma 4.2. The term R(p) := 1
2R1 + R2 + R3 is a ﬁnite sum of terms of the form
$
R/Z×D
(
[0,1]K
gp(u,v,w ; s1,..., sK−2)⊗ h′(u + sK−1v + sKw) dθ1··· dθK dv dw du
whereG(p) : (0,∞)3→ R is an analytic funtion, s j∈
{
0,θ j
}
for j = 1,..., K,
gp(u,v,w ; s1,..., sK−2) =G(p)
(|∆0,wγ|
|w| ,|∆0,vγ|
|v| ,|∆v,wγ|
|v−w|
)
Γ(u,v,w, s1, s2)·
·

K1⨂
i=3
γ′(u + siv)
⊗

K2⨂
j=K1
γ′(u + siw)
⊗

K−2⨂
j=K2
γ′(u +v + si(w−v))
,
and Γ(u,v,w, s1, s2) is a term of one of the four types
(γ′(u + s1w)−γ′(u + s1v))⊗ (γ′(u + s2w)−γ′(u + s2v))
|v|p−2|w|p−2|v−w|p ,
|γ′(u + s1w)−γ′(u + s2w)|2
|v|p−2|w|p−2|v−w|p ,
|γ′(u + s1v)−γ′(u + s2v)|2
|v|p−2|w|p−2|v−w|p ,
|γ′(u +v + s1(w−v))−γ′(u +v + s2(w−v))|2
|v|p−2|w|p−2|v−w|p .
Proof. Using
⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐2
|∆w,0γ|p+2|∆v,0γ|p|∆v,wγ|p· ⟨∆w,0γ,∆w,0h⟩ =G(p)
(|∆0,wγ|
|w| ,|∆0,vγ|
|v| ,|∆v,wγ|
|v−w|
) ⏐⏐⏐∆w,0γ∧∆ v,0γ
⏐⏐⏐2
|w|p+2|v|p|v−w|p· ⟨∆w,0γ,∆w,0h⟩
22
whereG(p)(z1, z2, z2) = z−p−2
1 z−p
2 z−p
3 together with
∆w,0γ
w ∧∆v,0γ
v =
(∆w,0γ
w −∆v,0γ
v
)
∧∆v,0γ
v =
∫ 1
0
∫ 1
0
(γ′(u + s1w)−γ′(u + s1v))∧γ′(u+s3v) ds1 ds3
we see that the ﬁrst term of R1 is of type 1. Similarly, one gets that all the terms of R1
are of type 1.
For the term R2 we use
⟨
P⊥
∆0,vγ(∆0,wγ),∆0,wh
⟩
= 1
|∆0,vγ|2
⟨(∆0,vγ∧∆ 0,wγ), (∆0,vγ∧∆ 0,wh)⟩
(4.1)
= v2w2
|∆0,vγ|2
(
[0,1]4
γ′(u+s1v)⊗γ′(u+s2w)⊗γ′(u+s3v)⊗h′(u+s4w) ds1 ds2 ds3 ds4
together with the fact that forw∈ R, u∈ R/Z
1
|∆w,0γ|α− 1
|w|α = 2G(α)

⏐⏐⏐∆w,0γ
⏐⏐⏐
|w|

1−|∆w,0γ|
2
|w|2
|w|α
=G(α)

⏐⏐⏐∆w,0γ
⏐⏐⏐
|w|

"
[0,1]2
|γ′(u + s1w)−γ′(u + s2w)|2
|w|α ds1 ds2
(4.3)
whereG(α)(z) = 1
2· 1−zα
1−z2· z−α is analytic on (0,∞) for α >0. Both equations together
with
1⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2 ⏐⏐⏐∆w,0γ
⏐⏐⏐p− 1
|v−w|p|v|p−2|w|p
=

1⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2 ⏐⏐⏐∆w,0γ
⏐⏐⏐p− 1⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2
|w|p

+

1⏐⏐⏐∆v,wγ
⏐⏐⏐p ⏐⏐⏐∆v,0γ
⏐⏐⏐p−2
|w|p
− 1⏐⏐⏐∆v,wγ
⏐⏐⏐p
|v|p−2|w|p

+

1⏐⏐⏐∆v,wγ
⏐⏐⏐p
|v|p−2|w|p− 1
|v−w|p|v|p−2|w|p

show that the frist term ofR2 is the sum of terms of type 2 to 4. Similarly for the second
term in R2.
Let us turn to the last term,R3. Again, we restrict to the ﬁrst term, the second is parallel.
We obtain
⟨
P⊤
∆v,0γ
(∆w,0γ
w − ∆v,0γ
v
)
,∆w,0h
w
⟩
|v−w|p|v|p−2|w|p−2 =
⟨
∆w,0γ
w − ∆v,0γ
v , ∆v,0γ
|∆v,0γ|
⟩
|v−w|p|v|p−2|w|p−2
⟨∆v,0γ⏐⏐⏐∆v,0γ
⏐⏐⏐,∆w,0h
w
⟩
=
⏐⏐⏐⏐⏐
∆v,0γ
v
⏐⏐⏐⏐⏐
−2
⟨∆w,0γ
w − ∆v,0γ
v ,∆v,0γ
v
⟩
|v−w|p|v|p−2|w|p−2
⟨∆v,0γ
v ,∆w,0h
w
⟩
23
=
⏐⏐⏐⏐⏐
∆v,0γ
v
⏐⏐⏐⏐⏐
−2
(⟨∆w,0γ
w ,∆v,0γ
v
⟩
− 1
)
|v−w|p|v|p−2|w|p−2
⟨∆v,0γ
v ,∆w,0h
w
⟩
=− 1
2
⏐⏐⏐⏐⏐
∆v,0γ
v
⏐⏐⏐⏐⏐
−2
⏐⏐⏐∆w,0γ
w − ∆v,0γ
v
⏐⏐⏐
2
|v−w|p|v|p−2|w|p−2
⟨∆v,0γ
v ,∆w,0h
w
⟩
,
which gives rise to type 4. □
Our next task is to show that Rp is in fact a lower-order term. More precisely, we have
Proposition 4.3 (Regularity of the remainder term). Ifγ∈ W(3p−4)/2+σ,2
ia (R/Z, Rn)
for someσ≥ 0 then Rp(γ,·)∈
(
W3/2−σ+ε,2
)∗
for anyε> 0.
This statement together with Proposition 4.1 immediately leads to the proof of the
regularity theorem which is deferred to the end of this section.
To prove Proposition 4.3, we ﬁrst note that, by partial integration, the terms ofR(p)(γ, h)
may be transformed into
(
[0,1]K
"
D
∫
R/Z
(
(−∆) ˜σ/2gp(·,v,w ; s1,..., sK−2)
)
(u)⊗
(
(−∆)− ˜σ/2h′)
(u + sK−1v + sKw) du dv dw dθ1··· dθK
≤
(
[0,1]K
"
D
‖gp(·,v,w ;... )‖W ˜σ,1(R/Z,Rn) dv dw dθ1··· dθK−2
‖‖‖(−∆)− ˜σ/2h′‖‖‖L∞(R/Z,Rn)
≤
(
[0,1]K
"
D
‖gp(... )‖W ˜σ,1(R/Z,Rn) dv dw dθ1··· dθK−2‖h‖W3/2+ε/2− ˜σ,2(R/Z,Rn),
where ˜σ ∈ R, ε > 0 can be chosen arbitrarily, and ( −∆) ˜σ/2 denotes the fractional
Laplacian. We let ˜σ := 0 ifσ = 0 and ˜σ := σ− ε
2 otherwise. Now the claim directly
follows from the succeeding auxiliary result.
Lemma 4.4 (Regularity of the remainder integrand). Letγ∈ W(3p−4)/2+σ,2
ia .
• Ifσ = 0 thengp∈ L1(R/Z× D, Rn) and
• ifσ> 0 then ((v,w )↦→gp(·,v,w ;... ))∈ L1(D, W ˜σ,1(R/Z, Rn)) for any ˜σ<σ .
The respective norms are bounded independently of s1,..., sK.
Proof. Recall that the argument ofG(p) is compact and bounded away from zero. Using
arc-length parametrization, we immediately obtain for the ﬁrst type
$
R/Z×D
|gp(u,v,w )| dv dw du≤ C
$
R/Z×D
|γ′(u + s1w)−γ′(u + s1v)|2
|w|p−2|v|p−2|w−v|p dw dv du
= C
$
R/Z×D
|γ′(u + s1(w−v))−γ′(u)|2
|w|p−2|v|p−2|w−v|p dw dv du
(1.3)
≤ C‖γ‖2
W(3p−4)/2,2.
24
For a term of the second type we get
$
R/Z×D
|gp(u,v,w )| dv dw du≤ C
$
R/Z×D
|γ′(u + s1w)−γ′(u + s2w)|2
|w|p−2|v|p−2|w−v|p dw dv du
= C
∫
R/Z
∫ 2/3
0
|γ′(u + s1w)−γ′(u + s2w)|2
|w|p−2
(∫ 2/3−w
0
1
vp−2(v +w)p dv
)
dw du
≤ C
∫
R/Z
∫ 2/3
0
|γ′(u + s1w)−γ′(u + s2w)|2
|w|3p−5
(∫ ∞
0
1
tp−2(1 + t)p dt
)
dw du
≤ C [γ]
W(3p−4)/2,2
and of course the same estimate is true for a term of the third kind. For term of type
four, we get along the same lines
$
R/Z×D
|gp(u,v,w )| dv dw du≤ C
$
R/Z×D
|γ′(u +v + s1(w−v)−γ′(u +v + s2(w−v))|2
|w|p−2|v|p−2|w−v|p dw dv du
= C
∫
(R/Z,Rn)
∫ 2/3
0
|γ′(u + s1(w +v))−γ′(u + s2(w +v))|2
|w|p−2
(∫ 2/3−w
0
1
(v +w)pvp−2 dv
)
dw du
≤ C
∫
(R/Z,Rn)
∫ 2/3
0
|γ′(u + s1 ˜w)−γ′(u + s2 ˜w)|2
| ˜w|3p−5
(∫ ∞
0
1
(t + 1)ptp−2 dt
)
dw du
≤ C [γ]
W(3p−4)/2,2.
We prove the second claim only for terms of the ﬁrst type, as the arguments for all
other terms follow the same line of argments. We will derive a suitable bound on
‖gp(·,w )‖W ˜σ,r for some r > 1. To this end, we choose q1,..., qK−2, which will be
determined more precisely later on, such that
K−2∑
i=1
1
qi
= 1
r.
The product rule, Lemma A.1, then leads to
‖gp(·,w )‖W ˜σ,r≤ C
‖‖‖G(p)‖‖‖W ˜σ,q1
‖γ′(· + s1w)−γ′(· + s1v)‖2
W ˜σ,2q2
|v|p−2|w|p−2|w−v|p
K−2∏
i=3
‖‖‖γ′‖‖‖W ˜σ,qi.
= C
‖‖‖G(p)‖‖‖W ˜σ,q1
‖γ′(· + s1(w−v))−γ′(·)‖2
W ˜σ,2q2
|v|p−2|w|p−2|w−v|p
K−2∏
i=3
‖‖‖γ′‖‖‖W ˜σ,qi.
For the second factor, we now choose q2 > r so small that Wσ,2 embeds into W ˜σ,2q2.
To this end, we set 1
r := 1− (σ− ˜σ) and 1
q2
:= 1− 2(σ− ˜σ). and qi := K−3
σ− ˜σ for
i = 1, 3, 4,..., K− 2.
Then for the ﬁrst factor we apply the chain rule, Lemma A.2. Recall thatG(p) is analytic
and its argument is bounded below away from zero and above by 1. We infer
‖‖‖G(p)‖‖‖W ˜σ,q1≤ C
‖‖‖γ′‖‖‖W ˜σ,q1 .
The Sobolev embedding gives
‖‖‖γ′‖‖‖W ˜σ,qi≤ C‖γ‖W(3p−4)/2+σ,2≤ C for i = 1, 3, 4,..., K− 2.
25
Together this leads to
‖gp(·,v,w )‖W ˜σ,r≤ C
‖γ′(· + s1(w−v))−γ′(·)‖2
Wσ,2
|v|p−2|w|p−2|w−v|p
and ﬁnally
"
D
‖gp(·,w )‖W ˜σ,r dv dw≤ C
"
D
‖γ′(· + s1(w−v))−γ′(·)‖2
Wσ,2
|v|p−2|w|p−2|w−v|p dv dw
(1.3)
≤ C‖γ‖W(3p−4)/2,2. □
Proof of Theorem 4. We start with the Euler-Lagrange Equation
δintM(p,q)(γ, h) +λ⟨γ′, h′⟩
L2 = 0 (4.4)
for any h∈ C∞(R/Z, Rn) whereλ∈ R is a Lagrange parameter stemming from the side
condition (ﬁxed length). Using (4.2) this reads
12Q(p)(γ, h) +λ⟨γ′, h′⟩
L2 + 12R(p)(γ, h) = 0. (4.5)
Since ﬁrst variation of the length functional satisﬁes
⟨γ′, h′⟩
L2 =
∑
k∈Z
|2πk|2 ⟨
ˆγk, ˆhk
⟩
Cd,
we get using Proposition 4.1 that there is a ˜c> 0 such that
12Q(p)(γ, h) +λ⟨γ′, h′⟩
L2 =
∑
k∈Z
˜ϱk
⟨
ˆγk, ˆhk
⟩
Cd (4.6)
where
˜ϱk = ˜c|k|3p−4 + o
(
|k|p−1)
as|k|↗∞.
Assuming thatγ∈ W(3p−4)/2+σ,2
ia for someσ≥ 0, we infer
12Q(p)(γ,·) +λ⟨γ′,·′⟩
L2∈
(
W3/2−σ+ε,2)∗
applying Proposition 4.3 to (4.5). Equation (4.6) implies
(
˜ϱk|k|−3/2+σ−ε ˆγk
)
k∈Z∈𝓁2.
Recalling that ˜ϱk|k|−3p+4 converges to a positive constant as|k|↗∞ , we are led to
γ∈ W
3p−4
2 +σ + 3p−7
2 −ε.
Choosingε := 3p−7
4 > 0, we gain a positive amount of regularity that does not depend
onσ. So by a simple iteration we get γ∈ W s,2 for all s≥ 0. □
