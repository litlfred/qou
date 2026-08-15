---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-005-15-modules-over-the-habiro-ring-of-k-indexed-by
section_title: "Modules over the Habiro ring of K indexed by K_3(K)"
section_number: 1.5
pages: 8-11
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
collection of modulesHR,ξ over the Habiro ringHR (withR given in (11)) labelled by elements
ofξ∈K3(K). (Philosophically, the modules ought to be labelled by K3(R). However, given
the isomorphism K2r−1(R)≃ K2r−1(K) for r > 1 (see e.g., Sec.5.2 of Weibel [45] as well
as [10, Eqn.(33)]), we choose to label our modules by K3(K).) These modules turn out to
be the home of perturbative quantum knot invariants, as we will see in Section 1.7.
Before explicitly defining these modules, we recall the original motivation for their ex-
istence. In Section 1.2, we recalled from [26] a series Φ( h) coming from the figure eight
knot 4 1. Its properties become much better when one passes to a “completion” given by
bΦ(h) = exp(iVol(41)/h) Φ(h), where Vol(4 1) is given by 2 Im(Li 2(eπi/3)) = 2.0299··· . This
dilogarithm is actually equal to a particular value of a regulator, which is a function from
K3(Q(√−3)) to C/(2πi)2Z. This already indicates a link between this series and algebraic
K-theory of the field Q(√−3), but work of Calegari and two of the authors [10] showed that
this link is even stronger. The asymptotics of the same Kashaev invariant at different roots
of unity gives similar series, but now the constant term at q =ζm (at least if 3|m) contains
the m-th root of a unit in Q(√−3,ζm) which up to m-th powers depends only on the class
ξ∈K3(Q(√−3) giving the volume. We want our module HR,ξ to contain an element whose
expansion at q = e−h is Φ(h). In this section, we will give such a definition. Its elements
have power series expansions at roots of unity with subtle integrality properties that the
series Φ(h) (and all the other series Φζ(h)) indeed satisfy. To achieve this, since our point of
view is p-adic for varying p, we will have to replace the completion bΦ(h) by a p-adic version
in which the usual dilogarithm is replaced with a p-adic dilogarithm. This motivates the
Definition 1.3 given below.
The elements ofHR,ξ will give collections of power series at roots of unity whose constant
terms contain the m-th root of the above mentioned unit εm(ξ) defined in [10, Thm.1.5].
This unit comes from the Chern class map cζm of algebraic K-theory
εm = c2
ζm :K3(K)→ K(ζm)×/(K(ζm)×)m (16)
and satisfies the property that ( σγεm(ξ))γ/εm(γ) is canonically an m-th power for every
integerγ prime to m, where σγ is the automorphism sending ζm toζγ
m. In [10] this property
is called χ−1-equivariance. In more invariant terms, this is a map from the set K3(K)
towards the groupoid of µm-torsors over K(ζm) (with this χ−1-equivariance datum); in fact,
these µm-torsors extend (necessarily uniquely) to OK[ζm]. Indeed, the mod m ´ etale Chern
character gives a canonical map
cζm :K3(K)∼=K3(OK)→H1(OK, Z/m(2))→H1(OK[ζm], Z/m(2))(Z/mZ)×∼=H1(OK[ζm],µm)χ−1
,
(17)
where the last isomorphism is induced by cup product with ζm ∈ H0(OK[ζm],µm)χ. In
particular, the units εm(ξ) can be chosen to be integral at any given finite set of places, and
we will always implicitly fix such a choice at the relevant places. We remind the reader that
K3(K), at least after tensoring with Q, is isomorphic to the Bloch group B(K) and that in
THE HABIRO RING OF A NUMBER FIELD 9
this interpretationξ is represented as a formal linear combinationP
i[xi], withxi∈ K×∖{1},
satisfyingP
ixi∧ (1−xi) = 0∈∧ 2 K×. We will use both points of views in this paper.
To give a first impression of the modules HR,ξ overHR, we note that their base change
to K[ζm][ [x] ] is induced by the µm-torsor described above (along the map from µm-torsors
to Gm-torsors, i.e. line bundles), noting that the µm-torsor deforms uniquely to the power
series ring. In concrete terms, this is the collection of power series
fm(x) ∈ εm(ξ)1/m K[ζm][ [x] ] (18)
whose leading term contains the m-th root εm(ξ)1/m as a factor.
This determines the line bundle (described as usual by its collection of power series)
overR⊗Z Q = K. In order to descend to R, we need to have a p-adic description. For this
we use the p-adic dilogarithm map
Dp :K3(Kp)→ Kp, Kp = R∧
p [ 1
p] = K⊗Q Qp (19)
of Coleman [11], which coincides with thep-adic regulator map as shown in Besser–de Jeu [7,
Thm.1.6(2)] and is discussed in detail in Section 3.1. With these maps we can define HR∧p,ξ
via globally invertible group-like sections, which can be thought of as an upgrading to power
series of the collection of units defined in [10].
Definition 1.3. Fix ξ∈K3(K) and a prime p. An invertible Lp(ξ)-section is a collection
f(q) = ( fm(x))m≥1,(m,p)=1, f m(x) ∈ εm(ξ)1/m (R∧
p [ζm]× +xKp[ζm][ [x] ]) (20)
of power series (here x =q−ζm as usual) that satisfies
log
φpbf(qp)
bf(q)p

∈
Y
m≥1, (m,p)=1
p
xR∧
p [ζm][ [x] ]. (21)
Here bf(q) = (bfm(x))m is the formal completion of f defined by
log(bfm(x)) = Dp(ξ)
m2 log(q) + log(fm(x)) ∈ x−1 Kp[ζm][ [x] ]. (22)
We denote theHR∧p -span of invertible Lp(ξ)-sections byHR∧p,ξ.
The construction of such invertible sections can be done via telescoping sums. Note also
that the condition (21) is a logarithmic version of that used in Dwork’s lemma (see Lemma 3.4
of Section 3.2). The existence of invertible sections and Dwork’s lemma makes it easy to see
thatHR∧p,ξ is a rank one module over HR∧p . This is summarised in the following theorem,
whose proof will be given in Section 3.2.
Theorem 1. Let K be a number field, and ∆ a number divisible by its discriminant and
by 6. For ξ∈ K3(K) and p a prime with (p, ∆) = 1 , there exists invertible Lp(ξ)-sections.
Moreover,HR∧p,ξ is a free rank 1 module overHR∧p .
In Section 3.2 we will construct some natural and explicit invertible sections. These
sections will depend on an expression of ξ as a Zp-linear combination of symbols associated
to roots of unityζ in Kp, and on the expansion of the infinite Pochhammer symbol (q1/2ζ;q)∞.
While these collections are only defined atζm withm prime top, they have a unique extension
10 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
to all roots of unity satisfying integrality and gluing conditions, as shown in Corollary 3.7 of
Section 3.2.
We can patch together these modules over the p-completed ring to define modules over
the global one. This is completely analogous to the description of the global Habiro ring
from thep-completed Habiro ring via the diagram (15). These collections are motivated and
modelled on series coming from perturbative Chern–Simons theory at roots of unity.
Definition 1.4. Fix ξ∈K3(K). TheHR-moduleHR,ξ consists of collections
f(q) = ( fm(x))m≥1, f m(x) ∈ εm(ξ)1/m K[ζm][ [x] ] (23)
such that under the canonical map K→ Kp we have (fm(x))m≥1,(m,p)=1∈H R∧p,ξ, and the
following gluing condition for γ∈ Z>0 is satisfied:
f(qγ)γf(q−1) ∈ HR[1/γ]|γ, (24)
whereHR[1/γ]|γ denotes the restriction of HR[1/γ] to collections of power series at roots of
unityζm with m prime to γ, as introduced after Definition 1.1.
Note that the function (γ∗f)(q) :=f(qγ) behaves like an element of the moduleHR[1/γ],ξ/γ|γ
(where again|γ denotes the restriction to roots of unity of order prime to γ). The issue is
that one must make sense ofξ/γ as an element ofK3. We also note that theχ−1-equivariance
of εm makes the a priori ambiguity of their m-th roots disappear in equation (24). For the
moment we assume that p is prime to 6 (cf. the remark in Section 1.6), because only then
does the above condition yield the correct gluing condition: one needs that there is some γ
prime to p such that γ2− 1 is also prime to p (see the end of the proof of Lemma 3.6 of
Section 3.2). Moreover, notice that f(qγ)γf(q−1) determinesf(q) forq near all roots of unity
of order prime to 6 as we vary γ∈ Z>0. More generally, one can consider the combinations
f(qγ1)··· f(qγn)f(q−γ′
1)··· f(q−γ′
n′), where P
kγ−1
k −P
kγ′−1
k = 0, the previous case being
n = γ, γi = γ, n′ = 1 and γ′
1 = 1. The important property of these combinations is that
including the polar part of equation (22) has no effect on the expansions at roots of unity
with order prime to Q
kγk
Q
kγ′
k. For example, taking q = ζm +x with (m,γ ) = 1 we find
that f(qγ)γf(q−1) = bf(qγ)γbf(q−1).
The moduleHR,ξ associated to the global ring is not necessarily free, but it is of rank one
and locally free, i.e., invertible. This was observed numerically in our early experiments. In
these experiments, we compared power series coming from two knots giving the same class
in K3(K) (in particular, the 5 2 and (−2, 3, 7)-pretzel knots with the field K being the cubic
field of discriminant −23 with R being its ring of integers with 23 inverted). We observed
that these series seemed to satisfy a linear dependence over HR. This numerical observation
is indeed true and is implied by Theorem 5 below and the following:
Theorem 2. We haveHR,0 =HR. In general, multiplication gives a canonical isomorphism
HR,ξ⊗HRHR,ξ′ ∼= HR,ξ+ξ′. (25)
In particular HR,ξ is an invertible HR-module, and ξ7→H R,ξ defines a homomorphism of
abelian groups
K3(K) → Pic(HR). (26)
THE HABIRO RING OF A NUMBER FIELD 11
Here, Pic(HR) denotes as usual the abelian group of line bundles on Spec(HR), i.e., the group
under tensor product of invertibleHR-modules. This map is actually a homomorphism from
the abelian group K3(K) (in the category of sets) to the abelian group of line bundles
onHR (in the category of groupoids), i.e., to every element in K3(K) we obtain an invertible
HR-module as opposed to just an isomorphism class.
We observe that, just as forHR, the definition of the module HR,ξ becomes simpler when
K is abelian over Q. Indeed, in that case the field K can be embedded in Q(ζ) for some
root of unity ζ. Assume that ξ ∈ B(K) can be represented as a Gal( Q(ζ)/K)-invariant
combinationξ =P
jnj[ζj]. (We do not know whether this is always the case, at least after
tensoring with Q, but it certainly holds in many examples, e.g., the example coming from
the figure eight knot, where ξ = 2[ζ6].) Then HR,ξ contains the element Q
j(q1/2ζj;q)
nj
∞ and
is freely generated by this element as an HR-module. Compare Theorem 10 of Section 3.2.
The next proposition summarises some of the properties of these HR-modules and the
operation, defined after Definition 1.4,f7→γ∗f. Its proof, along with the proof of Theorem 2,
are given in Section 3.3.
Proposition 1.5. We have:
(a) If f∈H R,ξ, then τf∈H R,−ξ, where τf := (−1)∗f is the involution f(q)7→f(q−1).
(b) If f,g ∈H R,ξ, then f·τg∈H R. Moreover, there exist a,b∈H R such that af =bg.
(c) If f∈P R and γ,γ′∈ Z are non-zero then (γγ′)∗f = γ∗(γ′∗f).
(d) Iff∈H R,ξ andγ a positive integer, then (γ∗f)γ∈H R[γ−1],ξ|γ (see Definitions 1.1 and 1.4).
(e) If f∈H R,ξ and m∈ Z>0 and fm(x) = 0 then fpm(x) = 0 for all primes p not diving ∆.
(f ) If f(q)∈H R,ξ, then fm(0)∈R[ζm,ε 1/m
m ] for (m, ∆) = 1.
Remark 1.6. The operation τ corresponds geometrically to the orientation reversal of an
oriented manifold, i.e., the quantum invariants of an oriented three-manifold with the oppo-
site orientation are equal to the operation τ applied to the original invariants.
