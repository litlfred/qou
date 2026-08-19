---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-000-1-setting-the-stage
section_title: "Setting the stage"
section_number: 1
pages: 1-7
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
---
2. Algebra of BPS states and its representations 7
3. B-model and matrix factorizations 10
4. Colored HOMFLY homology 15
5. Mirror symmetry for knots 25
6. Unreduced colored HOMFLY homology 30
Appendix A. Notations 36
Appendix B. Kauﬀman and S2 homologies of the knots 8 19 and 9 42 37
Appendix C. H3 homology of the ﬁgure-eight knot 41
Appendix D. Computation of the unreduced homology of the unknot 42
References 44
1. Setting the stage
Quantum knot invariants were introduced in 1980’s [ 1, 2 ]: for every represen-
tation R of a Lie algebra g, one can deﬁne a polynomial invariant
P
g,R
(K) of a
knot K. Its reduced version is
(1.1) P g,R (K) = P
g,R
(K)
P
g,R
( )
,
1
2 SERGEI GUKOV AND MARKO STO ˇSI ´C
where denotes the unknot.
A categoriﬁcation of the polynomial P g,R (K) (or its unreducedversion P
g,R
(K))
is a doubly-graded homology theory 1Hg,R (K) whose graded Euler characteristic is
equal to P g,R (K). In other words, if P g,R (K)(q, t) denotes the Poincar´ e polynomial
ofHg,R (K), then we have
P g,R (K)(q) = P g,R (K)(q, t =−1) .
Unlike P g,R (K), the explicit combinatorial deﬁnition of Hg,R (K) exists for very
few choices of g and R. However, physics insights based on BPS state counting and
Landau-Ginzburg theories predict various properties and a very r igid structure of
these homology theories.
One of the ﬁrst results was obtained in [ 3] for g = sl(N ) and its fundamental
representation R = . This work builds on a physical realization of knot homologies
as spaces of BPS states [ 4, 5 ]:
(1.2) Hknot = HBPS .
Among other things, this relation predicts the existence of a polyno mial knot in-
variantP (K)(a, q, t), sometimes called the superpolynomial, such that for all suf-
ﬁciently large N one has
(1.3) P sl(N ), (K)(q, t) = P (K)(a = qN , q, t) .
Moreover, the polynomial P (K)(a, q, t) has nonnegative coeﬃcients and is equal
to the Poincar´ e polynomial of a triply graded homology theory H (K) that cate-
goriﬁes the reduced two-variable HOMFLY polynomial P (K)(a, q), and similarly
for the unreduced invariants. This triply graded theory comes equ ipped with a
collection of diﬀerentials {dN}, such that the homology of H (K) with respect to
dN is isomorphic to Hsl(N ), (K).
There are only two triply-graded knot homologies that have been st udied in
the literature up to now. Besides the above-mentioned HOMFLY hom ology, the
second triply-graded theory, proposed in [ 6], similarly uniﬁes homological knot
invariants for the N -dimensional vector representation R = V of g = so(N ) and g =
sp(N ). This triply-graded theory HKauﬀ (K) comes with a collection of diﬀerentials
{dN}, such that the homology with respect to dN for N > 1 is isomorphic to
Hso(N ),V (K), while the homology with respect to dN for even N < 0 is isomorphic
toHsp(−N ),V (K). Since the graded Euler characteristic of HKauﬀ (K) is equal to the
(reduced) Kauﬀman polynomial of K,HKauﬀ (K) is called the Kauﬀman homology
of a knot K.
One way to discover diﬀerentials acting on all of these knot homology theories
is via studying deformations of the potentials and matrix factorizat ions in the cor-
responding Landau-Ginzburg theories (see section 3 for details). In particular, in
the case of the Kauﬀman homology one ﬁnds a peculiar deformation t hat leads to
a “universal” diﬀerential d→ and its conjugate d←, such that the homology with
respect to these diﬀerentials is, in both cases, isomorphic to the tr iply-graded HOM-
FLY homologyH (K).
A careful reader may notice that most of the existent results rev iewed here deal
with the fundamental or vector representations of classical Lie a lgebras (of Cartan
1All homologies in this paper are deﬁned over Q.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 3
type A, B, C, or D). In this paper, we do roughly the opposite: we focus mainly
on g = sl(N ) but vary the representation R. In particular, we propose inﬁnitely
many triply-graded homology theories associated with arbitrary sy mmetric ( Sr)
and anti-symmetric (Λ r) representation of sl(N ). Moreover, these colored HOM-
FLY homology theories come equipped with diﬀerentials, such that th e homology,
say, with respect to dSr
N is isomorphic to Hsl(N ),S r
(K), and similarly for R = Λ r.
Remarkably, in addition to the diﬀerentials labeled by N (for a given r) we also
ﬁnd coloreddiﬀerentials that allow to pass from one triply graded theory to anot her,
thus relating homological knot invariants associated with diﬀerent r epresentations!
Speciﬁcally, for each pair of positive integers ( r, m) with r > m , we ﬁnd a
diﬀerential dr→m, such that the homology of HSr
(K) with respect to dr→m is iso-
morphic to HSm
(K). Similarly, in the case of anti-symmetric representations, we
ﬁnd an inﬁnite sequence of triply-graded knot homologies HΛ r
(K), one for every
positive integer r, equipped with colored diﬀerentials that allow to pass between
two triply-graded theories with diﬀerent values of r.
The colored diﬀerentials are a part of a larger algebraic structure t hat becomes
manifest in a physical realization of knot homologies as spaces of BPS states. As it
often happens in physics, the same physical system may admit seve ral mathemat-
ical descriptions; a prominent example is the relation between Donald son-Witten
and Seiberg-Witten invariants of 4-manifolds that follows from phys ics of super-
symmetric gauge theories in four dimensions [ 7]. Similarly, the space of BPS states
in (1.2) admits several (equivalent) descriptions depending on how o ne looks at the
system of ﬁve-branes in eleven-dimensional M-theory [ 4] relevant to this problem.
Speciﬁcally, for knots in a 3-sphere S3 the relevant system is a certain conﬁg-
uration of ﬁve-branes in M-theory on R× M4× X, where M4∼
= R4 is a 4-manifold
with isometry group U (1)P× U (1)F and X is a non-compact toric Calabi-Yau 3-
fold (both of which will be discussed below in more detail). And, if one loo ks at
this M-theory setup from the vantage point of the Calabi-Yau spac e X, one ﬁnds
a description of BPS states via enumerative geometry of X. Furthermore, for sim-
ple knots and links that preserve toric symmetry of the Calabi-Yau 3 -fold X the
study of enumerative invariants reduces to a combinatorial proble m of counting
certain 3d partitions (= ﬁxed points of the 3-torus action [ 8]), hence, providing a
combinatorial formulation of knot homologies in terms of 3d partition s [ 9, 10 ].
On the other hand, if one looks at this M-theory setup from the van tage point
of the 4-manifold M4, one can express the counting of BPS invariants in terms
of equivariant instanton counting on M4. In this approach (see e.g. [11]), the
“quantum” q-grading and the homological t-grading on the space (1.2) originate
from the equivariant action of U (1)P× U (1)F on M4.
A closely related viewpoint, that will be very useful to us in what follow s, is
based on the ﬁve-brane world-volume theory [ 12]. Let us brieﬂy review the basic
ingredients of this approach that will make the relation to the setup of [ 4] more
apparent. In both cases, knot homology is realized as the space of BPS states and,
as we shall see momentarily, the physical realization of the triply-gr aded knot ho-
mology proposed in [ 4] is essentially the large- N dual of the system realizing the
doubly-graded knot homology in [ 12]. This is very typical for systems with SU (N )
4 SERGEI GUKOV AND MARKO STO ˇSI ´C
gauge symmetry 2 which often admit a dual “holographic” description that com-
prises all N in the same package and leads to useful computational techniques [13].
In the case of sl(N ) homological knot invariants, the ﬁve-brane conﬁguration
described in [ 12, sec. 6] is the following:
space-time : R× T∗W× M4
N M5-branes : R× W× D(1.4)
M5-brane : R× LK× D
Here, W is a 3-manifold and D∼
= R2 is the “cigar” in the Taub-NUT space M4∼
=
R4. The Lagrangian submanifold LK⊂ T∗W is the conormal bundle to the knot
K⊂ W ; in particular,
(1.5) LK∩ W = K .
In all our applications, we consider W = S3 (or, a closely related case of W = R3).
Similarly, the setup of [ 4] can be summarized as
space-time : R× X× M4(1.6)
M5-brane : R× LK× D
where X is the resolved conifold, i.e. the total space of the O(−1)⊕O (−1) bundle
over CP1. From the way we summarized (1.4) and (1.6), it is clear that they hav e
many identical elements. The only diﬀerence is that (1.4) has extra M 5-branes
supported on R× W× D, whereas (1.6) has a diﬀerent space-time (with a 2-cycle
in the Calabi-Yau 3-fold X), which is exactly what one expects from a holographic
duality or large- N transition [ 14, 15 ].
Indeed, what is important for the purpose of studying the space o f BPS states,
HBPS, is that both (1.4) and (1.6) preserve the same amount of supersy mmetry
and have the same symmetries:
• time translations: both systems have a translation symmetry along the
time direction (denoted by the R factor in (1.4) and (1.6)). Therefore, in
both cases, one can ask for a space of BPS-states — on multiple M5- branes
in (1.4), and on a single M5-brane in (1.6) — which is precisely what was
proposed as a candidate for the sl(N ) knot homology (resp. HOMFLY
homology).
• rotation symmetries:
(1.7) U (1)P× U (1)F
Here, the two U (1) factors correspond, respectively, to the rotation sym-
metry of the tangent and normal bundle of D ∼
= R2 in a 4-manifold
M4 ∼
= R4. In particular, in both frameworks (1.4) and (1.6), the for-
mer is responsible for the q-grading of HBP S, which corresponds to the
conserved angular momentum derived from the rotation symmetry of D.
A well-known feature of the large- N duality is that the rank of the gauge group
turns into a geometric parameter of the dual system ( cf. [13] or [14]). In the present
case, it is the K¨ ahler modulus of the Calabi-Yau 3-fold X =OCP1(−1)⊕O CP1(−1):
(1.8) N ∼ log(a) = Vol( CP1) .
2The same is true for other classical groups.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 5
The reason we denote the K¨ ahler parameter by log( a) rather than a is that with
this convention a = qN is the standard variable of the HOMFLY polynomial / knot
homology.
W
−1
2W
−1
1W1
1
vol(CP1)
W
−1
3
N
32−1 0 1−2−3
W
1
W
1
23
region
Szendroi
Figure 1. For the conifold X, the space of stability conditions
is one-dimensional. It is parametrized by the K¨ ahler parameter
N∼ log(a) = Vol(CP1). This space is divided by walls of marginal
stability into a set of chambers, which can be identiﬁed with the
set of integers Z.
Another feature familiar to the practitioners of the reﬁned / motiv ic Donaldson-
Thomas theory is that HBPS can jump as one varies stability conditions [ 16, 17,
18, 19, 20, 21 ]. Thus, in a closely related type IIA superstring compactiﬁcation
on a Calabi-Yau 3-fold X, the stability parameters are the K¨ ahler moduli of X,
and in the present case there is only one K¨ ahler modulus (1.8) given b y the volume
of the CP1 cycle in X. Therefore, we conclude that the space (1.2) can jump as
one changes the stability parameter N∼ Vol(CP1).
Luckily, in the case where X is the total space of the O(−1)⊕O (−1) bundle
over CP1 relevant to our applications, the wall-crossing behavior of the reﬁn ed
BPS invariants has been studied in the literature [ 22, 23, 18 ]. The one-dimensional
space of stability conditions is divided into a set of chambers illustrate d in Figure 1.
In each chamber, HBPS is constant and the jumps of closed BPS states occur at
the wallsW±1
n characterized by diﬀerent types of “fragments”:
(1.9)
W 1
n : D2/D0 fragments
W−1
n :
D2/D0 fragments
W 0
n : D0 fragments
Notice, the set of chambers in this model can be identiﬁed with Z, the set of integer
numbers. As we explain in the next section, this is not a coincidence. N amely,
as we shall see, every fragment corresponds to a diﬀerential act ing on the space
(1.2), so that in the present example one ﬁnds a set of diﬀerentials {dN} labeled
by N∈ Z.
The diﬀerentials {dN} are part of the homological algebra of knots / BPS
states, depending on whether one prefers to focus on the left or right side of the
relation (1.2). For larger representations, in addition to the diﬀere ntials{dN} one
ﬁnds colored diﬀerentials that allow to pass between homology theor ies associated
with diﬀerent R. Even though a combinatorial deﬁnition of the majority of such
6 SERGEI GUKOV AND MARKO STO ˇSI ´C
theories, with all the diﬀerentials, is still missing, their structure (d educed from
physics) is so rigid that enables computation of the homology groups for many
knots and passes a large number of consistency checks.
In particular, by computing the triply-graded homologies HSr
(K) andHΛ r
(K)
for various knots, we ﬁnd the following surprising symmetry betwee n the two the-
ories:
(1.10) HΛ r
i,j, ∗(K) ∼
= HSr
i,−j,∗(K) .
One of the implication is that HSr
(K) andHΛ r
(K) can be combined into a single
homology theory!
Conjecture 1.1. For every positive integer r, there exists a triply-graded
theoryHr(K) together with a collection of diﬀerentials {dr
N}, with N∈ Z, such
that the homology of Hr(K) with respect to dr
N , for N > 0, is isomorphic to
Hsl(N ),S r
(K), while the homology of Hr(K) with respect to dr
N , for N < 0, is
isomorphic (up to a simple regrading) to Hsl(−N ), Λ r
(K).
Moreover, it is tempting to speculate that the symmetry (1.10) ext ends to all
representations:
(1.11) “mirror symmetry” : Hλ (K) ∼
= Hλ t
(K) ,
where λ and λt are a pair of Young tableaux related by transposition (mirror
reﬂection across the diagonal), e.g.
λ =
←→ λt =
The symmetry (1.11) has not been discussed in physical or mathema tical literature
before.
While we oﬀer its interpretation in section 5.3, we believe the mirror sym metry
for colored knot homology (1.11) deserves a more careful study, both in physics as
well as in mathematics. In particular, its deeper understanding sho uld lead to the
“categoriﬁcation of level-rank duality” in Chern-Simons theory, wh ich is the origin
of the simpler, decategoriﬁed version of (1.11):
(1.12) P λ (K)(a, q) = P λ t
(K)(a, q−1)
for colored HOMFLY polynomials [ 24, 25, 26, 27 ], and extends the familiar sym-
metry q ↔ q−1 of the ordinary HOMFLY polynomial. We plan to pursue the
categoriﬁcation of level-rank duality and to study the new, homolog ical symmetry
(1.11) in the future work.
Organization of the paper. We start by explaining in section 2 that, in gen-
eral, the space of open BPS states forms a representation of the algebra of closed
BPS states. Then, in section 3 we review elements of the connection between string
realizations (1.4)–(1.6) of knot homologies and Landau-Ginzburg mo dels that play
an important role in mathematical formulations of certain knot homo logies based
on Lie algebra g and its representation R. In particular, we illustrate in simple
examples how the corresponding potentials Wg,R can be derived from the physical
setup (1.4)–(1.6) and how deformations of these potentials lead to various diﬀer-
entials acting on Hg,R (K). This gives another way to look at the algebra acting
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 7
on (1.2). Based on these predictions, in section 4 we summarize the m athematical
structure of the triply-graded homology HSr
(K), together with its computation for
small knots. Section 5 lists the analogous properties of the homolog y associated
with anti-symmetric representations, and explains the explicit form of the “mirror
symmetry” (1.10) between symmetric and anti-symmetric triply-gr aded theories.
Unreduced triply-graded theory for symmetric and anti-symmetr ic representations
is brieﬂy discussed in section 6. In appendix A we collect the list of our n otations,
whereas in appendix B we present the computations of the S2, Λ 2 and Kauﬀ-
man triply-graded homology for knots 8 19 and 9 42. These particular examples of
“thick” knots provide highly non-trivial tests of all the properties of the homologies
presented in the paper. Appendix C contains the computation of th e S3 and Λ 3
homology of the ﬁgure-eight knot 4 1. Finally, appendix D collects some notations
and calculations relevant to the unreduced colored HOMFLY polynom ial of the
unknot discussed in section 6.
