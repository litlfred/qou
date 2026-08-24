---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-002-12-cusp-area-and-link-diagrams
section_title: "Cusp area and link diagrams"
section_number: 1.2
pages: 3-6
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
of 2–bridge links. Using similar techniques, in this paper w e are also able to bound the
lengths of slopes on maximal cusps in hyperbolic 2–bridge li nks. Since all 2–bridge links can
be represented by an alternating diagram, our results give f urther evidence for a conjectural
picture of the cusp shapes and maximal cusp metrics of altern ating knots.
For general alternating knots and links, there is increasin g evidence that the cusp shape
and maximal cusp metric ought to be bounded in terms of the twi st number of a reduced
diagram. We say that a link diagram is reduced if it does not contain any crossings that
separate the diagram: that is, any crossings in the projecti on plane such that there is a
simple closed curve meeting the diagram transversely in onl y that crossing. Similarly, two
crossings are said to be equivalent if there exists a simple c losed curve meeting the knot
diagram transversely in those two crossings, disjoint from the knot diagram elsewhere. The
twist number is the number of equivalence classes of crossings (called twist regions ).
Conjecture 1.1. The area of a maximal cusp metric on an alternating knot is boun ded
above and below by linear functions of the twist number of a re duced, alternating diagram.
Similarly, the length of the shortest non-meridional slope of an alternating knot is bounded
above and below by a linear function of the twist number of the diagram.
We ﬁrst became aware of this conjecture several years ago by v iewing slides of a talk
by Thistlethwaite, in which he showed using SnapPea that the conjecture holds for many
simple alternating knots. Lackenby proved a close variant t he conjecture, relating the twist
number of a diagram to the combinatorial length of slopes [37]. However, Lackenby’s methods
are purely combinatorial and cannot be applied to give the ge ometric information of the
conjecture.
In this paper we prove the conjecture for 2–bridge link compl ements. In particular, we
show the following.
Theorem 4.8. LetK be a 2–bridge link in S3, whose reduced alternating diagram has twist
number t. Let C be a maximal neighborhood about the cusps of S3/integerdivideK, in which the two
cusps have equal volume if K has two components. Then
8
√
3
147 (t − 1) ≤ area(∂C ) < 2
√
3 v8
v3
(t − 1).
Furthermore, ifK is a knot, let γ be any non-trivial arc that starts on a meridian and comes
back to the same meridian (for example, a non-meridional sim ple closed curve). Then its
4 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
length satisﬁes
ℓ(γ) ≥ 4
√
6
√
2
147 (t − 1).
This result should be compared to that of Adams et al. [3], where they prove upper bounds
on cusp area in terms of the crossing number c of a knot. For alternating knots, including
2–bridge knots, they show that the cusp area satisﬁes area( ∂C ) ≤ 9c − 36 + 36/c. For those
2–bridge knots whose diagrams have very few crossings per tw ist region (in particular, when
c/t <1.39), the bound of Adams et al. is sharper than the upper bound of Theorem 4.8.
For more general 2–bridge knots that have more crossings per twist region, the upper bound
of Theorem 4.8 is a signiﬁcant improvement. To the best of our knowledge, the lower bound
of Theorem 4.8 does not have any predecessors in the literatu re.
1.3. Applications to hyperbolic Dehn ﬁlling. The shapes of the cusps and their actual
metrics give information not just on the 3–manifold itself, but also on the Dehn ﬁllings of
that manifold.
For example, modulo the geometrization conjecture, severa l theorems imply that Dehn
ﬁllings on slopes of suﬃcient length yield hyperbolic manif olds (these are the 2 π–Theorem,
due to Gromov and Thurston [13]; the 6–Theorem, due to Agol [4 ] and Lackenby [37]; and
the 7.515–Theorem, due to Hodgson and Kerckhoﬀ [32]). When we comb ine these theorems
with the results on maximal cusp areas and slope lengths abov e, we ﬁnd that Farey manifolds
with long monodromy admit no non-trivial Dehn ﬁllings, wher e “long” is explicit.
In particular, Bleiler and Hodgson [13] note that the work of Jørgensen [34] combined with
the 2π–Theorem implies that there is a constant N such that every non-trivial Dehn ﬁlling
of a punctured torus bundle with monodromy length s> N gives a hyperbolic 3–manifold.
However, they remark on the lack of an explicit value for the c onstantN . Now Theorem 4.1,
coupled with the 6–Theorem, allows the estimate N ≤ 90.
More recently, the authors proved a result that bounds the vo lume of manifolds obtained
by Dehn ﬁlling along a slope of length at least 2 π, in terms of the length of that slope [25].
Thus we may combine Theorem 4.1 with this recent result to est imate the volumes of the
manifolds obtained by Dehn ﬁlling. For example, if M is a punctured–torus bundle with
monodromy of length s >94, then the length of any non-trivial slope γ on the cusp of M
(i.e. any slope transverse to the ﬁbers) will be at least 2 π. Then by [25, Theorem 1.1], the
volume of the manifold M (γ) obtained by Dehn ﬁlling M alongγ will be bounded explicitly
below. See Corollary 4.6.
One large class of examples obtained by Dehn ﬁlling 4–punctu red sphere bundles is the
class of closed 3–braids, which has been extensively studie d by others (see e.g. Murasugi [45],
Birman and Menasco [11]). In this paper, we classify the hype rbolic links that are closed
3–braids (see Theorem 5.5), and obtain the ﬁrst estimates on volumes of these links.
To state these results, let σ1, σ2 denote the generators for B3, the braid group on three
strands, as in Figure 1. Let C = (σ1σ2)3. It is known, by work of Schreier [51], that most
PSfrag replacementsσ1 σ2
Figure 1. Braid group generators σ1 and σ2.
CUSP AREAS OF F AREY MANIFOLDS 5
3–braids are conjugate to words of the form w =C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 , where pi, qi are all
positive. In particular, all 3–braids with hyperbolic clos ures are of this form, as we shall
show in Theorem 5.5. Following Birman and Menasco [11], we ca ll such braids generic.
Theorem 5.6. Let K = ˆw be the closure of a generic 3–braid w = C kσp1
1 σ−q1
2 · · ·σps
1 σ−qs
2 ,
whereC = (σ1σ2)3, and pi, qi are all positive. Suppose, furthermore, that w is not conjugate
to σp
1σq
2 for arbitrary p, q. Then K is hyperbolic, and
4v3s − 277 < vol(S3/integerdivideK) < 4v8s,
where v3 = 1.0149... is the volume of a regular ideal tetrahedron and v8 = 3.6638... is the
volume of a regular ideal octahedron. Furthermore, the mult iplicative constants in both the
upper and lower bounds are sharp.
1.4. V olume and Jones polynomial invariants. The volume estimate of Theorem 5.6
has a very interesting application to conjectures on the rel ationship of the volume to the
Jones polynomial invariants of hyperbolic knots.
For a knot K, let
JK (t) = αKtm +βKtm−1 +... +β′
Ktr+1 +α′
Ktr
denote the Jones polynomial of K. We will always denote the second and next–to–last
coeﬃcients of JK(t) by βK and β′
K , respectively.
The Jones polynomial ﬁts into an inﬁnite family of knot invar iants: the colored Jones
polynomials. These are Laurent polynomial knot invariants J n
K (t), n > 1, where J 2
K (t) =
JK (t). The volume conjecture [36, 44] states that for a hyperboli c knot K,
2π lim
n→∞
log
⏐
⏐J n
K (e2πi/n )
⏐
⏐
n = vol(S3/integerdivideK),
where e2πi/n is a primitive n-th root of unity. If the volume conjecture is true, then one
expects correlations between vol( S3/integerdivideK) and the coeﬃcients of J n
K(t), at least for large
values of n. For example, for n ≫ 0 one would have
vol(S3/integerdivideK) < C||J n
K ||,
where ||J n
K || denotes the sum of absolute values of the coeﬃcients of J n
K(t) andC is a constant
independent of K. At the same time, several recent results and much experimen tal evidence
[18, 22, 25, 26] actually indicate that there may be a correla tion between vol(S3/integerdivideK) and the
coeﬃcients of the Jones polynomial itself. These results pr ompt the following question.
Question 1.2. Do there exist constants Ci > 0, i = 1,..., 4, and a function BK of the
coeﬃcients of JK (t), such that all hyperbolic knots satisfy
(1) C1 BK −C2 < vol(S3/integerdivideK) < C3 BK +C4?
Dasbach and Lin [22] showed that for alternating knots, equa tion (1) holds for BK :=
|βK |+|β′
K|. They also presented experimental evidence suggesting lin ear correlations between
|βK | + |β′
K | and the volume of non-alternating knots; their data is based on knots with a
low numbers of crossings. The authors of the current paper ha ve shown that the same
function works for several large families in the class of adequate knots , which are a vast
generalization of alternating knots [25, 26]. In fact, Dasb ach and Lin [21] and Stoimenow
[54] showed that for adequate knots, the second and next–to– last coeﬃcients of the colored
Jones polynomial J n
K (t) are independent of n, equal to those of the Jones polynomial JK (t).
So these results establish strong versions of relations bet ween volume and coeﬃcients of the
6 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
colored Jones polynomials for these knots, as predicted by t he volume conjecture. This led
to some hope that not only would Question 1.2 be answered in th e aﬃrmative, but also that
BK = |βK | + |β′
K | could always work in equation (1).
In this paper we show that a slightly modiﬁed function, invol ving the ﬁrst two and the last
two coeﬃcients of the Jones polynomial, satisﬁes equation ( 1) for hyperbolic closed 3-braids.
Building on Theorem 5.6, we prove the following.
Theorem 6.6. LetK be a hyperbolic closed 3–braid. From the Jones polynomial JK (t), we
deﬁne ζK,ζ ′
K as follows. Let
ζK =
{
βK, if |αK| = 1
0, otherwise and ζ ′
K =
{
β′
K, if |α′
K | = 1
0, otherwise.
Deﬁne ζ = max {|ζK|, |ζ ′
K|}. Then
4v3 ·ζ − 281 < vol(S3/integerdivideK) < 4v8 (ζ + 1).
Furthermore, the multiplicative constants in both the uppe r and lower bounds are sharp.
We remark that the quantity ζ = max {|ζK|, |ζ ′
K|}, as deﬁned in Theorem 6.6, will also
serve to estimate the volumes of alternating links, sums of a lternating tangles, and highly
twisted adequate links. In other words, this quantity estim ates the volume of every family of
knots and links where the volume is known to be bounded above a nd below in terms of the
Jones polynomial. The quantity ζ depends only on the ﬁrst two and last two coeﬃcients of
JK (t), and can be taken as positive evidence for Question 1.2. On t he other hand, we also
show that no function of βK and β′
K alone can satisfy equation (1) for all hyperbolic knots.
Theorem 6.8. There does not exist a function f (·, ·) of two variables, together with constants
Ci> 0, i = 1,..., 4, such that
C1f (βK,β ′
K ) −C2 < vol(S3/integerdivideK) < C3f (βK,β ′
K ) +C4
for every hyperbolic knot K. In other words, the second and next–to–last coeﬃcients of th e
Jones polynomial do not coarsely predict the volume of a knot .
Theorem 6.8 relies on two families of examples: adequate Mon tesinos knots and closed
3–braids. For both of these families, Stoimenow found upper bounds on volume in terms of
outer coeﬃcients of the Jones polynomial [54]. While Theore m 6.8 implies that equation (1)
cannot hold for any function of βK and β′
K alone, there might still be an aﬃrmative answer
to Question 1.2 that uses other coeﬃcients.
