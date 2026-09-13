---
doc_id: arxiv-1308.2499v1
doc_title: "Towards a regularity theory for integral Menger curvature"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-11
source_pdf: 1308.2499v1.pdf
source_sha256: 3b20abdc0e1b0ba9
---
1 Classiﬁcation of ﬁnite-energy curves 6
2 Existence of minimizers within knot classes 11
3 Di ﬀerentiability 15
4 Regularity of stationary points 19
A Product and chain rule 26
B Equivalence of fractional seminorms 27
∗Workgroup Applied Analysis, Karlsruhe Institute of Technology, Kaiserstraße 89 – 93, 76133 Karlsruhe,
Germany, simon.blatt@kit.edu
∗∗Fakult¨at f ¨ur Mathematik, Universit ¨at Duisburg-Essen, Forsthausweg 2, 47057 Duisburg, Germany,
philipp.reiter@uni-due.de
1
arXiv:1308.2499v1  [math.AP]  12 Aug 2013
Introduction
Imagine a closed curve in the Euclidean space. Each triple of distinct points on the
curve uniquely deﬁnes its circumcircle that passes through these three points. It degen-
erates to a line if and only if the points are collinear. The reciprocal of the circumcircle
radius can be seen as some kind of approximate curvature. How much information on
shape and regularity of the curve can be drawn from the Lp-norm of the latter quantity?
Motivated from applications in microbiology, Gonzalez and Maddocks [14] investi-
gated this question for the casep =∞. They were in search of a notion for thethickness
of an embedded curve that, in contrast to other approaches, e.g. Litherland et al. [24],
does not require initial regularity of the respective curves.
Thickness is inﬂuenced by both local and global properties of a curve and is addi-
tionally related to the regularity of the curve. In fact, the thickness of an arc-length
parametrized curve is ﬁnite if and only if it is embedded and has a Lipschitz continu-
ous tangent, i.e., it is C1,1, see Gonzalez et al. [15]. Consequently, any curve of ﬁnite
thickness parametrized by arc-length is bi-Lipschitz continuous with a bi-Lipschitz
constant only depending on its thickness.
The latter is particularly interesting in the context of applications. Instead of trying to
immediately determine the knot type of a given possibly quite entangled curve, one
could ﬁrst “simplify” it in order to obtain a nicely shaped curve, having large distances
between distant strands. Such a deformation process could be deﬁned by the gradient
ﬂow of a suitable functional which should prevent the curve from leaving the ambient
knot class, preserving the bi-Lipschitz property.
This idea was formalized into the concept of knot energies by O’Hara [29, Def. 1.1].
A functional on a given space of knots is called a knot energy if it is bounded below
and self-repulsive, i.e., it blows up on sequences of embedded curves converging to a
non-embedded limit curve.
Among other functionals Gonzalez and Maddocks [14] also proposed to investigate the
functional
Mp(γ) :=
$
(R/Z)3
|γ′(u1)||γ′(u2)||γ′(u3)|
R(γ(u1),γ (u2),γ (u3))p du1 du2 du3, p∈ (0,∞),
which is called integral Menger1curvature. Here γ : R/Z → Rn is an absolutely
continuous curve and R(x,y, z) denotes the circumcircle of the three points x,y, z∈ Rn
given by
R(x,y, z) :=|y− z||y− x|| z− x|
2|(y− x)∧ (z− x)| = |y− z|
2 sin∢ (y− x, z− x). (0.1)
The functionals Mp have been investigated by Strzelecki, Szuma ´nska and von der
Mosel in [35] wherein further references can be found. Their results cover the case
p> 3 where Mp is known to be a knot energy. Especially they have been able to show
that ﬁnite energy of an arc-length parametrized curve impliesC1,1−3/p-regularity and its
1Named after K arl Menger, 1902 – 1985, US-Austrian mathematician, who used the circumcircle for
generalizing geometric concepts to general metric spaces [27]. He worked on many ﬁelds including distance
geometry, dimension theory, graph theory. Menger was a student of Hahn in Vienna where he received a
professorship in 1927. Being member of the Vienna Circle, he was also interested in philosophy and social
science. After emigrating to the USA in 1937, he obtained a position at Notre Dame, later at Chicago. See
Kass [18] for further reading.
2
image is C1-homeomorphic to the circle. The regularity statement has been sharpened
in [3].
The element M2 is referred to as total Menger curvature . Interestingly, it plays an
important rˆole in complex analysis, more precisely in the proof of Vitushkin’s conjec-
ture, a partial solution to Painlev´ e’s problemwhich asks to determine removable sets.
These are compact sets K⊂ C such that for any open U⊂ C containing K and for any
bounded analytic function U\K→ C, the latter can be extended to an analytic function
on U. Vitushkin conjectured that a compact set K with positive ﬁnite one-dimensional
Hausdorﬀ measure is removable if and only if it ispurely unrectiﬁable, i.e. it intersects
every rectiﬁable curve in a set of measure zero.
A central result in this context is the the curvature theorem of David and L ´eger [23]
stating that one-dimensional Borel sets in C with ﬁnite total Menger curvature are
1-rectiﬁable. Mel ′nikov and Verdera [25, 26, 39] discovered a connection between
L2-boundedness of the Cauchy integral operator on Lipschitz graphs and the Menger
curvature. For further details regarding Vitushkin’s conjecture for removable sets we
refer to Dudziak’s monography [12] and references therein.
Menger curvature for higher-dimensional objects has been discussed in [19, 21, 22, 4,
20, 34]. Further information on the context of the integral Menger curvature within the
ﬁeld of geometric knot theory and geometric curvature energies can be found in the
recent surveys by Strzelecki and von der Mosel [38, 37].
In this article we make a ﬁrst step towards the regularity theory of stationary points of
integral Menger curvature. Regularity theory for minimizers of certain knot energies
has been developed in [28, 13, 16, 32, 31, 8, 5]. A summary is given in [6, 7].
Unfortunately the Euler-Lagrange operator of Mp is not only non-local but also de-
generate. In order to produce non-degenerate energies, we embed this family into the
two-parameter family of generalized integral Menger curvature
intM(p,q)(γ) :=
$
(R/Z)3
|γ′(u1)||γ′(u2)||γ′(u3)|
R(p,q)(γ(u1),γ (u2),γ (u3)) du1 du2 du3, p, q> 0, (0.2)
where
R(p,q)(x,y, z) := (|y− z||y− x|| z− x|)p
|(y− x)∧ (z− x)|q =|y− z|p|y− x|p−q|z− x|p−q
sin∢ (y− x, z− x)q , x,y, z∈ Rn.
(0.3)
Note that the functionR(p,q) is symmetric in all components. Of course,Mp = 2pintM(p,p).
The elements of this family are knot energies under certain conditions only. More
precisely, we will see in Remark 1.2 that they are punishing self-intersections if and
only if
p≥ 2
3q + 1. (0.4)
On the other hand, these energies can only be ﬁnite on closed curves iﬀ
p< q + 2
3, (0.5)
see Remark 1.3. The sub-critical range, i.e. the range of parameters that lead to a
sub-critical Euler-Lagrange equation,2 is given by
p∈
( 2
3q + 1, q + 2
3
)
(q> 1), (0.6)
2In contrast, the corresponding range is called super-critical by Strzelecki et al. [36] as it lies above the
respective critical value for which the energy is scale-invariant.
3
and its non-degenerate part (leading to a non-degenerate equation) is
p∈
( 7
3, 8
3
)
, q = 2. (0.7)
These areas are visualized in Figure 1.
p = 2
3 q + 1
p = q + 2
3
p = qEnergy
decrease
1 2 3 4 5
1
2
3
4
5
0
p
q q
Figure 1: The range of intM(p,q). Above the green line, the integrand is not suﬃciently
singular to penalize self-intersections, thus intM(p,q) is not a knot energy. On the other
hand, below the red line, forq> 1, the integrand is so singular, that the integral is either
equal to zero or inﬁnite, so there are no ﬁnite-energy C1-knots at all. The hatched area
reveals the strange behavior that there are no ﬁnite-energyC3-knots while it takes ﬁnite
values on polygons.
In [3], a characterization of curves with ﬁniteMp energy was given in terms of function
spaces. Using this technique we infer
Theorem 1 (Classiﬁcation of ﬁnite-energy curves).
Consider the sub-critical case (0.6) and let γ∈ C1(R/Z, Rn) be an injective curve
parametrized by arc-length. Then intM(p,q)(γ) <∞ if and only if γ∈ W(3p−2)/q−1,q.
Moreover, one then has, for constants C,β> 0 depending on p, q only,
‖γ‖W(3p−2)/q−1,q≤ C
(
intM(p,q)(γ) + intM(p,q)(γ)β)
. (0.8)
We will use the last theorem to show
Theorem 2 (Existence of minimizers within knot classes).
In the sub-critical case (0.6), there is a minimizer of intM(p,q) among all injective,
regular curvesγ∈ C1(R/Z, Rn) in any knot class.
To shorten notation we use the abbreviation
∆v,w• :=•(u +v)−• (u +w) (0.9)
4
throughout this paper. Furthermore, we sometimes omit the argument of a function if
it is precisely the variable u, i.e.γ =γ(u) etc.
The ﬁrst variation ofMp, p≥ 2, has been derived by Hermes [17, Thm. 2.33, Rem. 2.35].
Here we use a diﬀerent approach to prove
Theorem 3 (Diﬀerentiability). In the sub-critical case (0.6) the functional intM(p,q)
is C1 on the subspace of all regular embedded W(3p−2)/q−1,q-curves.
For any arc-length parameterized embedded γ ∈ W(3p−2)/q−1,q(R/Z, Rn) and h ∈
W(3p−2)/q−1,q(R/Z, Rn), the ﬁrst variation of intM(p,q) atγ in direction h amounts to
δintM(p,q)(γ, h)
=
$
(R/Z)3
{
2q
⏐⏐⏐∆v,0γ∧∆ w,0γ
⏐⏐⏐q−2
(⏐⏐⏐∆v,wγ
⏐⏐⏐
⏐⏐⏐∆v,0γ
⏐⏐⏐
⏐⏐⏐∆w,0γ
⏐⏐⏐
)p· ⟨∆v,0γ∧∆ w,0γ,∆v,0γ∧∆ w,0h⟩
− 3p
⏐⏐⏐∆v,0γ∧∆ w,0γ
⏐⏐⏐q
(⏐⏐⏐∆v,wγ
⏐⏐⏐
⏐⏐⏐∆v,0γ
⏐⏐⏐
⏐⏐⏐∆w,0γ
⏐⏐⏐
)p·
⟨∆v,wγ,∆v,wh⟩
⏐⏐⏐∆v,wγ
⏐⏐⏐2
+ 3
⏐⏐⏐∆v,0γ∧∆ w,0γ
⏐⏐⏐q
(⏐⏐⏐∆v,wγ
⏐⏐⏐
⏐⏐⏐∆v,0γ
⏐⏐⏐
⏐⏐⏐∆w,0γ
⏐⏐⏐
)p· ⟨γ′, h′⟩}
dw dv du.
(0.10)
Using this formula, we will see that stationary points of the energies intM(p,2) restricted
to ﬁxed length satisfy some kind of non-local uniformly elliptic pseudo-di ﬀerential
equation. If furthermore p∈
( 7
3, 8
3
)
, the non-linearity turns out to be sub-critical and
we can ﬁnally use the Euler-Lagrange equation to prove the following main result of
this article:
Theorem 4 (Regularity of stationary points).
For p ∈ ( 7
3, 8
3), let γ ∈ W3p/2−2,2(R/Z, Rn) be a stationary point of intM(p,2) with
respect to ﬁxed length, injective and parametrized by arc-length. Thenγ∈ C∞.
In a sense this concludes our study of the non-degenerate, subcritical cases of the most
prominent knot energies for curves. Regularity theory for the non-degenerate sub-
critical case has already been performed for O’Hara’s energies [8] and for the general-
ized tangent-point energies [5]. The treatment of the critical case however turns out to
be far more involved and has yet only be done for O’Hara’s knot energies [9].
We brieﬂy introduce Sobolev-Slobodecki˘ ı spacesin the form we will use them in this
text. Let f∈ W1,1(R/Z, Rn). For s∈ (0, 1) andϱ∈ [1,∞) we deﬁne the seminorm
[ f]
W1+s,ϱ :=
(∫
R/Z
∫ 1/2
−1/2
| f′(u +w)− f′(u)|ϱ
|w|1+ϱs dw du
)1/ϱ
. (0.11)
On W1,ϱ this seminorm is equivalent to
 f 
W1+s,ϱ :=
(∫
R/Z
∫ 1/4
−1/4
| f (u +w)− 2 f (u) + f (u−w)|ϱ
|w|1+ϱ(1+s) dw du
)1/ϱ
, (0.12)
see Appendix B.
5
Now let Wk,ϱ(R/Z, Rn), k∈ N, denote the usual Sobolev space (recall W0,ϱ := Lϱ) and
Wk+s,ϱ(R/Z, Rn) :=
{
f∈ Wk,ϱ(R/Z, Rn)
⏐⏐⏐‖ f‖Wk+s,ϱ <∞
}
which we equip, depending on the situation, either with the norm‖ f‖Wk,ϱ+
[
f (k−1)
]
W1+s,ϱ
or with‖ f‖Wk,ϱ +

f (k−1)

W1+s,ϱ respectively.
Without further notice we will frequently use the embedding
Wk+s,ϱ(R/Z, Rn)↪→ Ck,s−1/ϱ(R/Z, Rn), ϱ ∈ (1,∞), s∈ (ϱ−1, 1). (0.13)
We will denote by Cia resp. Wia injective (embedded) curves parametrized by a rc-
length. As usual, a curve is said to be regular if there is some c > 0 such that|γ′|≥ c
a.e. Constants may change from line to line.
1 Classiﬁcation of ﬁnite-energy curves
Before we begin the discussion of the ﬁrst variation, let us rewrite the integral Menger
curvature using the symmetry and a suitable covering of the domain of integration
(R/Z)3 by domains, on which it is easier to estimate the terms that will appear. The
general idea here is quite similar to [3] and Hermes [17], but we will show that it is
actually enough to integrate over a certain subdomain of (R/Z)3.
To this end we deﬁne the range of integration
D :=
{
(v,w )∈ (− 1
2, 0)× (0, 1
2)
⏐⏐⏐w≤ 1 + 2v,v≥− 1 + 2w
}
, (1.1)
which is depicted in Figure 2.
-1
1
0 v
w
D
Figure 2: The range of integration D
Lemma 1.1 (Domain decomposition). Let f ∈ L1
(
(R/Z)3)
be symmetric in all com-
ponents, i.e. f = f◦σ for all permutationsσ∈ S3. Then
$
(R/Z)3
f (u1, u2, u3) du1 du2 du3 = 6
$
R/Z×D
f (u, u +v, u +w) dw dv du.
6
Proof. Let Pσ∈ R3×3 denote the permutation matrix corresponding to σ∈ S3. We
ﬁrst show that the images{ Pσ (R/Z× D)|σ∈ S3} cover (R/Z)3.
Consider (u1, u2, u3)∈ (R/Z)3. Then after a suitable permutation we can assume that
dR/Z(u1, u3) = max(dR/Z(u1, u2), dR/Z(u2, u3), dR/Z(u1, u3))
where dR/Z(x,y ) = min{|x−y− k| : k∈ Z}∈ [0, 1
2] denotes the distance in R/Z. Hence,
interchanging u1 and u3 if necessary, there are (v,w )∈
[
− 1
2, 0
]
×
[
0, 1
2
]
with
u1 = u2 +v, u3 = u2 +w,
and
max (−v,w ) = max(dR/Z(u1, u2), dR/Z(u2, u3))
≤ dR/Z(u1, u3) = min (w−v, 1− (w−v))≤ 1−w +v,
so (v,w )∈ D. Since furthermore
#S3·|R/Z× D| = 6· 1
6 =
⏐⏐⏐(R/Z)3⏐⏐⏐
the sets{ Pσ (R/Z× D)|σ∈ S3} form up to sets of measure zero a disjoint partition of
(R/Z)3. □
Following Lemma 1.1 we derive using (0.9)
intM(p,q)(γ) = 6
$
R/Z×D
⏐⏐⏐∆v,0γ∧∆ 0,wγ
⏐⏐⏐q
(⏐⏐⏐∆v,0γ
⏐⏐⏐
⏐⏐⏐∆0,wγ
⏐⏐⏐
⏐⏐⏐∆v,wγ
⏐⏐⏐
)p
⏐⏐⏐γ′(u)
⏐⏐⏐
⏐⏐⏐γ′(u +v)
⏐⏐⏐
⏐⏐⏐γ′(u +w)
⏐⏐⏐ dw dv du.
(1.2)
Proof of Theorem 1. Recall that any embedded W1+s,ϱ
ia -curve, s > 1
ϱ, is bi-Lipschitz
continuous [2, Lemma 2.1]. We obtain, using |a∧ b| =|a∧ (a± b)|≤|a|| a± b| for
a, b∈ R3,
intM(p,q)(γ)≤ C
$
R/Z×D
⏐⏐⏐⏐
∫ 1
0 γ′(u +θ1v) dθ1∧
∫ 1
0 γ′(u +θ2w) dθ2
⏐⏐⏐⏐
q
|v|p−q|w|p−q|v−w|p dw dv du
≤ C
$
R/Z×D
∫ 1
0 |γ′(u +θv)−γ′(u +θw)|q dθ
|v|p−q|w|p−q|v−w|p dw dv du
≤ C
∫ 1
0
$
R/Z×D
|γ′(u +θ(v−w))−γ′(u)|q
|v|p−q|w|p−q|v−w|p dw dv du dθ
where C depends on p, q and γ. Substituting Φ : (v,w )↦→ (t, ˜w) : =
( v
v−w,θ (v−w)
)
,
|det DΦ(v,w )| = θ
|v−w|, Φ(D)⊂ [0, 1]× [−1, 0], we arrive at
intM(p,q)(γ)
≤ C
∫ 1
0
θ−1
∫
R/Z
∫ 1
0
∫ 0
−1
|γ′(u + ˜w)−γ′(u)|q
⏐⏐⏐t ˜w
θ
⏐⏐⏐p−q ⏐⏐⏐(t− 1) ˜w
θ
⏐⏐⏐p−q ⏐⏐⏐ ˜w
θ
⏐⏐⏐p−1 d ˜w dt du dθ
≤ C
∫ 1
0
θ3p−2q−2 dθ
∫ 1
0
dt
|t(1− t)|p−q
∫
R/Z
∫ 0
−1
|γ′(u + ˜w)−γ′(u)|q
| ˜w|3p−2q−1 d ˜w du
≤ C
([γ]q
W(3p−2)/q−1,q +
‖‖‖γ′‖‖‖q
L∞
)
≤ C‖γ‖q
W(3p−2)/q−1,q.
(1.3)
7
For the other implication, we ﬁrst derive for given vectors a, b∈ Rn,|a| =|b| = 1,
⟨a, b⟩≥ 0,
|a∧ b|2 =|a|2|b|2−⟨a, b⟩2≥ 1−⟨a, b⟩ = 1
2|a− b|2. (1.4)
By uniform continuity ofγ′ we may chooseδ =δ(γ)∈ (0, 1
2) such that
⏐⏐⏐γ′(u +v)−γ′(u +w)
⏐⏐⏐≤ 1
10 for all u∈ R/Z, v,w ∈ [−δ,δ]. (1.5)
In fact, we may choose δ to be maximal, i.e. we assume that there are ˜u∈ R/Z, ˜v, ˜w∈
[−δ,δ] with ⏐⏐⏐γ′(˜u + ˜v)−γ′(˜u + ˜w)
⏐⏐⏐ = 1
10. (1.6)
We ﬁx u0∈ R/Z. Asγ∈ C1(R/Z, Rn) we may apply a suitable translation and rotation
of the ambient space Rn such that γ(u0) = 0 and there is a function f ∈ C1(R, Rn−1)
with‖ f‖L∞≤ 1 and f (0) = 0 such that ˜γ(u) := (u, f (u)) satisﬁes ˜γ(B2δ(0))⊂ γ(R/Z).
Then
1
2
⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐≤|v|≤
⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐. (1.7)
Arc-length parametrization ofγ gives
intM(p,q)(˜γ)
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ δ
−δ
⏐⏐⏐⏐⏐
∆v,0 ˜γ
|∆v,0 ˜γ|∧ ∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐p−q ⏐⏐⏐∆0,w ˜γ
⏐⏐⏐p−q ⏐⏐⏐∆v,w ˜γ
⏐⏐⏐p dw dv du
(1.4)
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ δ
−δ
⏐⏐⏐⏐⏐signv∆v,0 ˜γ
|∆v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐p−q ⏐⏐⏐∆0,w ˜γ
⏐⏐⏐p−q ⏐⏐⏐∆v,w ˜γ
⏐⏐⏐p dw dv du
(1.7)
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ δ
−δ
⏐⏐⏐⏐⏐signv∆v,0 ˜γ
|∆v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|p−q|w|p−q|v−w|p dw dv du
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ δ
−δ

⏐⏐⏐⏐⏐signv∆v,0 ˜γ
|∆v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|p−q|w|p−q|v−w|p +
⏐⏐⏐⏐⏐− signv∆−v,0 ˜γ
|∆−v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|p−q|w|p−q|v +w|p

dw dv du
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ |v|
−|v|

⏐⏐⏐⏐⏐signv∆v,0 ˜γ
|∆v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|p−q|w|p−q|v +w|p +
⏐⏐⏐⏐⏐− signv∆−v,0 ˜γ
|∆−v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|p−q|w|p−q|v−w|p

dw dv du
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
∫ |v|
−|v|
⏐⏐⏐⏐⏐signv∆v,0 ˜γ
|∆v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
+
⏐⏐⏐⏐⏐− signv∆−v,0 ˜γ
|∆−v,0 ˜γ| + signw∆0,w ˜γ
|∆0,w ˜γ|
⏐⏐⏐⏐⏐
q
|v|3p−2q dw dv du
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
⏐⏐⏐⏐⏐
∆v,0 ˜γ
|∆v,0 ˜γ| + ∆−v,0 ˜γ
|∆−v,0 ˜γ|
⏐⏐⏐⏐⏐
q
|v|3p−2q−1 dv du
(1.8)
where c> 0 only depends on p and q. The last line in (1.8) is bounded below by
c
∫ u0+δ
u0−δ
∫ δ
−δ
⏐⏐⏐∆v,0 ˜γ +∆−v,0 ˜γ
⏐⏐⏐q
|v|3p−q−1 dv du− C
∫ u0+δ
u0−δ
∫ δ
−δ
⏐⏐⏐∆−v,0 ˜γ
⏐⏐⏐q
⏐⏐⏐⏐⏐
1
|∆v,0 ˜γ|− 1
|∆−v,0 ˜γ|
⏐⏐⏐⏐⏐
q
|v|3p−2q−1 dv du
8
(1.7)
≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
|˜γ(u +v)− 2˜γ(u) + ˜γ(u−v)|q
|v|3p−q−1 dv du− C
∫ u0+δ
u0−δ
∫ δ
−δ
⏐⏐⏐⏐⏐
v
|∆v,0 ˜γ|− v
|∆−v,0 ˜γ|
⏐⏐⏐⏐⏐
q
|v|3p−2q−1 dv du.
By ⏐⏐⏐⏐⏐⏐⏐
v⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐− v⏐⏐⏐∆−v,0 ˜γ
⏐⏐⏐
⏐⏐⏐⏐⏐⏐⏐≤
⏐⏐⏐⏐⏐⏐⏐
(v,∆v,0 f )⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐ + (−v,∆−v,0 f )⏐⏐⏐∆−v,0 ˜γ
⏐⏐⏐
⏐⏐⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐⏐⏐
∆v,0 ˜γ⏐⏐⏐∆v,0 ˜γ
⏐⏐⏐ + ∆−v,0 ˜γ⏐⏐⏐∆−v,0 ˜γ
⏐⏐⏐
⏐⏐⏐⏐⏐⏐⏐
we may use (1.8) to absorb the last term which ﬁnally leads to
intM(p,q)(γ)≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
|˜γ(u +v)− 2˜γ(u) + ˜γ(u−v)|q
|v|3p−q−1 dv du.
Since reparametrization to arc-length preserves regularity, we arrive at
intM(p,q)(γ)≥ c
∫ u0+δ
u0−δ
∫ δ
−δ
|γ(u +v)− 2γ(u) +γ(u−v)|q
|v|3p−q−1 dv du. (1.9)
As u0 was chosen arbitrarily, we obtain
γq
W(3p−2)/q−1,q≤ C
(
intM(p,q)(γ) +
‖‖‖γ′‖‖‖q
L∞δ−3p+2q+2)
(1.10)
uniformly on R/Z. Since the exponent−3p + 2q + 2 is negative, we have to show that
δ is uniformly bounded away from zero in order to ﬁnish the proof. To this end we will
establish the Morrey-type estimate
‖‖‖γ′(· +w)−γ′(·)
‖‖‖L∞≤ CintM(p,q)(γ)1/q|w|α for allw∈ [− 1
2, 1
2] (1.11)
whereα = 3(p− 1)/q− 2 > 0. As δ was chosen to be maximal with respect to (1.6),
we arrive at
1
10≤ CintM(p,q)(γ)1/qδα
which, applied to (1.10), gives (0.8).
It remains to prove (1.11) which follows by standard arguments due to Campanato [11].
Let γ′
Br(x) denote the integral mean of γ′ over Br(x). We calculate for x∈ R/Z and
r∈ (0,δ )
1
2r
∫
Br(x)
|γ′(v)−γ′
Br(x)| dv≤ 1
4r2
∫
Br(x)
∫
Br(x)
|γ′(v)−γ′(u)| du dv
≤
( 1
4r2
∫
Br(x)
∫
Br(x)
|γ′(v)−γ′(u)|q du dv
)1/q
≤ Crα
(∫
Br(x)
∫
Br(x)
|γ′(v)−γ′(u)|q
|u−v|3p−2q−1 du dv
)1/q
(1.9)
≤ CrαintM(p,q)(γ)1/q.
As (1.11) only involves the domain of γ up to a measure zero set, we may restrict to
Lebesgue points. We choose two Lebesgue points u,v ∈ R/Z ofγ′ with r :=|u−v|∈
(0, δ
2). Then
|γ′(u)−γ′(v)|≤
∞∑
k=0
⏐⏐⏐⏐γ′
B21−kr(u)−γ′
B2−kr(u)
⏐⏐⏐⏐ +
⏐⏐⏐γ′
B2r(u)−γ′
B2r(v)
⏐⏐⏐ +
∞∑
k=0
⏐⏐⏐⏐γ′
B21−kr(v)−γ′
B2−kr(v)
⏐⏐⏐⏐.
9
Since
⏐⏐⏐γ′
B2r(u)−γ′
B2r(v)
⏐⏐⏐≤
∫
B2r(u)|γ′(x)−γ′
B2r(u)| dx +
∫
B2r(v)|γ′(x)−γ′
B2r(v)| dx
|B2r(u)∩ B2r(v)|
≤ C|u−v|αintM(p,q)(γ)1/q
as r =|u−v| and, for ally∈ R/Z, R∈ (0, δ
2),
⏐⏐⏐γ′
B2R(y)−γ′
BR(y)
⏐⏐⏐≤
∫
BR(y)|γ′(x)−γ′
B2R(y)| dx +
∫
BR(y)|γ′(x)−γ′
BR(y)| dx
2R
≤ CRαintM(p,q)(γ)1/q,
we deduce|γ′(u)−γ′(v)|≤ C
(∑∞
k=0 2−kα + 1 + ∑∞
k=0 2−kα
)
|u−v|αintM(p,q)(γ)1/q. Thus
|γ′(u)−γ′(v)|≤ C|u−v|αintM(p,q)(γ)1/q for all Lebesgue points of γ′ with|u−v| < δ
2.
The case|u−v|≥ δ
2 follows by the triangle inequality. □
Let us conclude this section by brieﬂy commenting on the other ranges in the ( p, q)-
domain, see Figure 1.
Remark 1.2 (Non-repulsive energies for p < 2
3 q + 1). A bi-Lipschitz estimate is not
guaranteed for injective curves if p < 2
3q + 1. We brieﬂy give the following example.
Consider the curves u↦→ (u, 0, 0) and u↦→ (0, u,δ ) for u∈ [−1, 1], δ∈ [0, 1]. The
interaction of these strands leads to the intM(p,q)-value
C
$
[−1,1]3
(
δ2 + u2
)q/2
|v−w|p−q (δ2 + u2 +v2)p/2 (δ2 + u2 +w2)p/2 dw dv du
≤ C
$
[−1,1]3
(
δ2 + u2
)(q−p)/2
|v−w|p−q (δ2 + u2 +v2 +w2)p/2 dw dv du.
Introducing polar coordinatesu = r cosϑ,v = r sinϑ cosϕ,w = r sinϑ sinϕ, the former
quantity is bounded by
C
∫ √
3
0
∫ π
0
(
δ2 + r2 cos2ϑ
)(q−p)/2
r2 sinϑ
rp−q sinp−qϑ(δ2 + r2)p/2 dϑ dr
∫ 2π
0
dϕ
|cosϕ− sinϕ|p−q
|                       {z                       }
≤C
≤ C
√
3∫
0

∫
[0,π
4 ]∪[ 3π
4 ,π]
(
δ2 + r2
)(q−p)/2
dϑ
rp−q−2 sinp−q−1ϑ|     {z     }
≥1
(δ2 + r2)p/2 +
3π
4∫
π
4
(
δ2 + r2 cos2ϑ
)(q−p)/2
r sinϑ
rp−q−1 sinp−qϑ(δ2 + r2)p/2 dϑ

dr
≤ C
∫ √
3
0
(
(δ + r)−3p+2q+2 + r−p+q+1 (δ + r)−p
∫ r
0
(
δ2 +σ2)(q−p)/2
dσ
)
dr
≤ C
(
1−δ−3p+2q+3)
≤ C.
Using Theorem 1 and the monotonicity of intM (·,q) for ﬁxed q, it is easy to produce
a family of knots uniformly converging to a non-embedded curve without an energy
blow-up asδ↘ 0, so these energies are not self-repulsive. ^
10
Remark 1.3 (Singular energies for p≥ q + 2
3, q > 1). For p≥ q + 2
3, q > 1, and an
absolutely continuousγ : R/Z→ R we have intM(p,q)(γ)≡∞ for all C1-curvesγ. To
see this, note that we assumed p< 2
3q + 1 in Theorem 1 mainly because neither (0.11)
nor (0.12) is not deﬁned for s≥ 1. For general p≥ 2
3q + 1 we nevertheless still have
∫
R/Z
∫ 1/2
−1/2
|γ′(u +w)−γ′(u)|q
|w|3p−2q−1 dw du≤ C
(
intM(p,q)(γ) + intM(p,q)(γ)β)
.
Applying Brezis [10, Prop. 2], the function γ′ is constant, hence γ lies on a straight
line. Therefore, γ cannot be a closed C1-curve. ^
Remark 1.4 (Strange energies for p∈ [q + 2
3 , 2
3 q + 1)). On p∈ [q+ 2
3, 2
3q+1), p, q>
0, see the hatched area in Figure 1, we ﬁnd the strange behavior that there are no
closed ﬁnite-energy C3-curves while self-intersections, and in particular corners, are
not penalized. So piecewise linear curves (polygonals) have ﬁnite energy.
The latter can be seen by adapting the calculation in Remark 1.2. For the former we
recall that a closed arc-length parametrized C2-curve must have positive curvature|γ′′|
at some point u0 and by continuity there arec,δ> 0 with|γ′′|≥ c> 0 on [u0−δ,u0+δ].
Asγ′′⊥γ′ we obtain|γ′′∧γ′| =|γ′′|≥ c. So intM(p,q)(γ) is bounded below by
u0+δ∫
u0−δ
δ∫
−δ
2
3|v|∫
1
3|v|
|v|−3p+2q
⏐⏐⏐⏐⏐
∆v,0γ
v ∧∆0,wγ
w
⏐⏐⏐⏐⏐
q
dw dv du
=
u0+δ∫
u0−δ
δ∫
−δ
2
3|v|∫
1
3|v|
|v|−3p+2q
⏐⏐⏐⏐⏐⏐
v−w
2 γ′′(u)∧γ′(u) + v2
2
∫ 1
0
(1−ϑ1)2γ′′′(u +ϑ1v) dϑ1∧
(
γ′(u) + w
2γ′′(u)
)
− w2
2
∫ 1
0
(1−ϑ2)2γ′′′(u +ϑ2w) dϑ1∧
(
γ′(u) + v
2γ′′(u)
)
+ v2w2
2
"
[0,1]2
(1−ϑ1)2(1−ϑ2)2γ′′′(u +ϑ1v)∧γ′′′(u +ϑ2w) dϑ1 dϑ2
⏐⏐⏐⏐⏐⏐
q
dw dv du
≥δ
[
˜c− Cδ
‖‖‖γ′′′‖‖‖q
L∞
(‖‖‖γ′′′‖‖‖L∞ +
‖‖‖γ′′‖‖‖L∞ + 1
)q]∫ δ
−δ
|v|−3p+3q+1 dv.
Lesseningδ> 0, the square bracket is positive. This gives intM(p,q)(γ) =∞. ^
