---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-010-4-partial-uniform-estimates
section_title: "Partial uniform estimates"
section_number: 4
pages: 17-22
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
---
Let M be a Riemann surface of genus g and constant curvature ( −1).
In this section, we prove that there is a (positive) lower bou nd of (1.1)
depending only on the injective radius of the point. More pre cisely, for
m large enough, for any x ∈ M , there is a section S ∈ H 0(M,K m
M ) such
that ||S||L2 = 1 and ||S||(x) ≥ C(δx) where C(δx) is a positive constant
depending only on δx and δx is the injective radius at x.
17
Note that in the result the lower bound doesn’t depend on the i njective
radius of M , which will go to zero as M approaches the boundary of the
Teichm¨ uller space.
We use all the notations of in § 3 about the collars and the functions on
them. The following proposition is a corollary of the collar theorem:
Proposition 4.1. LetM be a Riemann surface of genus g ≥ 2 and constant
curvature (−1). Let γ1, · · ·,γ s be the closed geodesics on M such that
length(γi) ≤ 1
1000, 1 ≤i ≤s.
Let Cγi(1 ≤ i ≤ s) be the corresponding collars embedded in M (Theo-
rem 3.1). Then for any x ∈ M \U s
i=1Cγi, there is an absolute constant
ε2 > 0 such that
δx ≥ε2.
Proof. Let δ = 1
4000 . Let x ∈ M \ ∪s
i=1Cγi and inj(x) ≥ δx > 0. Then
there is a point y ∈M such that there are two geodesics l1 andl2 connecting
x andy butl1 andl2 are not homotopic to each other. If δx> 1, the theorem
has been proved. Otherwise, let γ′ be the shortest closed curve homotopic
to the closed curve l−1
1 l2 in
D′ =M \ ∪
length(γi)<2δ
Cγi(Ri − 2),
where
Cγi(Ri − 2) = {x|dist(x,γ i)<R i − 2}.
SinceD′ is a compact set. If γ′ doesn’t touch any of the boundary ∂C γi(Ri −
2) for any i, then γ′ must be a closed geodesic and by the deﬁnition, we
have length(γ) ≥ 1
1000 and thus δx ≥ 1
2000 . Otherwise either δx > 1 or
γ′ ⊂Cγi(Ri − 1)\Cγi (Ri − 2) for some i. In the latter case, since γ′ is not
homotopic to zero, we see that
length(γ′) ≥length(γi) cosh(Ri − 2) ≥ 1
18ε1
(remember length(γi) sinhRi =ε1). Thus
δx ≥ 1
2length(γ′) ≥ 1
36ε1 ≥ε2
for ε2 = 1
36ε1.
Using the above lemma, we know that outside the collars whose shortest
closed geodesics are small, the injective radius has a lower bound and the
weight function in Proposition 2.1 can be constructed in the ordinary way.
Ifx ∈Cγi for some i, we are going to construct the weight functions having
the compact support within Cγi. For this reason, let’s ﬁrst assume that Cδ
is a collar with δ < 1
1000 and do some analysis on it.
18
Let’s ﬁx some notations: there are absolute constants ε3,ε 4 > 0 such that
ε3 <δ coshR,δ cosh(R ± 4),δ sinh(R ± 4),δe R±4 <ε 4.(4.1)
Let (ρ,θ ) be the local coordinate of the collar C =Cδ as in § 3. Then
w =e
2πi
δ θ− 4π
δ (arctan eρ − π
4 )(4.2)
is the holomorphic function on Cδ. Let x0 and p0 be the points on Cδ such
that the local coordinate of x0 and p0 can be represented as: x0 = (ρ0, 0)
for R − 4 > ρ0 ≥ 0 and p0 = (R − 1, 0). The function w at x0 and p0 has
the values
w0 =e− 4π
δ (arctan eρ 0 − π
4 ),
wp0 =e− 4π
δ (arctan eR− 1− π
4 )
(4.3)
at x0 and p0 respectively. Let
α = 2 arctaneρ0
π ,(4.4)
and deﬁne the functions ϕ 1, ϕ 2 and ϕ 3 on Cδ to be
ϕ 1 = log |w
w0
− 1|,
ϕ 2 = log | w
wp0
− 1|,
ϕ 3 =ϕ 1 −αϕ 2.
(4.5)
The Riemann metric on Cδ can be represented as
ds2 =dρ2 + (coshρ)2dθ2.(4.6)
Let the injective radius at x0,p0 andx be δx0,δp0 andδx. Then we have an
absolute constant ε5 > 0 such that



1
2δ coshρ0 >δ x0 >ε 5δ coshρ0,
1
2ε1 >δ p0 >ε 5,
1
2δ coshρ>δ x >ε 5δ coshρ.
(4.7)
We establish some elementary properties of the function ϕ 3. Let d =d(x)
be the distance function to the point x0. Then we have
Lemma 4.1. With the notations as above, there are constants C9,C 10 > 0
such that
ϕ 3 ≤C9,(4.8)
for −R + 1 ≤ρ ≤R − 2 and
ϕ 3 ≥ logd(x) − 4π
δeρ −C10(4.9)
for d(x) ≤δx0.
19
Proof. By (4.2) and (4.3), we have
w
w0
=e
2πi
δ θ− 4π
δ (arctan eρ −arctan eρ 0 ),
w
wp0
=e
2πi
δ θ− 4π
δ (arctan eρ −arctan eR− 1).
(4.10)
From (4.10), we have









log | w
w0
− 1| ≤ log 2 ρ0 ≤ρ ≤R − 2,
log |1 − w0
w | ≤ log 2 −R + 1 ≤ρ ≤ρ0,
log | w
wp0
| ≥ 0 −R + 1 ≤ρ ≤R − 1,
log |1 − wp0
w | ≥ log(1 −e− 2π
ε4 ) −R + 1 ≤ρ ≤R − 2.
(4.11)
If ρ0 ≤ρ ≤R − 2, then we can write
ϕ 3 = log |w
w0
− 1| −α log | w
wp0
| −α log |1 − wp0
w |.
By (4.11), we have
ϕ 3 ≤ log 2 − log(1 −e− 2π
ε4 ).(4.12)
If −R + 1 ≤ρ ≤ρ0. We can write
ϕ 3 = log |w
w0
| −α log | w
wp0
| + log |1 − w0
w | −α log |1 − wp0
w |.(4.13)
Using (4.10), we have
log |w
w0
| −α log | w
wp0
|
= − 8
δ(π
2 − arctaneρ0) arctaneρ + 8
δ arctaneρ0(π
2 − arctaneR−1).
(4.14)
Thus by (4.1) and (4.7)
− 4ε5
δx0
≤ log |w
w0
| −α log | w
wp0
| ≤ 4π
ε3
.(4.15)
By (4.11), (4.13) and (4.15), we have
ϕ 3 ≤ 4π
ε3
+ log 2 − log(1 −e− 2π
ε4 ).(4.16)
Thus by (4.12) and (4.16), we have ϕ 3 ≤C9 for
C9 = 4π
ε3
+ log 2 − log(1 −e− 2π
ε4 ).
Let’s now assume that d(x) < δx0. Then by the triangle inequality we
have 


|ρ −ρ0| + |θ| coshρ0 ≥d(x) 0 ≤θ coshρ0<d (x),
|ρ −ρ0| + |θ −δ coshρ0| ≥ d(x) δ coshρ0 −d(x)
<θ coshρ0 <δ coshρ0.
(4.17)
20
Without losing generality we assume that 0 ≤ θ ≤ d(x) and |ρ −ρ0| +
|θ| coshρ0 ≥d(x). If θ coshρ0 ≥ 1
4d(x), then
|w
w0
− 1| ≥ e− 4π
δ (arctan eρ −arctan eρ 0 ) sin 2π
δ θ ≥ π
4e−πd(x).(4.18)
On the other hand, if |ρ −ρ0| ≥ 1
2d(x), then
|w
w0
− 1| ≥ e−π 2π
ε1
d.(4.19)
By (4.18) and (4.19), there is a constant C11> 0 such that
log |w
w0
− 1| ≥ logd −C11.(4.20)
We also have
log | w
wp0
− 1| ≤ log 2 + 4π
δeρ.(4.21)
for d ≤δx0. By (4.20) and (4.21), from (4.5)
ϕ 3 ≥ logd −C11 − (log 2 + 4π
δeρ ).
This completes the proof of Lemma 4.1.
Lemma 4.2. There is a constant C12> 0 such that
|ϕ 3| ≤ C12, |∇ϕ 3| ≤ C12
for R − 3< |ρ|<R − 2.
Proof. By the above lemma, we see that
ϕ 3 ≤C9
for the constant C9. Thus we just need to prove the lower bound of ϕ 3 and
the bound for the derivative of ϕ 3.
If R − 3<ρ<R − 2, by (4.10), we have
|w
w0
| ≤ e− 2π
ε1.(4.22)
Thus
ϕ 1 ≥ log(1 −e− 2π
ε1 ).(4.23)
Also we have
| w
wp0
| ≤ e
4π
ε3(4.24)
for R − 3<ρ<R − 2. Thus
ϕ 3 ≥ log(1 −e− 2π
ε1 ) − log(1 +e
4π
ε3 ).(4.25)
If R − 3< −ρ<R − 2, then by (4.14), we have
log |w
w0
| −α log | w
wp0
| ≥ − 8
δ(π
2 − arctaneρ0 ) arctane−(R−3) ≥ − 2
ε2
.
21
By (4.13), we have
ϕ 3 ≥ − 8
ε3
+ log(1 −e− π 2
2 ) − log 2.(4.26)
Combining (4.25) and (4.26), we get the lower bound of ϕ 3. Next let’s
consider ∇ϕ 3. Obviously
|∇ϕ 3| ≤ |∇ϕ 1| + |∇ϕ 2|.
Thus we just need to estimate |∇ϕ 1| and |∇ϕ 2|. By (4.6), the Riemann
metric under the coordinate w can be written as
ds2 = δ2(coshρ)2
4π 2|w|2 dwdw.
Thus
|∇ϕ 1|2 = 4π 2|w|2
δ2(coshρ)2 · 1
|w −w0|2 = 4π 2
δ2(coshρ)2 · 1
|1 − w0
w |2,
|∇ϕ 2|2 = 4π 2|w|2
δ2(coshρ)2 · 1
|w −wp0|2 = 4π 2
δ2(coshρ)2 · 1
|1 − wp0
w |2.
Using the same elementary estimates as above, we get,











| w0
w | ≥ e
2π
ε1 R − 3<ρ<R − 2,
| w0
w | ≤ e− π 2
2δ R − 3< −ρ<R − 2,
| wp0
w | ≤ e− 2π
ε1 R − 3<ρ<R − 2,
| wp0
w | ≤ e− π 2
2δ R − 3< −ρ<R − 2.
(4.27)
Using these results, we get the bound for the gradient of ϕ 1 and ϕ 2. This
completes the proof of the lemma.
The following proposition summarizes the technical result s of this section.
Proposition 4.2. SupposeM is a compact Riemann surface of genus g ≥ 2
and constant curvature (−1). Then for any x0 ∈ M , there is a function
ϕ =ϕ x0 such that ϕ is smooth on M \{x} and
