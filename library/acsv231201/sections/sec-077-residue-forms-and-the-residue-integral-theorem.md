---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-077-residue-forms-and-the-residue-integral-theorem
section_title: "Residue forms and the residue integral theorem"
section_number: null
pages: 503-516
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Corollary C.4. Let Y be a closed subspace of Cd
∗ and let α andβ be relative
cycles in the pair (M,M∩ Y) that are homologous in (Cd
∗, Y). There is a well-
deﬁned intersection class INT[α,β ;V]Y∈ Hd−1(V∗, Y) such that if H is any
(d + 1)-chain inCd
∗ with∂ H =α′−β′ +γ, where [α′] = [α] and [β′] = [β] in
Hd(M,M∩ Y) andγ∈ Y, and if H intersectsV transversely, then H∩V is
a relative cycle in the class INT[α,β ;V]Y. □
By the excision property of homology, the pair ( M,M∩ Y) is homotopy
equivalent to the pair (M\ Y◦,∂ Y). This allows us to extend Corollary C.4 to
the case whereα andβ can intersectV, but only in the interior of Y.
Corollary C.5. Let Y be a closed subspace of Cd
∗ and let α andβ be relative
cycles homologous in(Cd, Y) intersectingV only in the interior of Y. There is a
well-deﬁned intersection class INT[α,β ;V]Y∈ Hd−1(V∗,V∗∩ Y), depending
only on the class of α−β in Hd(M,M∩ Y), such that if H is a (d + 1)-chain
inCd
∗ with∂ H = α−β +γ, whereγ is supported on the interior of Y, and if
the intersection of H withV is transverse away from the interior of Y, then
H∩V is a relative cycle representing the class INT[α,β ;V]Y. □
In the special case of Corollary C.5, where β = 0 and Y is the set of points
at height c or less, we denote the relative intersection class by INT[α;V]≤c.
C.2 Residue forms and the residue integral theorem
Integrating a diﬀerential form over a diﬀerence of chains can often be reduced
to integrating a residue form over an intersection cycle. Because residues de-
pend on local behavior, we work with subsets of Cd that are locally deﬁned
by analytic functions. An analytic hypersurface (or simply hypersurface) is
a set V ⊂Cd such that for any w ∈ Vand any su ﬃciently small neigh-
borhoodD ofw inCd there is an analytic function QD onV∩D such that
V∩D ={z∈D : QD(z) = 0}. If the function QD can be chosen to have
nonvanishing gradient onV∩D then we sayV is a smooth analytic hyper-
surface atw, and we callV a smooth analytic hypersurface if it is a smooth
analytic hypersurface at every point.
Although the theory of multivariate residues is much more involved than its
univariate counterpart, we require it only for di ﬀerential forms whose singu-
larities lie on unions of smooth analytic hypersurfaces. We build our results in
four degrees of generality, starting with forms having smooth simple poles,
then forms with smooth higher order poles, followed by forms with trans-
versely intersecting smooth sheets of simple poles, and concluding with forms
having transversely intersecting smooth sheets with higher order poles.
486 Residue forms and classical Morse theory
C.2.1 Residue forms for smooth simple poles
Fix a smooth analytic hypersurfaceV deﬁned locally by analytic functions QD
as above, and recall our notationM =Cd
∗\V and dz = dz1∧···∧ dzd. We say
that a d-formω∈ Ed(M) has smooth poles of order k onV if for anya∈V
there is a su ﬃciently small neighborhood D ofa in Cd
∗ such that QD(z)kω
extends to a holomorphic form on D but QD(z) jω does not extend to such a
holomorphic form for any 0≤ j < k. A form with smooth poles of order one
is said to have simple poles.
Proposition C.6. Let ω be a holomorphic d-form with smooth simple poles
onV, represented as a quotient ω = P(z)/Q(z) dz of analytic functions on
M∩D for some domainD⊂ Cd on which the gradient of Q does not vanish.
IfW =V∩D andι :W ↪→D is the inclusion ofW intoCd then there is a
(d− 1)-formθ onD solving dQ∧θ = P dz and any such solution restricts to
a unique (d− 1)-form Res(ω) =ι∗θ onW called the residue ofω onW.
Remark C.7. Our deﬁnition of the residue is both natural, meaning it does
not depend on the particular polynomials P and Q used to represent ω =
P(z)/Q(z) dz onD, and functorial, meaning Res(f∗ω) = f∗ Res(ω) for smooth
functions f . Because the residue is natural, we can deﬁne Res( ω) on all ofV
by deﬁning it locally over the elements of a cover of V by suﬃciently small
domains using Proposition C.6.
Proof We must show both that dQ∧θ = P dz always has a holomorphic so-
lution, and that the restriction of any such solution toV is unique. Uniqueness
follows from Exercise A.18 at the end of Appendix A: if θ1 and θ2 are two
solutions then dQ∧ (θ1−θ2) = 0, hence Exercise A.18 impliesι∗θ1 =ι∗θ2. The
existence of a solution follows from the following proposition, which expresses
the residue explicitly in local coordinates in suﬃciently small neighborhoods,
by combining residues in local neighborhoods as discussed in Remark C.7. □
Proposition C.8. Under the hypotheses of Proposition C.6, if the partial deriva-
tive∂Q/∂zk is nonvanishing onD for some ﬁxed k≤ d andr∈Zd then
Res(z−rω) = (−1)k−1z−rP(z)
Qzk(z) dzˆk, (C.2.1)
where dzˆk = dz1∧···∧ dzk−1∧ dzk+1∧···∧ dzd.
Proof If k = 1 andθ is the right-hand side of (C.2.1), then
dQ∧θ =

d∑
j=1
Qz j(z)dz j
∧
(z−rP
Qz1(z) dz2∧···∧ dzd
)
=z−rP dz,
C.2 Residue forms and the residue integral theorem 487
as desired. In the general case, the sign (−1)k−1 comes from the position of dzk
in the wedge product. □
Exercise C.1. Letω = 1/Q(x, y) dxdy, where Q(x, y) = 1− x− xy + y2. Find
a formula for Res(ω) onV =VQ in terms of dx only, and another in terms of
dy only. Prove that the restrictions of these forms toV are equal.
Theorem C.9 (residue integral theorem) . SupposeV = VQ = {z ∈ Cd :
Q(z) = 0} is deﬁned globally by a function Q that is analytic on a neighbor-
hood ofV and has nonvanishing gradient onV, and let ω be a holomorphic
d-form onM with smooth simple poles on V. If α and β are d-cycles inM
whose projections to Hd(Cd
∗) are equal then
∫
α
ω−
∫
β
ω = 2πi
∫
INT[α,β;V]
Res(ω).
Proof Vanishing of [α−β] in Hd(Cd
∗) by deﬁnition implies the existence of a
(d + 1)-chain H onCd
∗ with boundary α−β. Perturbing slightly if necessary,
we can assume without loss of generality that H intersectsV transversely.
Letting N denote the intersection of H with a small neighborhood of V and
Θ = H−N, the vanishing of holomorphic integrals ofd-forms over boundaries
(Theorem A.27) implies that the integral of the holomorphicd-formω over∂Θ
vanishes. In other words,
∫
α
ω−
∫
β
ω =
∫
∂N
ω.
The Collar Lemma (Lemma C.1) implies that N is homotopic to a product
σ× Bε, whereσ = H∩V . Thus∂N is homotopic to∂(σ× Bε), which is equal
toσ×∂Bε becauseσ is a cycle, giving
∫
σ×∂Bε
ω =
∫
σ
(∫
∂Bε
ω
)
.
Using functoriality of the residue, we may change coordinates so thatV is the
complex hyperplane deﬁned by z1 = 0. Thus we need only prove our claim
in the case where Q(z) = z1. Writing ω = (P/z1)dz1∧ (dz2∧···∧ dzd), the
iterated integral is
∫
σ
[∫
∂Bε
P(z)
z1
dz1
]
dz2∧···∧ dzd.
By standard univariate complex analysis, the inner integral at a point (z2,..., zd)
is the residue with respect to t of the meromorphic function P(t, z2,..., zd)/t at
488 Residue forms and classical Morse theory
the pole (0, z2,..., zd). This is equal to
(2πi)
∫
σ
P(0, z2,..., zd),
which in this special case is precisely
∫
σ Res(ω). □
There is also a relative version of this result.
Theorem C.10 (relative residue integral theorem). LetV andω be as in The-
orem C.9. If Y is any closed subspace ofCd
∗ such that Hd(Cd
∗, Y) vanishes, and
ifα is a d-cycle inM, then
∫
α
ω = 2πi
∫
INT[α,0;V]
Res(ω) +
∫
C′
ω (C.2.2)
for some chainC′ supported on the interior of Y. In particular, if ω = z−rη
for some holomorphic form η onM and if Y is the set where the real part of
h ˆr =− ˆr· logz is at most c then, asλ→∞ ,
∫
α
ω = 2πi
∫
INT[α,0;V]
Res(ω) + O
(
eλc′)
(C.2.3)
for any c′ > c.
Proof By the vanishing of Hd(Cd
∗, Y) there is a ( d + 1)-chain H with∂ H =
α +γ andγ supported on the interior of Y. Let N denote the intersection of H
with a neighborhood ofV. As before,
∫
α
ω =
∫
γ
ω +
∫
∂N
ω.
Letting σ = H∩V , we recall that ∂N is homotopic to σ× Bε plus a piece
γ′ in the interior of Y. TakingC′ = γ +γ′, the rest of the proof of (C.2.3)
is the same as that of Theorem C.9. The asymptotic estimate follows because⏐⏐⏐⏐
∫
C′ω
⏐⏐⏐⏐≤ eλc ∫
C′|η|, as in the proof of Proposition B.10. □
C.2.2 Residue forms on smooth higher order poles
Letω andω′ be holomorphic d-forms onM with simple poles on the smooth
varietyV =VQ. If ω and ω′ are cohomologous in Hd(M) then [Res(ω)] =
[Res(ω′)] in Hd−1(V∗), and the study of residue classes of forms with smooth
higher order poles can be reduced to those with smooth simple poles using this
property.
C.2 Residue forms and the residue integral theorem 489
Lemma C.11 (Gelfand–Shilov reduction). If ω is a holomorphic d-form on
M with smooth poles of order k ≥ 2 onV and the representation ω =
P(z)/Q(z)k dz holds on a domainD then
ω = dQ
Qk∧ψ + θ
Qk−1
= d
( −ψ
(k− 1)Qk−1
)
+ θ1
Qk−1
for some holomorphic forms ψ and θ, where θ1 = θ + dψ/(k− 1). Thus, any
d-form onM with smooth poles of order k is cohomologous to a d-form onM
with smooth poles of order k− 1.
Proof See [AY83, Lemma 17.1]. □
If ω is any d-form onM with smooth poles then Lemma C.11 implies ω
is cohomologous to a d-form ω′ onM with smooth simple poles, and we
deﬁne the residue class [Res(ω)] of ω to be the class [Res(ω′)]∈ Hd−1(V∗).
To simplify notation we usually write Res( ω) for the class [Res( ω)]. As our
integrals of residues depend only on their cohomology classes, there is no harm
in this abuse of notation. This inductive deﬁnition gives the following corollary
of Theorem C.9.
Corollary C.12. Suppose the assumptions of Theorem C.9 hold, except thatω
can have smooth poles of any order onV. Ifα andβ are d-cycles inM whose
projections to Hd(Cd
∗) are equal then the identity
∫
α
ω−
∫
β
ω = 2πi
∫
INT[α,β;V]
Res(ω)
still holds.
Just as for smooth poles, there is an explicit formula for the residue of a
form with higher order poles. We state the following theorem for the types of
integrands that arise in our asymptotic analyses.
Lemma C.13. Let dzˆk denote the (d− 1)-form dz1∧···∧ dzk−1∧ dzk+1∧···∧
dzd. Wherever the functions P (z)z−r and Q (z) are analytic and the partial
derivative Qzk(z) does not vanish,
Res
(
z−r P(z)
Q(z)𝓁 dz
)
=z−rΦrk(z) (C.2.4)
for a polynomial
Φrk(z) =
[
(−1)k−1
(−rk
𝓁− 1
)
z−(𝓁−1)
k
P(z)
Qzk(z)𝓁 + O
(
r𝓁−2
k
)]
dzˆk
490 Residue forms and classical Morse theory
in rk of degree 𝓁− 1 whose coeﬃcients are analytic functions of z explicitly
given in terms of derivatives of P and Q.
Proof We induct on 𝓁, with the case 𝓁 = 1 handled by Proposition C.8. As-
sume for an induction that the lemma holds for 𝓁− 1. Because the residue of
an exact form is zero, we let
η = (−1)k−1z−r P(z)
(𝓁− 1)Q(z)𝓁−1Qzk(z)dzˆk
and examine
0 = Res(dη)
= Res
z−r Pzk(z)
(𝓁− 1)Q(z)𝓁−1Qzk(z)dz +z−r −rkP(z)z−1
k
(𝓁− 1)Q(z)𝓁−1Qzk(z)dz
−z−r P(z)
Q(z)𝓁 dz−z−r P(z)Qzk,zk(z)
(𝓁− 1)Q(z)𝓁−1Qzk(z)dz
]
.
Isolating the third term on the right yields
Res
(
z−r P(z)
Q(z)𝓁 dz
)
= Res
z−r −rkP(z)z−1
k
(𝓁− 1)Q(z)𝓁−1Qzk(z) dz

+ Res
(
z−r A(z)
Q(z)𝓁−1 dz
)
,
(C.2.5)
for an analytic functionA independent of rk. Applying the induction hypothesis
to the ﬁrst residue on the right-hand side of (C.2.5) shows that it equals
(−1)k−1

−rk
𝓁− 1
(−rk− 1
𝓁− 2
)
z−rz−(𝓁−2)
k
P(z)z−1
k /Qzk(z)
Qzk(z)𝓁−1 + O
(
r𝓁−3
k
) dzˆk,
while applying the induction hypothesis to the second residue on the right-
hand side of (C.2.5) proves that it isO
(
r𝓁−2
k
)
. Combining powers of Qzk(z) and
powers of zk, and simplifying −rk
𝓁− 1
(−rk− 1
𝓁− 2
)
=
(−rk
𝓁− 1
)
, then gives the stated
result. □
C.2.3 Iterated residue forms for simple poles on transverse sheets
In this section we summarize a generalization of residue forms to the case
whereV is the union of a ﬁnite number of smooth analytic hypersurfaces that
intersect transversely. A full treatment of residues for forms with transverse
poles can be found in [AY83, Section 16.5].
C.2 Residue forms and the residue integral theorem 491
Deﬁnition C.14. IfV⊂ Cd is an analytic hypersurface then we call w∈V
a transverse multiple point ofV if there exists a neighborhoodD ofw inCd
such thatD∩V =D∩ (VQ1∪···∪V Qk) for smooth analytic hypersurfaces
{VQ j : 1 ≤ j≤ k} deﬁned by analytic functions Q j(z) whose gradients at
z =w are linearly independent. When this collection of analytic functions is
understood andm∈Nk then we writeQ(z)m = Q1(z)m1··· Qk(z)mk. If every
point ofV is a transverse multiple point then we callV a transverse analytic
hypersurface.
Example C.15. Every smooth analytic hypersurface is a transverse analytic
hypersurface. ◁
Fix a transverse analytic hypersurface V and let ω be a d-form onM =
Cd\V . We say thatω has a transverse pole (or transverse multiple point) of
orderm∈Nk atw∈V if
• there exists a neighborhoodD ofw inCd and analytic functions Q1,..., Qk
onD such thatD∩V =D∩ (VQ1∪···∪V Qk) and the gradients of the Qi
are linearly independent atw (in particular, they are all non-zero),
• there exists an analytic function P onD such that ω = P(z)/Q(z)mdz
whenz∈D∩M , and
• there is no possible choice of Q and P such that these properties hold with
any coordinate ofm decreased.
A transverse multiple point of order 1 is called a transverse simple pole (or
transverse simple point). The ﬁnal item in this deﬁnition implies that the nu-
merator P and denominator factors Qk in the local representation of ω are co-
prime in the ring of germs of analytic functions, ensuring thatm is the correct
notion of order (no unwanted cancellation can occur).
Letp be a transverse simple pole of the d-formω, with the local represen-
tation
ω = P(z)
Q1(z)··· Qk(z)dz
in some neighborhood of p. To simplify notation we writeVi =VQi and let
S = ⋂k
i=1Vi be the stratum ofV containingp. Because the gradients of the
Qi are linearly independent at p, there exist coordinates π = {π1,...,π d−k}
that locally analytically parametrize S near p. In particular, writing zπ =
(zπ1,..., zπd−k) there exists a neighborhood D ofp in Cd and analytic func-
tionsζi(zπ) onD for i<π such thatz∈D lies inS if and only if zi =ζi(zπ)
for all i<π.
As detailed later in these appendices, ifD is suﬃciently small thenM∩D
has a local product structure ˜N×S . Becausep is a transverse multiple point
492 Residue forms and classical Morse theory
with k sheets, the factor ˜N is homotopy equivalent to a k-torus and we can
represent the homology of ˜N using a product of k circles aroundp. To make
this explicit, we note that the map Ψ :D→ Cd deﬁned by
Ψ(z) = (Q1(z),..., Qk(z), zπ1− pπ1,..., zπd−k− pπd−k
) (C.2.6)
is a bi-analytic change of coordinates taking D∩S to a neighborhood of the
origin in{0}× Cd−k. Let Tε⊆ Ck×{ 0} denote the product of circles of radius
ε in each of the ﬁrst k coordinates. If ε is suﬃciently small then Tε⊂ Ψ(D)
and the cycle T = Ψ−1(Tε) will be a generator for Hk( ˜N). We giveD the local
product structure that Ψ−1 induces from the product structure onCd.
Deﬁnition C.16. If f is a diﬀerentiable function then thelogarithmic gradient
of f atz is
(∇log f )(z) := (z1 fz1(z),..., zd fzd(z)).
For eachz∈S , the augmented lognormal matrix is the d× d matrix
ΓΨ(z) =

(∇log Q1)(z)
...
(∇log Qk)(z)
zπ1eπ1
...
zπd−keπd−k

,
wheree j denotes the jth elementary basis vector. Equivalently, ΓΨ = JΨD
where D is the diagonal matrix with entries z1,..., zd and JΨ is the Jacobian
matrix of the map Ψ.
Remark. The deﬁnition of ΓΨ depends on the choice of factorization, each
factor being determined only up to a complex multiple. Suitable normalizations
are assumed later in the deﬁnition of the torus T following (10.3) and the
determination of the orientation in the proof of Theorem 10.25.
Theorem C.17 (iterated residues). Under the setup discussed above, let ω be
the holomorphic d-formω = P(z)∏k
j=1 Q j(z) dz onM∩D and writeSD =S∩D =
V1∩···∩V k∩D .
(i) Iterated residue is well deﬁned. The restriction toSD of any d-form θ
onD satisfying
dQ1∧···∧ dQk∧θ = P dz (C.2.7)
is independent of the particular solutionθ.
C.2 Residue forms and the residue integral theorem 493
(ii) Formula for the iterated residue.Denoting the iterated residue deﬁned
by this restriction by Res(ω;SD), there is a formula
Res

P(z)
∏k
j=1 Q j(z)
dz ;SD
 = P(z)
det JΨ(z)
⏐⏐⏐⏐⏐ zi=ζi(zπ)
for all i<π
dzπ1∧···∧ dzπd−k.
(C.2.8)
(iii) Residue integral identity. Let σ be any (d− k)-chain inSD and T =
Ψ−1(Tε) be as above. Then
1
(2πi)k
∫
T×σ
P(z) dz
∏k
j=1 Q j(z)
=
∫
σ
Res

P(z)
∏k
j=1 Q j(z)
;SD
 . (C.2.9)
(iv) Formula for Cauchy integral. In particular,
1
(2πi)k
∫
T×σ
z−r−1P(z)
∏k
j=1 Q j(z)
dz =
∫
σ
z−rP(z)
det ΓΨ(z)
⏐⏐⏐⏐⏐ zi=ζi(zπ)
for all i<π
dzπ1∧···∧ dzπd−k.
(C.2.10)
Proof We ﬁrst prove all four parts under the assumption that Q j(z) = z j for
all 1≤ j≤ k. Settingπi = k + i for all 1≤ i≤ d− k, the formθ = P(z) dzk+1∧
···∧ dzd satisﬁes (C.2.7). As in the proof of Proposition C.6 above, the result of
Exercise A.17 implies thatι∗θ is well deﬁned, yielding (i). The formula (C.2.8)
is also evident in this case: JΨ is the identity matrix, hence (C.2.8) agrees with
our choice ofθ after setting zi = 0 for 1≤ i≤ k, proving (ii). For (iii), we write
the left-hand side as an iterated integral
1
(2πi)k
∫
σ
∫
γ1
···
∫
γk
P(z) dz
∏k
j=1 Q j(z)
,
whereγ j is the circle of radiusε about the origin in the jth coordinate. Apply-
ing the univariate residue theorem to each of the inner k integrals leaves
∫
σ
P(z) dzk+1∧···∧ dzd,
proving (iii). Finally, (iv) follows from (iii) by replacing P(z) withz−r−1P(z)
in (C.2.8) and absorbing one factor of each z j in the denominator when going
from det JΨ to det ΓΨ.
For the general case, map by Ψ and use functoriality. The fact that Res is
well deﬁned and functorial follows from the same argument as in the proof
of Proposition C.6. Applying the case already proved to the image space and
pulling back by Ψ−1, it remains only to observe thatdzk+1∧···∧ dzd pulls back
to 1
det JΨ(z)
⏐⏐⏐⏐zi=ζi(zπ) : i<π
dzπ1∧···∧ dzπd−k, and P(0) pulls back to P(z)|zi=ζi(zπ) : i<π.
□
494 Residue forms and classical Morse theory
Remark. The residue depends on Q j only via its gradient. The sign of the
residue form depends on the order of the factors in the denominator, and we
account for this when using residue forms to determine asymptotics.
When the stratumS is a single point (meaning k = d) the residue atp is just
a number, simplifying the conclusions of Theorem C.17 as follows.
Corollary C.18. Suppose the hypotheses of Theorem C.17 hold in the special
case where k = d, so that the residue ofω atp is a numberθ0. Then
(i) P (p) dz =θ0 (dQ1∧···∧ dQd) (p),
(ii) Res

P(z)
∏d
j=1 Q j(z)
dz ;p
 = P(p)
det JΨ(p),
(iii) 1
(2πi)d
∫
Ψ−1(Tε)
P(z) dz
∏d
j=1 Q j(z)
= Res

P(z)
∏d
j=1 Q j(z)
;p
,
(iv) 1
(2πi)d
∫
Ψ−1(Tε)
z−r−1P(z)∏s
j=1 Q j(z)dz = p−r−1P(p)
det JΨ(p) = p−rP(p)
det ΓΨ(p).
Example C.19 (two lines inC2). Let
Q(x, y) =
(
1− 1
3 x− 2
3y
)(
1− 2
3 x− 1
3y
)
so thatVQ has a transverse multiple point at ( x, y) = (1, 1). The gradients of
the factors of Q are (1/3, 2/3) and (2/3, 1/3), which are also their logarithmic
gradients when x = y = 1. The determinant of ΓΨ is therefore one of±1/3, the
sign choice depending on the order in which we choose the factors. Up to sign,
the iterated residue of Q(x, y)−1dx∧ dy at (1, 1) is thus the number 3. ◁
Example C.20 (dimension three with two factors) . Consider the generating
function
F(x, y, z) = 16
(4− 2x− y− z)(4− x− 2y− z),
whose singular set consists of two planes meeting at the complex line S =
{(1, 1, 1) +λ(−1,−1, 3): λ∈ C}. In this case we can parametrize S globally
by any of its three coordinates (i.e., we can take D = C3). Choosing the third
C.2 Residue forms and the residue integral theorem 495
coordinate, makingπ1 = 3, we obtain
JΨ(x, y, z) =

−2 −1 −1
−1 −2 −1
0 0 1
 ,
whence det ΓΨ = 3 and
Res(F(x, y, z) dx∧ dy∧ dz;S) = 16
3 dz.
Choosing one of the ﬁrst two coordinates leads to an equivalent answer: the
ﬁrst two rows of JΨ are unchanged while the third row becomes either (1, 0, 0)
or (0, 1, 0), ultimately giving the representations −16dx and 16dy. These are
all equal, up to sign, as 1-forms onS. ◁
C.2.4 Iterated residue forms for higher order poles on transverse
divisors
In Section C.2.2 above we used Gelfand–Shilov reduction (Lemma C.11) to
deﬁne a residue for higher order smooth poles in terms of the residue for
smooth simple poles. A version of Gelfand–Shilov reduction also works for
iterated residues leading, through a computation analogous to the ones used to
establish Theorem C.17, except messier, to the following result.
Proposition C.21. LetS be a smooth codimension k variety in Cd
∗ deﬁned
by the vanishing of k analytic functions Q 1,..., Qk, let U denote the module
over holomorphic functions of all meromorphic forms that can be written as
ψ/∏k
j=1 Q
n j
j , where ψ is holomorphic in a neighborhood of S in Cd, and let
R = U/E, where E is generated by the forms {Res(dη) : η∈ R}. Then every
class in R has a representative in which each power nj is equal to 1. □
The rest of this section is devoted to the statement and proof of Theo-
rem C.24, an explicit formula for the residue in the speciﬁc case we use in
this text. We begin with a lemma indicating what form the answer will take.
Lemma C.22. Let f, f1,..., fd be smooth functions ofu∈Ck. Then
( ∂
∂u
)n
f (u) f1(u)r1··· fd(u)rd = f (u) f1(u)r1··· fd(u)rdΦ(r,u),
where Φ is a polynomial inr of degree|n| = n1 +··· + nk. The leading term of
Φ isK(r,u)n = ∏k
j=1K j(r,u)n j, where
K j(r,u) =
d∑
i=1
ri
∂ log fi
∂u j
.
496 Residue forms and classical Morse theory
Proof We show by induction that
( ∂
∂u
)n
f (u) f1(u)r1··· fd(u)rd = f (u) f1(u)r1··· fd(u)rd [K(r,u)n + Q(r,u)]
(C.2.11)
for alln, where Q is a polynomial in r of degree less than|n|. Whenn = 0
this holds with Q = 0. Assuming this holds for n, taking the logarithm and
diﬀerentiating with respect tou j gives, after some algebraic simpliﬁcation, that( ∂
∂u
)n+δ j
f (u) f1(u)r1··· fd(u)rd equals the right-hand side of (C.2.11) when
K(r,u)n + Q(r,u) is replaced by
∂ log f
∂u j
+K j· (Kn + Q) + ∂
∂u j
(Kn + Q).
The terms in this expression other thanK j·Kn =Kn+δ j are polynomials inr
of degree at most|n|, completing the induction. □
We now specialize to our context.
Corollary C.23. Let Ψ be the parametrization deﬁned in(C.2.6) with Jacobian
matrix J Ψ(z). If we parametrize z = z(u) for variables u∈ Ck andm is a
vector of positive integers then
( ∂
∂u
)m−1 
z(u)−rP
(
Ψ−1(u)
)
∏d
j=1 z j(u) det JΨ
(Ψ−1(u))
 =
z(u)−rP
(
Ψ−1(u)
)
P(r,u)
∏d
j=1 z j(u) det JΨ
(Ψ−1(u)) ,
(C.2.12)
where
P(r,u) =

k∏
j=1

d∑
i=1
ri
∂ log zi(u)
∂u j

m j−1
+ R(r,u)
 (C.2.13)
for some polynomial R inr of degree less than|m|− k.
Theorem C.24. Under our running assumptions, the iterated residue has a
computable expression
Res
z−r−1 P(z)
∏k
j=1 Q j(z)m j
dz ; SD
 = z−rP(r,z)∏
j∈π z j
⏐⏐⏐⏐⏐⏐zi=ζi(zπ) : i<π
dzπ,
(C.2.14)
whereP(r,z) is a polynomial in r of degree|m|− k. The leading term of
P(r,z) is
P(r,z)∼ (−1)|m−1|
(m− 1)!
P(z)
det ΓΨ(z) (rΓ−1
Ψ )m−1 , (C.2.15)
where ΓΨ is the matrix from Deﬁnition C.16, the notation (rΓ−1
Ψ )m−1 stands
C.2 Residue forms and the residue integral theorem 497
for ∏k
i=1(rΓ−1
Ψ )mi−1
i , and (m− 1)! = ∏k
i=1(mi− 1)!. When k = d, the for-
mula (C.2.14) simpliﬁes slightly to
Res
z−r−1 P(z)
∏d
j=1 Q j(z)m j
dz ;p
 = p−rP(r,p). (C.2.16)
Remark. Recall that the factors {Qi : 1 ≤ i ≤ k} are deﬁned only up
to transformations multiplying each Qi by a complex number λi, satisfying∏k
i=1λm1
i = 1. This multiplies det ΓΨ by ∏k
i=1λi and divides (rΓ−1
Ψ )m−1 by∏k
i−1λmi−1
i , thus leaving the ratio (rΓ−1
Ψ )m−1/ det ΓΨ which appears in (C.2.15)
invariant. Later, when we need to compute orientations, it will be convenient
to normalize each Qi to have constant term 1, simultaneously normalizingP to
have constant term a0.
Example C.25. Let a and b be positive integers and consider the function
F(x, y, z) = 16
(4− 2x− y− z)a (4− x− 2y− z)b ,
generalizing the function in Example C.20. Choosing to parametrize the line
S deﬁned by the common zero sets of the denominator factors of F by the
coordinate z, we have the matrix
ΓΨ(x, y, z) =

−2x −y −z
−x −2y −z
0 0 1
 ,
whence det ΓΨ = 3xy and, writingr = (r, s, t),
rΓ−1
Ψ =
( sx− 2ry
3xy , ry− 2sx
3xy , 3txy− ryz− sxz
3xy
)
.
Since we can parametrize x = y = g(z) onS where g(z) = (4− z)/3, we have
det ΓΨ|x=y=g(z) = (4− z)2
3
and
(rΓ−1
Ψ )m−1⏐⏐⏐x=y=g(z) =
(2r− s
z− 4
)a−1 (2s− r
z− 4
)b−1
,
wherem = (a, b). Thus
Res
[
z−r−1F(z) dz;S
]
= x−ry−sz−t−1 [
P0(z) + O
(
(r + s)a+b−3)]
dz, (C.2.17)
where, taking into account (−1)|m−1| = (−1)(a−1)+(b−1) to change factors ofz−4
