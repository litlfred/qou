---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-054-41-the-schottky-problem-in-genus-4-71
section_title: "The Schottky problem in genus 4 71"
section_number: 4.1
pages: 79-81
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
To avoid case distinctions, from now on we putG(g) = SOg!(C) if g is
odd andG(g) = Spg!(C) if g is even. The main goal of this chapter is to
prove the following weaker version of our conjecture, extending ideas that
have been used in dimensiong = 4 in the earlier preprint [67].
THEOREM 4.2. For a general complex ppav X of dimension g with a
symmetric theta divisorΘ one has
G(δΘ) = G(g),
and δΘ corresponds to the standard representation of this group.
As we have remarked above, this essentially means that for a general
ppav the Tannaka group of the theta divisor is as large as possible — the
main task will be to ﬁnd sufﬁciently large lower bounds on this group. By
a constructibility argument it sufﬁces to do this for the generic ﬁbre of a
suitable family of ppav’s over a smooth complex algebraic curveS. So we
can apply degeneration methods: By theorem 3.15 the Tannaka group of the
generic ﬁbre admits those of the perverse sheaves of nearby cycles on the
special ﬁbres as subquotients. With this in mind, we collect in section 4.3
some general properties of the monodromy ﬁltration that allow to control
the nearby cycles in concrete geometric situations. The crucial part of our
argument is then given in section 4.4 where we consider three degenerations
of a generic ppav — in one of them the theta divisor becomes nodal, and
in the other two the ppav degenerates into a product of ppav’s resp. into a
Jacobian variety. In each case the nearby cycles contain a large irreducible
constituent that can be controlled geometrically, and this will reduce the
proof of our theorem to arguments in representation theory to be worked
out in section 4.5.
4.1. The Schottky problem in genus 4
Before we come to the proof of theorem 4.2, let us brieﬂy discuss its
connection with the Schottky problem. Recall that in dimensiong≥ 4 the
Andreotti-Mayer locusNg⊂ Ag of ppav’s with a singular theta divisor is
itself a divisor with precisely two irreducible components [26]. One of the
components is the locusθnull,g of all ppav’s with a vanishing theta null; the
other component contains the closureJg of the locus of Jacobian varieties
and forg = 4 is equal to it [8]. This being said, in dimensiong = 4 we can
sharpen the formulation of theorem 4.2 as follows.
THEOREM 4.3. For g= 4 the locus of all ppav’s with G(δΘ)⁄= Sp24(C)
is contained in a Zariski-closed subset ofA4 whose divisorial components
are preciselyJ4 and θnull,4.
72 Chapter 4 – The Tannaka group of the theta divisor
The proof of this will be given along with our proof of theorem 4.2,
based on the observation that every divisor onA4 intersects the locus of
Jacobian varieties — on the Tannakian side this information is encoded in
part (3) of proposition 4.12 below. Assuming the theorem, we recover the
following result of [67].
COROLLARY 4.4. For g= 4 the invariant G= G(δΘ) determines both
the Jacobian locus and the theta null locus
J4⊂ A4 and θnull,4⊂ A4.
Proof.Theorem 4.3 says that the closure of the locus of all ppav’s inA4
withG⁄= Sp24(C) is a proper Zariski-closed subset, withJ4 and θnull,4 as
its only divisorial components. By the result quoted at the beginning of this
chapter, the groupGis equal toSl6(C)/µ3 for a general ppav in the Jacobian
locusJ4. By way of contrast, for a general ppav inθnull,4 the degeneration
argument in part (2) of proposition 4.12 below shows that the irreducible
representationW∈ RepC(G) corresponding to the simple perverse sheafδΘ
has dimension dim(W) = g!−2 = 22. In particular, for such a ppav the
groupG is different fromSl6(C)/µ3 since by [3] the latter does not admit
an irreducible representation of dimension 22. □
In this context, we remark that the possible singularities of theta divisors
in dimensiong = 4 can be described explicitly as follows. LetJ4,hyp be
the closure of the locus of Jacobian varieties of hyperelliptic curves, and
denote byA4,dec⊂ θnull,4∩ J4 the locus of decomposable ppav’s. Then
the following types of singularities occur.
LEMMA 4.5. a) For ppav’s inJ4\ (θnull,4∩ J4) the theta divisors
have precisely two singularities, both ordinary double points. b) For ppav’s
in θnull,4\(θnull,4∩J4) they have only one singularity, again an ordinary
double point. c) On(θnull,4∩J4)\ (J4,hyp∪A4,dec) they have only one
singular point, and there the Hesse matrix of the Riemann theta function
has rank three. d) OnJ4,hyp\(J4,hyp∩A4,dec) the singular locus of each
theta divisor has dimension one. e) OnA4,dec it has dimension two.
Proof. It has been shown in [54, thm. 10 and cor. 15] that fora), b)
andc) the rank of the Hesse matrix at any singular point of the theta divisor
is the given one. In particular, in casesa) andb) only isolated singularities
occur. This also holds forc) since by Riemann’s singularity theorem the
singular locus of the theta divisor on a Jacobian variety is the Brill-Noether
subvarietyW1
g−1, which in the non-hyperelliptic case has dimensiong−4 by
Martens’ theorem [6, th. 4.5.1]. The number of singularities can be obtained
from [20, sect. 10] and from [8] and [81, case b2, p. 55f]. Partd) follows
again from Martens’ theorem, ande) is trivial. □
