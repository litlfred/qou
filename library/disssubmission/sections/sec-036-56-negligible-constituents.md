---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-036-56-negligible-constituents
section_title: "Negligible constituents"
section_number: 5.6
pages: 127-131
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
119
any such curve has genus g ˜C = 2g+1 = 9. Hence the adjunction formula for
the genus of a smooth curve on a smooth projective surface [55, prop. V.1.5]
gives the intersection number
degY(λ 2) = 2g ˜C −2−degY(KY| ˜C) = 16−16 = 0,
indeed for the canonical class KY we have
deg ˜C(KY| ˜C) = degY(λ ∪KY) = degX(2·[Θ]4/3) = 16
by the formula i!(λ) = [Θ]3/3 from above and by lemma 5.5. We then also
obtain the intersection number degY(β 2) = degY(λ 2)−degY(α2) = −8/3,
and to see that the vector e is a minimal vector all that remains to be done
is to divide the bilinear form by two.
□
It seems a tempting idea to prove theorem 5.1 by looking directly at the
monodromy operation on the fundamental classes of the Prym-embedded
curves from above, but we have not seen how to do this. In what follows we
give a different proof which does not use the Prym construction, and from
this point of view the theorem can be seen as an independent result about
the monodromy operation on the 27 Prym-embedded curves.
5.6. Negligible constituents
We now justify our earlier statement that for a general ppav the local
systems underlying the variations of Hodge structures V+ and V−from
lemma 5.10 are irreducible. In fact we will obtain stronger results since we
will work with perverse sheaves on the whole ppav rather than with local
systems on a Zariski-open dense subset. This shift in perspective reveals a
close connection with the Tannakian formalism of convolution as developed
in chapters 2 and 3, which is of interest in its own right.
Recall that for any complex abelian variety X, the convolution product
on the derived category Db
c (X,C) of bounded complexes of C-sheaves with
constructible cohomology sheaves in the sense of [10] is deﬁned by
K ∗L = Ra∗(K ⊠L) ∈Db
c (X,C)
for
K,L ∈Db
c (X,C),
where a : X × X −→X denotes the group law. One of the main results of
chapter 2 was that the full abelian subcategory Perv(X,C) ⊂Db
c (X,C) of
perverse sheaves is almost stable under the convolution product: Let us say
that a perverse sheaf is negligible if all its perverse subquotients have Euler
characteristic zero; then theorem 2.13 shows that for all P,Q ∈Perv(X,C)
and all n̸ = 0 the perverse cohomology sheaves
pHn(X,P∗Q) ∈Perv(X,C)
are negligible. At the other end of the scale, we will say that a perverse
sheaf is clean if it does not have any negligible subquotients.
120
Chapter 5 – A family of surfaces
Suppose now that X has dimension g ≥2 and is principally polarized
with a symmetric theta divisor Θ ⊂X, and consider the perverse intersection
cohomology sheaf
δΘ = ICΘ[g−1] ∈Perv(X,C).
This is a semisimple perverse sheaf and arises via intermediate extension
from the constant sheaf on the smooth locus of the theta divisor. Thus we
have δΘ = CΘ[g−1] if the theta divisor is smooth, but later on we will also
deal with isolated singularities.
LEMMA 5.20. If the theta divisor Θ has at most isolated singularities,
then for every clean perverse sheaf P and all n ∈Z, any simple negligible
subquotient of pHn(δΘ ∗P) is isomorphic to δX = CX[g].
Proof. By Verdier duality it sufﬁces to show this for n ≤0. Since the
theta divisor is a local complete intersection, by [65, lemma III.6.5] the
shifted constant sheaf λΘ = CΘ[g −1] is perverse, so we have an exact
sequence of perverse sheaves
0 −→κ −→λΘ −→δΘ −→0
where κ is a skyscraper sheaf supported on the ﬁnite set of singular points
of the theta divisor. Convolution with the clean perverse sheaf P yields a
distinguished triangle
κ ∗P
/ λΘ ∗P
/ δΘ ∗P
[+1] / ···
where κ ∗P is again a clean perverse sheaf. By the corresponding long
exact sequence of perverse cohomology groups, it will therefore sufﬁce to
show that every simple negligible subquotient of pHn(λΘ∗P) for n ≤0 must
be isomorphic to δX. But this follows as in [110, ex. 3] from the excision
sequence for the ample divisor Θ ⊂X with afﬁne complement X \Θ, using
Artin’s vanishing theorem.
□
Let us now consider the convolution square δΘ ∗δΘ. Due to Gabber’s
decomposition theorem this is a direct sum of degree shifts of semisimple
perverse sheaves. So we can write
δΘ ∗δΘ = S2(δΘ)⊕Λ2(δΘ)
where the symmetric square and the alternating square on the right hand side
are by deﬁnition the maximal direct summands on which the commutativity
constraint
S = SδΘ,δΘ :
δΘ ∗δΘ −→δΘ ∗δΘ
from section 2.1 acts by +1 resp. by −1. We want to relate the above sheaf
complexes to the variations of Hodge structures V± in lemma 5.10. In this
5.6. Negligible constituents
121
context, the contribution from the weak Lefschetz theorem will be described
by the complexes
L± =
M
µ ∈I±
Hg−2−|µ|(X,C)⊗C δX[µ]
with
(
I+ = 1+2Z,
I−= 2Z,
where by convention Hi(X,C) = 0 for i < 0. Strictly speaking certain Tate
twists should be inserted in the above deﬁnition so that L± become pure
complexes of weight 2g −2 like δΘ ∗δΘ, but to keep the notations simple
we will in what follows suppress all occuring Tate twists.
LEMMA 5.21. If Θ has at most isolated singularities, then there are
semisimple perverse sheaves δ± ∈Perv(X,C) such that
S2(δΘ) ∼= L+ ⊕δ+
and
Λ2(δΘ) ∼= L−⊕δ−,
and over the Zariski-open dense subset U ⊂X from lemma 5.10 we have an
isomorphism
δ±|U ∼= V±ε[g]
with a sign twist by
ε = (−1)g−1.
Proof. Consider the smooth proper family fU :YU −→U that we deﬁned
in lemma 5.3. By the construction in the proof of that lemma, we have a
cartesian diagram
YU = f −1(U)  
/
fU

Θsm ×Θsm  
/ Θ×Θ
f

U  
/ X
where Θsm ⊆Θ is the smooth locus of the theta divisor and where f is
induced by the group law. From the deﬁnition of convolution we therefore
obtain natural identiﬁcations
(δΘ ∗δΘ)|U ∼= (CΘ[g−1]∗CΘ[g−1])|U ∼= R fU∗(CYU[2g−2]).
By Gabber’s decomposition theorem this is a direct sum of degree shifts of
semisimple perverse sheaves, hence
(δΘ ∗δΘ)|U ∼=
2g−4
M
n=0
Hn[2g−2−n]
for the local systems Hn = Rn fU∗(CYU) with stalks Hn
x = Hn(Yx,C). In
the proof of lemma 5.10 we have observed that these local systems contain
constant subsheaves whose stalks are the subspaces which are the images
of the restriction morphisms Hn(X,C) −→Hn(Yx,C). This being said, we
obtain that
(δΘ ∗δΘ)|U = (L+ ⊕L−)|U ⊕V[g]
122
Chapter 5 – A family of surfaces
where V = V+ ⊕V−denotes the local system underlying the variations of
Hodge structures in lemma 5.10. Via Gabber’s decomposition theorem one
then deduces that
δΘ ∗δΘ = L+ ⊕L−⊕δ
for some
δ ∈Db
c (X,C).
But we know from theorem 2.13 that for all n̸ = 0 the perverse cohomology
sheaves pHn(δΘ ∗δΘ) are negligible and are hence by lemma 5.20 multiples
of the constant perverse sheaf δX. Since over the open dense subset U ⊂X
we have δ|U = V[g], it then follows that δ is a perverse sheaf.
Now consider the direct sum decomposition δ = δ+ ⊕δ−where δ± ⊂δ
are deﬁned as the maximal perverse subsheaves on which the commutativity
constraint S : δΘ ∗δΘ −→δΘ ∗δΘ acts by ±1. Going back to the deﬁnitions,
one checks that this commutativity constraint S induces on the stalks the
involution ε ·σ∗
x : Hn(Yx,Q) −→Hn(Yx,Q) where σx :Yx −→Yx denotes the
involution that we deﬁned in section 5.2 and where the twist by the extra
sign ε = (−1)g−1 comes from the degree shift in δΘ = ICΘ[g−1] because
of the Koszul rule for the tensor product of complexes.
□
Recall that a perverse sheaf is said to be clean if it does not admit any
perverse subquotients which are negligible. For a smooth theta divisor we
claim that L± are the only negligible constituents in δΘ ∗δΘ.
LEMMA 5.22. If the theta divisor Θ ⊂X is smooth, then δ± are clean.
Proof. If this were not true, then by lemma 5.20 the semisimple perverse
sheaf δ+ ⊕δ−would contain δX as a summand. Then H−g(X,δ+ ⊕δ−)̸ = 0
and hence the inclusion
H−g(X,L+ ⊕L−) ,→H−g(X,δΘ ∗δΘ)
would be strict. However, the K¨unneth formula in lemma 3.4 and the weak
Lefschetz theorem for the smooth ample divisor Θ ⊂X show that
H−g(X,δΘ ∗δΘ) =
g−1
M
n=1
H−n(X,δΘ)⊗Hn−g(X,δΘ)
=
g−1
M
n=1
Hg−1−n(X,C)⊗Hn−1(X,C)
which by direct inspection is equal to H−g(X,L+ ⊕L−).
□
Note that for a general complex ppav of dimension g the theta divisor
is smooth by the work of Andreotti and Mayer [4], so the above lemma
together with theorem 4.2 leads to the ﬁnal result of this section.
PROPOSITION 5.23. If X is a general complex ppav of dimension g,
then the local systems underlying V± are irreducible.
