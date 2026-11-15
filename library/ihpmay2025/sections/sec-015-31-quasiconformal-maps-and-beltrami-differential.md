---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-015-31-quasiconformal-maps-and-beltrami-differential
section_title: "Quasiconformal maps and Beltrami differentials"
section_number: 3.1
pages: 21-22
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
We begin with a brief survey of the theory of quasiconformal maps (without proof). Roughly,
quasiconformal maps are orientation preserving homeomorphisms which distort the conformal
structure by a bounded amount. One may view them as the conformal analogue of bilipschitz
maps, which distort the metric structure a bounded amount. Good references for the theory
of quasiconformal maps are the books of Lehto-Virtanen [48] and Lehto [47]. This section is
plagiarized from the research monograph of Canary-McCullough [30].
Given a function f : D →C defined on a domain D in C, we may write it as f(x, y) =
u(x, y) + iv(x, y). We say f is ACL (absolutely continuous on lines) if given any rectangle
R = [a, b]×[c, d] in D both u and v are absolutely continuous restricted to almost every vertical
and almost every horizontal line segment in R. If f is ACL then the partial derivatives of u
and v exist almost everywhere and we define fx = ux + ivx and fy = uy + ivy. Then, we let
fz = 1
2(fx −ify) and f¯z = 1
2(fx + ify). (Recall that the Cauchy-Riemann equations assert
that if f is analytic then f¯z = 0 for all z ∈D.) We define the Beltrami differential of f to be
µf = f¯z
fz
Notice that if f is differentiable at a point z and Jf(z) is its Jacobian, then the image
of the unit circle (in the tangent space Tz(D)) under Jf(z) is an ellipse, the ratio of the lengths
of the axes is given by K(z) = 1 + |µf(z)|
1 −|µf(z)| and the angle that the preimage of the (longer) axis
makes with the x-axis is 1
2 arg(µf(z)).
One says that an orientation-preserving homeomorphism f : D →D′ is K-quasiconformal if
f is ACL and |µf| ≤K−1
K+1 almost everywhere. This says that, typically, very small circles are
taken to curves very much like ellipses with eccentricity at most K. One way of formalizing
this is by defining
H(z) = lim sup
r→0
maxθ |f(z + reiθ) −f(z)|
minθ |f(z + reiθ) −f(z)| .
An orientation-preserving homeomorphism f : D →C ∪{∞} is K-quasiconformal if and only
if H is bounded on D −{∞, f−1(∞)} and H(z) ≤K almost everywhere in D (see pages 177
and 178 in Lehto [47]). If one uses the spherical metric on C, then one need not exclude ∞and
f−1(∞) from consideration.
One may check that the composition of a K1-quasiconformal map and a K2-quasiconformal
map is a K1K2-quasiconformal map. Another useful fact is:
Proposition 3.1. (Lehto-Virtanen [48, Thm. 1.5.1]) A quasiconformal map is conformal if and
only if it is 1-quasiconformal.
The most fundamental result concerning quasiconformal maps is the Measurable Riemann
Mapping Theorem (see Ahlfors-Bers [5] or Lehto [47]) which asserts that the Beltrami differential
22
RICHARD D. CANARY
determines the quasiconformal map (up to normalization) and that every Beltrami differential
(of norm less than 1) determines a quasiconformal map.
Measurable Riemann Mapping Theorem: Suppose that µ ∈L∞(C, C) and ||µ||∞< 1. Then
there exists a unique quasiconformal map ϕµ : C →C whose Beltrami differential is µ and such
that ϕµ fixes 0, 1, and ∞. Moreover, ϕµ depends analytically on µ.
Notice that one may combine the Measurable Riemann Mapping Theorem and the traditional
Riemann Mapping Theorem to observe that the same result holds for the upper half-plane H2.
This version of the result is used in traditional Teichm¨uller theory and also plays a role in our
proof of the Quasiconformal Parameterization Theorem.
Measurable Riemann Mapping Theorem (Disk version): Suppose that µ ∈L∞(H2, C) and
||µ∞|| < 1.
Then there exists a unique quasiconformal map ϕµ : H2 →H2 whose Beltrami
differential is µ and such that ϕµ fixes i, 2i, and 3i. Moreover, ϕµ depends analytically on µ.
An alternative characterization of quasiconformal mappings of C is obtained by considering
bilipschitz homeomorphisms of H3. The Fellow Traveller property may be used to show that any
bilipschitz homeomorphism of H3 to itself extends continuously to a homeomorphism of ∂H3 to
itself. One must work a little harder (although not too much harder) to show that this extension
is quasiconformal. (I like how this is written up in Thurston’s notes [75], but one may find this
argument many places.) It is a deeper fact that any quasiconformal automorphism of ∂H3
extends to a bilipschitz map of H3. (One place to read an exposition is in Matsuzaki-Taniguchi
[55, Thm 5.3.1].)
Proposition 3.2. Let ϕ: C →C be an orientation-preserving homeomorphism. Then ϕ is quasi-
conformal if and only if it extends to a homeomorphism Φ: H3 ∪C →H3 ∪C whose restriction
to H3 is bilipschitz (with respect to the hyperbolic metric).
Notice that one can show that a bilipschitz map extends to a well-defined map of the boundary
using only the Fellow Traveller Property. One must work a little harder (although not too much
harder) to show that this extension is quasiconformal.
The fact that quasiconformal maps
extend to bilipschitz maps is a deeper fact.
It will also be useful to know that quasiconformal homeomorphisms take sets of measure zero
to sets of measure zero (see [48]).
Theorem 3.3. If f : C ∪{∞} →C ∪{∞} is a quasiconformal map and E ⊂C has measure
zero, then f(E) has measure zero.
