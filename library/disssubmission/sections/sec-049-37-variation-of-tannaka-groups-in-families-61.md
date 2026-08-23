---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-049-37-variation-of-tannaka-groups-in-families-61
section_title: "Variation of Tannaka groups in families 61"
section_number: 3.7
pages: 69-71
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
are an epi- resp. an isomorphism. The ﬁnal statement then follows from the
observation that these homomorphisms come from morphisms between the
underlying schemes and that the intersection of any two Zariski-open dense
subsets of the irreducible schemeΠ(X)l∼= Π(Xη)l is non-empty. □
3.7. Variation of Tannaka groups in families
In this section we turn the local result from theorem 3.15 into a more
global statement. Under some mild ﬁniteness assumptions we will see that
for a smooth family of varieties, the Tannaka groups of the ﬁbres deﬁne a
constructible stratiﬁcation of the base space. This will be used in chapter 4
to determine the Tannaka group for the theta divisor of a general principally
polarized complex abelian variety.
For technical reasons we will restrict ourselves to abelian rather than
semiabelian schemes. In what followsX−→S always denotes an abelian
scheme whose base schemeS is an algebraic variety over an algebraically
closed ﬁeldk of characteristic zero. Let
Y   //
???????? X

S
be a closed subscheme which is smooth of relative dimensiond over the
base S, and for geometric pointss in S consider the perverse intersection
cohomology sheaf
δYs = ΛYs[d]∈ P(Ys) = Perv(Ys,Λ)
on the ﬁbreYs. We want to understand how the Tannaka groupsG(δYs) vary
with the chosen points. The following examples illustrate that in spite of
our smoothness assumption, this is in general a non-trivial problem which
involves the symmetry properties of the ﬁbresYs.
EXAMPLE 3.17. (a) If S = E is an elliptic curve and X= S×E, then
for the tautological subvariety Y={(e,e)∈ X| e∈ E} we have
G(δYs)∼=
{
Z/nZ if s is a torsion point in E of precise order n,
Gm if s is a point of inﬁnite order in E.
(b) If Y→ S is a smooth, projective family of curves of genus g≥ 3 and is
embedded into its relative Picard scheme X=Pic0
Y/S in a suitable way, then
by [106, th. 14]we have
G(δYs)∼=
{
Sp2g−2(Λ) if Ys is hyperelliptic,
Sl2g−2(Λ) otherwise.
62 Chapter 3 – Perverse sheaves on semiabelian varieties
In particular, example(a) shows that without further assumptions the
Tannaka groups do not always deﬁne a constructible stratiﬁcation ofS. In
general we only have the following semicontinuity property.
LEMMA 3.18. Let η∈ S be any scheme-theoretic point, s∈{η} a point
in its closure, and consider geometric pointsη ands above these. Then we
have an embedding
G(δYs) ↪→ G(δYη).
Proof.The statement is only concerned with the geometric ﬁbres of the
familiesY−→S andX−→S, so we can replace these families by their base
change under any quasi-ﬁnite morphismS′−→S whose image contains the
pointss and η as indicated in the following diagram.
Y′ //
xxqqqqqqqqq ;;

;;;;;;;;
X′

xxqqqqqqqqq
Y //

::::::::::::: X

S′
xxrrrrrrrrrr ∃s′1
xxqqqqqqqqqq ∃η′0
wwppppppppp
S s η
In particular, replacingS by the reduced closed subschemeS′ ={η}red we
can assumeS is irreducible with generic pointη. By normalization we can
also achieve thatS is a normal variety. Furthermore, passing to an open
neighborhood of the points we can assume that
S = Spec(A)
is afﬁne. Letp◁A be the prime ideal corresponding to the points. Without
loss of generalitys⁄= η, so we can ﬁnd a non-zero elementf∈ p\{0} in
our prime ideal. Then the vanishing locus
V(f ) = Spec(A/(f )) ↪→ S = Spec(A)
is a proper closed subscheme of codimension one and containss. Now take
any irreducible componentD ↪→V(f )red of the underlying reduced closed
subscheme such that the points lies on the Weyl divisorD, and let ηD be
a geometric generic point of this irreducible divisor. By induction on the
dimension dim(S) we have an embedding
G(δYs) ↪→ G(δYηD),
hence it will be enough to prove our claim whens = ηD is the generic point
of an irreducible Weyl divisorD on S.
This being said, recall from the above that we can assumeS to be normal
and hence regular in codimension one. In this case the one-dimensional
