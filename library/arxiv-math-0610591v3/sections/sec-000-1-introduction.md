---
doc_id: arxiv-math-0610591v3
doc_title: "SCHUR–WEYL DUALITY IN POSITIVE CHARACTERISTIC"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: arxiv-math-0610591v3.pdf
source_sha256: 187a84c35624b171
toc_source: outline
---
Given a set A write SA for the symmetric group on A, i.e., the group
of bijections of A. For σ ∈SA and a ∈A we always write aσ for the
image of a under σ. In other words, we choose to write maps in SA
on the right of their argument. This means that στ (for σ, τ ∈SA) is
deﬁned by a(στ) = (aσ)τ.
We will write Sr as a shorthand for S{1,...,r}.
Consider the group Γ = GL(V ) of linear automorphisms on an n-
dimensional vector space V over a ﬁeld K. We write elements g ∈Γ on
the left of their argument. (Indeed, maps are generally written on the
left in this article, except when they belong to a symmetric group.) The
given action (g, v) →g(v) of Γ on V induces a corresponding action
on a tensor power V ⊗r, with Γ acting the same in each tensor position:
g(u1⊗· · ·⊗ur) = (g(u1))⊗· · ·⊗(g(ur)), for g ∈Γ, ui ∈V . Evidently the
action of Γ commutes with the “place permutation” action of Sr, acting
on V ⊗r on the right via the rule (u1 ⊗· · · ⊗ur)σ = u1σ−1 ⊗· · · ⊗urσ−1.
In this action, a vector that started in tensor position iσ−1 ends up in
tensor position i, thus a vector that started in tensor position i ends
up in tensor position iσ.
We write KG for the group algebra of a group G. The fact that the
two actions commute means that the corresponding representations
(1.1)
Ψ : KΓ →EndK(V ⊗r);
Φ : KSr →EndK(V ⊗r)
The author is grateful to Jun Hu for bringing reference [12] to his attention, and
to the referee for useful suggestions.
1
2
STEPHEN DOTY
induce inclusions
(1.2)
Ψ(KΓ) ⊆EndSr(V ⊗r);
Φ(KSr) ⊆EndΓ(V ⊗r)
where EndSr(V ⊗r) (respectively, EndΓ(V ⊗r)) is deﬁned to be the alge-
bra of linear operators on V ⊗r commuting with all operators in Φ(Sr)
(respectively, Ψ(Γ)). Equivalently, the commutativity of the two ac-
tions says that the representations in (1.1) induce algebra homomor-
phisms
(1.3)
Ψ : KΓ →EndSr(V ⊗r);
Φ : KSr →EndΓ(V ⊗r).
The statement that has come to be known as “Schur–Weyl duality” is
the following.
Theorem 1 (Schur–Weyl duality). For any inﬁnite ﬁeld K, the inclu-
sions in (1.2) are actually equalities. Equivalently, the induced maps
in (1.3) are surjective.
In case K = C this goes back to a classic paper of Schur [21].1 The
main purpose of this survey is to write out a complete proof of the
theorem for an arbitrary inﬁnite ﬁeld, assuming the truth of the result
in case K = C. The strategy, suggested by S. Koenig, is to argue that
the dimension of each of the four algebras in the inclusions (1.2) is
independent of the characteristic of the inﬁnite ﬁeld K. The claim for
a general inﬁnite ﬁeld K then follows immediately from the classical
result over C, by dimension comparison.
We make no claim that this strategy is “best” in any sense; it is
merely one possible approach. For a completely diﬀerent recent ap-
proach, see [16].
