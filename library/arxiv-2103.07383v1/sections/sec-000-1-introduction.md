---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
An easy way to produce a knot is to tie a piece of string and glue the ends together. This
motivates the mathematical deﬁnition of a knot as a continuous embedding of a circle into three-
dimensional Euclidean space. Depending on the initial knotting, diﬀerent knot types arise. We
say that two knots are of the same knot class if there exists an ambient isotopy [Cro04, p. 4f.]
that deforms one knot to the other avoiding any sort of self-intersections or “cutting and glueing”
phenomena. In the following we aim to investigate the regularity of optimal shapes for knots
within their knot classes.
Lead by the question of determining optimal representatives for given polygonal knot classes,
Fukuhara [Fuk88] introduced the idea to apply some sort of self-repelling potentials to given
2020 Mathematics Subject Classiﬁcation.35A20, 35A10, 35B65, 57K10
Key words and phrases.Analyticity, knot energy, generalized integral Menger curvature, method of majorants,
fractional Leibniz rule, bootstrapping.
1
arXiv:2103.07383v1  [math.AP]  12 Mar 2021
knots and follow their gradient ﬂow towards the local minimizer. Based on that concept, O’Hara
later established the notion of knot energies by deﬁning them as real-valued functionals on the
space of knots that are bounded from below and self-repulsive, i.e. the energy blows up on a
sequence of knots that converges to a curve with self-intersections [O’H03].
O’Hara was also the ﬁrst to suggest such a potential knot energy for actual knots [O’H91],
motivatedfromtheelectrostaticpotentialenergy, inparticulartheself-avoidanceeﬀectsdescribed
by Coulomb’s law. Later, this energy was named Möbius energy due to its invariance with respect
to Möbius transformations shown by Freedman, He and Wang [FHW94].
Motivated by applications to molecular biology, Gonzalez and Maddocks elaborated a com-
pletely diﬀerent approach to deﬁne knot energies in search of a new notion for thickness of knots
[GM99]. For any continuous, closed, and rectiﬁable curveγ: R/Z→R3, where R/Z∼= S1
denotes the circle of length 1, they characterized the thickness ofγby
∆(γ) = inf
x,y,z∈γ
R(x,y,z ),
where R(x,y,z ) stands for unique circumcircle radius of three pointsx,y,z ∈Rn given by
R(x,y,z ) =|y−z||y−x||z−x|
2|(y−x)∧(z−x)|= |y−z|
2 sin∡(y−x,z−x).
Observe that ∆(γ) = 0 if γintersects itself. Therefore, the quotientL(γ)/∆(γ) of lengthL(γ)
over thickness ∆(γ) called ropelength serves as a starting point for new self-repelling potential
energies. We remark that thickness is related to the local radius of curvature since the circum-
circle of three pointsx,y,z on a suﬃciently regular curveγconverges to the osculating circle at
x for y and z converging tox on γ. The radius of the osculating circle atx on γis the inverse
of the local curvature.
The ropelength imposes technical challenges as it consists of operators that are hard to
diﬀerentiate. These drawbacks can be softened as suggested in [GM99] by exchanging point-wise
maximization with integration, which leads to variousintegral Menger1 curvature energiessuch
as
Mp(γ) =

(R/Z)3
|γ′(r)||γ′(s)||γ′(t)|
R(γ(r),γ(s),γ(t))p dr ds dt. (1)
for anyp> 0. Note that for curves parametrized by arc-lengthlimp→∞M1/p
p (γ) = 1
∆(γ). Other
variants between ropelength andMp can be found in [GM99].
For p > 3, these functionals are indeed knot energies according to O’Hara’s deﬁnition, as
Strzelecki, Szumańska and von der Mosel showed in [SSvdM13]. Furthermore, they proved a
geometric Morrey-Sobolev imbedding in three dimensions, in particular that ﬁnite energy of an
arc-length parametrized curve impliesC1,1−3
p-regularity and its image isC1-diﬀeomorphic to the
circle [SSvdM10]. Blatt completed the characterization of energy spaces in [Bla13]. Generaliza-
tions of the integral Menger curvature to higher-dimensional objects can be found for example
in [SvdM11, BK12, Kol14]. For further information on the integral Menger curvature energies
we refer the reader for example to the survey paper [SvdM13].
In order to tackle the main question of the present paper, the regularity of optimal shapes
for knots, we ﬁrst need to choose a suitable knot energy and then conduct regularity studies on
its stationary points. Now if we chose for this purpose the integral Menger curvature energies
1Named after the Austrian-American mathematician Karl Menger (1902-1985) who used the radius of circum-
scribed circles on a curve to generalize the concept of curvature to metric spaces [Men30]
2
Mp,p> 3, we would arrive at nonlinear, non-local and degenerate Euler-Lagrange operators. A
formula for the ﬁrst variation can be found in [Her12] and for its second and third variation in
[Kna20]. Hence, to produce non-degenerate energies from the integral Menger curvature energies
given in (1), Blatt and Reiter [BR15] suggested to generalizeMp to
intM(p,q)(γ) =

(R/Z)3
|γ′(u1)||γ′(u2)||γ′(u3)|
R(p,q)(γ(u1),γ(u2),γ(u3)) du1 du2 du3, (2)
where they decoupled the circumcircle radius to
R(p,q)(x,y,z ) = (|y−z||y−x||z−x|)p
|(y−x)∧(z−x)|q =|y−z|p|y−x|p−q|z−x|p−q
sin ∡(y−x,z−x)q
for anyp,q > 0. Observe thatMp(γ) = 2pintM(p,p)(γ). According to [BR15], these energies
are well-deﬁned knot energies forp≥2
3q + 1 and give ﬁnite energy values on closed curves for
p<q + 2
3. Moreover, minimizers exist within every knot class forp∈( 2
3q + 1,q + 2
3) and q >1.
For the particular case q = 2 and therefore p ∈( 7
3, 8
3), the generalized integral Menger
curvature energies in (2) indeed lead to non-degenerate Euler-Lagrange equations, for which
Blatt and Reiter proved the following regularity result by a combination of potential estimates
and Sobolev-embeddings.
Theorem 1.1. [BR15, Theorem 4] Forp∈( 7
3, 8
3), let γ: R/Z→Rn be a simple curve in
W
3
2p−2,2(R/Z, Rn) parametrized by arc-length. Ifγis a stationary point of the generalized integral
Menger curvature intM(p,2) with respect to ﬁxed length, thenγ∈C∞(R/Z, Rn).
Furthermore, Blatt and Reiter characterizedC1-curves of ﬁnite generalized integral Menger
curvature energy by curves in the fractional Sobolev spaceW
3p−2
q −1,q(R/Z, Rn) [BR15, Theo-
rem 1]. This result, combined with Theorem 1.1, raises the question whether stationary points
of ﬁnite generalized integral Menger curvature energies are not only smooth but also analytic.
For the Möbius energy the statement was elaborated by [BV19] based on the corresponding
smoothnessresultestablishedby[BRS16]. Thesameholdsforanon-degeneraterangeofO’Hara’s
energies as shown in [Vor20] based on [BR13]. Hence it seems reasonable that it is possible to
transfer the techniques to the non-degenerate range of energiesintM(p,2) for p∈( 7
3, 8
3).
The main method used in these papers to show analyticity is based on the method of ma-
jorants, motivated by the proof of Cauchy-Kovalevsky’s theorem [Kov1875], see also [Cau1882,
pp. 17–33]. For applying this technique, it is necessary to establish a recursive estimate for
derivatives of critical curves. It turns out that in such estimates, there appears a fractional
derivative of the product of two functions, which subsequently leads to a fractional Leibniz rule.
Unfortunately, in contrast to the bilinear Hilbert transform in [BV19] and fractional Leibniz rule
in [Vor20], in our case this recursive estimate does not produce a suﬃcient diﬀerence in the order
of diﬀerentiability, which is why we repeat it to obtain a diﬀerence of order1. This repetition
seems to lead to Gevrey regularity of order2 for critical curves, which is weaker than analyticity,
cf. [KP02, Deﬁniton 4.1.19] or [Rod93, Chapter 1.4], but we are able to conﬁrm the analyticity
in the aﬃrmative:
Theorem 1.2. Forp∈( 7
3, 8
3), letγ: R/Z→Rn be a simple curve inC∞(R/Z, Rn) parametrized
by arc-length. Ifγis a critical point of the generalized integral Menger curvatureintM(p,2) with
respect to ﬁxed length, then the curveγis analytic.
3
A closer look at the proof of the main theorem reveals that smoothness ofγis actually not
needed. It suﬃces to assume that‖γ(i)‖H
5
2
is ﬁnite fori∈{0, 1, 2}, i.e. γ∈H4+ 1
2 (R/Z, Rn).
All additional regularity is obtained by an inductive argument.
However, by the characterization of the energy spaces in [BR15, Theorem 1] and the regularity
result Theorem 1.1, ﬁnite energyintM(p,2) of a critical point implies its smoothness already. We
conclude:
Corollary 1.3. Letγ: R/Z→Rn be a simple curve inC1(R/Z, Rn) parametrized by arc-length
with intM(p,2)(γ) <∞for p∈( 7
3, 8
3). If γis a critical point ofintM(p,2) with respect to ﬁxed
length, then the curveγis analytic.
One should be able to drop theC1-assumption in the previous result by obtaining suﬃcient
initial regularity via techniques that proved to be successful in showing a geometric Morrey-
Sobolev imbedding forMp with p> 3, cf. [SSvdM10, Theorem 1.2].
Further analyticity and Gevrey regularity results in the context of non-local diﬀerential equa-
tions can be found for example in [DFSS12, DFSS14, AFV15, Bla20a, Bla20b].
Exposé of the present work
As stated above, the central idea of our proof is the same as in the one for the Cauchy-Kovalevsky
theoremandgoesasfollows. Acurve γ∈C∞(R/Z, Rn)isanalyticifandonlyifwehaveconstants
C >0 and r> 0 such that for alll∈N0
‖γ(l)‖L∞≤Cl!
rl.
Suppose we had a recursive estimate
‖γ(l+1)‖L∞≤Φ(l;‖γ‖L∞,...,‖γ(l)‖L∞)
and an analytic functionc : (−ε,ε)→R with
c(l+1)(0) = Φ(l;c(0),...,c (l)(0)) and c(0)≥‖γ‖L∞.
Then, by induction,
0≤‖γ(l+1)‖L∞≤Φ(l + 1;c(0),...,c (l)(0)) =c(l+1)(0)≤C (l + 1)!
rl+1
for alll∈N and so,γis analytic.
The largest part is devoted to obtaining the required recursive estimate. In Section 2, we
review a decomposition of the ﬁrst variation ofintM(p,2) given in [BR15, Section 4] into a highest-
and lower-order terms called⟨Q(p) and ⟨R(p). In a critical point,⟨Q(p) is equal to−⟨R(p) and we
may use the regularity gap between those to establish the recursive estimate. To that end,
Section 3 yields an estimate of∂l+3γby ∂l⟨Q(p)(γ). In Section 4 we bound∂l⟨R(p)(γ) by ∂l+2γ
via a fractional Leibniz rule. Looking at the norms involved, it turns out that these estimates
combined only lead to a regularity gain strictly between1
2 and 1 which is not enough for the
recursive estimate, so in Subsection 5.1, we iterate the above once more using the fact thatγ
is a critical point. The remainder of Section 5 is dedicated to ﬁnding the analytic majorantc
which fulﬁls the same recursive estimate with equality. Finally, Section 6 discusses a few simple
consequences of the analyticity of critical points, not only forintM(p,2), in geometric knot theory.
We expect that our approach extends to functionals whose ﬁrst variation admits a decompo-
sition with properties similar to those of⟨Q(p) and ⟨R(p). A probably valid generalization would
be to assume only an arbitrarily small gain in regularity, see page 23.
4
Notation
In the following we give a short introduction to the fractional Sobolev spaces we are using in
this paper. First, we present a continuation of the usual periodic Sobolev spaces of integer order
Wk,p(R/Z, Rn) to Sobolev–Slobodeckij spacesWk+s,p(R/Z, Rn) for 0 < s <1. The latter are
deﬁned by
Wk+s,p(R/Z, Rn) :={f∈Wk,p(R/Z, Rn)|[f(k)]W s,p(R/Z,Rn) <∞}
equipped with the norm
‖f‖W k+s,p(R/Z,Rn) :=‖f‖k,p
W (R/Z, Rn) + [f(k)]W s,p(R/Z,Rn),
where
[f(k)]W s,p(R/Z,Rn) :=
(
R/Z
1/2
−1/2
|f(k)(x)−f(k)(y)|p
|x−y|1+ps dx dy
{1
p
is the so-called Gagliardo seminorm ofk-th derivative off.
Second, we consider Bessel potential spaces of orders≥0 on the circleR/Z that are given
by
Hs(R/Z, Cn) :={f∈L2(R/Z, Cn)|‖f‖H s :=‖f‖H s(R/Z,Cn) :=
⨂
(f,f )H s <∞},
equipped with the inner product
(f,g )H s := (f,g )H s(R/Z,Cn) :=
∑
k∈Z
(1 +k2)s⟨f(k),g(k)⟩Cn.
Here, ˆf(k) =
 1
0 e−2πikxf(x) dx is the k-th Fourier coeﬃcient off. For any integer k ≥0,
the introduced spaceHk coincides with the classical Sobolev spaceWk,2 and their norms‖·
‖H k and‖f‖W k,2 := (∑k
ν=0‖f(ν)‖2
L2)
1
2 are equivalent (cf. [Rei12, Lem. 1.2] or [AF03, 7.62]).
Moreover, Bessel potential spaces coincide with Sobolev–Slobodeckij spaces in the case ofp = 2,
in particular, they have equivalent norms as stated in [DNPV12, Proposition 3.4] for spaces
on the domain Rd. The proof can be modiﬁed to ﬁt our situation. It can be shown that
Hs(R/Z, Rn)⊆Ht(R/Z, Rn) for any 0≤t<s (cf. [Tay96, Chapter 4, Proposition 3.4]) as well
as Hs(R/Z, Rn)⊆C(R/Z, Rn) for anys> 1
2 (cf. [Tay96, Chapter 4, Proposition 3.3]).
Furthermore, Hm satisﬁes the Banach algebra property for anym≥1
2, i.e. there exists a
positive constantC =C(m) such that
‖fg‖H m≤C‖f‖H m‖g‖H m (3)
for allf,g ∈Hm(R/Z, R) (cf. [AF03, Theor. 4.39]).
For further information on fractional Sobolev spaces, we refer the reader for instance to
[AF03, DNPV12, RS96, Tri10].
2 Decomposition of the ﬁrst variation
Hermes was the ﬁrst to derive Gateaux diﬀerentiability and a formula for the ﬁrst variation of the
integral Menger curvatureMp = 2pintM(p,p) for p≥2 in his PhD thesis [Her12, Theorem2.33,
Remark2.35]. In [BR15, Theorem3], Blatt and Reiter extended this result to the generalized
5
integral Menger curvature intM(p,q) for the sub-critical rangep∈( 2
3q + 1,q + 2
3) and q > 1.
However, they approached the problem diﬀerently to Hermes by taking advantage of studying a
certain subdomain of integration as well as using the newly discovered characterization of energy
spaces developed in [Bla13, Theorem1.1] and [BR15, Theorem1]. The latter states that injective
curves inC1(R/Z, Rn) parametrized by arc-length have ﬁnite generalized integral Menger cur-
vature iﬀ they belong to the fractional Sobolev spaceW (3p−2)/q−1,q(R/Z, Rn) [BR15, Theorem
1].
To summarize Blatt and Reiter’s ﬁndings regarding the ﬁrst variation of the generalized in-
tegral Menger curvature intM(p,q), cf. [BR15, Theorem 3], they showed that it is continuously
diﬀerentiable on the subspace of all regular embeddedW (3p−2)/q−1,q-curves. Furthermore, they
gave an explicit formula for the ﬁrst variation of intM(p,q) at any arc-length parametrized em-
bedded γ∈W (3p−2)/q−1,q(R/Z, Rn) in directionh∈W (3p−2)/q−1,q(R/Z, Rn).
In the following we will restrict ourselves to the non-degenerate, sub-critical range of gener-
alized integral Menger curvature, i.e.q = 2 and p∈( 7
3, 8
3). In [BR15] it has turned out to be
helpful in that case to decompose its ﬁrst variation into a term of highest order and lower order
terms in order to study the regularity of critical points.
Hence we start with recapitulating a decomposition of the ﬁrst variation introduced in [BR15,
(4.2) and Lemma 4.2]. Note that we abbreviate
∆ x,yf :=f(u +x)−f(u +y)
and
D :=
{
(v,w )∈
(
−1
2, 0
{
×
(
0, 1
2
{⏐⏐w≤1 + 2v,v ≥−1 + 2w
}
.
We observe for any arc-length parametrized embedded γ∈W
3
2p−2,2(R/Z, Rn) and h ∈
W
3
2p−2,2(R/Z, Rn) that
δintM(p,2)(γ,h) = 12(Q(p)(γ,h) +R(p)(γ,h)), (4)
where the main term is given by
Q(p)(γ,h) :=

R/Z×D
⟨
∆ w,0γ
w −∆ v,0γ
v , ∆ w,0h
w −∆ v,0h
v
⟩
|v−w|p|v|p−2|w|p−2 dw dv du.
The remainder term can be expressed as following.
Lemma 2.1 ([BR15, Lemma 4.2]).The termR(p)(γ,h) is a ﬁnite sum of terms of the form

R/Z×D

···

[0,1]K
gp(u,v,w ;s1,...,sK−2)⊗h′(u +sK−1v +sKw) dθ1···dθK dv dw du (5)
whereG(p) : (0,∞)3→R is an analytic function,⊗may denote any kind of product structure,
such as cross product, dot product, scalar or matrix multiplication,sj∈{0,θj}for j = 1,...,K,
gp(u,v,w ;s1,...,sK−2) =G(p)
(|∆0,wγ|
|w|,|∆0,vγ|
|v|,|∆v,wγ|
|v−w|
{
Γ(u,v,w,s 1,s 2)·
·
(K1⨂
i=3
γ′(u +siv)
(
⊗


K2⨂
j=K1
γ′(u +siw)
(
(⊗


K−2⨂
j=K2
γ′(u +v +si(w−v))
(
(,
6
and Γ(u,v,w,s 1,s 2) is a term of one of the four types
(γ′(u +s1w)−γ′(u +s1v))⊗(γ′(u +s2w)−γ′(u +s2v))
|v|p−2|w|p−2|v−w|p ,
|γ′(u +s1w)−γ′(u +s2w)|2
|v|p−2|w|p−2|v−w|p ,
|γ′(u +s1v)−γ′(u +s2v)|2
|v|p−2|w|p−2|v−w|p ,
|γ′(u +v +s1(w−v))−γ′(u +v +s2(w−v))|2
|v|p−2|w|p−2|v−w|p .
