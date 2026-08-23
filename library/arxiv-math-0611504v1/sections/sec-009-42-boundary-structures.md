---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-009-42-boundary-structures
section_title: "Boundary structures"
section_number: 4.2
pages: 21-22
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
tures by using the notions of section 3. Fix an e-triangulation (T,b ) of F . Following Remark 2.2 and
the deﬁnition of log-branches, we put:
Deﬁnition 4.1. Letz ∈ ZI (T,b )±, ande be a non boundary edge of T . Denote lz(e) the canonical log-
branch of W ±(z)(e), computed from the idealization of Star( e) as in Lemma 2.9 and before Deﬁnition
3.8. For any collection m = {mλ}λ of integers, one for each edge λ inT , the classical Log-I-parameter
of (z,m ) at e is
l(z,m)(e) = lz(e) +
√
−1π(ma +mc −mb −md),
where a, ...,d make Link(e) with a, c opposite and e, a have coherent branching orientations (see
Figure 10). Similarly, for every N > 1 and any other collection n = {nλ}λ of integers, the quantum
Log-I-parameter at e is
l(z,m)(e) +
√
−1πN (ma +mc −mb −md) − ∗b
√
−1π(N + 1)(na +nc −nb −nd).
We call the collections
f = {fe}e = {(l(z,m)(e) − log(W ±(z)(e)))/π
√
−1}e
and
c = {ce}e = {na +nc −nb −nd}e
the ﬂattenings of ( z,m ) and the charge of n respectively, and we denote generically by L any such a
system of classical or quantum ( ±)-Log-I-parameters.
Remark that if z ∈ ZI (T,b, C−) and C has no trivial entries, then the ( −)-Log-I-parameters depend
on W −(z), not on z, because of Proposition 3.9.
Deﬁnition 4.2. The QHFT category is the (2 + 1)-bordism category with objects th e empty set and
any ﬁnite union of the [ ∗F, (T,b, L),φ ], where L is a system of (+)-Log- I-parameters, and morphisms
the 4-uples ( ˜Y, ˜LF,ρ,α ±), where: ρ is a conjugacy class of PSL (2, C)-valued representations of π1( ˜Y \
˜LF );α± are QHFT objects with targets ∂± ˜Y , such that for every [ ∗F, (T,b, L),φ ], the character φ∗(ρ)
22 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
e
b c
da
Figure 10. Notations for Log- I-parameters.
coincides with Θ( W +(z)). We say that ( ˜Y, ˜LF,ρ ) is the support of a QHFT bordism from α− toα+,
and that α± is a QHFT surface.
Given bordisms B and B′ from α− to α+ and α′
− to α′
+, respectively, assume that β+ and β′
− are
subobjects of α+ and α′
− that coincide up to the change of orientation.
Deﬁnition 4.3. The bordism B′′ from α′′
− = α− ∪ (α′
− \β′
−) to α′′
+ = α′
+ ∪ (α+ \β+) obtained by
gluing B and B′ along β+ is called the composition of B followed by B′. We write B′′ = B′ ∗ B.
Examples from hyperbolic geometry . Any topologically tame hyperbolic 3-manifold Y with
hyperbolic holonomy ρ and a tangle LF of singularities makes a QHFT bordism. More speciﬁcally,
any geometrically ﬁnite non compact complete hyperbolic 3-manifold Y deﬁnes a triple (Y ′,L F,ρ ) with
a non empty linkLF , as follows. The manifold Y has a natural compactiﬁcation ¯Y , with Y ∼
= Int( ¯Y ),
which is a “pared” manifold ( ¯Y,P ). Here P is a union of disjoint tori or annuli embedded in the
boundary of ¯Y . The tori correspond to the cusps of Y . Each annulus A of P comes from a couple of
cusps on some boundary component of (a small neighborhood of) t he convex core of Y ; A is ﬁbered
by geodesic arcs. If A is separating the cusps belong to diﬀerent components. Deﬁne Y ′′ as the result
of attaching a 2-handle to ¯Y at each annulus A, so that P is contained in the interior of Y ′′ and is
transverse to ∂Y ′′. Equivalently, Y ′′ contains a properly embedded framed 1-tangle L′
F made by the
cocores of the 2-handles, the framing being determined by the ﬁbr ation by intervals of the annuli of
P . Let us choose a framing at each torus of P . By Dehn ﬁlling we get a manifold Y ′, and Y ′′ is the
exterior in Y ′ of the union L′′
F of the framed cores of the ﬁlling solid tori. Hence, if every boundary
component of the convex core of Y contains at least one cusp, associated to Y and the cusp framings
we have ( Y ′,L F,ρ ), where LF = L′
F ∪L′′
F intersects all the boundary components of Y ′, and ρ is
a PSL (2, C)-character of Y ′ \LF ∼
= Y . If furthermore ρ is the holonomy of a complete hyperbolic
metric on Y andY has inﬁnite volume ends, then ∂Y ′ is non empty. We can give the triple ( Y ′,L F,ρ )
a natural boundary structure α− ∪α+, induced by exponential I-parameters of the pleated surfaces
in the boundary of the convex core (see eg. [14]).
