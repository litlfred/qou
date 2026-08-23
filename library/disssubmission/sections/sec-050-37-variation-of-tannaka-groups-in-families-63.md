---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-050-37-variation-of-tannaka-groups-in-families-63
section_title: "Variation of Tannaka groups in families 63"
section_number: 3.7
pages: 71-73
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
local ringOS,s = Ap is a discrete valuation ring. Its residue ﬁeldk(s) can be
identiﬁed naturally with the function ﬁeldk(D) of the reduced irreducible
subvarietyD ↪→S via the diagram
A // //

A/p   //

k(D)
Ap
55
// // Ap/pAp k(s)
∼=
OO
where the dotted arrows exist by the universal property of the localization
functor. Hence we can replaceS by the strict HenselizationSpec(Ashp ) which
still hass and η as geometric points. From theorem 3.15 we then obtain an
embedding
G(Ψ(δYη)) ↪→ G(δYη)
for the nearby cycles on the corresponding abelian scheme, and our claim
follows because for a smooth morphismY→S one hasΨ(δYη) = δYs. □
To obtain a constructibility statement for the stratiﬁcations deﬁned by
the Tannaka groups, we need to impose some ﬁniteness conditions on the
perverse sheaves on the ﬁbres. To simply the notation, let us temporarily
assume thatX is an abelian variety overS = Spec(k). Let P∈ P(X) be a
perverse sheaf, and consider the equivalence
ω : ⟨P⟩ ∼−→RepΛ(G(P))
from corollary 3.10. In what follows we will be particularly interested in
the determinant character
det(ω(P)).
Like any character of the Tannaka group, this determinant corresponds by
part (b) of proposition 1.6 to a perverse skyscraper sheafδx∈ P(X) which
is supported on a closed pointx∈ X. In this context the following two
conditions are equivalent:
• the determinant det(ω(P)) is a torsion character of ordern,
• the corresponding pointx∈ X is a torsion point of ordern.
In many applicationsP is isomorphic to its adjoint dualP∨ = (−idX)∗D(P)
so thatω(P) is self-dual and the above conditions hold withn = 2.
LEMMA 3.19. Let d,n∈ N. Then there exists a ﬁnite set of subgroups
of Gld(Λ) with the property that for every simple perverse sheaf P∈ P(X)
of Euler characteristicχ(P) =d with
det(ω(P))⊗n = 1,
the Tannaka group G(P) is isomorphic to one of these ﬁnitely many groups.
64 Chapter 3 – Perverse sheaves on semiabelian varieties
Proof.Lemma B.1 and B.2 in the appendix show that up to conjugation
there are only ﬁnitely many possibilities for the Tannaka groupG = G(P)
as a subgroup ofGld(Λ). □
Let us now return to the case of an abelian schemep : X−→S whose
base scheme is an arbitrary varietyS over the algebraically closed ﬁeldk
of characteristic zero. For any sheaf complexP∈ D(X) and any geometric
points of S we will denote by
Ps = i∗
s(P)∈ D(Xs)
the restriction to the geometric ﬁbreis : Xs−→X. Then the constructibility
result we are interested in can be formulated as follows.
PROPOSITION 3.20. Let n∈ N, and consider a complex P∈ D(X) such
that for each geometric points of S, the restriction Ps is a simple perverse
sheaf with
det(ω(Ps))⊗n = 1.
Then there are reductive algebraic groups G1, . . . ,Gm and a stratiﬁcation
into locally closed subsets
S =
m⨆
i=0
Si such that G(Ps) =Gi for all geometric pointss in Si.
Proof. Recall from [29, prop. 3.1(c)] that ifV is a ﬁnite-dimensional
vector space overΛ, then any reductive algebraic subgroup ofGl(V) is
determined uniquely by its subspaces of invariants in the tensor powersW⊗r
of W = V⊕V∨ with r∈ N. Furthermore, if we only want to distinguish
between ﬁnitely many given reductive subgroups up to conjugacy, then it
sufﬁces to look at exponentsr≤ r0 for some ﬁxedr0∈ N.
Hence in view of lemma 3.19 our claim will follow if we can show that
in a suitable sense, the tensor functorω :⟨Ps⟩−→RepΛ(G(Ps)) in the proof
of corollary 3.10 varies in a constructible way with the geometric points
and that the subspaces of invariants — corresponding to the direct sum of
all direct summands1 = δ0 in the convolution powers ofPs⊕P∨s — also
vary in a constructible way. More precisely, we would be done if we could
show that there exist
(a) a complexP∨∈ D(X) which on each geometric ﬁbreXs restricts
to the adjoint dual
P∨
s = (−id)∗D(Ps),
(b) a characterχ∈ Π(X) such that for the twistQ =Pχ⊕P∨χ the direct
image complex
W = Rp∗(Q)
