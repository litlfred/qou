---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-066-interpretation-of-locales
section_title: "Interpretation of locales"
section_number: null
pages: 170-175
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
global-interpretation PoincareTarskiAbsolute: TarskiAbsolute where cong = p-congruent and betw = p-between
defines p-on-line = Poincare TarskiAbsolute.on-line and
p-on-ray = Poincare TarskiAbsolute.on-ray and
p-in-angle = PoincareTarskiAbsolute.in-angle and
p-ray-meets-line = Poincare TarskiAbsolute.ray-meets-line
proof—
show TarskiAbsolute p-congruent p-between
proof

1. Reflexivity of congruence

fix ry
show p-congruent © y y ©
unfolding p-congruent-def
by transfer (simp add: poincare-distance-sym)
next

2. Transitivity of congruence

fix ryzuvw
show p-congruent zy zu A p-congruent x y v w —+ p-congruent zu vw
by (transfer, simp)
next

3. Identity of congruence

fix cry z
show p-congruent ty zz—> x= y
unfolding p-congruent-def
by transfer (simp add: poincare-distance-eq-0-iff)
next

4. Segment construction

170
fix ryab
show 4 z. p-between x y z A p-congruent y za b
using segment-construction
unfolding p-congruent-def
by transfer (simp, blast)
next

5. Five segment

fix cyza' yz’ uu’

show x # y A p-between x y z A p-between x’ y’ z' A
p-congruent x y x’ y' A p-congruent y zy’ z' A
p-congruent 2 ux’ u' A p-congruent y uy! u’ —
p-congruent zu z'u’
unfolding p-congruent-def
apply transfer
using five-segment-axiom
by meson

next

6. Identity of betweeness

fix ry
show p-between ryt —-> r=y
by transfer (simp add: poincare-between-sum-distances poincare-distance-eq-0-iff poincare-distance-sym)
next

7. Pasch

fix ryzuv
show p-between x u z A p-between y v z —> (A a. p-between ua y A p-between x a v)
apply transfer
using Pasch
by blast
next

8. Lower dimension

show J a. 4 6.4 c. 7 p-between a b c A 7 p-between b c a A 7 p-between c a b
apply (transfer)
using lower-dimension-axiom
by simp
next

9. Upper dimension

fix ryzuv
show p-congruent «ux v A p-congruent y uy uv A p-congruent zuzvu A u#v—
p-between x y z V p-between y zx V p-between zx y
unfolding p-congruent-def
by (transfer, simp add: upper-dimension-axiom)
qed
qed

interpretation Poincare TarskiHyperbolic: TarskiHyperbolic
where cong = p-congruent and betw = p-between
proof

10. Euclid negation

show 5 abc dt. p-betweenadt A p-betweenbdc\a#dA
(V « y. p-between a b x A p-between a c y —+ 7 p-between x t y)
using negated-euclidean-ariom
by transfer (auto, blast)
next
fix aal «2
assume 7 TarskiAbsolute.on-line p-between a x1 «2
hence — p-on-line a x1 £2
using TarskiAbsolute.on-line-def|OF Poincare TarskiAbsolute. TarskiAbsolute-arioms

171
using Poincare TarskiAbsolute.on-line-def
by simp

11. Limiting parallels

thus dal a2.
— TarskiAbsolute.on-line p-between a al a2 A
— TarskiAbsolute.ray-meets-line p-between a al «1 x2 A
— TarskiAbsolute.ray-meets-line p-between a a2 «1 x2 A
(Va'. TarskiAbsolute.in-angle p-between a’ al a a2 —+ TarskiAbsolute.ray-meets-line p-between a a’ x1 x2)
unfolding TarskiAbsolute.in-angle-def[OF Poincare TarskiAbsolute. TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-ray-def|OF Poincare TarskiAbsolute. TarskiAbsolute-axioms]
unfolding TarskiAbsolute.ray-meets-line-def|OF Poincare TarskiAbsolute. TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-ray-def|OF Poincare TarskiAbsolute. TarskiAbsolute-axioms]
unfolding TarskiAbsolute.on-line-def[OF Poincare TarskiAbsolute. TarskiAbsolute-axioms|
unfolding Poincare TarskiAbsolute.on-line-def
apply transfer
proof—
fix a x1 x2
assume *: a € unit-disc x1 € unit-disc 72 € unit-disc
7 (poincare-between a x1 x2 V poincare-between x1 a 22 V poincare-between t1 x2 a)
hence — poincare-on-line a x1 «2
using poincare-collinear3-iff [of a x1 x2]
using poincare-between-rev poincare-on-line-def by blast
hence 5 al €unit-disc.
da2€unit-disc.
— poincare-on-line a al a2 A
— poincare-ray-meets-line a al x1 72 \
— poincare-ray-meets-line a a2 x1 «2 A
(V a'Eunit-disc.
poincare-in-angle a' al a a2 —+
poincare-ray-meets-line a a’ x1 x2)
using limiting-parallels[of a x1 x2] *
by blast
then obtain al a2 where **: al €unit-disc a2€unit-disc — poincare-on-line a al a2
— poincare-ray-meets-line a a2 x1 42
7 poincare-ray-meets-line a al x1 42
V a’Eunit-disc.
poincare-in-angle a’ al a a2 —+
poincare-ray-meets-line a a’ x1 x2
by blast
have 7 (Ax€{z. z € unit-disc}.
(poincare-between a x al V
poincare-between a al x) A
(poincare-between x x1 42 V
poincare-between x1 x x2 V
poincare-between x1 x2 x))
using (— poincare-ray-meets-line a al «1 «2»
unfolding poincare-on-line-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iff [of - x1 x2] poincare-between-rev *(2, 3)
by auto
moreover
have 7 (Ax€{z. z € unit-disc}.
(poincare-between a x a2 V
poincare-between a a2 x) \
(poincare-between x x1 42 V
poincare-between x1 x x2 V
poincare-between x1 x2 x))
using (— poincare-ray-meets-line a a2 «1 x2»
unfolding poincare-on-line-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iff [of - x1 x2] poincare-between-rev *(2, 3)
by auto
moreover
have 7- (poincare-between a al a2 V poincare-between al a a2 V poincare-between al a2 a)
using ‘~ poincare-on-line a a1 a2) poincare-collinear3-iff [of a al a2]
using *(1) **(1—2)
unfolding poincare-on-line-def

172
by simp
moreover
have (V a'E{z. z € unit-disc}.
a#ali
a#a2A
a’ #an
(Are{z. z € unit-disc}.
poincare-between al z a2 A
cA#al A
x # aA
(poincare-between a a' x V
poincare-between a x a’)) —+
(Are{z. z € unit-disc}.
(poincare-between a x a’ V
poincare-between aa’ x) A
(poincare-between x x1 x2 V
poincare-between x1 x x2 V
poincare-between x1 x2 x)))
using **(6)
unfolding poincare-on-line-def poincare-in-angle-def poincare-ray-meets-line-def poincare-on-ray-def
using poincare-collinear3-iff [of - x1 x2] poincare-between-rev *(2, 3)
by auto
ultimately
show Jale{z. z € unit-disc}.
Fa2e{z. z € unit-disc}.
w— (poincare-between a al a2 V poincare-between al a a2 V poincare-between al a2 a)
a (Axe{z. z © unit-disc}.
(poincare-between a x al V
poincare-between a al x) A
(poincare-between x x1 42 V
poincare-between x1 x x2 V
poincare-between x1 x2 x)) A
a (Axe{z. z © unit-disc}.
(poincare-between a x a2 V
poincare-between a a2 x) \
(poincare-between x x1 42 V
poincare-between x1 x x2 V
poincare-between x1 x2 x)) A
(Va'e{z. z € unit-disc}.
a#ali
a#a2A
a’ #an
(Are{z. z € unit-disc}.
poincare-between al z a2 A
cA#al A
x # aA
(poincare-between a a' x V
poincare-between a x a’)) —+
(Are{z. z € unit-disc}.
(poincare-between a x a’ V
poincare-between aa’ x) A
(poincare-between x x1 x2 V
poincare-between x1 x x2 V
poincare-between x1 x2 x)))
using **(1, 2)
by auto
qed
qed

interpretation PoincareElementaryTarskiHyperbolic: ElementaryTarskiHyperbolic p-congruent p-between
proof

12. Continuity
fix pv
assume J a.V zc. V y. px Aw y —> p-betweena xy
thus 4 b.V2.V yprAwd y — p-between x by

173
apply transfer
using continuity
by auto

qed

end

174
References

{1] R. Coghetto. Klein-Beltrami Model. Part I. Formalized Mathematics, 26(1):21-32, 2018.
[2] R. Coghetto. Klein-Beltrami Model. Part II. Formalized Mathematics, 26(1):33-48, 2018.

[3] N. Lobatschewsky. Geometrische Untersuchungen zur Theorie der Parallellinien, pages 159-223. Springer
Vienna, Vienna, 1985.

[4] T. J. M. Makarios. A Mechanical Verification of the Independence of Tarski’s Euclidean Axiom. Master’s
thesis, Victoria University of Wellington, 2012. Master Thesis.

[5] F. Marié and D. Simi¢. Formalizing Complex Plane Geometry. Annals of Mathematics and Artificial
Intelligence, 74(3-4):271-308, 2015.

{6] F. Mari and D. Simi. Complex geometry. Archive of Formal Proofs, Dec. 2019. http://isa-afp.org/entries/
Complex_Geometry.html, Formal proof development.

[7] W. Schwabhauser, W. Szmielew, and A. Tarski. Metamathematische Methoden in der Geometrie. Springer-
Verlag, Berlin, 1983.

{8] H. Schwerdtfeger. Geometry of Complex Numbers: Circle Geometry, Moebius Transformation, Non-
euclidean Geometry. Courier Corporation, 1979.

175
