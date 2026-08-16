---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-060-44-degenerations-of-abelian-varieties-81
section_title: "Degenerations of abelian varieties 81"
section_number: 4.4
pages: 89-91
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
Hesse matrix ( ∂2ϑ
∂zα∂zβ
(τ,z)
)
α,β=1,...,g
is non-zero. Then the heat equation
∂ ϑ
∂ ταβ
(τ,z) = 2πi· (1+δαβ )· ∂2ϑ
∂zα∂zβ
(τ,z)
implies for the gradient with respect to the variableτ that (∇τϑ)(τ,z)⁄= 0
as well. Hence, takingS to be a curve which passes through the points in
a sufﬁciently general tangent directionu, we obtain with notations as in the
preceding paragraph that
(∂F/∂w)(0,z) = ( u· ∇τϑ)(τ,z)⁄= 0
whereF(w,z) = ϑ(h(w),z) is deﬁned forw in some coordinate disk∆⊂ S
by a suitable local lifth : ∆→ Hg with h(0) = τ. In particular, since the
gradient ofF does not vanish at the considered point, it follows that(τ,z)
deﬁnes a smooth point of the total spaceΘS of our family. This shows that
the inclusion in claim(b) is strict. □
We will now use the above construction to obtain information about the
Tannaka groupsG(δΘτ ) by varying the base pointτ∈ Ag,n(C). In order to
apply the algebraic formalism of nearby cycles developed in section 4.3 we
consider perverse sheaves with coefﬁcients inΛ = Ql throughout, but the
ﬁnal result may as well be read in the category of analytic perverse sheaves
with coefﬁcients inΛ = C. Anyway all the occuring perverse sheaves will
be of geometric origin in the sense of [10, sect. 6.2.4].
In general it is not clear how to put the perverse sheavesδΘτ for the
various pointsτ∈ Ag,n(C) into a global family because there is no good
relative notion of a perverse intersection cohomology sheaf. However, over
the Zariski-open dense locusU⊂ Ag,n of ppav’s with a smooth theta divisor
this is no issue — the shifted constant sheafΛΘ[g−1] restricts toδΘτ on the
ﬁbre Xτ for each geometric pointτ in U. This being said, proposition 3.20
shows that there are ﬁnitely many reductive algebraic groupsG1, . . . ,Gm
overΛ and a constructible stratiﬁcation
U =
m⨆
i=0
Ui with G(δΘτ ) =Gi for all geometric pointsτ inUi.
The hypotheses of the proposition are satisﬁed because for each geometric
point τ in U the divisor Θτ⊂ Xτ is irreducible and symmetric. Indeed
these two conditions precisely say that the perverse sheafδΘτ is simple and
isomorphic to its adjoint dual.
82 Chapter 4 – The Tannaka group of the theta divisor
LetU0⊆U be the open dense stratum so thatG0⊆ G(g) is the Tannaka
group of the theta divisor on a generic ppav. By lemma 4.6 the perverse
intersection cohomology sheaf of such a theta divisor corresponds on the
Tannakian side to the restrictionV|G0 of the standard representationV of
the special orthogonal or symplectic groupG(g).
PROPOSITION 4.12. With notations as above, the following properties
hold for the Tannaka groups of smooth theta divisors.
(1) For g= g1 +g2 the generic Tannaka group G0 has a subquotient
which is isogenous to
G(g1)×G(g2),
provided that theorem 4.2 holds for the dimensions g1 and g2.
(2) There exists a connected subgroup H↪→ G0 and an irreducible
representation W of H such that
V|H =
{
W⊕1⊕1 if g is even,
W⊕1 if g is odd,
where1 denotes the one-dimensional trivial representation.
(3) For g≥ 4 and any stratum Ui of codimension at most one in U
there exists a homomorphism
f : Sl2g−2(Λ)−→Gi
such that f∗(V) contains the g−1st fundamental representation of
the special linear group as a direct summand.
Proof.Consider a morphism from a smooth irreducible quasi-projective
complex curveS to the moduli spaceAg,n such that the generic point ofS is
mapped into some stratumUi in the above stratiﬁcation, and ﬁx a geometric
generic pointη of S. Passing to the strict Henselization ofS at s∈ S(C)
we can form the perverse sheafΨ(δΘη)∈ Perv(Xs,C) of nearby cycles. By
theorem 3.15 we have an embedding
G(Ψ(δΘη)) ↪→ G(δΘη) = Gi ↪→ G(g)
such thatΨ(δΘη) corresponds on the Tannakian side to the restriction of the
standard representationV to the subgroupG(Ψ(δΘη)). We will apply this
remark in the following situations.
For part (1) takeS ↪→ Ag,n to be an embedding of a smooth curve which
meets the locus of decomposable ppav’s in a single points∈S(C) but which
is otherwise contained in the open dense stratumU0 and has the properties
