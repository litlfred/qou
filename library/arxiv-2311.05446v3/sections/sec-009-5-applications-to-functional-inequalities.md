---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-009-5-applications-to-functional-inequalities
section_title: "Applications to functional inequalities"
section_number: 5
pages: 25-29
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
In this section, we present some applications of the second part of Propo-
sition 4.12, that is, the (2,n)-convexity ofD(µ t∥γ) when one endpoint of
the geodesic segment{µ t}t∈[0,1] is an even strongly log-concave probability
measure, and the other is theγitself. More specifically, we will prove im-
proved (2,n) versions to the (a priori (1,∞)−) GaussianHWI, Logarithmic
Sobolev, and Talagrand inequalities, for even strongly log-concave probabil-
ity measures.
Definition 5.1.The (relative)Fisher informationof a measureµis defined
by,
I(µ∥γ) =
Z |∇f| 2
f dγ,(67)
wheref= dµ
dγ .
As discussed in the Introduction, HWI inequalities relate the three quan-
tities that its initials correspond to. The main idea is to do calculus on
the relative entropyD(µ t∥γ) along the displacement interpolation between
µandγ, using the convexity properties of relative entropy. This accounts
for the “H” and the “W”. The Fisher informationI(µ∥γ) appears because
26 GAUTAM AISHWARYA AND LIRAN ROTEM
it plays the role of the squared norm of the gradient ofD(·∥γ) under the
previously mentioned Riemannian-like structure onW 2(Rn). This makes
the Fisher information a natural candidate to bound the derivative of rela-
tive entropy along any given (unit) tangent. To the interested reader who
is unfamiliar with the idea outlined in this paragraph, we recommend the
clear heuristic treatment of the (K,∞)-case in [38, Section 3]. Logarithmic
Sobolev and Talagrand inequalities (which relateH,I, andW,I, respec-
tively) follow from a suitable HWI inequality.
We follow the footsteps of [21, Section 3.4] where the authors derive (κ,n)-
versions of these inequalities from (κ,n)-convexity of relative entropy in a
very general setup. While a global (κ,n)-convexity condition is assumed in
[21], it is easily seen from the proofs that the requirement is only on the
interpolations connecting a measureµ(for which the inequalities are to be
proven) to the reference measure (γin our case). Therefore, for complete-
ness, we will only sketch the main steps in [21] adapted to our setup. The
reader is referred to [21] for more details.
To begin with, we decipher what the local condition of (2,n)-convexity
means globally. Towards this, we need some definitions.
Definition 5.2.[21, Definition 2.1] Forθ≥0, we define the following
functions.
s(θ) =s 2/n(θ) =
rn
2 sin
 r
2
nθ
!
,
c(θ) =c 2/n(θ) = cos
 r
2
nθ
!
.
(68)
Fort∈[0,1], we set
σ(t)(θ) =σ (t)
2/n(θ) =
( s(tθ)
s(θ),ifθ< pn
2π,
∞,otherwise.
(69)
In terms of the coefficientsσ (t) we may write a global condition for (2,n)-
convexity.
Lemma 5.3.[21, Lemma 2.2]The(2,n)-convexity ofD(µ t∥γ)implies that,
e−D(µt∥γ)
n ≥σ (1−t)(W2(µ0,µ 1))e−D(µ0∥γ)
n +σ (t)(W2(µ0,µ 1))e−D(µ1∥γ)
n .(70)
Proof outline.Letu(t) =e −D(µt∥γ)
n letv(t) denote the RHS in the above
inequality. The (2,n)-convexity ofD(µ t∥γ) is equivalent to the condi-
tionu ′′(t)≤− 2
n W 2
2 (µ0,µ 1)u(t). On the other hand,v(t) satisfiesv ′′(t) =
− 2
n W 2
2 (µ0,µ 1)v(t). The proof concludes by a maximum principle.□
Remark 5.4.Lemma 5.3 forcesW 2
2 (µ,γ)≤ n
2π2 for all even strongly
log-concave probability measures because the coefficientsσ (t)(·) blow up atpn
2π. However, this is not alarming since the stronger boundW 2
2 (µ,γ)≤n
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 27
can be obtained by a straightforward calculation using Caffarelli’s contrac-
tion theorem and the Gaussian Poincar´ e inequality.
Using Lemma 5.3, we obtain Theorem 1.7, which is restated below.
Theorem 5.5(A (2,n)-HWI inequality).Letµbe an even strongly log-
concave probability measure onR n, then,
e
D(µ0∥γ)
n −D(µ1∥γ)
n ≤c(W 2(µ0,µ 1)) + 1
n s(W2(µ0,µ 1))
p
I(µ0∥γ),(71)
where{µ 0,µ 1}={µ,γ}.
In particular,
e
D(µ∥γ)
n ≤c(W 2(µ,γ)) + 1
n s(W2(µ,γ))
p
I(µ∥γ).(72)
Proof outline.When{µ 0,µ 1}={µ,γ}, the relative entropyD(µ t∥γ) is
(2,n)-convex by Proposition 4.12 and Theorem 4.6. Therefore, Equation
(70) holds. Now subtractinge −D(µ0∥γ)
n from both sides of Equation (70),
dividing both sides byt, and lettingt→0, we obtain
e−D(µ1∥γ)
n ≤c(W 2(µ0,µ 1))·e−D(µ0∥γ)
n + s(W2(µ0,µ 1))
W2(µ0,µ 1)
d
dte−D(µt∥γ)
n

t=0
.(73)
Observing that
d
dte−D(µt∥γ)
n

t=0
= 1
ne−D(µ0∥γ)
n
d
dt (−D(µt∥γ))|t=0
≤ 1
ne−D(µ0∥γ)
n
p
I(µ0∥γ)W2(µ0,µ 1)
(74)
completes the proof of the first inequality. Here we have used a piece from
the computation (49),
d
dt (−D(µt∥γ))|t=0 =
Z
Lθ0 dµ0 =−
Z
⟨∇logf,∇θ 0⟩dµ 0
≤
Z
|∇logf| 2 dµ0
1/2Z
|∇θ0|2 dµ0
1/2
=
p
I(µ0∥γ)W2(µ0,µ 1),
(75)
wheref= dµ0
dγ and∇θ t denotes the velocity field driving the displacement
interpolation fromµ 0 toµ 1.
The second inequality is obtained simply by settingµ 0 =µ,µ 1 =γ.□
As immediate corollaries, dimensional improvements of the Gaussian Log-
arithmic Sobolev and Gaussian Talagrand inequalities are obtained for even
strongly log-concave measures.
Corollary 5.6(A Logarithmic Sobolev inequality).Letµbe an even strongly
log-concave probability measure onR n. Then,
4D(µ∥γ)≤2n

e
2
nD(µ∥γ)−1

≤I(µ∥γ).(76)
28 GAUTAM AISHWARYA AND LIRAN ROTEM
Proof.We square both sides of Equation (72) to obtain
e
2
nD(µ∥γ)≤c(W 2(µ,γ)) 2+ 2
n s(W2(µ,γ))c(W 2(µ,γ))
p
I(µ∥γ)+ 1
n2 s(W2(µ,γ)) 2I(µ|γ).
(77)
The inequality 2ab≤2a 2 + 1
2b2 applied toa=s/ √n,b=c
p
I(µ∥γ)/n, gives
e
2
nD(µ∥γ)≤

c(W2(µ,γ)) 2 + 2
n s(W2(µ,γ)) 2

1 + 1
2nI(µ∥γ)

.(78)
Now the identityc 2 + 2
n s2 = 1 allows us to conclude the second inequality
in the assertion. The first inequality, which compares our result with a
Logarithmic Sobolev inequality in a more standard form, follows from the
inequalitye x−1≥x.□
Remark 5.7.The Gaussian measure satisfies a Logarithmic Sobolev in-
equality with constant 1, that is,D(µ∥γ)≤ C
2I(µ∥γ),C= 1, without sym-
metry or concavity assumptions onµ. Moreover, Bobkov, Gozlan, Roberto
and Samson’s result from [8] implies that ifµis strongly log-concave and
centered, we already haven

e
2
nD(µ∥γ)−1

≤I(µ∥γ) – See Corollary 2.2
there and note that indeedb≤1 in this setting by Poincar´ e. Corollary
5.6 says that, for even strongly log-concave measures, both of these results
improve by a factor of 2. It is well known that the Poincar´ e constant of the
Gaussian measure improves to 1/2 for even functions. Given the relationship
between Logarithmic Sobolev inequalities (stronger) and Poincar´ e inequali-
ties (weaker), one may wonder if Corollary 5.6 can be strengthened to hold
for all even measures. However, this is not the case; the improvement by a
factor of 2 in the Gaussian Poincar´ e inequality for even functions cannot be
lifted to the same improvement in the Logarithmic Sobolev inequality for
even measures without further assumptions, as the following example shows.
Example 5.8.Letµdenote the distribution oftZ, whereZhas the dis-
tribution of standard Gaussian inR. Then, all quantities involved can be
explicitly computed,
D(µ∥γ) =−logt+ t2
2− 1
2,andI(µ∥γ) = (t2−1) 2
t2 .(79)
Ast7→∞, we have 4D(µ∥γ)
t2 →2 but I(µ∥γ)
t2 →1. On the other hand, taking
the limitt→1 shows that our inequality is sharp.
The improvement in the Logarithmic Sobolev inequality for even strongly
log-concave measures also reflects in the convergence rate to equilibrium.
Corollary 5.9.LetP ∗
tµdenote the Ornstein-Uhlenbeck evolution of an even
strongly log-concave measureµ=µ 0, that is,dP ∗
tµ=P t

dµ
dγ

dγ. Here
Pt denotes the Ornstein-Uhlenbeck semigroup. Then,
D(P∗
tµ∥γ)≤e −4tD(µ0∥γ).(80)
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 29
Proof sketch.The proof is a standard argument using the facts that d
dtD(P∗
tµ∥γ) =
−I(P∗
tµ∥γ), and that the Ornstein-Uhlenbeck semigroupP t (which acts on
functions) preserves the class of even functions as well as the class of log-
concave functions.□
Remark 5.10.The previous proof uses only the dimension-free part 4D(µ∥γ)≤
I(µ∥γ) in Corollary 5.6. One can use the dimensional dependence avail-
able. However, this really improves the inequality only for short timest.
Long-term behavior seems to be dominated by the “curvature” aspect. The
interested reader may also consult [4].
We conclude this section with another typical application of the HWI
inequality.
Corollary 5.11(A Talagrand inequality).Letµbe an even strongly log-
concave probability measure onR n. Then,
W 2
2 (µ,γ)≤−nlog cos
 r
2
n W2(µ,γ)
!
≤D(µ∥γ).(81)
Proof.This follows from plugging inγ=µ 0 andµ=µ 1 in the HWI In-
equality (71), which makesI(µ 0) = 0.□
Remark 5.12.The Gaussian measure satisfiesW 2
2 (µ,γ)≤2D(µ∥γ) for
all probability measuresµ. Since the Gaussian Talagrand inequality is also
stronger than the Poincar´ e inequality ([38, Section 7]), one may again con-
sider the possibility that Corollary 5.11 holds for all even measures. How-
ever, again, this is not the case. The example presented in the case of the
Logarithmic Sobolev inequality serves us here as well.
Example 5.13.Letµdenote the distribution oftZ, whereZhas the dis-
tribution of standard Gaussian inR. Then,
W 2
2 (µ,γ) = (t−1) 2,andD(µ∥γ) =−logt+ t2
2− 1
2.(82)
Ast→∞, we have W 2
2 (µ,γ)
t2 →1 but D(µ∥γ)
t2 → 1
2. On the other hand, as
before, takingt→1 shows that our inequality is sharp.
