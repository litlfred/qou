---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-090-59-a-smooth-global-family-131
section_title: "A smooth global family 131"
section_number: 5.9
pages: 139-141
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
by its pull-back under this base change. In particular, since´etale-locally
any smooth morphism admits a section, we can assume that there exists a
sectionσ : S−→U of our familyf : U−→S. Since by assumptionL has
ﬁnite monodromy, we can after passing to a further branched cover assume
that the local systemσ∗(L) is trivial. Now recall from [102, cor. 5.1] that
for any (not necessarily proper) morphismf :U−→S of complex algebraic
varieties, there exists a Zariski-open dense subsetS′⊆ S over which the
restrictionU′−→S′ is a topologically locally trivial ﬁbration in the analytic
topology. We then in particular have the exact ﬁbration sequence
··· // π1(Us,u) // π1(U′,u) // π1(S,s) //
σ∗
xx
···
for s∈ S′(C) and u = σ(s). Hence the triviality ofσ∗(L) implies that the
monodromy group
G(u) = Im(π1(Us,u)−→AutC(Lu))
is mapped isomorphically onto the group
GU′ = Im(π1(U′,u)−→AutC(Lu))
via the homomorphismi in the diagram from the beginning of the proof,
and hence the lemma follows. □
5.9. A smooth global family
To complete the proof of theorem 5.1 it remains to construct an abelian
schemeXS−→S with the properties discussed in section 5.2, which will
allow to relate the monodromy group of the local systemV+ for a general
ppav of dimensiong = 4 to the corresponding monodromy group for the
Jacobian variety of a smooth non-hyperelliptic curve. To this end we ﬁx an
integern≥3 and work as in section 4.1 over the moduli spaceA4,n of ppav’s
of dimension 4 with a full leveln structure, which by [80, chapt. 7.3] is
represented by a smooth quasi-projective variety. For subvarietiesS ↪→A4,n
we denote by
ΘS   //
""DDDDDDDDD
XS

S
the corresponding abelian scheme with its relatively ample divisor which
on the universal covering is deﬁned by the Riemann theta function. We are
132 Chapter 5 – A family of surfaces
interested in the composite morphism
f : YS = ΘS×S ΘS   // XS×S XS
a // XS
wherea denotes the group law of the abelian scheme. For eachs∈ S(C)
the restriction f|Xs : f−1(Xs)−→Xs is the family of the intersections of
translates of the theta divisor for the corresponding ppavXs as in the proof
of the Bertini-type lemma 5.3.
LEMMA 5.28. There exists a smooth quasi-projective curve S⊂ A4,n
with the following properties.
(a) For some s0∈S(C) the ﬁbre Xs0 is the Jacobian variety of a general
curve, whereas for all other points s⁄= s0 the theta divisorΘs⊂ Xs
is smooth.
(b) The family f : YS−→S of intersecting theta divisors restricts to a
smooth proper morphism
f|US : f−1(US)−→US
over some Zariski-open subset US⊂ XS which surjects onto S.
Proof. The locus of all ppav’s with a singular theta divisor is itself
a divisor in the moduli spaceA4,n, and it contains the locus of Jacobian
varieties as a component [4]. Hence if we take S ↪→ A4,n to be a smooth
quasi-projective complex curve which meets the locus of Jacobian varieties
in a general points0∈ S(C) and is otherwise contained in the Zariski-open
dense locus of ppav’s with a smooth theta divisor, then(a) holds.
Consider then the corresponding morphismf :YS−→XS. By the generic
ﬂatness theorem in the form of lemma 5.29 below, we ﬁnd a Zariski-open
dense subsetUS⊂ XS which maps surjectively ontoS and furthermore has
the property that the restriction
f|US : f−1(US)−→US
is a ﬂat morphism. Now recall from lemma 4.5 that the theta divisor of the
non-hyperelliptic Jacobian varietyXs0 has only isolated singularities, so by
the Bertini-type lemma 5.3 we can ﬁnd a pointu in Us0 = US∩Xs0 such
that the ﬁbreYu = f−1(u) is smooth. Furthermore, for any proper and ﬂat
morphism of varieties over a ﬁeld which has at least one smooth ﬁbre, there
exists by [55, ex. III.10.2] a non-empty Zariski-open subset of the target
over which the morphism is smooth. In our case thereforef restricts to
a smooth morphism over some Zariski-open neighborhood of the pointu
in US. We can replaceUS by such a neighborhood and accordingly shrink
the curveS in such a way that the special points0 still lies inS(C) but that
now also the properties in claim(b) are satisﬁed. □
