---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-089-58-the-difference-morphism-129
section_title: "The difference morphism 129"
section_number: 5.8
pages: 137-139
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
one-dimensional trivial representation plus only a single further irreducible
representation. Now recall that by deﬁnitionG(dn) is a subgroup of the
symmetric groupSN. If V = CN denotes the permutation representation
of SN, then the monodromy representation of the subgroupG(dn) is simply
the restriction ofV to this subgroup. Note that V = 1⊕W splits as the
direct sum of the one-dimensional trivial representation plus an irreducible
representationW of SN with dimensionN−1. In these terms, the remarks
at the beginning of the proof amount to the statement that the restriction
ofW to the subgroupG(dn)≤ SN remains irreducible.
It is a general fact from the theory of permutation groups [91, th. 1(b)]
that any subgroup ofSN with this irreducibility property is a 2-transitive
subgroup. So by lemma D.1 in the appendix it will sufﬁce to show that for a
general curveC of genusg = 2n the monodromy groupG(dn) contains the
hyperelliptic one from lemma 5.26. For this we consider a degeneration of
a general curve into a hyperelliptic curve.
Let p : C→ S be a ﬂat, projective family of smooth curves of genusg
over a smooth quasi-projective complex base curveS, and assume that the
ﬁbre Cs = p−1(s) is hyperelliptic for some special points = s0∈ S(C) but
non-hyperelliptic for alls⁄= s0. The existence of such families follows
e.g. from [5, th. XII.9.1]. To rephrase our previous constructions in this
relative setting, letX be the relative Picard scheme ofC overS as deﬁned
in [15, sect. 8.2], and denote byCn = (C×S···× S C )/Sn the n-th relative
symmetric product. LetL be a Poincar´e bundle onC×S×Cn so that for
all s∈ S(C) and every divisorD∈ Cn,s(C) we haveL|Cs×{D}∼= OCs(D).
If p1, p2 : C×S Cn×S Cn→ C×S Cn denote the projections, then by the
universal property of the Picard scheme the line bundlep∗
1(L )⊗ p∗
2(L−1)
determines a morphismdn : Cn×S Cn→ X which on the ﬁbres over each
points∈ S(C) restricts to the difference morphism from above.
This being said, take an open subsetU⊆ X over whichdn is ﬁnite´etale
of degreeN and such that over every points∈ S(C) the ﬁbreUs =U∩Xs
is dense inXs. Applying the semicontinuity lemma 5.27 below to the local
system L = dn∗(CCn×SCn)|U, we obtain that the monodromy group ofdn
for a general curve of genusg = 2n contains the hyperelliptic one from
lemma 5.26 as a subgroup. This ﬁnishes the proof. □
For the above degeneration argument we have made use of the following
semicontinuity property for monodromy groups in families. Letf : U→ S
be a smooth morphism of complex algebraic varieties whose target is a
quasi-projective curveS, and consider a local systemL of complex vector
spaces onU with ﬁnite monodromy group. For any pointu∈ U(C) with
images = f (u) we denote by
G(u) = Im(π1(Us,u)−→AutC(Lu))
130 Chapter 5 – A family of surfaces
the monodromy group of the restrictionL|Us of the given local systemL to
the ﬁbreUs = f−1(s). Up to isomorphism the groupG(u) of course only
depends on the image points = f (u).
LEMMA 5.27. Let u0∈U(C). Then there is a non-empty Zariski-open
subset S′⊆ S with the following property: For all points u∈ f−1(S′(C)),
any identiﬁcationLu0
∼= Lu of the stalks gives rise to an embedding of the
monodromy groups such that the following diagram commutes.
G(u0)   ∃ //_ _ _ _ _ _ _
 _

G(u) _

AutC(Lu0)
∼= // AutC(Lu)
Proof. The inclusionUs0 ↪→U of the special ﬁbre, followed by a path
from u0 to u to change the base points, induces on fundamental groups a
pushforward homomorphism
π1(Us0,u0) // π1(U,u0)
∼= // π1(U,u).
For any Zariski-open dense subsetS′⊂ S with preimageU′ = f−1(S′) and
all s∈ S′(C) this leads to a commutative diagram
π1(Us0,u0) //

π1(U,u)

π1(U′,u)oooo

π1(Us,u)oo

G(u0)   //
 _

GU _

GU_

G(u)? _ioo
_

AutC(Lu0)
∼= // AutC(Lu) AutC(Lu) AutC(Lu)
whereGU⊆AutC(Lu) denotes the image ofπ1(U,u) under the monodromy
representation. Note thatGU coincides with the image ofπ1(U′,u) because
the embedding of any Zariski-open dense subset induces an epimorphism
on fundamental groups. The proof of the lemma would be ﬁnished if we
could show that the embeddingi in the above diagram is an isomorphism
for a suitable choice of the Zariski-open dense subsetS′⊆ S.
This need not be the case in general. However, since the statement of
the lemma only concerns the ﬁbres of the familyf : U−→S and not the
total space, we can for the purpose of the proof replace the given family
by its base change under any quasi-ﬁnite branched cover of a Zariski-open
dense subset ofS containings0, accordingly replacing the local systemL
