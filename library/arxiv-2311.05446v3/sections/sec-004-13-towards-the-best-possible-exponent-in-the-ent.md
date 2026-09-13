---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-004-13-towards-the-best-possible-exponent-in-the-ent
section_title: "Towards the best possible exponent in the entropy inequality"
section_number: 1.3
pages: 5-8
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
As mentioned, Theorem 1.3 implies the Kolesnikov-Livshyts inequality (4),
but not the result of Eskenazis–Moschidis with the optimal exponent 1
n.
Since this result is known to be true, one can hope for a version of Theorem
1.4 that will imply it, that is, a version with the sharp coefficient 1
n, under
suitable assumptions on the potentialVand the measuresµ 0 andµ 1.
One natural way to approach this problem is to perform the local analysis
directly onD(·∥ν) instead of splitting it to two components. Indeed, the con-
cavity ofe −aD(µt∥ν) along a displacement interpolation{µ t}t∈[0,1] amounts
to the inequality
d2
dt2D(µt∥ν)≥a
 d
dtD(µt∥ν)
2
.(9)
As we will see later, both sides of the above inequality can be explicitly
written in terms of certain differential operators applied to the velocity field
driving the optimal transport. This leaves us with an inequality of almost
the same form as the sufficiency criteria of Kolesnikov–Livshyts discussed
earlier. In the case ofν=γ, an auxiliary construction from [22] allows us
to prove the following theorem:
Theorem 1.5.Suppose{µ t}t∈[0,1] is a displacement interpolation such that
eachµ t is even and satisfies the odd Poinc´ are inequality with constant1,
that is
R
f 2 dµt≤
R
|∇f| 2 dµ, for every odd test functionf. Then,
d2
dt2D(µt∥γ)≥2W 2
2 (µ0,µ 1) + 1
n
 d
dtD(µt∥γ)
2
,(10)
whereW 2(µ0,µ 1)denotes the2-Wasserstein metric (induced by the optimal
transport problem).
Thus, as readers familiar with the curvature-dimension framework may
notice, under these assumptions on theµ t, not only can the “dimensional”
improvement to 1
n be obtained, but the “curvature” also improves to 2. Note
that, without any restrictions on theµt, d2
dt2D(µt∥γ)≥W 2
2 (µ0,µ 1) is always
true, which is reflective of the fact that Gauss space satisfies properties akin
to a complete Riemannian manifold with Ricci curvature lower bounded by
the metric tensor.
WhenKis a convex body, then the density ofν K with respect toνis
a log-concave function. This is the property ofν K that typically expresses
itself in extensions of various phenomena from the geometry of sets to the
6 GAUTAM AISHWARYA AND LIRAN ROTEM
geometry of measures. Whenνis the Gaussian measureγ, measures hav-
ing a log-concave density with respect toγare called strongly log-concave
measures. Given that the Gaussian measure satisfies a Brunn–Minkowski
inequality with exponent 1
n over origin-symmetric convex bodies, it is a nat-
ural question whether displacement interpolation between two even strongly
log-concave probability measures satisfies the assumptions of Theorem 1.5.
Question 1.6.Supposeµ 0,µ 1 are even strongly log-concave probability
measures onR n. Let{µ t}t∈[0,1] denote the displacement interpolation be-
tweenµ 0 andµ 1. Is it true that eachµ t,t∈(0,1), satisfies the Poinc´ are
inequality for odd functions with constant 1?
Note that the Brascamp–Lieb inequality ([13, Theorem 4.1]) guarantees
thatµ 0 andµ 1 in the above setup satisfy a Poinc´ are inequality with con-
stant 1 for all functions. Also note, that a positive answer to Question
1.6, combined with our Theorem 1.5, would yield an entropic proof of the
Eskenazis–Moschidis result. We show that Question 1.6 has an affirmative
answer in several cases, namely when the dimension of the ambient space
is one, or when bothµ 0 andµ 1 are themselves Gaussian measures, or when
one of{µ 0,µ 1}is the standard Gaussianγ.
1.4.Functional Inequalities.While we cannot answer Question 1.6 in full
generality, the case whereµ 0 orµ 1 isγitself does suffice to prove several
fundamental functional inequalities.
The HWI inequality, originally introduced by Otto and Villani in [38], as-
serts a relationship between the three elemental quantities—D(·∥γ),W2(·,γ),
andI(·∥γ). The “H” in HWI stands for relative entropy (as it is sometimes
denoted), “W” is for the Wasserstein distance, and “I” for Fisher infor-
mation. Recall that, ifP ∗
sµdenotes the evolution of the measureµunder
the Ornstein–Uhlenbeck process at times, then the Fisher information is
I(µ∥γ) =− d
dsD(P∗
sµ∥γ)

s=0. Using the methods from [21], we obtain the
following strengthening of the Gaussian HWI inequality for even strongly
log-concave measures as a consequence of our results.
Theorem 1.7(An HWI inequality).Letµbe an even strongly log-concave
probability measure onR n. Suppose{µ 0,µ 1}={µ,γ}. Then,
e
D(µ0∥γ)
n −D(µ1∥γ)
n ≤cos
 r
2
n W2(µ0,µ 1)
!
+ 1√
2n sin
 r
2
n W2(µ0,µ 1)
!
p
I(µ0∥γ).
(11)
The original HWI inequality of Otto–Villani ([38, Theorem 3]) for the
Gaussian measure, which is valid without symmetry or log-concavity as-
sumptions onµ, states that
D(µ0∥γ)−D(µ 1∥γ)≤W 2(µ0,µ 1)
p
I(µ0∥γ)− 1
2 W 2
2 (µ0,µ 1).(12)
To compare our inequality (11) with the original HWI inequality (12), the
reader may raise both sides of (11) to the powernand sendn→∞. A
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 7
key feature of HWI type inequalities, perhaps even the motivation behind
it in [38], is that they unify two other important families of inequalities.
At one end, by settingµ 0 =µandµ 1 =γin Theorem 1.7, after some el-
ementary manipulations, we get a refinement of the Gaussian Logarithmic
Sobolev inequality. Although first popularized in the mathematical com-
munity through a contribution of Gross ([27]), the Gaussian Logarithmic
Sobolev inequality had previously appeared in the work of Federbush ([24])
and even earlier as an information-theoretic uncertainty principle by Stam
([43]).
Corollary 1.8(A Logarithmic Sobolev inequality with an application).Let
µbe an even strongly log-concave probability measure onR n. Then,
4D(µ∥γ)≤2n

e
2
nD(µ∥γ)−1

≤I(µ∥γ).(13)
Therefore,
D(P∗
tµ∥γ)≤e −4tD(µ0∥γ).(14)
On the other hand, withµ 0 =γandµ 1 =µ, the transportation cost-
information inequality of Talagrand ([46]) is improved for even strongly log-
concave probability measures.
Corollary 1.9(A Talagrand inequality).Letµbe an even strongly log-
concave probability measure onR n. Then,
W 2
2 (µ,γ)≤−nlog cos
 r
2
n W2(µ,γ)
!
≤D(µ∥γ).(15)
The original inequalities assert 2D(µ∥γ)≤I(µ∥γ) and 1
2 W 2
2 (µ,γ)≤
D(µ∥γ), respectively, for all probability measuresµ. Thus, even if we com-
pletely ignore the dimensional improvements that we have obtained, both
the Gaussian Logarithmic Sobolev and the Talagrand inequalities show an
improvement by a multiplicative factor of 2 when restricted to even strongly
log-concave measures. From examples presented in the main body of the text
(see Examples 5.8 and 5.13), the reader will see that both assumptions—
central symmetry and strong log-concavity of the measure, are essential for
this improvement. Dimensional improvements in Gaussian functional in-
equalities have been pursued before, for example, in the works of Bakry
and Ledoux ([7]), Bobkov, Gozlan, Roberto, and Samson ([8]), and more re-
cently, Bolley, Gentil, and Guillin ([9]). However, none of these results gives
the multiplicative improvement we get by restricting to even strongly log-
concave measures. Readers interested in dimension-dependent functional
inequalities may also consult [4, 5, 23, 42].
The rest of this paper is organized as follows. In Section 2 we give the
necessary background on optimal transport and describe the previous works
on displacement concavity of entropy. In Section 3 we give the relatively
short proofs of Theorems 1.3 and 1.4.
8 GAUTAM AISHWARYA AND LIRAN ROTEM
Then, in Section 4 we restrict our attention to the caseν=γ, to dis-
cuss potential improvements to convexity properties ofD(·∥γ) beyond those
established in Section 3. In particular we prove Theorem 1.5. Finally, in
Section 5 we apply our findings from the previous section to prove functional
inequalities such as Theorem 1.7 and its corollaries.
