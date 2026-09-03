---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-5
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
2 Mathematical background. 5
2.1 Geometry of posets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Nets of C*-algebras. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Nets and presheaves of tensor categories. . . . . . . . . . . . . . . . . . . . . . . . . . 9
3 Presheaves in quantum ﬁeld theory . 13
3.1 Charge structure. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2 Symmetry. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.3 The main result. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 Group bundles as global gauge symmetries. 20
4.1 Twisted ﬁeld nets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.2 Twisted nets and background potentials. . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.3 Current algebras on S1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.4 Existence of ﬁeld nets with a given gauge symmetry. . . . . . . . . . . . . . . . . . . 26
5 Conclusions and the gerbe perspective. 28
A Symmetry and ﬁelds in globally hyperbolic manifolds. 30
1
1 Introduction.
In the ordinary approach to the theory of particle physics quantu m ﬁelds are fundamental objects,
but do not necessarily yield quantum observables because the prop erty of gauge invariance with
respect to a symmetry group must be imposed.
In algebraic quantum ﬁeld theory this point of view is subverted: at a ﬁrst stage only quan-
tum observables are considered, in the spirit that these contain all the physical informations of the
system under consideration. Thus one could ask whether the obse rvable quantities determine the
quantum ﬁelds and the gauge group, and the answer to this questio n is a pivotal result: quan-
tum ﬁelds and gauge group can be reconstructed, starting from t he observable algebra and the
set, called the superselection structure, of its physically relevant Hilbert space representations ( sec-
tors), that are interpreted as quantum charges ([17]). A celebrated m athematical byproduct is
the Doplicher-Roberts duality for compact groups vs. abstract symmetric tensor categories, that
generalizes Tannaka-Krein duality ([16]).
The mathematical scenario of the above construction is the one de ﬁned by Haag, Kastler and
then Araki in the middle sixties ([3, Chp.4],[23, Chp.III]): we have a base ∆ dc of the Minkowski
spacetime, the one of double cones, and, for any o ∈ ∆ dc , a C*-algebra Ao that is interpreted as
the one of quantum observables localized within o. Starting from this interpretation, it is natural
to require that there are inclusion *-morphisms
o′o :Ao →Ao′ : o′′o′ ◦o′o =o′′o , ∀o ⊆o′ ⊆o′′ ∈ ∆ dc . (1.1)
The pair A := (A, ) is known as the observable net and is usually – but not always – realized by
means of quantum ﬁelds in the sense of Wightman ([3, §4.8]). An important point is that ∆ dc is
a directed poset (partially ordered set) when ordered under inclusion, and this implies that we can
construct the inductive limit C*-algebra ⃗A := limj(A, ) that can be represented as a *-algebra of
operators on a ﬁxed Hilbert space. The superselection structure is then realized as a symmetric
tensor C*-category T of *-endomorphisms of ⃗A , and characterized as the dual of the compact
gauge group G. This means, in particular, that any ρ ∈ obj T deﬁnes a ﬁnite-dimensional, unitary
representation
uρ :G →UHρ (1.2)
such that Hρ appears in the ﬁeld algebra as the G-vector space spanned by a multiplet of ﬁeld
operators ψ1,...,ψ dim(uρ) , see ([17]).
Now, for generic spacetimes M in algebraic quantum ﬁeld theory it is customary to select a
convenient base ∆, according to the causal properties and symme tries of M . In in this way one
obtains, for example, the base of intervals with proper closure for the circle in conformal theory,
and the base of diamonds generating the topology of a globally hyperbolic spacetime, that is th e
setting of general relativity 1. We note that when elements of ∆ are arcwise and simply connected
(as intervals, double cones and diamonds), we are able to recover b ase-independent invariants of
M : the fundamental group π1(M ) ([35]), the ﬁrst singular and de Rham cohomology ([34]) and the
category of ﬂat bundles ([33, 34]). In several cases of physical in terest, in particular when π1(M ) is
not trivial (anti-de Sitter spacetimes, the circle, Aharonov-Bohm solenoids), ∆ cannot be directed,
see (2.3), and A is more generally a C*-precosheaf.
At the mathematical level, at the present time the most general su perselection structure available
on spacetimes with at least two spatial dimensions is the one deﬁned b y Brunetti and Ruzzi ([9]): it
1 In principle we may ﬁnd more that a suitable base for the purpo ses of algebraic quantum ﬁeld theory; but the
superselection structure turns out to be independent of the base up to isomorphism, see [35, Theorem 2.23].
2
is expressed in terms of cocycles z with values in the unitary precosheaf of A , that play the role of
charge transporters in the terminology of [30, 31]. This generalizes previous works by Guid o, Longo,
Roberts, Verch and Ruzzi ([30, 31, 22, 35]), with the motivation of clarifying the relations between
spacetime topology and structural properties of quantum ﬁeld th eory. The diﬀerence between the
approach of ([9]) and the one of [22, 35] is that in the ﬁrst case we ha ve that observable unitary
phases (that we call holonomies) appear when one performs a charge transport around a closed lo op
(see [9, §7]). This feature is typical in situations like the Aharonov-Bohm eﬀec t ([19, §15.5],[18, 1]),
where the electromagnetic ﬁeld gives rise to observable eﬀects indu ced by the holonomy of the vector
potential. The sectors studied in [22, 35], instead, have trivial holon omy in the above sense and for
this reason, following [9], we call them topologically trivial sectors .
The Brunetti-Ruzzi superselection structure yields a symmetric t ensor C*-category Z 1,•(A) de-
scribing charge composition, statistics and the particle-antipartic le correspondence ( conjugate sec-
tors), contains the set Z 1,•
t (A) of topologically trivial sectors as a full subcategory, and coincide s
with it when π1(M ) is trivial. Nevertheless at the present time it is not clear how to perf orm a
ﬁeld reconstruction as in the cases of Minkowski spacetime ([17]) an d topologically trivial sectors
in spacetimes where ∆ is directed ([22]), so we do not know whether it is possible to interpret the
dual group of Z 1,•(A) as the gauge group. We stress that this problem is open also for to pologically
trivial sectors in spacetimes with nontrivial fundamental group.
In the present paper we focus on globally hyperbolic spacetimes M with at least two spatial
dimensions. This last condition is motivated by the fact that we are int erested in sectors having
ordinary Fermi-Bose (para)statistics that, as well-known, in low-d imensional spacetimes are not
ensured (braided statistics may appear, see [22, §3]). Following the standard approach ([22, 35, 9])
we take ∆ as the base of diamonds whose basic properties, related t o the features of Cauchy surfaces
in M , are discussed in [22, §2.1] and [35, §3.2].
In one of our main results we prove that Z 1,•(A) is the category of sections of a presheaf S•
of symmetric tensor C*-categories with simple units (Theorem 3.5). Our intention is to use S• as
a tool to perform the ﬁeld reconstruction (see the following parag raphs and §5), anyway our result
also gives new light on the structure of Z 1,•(A): ﬁrst, it allows us to assign to sectors new invariants
of geometric nature, and, secondly, it suggests that the dual ob ject describing the superselection
structure may not to be merely a group.
In fact, as a consequence of abstract results for generic presh eaves ([39]), we have that Z 1,•(A)
can be characterized as a Tannaka-type dual ˆG of a locally constant – or, equivalently, ﬂat – group
bundle
G → M .
Thus we have G -equivariant ﬂat vector bundles in place of the unitary representa tions (1.2), and,
keeping in mind the above-mentioned interpretation of G-Hilbert spaces in terms of multiplets of
ﬁelds, this suggests that the charged ﬁeld operators that are ex pected to give rise to sectors in
Z 1,•(A) should be visualized in terms of local sections of ﬂat bundles. This ide a is not new and has
been formulated in the setting of quantum ﬁelds ([26, 2]), and is curr ently object of research ([27]).
An essential ingredient of the duality result is given by an embedding m orphism I : S• → C,
where C is a presheaf of full subcategories of the one of Hilbert spaces. Th is is a crucial point: I
may not exist or not to be unique, so the same holds for G which, when existing, will depend on
the choice of I . This does not exclude that there is a criterion to select a unique ”ph ysical” gauge
group bundle Gphys , nevertheless our results show that the isomorphism
Z 1,•(A) ≃ ˆGphys (1.3)
3
does not suﬃce to characterize Gphys , diﬀerently from what happens in the Minkowski spacetime.
From the point of view of invariants, we prove that any sector z deﬁnes a compact Lie group
Gz ⊆ U(d) , d ∈ N, and a projective representation
χz :π1(M ) →NGz/Gz ,
where NGz is the normalizer of Gz in U(d) . The importance of χz relies in the fact that an
embedding of S• deﬁnes, for any sector z , a lift
ˆχz :π1(M ) →NGz , χz = ˆχz modGz .
Lifts of χz are classiﬁed in cohomological terms by a NGz -valued 1–cochain uz deﬁned on the
simplicial set of ∆ (see Theorem 2.4). We interpret χz as a ﬂat principal NGz/Gz -bundle and
assign to it Cheeger-Chern-Simons characteristic classes living in th e odd cohomology of M (see
(2.6)) that vanish when z ∈Z 1,•
t (A).
To illustrate how group bundles yield gauge symmetries we construct ﬁeld C*-precosheaves
obtained by twisting a given ”topologically trivial” ﬁeld net with gauge gr oup G (Lemma 4.1).
The resulting C*-precosheaf is acted upon by a locally constant G-bundle and has representations
with nontrivial holonomy in the sense of [9], with the feature that non -triviality of the holonomy
is explicitly related with non-triviality of the gauge group bundle. In ac cordance with the above-
mentioned duality breaking, we have examples of inequivalent ﬁeld pre cosheaves – acted upon by
inequivalent group bundles – having the same observable net, this las t represented on a ﬁxed Hilbert
space (Cor.4.3). In §4.2 we discuss twists given by background classical potentials intera cting with
Dirac ﬁelds, obtaining relative phases analogous to those appearing in the Aharonov-Bohm eﬀect.
In §4.4, by using generalized free ﬁelds we show that for every locally con stant G-bundle (with
suitable structure group) there is a ﬁeld C*-precosheaf having it as a ”group” of global gauge
symmetries. The choice of considering free ﬁelds is dictated by the c urrent lack (at least at the
author knowledge) of nonperturbative, local quantum ﬁelds in spa cetimes with nontrivial π1(M ) and
spacetime dimension ≥ 3 ; but since our twisting procedure works independently of the spa cetime
dimension, in §4.3 we apply our result to conformal current algebras, where the c ases G = Z2n ,
n ∈ N, occur ([6, 7]).
The loss of uniqueness and – in theory – of existence of the dual gro up bundle can be avoided
already at the mathematical level, moving ourselves in the more conv enient setting of gerbes over
∆. This notion is illustrated in §5. We shall show in a forthcoming paper ([40]) that S• deﬁnes
a unique dual group gerbe ˇG, which may collapse to several, possibly inequivalent, group bundles
having the same dual. In this spirit, we prove in (5.2) that the above- mentioned cochains uz deﬁne
Lie group gerbes, that will turn out to be ﬁnite-dimensional repres entations of ˇG .
On these grounds we expect that, at least a priori , existence and uniqueness of a ﬁeld C*-
precosheaf having A as ﬁxed-point precosheaf are not ensured. Thus we give the notio n of ˇG -C*-
gerbe over a poset, deﬁned as a pair F = (F,i ) where F := {Fo}o∈∆ is a family of C*-algebras
with *-monomorphisms io′o : Fo → Fo′ , o ⊆ o′ , whose possible precosheaf structures are encoded
by ˇG (see (5.3): an interesting point is that ﬁxed-point algebras of a ˇG-C*-gerbe always have a
unique precosheaf structure). The fact that a unique ”ﬁeld gerb e” F may be reconstructed starting
from A and Z 1,•(A) is object of a work in progress, in which the presheaf S• plays a crucial role
(see §5). In this setting, we expect that some invariant of Z 1,•(A), beside (1.3), should allow us
to pick a unique ”physical” ﬁeld C*-precosheaf in which F would collapse, carrying a Gphys -action.
Constructions of ˇG -C*-gerbes, deﬁned by Wightman ﬁelds and labelled by projective repre sentations
of the fundamental group, are made in Theorem 5.1.
4
