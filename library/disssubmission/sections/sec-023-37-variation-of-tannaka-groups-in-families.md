---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-023-37-variation-of-tannaka-groups-in-families
section_title: "Variation of Tannaka groups in families"
section_number: 3.7
pages: 69-77
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
61
are an epi- resp. an isomorphism. The ﬁnal statement then follows from the
observation that these homomorphisms come from morphisms between the
underlying schemes and that the intersection of any two Zariski-open dense
subsets of the irreducible scheme Π(X)l ∼= Π(Xη)l is non-empty.
□
3.7. Variation of Tannaka groups in families
In this section we turn the local result from theorem 3.15 into a more
global statement. Under some mild ﬁniteness assumptions we will see that
for a smooth family of varieties, the Tannaka groups of the ﬁbres deﬁne a
constructible stratiﬁcation of the base space. This will be used in chapter 4
to determine the Tannaka group for the theta divisor of a general principally
polarized complex abelian variety.
For technical reasons we will restrict ourselves to abelian rather than
semiabelian schemes. In what follows X −→S always denotes an abelian
scheme whose base scheme S is an algebraic variety over an algebraically
closed ﬁeld k of characteristic zero. Let
Y  
/
?
?
?
?
?
?
?
?
X

S
be a closed subscheme which is smooth of relative dimension d over the
base S, and for geometric points s in S consider the perverse intersection
cohomology sheaf
δYs = ΛYs[d] ∈P(Ys) = Perv(Ys,Λ)
on the ﬁbre Ys. We want to understand how the Tannaka groups G(δYs) vary
with the chosen point s. The following examples illustrate that in spite of
our smoothness assumption, this is in general a non-trivial problem which
involves the symmetry properties of the ﬁbres Ys.
EXAMPLE 3.17. (a) If S = E is an elliptic curve and X = S × E, then
for the tautological subvariety Y = {(e,e) ∈X | e ∈E} we have
G(δYs) ∼=
(
Z/nZ
if s is a torsion point in E of precise order n,
Gm
if s is a point of inﬁnite order in E.
(b) If Y →S is a smooth, projective family of curves of genus g ≥3 and is
embedded into its relative Picard scheme X = Pic0
Y/S in a suitable way, then
by [106, th. 14] we have
G(δYs) ∼=
(
Sp2g−2(Λ)
if Ys is hyperelliptic,
Sl2g−2(Λ)
otherwise.
62
Chapter 3 – Perverse sheaves on semiabelian varieties
In particular, example (a) shows that without further assumptions the
Tannaka groups do not always deﬁne a constructible stratiﬁcation of S. In
general we only have the following semicontinuity property.
LEMMA 3.18. Let η ∈S be any scheme-theoretic point, s ∈{η} a point
in its closure, and consider geometric points η and s above these. Then we
have an embedding
G(δYs) ,→G(δYη).
Proof. The statement is only concerned with the geometric ﬁbres of the
families Y −→S and X −→S, so we can replace these families by their base
change under any quasi-ﬁnite morphism S′ −→S whose image contains the
points s and η as indicated in the following diagram.
Y ′
/
xqqqqqqqqq
;;

;;;;;;;;
X′

xqqqqqqqqq
Y
/

:::::::::::::
X

S′
xrrrrrrrrrr
∃s′
1
xqqqqqqqqqq
∃η′
0
wppppppppp
S
s
η
In particular, replacing S by the reduced closed subscheme S′ = {η}red we
can assume S is irreducible with generic point η. By normalization we can
also achieve that S is a normal variety. Furthermore, passing to an open
neighborhood of the point s we can assume that
S = Spec(A)
is afﬁne. Let p◁A be the prime ideal corresponding to the point s. Without
loss of generality s̸ = η, so we can ﬁnd a non-zero element f ∈p \ {0} in
our prime ideal. Then the vanishing locus
V(f) = Spec(A/(f)) ,→S = Spec(A)
is a proper closed subscheme of codimension one and contains s. Now take
any irreducible component D ,→V(f)red of the underlying reduced closed
subscheme such that the point s lies on the Weyl divisor D, and let ηD be
a geometric generic point of this irreducible divisor. By induction on the
dimension dim(S) we have an embedding
G(δYs) ,→G(δYηD),
hence it will be enough to prove our claim when s = ηD is the generic point
of an irreducible Weyl divisor D on S.
This being said, recall from the above that we can assume S to be normal
and hence regular in codimension one. In this case the one-dimensional
3.7. Variation of Tannaka groups in families
63
local ring OS,s = Ap is a discrete valuation ring. Its residue ﬁeld k(s) can be
identiﬁed naturally with the function ﬁeld k(D) of the reduced irreducible
subvariety D ,→S via the diagram
A
/ /

A/p  
/

k(D)
Ap
5
/ / Ap/pAp
k(s)
∼=
O
where the dotted arrows exist by the universal property of the localization
functor. Hence we can replace S by the strict Henselization Spec(Ash
p ) which
still has s and η as geometric points. From theorem 3.15 we then obtain an
embedding
G(Ψ(δYη)) ,→G(δYη)
for the nearby cycles on the corresponding abelian scheme, and our claim
follows because for a smooth morphism Y →S one has Ψ(δYη) = δYs.
□
To obtain a constructibility statement for the stratiﬁcations deﬁned by
the Tannaka groups, we need to impose some ﬁniteness conditions on the
perverse sheaves on the ﬁbres. To simply the notation, let us temporarily
assume that X is an abelian variety over S = Spec(k). Let P ∈P(X) be a
perverse sheaf, and consider the equivalence
ω :
⟨P⟩
∼
−→RepΛ(G(P))
from corollary 3.10. In what follows we will be particularly interested in
the determinant character
det(ω(P)).
Like any character of the Tannaka group, this determinant corresponds by
part (b) of proposition 1.6 to a perverse skyscraper sheaf δx ∈P(X) which
is supported on a closed point x ∈X. In this context the following two
conditions are equivalent:
• the determinant det(ω(P)) is a torsion character of order n,
• the corresponding point x ∈X is a torsion point of order n.
In many applications P is isomorphic to its adjoint dual P∨= (−idX)∗D(P)
so that ω(P) is self-dual and the above conditions hold with n = 2.
LEMMA 3.19. Let d,n ∈N. Then there exists a ﬁnite set of subgroups
of Gld(Λ) with the property that for every simple perverse sheaf P ∈P(X)
of Euler characteristic χ(P) = d with
det(ω(P))⊗n = 1,
the Tannaka group G(P) is isomorphic to one of these ﬁnitely many groups.
64
Chapter 3 – Perverse sheaves on semiabelian varieties
Proof. Lemma B.1 and B.2 in the appendix show that up to conjugation
there are only ﬁnitely many possibilities for the Tannaka group G = G(P)
as a subgroup of Gld(Λ).
□
Let us now return to the case of an abelian scheme p : X −→S whose
base scheme is an arbitrary variety S over the algebraically closed ﬁeld k
of characteristic zero. For any sheaf complex P ∈D(X) and any geometric
point s of S we will denote by
Ps = i∗
s(P) ∈D(Xs)
the restriction to the geometric ﬁbre is : Xs −→X. Then the constructibility
result we are interested in can be formulated as follows.
PROPOSITION 3.20. Let n ∈N, and consider a complex P ∈D(X) such
that for each geometric point s of S, the restriction Ps is a simple perverse
sheaf with
det(ω(Ps))⊗n = 1.
Then there are reductive algebraic groups G1,...,Gm and a stratiﬁcation
into locally closed subsets
S =
m
G
i=0
Si such that G(Ps) = Gi for all geometric points s in Si.
Proof. Recall from [29, prop. 3.1(c)] that if V is a ﬁnite-dimensional
vector space over Λ, then any reductive algebraic subgroup of Gl(V) is
determined uniquely by its subspaces of invariants in the tensor powersW ⊗r
of W = V ⊕V ∨with r ∈N. Furthermore, if we only want to distinguish
between ﬁnitely many given reductive subgroups up to conjugacy, then it
sufﬁces to look at exponents r ≤r0 for some ﬁxed r0 ∈N.
Hence in view of lemma 3.19 our claim will follow if we can show that
in a suitable sense, the tensor functor ω : ⟨Ps⟩−→RepΛ(G(Ps)) in the proof
of corollary 3.10 varies in a constructible way with the geometric point s
and that the subspaces of invariants — corresponding to the direct sum of
all direct summands 1 = δ0 in the convolution powers of Ps ⊕P∨
s — also
vary in a constructible way. More precisely, we would be done if we could
show that there exist
(a) a complex P∨∈D(X) which on each geometric ﬁbre Xs restricts
to the adjoint dual
P∨
s
= (−id)∗D(Ps),
(b) a character χ ∈Π(X) such that for the twist Q = Pχ ⊕P∨
χ the direct
image complex
W = Rp∗(Q)
3.7. Variation of Tannaka groups in families
65
is a constructible sheaf on S which is concentrated in degree zero
and has geometric stalks
Ws = H0(Xs,Qs) = ω(Ps ⊕P∨
s ),
(c) for each r ≤r0 a constructible subsheaf of W ⊗r whose stalks at any
geometric point s coincide under the above identiﬁcation with the
cohomology of the direct sum of all skyscraper summands 1 = δ0
in the convolution Q∗r
s = Qs ∗···∗Qs.
In general this is too much to expect. However, since the groups Gs = G(Ps)
only depend on the geometric ﬁbres of our abelian scheme and since for
the proof of constructibility we can argue by Noetherian induction on the
dimension dim(S), it will do no harm if we replace our original abelian
scheme by the base change
X′ = X ×S S′ −→S′
under a quasi-ﬁnite ´etale morphism S′ −→S and also replace P ∈D(X)
by its pull-back P′ ∈D(X′). In particular, for the proof of the proposition
we are free to replace our base scheme S by arbitrary Zariski-open dense
subsets of S and also by ﬁnite ´etale covers of such subsets.
With this extra freedom, property (a) can be obtained from the general
fact [64, prop. 1.1.7] that for any morphism p : X →S of varieties with
smooth target variety S and any P ∈D(X), there is a Zariski-open dense
subset S′ ,→S such that the formation of the relative dual
DX/S(P) = RH om(P, p!ΛS)
commutes with every base change that factors over S′ ,→S. Property (b) will
be obtained in lemma 3.21 after a base change to a ﬁnite ´etale cover of some
Zariski-open dense subset of S, which is needed to make sure that there are
sufﬁciently many characters available. For part (c) consider the relative
convolution power Q∗r = Ra∗(Q⊠S ···⊠S Q) where a : X ×S ···×S X −→X
is the group law. We have a relative K¨unneth isomorphism
Rp∗(Q∗r)
∼=
−→(Rp∗(Q))⊗r = W ⊗r
as in the absolute case. Let Z ⊂X be the zero section of our abelian scheme,
and consider the morphism
ϕ :
Rp∗(RH om(ΛZ,Q∗r)) −→RH om(ΛS,W ⊗r) ∼= W ⊗r
which corresponds by adjunction to the composite morphism ψ given by
the following diagram (where the diagonal arrow on the left comes from
66 Chapter 3 — Perverse sheaves on semiabelian varieties

the adjoint of the relative Ktinneth isomorphism).

y

RHom(Az, O*")

RHAom(p*(As), p (W*"))

p (RH om(As, W°"))

As a candidate for the constructible subsheaf in part (c) we take the image of
the induced morphism .#°(@) on the stalk cohomology sheaves in degree
zero. After shrinking S we can by loc. cit. assume that the occuring R#om
commute with base change. If we put

K = (Ps@PY)*”

and denote by 4; the restriction of the character x to the geometric fibre X;,
then on stalks we obtain a commutative diagram

Pall .
H(X;, RAom(8y,Ky,)) ——

H®(X;,Ky;)

|

Hom(d,"H(K) z)

Diez Ext'(5p,"H"(K) z,)

where the Ext and Hom in the lower row refer to the abelian category P(X;)
and where the vertical identifications come from Gabber’s decomposition
theorem by which Ky, © @jez?H'(K)y,[—i]. The fact that #°(@); factors
over the projection in the lower row follows from the observation that by
part (b) we have H°(X;,?H"(K)y,) = 0 for all i# 0. Hence (c) follows as
well, and we are done. O

In the above proof we have used that after a suitable quasi-finite étale
base change there exist enough characters ¥ € II(X) so that we can apply

the vanishing theorem from section 3.1 fibre by fibre. More precisely we
have the following result.

LEMMA 3.21. Let P € D(X) be a complex which restricts to a perverse
sheaf on each geometric fibre of the abelian scheme X — S, and suppose
that S is irreducible. Then there exists

© a quasi-finite étale morphism f : S' > S,
e acharacter x € T1(X') for the abelian scheme X' = X x35",

such that the direct image of P' = (idx, f)*(P) € D(X") under the structure
morphism p : X' — S' satisfies

FE\(Rp.(P'@,Ly)) = 0 forall i#0.
3.7. Variation of Tannaka groups in families
67
Proof. Take a geometric generic point η of S. The set of all torsion
characters χη : π1(Xη,0) −→Λ∗is dense in the character torus Π(Xη), so
by the generic vanishing theorem from chapter 1 we can ﬁnd a character χη
of some ﬁnite order N ∈N with the property that Hi(Xη,Pη ⊗Λ Lχη) = 0 for
all i̸ = 0. If we could extend this character to a global character χ ∈Π(X),
then the above vanishing property would mean that for the direct image
under p : X →S the generic stalk cohomology satisﬁes
H i(Rp∗(P⊗Λ Lχ))η = 0
for all
i̸ = 0.
Since the cohomology sheaves are constructible, the vanishing of their stalks
at the geometric generic point η would imply their vanishing over some
open dense subset U ⊆S, and we would be done even without the need to
pass to a ﬁnite ´etale cover of the base variety S and without using that χη is
a torsion character of order N.
However, in general it may be impossible to ﬁnd χη ∈Π(Xη) with the
required property which lifts to some χ ∈Π(X) (for example, think of the
universal abelian scheme X over a ﬁnite level cover S of the moduli space of
principally polarized abelian varieties — here the abelianized fundamental
group πab
1 (X) and hence also the group Π(X) is ﬁnite). To get around this
problem we perform a base change under a ﬁnite ´etale cover depending on
the chosen torsion character χη. Consider the split exact ﬁbration sequence
0
/ π1(Xη,0)
/ π1(X,0)
/ π1(S,η)
/
x
0
from [51, exp. XIII, prop. 4.3 and ex. 4.4], where the splitting comes from
the zero section of our abelian scheme. Via the splitting, the group π1(S,η)
acts by conjugation on π1(Xη,0) and hence on the corresponding character
torus Π(Xη). Since the group of torsion points of order N in this torus
is ﬁnite, we can ﬁnd a normal subgroup of ﬁnite index in π1(S,η) which
ﬁxes every such torsion point. This normal subgroup deﬁnes a ﬁnite ´etale
cover S′ −→S for which the character χη ∈Π(Xη) can be extended to a
character χ ∈Π(X′). After a base change by this ﬁnite ´etale cover we can
then proceed as in the ﬁrst part of the proof.
□
CHAPTER 4
