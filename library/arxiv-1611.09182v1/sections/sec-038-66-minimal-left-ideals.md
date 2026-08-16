---
doc_id: arxiv-1611.09182v1
doc_title: ""
section_id: sec-038-66-minimal-left-ideals
section_title: "Minimal left ideals"
section_number: 6.6
pages: 55-57
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? C. Furey A thesis presented to the University of Waterloo in fulfillment of the thesis requirement for the degree of Doctor of Philosophy Physics — 57 sections"
---
to mimic the set of quarks and leptons of the standard model.
6.6 Minimal left ideals
We are now proposing to represent quarks and leptons using minimal left ideals within our
space of octonionic operators, C⊗← −O≃ Cl(6). That is, within the space of the αi,α†
j, and
their products. A pair of these ideals, Su and Sd, will be constructed using our procedure
from Section 4.5.2:
1. Our vector space, V, is spanned by the elements ie1,ie 2,...ie 6 over C, in keeping
with Figure 6.2. The quadratic form is given by Q(v) ={v,v}.
2. An MTIS of V is three-complex-dimensional in this case, and can be spanned
byα1 = 1
2 (−e5 +ie4), α2 = 1
2 (−e3 +ie1), and α3 = 1
2 (−e6 +ie2).
3. Our nilpotent object is then given by ω ≡ α1α2α3.
4. This leads to the primitive idempotent, ωω† =α1α2α3α†
3α†
2α†
1.
5. Our minimal left ideal is ﬁnally given by Su≡ C⊗← −O ωω†, below.
The eight-complex-dimensional minimal left ideal for the ﬁrst ladder system is given
by
47
Su≡
V ωω†
+ ¯Drα†
1ωω† + ¯Dgα†
2ωω† + ¯Dbα†
3ωω†
+U rα†
3α†
2ωω† + U gα†
1α†
3ωω† + U bα†
2α†
1ωω†
+ E +α†
3α†
2α†
1ωω†,
(6.19)
whereV, ¯Dr,... E + are 8 suggestively named complex coeﬃcients.
As
αiωω† = 0 ∀i, (6.20)
ωω† plays the role of the vacuum state, where the term vacuum is used loosely. Again,
it is not to be interpreted as a zero-particle state. However, readers may recognize the
similarity between Su and a Fock space.
The conjugate system of Section 6.5 analogously leads to
Sd≡
¯V ω†ω
Drα1ω†ω + Dgα2ω†ω + Dbα3ω†ω
+ ¯U rα3α2ω†ω + ¯U gα1α3ω†ω + ¯U bα2α1ω†ω
+ E−α3α2α1ω†ω,
(6.21)
where ¯V,Dr,... E− are eight complex coeﬃcients.
This new ideal, (6.21), is linearly independent from the ﬁrst, (6.19), in the space of
octonionic operators. Clearly, the two are related via the complex conjugate, i↦→− i.
In fact, the complex conjugate is all that is needed in order to map particles into anti-
particles, and vice versa. This was a feature in the models of [42], [35], and also in the
context of left- and right-handed Weyl spinors in [34] and Section 3.5.3 of this thesis. It
was not a feature in [8], [13], [14], [26], or [27], where an additional quaternionic algebra
was implemented in order to obtain Sd.
The Cliﬀord algebra, Cl(6), is known to have just a single 8-complex-dimensional ir-
reducible representation, as in Su, above. In this text, we will none-the-less be including
the conjugate ideal, Sd, in analogy to our inclusion of both left- and right-handed Weyl
48
spinors in Section 4.8. Just as in the case with Weyl spinors, rotations between Su andSd
are enacted via right multiplication onto these ideals. Su and Sd can then be combined
into a single irreducible representation under Cl(6)⊗C Cl(2), where the factor of Cl(2)
accounts for the right action that mixes these two spinors with each other. Unlike in the
earlier literature, this additional factor of Cl(2) will originate from right multiplication of
our original octonionic operators on these ideals, instead of having to introduce an entirely
new Cliﬀord algebra, Cl(2). This topic of doubling the spinor space will come up again in
Chapter 9.
As a ﬁnal note, we point out that another interesting way to obtain anti-particles could
be to use the conjugate †, instead of ∗. In that case, the two minimal left ideals would
not be entirely linearly independent from each other. That is, we would ﬁnd a special
Majorana-like property unique to the neutrino:
(
ωω†)†
=ωω†.
