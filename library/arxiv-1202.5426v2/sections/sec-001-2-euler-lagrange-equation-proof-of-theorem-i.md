---
doc_id: arxiv-1202.5426v2
doc_title: "Hard analysis meets critical knots Stationary points of the M öbius energy are smooth S. Blatt∗ Φ. Reiter∗∗ A. Schikorra∗∗∗"
section_id: sec-001-2-euler-lagrange-equation-proof-of-theorem-i
section_title: "Euler-Lagrange equation: Proof of Theorem I"
section_number: 2
pages: 5-16
source_pdf: 1202.5426v2.pdf
source_sha256: 6c7668ad72e33b4b
doc_brief: "Hard analysis meets critical knots Stationary points of the M öbius energy are smooth S. Blatt∗ Φ. Reiter∗∗ A. Schikorra∗∗∗ — 5 sections: Front matter; Introduction; Euler-Lagrange equation: Proof of"
---
This section is devoted to the proof of Theorem I which especially involves the derivation of
a formula for the ﬁrst variation.
By H3/ 2
ir we will denote the set of injective and regular curves in H3/ 2. The set H1,∞
ir is deﬁned
accordingly. First we will need the following lemma, to guarantee that E(2) is well deﬁned on
a suﬃciently small H3/ 2∩ H1,∞ neighborhood of the curveγ:
Lemma 2.1 (H3/2
ir ∩H1,∞ is open in H3/2∩H1,∞). For anyγ∈ H3/ 2
ir (R/ Z, Rn)∩H1,∞(R/ Z, Rn)
there is someτ0 =τ0(γ)> 0 with
Y :=
{
γ+ϕ
⏐⏐⏐ϕ∈ H1,∞(R/ Z, Rn),
‖‖‖ϕ′‖‖‖L∞≤τ0
}
⊂ H1,∞
ir . (2.1)
Moreover, there is a constant c= c(γ)> 0 with
min{|˜γ(u +w)− ˜γ(u)|, d˜γ(u +w, u)}≥ c|w|, |˜γ′(u)|≥ c (2.2)
5
for all ˜γ∈ Y and (u,w )∈ U0.
Proof. We ﬁrst show thatγis bi-Lipschitz. To this end, chooseδ∈ (0, 1
2) with

∫
Br(z)
∫
Br(0)
|γ′(u +w)−γ′(u)|2
|w|2 dw du

1/ 2
≤ 1
2
for all z∈ R/ Z and all r∈ [0,δ] which gives
1
2r
∫
Br(z)
⏐⏐⏐⏐⏐γ′(x)− 1
2r
∫
Br(z)
γ′(y) dy
⏐⏐⏐⏐⏐dx
≤ 1
4r2
∫
Br(z)
∫
Br(z)
|γ′(x)−γ′(y)| dx dy
≤

1
4r2
∫
Br(z)
∫
Br(z)
|γ′(x)−γ′(y)|2 dx dy

1/ 2
≤

∫
Br(z)
∫
Br(z)
|γ′(x)−γ′(y)|2
|x−y|2 dx dy

1/ 2
≤ 1
2.
Since
⏐⏐⏐⏐1
2r
∫
Br(z)γ′(y) dy
⏐⏐⏐⏐≤ 1 we deduce that
inf
a∈Rn
|a|≤1
1
2r
∫
Br(z)
⏐⏐⏐γ′(y)− a
⏐⏐⏐dy≤ 1
2.
For x,y ∈ R/ Z with|x−y|≤ 2δlet r := 1
2|x−y| and z∈ R/ Z be the midpoint of the shorter
arc between x andy. Then
|γ(x)−γ(y)| = sup
a∈Rn
|a|≤1
∫
Br(z)
⟨γ′(t), a⟩dt
= sup
a∈Rn
|a|≤1
∫
Br(z)
⟨γ′(t),γ′(t) + (a−γ′(t))⟩dt
≥
1− inf
a∈Rn
|a|≤1
1
2r
∫
Br(z)
|γ′(t)− a| dt
|x−y|
6
≥ 1
2|x−y|
for all x,y ∈ R/ Z with|x−y|≤ 2δ. Sinceγis embedded and
(x,y )↦→|γ(y)−γ(x)|
|y− x|
deﬁnes a continuous positive function on Iδ:={(x,y )∈ (R/ Z)2 :|x−y|≥ 2δ}, we furthermore
have
|γ(x)−γ(y)|≥ min
( ˜x, ˜y)∈Iδ
|γ(˜y)−γ( ˜x)|
|˜y− ˜x|/bracehtipupleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipdownright/bracehtipdownleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipupright
>0
|x−y|.
for all (x,y )∈ Iδ. Hence, there is a c0 = c0(γ)> 0 with
|γ(x)−γ(x +w)|≥ c0|w|
for allw∈ [−1/ 2, 1/ 2]. Lessening c0 if necessary, we can also achieve by regularity
⏐⏐⏐γ′⏐⏐⏐≥ c0 on R/ Z.
Lettingτ0 := 1
2c0 we obtain for arbitrary ˜γ∈ Y
|˜γ(u +w)− ˜γ(u)|≥| γ(u +w)−γ(u)|−| (˜γ−γ)(u +w)− (˜γ−γ)(u)|
≥ c0|w|−
‖‖‖γ′− ˜γ′‖‖‖L∞|w|
≥ 1
2c0|w|
and ⏐⏐⏐˜γ′⏐⏐⏐≥
⏐⏐⏐γ′⏐⏐⏐−
⏐⏐⏐˜γ′−γ′⏐⏐⏐≥ c0−
‖‖‖γ′− ˜γ′‖‖‖L∞≥ 1
2c0.
From the latter estimate we deduce by (1.1) for u∈ R/ Z,w∈ [− 1
2, 1
2]
d˜γ(u +w, u)≥ d˜γ(u±w, u)≥ 1
2c0|w|.
We have established (2.2) which gives (2.1). □
We will use the last lemma to prove the following theorem, from which Theorem I will follow
quite easily.
7
Proposition 2.2. The energy E (2) is continuously di ﬀerentiable on
(
H3/ 2
ir ∩ H1,∞
)
(R/ Z, Rn).
The derivative of E(2) atγ∈ H3/ 2
ir ∩ H1,∞ in directionϕ∈ H3/ 2
ir ∩ H1,∞ exists and is given by
δE(2)(γ;ϕ) =
2 lim
εց0
/iintegdisplay
Uε
{( 1
|γ(u +w)−γ(u)|2− 1
dγ(u +w, u)2
)⟨γ′(u)
|γ′(u)|2,ϕ′(u)
⟩
−

⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4 −
d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u)
dγ(u +w, u)3

}
|γ′(u +w)||γ′(u)| dw du.
(2.3)
Asγis absolutely continuous and regular, the derivative d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u) is well-deﬁned
for almost all (u,w )∈ U0. From (1.1) we deduce
d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u) =

|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|,ϕ′(u +σw)
⟩
dσ if L (γ|[u, u+w])< 1
2 L (γ),
−|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|,ϕ′(u +σw)
⟩
dσ if L (γ|[u, u+w])> 1
2 L (γ).
(2.4)
To prove Proposition 2.2, we will ﬁrst show that the following approximations of the e nergy
E(2), in which we cut o ﬀthe singular part, are continuously di ﬀerentiable and provide a for-
mula for the ﬁrst variation. For ε∈ (0, 1
2) we set
E(2)
ε (γ) :=
/iintegdisplay
Uε
( 1
|γ(u +w)−γ(u)|2− 1
dγ(u +w, u)2
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du.
Lemma 2.3. Forε∈ (0, 1
2) the functional E (2)
ε is continuously diﬀerentiable on the space of
all injective regular curves in H 3/ 2(R/ Z, Rn)∩ H1,∞(R/ Z, Rn). The directional derivative at
γ∈ H3/ 2
ir (R/ Z, Rn)∩ H1,∞(R/ Z, Rn) in directionϕ∈ H3/ 2(R/ Z, Rn)∩ H1,∞(R/ Z, Rn) is given
by
δE(2)
ε (γ;ϕ) =
2
/iintegdisplay
Uε
{( 1
|γ(u +w)−γ(u)|2− 1
dγ(u +w, u)2
)⟨γ′(u)
|γ′(u)|2,ϕ′(u)
⟩
−

⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4 −
d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u)
dγ(u +w, u)3

}
|γ′(u +w)||γ′(u)| dw du.
(2.5)
8
Proof. Applying Lemma 2.1, we obtain an H3/ 2∩ H1,∞-neighborhood Y ⊂ H3/ 2
ir ∩ H1,∞ of
γsuch that ( 2.2) uniformly holds on Y for any element in Uε. The integrand in ( 2.5) is
almost everywhere the pointwise derivative of the integran d in E(2)
ε . Using ( 1.1) and ( 2.4),
one sees furthermore that this pointwise derivative is majo rized by some L1-function. So,
Lebesgue’s Theorem permits to interchange diﬀerentiation and integration which, by a suitable
reparametrization, results in (2.5).
As for continuity of E(2)
ε andδE(2)
ε the only diﬃculty is to treat the intrinsic distance. Recalling
the continuity of the length functional with respect to abso lutely continuous curves we can
directly read o ﬀfrom (1.1) that the integrand of E(2)
ε deﬁnes a continuous operator ( H3/ 2
ir ∩
H1,∞)(R/ Z, Rn)→ L1(Uε).
Since γis regular, for any u ∈ R/ Z there are at most two points w ∈ [− 1
2, 1
2] satisfying
L (γ|[u, u+w]) = 1
2 L (γ) which results in a null set in U0. Additionally using ( 2.4), we see
that the integrand of δE(2)
ε gives rise to a continuous mapping ( H3/ 2
ir ∩ H1,∞)(R/ Z, Rn)×
H1,∞(R/ Z, Rn) → L1(Uε). Being linear and bounded in the second component, it can be
viewed as a continuous mapping from H1,∞ into the linear bounded operators H3/ 2
ir ∩ H1,∞→
L1(Uε).
Altogether, the integrand of E(2)
ε is a continuously di ﬀerentiable functional H3/ 2
ir ∩ H1,∞→
L1(Uε). The statement now follows from the chain rule and the fact t hat the integration oper-
ator
L1(Uε)→ R, g ↦→
/iintegdisplay
Uε
g(u,w ) du dw,
is continuously diﬀerentiable as it is a bounded linear operator. □
Due to the fact that bounded L1-sequences are not uniformly integrable, the approximatio ns
E(2)
ε do not even form a Cauchy sequence inC0(H3/ 2
ir ∩H1,∞). In order to prove Proposition2.2,
we state in Lemma 2.4 below that E(2)
ε is nearly a Cauchy sequence in C1(Xδ) for subsets
Xδ⊂ H3/ 2
ir ∩ H1,∞,δ≥ 0, which satisfy the following substitute of the uniform int egrability
property
lim sup
ε→0
sup
γ∈Xδ
(/iintegdisplay
R/ Z×[−ε,ε]
|γ′(u +w)−γ′(u)|2
w2 dw du
)1/ 2
≤δ. (2.6)
The statement involves the Lipschitz constant
lipY E = sup
f, ˜f∈Y
f /nequal˜f
⏐⏐⏐E( f )− E( ˜f )
⏐⏐⏐
‖‖‖f− ˜f
‖‖‖
for some real-valued functional E and a subset Y contained in its domain.
Lemma 2.4. We have
E(2)
ε (γ)→ E(2)(γ)
9
for allγ∈ H3/ 2
ir ∩ H1,∞.
Furthermore, for anyγ0∈ H3/ 2
ir ∩ H1,∞ there is an open subset Y⊂ H3/ 2
ir ∩ H1,∞ and a constant
C = C(γ0)<∞ such that
lim sup
ε1,ε2→0
lipXδ∩Y(E(2)
ε1 − E(2)
ε2 )≤ Cδ (2.7)
for all subsets Xδ⊂ H3/ 2∩ H1,∞ satisfying (2.6) withδ∈ [0, 1].
Proof. From Lemma 2.1 we get a H3/ 2∩ H1,∞-neighborhood Y⊂ H3/ 2
ir ∩ H1,∞ ofγsuch that
(2.2) holds for allγ∈ Y. Making Y smaller if necessary, we may also assume the existence of
anε0 > 0 with
dγ(u +w, u) = L (γ|[u, u+w])
for allγ∈ Y andw∈ [−ε0,ε0].
In order to bring the integrand in the deﬁnition of E(2) and E(2)
ε in a more convenient form we
introduce the function
g(ζ,η,ϑ,ι) := ζ−2−η−2
η2−ζ2 ϑι
which is Lipschitz continuous and positive on [˜c,∞)4 for any ˜c > 0. We deﬁne for u∈ R/ Z,
w∈ [−ε0,ε0]
Gγ: (u,w )↦→g

⏐⏐⏐⏐⏐⏐⏐⏐⏐
1∫
0
γ′(u +θ1w) dθ1
⏐⏐⏐⏐⏐⏐⏐⏐⏐
,
1∫
0
⏐⏐⏐γ′(u +θ2w)
⏐⏐⏐dθ2,
⏐⏐⏐γ′(u +w)
⏐⏐⏐,
⏐⏐⏐γ′(u)
⏐⏐⏐
.
We have chosen Y in such a way that the arguments in G are uniformly bounded away from
zero. Then we decompose the integrand in the deﬁnition of E(2) for|w|≤ ε0 into
( 1
|γ(u +w)−γ(u)|2− 1
dγ(u +w, u)2
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐
= 1
w2

1⏐⏐⏐⏐
∫1
0 γ′(u +θ1w) dθ1
⏐⏐⏐⏐
2− 1
(∫1
0|γ′(u +θ2w)| dθ2
)2

⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐
=Gγ(u,w )
(∫1
0|γ′(u +θ2w)| dθ2
)2
−
⏐⏐⏐⏐
∫1
0 γ′(u +θ1w) dθ1
⏐⏐⏐⏐
2
|w|2
=Gγ(u,w )
/iintegtext
[0, 1]2 (|γ′(u +θ1w)||γ′(u +θ2w)|−⟨γ′(u +θ1w),γ′(u +θ2w)⟩) dθ1 dθ2
|w|2 .
10
Using 2|a||b|− 2⟨a, b⟩=|a− b|2−|| a|−| b||2 for a, b∈ Rn this can be written as
1
2Gγ(u,w )
/iintegtext
[0, 1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
w2
− 1
2Gγ(u,w )
/iintegtext
[0, 1]2 (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2 dθ1 dθ2
w2 .
We ﬁrst use this to get
E(2)(γ)− E(2)
ε (γ)≤ C
∫
R/ Z
ε∫
−ε
Gγ(u,w )
/iintegtext
[0, 1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
w2 dwdu
≤ C
∫
R/ Z
ε∫
−ε
/iintegtext
[0, 1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
w2 dwdu
ε→0
−−−→0
which proves the pointwise convergence stated in the lemma.
Let now 0<ε1 <ε2 <ε0 and set
F := E(2)
ε1 − E(2)
ε2.
Using the decomposition of the integrand above, we get
F(γ) = 1
2
∫
R/ Z
∫
ε1<|w|<ε2
Gγ(u,w )
/iintegtext
[0, 1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
w2 dw du
− 1
2
∫
R/ Z
∫
ε1<|w|<ε2
Gγ(u,w )
/iintegtext
[0, 1]2 (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2 dθ1 dθ2
w2 dw du
=: 1
2 F(2)
1 (γ)− 1
2 F(2)
2 (γ).
To estimate the diﬀerence F(˜γ)− F(γ) forγ,˜γ∈ Y0, we ﬁrst consider
⏐⏐⏐G˜γ(u,w )−Gγ(u,w )
⏐⏐⏐
≤ C
⏐⏐⏐⏐⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1∫
0
˜γ′(u +θ1w) dθ1
⏐⏐⏐⏐⏐⏐⏐⏐⏐
−
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1∫
0
γ′(u +θ2w) dθ2
⏐⏐⏐⏐⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐⏐⏐⏐
+ C
⏐⏐⏐⏐⏐⏐⏐⏐⏐
1∫
0
(⏐⏐⏐˜γ′(u +θw)
⏐⏐⏐−
⏐⏐⏐γ′(u +θw)
⏐⏐⏐
)
dθ
⏐⏐⏐⏐⏐⏐⏐⏐⏐
+ C
⏐⏐⏐
⏐⏐⏐˜γ′(u +w)
⏐⏐⏐−
⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐+ C
⏐⏐⏐
⏐⏐⏐˜γ′(u)
⏐⏐⏐−
⏐⏐⏐γ′(u)
⏐⏐⏐
⏐⏐⏐
11
≤ C
1∫
0
⏐⏐⏐˜γ′(u +θw)−γ′(u +θw)
⏐⏐⏐dθ+ C
⏐⏐⏐˜γ′(u +w)−γ′(u +w)
⏐⏐⏐+ C
⏐⏐⏐˜γ′(u)−γ′(u)
⏐⏐⏐
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞.
We arrive at
⏐⏐⏐F(2)
1 (˜γ)− F(2)
1 (γ)
⏐⏐⏐
≤
/iintegdisplay
R/ Z×[−ε2,ε2]
⏐⏐⏐G˜γ(u,w )−Gγ(u,w )
⏐⏐⏐
/iintegtext
[0, 1]2|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2 dθ1 dθ2
w2 dw du
+
/iintegdisplay
R/ Z×[−ε2,ε2]
⏐⏐⏐Gγ(u,w )
⏐⏐⏐
/iintegtext
[0, 1]2
⏐⏐⏐|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2−|γ′(u +θ1w)−γ′(u +θ2w)|2⏐⏐⏐dθ1 dθ2
w2
dw du
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
/iintegdisplay
[0, 1]2
/iintegdisplay
R/ Z×[−ε2,ε2]
|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2
w2 dw du dθ1 dθ2
+ C
‖‖‖γ′‖‖‖L∞
/iintegdisplay
[0, 1]2
/iintegdisplay
R/ Z×[−ε2,ε2]
|(˜γ′ +γ′)(u +θ1w)− (˜γ′ +γ′)(u +θ2w)||(˜γ′−γ′)(u +θ1w)− (˜γ′−γ′)(u +θ2w)|
w2
dw du dθ1 dθ2
≤ C [ ˜γ′] 2
H1/ 2
2ε2
‖‖‖˜γ′−γ′‖‖‖L∞ + C
‖‖‖γ′‖‖‖L∞
[ ˜γ′ +γ′]
H1/ 2
2ε2
[ ˜γ′−γ′]
H1/ 2
2ε2
where we set forε∈ (0, 1
2)
[ f]
H1/ 2
ε
:=
(/iintegdisplay
R/ Z×[−ε,ε]
| f (u +w)− f (u)|2
w2 dw du
)1/ 2
.
For the second term we compute
⏐⏐⏐F(2)
2 (˜γ)− F(2)
2 (γ)
⏐⏐⏐
≤
/iintegdisplay
R/ Z×[−ε2,ε2]
⏐⏐⏐G˜γ(u,w )−G γ(u,w )
⏐⏐⏐
/iintegtext
[0, 1]2(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)2 dθ1 dθ2
w2 dw du
12
+
/iintegdisplay
R/ Z×[−ε2,ε2]
⏐⏐⏐Gγ(u,w )
⏐⏐⏐·
·
/iintegtext
[0, 1]2
⏐⏐⏐(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)2− (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2⏐⏐⏐dθ1 dθ2
w2
dw du
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
/iintegdisplay
[0, 1]2
/iintegdisplay
R/ Z×[−ε2,ε2]
|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2
w2 dw du dθ1 dθ2
+ C
‖‖‖γ′‖‖‖L∞
/iintegdisplay
[0, 1]2
/iintegdisplay
R/ Z×[−ε2,ε2]
|(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|) + (|γ′(u +θ1w)|−| γ′(u +θ2w)|)|
|w| ·
·|(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)− (|γ′(u +θ1w)|−| γ′(u +θ2w)|)|
|w| dw du dθ1 dθ2
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
[ ˜γ′] 2
H1/ 2
2ε2
+ C
‖‖‖γ′‖‖‖L∞
[ ⏐⏐⏐˜γ′⏐⏐⏐+
⏐⏐⏐γ′⏐⏐⏐
]
H1/ 2
2ε2
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H1/ 2
2ε2
.
Using the chain and product rule for Sobolev spaces and the formula
⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐=⟨˜γ′ +γ′, ˜γ′−γ′⟩
|˜γ′| +|γ′| ,
we obtain, assumingε0 < 1
4, for C > 0 depending on the constant from (2.2)
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H1/ 2
2ε2
≤
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H1/ 2(R/ Z)
≤ C
‖‖‖˜γ′−γ′‖‖‖H1/ 2∩L∞
‖‖‖˜γ′ +γ′‖‖‖H1/ 2∩L∞
(
1 + [ ˜γ′]
H1/ 2
2ε2
+ [ γ′]
H1/ 2
2ε2
)
where
‖·‖H1/ 2∩L∞ :=‖·‖H1/ 2 +‖·‖L∞.
Hence
⏐⏐⏐F(2)
2 (˜γ)− F(2)
2 (γ)
⏐⏐⏐≤ C
([ ˜γ′] 2
H1/ 2
2ε2
+
‖‖‖γ′‖‖‖L∞
([ ˜γ′]
H1/ 2
2ε2
+ [ γ′]
H1/ 2
2ε2
)‖‖‖˜γ′ +γ′‖‖‖H1/ 2∩L∞·
·
(
1 + [ ˜γ′]
H1/ 2
2ε2
+ [ γ′]
H1/ 2
2ε2
))
‖˜γ′−γ′‖H1/ 2∩L∞.
The claim follows from
lim sup
ε2ց0
sup
˜γ∈Xδ∩Y
[ ˜γ′]
H1/ 2
2ε2
≤δ.
□
13
Proof of Proposition 2.2. In order to prove that directional derivatives exist at γ0∈ H3/ 2
ir ∩
H1,∞ for all directionsϕ∈ H3/ 2∩ H1,∞ let Y be as in the proof of Lemma 2.4 and
X0 :={γ0 +τϕ|τ∈ (−1, 1)}.
First we observe that X0 satisﬁes (2.6), thus being an admissible set for Lemma 2.4. Indeed,
forγτ:=γ0 +τϕ,|τ|≤ 1,
(/iintegdisplay
R/ Z×[−ε,ε]
|γ′
τ(u +w)−γ′
τ(u)|2
|w|2 dw du
)1/ 2
≤

/iintegdisplay
R/ Z×[−ε,ε]
|γ′
0(u +w)−γ′
0(u)|2
|w|2 dw du

1/ 2
+
(/iintegdisplay
R/ Z×[−ε,ε]
|ϕ′(u +w)−ϕ′(u)|2
|w|2 dw du
)1/ 2
εց0
−−−→0. (2.8)
From this we deduce, for
fε:τ↦→E(2)
ε (γ0 +τϕ),
that
⏐⏐⏐f′
ε1(τ)− f′
ε2(τ)
⏐⏐⏐=
⏐⏐⏐δE(2)
ε1 (γ0 +τϕ;ϕ)−δE(2)
ε2 (γ0 +τϕ;ϕ)
⏐⏐⏐
≤ lim sup
θ→0
⏐⏐⏐⏐⏐⏐⏐
E(2)
ε1 (γ0 + (τ+θ)ϕ)− E(2)
ε1 (γ0 +τϕ)
θ − E(2)
ε2 (γ0 + (τ+θ)ϕ)− E(2)
ε2 (γ0 +τϕ)
θ
⏐⏐⏐⏐⏐⏐⏐
≤ lipX0∩Y
(
E(2)
ε1 − E(2)
ε2
)
‖ϕ‖H3/ 2∩H1,∞ (2.9)
ε1,ε2ց0
−−−−−−→0 by ( 2.7).
As E(2)
ε → E(2) pointwise, this proves that ( fε)ε>0 is a Cauchy sequence in C1((−τ0,τ0)) con-
verging to E(2)(γ0 +τϕ) = limεց0 E(2)
ε (γ0 +τϕ) as ε→ 0. Hence, especially all directional
derivatives of E(2) exist and
δE(2)(γ0;ϕ) = lim
εց0
δE(2)
ε (γ0;ϕ)
for allγ0∈ H3/ 2
ir ∩ H1,∞,ϕ∈ H3/ 2∩ H1,∞.
The next step is to establish Gˆ ateaux diﬀerentiability. To this end we merely have to show
δE(2)(γ0,·)∈
(
H3/ 2∩ H1,∞
)∗
forγ0∈ H3/ 2
ir ∩ H1,∞. Linearity carries over from E(2)
ε . In order
to prove boundedness we introduce
Xδ:={γ∈ H3/ 2 :‖γ−γ0‖H3/ 2≤δ} forδ∈ (0, 1] (2.10)
14
which also satisﬁes (2.6) as forγ∈ Xδwe have
(/iintegdisplay
R/ Z×[−ε,ε]
|γ′(u +w)−γ′(u)|2
|w|2 dw du
)1/ 2
≤

/iintegdisplay
R/ Z×[−ε,ε]
|γ′
0(u +w)−γ′
0(u)|2
|w|2 dw du

1/ 2
+δ
εց0
−−−→δ.
(2.11)
Now
δE(2)(γ0;ϕ) =δE(2)
ε (γ0;ϕ) +δE(2)(γ0;ϕ)−δE(2)
ε (γ0;ϕ)
=δE(2)
ε (γ0;ϕ) + lim
ε1ց0
(
δE(2)
ε1 (γ0;ϕ)−δE(2)
ε (γ0;ϕ)
)
and thus, arguing as in (2.9) and recallingδE(2)
ε (γ0;·)∈
(
H3/ 2∩ H1,∞
)∗
,
|δE(2)(γ0;ϕ)|≤| δE(2)
ε (γ0;ϕ)| + lim sup
ε1ց0
lipXδ∩Y
(
E(2)
ε1 − E(2)
ε
)
/bracehtipupleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipdownright/bracehtipdownleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipupright
<∞
‖ϕ‖H3/ 2∩H1,∞≤ C‖ϕ‖H3/ 2∩H1,∞
for all γ0∈ H3/ 2
ir ∩ H1,∞ andϕ∈ H3/ 2∩ H1,∞. Hence, E(2) is Gˆ ateaux diﬀerentiable and the
diﬀerential is given by (
E(2))′
(γ0) =δE(2)(γ0;·)
for allγ0∈ H3/ 2
ir ∩ H1,∞,ϕ∈ H3/ 2∩ H1,∞.
Finally, to see that the di ﬀerential is continuous, let σ >0 be given and let us choose δ >0
andε>0 so small that
lipXδ∩Y
(
E(2)
ε1 − E(2)
ε2
)(2.7)
≤ Cδ≤ 1
3σ
for allε1,ε2 <εwhere Xδis as in (2.10). Then we have forγ∈ Xδ∩Y and anyϕ∈ H3/ 2∩H1,∞
|δE(2)(γ;ϕ)−δE(2)(γ0;ϕ)|≤| δE(2)(γ;ϕ)−δE(2)
ε (γ;ϕ)| +|δE(2)
ε (γ;ϕ)−δE(2)
ε (γ0;ϕ)|
+|δE(2)
ε (γ0;ϕ)−δE(2)(γ0;ϕ)|
(2.9)
≤|δE(2)
ε (γ;ϕ)−δE(2)
ε (γ0;ϕ)| + 2
3σ‖ϕ‖H3/ 2∩H1,∞.
Since E(2)
ε is C1 we deduce that there is an open neighborhood V⊂ Xδofγ0 such that
|δE(2)
ε (γ;ϕ)−δE(2)
ε (γ0;ϕ)|≤ 1
3σ‖ϕ‖H3/ 2∩H1,∞
and hence
|δE(2)(γ;ϕ)−δE(2)(γ0;ϕ)|≤ σ‖ϕ‖H3/ 2∩H1,∞
for allγ∈ V. This proves that
(
E(2)
)′
is continuous from H3/ 2
ir ∩ H1,∞ into
(
H3/ 2∩ H1,∞
)∗
and
hence E(2) is C1(H3/ 2
ir ∩H1,∞). □
15
Proof of Theorem I. Using Proposition 2.2 we merely have to derive the formula of the ﬁrst
variation for a curve γ∈ H3/ 2
ir ∩ H1,∞ parametrized by arc-length and ϕ∈ H3/ 2∩ H1,∞. As
|γ′|≡ 1 a. e. we deduce from Lemma 2.3 and Equation (2.4)
δE(2)(γ;ϕ)
εց0
←−−−2
/iintegdisplay
Uε
{( 1
|γ(u +w)−γ(u)|2− 1
w2
)⟨γ′(u),ϕ′(u)⟩
− 2

⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4 −
d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u)
|w|3

}
dw du
where now
d
dτ
⏐⏐⏐τ=0 dγ+τϕ(u +w, u) =|w|
1∫
0
⟨γ′(u +θw),ϕ′(u +θw)⟩dθ
for all (u,w )∈ R/ Z× (− 1
2, 1
2). Hence,
δE(2)(γ;ϕ)
εց0
←−−−2
/iintegdisplay
Uε
{( 1
|γ(u +w)−γ(u)|2− 1
w2
)⟨γ′(u),ϕ′(u)⟩
−

⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4 −
∫1
0 ⟨γ′(u +θw),ϕ′(u +θw)⟩dθ
w2

}
dw du
= 2
/iintegdisplay
Uε
{( 1
|γ(u +w)−γ(u)|2− 1
w2
)⟨γ′(u),ϕ′(u)⟩
−
(⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4 −⟨γ′(u),ϕ′(u)⟩
w2
)}
dw du
= 2
/iintegdisplay
Uε
( ⟨γ′(u),ϕ′(u)⟩
|γ(u +w)−γ(u)|2−⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|4
)
dw du.
□
