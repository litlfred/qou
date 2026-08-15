---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-063-interpretation-of-locales
section_title: "Interpretation of locales"
section_number: null
pages: 170-175
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
global-interpretation PoincareTarskiAbsolute: TarskiAbsolute where cong = p-congruent and betw = p-between
deﬁnes p-on-line = PoincareTarskiAbsolute.on-line and
p-on-ray = PoincareTarskiAbsolute.on-ray and
p-in-angle = PoincareTarskiAbsolute.in-angle and
p-ray-meets-line = PoincareTarskiAbsolute.ray-meets-line
proof−
show TarskiAbsolute p-congruent p-between
proof
1. Reﬂexivity of congruence
ﬁx x y
show p-congruent x y y x
unfolding p-congruent-def
by transfer (simp add : poincare-distance-sym)
next
2. Transitivity of congruence
ﬁx x y z u v w
show p-congruent x y z u ∧ p-congruent x y v w −→ p-congruent z u v w
by (transfer, simp)
next
3. Identity of congruence
ﬁx x y z
show p-congruent x y z z −→ x = y
unfolding p-congruent-def
by transfer (simp add : poincare-distance-eq-0-iﬀ)
next
4. Segment construction
170
ﬁx x y a b
show∃ z. p-between x y z ∧ p-congruent y z a b
using segment-construction
unfolding p-congruent-def
by transfer (simp, blast)
next
5. Five segment
ﬁx x y z x ′ y ′ z ′ u u ′
show x⁄= y∧ p-between x y z ∧ p-between x ′ y ′ z ′∧
p-congruent x y x ′ y ′∧ p-congruent y z y ′ z ′∧
p-congruent x u x ′ u ′∧ p-congruent y u y ′ u ′−→
p-congruent z u z ′ u ′
unfolding p-congruent-def
apply transfer
using ﬁve-segment-axiom
by meson
next
6. Identity of betweeness
ﬁx x y
show p-between x y x −→ x = y
by transfer (simp add : poincare-between-sum-distances poincare-distance-eq-0-iﬀ poincare-distance-sym)
next
7. Pasch
ﬁx x y z u v
show p-between x u z ∧ p-between y v z −→ (∃ a. p-between u a y ∧ p-between x a v )
apply transfer
using Pasch
by blast
next
8. Lower dimension
show∃ a.∃ b.∃ c.¬ p-between a b c ∧¬ p-between b c a ∧¬ p-between c a b
apply (transfer)
using lower-dimension-axiom
by simp
next
9. Upper dimension
ﬁx x y z u v
show p-congruent x u x v ∧ p-congruent y u y v ∧ p-congruent z u z v ∧ u⁄= v−→
p-between x y z ∨ p-between y z x ∨ p-between z x y
unfolding p-congruent-def
by (transfer, simp add : upper-dimension-axiom)
qed
qed
interpretation PoincareTarskiHyperbolic: TarskiHyperbolic
where cong = p-congruent and betw = p-between
proof
10. Euclid negation
show∃ a b c d t . p-between a d t ∧ p-between b d c ∧ a⁄= d∧
(∀ x y. p-between a b x ∧ p-between a c y −→¬ p-between x t y )
using negated-euclidean-axiom
by transfer (auto, blast)
next
ﬁx a x1 x2
assume¬ TarskiAbsolute.on-line p-between a x1 x2
hence¬ p-on-line a x1 x2
using TarskiAbsolute.on-line-def [OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
171
using PoincareTarskiAbsolute.on-line-def
by simp
11. Limiting parallels
thus∃ a1 a2.
¬ TarskiAbsolute.on-line p-between a a1 a2 ∧
¬ TarskiAbsolute.ray-meets-line p-between a a1 x1 x2 ∧
¬ TarskiAbsolute.ray-meets-line p-between a a2 x1 x2 ∧
(∀ a ′. TarskiAbsolute.in-angle p-between a ′ a1 a a2 −→ TarskiAbsolute.ray-meets-line p-between a a ′ x1 x2 )
unfolding TarskiAbsolute.in-angle-def [OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-ray-def [OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
unfolding TarskiAbsolute.ray-meets-line-def[OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-ray-def [OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-line-def [OF PoincareTarskiAbsolute.TarskiAbsolute-axioms]
unfolding PoincareTarskiAbsolute.on-line-def
apply transfer
proof−
ﬁx a x1 x2
assume∗: a∈ unit-disc x1 ∈ unit-disc x2 ∈ unit-disc
¬ (poincare-between a x1 x2 ∨ poincare-between x1 a x2 ∨ poincare-between x1 x2 a )
hence¬ poincare-on-line a x1 x2
using poincare-collinear3-iﬀ[of a x1 x2 ]
using poincare-between-rev poincare-on-line-def by blast
hence∃ a1∈unit-disc.
∃ a2∈unit-disc.
¬ poincare-on-line a a1 a2 ∧
¬ poincare-ray-meets-line a a1 x1 x2 ∧
¬ poincare-ray-meets-line a a2 x1 x2 ∧
(∀ a ′∈unit-disc.
poincare-in-angle a ′ a1 a a2 −→
poincare-ray-meets-line a a ′ x1 x2 )
using limiting-parallels[of a x1 x2 ]∗
by blast
then obtain a1 a2 where∗∗: a1∈unit-disc a2∈unit-disc¬ poincare-on-line a a1 a2
¬ poincare-ray-meets-line a a2 x1 x2
¬ poincare-ray-meets-line a a1 x1 x2
∀ a ′∈unit-disc.
poincare-in-angle a ′ a1 a a2 −→
poincare-ray-meets-line a a ′ x1 x2
by blast
have¬ (∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a1 ∨
poincare-between a a1 x )∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x ))
using ‹¬ poincare-ray-meets-line a a1 x1 x2 ›
unfolding poincare-on-line-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iﬀ[of - x1 x2 ] poincare-between-rev∗(2, 3 )
by auto
moreover
have¬ (∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a2 ∨
poincare-between a a2 x )∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x ))
using ‹¬ poincare-ray-meets-line a a2 x1 x2 ›
unfolding poincare-on-line-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iﬀ[of - x1 x2 ] poincare-between-rev∗(2, 3 )
by auto
moreover
have¬ (poincare-between a a1 a2 ∨ poincare-between a1 a a2 ∨ poincare-between a1 a2 a )
using ‹¬ poincare-on-line a a1 a2 › poincare-collinear3-iﬀ[of a a1 a2 ]
using∗(1 )∗∗(1−2 )
unfolding poincare-on-line-def
172
by simp
moreover
have (∀ a ′∈{z. z∈ unit-disc}.
a⁄= a1∧
a⁄= a2∧
a ′⁄= a∧
(∃ x∈{z. z∈ unit-disc}.
poincare-between a1 x a2 ∧
x⁄= a1∧
x⁄= a2∧
(poincare-between a a ′ x∨
poincare-between a x a ′))−→
(∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a ′∨
poincare-between a a ′ x)∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x )))
using∗∗(6 )
unfolding poincare-on-line-def poincare-in-angle-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iﬀ[of - x1 x2 ] poincare-between-rev∗(2, 3 )
by auto
ultimately
show∃ a1∈{z. z∈ unit-disc}.
∃ a2∈{z. z∈ unit-disc}.
¬ (poincare-between a a1 a2 ∨ poincare-between a1 a a2 ∨ poincare-between a1 a2 a )∧
¬ (∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a1 ∨
poincare-between a a1 x )∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x ))∧
¬ (∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a2 ∨
poincare-between a a2 x )∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x ))∧
(∀ a ′∈{z. z∈ unit-disc}.
a⁄= a1∧
a⁄= a2∧
a ′⁄= a∧
(∃ x∈{z. z∈ unit-disc}.
poincare-between a1 x a2 ∧
x⁄= a1∧
x⁄= a2∧
(poincare-between a a ′ x∨
poincare-between a x a ′))−→
(∃ x∈{z. z∈ unit-disc}.
(poincare-between a x a ′∨
poincare-between a a ′ x)∧
(poincare-between x x1 x2 ∨
poincare-between x1 x x2 ∨
poincare-between x1 x2 x )))
using∗∗(1, 2 )
by auto
qed
qed
interpretation PoincareElementaryTarskiHyperbolic: ElementaryTarskiHyperbolic p-congruent p-between
proof
12. Continuity
ﬁx ϕ ψ
assume∃ a.∀ x.∀ y. ϕx∧ ψ y−→ p-between a x y
thus∃ b.∀ x.∀ y. ϕx∧ ψ y−→ p-between x b y
173
apply transfer
using continuity
by auto
qed
end
174
References
[1] R. Coghetto. Klein-Beltrami Model. Part I. Formalized Mathematics, 26(1):21–32, 2018.
[2] R. Coghetto. Klein-Beltrami Model. Part II. Formalized Mathematics, 26(1):33–48, 2018.
[3] N. Lobatschewsky. Geometrische Untersuchungen zur Theorie der Parallellinien , pages 159–223. Springer
Vienna, Vienna, 1985.
[4] T. J. M. Makarios. A Mechanical Veriﬁcation of the Independence of Tarski’s Euclidean Axiom. Master’s
thesis, Victoria University of Wellington, 2012. Master Thesis.
[5] F. Marić and D. Simić. Formalizing Complex Plane Geometry. Annals of Mathematics and Artiﬁcial
Intelligence, 74(3-4):271–308, 2015.
[6] F. Mari and D. Simi. Complex geometry. Archive of Formal Proofs , Dec. 2019. http://isa-afp.org/entries/
Complex_Geometry.html, Formal proof development.
[7] W. Schwabhäuser, W. Szmielew, and A. Tarski. Metamathematische Methoden in der Geometrie . Springer-
Verlag, Berlin, 1983.
[8] H. Schwerdtfeger. Geometry of Complex Numbers: Circle Geometry, Moebius Transformation, Non-
euclidean Geometry. Courier Corporation, 1979.
175
