---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-014-115-saitos-theorem-and-some-consequences
section_title: "Saito’s Theorem and some consequences"
section_number: 1.1.5
pages: 23-24
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
From the equivalence of the two deﬁnitions of the character variety, we know that
any character χ ∈ X(Γ) is the character of a representation ρ : Γ → SL2(k).
The following theorem of Kyoji Saito [Sai94] generalizes this fact and has crucial
applications for us. We detail the proof in Appendix A, because it is not available
in the literature.
Theorem 1.1.17.LetR be ak-algebra, andχ :B[Γ]→R anR-character. Assume
that χ(∆α,β)is invertible for someα,β ∈ Γ, and letA,B∈ SL2(R) such that TrA =
χ(Yα), TrB = χ(Yβ), TrAB = χ(Yαβ). Then there exists a unique representation
ρ : Γ→ SL2(R) whose character isχ and such thatρ(α) =A and ρ(β) =B.
As a application of this theorem, one can deduce the following proposition, see
[Mar15].
Proposition 1.1.18.Let K be either an algebraically closed ﬁeld or a degree one ex-
tension of an algebraically closed ﬁeld . Then theK-irreducible characters correspond
bijectively to GL2-conjugacy classes of irreducible representationsρ : Γ→ SL2(K).
Idea of the proof.Given an irreducible characterχ : B[Γ]→ K, we ﬁxα,β ∈ Γ
such that χ(∆α,β) is invertible and in order to use Saito’s Theorem, we produce
A =
(χ(Yα) 1
−1 0
)
and B =
(
0 − 1
u
u χ(Yβ)
)
for someu in an at most quadratic extensionˆK
of K such thatu +u−1 =χ(Yαβ). Then we obtain a representationρ : Γ→ SL2( ˆK)
whose character isχ, and general considerations about Brauer groups implies that
ρ could have been picked, in fact, inSL2(K).
The converse map is given byχ(Yγ) = Tr(ρ(γ)), as usual.
Remark 1.1.19. This proposition enlightens about the quotient mapπ : R(Γ)→
X(Γ). It says that given an irreduciblek-characterχ∈X(Γ), all representations in
its ﬁber are pairwise conjugated, hence the ﬁber is isomorphic to the whole group
PSL2(k). It is often summarized saying that on the irreducible open subset of the
character variety, the algebraic quotient is a principalPSL2(k) bundle. On the other
hand, both statement are false outside of the irreducible locus ofX(Γ) : in Example
1.1.5, we have seen that the ﬁber of a central character contains non trivial repre-
sentations, and it easy to see, for instance by a count of dimension, that ﬁbers are
2-dimensional, hence are not isomorphic toPSL2(k).
22
