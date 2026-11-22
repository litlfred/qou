---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-007-116-the-augmented-variety
section_title: "The augmented variety"
section_number: 1.1.6
pages: 24-25
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The augmented variety
In this subsection we deﬁne a two-fold cover of the character variety when Γ is the
fundamental group of a 3-manifold with boundary a single torus, which has been
previously considered by several authors, see for instance [DG16]. Both the deﬁnition
and the motivation arise from the following example. This augmented variety will
be used in Chapter 2.
Example 1.1.20 (The character variety X(∂M) = X(Z2)). Let χ ∈X(∂M) be
a k-character, it is the character of a semi-simple representation ρ : Z2 →SL2(k).
Since Z2 is abelian, it can be written ρ(γ) =

λ(γ)
0
0
λ−1(γ)

, and χ(Yγ) = λ(γ)+λ−1(γ)
for some λ ∈H1(∂M, k∗). Moreover, there is an involution σ of H1(∂M, k∗) that
sends λ to λ−1, and clearly what we have just described is a morphism X(∂M) →
H1(∂M, k∗)/σ ≃(k∗)2/σ that turns out to be an isomorphism.
On the functions algebra side, there is a map from B[Z2] into the algebra C[Z2] =
k[Zγ, γ ∈Z2]/(ZγZδ −Zγδ), the latter being isomorphic to k[X, X−1, Y, Y −1], that
sends Yγ 7→Zγ+Zγ−1. Its image lies in the σ-invariant part C[Z2]σ ≃k[X+X−1, Y +
Y −1, XY +(XY )−1], for σ : Zγ 7→Zγ−1 and we get an isomorphism B[Z2] ≃C[Z2]σ.
The double cover we are going to deﬁne is H1(∂M, k∗) in this example, it corresponds
to a choice of an eigenvalue function Zγ for γ ∈∂M a boundary curve.
Deﬁnition 1.1.21. We deﬁne the augmented representation variety ¯R(M) to be the
subvariety of R(M)×H1(∂M, k∗) given by the pairs {(ρ, λ), ρ : π1(M) →SL2(k), λ :
π1(∂M) →k∗, λ(γ) + λ(γ)−1 = Tr ρ(γ) ∀γ ∈π1(∂M)}.
Again SL2(k) acts on ¯R(M), trivially on the second factor, thus we deﬁne the aug-
mented character variety to be the quotient ¯X(M) = ¯R(M)// SL2(k).
The advantage of this two-fold covering is the following : on one hand the functions
of X(M) are trace functions, on the other hand on ¯X(M) we have at our disposal,
for any γ ∈π1(∂M), two eigenvalue functions Zγ±1 that maps the pair (ρ, λ) to an
eigenvalue λ(γ) for ρ(γ).
The following deﬁnition provides a direct description of the algebraic quotient.
Deﬁnition 1.1.22. Denote by ¯B[Γ] = B[Γ]⊗B[π1(∂M)] C[π1(∂M)] and we deﬁne the
augmented character variety as the ﬁbered product :
¯X(M) = X(M) ×X(∂M) H1(∂M, k∗)
that is, ¯X(M) = Spec ¯B[Γ].
23
