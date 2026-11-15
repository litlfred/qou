---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-020-141-reducible-character-in-components-of-irreduc
section_title: "Reducible character in components of irreducible type of the character variety"
section_number: 1.4.1
pages: 39-40
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Reducible character in components of irreducible type
of the character variety
Deﬁnition 1.4.1. Let X be a one dimensional component of irreducible type of
the character variety X(M), v ∈ˆX a ﬁnite point in the smooth projective model
of X, and ρ : π1(M) →SL2(Ov) a convergent representative of the tautological re-
presentation. We will say the representation ρ is residually reducible (resp. residualy
abelian, irreducible, central) if the residual representation ¯ρ : π1(M) →SL2(k) is
reducible (resp. abelian, irreducible, central). Recall in addition that a character χ
is said central if χ(Yγ)2 = 4 for all Yγ ∈k[X].
Since X is of irreducible type, irreducible characters are dense in X hence for a
generic v ∈ˆX, the tautological representation ρ will be residually irreducible. Ne-
vertheless, there may exists a ﬁnite set of points where it is residually reducible,
they correspond to characters that are intersection points of X with a component
of reducible type of X(M).
Proposition 1.4.2. Let χ ∈X a reducible character, v ∈ˆX the associated va-
luation, and ρ : Γ →SL2(Ov) a choice of convergent tautological representation.
Then the character χ¯ρ is not central, and in particular the representation ρ is not
residually central. Moreover, one can choose the tautological representation ρ such
that it is not residually abelian.
Proof. In [Por97, Lemma 3.9], it is proved that a reducible character χ¯ρ in a com-
ponent of irreducible type X cannot be central, because there exists a non abelian
representation σ : Γ →SL2(k) with character χ¯ρ. It proves the ﬁrst claim. It remains
to show that such a non abelian representation is realized as ¯ρ, for some choice of
tautological representation ρ. We give a tree-theoretical argument.
38
Let Tv be the Bass-Serre tree associated to v, and consider the action of Γ on Tv.
— As the tautological representation is convergent, the subtree T ′
v of ﬁxed points
is non empty.
— The tree T ′
v is ﬁnite, because if not it would contain an half-line, hence from
Subsection 1.3.2 the tautological representation would ﬁx a line in ˆO2
v and it
would contradict the irreducibility of ρ.
— The tree T ′
v is a segment : assume it contains a vertex of valence at least 3
s
t
u
v
Then t, u and v represents three distincts points in kP1, ﬁxed by the residual
representation ¯ρ. Hence ¯ρ(Γ) ⊂{± Id} but it is a contradiction with the ﬁrst
part of the proposition.
— We just proved that T ′ is of the following form :
s0
s1
s2
...
sn−1
sn
Fix a basis such that si is the lattice Ov ⊕tiOv. Then for any γ ∈Γ, ρ(γ) =

a(γ) b(γ)
c(γ) d(γ)

∈SL2(Ov), with c(γ) ∈(tn). We conclude by noting that for some
γ ∈Γ, we have b(γ) ∈O∗
v ; because if not there should be an other ﬁxed point
at the left of s0. Finally, ρ is not residually abelian, and residually reducible
as soon as n > 0.
