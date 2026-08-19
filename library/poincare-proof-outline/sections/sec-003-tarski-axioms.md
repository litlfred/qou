---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-003-tarski-axioms
section_title: "Tarski axioms"
section_number: null
pages: 4-5
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
In this section we introduce axioms of Tarski [ 7] trough a series of locales.
theory Tarski
imports Main
begin
The ﬁrst locale assumes all Tarski axioms except for the Euclid’s axiom and the continuity axiom and corresponds
to absolute geometry.
locale TarskiAbsolute =
4
ﬁxes cong :: ′p⇒ ′p⇒ ′p⇒ ′p⇒ bool
ﬁxes betw :: ′p⇒ ′p⇒ ′p⇒ bool
assumes cong-reﬂexive: cong x y y x
assumes cong-transitive: cong x y z u ∧ cong x y v w −→ cong z u v w
assumes cong-identity: cong x y z z −→ x = y
assumes segment-construction:∃ z. betw x y z ∧ cong y z a b
assumes ﬁve-segment: x⁄= y∧ betw x y z ∧ betw x ′ y ′ z ′∧ cong x y x ′ y ′∧ cong y z y ′ z ′∧ cong x u x ′ u ′∧ cong
y u y ′ u ′−→ cong z u z ′ u ′
assumes betw-identity: betw x y x −→ x = y
assumes Pasch: betw x u z ∧ betw y v z −→ (∃ a. betw u a y ∧ betw x a v )
assumes lower-dimension:∃ a.∃ b.∃ c.¬ betw a b c ∧¬ betw b c a ∧¬ betw c a b
assumes upper-dimension: cong x u x v ∧ cong y u y v ∧ cong z u z v ∧ u⁄= v−→ betw x y z ∨ betw y z x ∨ betw z
x y
begin
The following deﬁnitions are used to specify axioms in the following locales.
Pointp is on line ab.
deﬁnition on-line where
on-line p a b ←→ betw p a b ∨ betw a p b ∨ betw a b p
Pointp is on ray ab.
deﬁnition on-ray where
on-ray p a b ←→ betw a p b ∨ betw a b p
Pointp is inside angle abc.
deﬁnition in-angle where
in-angle p a b c ←→ b⁄= a∧ b⁄= c∧ p⁄= b∧ (∃ x. betw a x c ∧ x⁄= a∧ x⁄= c∧ on-ray p b x )
Rayrarb meets the line lalb.
deﬁnition ray-meets-line where
ray-meets-line ra rb la lb ←→ (∃ x. on-ray x ra rb ∧ on-line x la lb )
end
The second locales adds the negation of Euclid’s axiom and limiting parallels and corresponds to hyperbolic
geometry.
locale TarskiHyperbolic = TarskiAbsolute +
assumes euclid-negation:∃ a b c d t . betw a d t ∧ betw b d c ∧ a⁄= d∧ (∀ x y. betw a b x ∧ betw a c y −→¬ betw
x t y )
assumes limiting-parallels:¬ on-line a x1 x2 =⇒
(∃ a1 a2.¬ on-line a a1 a2 ∧
¬ ray-meets-line a a1 x1 x2 ∧
¬ ray-meets-line a a2 x1 x2 ∧
(∀ a ′. in-angle a ′ a1 a a2 −→ ray-meets-line a a ′ x1 x2 ))
The third locale adds the continuity axiom and corresponds to elementary hyperbolic geometry.
locale ElementaryTarskiHyperbolic = TarskiHyperbolic +
assumes continuity: [ [∃ a.∀ x.∀ y. ϕx∧ ψ y−→ betw a x y ] ] =⇒∃ b.∀ x.∀ y. ϕx∧ ψ y−→ betw x b y
end
