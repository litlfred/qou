---
doc_id: arxiv-1111.6782v2
doc_title: "Stationary Points of O’Hara’s Knot Energies"
section_id: sec-001-3-regularity-of-stationary-points
section_title: "Regularity of stationary points"
section_number: 3
pages: 13-17
source_pdf: 1111.6782v2.pdf
source_sha256: 5acfde49432e59e3
---
In this section we prove Theorem 1.2 so we are looking at embedded curves γ ∈
H(1+α)/2 parametrized by arc-length that satisfy
δE(α)(γ; h) +λ
∫
R/Z
⟨γ′, h′⟩= 0 ∀h∈ H(1+α)/2(R/Z, Rn) (3.1)
whereλ> 0 and
δE(α)(γ; h) = lim
εց0
/iintegdisplay
Uε
(
(α− 2)⟨γ′(u), h′(u)⟩
|w|α + 2 ⟨γ′(u), h′(u)⟩
|γ(u +w)−γ(u)|α
−α⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2
)
dw du.
To prove thatγ∈ C∞(R/Z, Rn), we ﬁrst decompose
δE(α)(γ; h) =αQ(α)(γ, h) + R(α)(γ, h) (3.2)
where
Q(α)(γ, h) := lim
εց0
/iintegdisplay
Uε
(⟨γ′(u), h′(u)⟩
|w|α −⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|w|α+2
)
dw du
and R(α)(γ, h) is given by
R(α)(γ, h) := 2 lim
εց0
/iintegdisplay
Uε
⟨γ′(u), h′(u)⟩( 1
|γ(u +w)−γ(u)|α− 1
|w|α
)
dw du
−α lim
εց0
/iintegdisplay
Uε
⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
( 1
|γ(u +w)−γ(u)|α+2− 1
|w|α+2
)
dwdu.
Later on, it will become evident that, in contrast toQ(α), the integral deﬁning R(α) is not
a principle value, i. e. we may write U0 instead of Uε.
It was already observed by He in [13] and the second author in [19] that Q(α)(γ, h) is a
lower order perturbation of the L2 product of (−∆)
α+1
4 γ and (−∆)
α+1
4 h. To see this, let us
ﬁrst extend Q(α) to complex valued functions by exchanging the scalar produc t on Rn
to the scalar product on Cn. We denote by ˆf (k) =
∫
R/Z f (u)e−2πiku du the k-th Fourier
coeﬃcient of f .
Proposition 3.1 (cf. [13, Lemma 2.3], [19, Proposition 1.4]). There is a sequence of
real numbers qk, k∈ Z, converging to a positive constant for|k|→∞ such that for all
γ, h∈ H(1+α)/2,2(R/Z, Rn) we have
Q(α)(γ, h) =
∑
k∈Z
qk|k|α+1 ˆγ(k)ˆh(k). (3.3)
Apart from this observation, the proof of Theorem 1.2 relies on the following estimate
regarding the term R(α)(γ, h). Basically it lets us treat this term like a lower order
perturbation.
Proposition 3.2. Letγ∈ H(α+1)/2+σ
ir be parametrized by arc-length,σ≥ 0.
13
(i) In the caseσ = 0 we have R(α)(γ,·)∈
(
H3/2+ε,2)∗
for anyε> 0.
(ii) Ifσ> 0 we have R(α)(γ,·)∈
(
H3/2− ˆσ,2
)∗
for all ˆσ<σ .
We will prove Proposition 3.2 using Sobolev embeddings and the fractional Leibniz
rule for Bessel potential spaces (cf. Lemma A.1).
First we will show, that the two summands buildingR(α) can be brought into a common
form and can thus be dealt with simultaneously. For that we us e the fundamental
theorem of calculus to get
⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
( 1
|γ(u +w)−γ(u)|α+2− 1
|w|α+2
)
=w2
∫1
0
∫1
0
⟨γ′(u + s1w), h′(u + s2w)⟩( 1
|γ(u +w)−γ(u)|α+2− 1
|w|α+2
)
ds1 ds2.
Furthermore, forβ> 0,
1
|γ(u +w)−γ(u)|β− 1
|w|β = |w|β
|γ(u +w)−γ(u)|β·
1− |γ(u+w)−γ(u)|β
|w|β
|w|β
= G(β)
(γ(u +w)−γ(u)
w
)2− 2|γ(u+w)−γ(u)|2
w2
|w|β
=
∫1
0
∫1
0
G(β)
(γ(u +w)−γ(u)
w
)|γ′(u +τ1w)−γ′(u +τ2w)|2
|w|β dτ1dτ2
where
G(β)(z) := 1
2|z|β· 1−| z|β
1−| z|2
is an analytic function away from the origin. Deﬁning
g(α,β)
s1,τ1,τ2(u,w ) := G(β)
(γ(u +w)−γ(u)
w
)|γ′(u +τ1w)−γ′(u +τ2w)|2
|w|α γ′(u + s1w)
we thus get
R(α)(γ, h) = lim
εց0
{
2
/iintegdisplay
Uε
/iintegdisplay
[0,1]2
⟨
g(α,α)
0,τ1,τ2
(u,w ), h′(u)
⟩
dτ1 dτ2 dw du
−α
/iintegdisplay
Uε
/iiiintegdisplay
[0,1]4
⟨
g(α,α+2)
s1,τ1,τ2 (u,w ), h′(u + s2w)
⟩
ds1 ds2 dτ1 dτ2 dw du
}
.
(3.4)
Thus using H¨ older’s inequality we get the estimate
R(α)(γ, h)≤ C‖h′‖L∞ sup
β∈{α,α+2},
s1,τ1,τ2∈[0,1]
∫1/2
−1/2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖L1
dw
≤ C‖h‖H3/2+ε,2 sup
β∈{α,α+2},
s1,τ1,τ2∈[0,1]
∫1/2
−1/2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖L1
dw
(3.5)
14
for anyε> 0.
Forσ∈ R let
Dσ := (−∆)σ/2. (3.6)
By partial integration we infer for ˜σ∈ R
∫
R/Z
⟨
g(α,β)
s1,τ1,τ2(u,w ), h′(u + s2w)
⟩
du =
∫
R/Z
⟨
D ˜σg(α,β)
s1,τ1,τ2(u,w ), D− ˜σh′(u + s2w)
⟩
du
and we can estimate the absolute value by
‖‖‖D− ˜σh′‖‖‖L∞
∫
R/Z
⏐⏐⏐⏐D ˜σg(α,β)
s1,τ1,τ2(u,w )
⏐⏐⏐⏐du≤ C‖h‖H3/2− ˜σ+ε,2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖H ˜σ,1
for anyε> 0. Combining this with Equation (3.4) we get
⏐⏐⏐R(α)(γ, h)
⏐⏐⏐≤ C‖h‖H3/2− ˜σ+ε,2 sup
β∈{α,α+2},
s1,τ1,τ2∈[0,1]
∫1/2
−1/2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖H ˜σ,1 dw
for all ˜σ andε >0. To prove Proposition 3.2, givenσ > ˆσ we set ˜σ = (σ + ˆσ)/2> ˆσ
andε = ˜σ− ˆσ in the calculations above, to get
⏐⏐⏐R(α)(γ, h)
⏐⏐⏐≤ C‖h‖H3/2− ˆσ,2 sup
β∈{α,α+2},
s1,τ1,τ2∈[0,1]
∫ 1/2
−1/2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖H ˜σ,1 dw. (3.7)
Proposition 3.2 now immediately follows from Estimate ( 3.5), Estimate (3.7) and the
succeding lemma.
Lemma 3.3. Letγ∈ H(α+1)/2+σ,2(R/Z, Rn) withσ≥ 0 andβ> 0.
(i) Ifσ = 0 theng(α,β)
s1,τ1,τ2∈ L1(R/Z× (− 1
2, 1
2), Rn). Furthermore, there is a constant
C <∞ independent ofτ1,τ2, and s1 such that
‖‖‖‖g(α,β)
s1,τ1,τ2
‖‖‖‖L1≤ C.
(ii) Ifσ >0 theng(α,β)
s1,τ1,τ2,·,·∈ L1((− 1
2, 1
2), H ˜σ,1(R/Z, Rn)) for all ˜σ<σ and there is a
constant C<∞ independent ofτ1,τ2, and s1 such that
∫1/2
−1/2
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖H ˜σ,1 dw≤ C.
Proof. Let us ﬁrst deal with the case σ = 0. We get
‖g(α,β)
s1,τ1,τ2‖L1(R/Z×(− 1
2, 1
2 ),Rn)
≤
∫
R,Z
∫1/2
−1/2
G(β)
(γ(u +w)−γ(u)
w
)|γ′(u +τ1w)−γ′(u +τ2w)|2
|w|α
⏐⏐⏐γ′(u + s1w)
⏐⏐⏐dwdu
≤ C‖γ′‖L∞
∫
R/Z
∫1/2
−1/2
|γ′(u +τ1w)−γ′(u +τ2w)|2
|w|α dwdu
≤ C‖γ′‖L∞‖γ‖2
H(α+1)/2,2
15
which proves the statement forσ = 0.
Since there is no suitable product rule for p = 1, we will estimate
‖‖‖‖g(α,β)
s1,τ1,τ2(·,w )
‖‖‖‖H ˜σ,p
for p> 1 suﬃciently small. For this we will use a small ˜p> p and let q be such that
1
p = 1
2 ˜p + 1
2 ˜p + 1
q + 1
q,
i. e. we set
q = 2 ˜pp
˜p− p.
Using that
γ(u +w)−γ(u)
w =
∫1
0
γ′(u +τw)dτ,
thatγ is bi-Lipschitz, and that G(β) is analytic away from the origin, we get that
‖‖‖‖‖‖G(β)
(γ(· +w)−γ(·)
w
)‖‖‖‖‖‖H ˜σ,q
≤ C‖γ‖H ˜σ+1,q≤ C
by the Sobolev embedding.
Using the fractional Leibniz rule (Lemma A.1) three times, we derive for ˜σ∈ (0,σ )
‖g(α,β)
s1,τ1,τ2(·,w )‖H ˜σ,p
≤ C
‖‖‖‖‖‖G(β)
(γ(· +w)−γ(·)
w
)‖‖‖‖‖‖H ˜σ,q
‖γ′‖H ˜σ,q
‖γ′(· +τ1w)−γ′(· +τ2w)‖2
H ˜σ,2 ˜p
|w|α
≤ C
‖γ′(· +τ1w)−γ′(· +τ2w)‖2
H ˜σ,2 ˜p
|w|α .
We now choose ˜p> 1 so small that Hσ,2 embeds into H ˜σ,2 ˜p and hence
‖g(α,β)
s1,τ1,τ2(·,w )‖H ˜σ,p≤ C
‖γ′(· +τ1w)−γ′(· +τ2w)‖2
Hσ,2
|w|α .
Thus, recalling (3.6),
∫1/2
−1/2
‖g(α,β)
s1,τ1,τ2(·,w )‖H ˜σ,p dw≤ C
∫1/2
−1/2
‖γ′(· +τ1w)−γ′(· +τ2w)‖2
L2
|w|α dw
+ C
∫1/2
−1/2
‖Dσ+1γ(· +τ1w)− Dσ+1γ(· +τ2w)‖2
L2
|w|α dw
≤ C
∫1/2
−1/2
‖γ′(·)−γ′(· + (τ2−τ1)w)‖2
L2
|w|α dw
+ C
∫1/2
−1/2
‖Dσ+1γ(·)− Dσ+1γ(· + (τ2−τ1)w)‖2
L2
|w|α dw
≤ C|τ2−τ1|
∫1
−1
‖γ′(·)−γ′(· +w)‖2
L2
|w|α dw
+ C|τ2−τ1|
∫1
−1
‖Dσ+1γ(·)− Dσ+1γ(· +w)‖2
L2
|w|α dw
≤ C‖γ′‖2
H(α−1)/2,2 + C‖Dσ+1γ‖2
H(α−1)/2,2≤ C.
16
This proves Lemma 3.3. □
Proof of Theorem 1.2. Recall that any ﬁnite-energy curve belongs to H(α+1)/2,2 by [3].
Let us assume that γ∈ H
α+1
2 +σ,2(R/Z, Rn) forσ≥ 0 is a stationary point of the energy
E(α) +λL . As the ﬁrst variation of the length functional gives rise to a linear lower
order term, Proposition 3.1 also applies to
~Q(α)
λ (γ, h) :=αQ(α)(γ, h) +λ
∫
R/Z
⟨γ′, h′⟩.
In the case thatσ = 0 we get from the Euler-Lagrange Equation (3.1) using the decom-
position (3.2) and Proposition 3.2
~Q(α)
λ (γ,·)∈
(
H3/2+ε,2)∗
for anyε> 0. Using Proposition 3.1 we hence get
(qk|k|α+1−3/2−ε ˆγ(k))k∈Z∈ℓ2.
Together with the fact that qk converge to a positive constant as k → ∞we get(
|k|α+1−3/2−ε ˆγ(k)
)
k∈Z∈ℓ2 and hence
γ∈ H
α+1
2 +α−2
2 −ε,2(R/Z, Rn).
Forσ> 0 we get using Proposition 3.2
~Q(α)
λ (γ,·)∈
(
H
3
2− ˆσ)∗
for all ˆσ<σ
and arguing as above
γ∈ H
(α+1
2 + ˆσ
)
+α−2
2 ,2
(R/Z, Rn)
for all ˆσ<σ .
If we now initially assume that γ∈ H
α+1
2 ,2 we deduce by induction and since α−2
2 > 0
that
γ∈ Hs,2(R/Z, Rn)
for all s∈ R and thusγ∈ C∞(R/Z, Rn). This proves Theorem 1.2 □
