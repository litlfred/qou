---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-033-5-the-period-map-the-period-map-determines-an-em
section_title: "The period map. The period map determines an embedding"
section_number: 5
pages: 39-40
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
fq : M∗
0, 3 → (H2, 0 ∼
= P1)/S4
whose image omits just one point. The domain is the (2 , 3, ∞) orbifold
and the target is the (2 , 3, 4) orbifold; and fq sends the cusp to the cone
point of order 4. These facts can be veriﬁed by showing the met ric comple-
tion of M0, 4 in the induced spherical metric is an orbifold; or by explici tly
computing the period map, using the elliptic forms above.
Remark: Shimura–T eichm¨ uller curves. Equation (8.2) determines a
remarkable curveV ⊂ M 3 (parameterized by b). M¨ oller showsV is the only
subvariety of any moduli space Mg, g ≥ 2 which is both a Shimura curve
and a Teichm¨ uller curve [Mo].
Irregular covers of elliptic curves. The preceding example was partic-
ularly simple because the maps pi :X →A were Galois coverings. To give
the ﬂavor of a more typical example, we describe a map p : X → A in the
case (n,d ) = (3, 6).
In this case X is a genus 4 curve, presented as a covering of ˆC branched
over 4 points. We can change the x-coordinate by a M¨ obius transformation
so the deﬁning equation for X becomes
X : y6 = (x3 − 3x −b)(x − 2)3
for some b ∈ C (because the cross-ratio of the roots of the polynomial on th e
right takes on all possible values). Now consider the ellipt ic curve deﬁned
by
A : z6 = (b − 2)4w(w − 1)3.
Because of its order 6 symmetry S(w,z ) = (w,ζ 6z), we have A ∼
= C/Z[ζ3];
and the formula
(w,z ) =
( x3 − 3x −b
2 −b ,y (x + 1)
)
(8.3)
38
deﬁnes an irregular, degree 3 map p :X →A. This map shows A occurs as
one of the rigid factors of Jac( X).
This calculation is motivated by the observation that the de sired map
p :X →A induces a map
p :X/⟨T ⟩ →A/⟨S⟩
between a pair of orbifolds with signatures (2 , 6, 6, 6) and (2 , 3, 6) respec-
tively. Since both orbifolds have genus zero, we can regard p as a rational
map of the form w =p(x). The signatures of these orbifolds suggest there
exists such a map with deg( p) = 3, sending the 3 points of order 6 in the
domain to the unique point of order 6 in the range. Any such map would be
totally ramiﬁed over the singular point of order 3, so in suit able coordinates
it would be a cubic polynomial; and we are led to formula (8.3) .
Remark. In the case ( n,d ) = (3 , 10), the projection to the rigid fac-
tor Jac(X) → A ∼
= C2/Z[ζ5] is not induced by a map p : X → Y with
Jac(Y ) ∼
=A. This can be established by showing there is no map from the
(10, 10, 10, 10) orbifold to the (2 , 5, 10) orbifold which lifts to the required
Z/10 covering spaces. (It is, however, induced by a correspond ence.)
