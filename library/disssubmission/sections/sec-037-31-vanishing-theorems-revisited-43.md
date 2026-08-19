---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-037-31-vanishing-theorems-revisited-43
section_title: "Vanishing theorems revisited 43"
section_number: 3.1
pages: 51-53
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
The groupΠ(X) of continuous charactersχ : πt
1(X,0)−→Λ∗ admits a
natural product decomposition
Π(X) = Π(X)l′×Π(X)l,
where
Π(X)l′ ={ χ∈ Π(X) : χn = 1 for somen withl ∤ n}
denotes the subgroup of all characters of ﬁnite order prime tol and where by
deﬁnitionΠ(X)l is the group of all characters that factor over the maximal
pro-l-quotientπ1(X,0)l = πt
1(X,0)l. The latter is a freeZl-module of ﬁnite
rank [17]. So with the same arguments as in [41, sect. 3.2] the setΠ(X)l
of pro-l-characters can be identiﬁed with the set ofΛ-valued points of a
scheme in a natural way (even though as in loc. cit. the multiplication of
characters does not come from a group scheme structure). This being said,
we consider the set of all tame characters
Π(X) =
∐
χ∈Π(X)l′
χ· Π(X)l
as the disjoint union of the inﬁnitely many componentsχ· Π(X)l indexed
by the torsion charactersχ∈ Π(X)l′, and we say that a statement holds for
a generic character if it holds for all characters in an open subset ofΠ(X)
that is dense in each of these components.
For sheaf complexesK∈D(X) and charactersχ∈ Π(X) we consider as
in the previous chapters the twistKχ =K⊗ΛLχ by the local systemLχ. Our
Tannakian constructions will be based on the following generic vanishing
assumption for such character twists.
ASSUMPTION GV(X). Let P∈ P(X). Then for genericχ∈ Π(X) the
forget support map
H•
c (X,Pχ)−→H•(X,Pχ)
is an isomorphism, and
Hi(X,Pχ) = Hi
c(X,Pχ) = 0 for all i ⁄= 0.
For complex abelian varieties this is precisely the content of the generic
vanishing theorem 1.1, the claim about the forget support map being trivial
in that case. At present we do not know whether the assumptionGV(X) also
holds for abelian varieties over an algebraically closed ﬁeldk of positive
characteristicp = char(k) > 0, but in any case the semiabelian version can
be deduced from the abelian one as follows.
THEOREM 3.1. If the maximal abelian variety quotient A= X/T of X
satisﬁes the assumption GV(A), then also GV(X) holds.
44 Chapter 3 – Perverse sheaves on semiabelian varieties
Proof.We ﬁrst claim that for any given perverse sheafP∈ P(X), the set
of all charactersχ which violate the conditions in our assumptionGV(X)
forms a closed subset of the schemeΠ(X). To see this, consider the Mellin
transformsM!(P) and M∗(P) as deﬁned in [41, sect. 3.3] (in loc. cit. the
deﬁnition is only given for algebraic tori, but it carries over verbatim to the
case at hand). These Mellin transforms are objects of the bounded derived
category of coherent sheaves onΠ(X) with the property that for alli∈ Z
and any characterχ∈ Π(X) we have isomorphisms
Hi
c(X,Pχ)∼= H i(Li∗
χM!(P)),
Hi(X,Pχ)∼= H i(Li∗
χM∗(P)),
whereiχ :{χ} ↪→Π(X) denotes the embedding of the closed point given by
the chosen character. Furthermore, we have a morphismM!(P)−→M∗(P)
which induces via the above identiﬁcations the forget support morphism on
cohomology. Since on a Noetherian scheme the support of any coherent
sheaf is a closed subset, it follows that the locus of all charactersχ which
violateGV(X) forms a closed subsetS (P)⊆ Π(X) as claimed.
We must show that under the assumptionGV(A) the complement of this
closed subsetS (P) meets every irreducible component ofΠ(X). So we
must see that for at least one characterχ in each component the properties
in GV(X) hold. To this end consider the exact sequence
0−→T i−→X f−→A−→0
which deﬁnes the given semiabelian variety. Lemma 3.2 below will show
that every component ofΠ(X) contains a characterχ such that the forget
support morphism
R f!(Pχ)−→R f∗(Pχ)
is an isomorphism. In this case Artin’s vanishing theorem for the afﬁne
morphismf also shows that these two isomorphic direct image complexes
are perverse [41, lemma 2.4]. For allϕ∈ Π(A) and ψ = f∗(ϕ)∈ Π(X) the
projection formula furthermore says
(R f!(Pχ))ϕ = R f!(Pχψ) and (R f∗(Pχ))ϕ = R f∗(Pχψ),
hence we are ﬁnished by an application of the vanishing assumptionGV(A)
to these perverse direct images. □
To ﬁll in the missing statement in the above proof, we consider the given
semiabelian variety as a torsorf : X−→A under the torusT in the sense
of [74, sect. III.4]. The condition of being a torsor is satisﬁed since clearly
the morphismX×k T−→X×A X, (x,t)↦→ (x,xt) is an isomorphism. The
result we are looking for only uses the structure as a torsor, and for its proof
it will be convenient to forget that our baseA is an abelian variety. So we
will work in the following setting.
