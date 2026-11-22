---
doc_id: arxiv-1202.5426v2
doc_title: "Hard analysis meets critical knots"
section_id: sec-003-4-bootstrapping-proof-of-theorem-iv
section_title: "Bootstrapping: Proof of Theorem IV"
section_number: 4
pages: 32-49
source_pdf: 1202.5426v2.pdf
source_sha256: 6c7668ad72e33b4b
toc_source: outline
doc_brief: "Hard analysis meets critical knots — 5 sections: Front matter; Introduction; Euler-Lagrange equation: Proof of"
---
In Theorem III we have shown, that |D|
1
2 g′ ∈Lp for some p > 2. We now work with Bessel-
potential / Sobolev spaces Hs,q, cf. [RS96, Tar07, Tri83], and the fact that |D|
1
2 g′ ∈Lp readily
implies that g′ ∈H
3
2 , ˜p for some ˜p ∈(2, p). The proof of Theorem IV relies on the decomposi-
tion of the ﬁrst variation
δE(2)(γ, h) = 2 lim
εց0
"
Uε
 
⟨γ′(u), h′(u)⟩
|γ(u + w) −γ(u)|2 −⟨γ(u + w) −γ(u), h(u + w) −h(u)⟩
|γ(u + w) −γ(u)|4
!
dw du,
Uε as in (1.2), into
2 (Q(γ, h) −T1(γ, h) −T2(γ, h)).
For a stationary point of the M¨obius energy we have
Q(γ, h) = T(γ, h) := T1(γ, h) + T2(γ, h)
for all h ∈H3/2(R/Z, Rn).
Let us bring these terms in a common form. Using
1
|γ(u + w) −γ(u)|α −
1
|w|α =
|w|α
|γ(u + w) −γ(u)|α

1 −|γ(u+w)−γ(u)|α
|w|α
|w|α

= Gα
 γ(u + w) −γ(u)
w
! 
2 −2 |γ(u+w)−γ(u)|2
|w|2
|w|α

=
1
Z
0
1
Z
0
Gα
 γ(u + w) −γ(u)
w
! |γ′(u + τ1w) −γ′(u + τ2w)|2
|w|α
!
dτ1dτ2
where
Gα(z) :=
1
2|z|α · 1 −|z|α
1 −|z|2
32
is an analytic function away from the origin for α ≥2. We hence get
T1(γ, h) = −
1
Z
0
1
Z
0
T 2
0,0,τ1,τ2(h)dτ1dτ2
T2(γ, h) =
1
Z
0
1
Z
0
1
Z
0
1
Z
0
T 4
s1,s2,τ1,τ2(h)dτ1dτ2ds1ds2
where
T α
s1,s2,τ1,τ2(h)
:=
1
Z
0
1/2
Z
−1/2
Gα
 γ(u + w) −γ(u)
w
! |γ′(u + τ1w) −γ′(u + τ2w)|2
w2
γ′(u + s1w)h′(u + s2w)dw du.
In the rest of this section, we will derive some estimates for the linear operators T α
s1,s2,τ1,τ2 that
do not depend on s1, s2, τ1, and τ2.
For this task, we will work with the Besov spaces Bs
p,q. Given s ∈(0, 1) and p, q ∈[1, ∞) one
way to deﬁne the norm on these spaces is to set
|f|Bsp,q :=

1/2
Z
−1/2
R
R/Z |f(u + w) −f(u)|pdu
q/p
|w|1+sq
dw

1/q
and to put
∥f∥Bsp,q := ∥f∥Lp + |f|Bsp,q.
The Besov space Bs
p,q(R/Z, Rn) then consists of all functions f ∈Lp with |f|Bsp,q < ∞.
Apart from this deﬁnition we just need the Sobolev embedding
H ˜s, ˜p ⊂Bs
p,q
if s < ˜s and s −1
p < ˜s −1
˜p which can be found in textbooks like, e.g., [Tri83, RS96, Tar07].
We also refer to [DNPV11].
The proof relies furthermore on the following rules for Bessel potential spaces.
Lemma 4.1 (Fractional Leibniz rule [CM78], [RS96, Lem. 5.3.7/1 (i)] ). Let f ∈Hs,p(R/Z, Rn),
g ∈Hs,q(R/Z, Rn) with s > 0, p, q, r ∈(1, ∞) and 1/p + 1/q = 1/r.
Then fg ∈Hs,r(R/Z, Rn) and
∥fg∥Hs,r ≤C (∥f∥Hs,p∥g∥Lq + ∥f∥Lp∥g∥Hs,q) .
33
For the following statement, one mainly has to treat

(Dkψ) ◦f

Hσ,p for k ∈N ∪{0} and
σ ∈(0, 1) which is e. g. covered by [RS96, Thm. 5.3.6/1 (i)].
Lemma 4.2 (Fractional chain rule). Let f ∈Hs,p(R/Z, Rn), s > 0, p ∈(1, ∞). If ψ ∈C∞(R)
is globally Lipschitz continuous and ψ and all its derivatives vanish at 0 then ψ ◦f ∈Hs,p and
∥ψ ◦f∥Hs,p ≤C∥ψ∥Ck∥f∥Hs,p
where k is the smallest integer greater than or equal to s.
The key to the proof of Theorem IV is the following lemma.
Lemma 4.3. Let γ ∈H
3
2 +β0,q(R/Z, Rn), α ≥2, and β0 ≥β ≥0, p, q ∈(1, ∞) be such that
β0 −1/q > β −1
2p. Then for all τ1, τ2, s1 ∈[0, 1] the function
g(u) :=
1/2
Z
−1/2
Gα
 γ(u + w) −γ(u)
w
! |γ′(u + τ1w) −γ′(u + τ2w)|2
w2
γ′(u + s1w)dw
is in Hβ,p. Furthermore, there is a constant C < ∞depending on ∥γ∥H3/2+β0,q and α, but not on
τ1, τ2, and s1, such that
∥g∥Hβ,p ≤C.
Proof. Note that
∥g∥Hβ,p ≤
1/2
Z
−1/2
∥gw∥Hβ,p
|w|2
dw
where
gw(u) := Gα
 γ(u + w) −γ(u)
w
!
γ′(u + s1w)|γ′(u + τ1w) −γ(u + τ2w)|2.
Choosing some ˜p ∈(p, p + 1) which will be determined later on and letting ˜q := 2 ˜pp
˜p−p leads to
1
p = 1
2 ˜p + 1
2 ˜p + 1
˜q + 1
˜q.
Using that
γ(u + w) −γ(u)
w
=
1
Z
0
γ′(u + τw)dτ,
that γ is bi-Lipschitz, and that Gα is analytic away from the origin, we get according to the
fractional chain rule (Lemma 4.2)

Gα
 γ(· + w) −γ(·)
w
!

Hβ,˜q
≤C∥γ∥Hβ+1,˜q ≤C.
34
Using the fractional Leibniz rule (Lemma 4.1), we derive
∥gw∥Hβ,p ≤C

Gα
 γ(· + w) −γ(·)
w
!

Hβ,˜q
∥γ′∥Hβ,˜q∥γ′(· + τ1w) −γ′(· + τ2w)∥2
Hβ,2 ˜p
≤C

∥γ′(· + τ1w) −γ′(· + τ2w)∥2
L2 ˜p + ∥|D|β+1γ(· + τ1w) −|D|β+1γ(· + τ2w)∥2
L2 ˜p

.
Hence,
∥g∥Hβ,p ≤C
1/2
Z
−1/2
∥γ′(· + τ1w) −γ′(· + τ2w)∥2
L2 ˜p
w2
dw
+ C
1/2
Z
−1/2
∥|D|β+1γ(· + τ1w) −|D|β+1γ(· + τ2w)∥2
L2 ˜p
w2
dw
≤C
1/2
Z
−1/2
∥γ′(·) −γ′(· + (τ2 −τ1)w)∥2
L2 ˜p
w2
dw
+ C
1/2
Z
−1/2
∥|D|β+1γ(·) −|D|β+1γ(· + (τ2 −τ1)w)∥2
L2 ˜p
w2
dw
≤C|τ2 −τ1|
1
Z
−1
∥γ′(·) −γ′(· + w)∥2
L2 ˜p
w2
dw
+ C|τ2 −τ1|
1
Z
−1
∥|D|β+1γ(·) −|D|β+1γ(· + w)∥2
L2 ˜p
w2
dw
≤C∥γ′∥2
B1/2
2 ˜p,2 + C∥|D|β+1γ∥2
B1/2
2 ˜p,2 ≤C
if ˜p ∈(p, p + 1) is chosen so small that
β0 −1
q > β −1
2 ˜p > β −1
2p.
This proves Lemma 4.3.
□
We use the last lemma to prove
Corollary 4.4. Let γ, β0, β,p and q be as in Lemma 4.3 and p′ be such that 1/p + 1/p′ = 1.
Then
35
• for all α ≥2 there is a constant C such that
|T α
s1,s2,τ1,τ2(h)| ≤C∥h∥H1−β,p′
for all s1, s2, τ1, τ2 ∈[0, 1] and h ∈C∞,
• the operator T(γ, ·) = T1(γ, ·) + T2(γ, ·) ∈

H3/2(R/Z, Rn)
∗can be extended to a
bounded operator on H1−β,p′.
Proof. For h ∈C∞(R/Z, Rn) we have
T(γ, h) = −
1
Z
0
1
Z
0
T 2
0,0,t1,t2(h)dt1dt2 +
1
Z
0
1
Z
0
1
Z
0
1
Z
0
T 4
s1,s2,t1,t2(h)ds1ds2dt1dt2
and hence the second part is an immediate consequence of the ﬁrst one.
Let Λs := (id −∆)
s
2 . Using that Λβ is self adjoint, we get
T α
s1,s2,τ1,τ2(h) =
1/2
Z
−1/2
Z
R/Z
Gα
 γ(· + w) −γ(·)
w
! |γ′(u + τ1w) −γ′(u + τ2w)|2
w2
γ′(u + s1w)h′(u + s2w)dudw
=
Z
R/Z
1/2
Z
−1/2

Λβgw

(u)
w2

Λ−βh′
(u + s2w)dwdu
and hence as in the proof of Lemma 4.3
|Ts1,s2,τ1,τ2(h)| ≤C
1/2
Z
−1/2
∥gw∥Hβ,p
w2
dw ∥h∥H1−β,p′ ≤C ∥h∥H1−β,p′
where C < ∞as in Lemma 4.3 does not depend on on s1, s2, τ1,or τ2.
□
Using the two statements above, we are led to the following fact from which Theorem IV
immediately follows.
Lemma 4.5. Let γ ∈H3/2+β0,q(R/Z, Rn), β0 ≥0, q ∈[2, ∞) and β0 −1
q > −1/2 be a stationary
point of the M¨obius energy parametrized by arc length. Then,
• if β0 = 0, we have γ ∈Hs for all s < 3/2 + 2(1/2 −1/q),
• if 0 < β0 < 1/2, we have γ ∈Hs for all s < 3/2 + 2(β0 + 1/2 −1/q),
• if β0 ≥1/2, we have γ ∈H3/2+β0+1/4.
36
Proof. We set
β = 0,
1
p = 2
q + ε,
if β0 = 0,
β = 0,
1
p = 2
q −2β0 + ε,
if 0 < β0 < 1/2,
β = β0 −1/4,
1
p = 2/3,
if β0 ≥1
2
and see that in each case the exponents satisfy the assumptions for the preceding Corollary 4.4
for all small enough ε > 0, so, for p′ with 1
p + 1
p′ = 1, the functional T(γ, ·) = T1(γ, ·)+T2(γ, ·)
can be extended to an operator in

H1−β,p′∗⊂(H3/2−1/p′−β)∗.
From the fact that γ is a stationary point of the M¨obius energy we then deduce that
Q(γ, ·) ∈(H3/2−1/p′−β)∗
and a comparison of the Fourier coeﬃcients gives
γ ∈H3/2+β+ 1
p′ .
Since
3/2 + β + 1
p′ = 5/2 + β −1
p =

3/2 + 2(1/2 −1/q) −ε
if β0 = 0,
3/2 + 2(β0 + 1/2 −1/q) −ε
if 0 < β0 < 1/2,
3/2 + β0 + 1/4
else,
this proves Lemma 4.5.
□
A. Appendix
In this section we gather some facts most of which can already be found in [Sch11] in slightly
diﬀerent versions. The main aim is to prove Lemma 3.1 and 3.2 which both rely on quasi-
locality of the Riesz potential Is. Afterwards, we give an easy proof of the iteration lemma
needed to deduce Dirichlet growth.
We will mainly deal with functions belonging to the Schwartz space S(R) of rapidly decreas-
ing smooth functions R →R. The statements carry over to more general situations by suitable
approximation arguments.
A.1. Quasi-locality
The essential tool apart from Sobolev inequalities is the following quantitative version of the
quasi-locality of the fractional Laplacian and the Riesz potential.
37
Lemma A.1 (Quasi-locality). Let p1, p2, q1, q2 ∈[1, ∞], where we assume that q2 = 1 if
p2 = 1, s ∈(−1, 1) and Ω1, Ω2 be disjoint domains with d := dist(Ω1, Ω2) > 0 and with
positive and ﬁnite Lebesgue measure. Then, for any f ∈S(R),
∥∆
s
2 (fχΩ2)∥(p1,q1),Ω1 ≲d−1−s|Ω1|1/p1|Ω2|1−1/p2∥f∥(p2,q2),Ω2
where we set
∆
s
2 :=

|D|s
if s > 0,
id
if s = 0,
I|s|
if s < 0.
Note, that ∥· ∥(1,q1), ∥· ∥(∞,q∞) are only considered in the inequalities that follow for q1 = 1 and
q∞= ∞.
Proof. For ˜ks(z) =
1
|z|1+s χR\Bd(z) and supp f ⊂Ω2 we have for all x ∈Ω1
∆
s
2 f(x) = cs(˜ks ∗f)(x)
and hence
|∆
s
2 f(x)| ≲∥f∥1,Ω2∥˜ks∥∞≤d−1−s∥f∥1,Ω2.
Hence,
∥∆
s
2 f∥(p1,q1),Ω1 ≤|Ω1|1/p1∥∆
s
2 f∥∞,Ω1 ≤d−1−s|Ω1|1/p1∥f∥1,Ω2
≤d−1−s|Ω1|1/p1|Ω2|1−1/p2∥f∥(p2,q2),Ω2.
□
A quite immediate consequence of this quasi-locality and Sobolev imbeddings is the following
lemma. To state it, let
Ak
Λ,r := B2kΛr −B2k−1Λr.
(A.1)
Lemma A.2. Let p ∈(1, ∞), q, ˜q ∈[1, ∞], s ∈(−1, 1/p) and −1
p∗= s −1
p.
(i) For f ∈S(R) with supp f ⊂Br we have
∥∆−s
2 f∥(p∗,q);R−BΛr ≲Λ−1+ 1
p ∥f∥(p,˜q),Br
uniformly for all Λ > 2.
(ii) If s ∈[0, 1
p), we have for all f ∈S(R)
∥Is f∥(p∗,q);R−BΛr ≲Λ−1+ 1
p ∥f∥(p,˜q);Br + ∥f∥(p,q);R−Br
uniformly for all Λ > 2.
38
(iii) For s ∈[0, 1
p) and any f ∈S(R), we have
∥Is f∥(p∗,q),Br ≲∥f∥(p,q),BΛr + Λ−1
p∗
∞
X
k=1

2−k 1
p∗∥f∥(p,˜q),Ak
Λ,r
uniformly for all Λ > 2.
Proof. For the ﬁrst inequality we use Lemma A.1 and sum up the estimate
∥∆−s
2 f∥(p∗,q),Ak
Λ,r ≲(Λ2k)−1+ 1
p ∥f∥(p,˜q);Br.
In the second case, we use
∥Is f∥(p∗,q),R−BΛr ≤∥Is(χBr f)∥(p∗,q),R−BΛr + ∥Is((1 −χBr)f)∥(p∗,q),R−BΛr
and estimate the ﬁrst term using (i) and the second term using Sobolev’s inequality to get
∥Is f∥(p∗,q),R−BΛr ≲Λ−1+ 1
p ∥f∥(p,˜q),Br + ∥f∥(p,q);R−Br.
To deduce the last inequality, we decompose f = χBΛr f + P∞
k=1 χAk
Λ,r f and estimate using
Sobolev’s inequality
∥Is(χBΛr f)∥(p∗,q),Br ≲∥f∥(p,q),BΛr
and using Lemma A.1
∥Is(χAk
Λ,r f)∥(p∗,q),Br ≲(Λ2k)−1
p∗∥f∥(p,˜q),Ak
Λ,r.
Summing up, this proves the last inequality.
□
Finally, we use the quasi-locality to prove
Proposition A.3. For p ∈(1, ∞), q ∈[1, ∞], s, t ≥0 with 0 < s + t < 1 there is a θ > 0 such
that we have for any f ∈Lp,q(R), Λ > 2, and r > 0
∥|D|s f∥(p,q),Br
≲
sup
ϕ∈C∞
0 (BΛ2r),
∥|D|tϕ∥(p′,q′)≤1
Z
f|D|s+tϕ + r−sΛ−θ ∥f∥(p,q);BΛr + r−sΛ−θ
∞
X
l=1
2−θl∥f∥(p,q),Al
Λ,r.
Proof. Assume that
sup
ϕ∈C∞
0 (BΛ2r),∥|D|tϕ∥(p′,q′)≤1
Z
f|D|s+tϕ ≤K.
39
For g ∈C∞
0 (Br) we consider
Z
R
(|D|s f)gdx =
Z
R
f|D|sgdx =
Z
BΛr
f|D|sgdx +
∞
X
l=1
Z
Al
Λ,r
f|D|sgdx.
For the ﬁrst term we use a smooth partition of unity (ηk)k∈N∪{0} with supp η0 ⊂BΛ2r and
supp ηk ⊂B(Λ22k+1)r −B(Λ22k−1−1)r to get

Z
BΛr
f|D|sgdx

≤

Z
BΛr
f|D|t+s (η0Itg) dx

+
∞
X
l=1

Z
BΛr
f|D|t+s (ηlItg) dx

≲K∥g∥(p′,q′) + ∥f∥(p,q);BΛr
∞
X
l=1
∥|D|t+s (ηlItg) ∥(p′,q′);BΛr.
Since by Lemma A.1 we have
∥|D|t+sηlItg∥(p′,q′);BΛr ≲(Λ22lr)−1−t−s(Λr)1/p′(Λ22lr)1−1/p′∥ηlItg∥(p′,q′)
≤(2l)−t−s−1/p′Λ−(2s+2t+1/p′)r−s−t∥Itg∥(p′,q′)
we can estimate this further by
K∥g∥(p′,q′) + Λ−θ1r−s−t∥f∥(p,q);BΛr∥Itg∥(p′,q′)
for θ1 = 2t + 2s + 1/p′.
Since supp g ⊂Br we get a scaled Poincar´e inequality by applying ﬁrst the Sobolev and then
the H¨older inequality
∥Itg∥(p′,q′) ≲∥g∥(
p′
p′t+1 ,q′),Br ≲rt∥g∥(p′,q′)
and using the quasi-locality (Lemma A.1) once more
∥|D|sg∥(p′,q′),Ak
Λr ≲(2kΛr)−1−sr1−1/p′(2kΛr)1/p′∥g∥(p′,q′) = Λ−θ22−kθ2r−s∥g∥(p′,q′)
for θ2 = 1 + s −1/p′.
Hence,
Z
R
(|D|s f) gdx ≤
K + Λ−θr−s∥f∥(p,q);BΛr + r−sΛ−θ
∞
X
l=1
2−θl∥f∥(p,q);Al
Λ,r
∥g∥(p′,q′),
for θ = min{θ1, θ2} which by duality proves the proposition.
□
40
A.2. Proofs of Lemmata 3.1 and 3.2
The following lemma is the starting point for the estimates of Hs and essentially follows from
the mean value theorem or a ﬁrst-order Taylor expansion.
Lemma A.4. Let δ ∈[0, 1], α ∈(0, 1). Then for almost all x, y, ξ ∈Rn we have

|x −ξ|−1+α −|y −ξ|−1+α

 ≲|x −y|δ 
|y −ξ|−1+α−δ + |x −ξ|−1+α−δχ|x−y|>2|x−ξ|

.
Proof. If |x −y| > 2|x −ξ| we get
|y −ξ| ≥|y −x| −|x −ξ| > |x −ξ|
and hence

|x −ξ|−1+α −|y −ξ|−1+α

 ≲|x −ξ|−1+α ≲|x −y|δ|x −ξ|−1+α−δ.
If |x −y| ≤2|x −ξ| we ﬁrst observe that the above argument leads to

|x −ξ|−1+α −|y −ξ|−1+α

 ≲|x −y|δ|y −ξ|−1+α−δ
if |x −y| > 2|y −ξ|.
To deal with the case that both |x −y| ≤2|x −ξ| and |x −y| ≤2|y −ξ| we observe that then
|y −ξ| ≤|x −ξ| + |x −y| ≤3|x −ξ|.
Hence, we get using the mean value theorem

|x −ξ|−1+α −|y −ξ|−1+α

 ≲|x −y| max
n
|x −ξ|−2+α, |y −ξ|−2+αo
≲|x −y||y −ξ|−2+α ≲|x −y|δ|y −ξ|−1+α−δ.
□
We use the lemma above to derive the following pointwise estimate for H1/2+s.
Lemma A.5 ([Sch11]). For s ∈[0, 1
2) and functions a, b ∈S(R) the following holds for any
ε, ε′ ∈[0, 1
6 −s
3):
|H1/2+s(a, b)| ≲I1/6−s/3(I1/6−s/3−ε||D|1/2−εa| I1/6−s/3−ε′||D|1/2−ε′b|)
+ I1/3−2s/3−ε||D|1/2−εa| I1/6−s/3−ε′||D|1/2−ε′b|
+ I1/6−s/3−ε||D|1/2−εa| I1/3−2s/3−ε′||D|1/2−ε′b|
+ I1/4−s/2−ε||D|1/2−εa| I1/4−s/2−ε′||D|1/2−ε′b|.
41
Proof. In order to shorten notation, we restrict to ε′ = ε; the general case is parallel. We use
the identities a = I 1
2 −ε|D|
1
2 −εa and b = I 1
2 −ε|D|
1
2 −εb. Then,
|H1/2+s(a, b)(x)|
≲
Z Z Z 
|y −z|−1+1/2−ε −|x −z|−1+1/2−ε 
|y −w|−1+1/2−ε −|x −w|−1+1/2−ε
|y −x|1+(1/2+s)
·
·

|D|
1−2ε
2 a(z)

|D|
1−2ε
2 b(w)

 dw dz dy.
Applying Lemma A.4 we get

|y −z|−1+1/2−ε −|x −z|−1+1/2−ε 
|y −w|−1+1/2−ε −|x −w|−1+1/2−ε
|y −x|1+(1/2+s)
≲(|y−w|−1+1/2−ε−δ+|x−w|−1+1/2−ε−δχ|x−y|>2|x−w|)(|y−z|−1+1/2−ε−δ+|x−z|−1+1/2−ε−δχ|x−y|>2|x−z|)
|x −y|1+1/2+s−2δ
≲(|y −w||y −z|)−1+1/2−ε−δ + (|x −w||y −z|)−1+1/2−ε−δ + (|y −w||x −z|)−1+1/2−ε−δ
|x −y|1+1/2+s−2δ
+ (|x −w||x −z|)−1+1/2−ε−δ
|x −y|1+1/2+s−2δ
χ|x−y|>2|x−w| χ|x−y|>2|x−z|.
For δ = 1/3 + s/3 we hence get
|H1/2+s(a, b)| ≲I1/6−s/3(I1/6−s/3−ε||D|
1−2ε
2 a| I1/6−s/3−ε||D|
1−2ε
2 b|)
+ I1/6−s/3−ε||D|
1−2ε
2 a| I1/3−2s/3−ε||D|
1−2ε
2 b|
+ I1/3−2s/3−ε||D|
1−2ε
2 a| I1/6−s/3−ε||D|
1−2ε
2 b| + A
where
A ≲
Z Z Z (|x −w||x −z|)−1+1/2−ε−δ
|x −y|1+1/2+s−2δ
χ|x−y|>2|x−w| χ|x−y|>2|x−z| dy
!
||D|
1−2ε
2 a(z)| ||D|
1−2ε
2 b(w)| dw dz
≲
Z Z
|x −w|−1+1/4−ε−s/2|x −z|−1+1/4−ε−s/2||D|
1−2ε
2 a(z)| ||D|
1−2ε
2 b(w)| dw dz
≲I1/4−s/2−ε||D|
1−2ε
2 a| I1/4−s/2−ε||D|
1−2ε
2 b|.
□
To estimate this further, we will use the following fact about lower order products which we
get using the quasi-locality.
Lemma A.6 (Lower order products). Let for s > 0, 0 ≤s1, s2, s3 ≤1/2, s1 + s2 + s3 = s,
and at least two of these si, i = 1, 2, 3, non-zero. Let p ∈(1, ∞), p2 ∈(1, 1
s2 ), p3 ∈(1, 1
s3 ) and
such that
1
p = 1
p2
+ 1
p3
−s.
42
Assume moreover that
|G(u, v)| ≲Is1
 Is2|u| Is3|v| ,
then there is some θ > 0 such that we have for any Λ > 4, and 1
q = 1
q1 + 1
q2 ,
∥G(u, v)∥(p,q),Br
(A.2)
≲∥u∥(p2,q1),BΛr∥v∥(p3,q2),BΛr + ∥u∥(p2,q1)Λ−θ
∞
X
k=2
2−θk∥v∥(p3,q2),BΛ2kr.
If supp |D|tv ⊂Br for some t ∈[0, 1
2], we furthermore get for any k ≥2, Λ > 16,
∥G(u, v)∥(p,q),Ak
Λ,r ≲Λ−θ2−θk∥u∥(p2,∞),R ∥v∥(p3,1),R.
(A.3)
Proof. Let
1
p∗
2
:= 1
p2
−s2,
1
p∗
3
:= 1
p3
−s3,
1
p1
:= 1
p∗
2
+ 1
p∗
3
= 1
p2
+ 1
p3
−s2 −s3,
and
1
p∗
1
:= 1
p ≡1
p2
+ 1
p3
−s = 1
p1
−s1.
Then by Lemma A.2 (iii), for Λ ˆ=
√
Λ, p∗ˆ=p∗
1 = p, p ˆ=p1, s ˆ=s1
∥G(u, v)∥(p∗
1,q),Br ≲∥Is2|u| Is3|v|∥(p1,q),BΛ1/2r + Λ−1/2p
∞
X
k=1
2−k/p∥Is2|u| Is3|v|∥(p1,q),BΛ1/22kr
≲∥Is2|u|∥(p∗
2,q1),BΛ1/2r ∥Is3|v|∥(p∗
3,q2),BΛ1/2r + Λ−1/2p
∞
X
k=1
2−k/p∥Is2|u|∥(p∗
2,q1),B2kΛ1/2r ∥Is3|v|∥(p∗
3,q2),B2kΛ1/2r.
Applying yet again Lemma A.2 (iii) to both factors in each sum with Λ ˆ=
√
Λ we arrive at
∥G(u, v)∥(p,q),Br ≲∥u∥(p2,q1),BΛr∥v∥(p3,q2),BΛr + ∥u∥(p2,q1)Λ−θ
∞
X
k=2
2−θk∥v∥(p3,q2),BΛ2kr.
As for the second estimate, we apply Lemma A.2 (ii) with Λ ˆ=
√
Λ to get
∥G(u, v)∥(p,q),R−BΛr = ∥Is1
 Is2|u| Is3|v| ∥(p∗
1,q),R−BΛr
43
≲Λ−θ1∥Is2|u| Is3|v|∥(p1,∞),BΛ1/2r + ∥Is2|u| Is3|v|∥(p1,q),R−BΛ1/2r
where θ1 = 1
2 −
1
2p1 . We estimate the ﬁrst term using H¨older’s inequality and Sobolev imbed-
ding theorem to get
Λ−θ1∥Is2|u| Is3|v|∥(p1,∞),BΛ1/2r ≤Λ−θ1∥u∥(p2,∞)∥v∥(p3,1).
For the second term we use H¨older’s inequality and Sobolev’s imbedding theorem to get
∥Is2|u| Is3|v|∥(p1,q),R−BΛ1/2r ≲∥Is2|u|∥(p∗
2,q1),R−BΛ1/2r∥Is3|v|∥(p∗
3,q2),R−BΛ1/2r
≲∥u∥(p2,∞),R∥Is3|v|∥(p∗
3,q2),R−BΛ1/2r.
Since
∥Is3|v|∥(p∗
3,q2),R−BΛ1/2r ≲Λ−θ2∥v∥(p3,1);BΛ1/4 + ∥v∥(p3,q);R−BΛ1/4
where θ2 = 1
4 −
1
4p3 and, using Lemma A.2 (i)
∥v∥(p3,q);R−BΛ1/4 = ∥|D|t(Itv)∥(p3,q);R−BΛ1/4 ≤Λ−θ2∥Itv∥(p∗∗
3 ,1) ≤Λ−θ2∥Itv∥(p3,1)
we deduce the statement for θ := min{θ1, θ2}.
□
We then have the following
Lemma A.7. There is a ε0 > 0 such that for δ, ε ∈[0, ε0), for any a, b ∈S(R), Λ > 4
∥H 1
2 (a, b)∥(2,q),Br ≲∥|D|1/2−δa∥(
2
1−2δ ,q1),BΛr∥|D|1/2−εb∥(
2
1−2ε ,q2),BΛr+
+ ∥|D|1/2−δa∥(
2
1−2δ ,q1)Λ−θ
∞
X
k=1
2−θ(k−1)∥|D|1/2−εb∥(
2
1−2ε ,q2),B2kΛr.
If supp b ⊂Br we furthermore get for any k ≥2, Λ > 16, s ∈[0, 1
2)
∥H 1
2 (a, b)∥(
2
1+2s ,q),Ak
Λ,r ≲(Λ2k)−θ∥|D|
1
2 a∥(2,∞),R ∥|D|1/2−εb∥(
2
1−2ε ,1),R.
Proof. Immediately from Lemma A.5, Lemma A.6 where s = 1
2 −ε −δ.
□
We use the lemma above to estimate the normal part as stated in Lemma 3.1.
Proof of Lemma 3.1. With (3.10) we obtain

|D|s|g′|2

(
2
1+2s ,∞),Br ≲r
1
2 +s. In order to show (3.11)
by the decomposition (3.8) it remains to treat the H-term. We rewrite
|D|sH 1
2 (a, b)
=
Hs+ 1
2 (a, b)
|      {z      }
=:I
+ a|D|
1+2s
2 b −|D|s(a|D|
1
2 b)
|                        {z                        }
=:II
+ b|D|
1+2s
2 a −|D|s(b|D|
1
2 a)
|                        {z                        }
=:III
.
44
We will show that all three terms satisfy the hypotheses of Lemma A.6. Due to Lemma A.5
this is true for the term I.
As for II note that II = 0 in case s = 0. If s ∈(0, 1), the potential deﬁnition (3.2) of |D|s gives
II(x) = c
a(x)
Z |D|
1
2 b(y) −|D|
1
2 b(x)
|x −y|1+s
dy −
Z a(y)|D|
1
2 b(y) −a(x)|D|
1
2 b(x)
|x −y|1+s
dy

= c
Z (a(x) −a(y))|D|
1
2 b(y)
|x −y|1+s
dy.
Using a = I 1
2 |D|
1
2 a we arrive at
|II(x)| ≲
Z |a(y) −a(x)|

|D|
1
2 b(y)

|x −y|1+s
dy ≲
Z Z 

|y −z|−1+ 1
2 −|x −z|−1+ 1
2

|D|
1
2 b(y)

|D|
1
2 a(z)

|x −y|1+s
dy dz.
For almost all x, y, z we get from Lemma A.4 choosing δ := 1
4 + s
2

|y −z|−1+ 1
2 −|x −z|−1+ 1
2

|x −y|1+s
≤(|x −z||x −y|)−1+ 1
4 −s
2 + (|y −z||x −y|)−1+ 1
4 −s
2 ,
which implies, using again (3.2)
|II(x)| ≲I 1−2s
4

|D|
1
2 a

 I 1−2s
4

|D|
1
2 b

 + I 1−2s
4


|D|
1
2 b

 I 1−2s
4

|D|
1
2 a


.
By symmetry a respective estimate holds also for the term III. Applying Lemma A.6 one
concludes.
□
Proof of Lemma 3.2. Again the proof relies on quasi-locality. First we decompose

Z
|D|
1
2 g′
iωi jH1/2(g′
j, φ)

 ≲

Z
BΛ1/2r
|D|
1
2 g′
iωi jH1/2(g′
j, φ)

+
∞
X
k=1

Z
Ak
Λ1/2,r
|D|
1
2 g′
iωi jH1/2(g′
j, φ)

≲∥|D|
1
2 g′∥(2,∞),BΛ1/2r∥H1/2(g′
j, φ)∥(2,1),BΛ1/2r
+
∞
X
k=1
∥|D|
1
2 g′∥(2,∞),Ak
Λ1/2,r∥H1/2(g′
j, φ)∥(2,1),Ak
Λ1/2,r.
Using Lemma A.7, the ﬁrst summand can be estimated by
∥Is|D|
1
2 φ∥(
2
1−2s ,1)
∥|D|
1
2 g′∥2
(2,∞),BΛr + ∥|D|
1
2 g′∥(2,∞),BΛr Λ−θ
∞
X
l=1
2−θl∥|D|
1
2 g′∥(2,∞),BΛ2lr
.
45
Applying the second part of Lemma A.7, the inﬁnite sum can be estimated by
Λ−θ∥Is|D|
1
2 φ∥(
2
1−2s ,1) ∥|D|
1
2 g′∥(2,∞)
∞
X
k=2
2−θk∥|D|
1
2 g′∥(2,∞),B2kΛr.
□
A.3. Iteration lemma
In order to prove Dirichlet growth, we need an iteration lemma whose proof is based on the
technique presented in [Tao01, notes4, p. 11]. The statement is also similar to the correspond-
ing one appearing in [DLR11a]. One should see this as a generalized version of De Giorgi’s
Iteration Lemma, cf., e.g., [Gia83].
Lemma A.8 (Iteration lemma). Let C < ∞and θ > 0 be given.
If bk ≥0, k ∈N0, satisfy
bk+m ≤εbk + C
2−θ(k+m) + 2−θm
k
X
l=1
2−θlbk−l

(A.4)
for all k ∈N0 and ε > 0 is small enough, m is big enough, then
bk ≲2−˜θk
for all k ∈N0 with ˜θ = θ/2.
Proof. We will prove that
∞
X
k=0
2˜θkbk ≤C
m
X
l=0
2˜θlbl + C.
(A.5)
Especially, the inﬁnite sum converges and hence the summands are a null series, which proves
the lemma.
Multiplying Equation (A.4) with 2˜θk, and summing over k we get
2−˜θm
∞
X
k=0
2˜θ(k+m)bk+m ≤ε
∞
X
k=0
2˜θkbk + C
∞
X
k=0
2−θ(k+m)2˜θk + C2−θm
∞
X
k=0
k
X
l=1
2−θl2˜θkbk−l
≤ε
∞
X
k=0
2˜θkbk + C2−θm
∞
X
k′=0
∞
X
l=1
2−θl2˜θ(k′+l)bk′ + C2−θm
≤ε
∞
X
k=0
2˜θkbk + ˜C2−θm
∞
X
k′=0
2˜θk′bk′ + C2−θm.
46
Assuming that m is so large that ˜C2−m(θ−˜θ) = ˜C2−mθ
2 < 1/4 and 0 < ε < 1
42−θm we get
∞
X
k=0
2˜θkbk ≤1
2
∞
X
k=0
2˜θkbk +
m
X
l=0
2˜θlbl + C
and hence
∞
X
k=0
2˜θkbk ≤C
m
X
l=0
2˜θlbl + C
if the inﬁnite series converges. If the sum is not known to converge, we apply the above
argument to the cut-oﬀseries

˜bk = bk
if k ≤N,
˜bk = 0
else
and get the uniform bound PN
k=0 2˜θkbk ≲Pm
l=0 2˜θlbl + 1. Letting N →∞we get (A.5).
□
References
[Ada75]
D. R. Adams. A note on Riesz potentials. Duke Math. J., 42(4):765–778, 1975.
[Bla11a]
S. Blatt. The energy spaces of the tangent-point energies. Preprint, 2011.
[Bla11b]
S. Blatt. The gradient ﬂow of the M¨obius energy near local minimizers. Cal-
culus of Variations and Partial Diﬀerential Equations, pages 1–37, 2011. DOI:
10.1007/s00526-011-0416-9.
[Bla12]
S. Blatt. Boundedness and regularizing eﬀects of O’Hara’s knot energies. J. Knot
Theory Ramif., 21(1), 2012.
[BR12]
S. Blatt and Ph. Reiter. Stationary Points of O’Hara’s Knot Energies. Manuscripta
mathematica, 2012.
[CM78]
R. R. Coifman and Y. Meyer. Au del`a des op´erateurs pseudo-diﬀ´erentiels, vol-
ume 57 of Ast´erisque. Soci´et´e Math´ematique de France, Paris, 1978.
[DL11]
F. Da Lio. Fractional Harmonic Maps into Manifolds in odd dimension n > 1.
Preprint, arXiv:1012.2741v1, 2011.
[DLR11a] F. Da Lio and T. Rivi`ere. 3-Commutators Estimates and the Regularity of 1/2-
Harmonic Maps into Spheres. APDE, 4(1):149–190, 2011.
[DLR11b] F. Da Lio and T. Rivi`ere. Sub-criticality of non-local Schr¨odinger systems with
antisymmetric potentials and applications to half-harmonic maps. Advances in
Mathematics, 227:1300–1348, 2011.
[DLS12]
F. Da Lio and A. Schikorra. n/p-Harmonic maps: regularity for the sphere case.
Preprint, arXiv:1202.1151v1.
47
[DNPV11] E. Di Nezza, G. Palatucci, E. Valdinoci.
Hitchhiker’s guide to the fractional
Sobolev spaces. Preprint, arXiv:1104.4345v3. Bull. Sci. Math., DOI: 10.1016/
j.bulsci.2011.12.004, 2011.
[FHW94]
M. H. Freedman, Z.-X. He, and Z. Wang. M¨obius energy of knots and unknots.
Ann. of Math. (2), 139(1):1–50, 1994.
[Gia83]
M. Giaquinta. Multiple integrals in the calculus of variations and nonlinear ellip-
tic systems, volume 105 of Annals of Mathematics Studies. Princeton University
Press, Princeton, NJ, 1983.
[Gra08]
L. Grafakos. Classical Fourier analysis, volume 249 of Graduate Texts in Math-
ematics. Springer, New York, second edition, 2008.
[Gra09]
L. Grafakos. Modern Fourier analysis, volume 250 of Graduate Texts in Mathe-
matics. Springer, New York, second edition, 2009.
[He99]
Z.-X. He. A formula for the non-integer powers of the Laplacian. Acta Math. Sin.
(Engl. Ser.), 15(1):21–24, 1999.
[He00]
Z.-X. He. The Euler-Lagrange equation and heat ﬂow for the M¨obius energy.
Comm. Pure Appl. Math., 53(4):399–431, 2000.
[H´el91]
F. H´elein. R´egularit´e des applications faiblement harmoniques entre une surface
et une vari´et´e riemannienne. C. R. Acad. Sci. Paris S´er. I Math., 312(8):591–596,
1991.
[Hun66]
R. Hunt. On L(p, q) Spaces. L’Enseignement Math´ematique, 12:249–276, 1966.
[KS97]
R. B. Kusner and J. M. Sullivan. M¨obius energies for knots and links, surfaces and
submanifolds. In Geometric topology (Athens, GA, 1993), volume 2 of AMS/IP
Stud. Adv. Math., pages 570–604. Amer. Math. Soc., Providence, RI, 1997.
[O’H91]
J. O’Hara. Energy of a knot. Topology, 30(2):241–247, 1991.
[O’H94]
J. O’Hara. Energy functionals of knots. II. Topology Appl., 56(1):45–61, 1994.
[Riv07]
T. Rivi`ere.
Conservation laws for conformally invariant variational problems.
Invent. Math., 168(1):1–22, 2007.
[Riv08]
T. Rivi`ere. Analysis aspects of Willmore surfaces. Invent. Math., 174(1):1–45,
2008.
[RS96]
T. Runst and W. Sickel. Sobolev spaces of fractional order, Nemytskij operators,
and nonlinear partial diﬀerential equations, volume 3 of de Gruyter Series in
Nonlinear Analysis and Applications. Walter de Gruyter & Co., Berlin, 1996.
[Rt10]
Ph. Reiter. Regularity theory for the M¨obius energy. Commun. Pure Appl. Anal.,
9(5):1463–1471, 2010.
[Rt12]
Ph. Reiter. Repulsive knot energies and pseudodiﬀerential calculus for O’Hara’s
knot energy family E(α). Mathematische Nachrichten, 2012.
48
[Sch10]
A. Schikorra.
Regularity of n/2-harmonic maps into spheres.
PhD-Thesis,
arXiv:1003.0646v2, 2010.
[Sch11]
A. Schikorra. Interior and Boundary-Regularity of Fractional Harmonic Maps on
Domains. Preprint, arXiv:1103.5203, 2011.
[Sch12]
A. Schikorra. Regularity of n/2-harmonic maps into spheres. J. Diﬀerential Equa-
tions, 252:1862–1911, 2012.
[Sim93]
L. Simon. Existence of surfaces minimizing the Willmore functional. Comm.
Anal. Geom., 1(2):281–326, 1993.
[Tar07]
L. Tartar. An introduction to Sobolev spaces and interpolation spaces, volume 3
of Lecture Notes of the Unione Matematica Italiana. Springer, Berlin, 2007.
[Tao01]
T.
Tao.
Harmonic
analysis
in
the
phase
plane.
Lecture
notes,
http://www.math.ucla.edu/˜tao/254a.1.01w, 2001.
[Tri83]
H. Triebel. Theory of function spaces, volume 78 of Monographs in Mathematics.
Birkh¨auser Verlag, Basel, 1983.
49
