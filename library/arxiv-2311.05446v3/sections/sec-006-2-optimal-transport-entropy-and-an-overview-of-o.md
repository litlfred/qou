---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-006-2-optimal-transport-entropy-and-an-overview-of-o
section_title: "Optimal transport, entropy, and an overview of our method"
section_number: 2
pages: 8-13
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
While the general problem of optimal transport can be posed in a much
more abstract setting, we will focus on the setup relevant for our purpose,
namely the optimal transport problem inRn with quadratic cost. For details
beyond the short treatment we present below, the reader is referred to the
excellent textbook [47], especially Chapters 2 and 5.
Forµ 0,µ 1∈P 2(Rn), denote by Π(µ 0,µ 1) the collection of all couplings
betweenµ 0 andµ 1. This means, Π(µ 0,µ 1) consists of probability measures
π∈P(R n×Rn) such that,
π(A×R n) =µ 0(A), π(Rn×B) =µ 1(B),(16)
for all Borel setsA,B⊆R n. IfX 0,X 1 areR n-valued random vectors with
distributionsµ 0,µ 1, respectively, then Π(µ 0,µ 1) is the collection of all pos-
sible joint distributions for (X 0,X 1).
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 9
The optimal transport problem, with quadratic cost, asks to minimize
I[π] =
Z
|x−y| 2 dπ(x,y),(17)
over allπ∈Π(µ 0,µ 1). This models the situation where mass distributed
according toµ 0 in space is to be displaced to mass distributed according to
µ1, where|x−y| 2 is the cost of moving a unit mass from the pointxto the
pointy. A couplingπrepresents a plan, where the infinitesimal dπ(x,y)
is the amount of mass to be moved fromxtoy. The problem then asks to
compute the cheapest way to displaceµ 0 toµ 1.
The optimal cost,
W2(µ0,µ 1) =

inf
π∈Π(µ0,µ1)
Z
|x−y| 2 dπ(x,y)
1/2
,(18)
called theWasserstein distance of order2 betweenµ 0 andµ 1, is in fact a
metric onP 2(Rn). The resulting metric space is called the 2-Wasserstein
space overRn, denotedW 2(Rn). The Wasserstein space overRn is a geodesic
space, that is, every two points can be connected by a continuous path
c: [0,1]→W 2(Rn) such that,W 2(c(s),c(t)) =|t−s|W 2(c(0),c(1)) for any
intermediate timess,t∈[0,1]. Every optimal couplingπ∈Π(µ 0,µ 1) gives
rise to a geodesic viac π(t) = (σ t)#π, whereσ t : (x,y)7→(1−t)x+ty.
Notions related to geodesic-convexity inW 2(Rn) are given special names, as
in the definition below.
Definition 2.1.
(1) A subsetS⊆W 2(Rn) is called adisplacement convex set, if given
any two measuresµ 0,µ 1∈S,
n
(σt)#π:W 2
2 (µ0,µ 1) =
Z
|x−y| 2 dπ(x,y),t∈[0,1]
o
⊆S.(19)
(2) A mapF:S→R∪{+∞}is called adisplacement convex functional
if the mapt7→F((σ t)#π) is convex on [0,1], for everyπsuch that
W 2
2 (µ0,µ 1) =
R
|x−y| 2 dπ(x,y). Similarly,Fis calleddisplacement
concaveif−Fis a displacement convex functional.
(3) If there is a unique constant-speed geodesic{µ t}t∈[0,1] fromµ 0 toµ 1,
then it is called thedisplacement interpolationbetweenµ 0 andµ 1,
and eachµ t is called adisplacement interpolant.
The geodesically convex subsetP 2,ac(Rn)⊆W 2(Rn) is uniquely geodesic.
This is facilitated by a theorem of Brenier ([15]), which ensures a unique
solution to optimal transport problem ifµ 0 has density, and describes the
structure of the optimal coupling.
Theorem 2.2.[47, Theorem 2.12 (ii)]Letµ 0,µ 1 ∈ P2(Rn). Ifµ 0 ∈
P2,ac(Rn)in addition, then there exists a unique convex functionϕsuch
that,T=∇ϕpushes forwardµ 0 toµ 1. Moreover, in this case the opti-
mal coupling in the optimal transport problem is unique, and is given by
π= [x7→(x,T(x))] #µ0.
10 GAUTAM AISHWARYA AND LIRAN ROTEM
The mapTin the above theorem is called theBrenier map fromµ 0 toµ 1.
If the conditions of the above theorem are met, then we can explicitly write
the displacement interpolant betweenµ0 andµ 1 asµt = (Tt)#µ0, whereTt =
(1−t)I+tTlinearly interpolates between the identity map and the Brenier
map fromµ 0 toµ 1. This interpolation was introduced in the pioneering
work of McCann ([36]), where the fact that the Jacobian matrix of the
transport mapsT t takes values in the space of positive semidefinite matrices
proved to be useful in establishing displacement convexity properties of some
important functionals. For example, [36, Theorem 2.2] contains the following
functionals as special cases.
Example 2.3.TheShannon–Boltzmann entropyh(µ) =−
R
dµ
dx

log

dµ
dx

dx
onP 2,ac(Rn) is displacement concave. In fact, this functional can be mean-
ingfully extended to all ofW 2(Rn) by settingh(µ) =−∞, whenµdoes not
have density with respect to the Lebesgue measure.
Example 2.4.Theexponentiated R´ enyi entropyA(µ) =e
1
nh(n−1)/n(µ) :=
R
dµ
dx
1− 1
n
dxis displacement concave.
Much later, in a considerably broader framework than we need here, Ex-
ample 2.3 was strengthened by Erbar, Kuwada, and Sturm ([21]) in the form
below.
Example 2.5.The exponentiated entropye h(µ)/n is displacement concave
onW 2(Rn).
Since support(µt)⊆(1−t)support(µ 0) +tsupport(µ1), displacement con-
cavity can be used to obtain sumset inequalities for geometric quantities
that admit a variational interpretation in terms of probability measures.
For example, ifK⊆R n is a compact set, then
sup
µ∈Pac(K)
h(µ) = log Voln(K),sup
µ∈Pac(K)
A(µ) = Voln(K)1/n.(20)
The upper-bounds implicit in both these formulas can be proved by a straight-
forward application of Jensen’s inequality, then one can check that these
upper-bounds are attained by the uniform distribution onK, leading to the
variational expressions above. SupposeK 0 andK 1 are compact subsets of
Rn. Then, Example 2.3 implies the 0-concavity of the Lebesgue measure,
while Example 2.4 and Example 2.5 imply the (a priori superior) (1/n)-
concavity of the Lebesgue measure.
In this paper, we appropriately generalize Example 2.5. To lift the frame-
work above to deal with an arbitrary reference measure instead of the
Lebesgue measure, we now introduce a way to measure entropy with re-
spect to a reference measure.
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 11
Definition 2.6(Relative entropy).Letνbe aσ-additive Borel measure on
Rn. We define the following functional onW 2(Rn),
D(µ∥ν) =
(R
dµ
dν

log

dµ
dν

dν,ifµhas density w.r.t.ν,
+∞,otherwise,
(21)
called therelative entropy ofµwith respect toν.
Remark 2.7.The relative entropyD(µ∥ν) is a quantification of how much
µis “spread out” from the viewpoint ofν. InR n, we get an absolute measure
of spread by looking at negative the amountµis spread out from the most
spread out measure Voln,h(µ) =−D(µ∥Vol n).
UsingD(·∥ν), one can obtain a variational formulation of theν-measure,
exactly as in the case of the Shannon–Boltzmann entropy and volume.
Lemma 2.8.LetK⊆R n be a compact set, then
inf
µ∈P(K)
D(µ∥ν) =−logν(K),(22)
where the supremum is attained byν K.
Proof.LetXbe anR n-valued random vector with distributionµ∈P(K).
Because of the way relative entropy is defined, we only need to consider mea-
suresµhaving density, sayf, with respect toν. Using Jensen’s inequality
we obtain,
−D(µ∥ν) =−
Z
flogfdν=Elog 1
f(X) ≤logE 1
f(X) ≤logν(K).(23)
The bound is attained whenfis constant, that is, whenµ=ν K. This can
be verified directly.□
Therefore, we have the following general principle formalizing our method.
Proposition 2.9.Letνbe aσ-finite Borel measure onR n. SupposeS⊆
W2(Rn)is a displacement convex set containingν K, for all compact sets in
a classKof compact subsets ofR n. Ife −aD(·∥ν) is displacement concave on
S,a>0, then
ν((1−t)K 0 +tK 1)a≥(1−t)ν(K 0)a +tν(K 1)a,(24)
for allK 0,K 1∈K.
Proof.In the assumed displacement concavity inequality
e−aD(µt∥ν)≥(1−t)e −aD(µ0∥ν) +e−aD(µ1∥ν),(25)
we plug inµ 0 =ν K0,µ 1 =ν K1. Since support(µ t)⊆(1−t)K 0 +tK 1, we
havee−aD(µt∥ν)≤ν((1−t)K 0 +tK 1)a which concludes the proof.□
12 GAUTAM AISHWARYA AND LIRAN ROTEM
Remark 2.10.Whene −aD(·∥ν),a >0, is displacement concave on all of
W2(Rn), we get thea-concavity of the measureν. In this case, the converse
is also true thereby extending Borell’s characterization (Theorem 1.1). This
is contained, rather implicitly, in the work of Erbar, Kuwada, and Sturm
([21]). The corresponding statement fora= 0, namely the equivalence
between displacement convexity ofD(·∥ν) and log-concavity ofν, had been
known earlier (see, for example [1, Theorem 9.4.11]).
Remark 2.11.The displacement concavity property ofe−aD(·∥ν) onW 2(Rn),
in the language of [21], is called theentropicCD(0,1/a)conditionfor the
metric measure space (R n,∥·∥ 2,ν). In this expression, “CD” stands for
curvature-dimension. Given that a Riemannian manifold (equipped with its
volume measure) has Ricci curvature bounded below by someκ∈Rand
its dimension is at mostn, several geometric and functional inequalities (in
terms ofκandn) follow. The curvature-dimension condition for Markov
diffusions, introduced in the work of Bakry– ´Emery [3], allows one to de-
fine the notion of “Ricci curvature bounded below byκ, dimension bounded
above byn” for weighted Riemannian manifolds (that is, Riemannian man-
ifolds equipped with a measure that is not necessarily the volume measure)
admitting consequences akin to the non-weighted case. On the other hand,
starting from the work of McCann [36], through the papers of Otto–Villani
[38], Cordero-Erausquin–McCann–Schmuckenschl¨ ager [19], it was eventually
established in the work of von Renesse–Sturm [49] that the “Ricci curvature
bounded below byκ” condition on weighted Riemannian manifolds could
equivalently be described using the displacementκ-convexity of relative en-
tropy on the 2-Wasserstein space over the Riemannian manifold. In the
landmark papers of Sturm [44, 45] and Lott–Villani [35], not only were di-
mensional considerations added (using R´ enyi entropy) to complete the pic-
ture on the displacement convexity-based alternative to the Bakry– ´Emery
approach to curvature-dimension in the weighted Riemannian setting, but
the natural extension of this theory to a wide class of metric measure spaces
was established and explored. In the setting of (infinitesimally Hilbertian)
metric measure spaces, the equivalence between the two approaches was es-
tablished by Erbar–Kuwada–Sturm [21], in which the authors introduce and
study the (κ,n)-convexity(see Definition 4.4) of relative entropy on Wasser-
stein space. Particularly, in the setting of the Euclidean space equipped
with a measure dν=e −V dx, the (κ,n)-convexity ofD(·∥ν) onW 2(Rn) is
equivalent to theCD(κ,n) condition defined in terms of the displacement
convexity of (relative) R´ enyi entropy (perhaps better known as R´ enyi di-
vergence among information theorists), which is further equivalent to the
Bakry–´Emery definition ofCD(κ,n) condition for the Markov semigroup
generated byLf= ∆f−⟨∇V,f⟩. However, such equivalences need not
hold over specific choices of Wasserstein geodesics. In the present work, our
choice of using exponentiated relative entropy instead of the exponentiated
R´ enyi divergence plays a key role.
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 13
Sometimes, to prove the displacement convexity properties of certain func-
tionals it is useful to take an “Eulerian viewpoint”. Forµ 0,µ 1∈P 2,ac(Rn),
consider the transport mapsT t as in the discussion preceding Example 2.3.
The previous description of the mapsT t expresses the displacement in terms
of the particle trajectoriesT t(x), of each particlex; this is the “Lagrangian
viewpoint”. One can equivalently describe the displacement in terms of a
time-dependent vector fieldv t such that,
vt(Tt(x)) = d
dtTt(x).(26)
The reason whyv t can be defined in the above manner is that trajectories
in optimal transport do not cross (in an almost-everywhere sense). Further,
an argument based on the dominated convergence theorem leads to the
continuity equation,
d
dt
Z
ϕdµ t =
Z
⟨∇ϕ,vt⟩dµ t,(27)
for all test functionsϕ. It can be shown thatv t is of the form∇θ t, andθ t
satisfies a Hamilton–Jacobi equation in the weak sense,
∂θt
∂t +|∇θt|2
2 = 0.(28)
Roughly speaking, the fact thatv t is a gradient field follows from Brenier’s
theorem and semigroup properties of optimal transport, while the Hamilton–
Jacobi equation is a consequence ofTt carrying each particle along a straight
line. For more details, the reader is referred to [47, Section 5.4].
