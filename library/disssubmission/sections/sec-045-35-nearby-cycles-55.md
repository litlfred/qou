---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-045-35-nearby-cycles-55
section_title: "Nearby cycles 55"
section_number: 3.5
pages: 63-65
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
EXAMPLE 3.12. For n∈ Nconsider the kernel X[n] of the multiplication
morphism[n] : X−→X. This kernel is a quasi-ﬁnite group scheme over S
and decomposes as a disjoint union
X[n] = Y∐ Z
where Y is ﬁnite over S and where Z∩Xs = ∅. In general Z⁄= ∅, but the
perverse skyscraper sheaf
δZη ∈ P(Xη) satisﬁes Ψ(δZη) = 0
since the support of the nearby cycles must be contained in Z∩Xs = ∅.
For the rest of this section we will always assume that for all geometric
pointst of S the ﬁbreXt satisﬁes the generic vanishing assumptionGV(Xt)
from section 3.1. We can then consider the quotient categories
D(Xt) =D(Xt)/T(Xt) and P(Xt) =P(Xt)/S(Xt)
as deﬁned in section 3.4. Note that the Euler characteristic is well-deﬁned
on objects of these quotient categories.
LEMMA 3.13. The functorΨ descends to a functorΨ: P(Xη)→P(Xs),
for all P,Q∈ P(Xη) we have
0≤ χ(Ψ(P))≤ χ(P),(i)
0≤ χ(Ψ(P)∗Ψ(Q))≤ χ(Ψ(P∗Q)),(ii)
and Ψ(P)∗Ψ(Q) is a direct summand ofΨ(P∗Q) in the categoryP(Xs).
Proof. We begin with some preliminary remarks. Letf : Y→ Z be a
homomorphism of semiabelianS-schemes. By abuse of notation we again
write f for any base change of it. Consider forY =Y×S S and Z = Z×S S
the commutative diagram
Ys
i //
f

Y
f

Yη
joo
f

Zs
i // Z Zη
joo
overS. ForK∈ D(Y) this gives a commutative diagram
i∗(R f!(K))
bc! //
α

R f!(i∗(K))
β

i∗(R f∗(K))
bc∗ // R f∗(i∗(K))
56 Chapter 3 – Perverse sheaves on semiabelian varieties
whereα and β denote the forget support morphisms and wherebc! andbc∗
are the base change morphisms. Let us brieﬂy recall how these latter two
are deﬁned — the direct image of the adjunction morphismK−→i∗(i∗(K))
yields two morphisms
R f!(K)−→R f!(i∗(i∗(K))) = i∗(R f!(i∗(K))),
R f∗(K)−→R f∗(i∗(i∗(K))) = i∗(R f∗(i∗(K))),
and again by adjunction these give rise to the base change morphismsbc!
and bc∗ from above. We also remark [7, exp. XVII, th. 5.2.6] that as a
result of the proper base change theorem, the base change morphismbc! is
always an isomorphism. PuttingK = Rj∗(L) with L∈ D(Yη), we obtain a
factorization
R f!(ΨY(L))
β //
α◦(bc!)−1 ’’PPPPPPPPPPP R f∗(ΨY(L))
ΨZ(R f∗(L))
bc∗
77nnnnnnnnnnnn
whereΨY and ΨZ denote the nearby cycles forY→S resp.Z→S. We will
apply this in the following two situations.
First we takef : X→S to be the structure morphism withY = X, Z = S
and L = P. In this case the above diagram more explicitly says that the
forget support morphismβ for the cohomology of the nearby cyclesΨ(P)
admits the following factorization.
H•c (Xs,Ψ(P))
β //
’’OOOOOOOOOOO H•(Xs,Ψ(P))
H•(Xη,P)
77ooooooooooo
Now consider a characterχ of the tame fundamental group ofX, and denote
by χt∈ Π(Xt) its pull-back to the ﬁbreXt over the special pointt =s or over
the geometric generic pointt = η. The projection formula (see section 3.6)
implies that we have
Ψ(Pχη) = ( Ψ(P))χs
for any such character. In lemma 3.16 we will see thatχ can be chosen in
such a way that the charactersχs and χη are both generic. By the generic
vanishing axiomGV(Xs) we can therefore assume that the forget support
morphismβ is an isomorphism, in which case the above factorization shows
that H•(Xs,Ψ(P)) is a direct summand ofH•(Xη,P). Furthermore, by the
generic vanishing axiomGV(Xη) we can also assume that all the occuring
hypercohomology groups are concentrated in cohomology degree zero, in
which case it follows that 0≤ χ(Ψ(P))≤ χ(P). In particular, the nearby
