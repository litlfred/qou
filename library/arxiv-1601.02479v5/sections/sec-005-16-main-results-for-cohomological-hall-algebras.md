---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-005-16-main-results-for-cohomological-hall-algebras
section_title: "Main results for cohomological Hall algebras"
section_number: 1.6
pages: 9-12
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
condition ζ is generic. The object H( Aζ ,S
W,µ ) is a unital algebra in the category of
Λζ
µ -graded monodromic mixed Hodge structures, which corresponds to a monoid
in the category D(MMHM(Λζ
µ )). The monoidal product in this category is deﬁned
by
F ⊠+ G := + ∗(F ⊠ G),
where F ⊠ G is the usual external tensor product, and + : NQ0 × NQ0 → NQ0 is the
addition map. A unital graded algebra structure is determined by a m ap
F ⊠+ F → F
satisfying the obvious associativity condition, along with a unit map Q{0} → F
from the constant sheaf supported at the monoidal unit 0 ∈ NQ0 . Although we
prove theorems regarding this monoid, we do so via theorems regar ding the monoid
(13) H(Aζ
W,µ ) ∈ D ≥,lf (MMHM(Mζ -ss
µ ))
in the category of monodromic mixed Hodge modules on the coarse mo duli space
ofζ-semistable CQ-modules of slope µ . After restricting to Mζ -ss,S
W and applying
the monoidal functor obtained by taking the direct image along the m ap
dim : Mζ -ss
µ → NQ0 ,
the monodromic mixed Hodge module (13) becomes isomorphic to the p erverse
associated graded version of the monoid (1). In symbols, there is a n isomorphism
of algebras
(14) H
(
dim∗
(
H
(
(Mζ -ss,S
µ֒Mζ -ss
µ )!Aζ
W,µ
)))
∼
= GrP
(
H(Aζ ,S
W,µ )
)
.
All of our main results regarding H( Aζ ,S
W,µ ) and H(Aζ
W,µ ) stem from the observa-
tion that all product and coproduct structures that we consider on H( Aζ ,S
W,µ ) and
H(Aζ ,S
W,µ ) respect the perverse ﬁltration, giving rise to the algebra struct ures on
the right hand side of (14) that are much easier to describe — precis ely, we prove
that (in an appropriate sense) the algebras appearing in (14) are s upercommutative
degenerations of the CoHA H( Aζ ,S
W,µ ).
10 BEN DA VISON AND SVEN MEINHARDT
To deﬁne this “appropriate sense”, we must take some care over t he signs in the
symmetrizing morphism
sw : F ⊠+ F → F ⊠+ F .
It was noted already in [30] that the cohomological Hall algebra on th e graded
vector space (2), while not commutative, becomes commutative af ter twisting by a
simple system of signs. There are two related ways of expressing th is idea, which
we develop in tandem in this paper.
Firstly, the algebra is commutative, after replacing the usual symmetrizing mor-
phism for the category in which we consider it (involving the Koszul sig n rule) by
a new one, which depends on NQ0 -degree. We consider an adapted symmetrizing
morphismτ sw for the categories of monodromic mixed Hodge modules on Λζ
µ and
Mζ -ss
µ , with respect to which Theorems C and D are stated — see Section 6.1 for
the provenance of these signs. At the level of elements, the rule is easy to state.
Consider the form τ induced by
(15) τ : d′ ⊗ d′′ ↦→χ(d′, d′′) +χ(d′, d′)χ(d′′, d′′)
on the Z/2Z-vector space V = (Z/2Z)Q0 . Then
τ sw(a ⊗ b) = ( −1)τ (d′,d′′)+|a|·|b|b ⊗ a
where d′ and d′′ are the NQ0 -degrees of a and b respectively, and |a| and |b| are
their cohomological degrees. In other words, we modify the usual Koszul sign rule
by ( −1)τ (d′,d′′).
Now we describe the second approach to signs. As in [30, Sec.2.6] and [16] it is
sometimes more convenient to modify the deﬁnition of the product in the CoHA
H(Aζ ,S
W,µ ), so that the algebra (or in the context of this paper, its pervers e associated
graded algebra) becomes supercommutative with respect to the u sual Koszul sign
rule. The form τ vanishes on pairs d ⊗ d, and so there exists a bilinear form ψ on
V such that
(16) ψ (d′, d′′) +ψ (d′′, d′) =τ(d′, d′′).
We deﬁne the underlying graded monodromic mixed Hodge structure of H(ψAζ ,S
W,µ )
to be the same as that of H( Aζ ,S
W,µ ). We deﬁne the multiplication on H( ψAζ ,S
W,µ ) via
(17) a ⊗ b ↦→(−1)ψ (d′,d′′) H(∗ζ ,S
W,µ )(a ⊗ b)
where a ∈ H(ψAζ ,S
W,d′ ) and b ∈ H(ψAζ ,S
W,d′′ ). Associativity of the twisted CoHA follows
from associativity for the untwisted CoHA and bilinearity of ψ .
Our ﬁrst main result concerning CoHAs is an upgrade of Theorem A. I t states
that the isomorphisms of Theorem A can be realised explicitly as PBW-t ype isomor-
phisms deﬁned using the structure of the relative, or absolute CoH A, respectively.
Theorem C. Let ζ be a µ -generic Bridgeland stability condition. The localised
bialgebra structure on H(Aζ ,S
W,µ ) induces a (non-localised) Hopf algebra structure on
GrP(H(Aζ ,S
W,µ )), which is a free commutative algebra with respect to the symm etriz-
ing morphismτsw. There is a canonical PBW isomorphism in D≥,lf (MMHM(Mζ -ss
µ )):
(18) τ Sym⊠⊕
(
H(BC*)vir ⊗ BPSζ
W,µ
)
→ H(Aζ
W,µ )
that is realized via a canonical embedding 4 H(BC*)vir ⊗ BPSζ
W,µ ⊂ H (Aζ
W,µ ) and
the relative cohomological Hall algebra multiplication. T here is a similar canonical
4Strictly speaking, these maps are embeddings in the categor y of Z-graded monodromic mixed
Hodge-modules, considered as maps in the derived category o f monodromic mixed Hodge modules
via the natural embedding of categories.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 11
PBW isomorphism over the base Λζ
µ :
(19) τ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
→ H(Aζ ,S
W,µ ).
and the map is deﬁned via the cohomological Hall algebra prod uct on H(Aζ ,S
W,µ ). If
ψ is a bilinear form as in (16), then GrP(H(ψAζ ,S
W,µ )) is a free supercommutative
algebra, and there are canonically deﬁned PBW isomorphisms
Sym⊠⊕
(
H(BC*)vir ⊗ BPSζ
W,µ
)
→ H(ψAζ
W,µ )(20)
Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
→ H(ψAζ ,S
W,µ )(21)
to the relative and absolute CoHAs with the ψ -twisted multiplication.
Note that we do not claim that in the “absolute” cases (18) and (20) the canonical
isomorphisms of Theorem C are isomorphisms of algebras — in many inte resting
cases they will not be, hence the moniker “PBW theorem”. We expec t that the
case of symmetric quivers with zero potential, for which it is proved b y Eﬁmov
in [16] that the ψ -twisted cohomological Hall algebra is free supercommutative, is
atypical.
Our ﬁnal theorem is a more general PBW type statement for the wh ole CoHA.
Just as Theorem C states that the integrality isomorphisms of Theo rem A can be
realised in terms of PBW-type isomorphisms in the relative CoHA, Theo rem D
states that the same is true of the combination of the integrality iso morphisms (for
every slope) and the wall crossing isomorphism, for a generic stabilit y condition.
Theorem D. Letζ be a generic stability condition for Q. Then there are embed-
dings5 (Mζ -ss
µ → M )∗BPSζ
W,µ ⊂ H (AW,µ ) and H(Mζ -ss,S
µ , BPSζ
W,µ ) ⊂ H(AS
W )
such that the resulting morphisms
⊠
tw
⊕,∞
µ
− →−∞
τ Sym⊠⊕
(
H(BC*)vir ⊗ (Mζ -ss
µ → M)∗BPSζ
W,µ
)
→ H(AW )
⊠
tw
+,∞
µ
− →−∞
τ Sym⊠+
(
H(BC*)vir ⊗ H(Mζ -ss,S
µ , BPSζ
W,µ )
)
→ H(AS
W )
induced by the relative and absolute cohomological Hall alg ebra multiplications, re-
spectively, are isomorphisms. Similarly, if ψ is a twist deﬁned as in (16), then the
morphisms
⊠
tw
⊕,∞
µ
− →−∞ Sym⊠⊕
(
H(BC*)vir ⊗ (Mζ -ss
µ → M)∗BPSζ
W,µ
)
→ H(AW )
⊠
tw
+,∞
µ
− →−∞ Sym⊠+
(
H(BC*)vir ⊗ H(Mζ -ss,S
µ , BPSζ
W,µ )
)
→ H(AS
W )
induced by the same embeddings as above and the ψ -twisted relative and absolute
cohomological Hall algebra multiplications are isomorphi sms.
Theorem C and D together give a very general structural result o n the relative
and absolute CoHAs, namely that they are obtained by inﬁnite exten sions of alge-
bras (indexed by descending slope) that are themselves noncommu tative deforma-
tions of free supercommutative algebras, with characteristic fun ctions determined
by the cohomological BPS invariants.
5See previous footnote.
12 BEN DA VISON AND SVEN MEINHARDT
