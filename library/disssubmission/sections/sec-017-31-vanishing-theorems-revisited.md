---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-017-31-vanishing-theorems-revisited
section_title: "Vanishing theorems revisited"
section_number: 3.1
pages: 50-54
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
To formulate the generic vanishing axiom that generalizes theorem 1.1
to the non-proper case over a ﬁeld k of arbitrary characteristic, we consider
characters of the tame fundamental group. As a base point we will always
take the neutral element 0 ∈X(k). Recall from [97, sect. 1.3] that every
semiabelian variety X has a smooth compactiﬁcation with a normal crossing
boundary divisor. The tame fundamental group π t
1(X,0) classiﬁes the ﬁnite
´etale covers of X that are tamely ramiﬁed along each component of such
a boundary divisor, see [51, exp. XIII, sect. 2 and 5], [52] and [93]. In
particular π t
1(X,0) is a quotient of the ´etale fundamental group π1(X,0),
and equal to it if the ﬁeld k has characteristic zero or if X is proper.
3.1. Vanishing theorems revisited
43
The group Π(X) of continuous characters χ : π t
1(X,0) −→Λ∗admits a
natural product decomposition
Π(X) = Π(X)l′ ×Π(X)l,
where
Π(X)l′ = { χ ∈Π(X) : χn = 1 for some n with l ∤n }
denotes the subgroup of all characters of ﬁnite order prime to l and where by
deﬁnition Π(X)l is the group of all characters that factor over the maximal
pro-l-quotient π1(X,0)l = π t
1(X,0)l. The latter is a free Zl-module of ﬁnite
rank [17]. So with the same arguments as in [41, sect. 3.2] the set Π(X)l
of pro-l-characters can be identiﬁed with the set of Λ-valued points of a
scheme in a natural way (even though as in loc. cit. the multiplication of
characters does not come from a group scheme structure). This being said,
we consider the set of all tame characters
Π(X)
=
a
χ∈Π(X)l′
χ ·Π(X)l
as the disjoint union of the inﬁnitely many components χ · Π(X)l indexed
by the torsion characters χ ∈Π(X)l′, and we say that a statement holds for
a generic character if it holds for all characters in an open subset of Π(X)
that is dense in each of these components.
For sheaf complexes K ∈D(X) and characters χ ∈Π(X) we consider as
in the previous chapters the twist Kχ = K ⊗ΛLχ by the local system Lχ. Our
Tannakian constructions will be based on the following generic vanishing
assumption for such character twists.
ASSUMPTION GV(X). Let P ∈P(X). Then for generic χ ∈Π(X) the
forget support map
H•
c (X,Pχ) −→H•(X,Pχ)
is an isomorphism, and
Hi(X,Pχ) = Hi
c(X,Pχ) = 0
for all
i̸ = 0.
For complex abelian varieties this is precisely the content of the generic
vanishing theorem 1.1, the claim about the forget support map being trivial
in that case. At present we do not know whether the assumption GV(X) also
holds for abelian varieties over an algebraically closed ﬁeld k of positive
characteristic p = char(k) > 0, but in any case the semiabelian version can
be deduced from the abelian one as follows.
THEOREM 3.1. If the maximal abelian variety quotient A = X/T of X
satisﬁes the assumption GV(A), then also GV(X) holds.
44
Chapter 3 – Perverse sheaves on semiabelian varieties
Proof. We ﬁrst claim that for any given perverse sheaf P ∈P(X), the set
of all characters χ which violate the conditions in our assumption GV(X)
forms a closed subset of the scheme Π(X). To see this, consider the Mellin
transforms M!(P) and M∗(P) as deﬁned in [41, sect. 3.3] (in loc. cit. the
deﬁnition is only given for algebraic tori, but it carries over verbatim to the
case at hand). These Mellin transforms are objects of the bounded derived
category of coherent sheaves on Π(X) with the property that for all i ∈Z
and any character χ ∈Π(X) we have isomorphisms
Hi
c(X,Pχ) ∼= H i(Li∗
χM!(P)),
Hi(X,Pχ) ∼= H i(Li∗
χM∗(P)),
where iχ : {χ} ,→Π(X) denotes the embedding of the closed point given by
the chosen character. Furthermore, we have a morphism M!(P) −→M∗(P)
which induces via the above identiﬁcations the forget support morphism on
cohomology. Since on a Noetherian scheme the support of any coherent
sheaf is a closed subset, it follows that the locus of all characters χ which
violate GV(X) forms a closed subset S (P) ⊆Π(X) as claimed.
We must show that under the assumption GV(A) the complement of this
closed subset S (P) meets every irreducible component of Π(X). So we
must see that for at least one character χ in each component the properties
in GV(X) hold. To this end consider the exact sequence
0 −→T
i
−→X
f
−→A −→0
which deﬁnes the given semiabelian variety. Lemma 3.2 below will show
that every component of Π(X) contains a character χ such that the forget
support morphism
Rf!(Pχ) −→Rf∗(Pχ)
is an isomorphism. In this case Artin’s vanishing theorem for the afﬁne
morphism f also shows that these two isomorphic direct image complexes
are perverse [41, lemma 2.4]. For all ϕ ∈Π(A) and ψ = f ∗(ϕ) ∈Π(X) the
projection formula furthermore says
(Rf!(Pχ))ϕ = Rf!(Pχψ)
and
(R f∗(Pχ))ϕ = Rf∗(Pχψ),
hence we are ﬁnished by an application of the vanishing assumption GV(A)
to these perverse direct images.
□
To ﬁll in the missing statement in the above proof, we consider the given
semiabelian variety as a torsor f : X −→A under the torus T in the sense
of [74, sect. III.4]. The condition of being a torsor is satisﬁed since clearly
the morphism X ×k T −→X ×A X, (x,t) 7→(x,xt) is an isomorphism. The
result we are looking for only uses the structure as a torsor, and for its proof
it will be convenient to forget that our base A is an abelian variety. So we
will work in the following setting.
3.1. Vanishing theorems revisited
45
Let B be an arbitrary variety over the ﬁeld k, and let f : Y −→B be a
torsor under the torus T. By remark 4.8 (a) in loc. cit. there exists an ´etale
covering B′ −→B (not necessarily ﬁnite) over which our torsor admits a
trivialization.
Y ×B B′
∼=
/
#G
G
G
G
G
G
G
G
G
T ×k B′
{xxxxxxxxx
B′
Let us denote by i :Yb = f −1(b) −→Y the ﬁbre over some chosen geometric
point b ∈B(k). In what follows we ﬁx a base point y ∈Yb(k) and denote the
group of all continuous characters of the tame fundamental group πt
1(Yb,y)
as above by Π(Yb), and similarly for Π(Y). Since Yb is isomorphic to the
torus T, the character group Π(Yb) can be identiﬁed with the set of closed
points of a scheme as explained above. In particular, it makes sense to speak
about its irreducible components.
LEMMA 3.2. In the above setting, for every perverse sheaf P ∈P(Y)
there exists a subset U ⊆Π(Yb) which meets every irreducible component
and has the property that the forget support morphism
Rf!(Pχ) −→R f∗(Pχ)
is an isomorphism for all characters χ ∈Π(Y) with pull-back i∗(χ) ∈U.
Proof. Let g : B′ −→B be an ´etale covering which trivializes the given
torsor in the sense that the pull-back Y ′ = Y ×B B′ is isomorphic over B′
to the trivial torsor T ×k B′. Choosing a geometric point b′ ∈B′(k) with
image g(b′) = b, we have a commutative diagram
Yb
i′
/

i
%
Y ′
f ′

g′
/ Y
f

Spec(k)
b′
/
b
9
B′
g
/ B
where the two squares are Cartesian. Since g is an ´etale covering, the forget
support morphism Rf!(Pχ) −→Rf∗(Pχ) is an isomorphism iff its pull-back
under g∗is an isomorphism. For the pull-back P′ = g′∗(P) and χ′ = g′∗(χ)
46
Chapter 3 – Perverse sheaves on semiabelian varieties
we have a commutative diagram
g∗(Rf!(Pχ))
/
∼=

g∗(Rf∗(Pχ))
∼=

Rf ′
!(P′
χ′)
/ R f ′
∗(P′
χ′)
where the vertical arrows are isomorphisms due to the smooth base change
theorem [38, th. I.7.3]. Furthermore, by construction i′∗(χ′) = i∗(χ). Hence
it will be enough to prove the lemma in the case of the trivial torsor, and this
has been done in [41, cor. 2.3.2].
□
Let us now return to our semiabelian variety X. For later reference it will
be convenient to reformulate the observation in theorem 3.1 in the following
equivalent way.
COROLLARY 3.3. Suppose that A = X/T satisﬁes axiom GV(A), and
let K ∈D(X) be a constructible sheaf complex. For all degrees r ∈Z and a
generic character χ ∈Π(X) then
Hr
c(X,Kχ) ∼= Hr(X,Kχ) ∼= H0(X, pHr(K)χ),
where the ﬁrst isomorphism is induced by the forget support morphism.
Proof. For the perverse cohomology groups Pr = pHr(K) and χ ∈Π(X)
we have (Pr)χ = pHr(Kχ) since twisting by χ is a t-exact functor for the
perverse t-structure. Only ﬁnitely many Pr are non-zero, so for generic χ
and all r theorem 3.1 says that the hypercohomology groups Hs
c(X,(Pr)χ)
and Hs(X,(Pr)χ) will be isomorphic to each other via the forget support
morphism, and vanish for all s̸ = 0. Then the spectral sequences
Ers
2 = Hs(X,(Pr)χ) =⇒Hr+s(X,Kχ)
Ers
2 = Hs
c(X,(Pr)χ) =⇒Hr+s
c
(X,Kχ)
degenerate, and our claim follows since the forget support map between the
limit terms is induced from the one between the E2-terms.
□
