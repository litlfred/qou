---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-084-56-negligible-constituents-119
section_title: "Negligible constituents 119"
section_number: 5.6
pages: 127-129
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
any such curve has genusg ˜C =2g+1 =9. Hence the adjunction formula for
the genus of a smooth curve on a smooth projective surface [55, prop. V .1.5]
gives the intersection number
degY(λ2) = 2g ˜C−2−degY(KY| ˜C) = 16−16 = 0,
indeed for the canonical classKY we have
deg˜C(KY| ˜C) = degY(λ∪KY) = degX(2· [Θ]4/3) = 16
by the formulai!(λ) = [Θ]3/3 from above and by lemma 5.5. We then also
obtain the intersection number degY(β2) =degY(λ2)−degY(α2) =−8/3,
and to see that the vectore is a minimal vector all that remains to be done
is to divide the bilinear form by two. □
It seems a tempting idea to prove theorem 5.1 by looking directly at the
monodromy operation on the fundamental classes of the Prym-embedded
curves from above, but we have not seen how to do this. In what follows we
give a different proof which does not use the Prym construction, and from
this point of view the theorem can be seen as an independent result about
the monodromy operation on the 27 Prym-embedded curves.
5.6. Negligible constituents
We now justify our earlier statement that for a general ppav the local
systems underlying the variations of Hodge structuresV+ and V− from
lemma 5.10 are irreducible. In fact we will obtain stronger results since we
will work with perverse sheaves on the whole ppav rather than with local
systems on a Zariski-open dense subset. This shift in perspective reveals a
close connection with the Tannakian formalism of convolution as developed
in chapters 2 and 3, which is of interest in its own right.
Recall that for any complex abelian varietyX, the convolution product
on the derived categoryDbc (X,C) of bounded complexes ofC-sheaves with
constructible cohomology sheaves in the sense of [10] is deﬁned by
K∗L = Ra∗(K⊠L)∈ Db
c (X,C) for K,L∈ Db
c (X,C),
wherea : X×X−→X denotes the group law. One of the main results of
chapter 2 was that the full abelian subcategory Perv(X,C)⊂ Dbc (X,C) of
perverse sheaves is almost stable under the convolution product: Let us say
that a perverse sheaf is negligible if all its perverse subquotients have Euler
characteristic zero; then theorem 2.13 shows that for allP,Q∈ Perv(X,C)
and alln⁄= 0 the perverse cohomology sheaves
pHn(X,P∗Q)∈ Perv(X,C)
are negligible. At the other end of the scale, we will say that a perverse
sheaf is clean if it does not have any negligible subquotients.
120 Chapter 5 – A family of surfaces
Suppose now thatX has dimensiong≥ 2 and is principally polarized
with a symmetric theta divisorΘ⊂X, and consider the perverse intersection
cohomology sheaf
δΘ = ICΘ[g−1]∈ Perv(X,C).
This is a semisimple perverse sheaf and arises via intermediate extension
from the constant sheaf on the smooth locus of the theta divisor. Thus we
haveδΘ = CΘ[g−1] if the theta divisor is smooth, but later on we will also
deal with isolated singularities.
LEMMA 5.20. If the theta divisorΘ has at most isolated singularities,
then for every clean perverse sheaf P and all n∈ Z, any simple negligible
subquotient ofpHn(δΘ∗P) is isomorphic toδX = CX[g].
Proof. By Verdier duality it sufﬁces to show this forn≤ 0. Since the
theta divisor is a local complete intersection, by [65, lemma III.6.5] the
shifted constant sheafλΘ = CΘ[g−1] is perverse, so we have an exact
sequence of perverse sheaves
0−→κ−→λΘ−→δΘ−→0
whereκ is a skyscraper sheaf supported on the ﬁnite set of singular points
of the theta divisor. Convolution with the clean perverse sheafP yields a
distinguished triangle
κ∗P // λΘ∗P // δΘ∗P
[+1] //···
where κ∗ P is again a clean perverse sheaf. By the corresponding long
exact sequence of perverse cohomology groups, it will therefore sufﬁce to
show that every simple negligible subquotient ofpHn(λΘ∗P) forn≤0 must
be isomorphic toδX. But this follows as in [110, ex. 3] from the excision
sequence for the ample divisorΘ⊂ X with afﬁne complementX\Θ, using
Artin’s vanishing theorem. □
Let us now consider the convolution squareδΘ∗ δΘ. Due to Gabber’s
decomposition theorem this is a direct sum of degree shifts of semisimple
perverse sheaves. So we can write
δΘ∗δΘ = S2(δΘ)⊕Λ2(δΘ)
where the symmetric square and the alternating square on the right hand side
are by deﬁnition the maximal direct summands on which the commutativity
constraint
S = SδΘ,δΘ : δΘ∗δΘ−→ δΘ∗δΘ
from section 2.1 acts by+1 resp. by−1. We want to relate the above sheaf
complexes to the variations of Hodge structuresV± in lemma 5.10. In this
