---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-085-56-negligible-constituents-121
section_title: "Negligible constituents 121"
section_number: 5.6
pages: 129-131
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
context, the contribution from the weak Lefschetz theorem will be described
by the complexes
L± =
⨁
µ∈I±
Hg−2−|µ|(X,C)⊗C δX[µ] with
{
I+ = 1+2Z,
I− = 2Z,
where by conventionHi(X,C) = 0 fori < 0. Strictly speaking certain Tate
twists should be inserted in the above deﬁnition so thatL± become pure
complexes of weight 2g−2 like δΘ∗ δΘ, but to keep the notations simple
we will in what follows suppress all occuring Tate twists.
LEMMA 5.21. If Θ has at most isolated singularities, then there are
semisimple perverse sheavesδ±∈ Perv(X,C) such that
S2(δΘ)∼= L+⊕δ+ and Λ2(δΘ)∼= L−⊕δ−,
and over the Zariski-open dense subset U⊂X from lemma 5.10 we have an
isomorphism
δ±|U∼= V±ε[g] with a sign twist by ε = (−1)g−1.
Proof.Consider the smooth proper familyfU :YU−→U that we deﬁned
in lemma 5.3. By the construction in the proof of that lemma, we have a
cartesian diagram
YU = f−1(U)   //
fU

Θsm×Θsm   // Θ×Θ
f

U   // X
where Θsm⊆ Θ is the smooth locus of the theta divisor and wheref is
induced by the group law. From the deﬁnition of convolution we therefore
obtain natural identiﬁcations
(δΘ∗δΘ)|U∼= (CΘ[g−1]∗CΘ[g−1])|U∼= R fU∗(CYU[2g−2]).
By Gabber’s decomposition theorem this is a direct sum of degree shifts of
semisimple perverse sheaves, hence
(δΘ∗δΘ)|U ∼=
2g−4⨁
n=0
Hn[2g−2−n]
for the local systemsHn = Rn fU∗(CYU) with stalks Hnx = Hn(Yx,C). In
the proof of lemma 5.10 we have observed that these local systems contain
constant subsheaves whose stalks are the subspaces which are the images
of the restriction morphismsHn(X,C)−→Hn(Yx,C). This being said, we
obtain that
(δΘ∗δΘ)|U = ( L+⊕L−)|U⊕V[g]
122 Chapter 5 – A family of surfaces
whereV = V+⊕V− denotes the local system underlying the variations of
Hodge structures in lemma 5.10. Via Gabber’s decomposition theorem one
then deduces that
δΘ∗δΘ = L+⊕L−⊕δ for some δ∈ Db
c (X,C).
But we know from theorem 2.13 that for alln⁄= 0 the perverse cohomology
sheavespHn(δΘ∗δΘ) are negligible and are hence by lemma 5.20 multiples
of the constant perverse sheafδX. Since over the open dense subsetU⊂ X
we haveδ|U = V[g], it then follows thatδ is a perverse sheaf.
Now consider the direct sum decompositionδ = δ+⊕δ− whereδ±⊂ δ
are deﬁned as the maximal perverse subsheaves on which the commutativity
constraintS : δΘ∗δΘ−→δΘ∗δΘ acts by±1. Going back to the deﬁnitions,
one checks that this commutativity constraintS induces on the stalks the
involutionε·σ∗x : Hn(Yx,Q)−→Hn(Yx,Q) whereσx :Yx−→Yx denotes the
involution that we deﬁned in section 5.2 and where the twist by the extra
sign ε = (−1)g−1 comes from the degree shift inδΘ = ICΘ[g−1] because
of the Koszul rule for the tensor product of complexes. □
Recall that a perverse sheaf is said to be clean if it does not admit any
perverse subquotients which are negligible. For a smooth theta divisor we
claim thatL± are the only negligible constituents inδΘ∗δΘ.
LEMMA 5.22. If the theta divisorΘ⊂ X is smooth, thenδ± are clean.
Proof.If this were not true, then by lemma 5.20 the semisimple perverse
sheafδ+⊕δ− would containδX as a summand. ThenH−g(X,δ+⊕δ−)⁄=0
and hence the inclusion
H−g(X,L+⊕L−) ↪→ H−g(X,δΘ∗δΘ)
would be strict. However, the K¨unneth formula in lemma 3.4 and the weak
Lefschetz theorem for the smooth ample divisorΘ⊂ X show that
H−g(X,δΘ∗δΘ) =
g−1⨁
n=1
H−n(X,δΘ)⊗Hn−g(X,δΘ)
=
g−1⨁
n=1
Hg−1−n(X,C)⊗Hn−1(X,C)
which by direct inspection is equal toH−g(X,L+⊕L−). □
Note that for a general complex ppav of dimensiong the theta divisor
is smooth by the work of Andreotti and Mayer [4], so the above lemma
together with theorem 4.2 leads to the ﬁnal result of this section.
PROPOSITION 5.23. If X is a general complex ppav of dimension g,
then the local systems underlyingV± are irreducible.
