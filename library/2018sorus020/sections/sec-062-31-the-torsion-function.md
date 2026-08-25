---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-062-31-the-torsion-function
section_title: "The torsion function"
section_number: 3.1
pages: 85-87
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
has a pole atx.
The proof of this theorem recovers two cases, treated separately in Section 3.3.1,
where the components of the incompressible surface split M, and Section 3.3.2,
where they do not. The hypothesis on the boundary eigenvalues is discussed in the
beginning of Section 3.3.1, on the other hand it is automatically satisﬁed in Section
3.3.2.
If M is hyperbolic, the question whether the torsion deﬁnes a non-constant func-
tion on a geometric component has been addressed in [DFJ12, Section 1.7]. It is
motivated by the following observation and conjecture : this article of Nathan Dun-
ﬁeld, Stefan Friedl and Nicholas Jackson studies twisted Alexander polynomial of
hyperbolic knots. It is a Laurent polynomial∆ρ(t) associated to a representation of
the fundamental groupρ :π1(M)→ SL2(C), and it follows from its deﬁnition that
∆ρ(1) = tor(M,ρ )(χρ), for χρ the character corresponding toρ. It is conjectured
from numerical evidences that this polynomial considered at the holonomy repre-
sentation carries a lot of topological information on the manifoldM, as ﬁberness,
chirality, genus and volume. If the torsion was constant, it would suggest a disproof
of this conjecture . This question is motivated by the fact that the torsion is known
to be locally constant on the character variety of torus knots. The ﬁrst computation
of non constant torsion function has been performed by Teruaki Kitano in [Kit94]
for the ﬁgure-eight knot. We deduce the following corollary of Theorem 3.0.2, which
answer partially to this question. Recall that a connected surfaceΣ∈ M is free if
M\S is a union of handlebodies.
Corollary 3.0.3.LetM be a hyperbolic manifold andX be a geometric component
of its SL2(C) character variety. Assume that an ideal point ofX detects an incom-
84
pressible surface which is connected or union of parallel free copies, and such that
the eigenvalue of its boundary curve is 1. Then the torsion function is not constant
on the componentX.
The relation with twisted Alexander polynomial suggests an other interpretation of
the vanishing locus of the torsion : given an irreducible representationρ :π1(M)→
SL2(k), one can construct a semi-simple representation ˜ρ : π1(M)→ SL3(k) by
deﬁning˜ρ =
(ρ 0
0 1
)
. A classical dimensional argument (see [HP15, Section 5] for
instance), shows that if˜ρ is deformable into irreducible representations in the cha-
racter varietyX(M, SL3(k)) then it necessarily exists a reducible, non semi-simple
representation ˜ρ′ with the same character, namely˜ρ′ = (ρ z
0 1 ) where z :π1(M)→k2
represents a non trivial class in H1(M,ρ ). More generally, given λ ∈ k∗ and a
surjective abelianization mapϕ : π1(M)→ Z, it is proven in [HP15] that if the
representation ˜ρλ =
(λϕρ 0
0 λ−2ϕ
)
is deformable into irreducible representations, then
the Twisted Alexander Polynomial∆ρ(λ3) vanishes. A converse statement is proved
in the case whenλ3 is a simple root of the Twisted Alexander Polynomial. Our
Theorem 3.0.1 is a ﬁrst step in a proof of a general converse statement whenλ = 1,
saying that if∆ρ(1) = 0 then there exists a non trivialz∈ H1(M,ρ ), hence a non
semi-simple ˜ρ′ as above, generalizing an basic fact from theSL2-case.
This chapter divides into three sections, in Section 1 we deﬁne the torsion as a
rational function on a component on the character variety, in Section 2 we prove
Theorem 3.0.1, and in Section 3 we prove Theorem 3.0.2.
3.1 The torsion function
LetX be a one-dimensional, reduced component of irreducible type of the character
varietyX(M), recall that a component of irreducible type means that it contains the
character of an irreducible representation. In Section 1.1.7 we deﬁnedρ :π1(M)→
SL2(k(X)) the tautological representation, up to conjugation. Hence the torsion of
thetwistedcomplex C∗(M,ρ )ofk(X)-vectorspacesiswell-deﬁned,andisanelement
of the homological determinant vector spacetor(M,ρ )∈ det(H∗(M,ρ )). The ﬁrst
statement of the following proposition follows directly from this deﬁnition. Recall
thatX is a geometric component if it carries the holonomy character of a hyperbolic
structure onM. In Section 1.3.4, we have seen that for anyχ∈X there is a valuation
v on k(X), and a choice of a convergent tautological representationρ : π1(M)→
SL2(Ov). The reduction modt mapOv→ k deﬁnes a residual representation¯ρ :
85
π1(M)→ SL2(k− whose character is the pointχ. We denote byH∗(M,ρ )v the
cohomologicalOv-modules and by H∗(M, ¯ρ) the residual cohomological k-vector
spaces.
Proposition 3.1.1.If the complexC∗(M,ρ ) is acyclic, then the Reidemeister func-
tion tor(M,ρ )∈k(X)∗ deﬁnes a rational function on the curveX. In particular, it
is the case as soon asX is a geometric component.
Proof. We just have to show that ifX is a geometric component, thenHi(M,ρ ) = 0
for alli. SinceM has the homotopy type of a two-dimensional CW complex, it has
no homology in rank greater that 2.
The space of invariantsH0(M,ρ ) ={z∈k(X)2|ρ(γ)z =z,∀γ∈π1(M)} is non tri-
vial if and only ifTr(ρ(γ)) = 2 for allγ∈π1(M), but the tautological representation
is irreducible, thusH0(M,ρ ) = 0.
We know that the Euler characteristicχ(M) is zero, hence it is now enough to
prove that H1(M,ρ ) = 0 . The Universal Coeﬃcients Theorem provides isomor-
phisms H1(M,ρ )v⊗k(X)≃ H1(M,ρ ) and H1(M, ¯ρ)≃ H1(M,ρ )v⊗k, hence it
is enough to show that for someχ∈ X, one hasH1(M, ¯ρ) = 0 . It follows from
Ragunathan’s vanishing theorem (see for instance [MP12, Theorem 0.2]) that it is
the case ifχ is the character of a holonomy representation.
Remark 3.1.2. As soon as there exists a characterχ∈ X such thatH1(M, ¯ρ) is
trivial, the proposition applies and the torsion deﬁnes a well-deﬁned function on the
curveX. If follows from the semi-continuity of the dimension ofH1(M, ¯ρ) onX that
in this case,H1(M, ¯ρ) is trivial for all but a ﬁnite numbersχ∈X. It has been the
way to deﬁne almost everywhere the torsion function onX, the novelty here is that
it is deﬁneda priori even at charactersχ with non trivial ﬁrst cohomology groups.
Indeed, we will show in the next section that the torsion vanishes exactly in those
points.
