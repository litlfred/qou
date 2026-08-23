---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-003-12-the-ring-ˆzq-of-analytic-functions-on-the-set
section_title: "The ring ˆZ[q] of analytic functions on the set of roots of unity. The"
section_number: 1.2
pages: 2-3
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
invariantJM of an integral homology sphere M which we construct in the paper
takes values in a completion ˆZ[q] of the polynomial ring Z[q], which was introduced
in [17] and studied in [18]. One of the simplest deﬁnitions of ˆZ[q] is
ˆZ[q] = lim←−nZ[q]/((q)n),
where we set
(q)n = (1−q)(1−q2)··· (1−qn).
The ring ˆZ[q] may be regarded as the ring of “analytic functions deﬁned on the
setZ of roots of unity”. This statement is justiﬁed by the followi ng facts. (The
following overlaps those in [17, 18].)
First of all, each element of ˆZ[q] can be evaluated at each root of unity . That
is, for each ζ∈Z , the evaluation map ev ζ : Z[q]→ Z[ζ], f (q)↦→f (ζ), induces a
(surjective) ring homomorphism
evζ : ˆZ[q]→ Z[ζ],
since ev ζ((q)n) = 0 if n≥ ord(ζ). It is often useful to write f (ζ) = ev ζ(f (q)) for
f (q)∈ ˆZ[q].
Second, each element of ˆZ[q] can be regarded as a (set-theoretic) function on the
set of roots of unity. This means that each f∈ ˆZ[q] is determined uniquely by the
values ev ζ(f )∈ Z[ζ] for all ζ∈Z , or, equivalently, the function
evZ : ˆZ[q]→
∏
ζ∈Z
Z[ζ], f (q)↦→(f (ζ))ζ∈Z.(1.1)
is injective [18, Theorem 6.3]. Here, in a natural way, ∏
ζ∈Z Z[ζ] can be regarded
as a subring of the ring of C-valued functions on Z.
Third, each element of ˆZ[q] has a power series expansion in q−ζ for each root
of unity, and any such power series determines ˆZ[q]. In fact, for each ζ∈Z , the
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 3
inclusion Z[q]⊂ Z[ζ][q] induces a ring homomorphism
ιζ : ˆZ[q]→ Z[ζ][[q−ζ]],(1.2)
since, for each i≥ 0, (q)n is divisible by ( q−ζ)i in Z[ζ][q] if n≥ i ord(ζ). Since
ιζ is injective [18, Theorem 5.2], each f∈ ˆZ[q] is determined by the power series
ιζ(f ). ιζ (f ) may be regarded as the Taylor expansion of f , see Section 12.3.1.
Fourth, each element of ˆZ[q] is completely determined by its values on a subset
Z ′⊂Z ifZ ′ has a limit point. Otherwise, not completely. To explain what this
means, we introduce a topology on the set Z, which is diﬀerent from the usual one
induced by the topology of C. Two elements ζ,ξ ∈Z are said to be adjacent ifζξ −1
is of prime power order, or, equivalently, if ζ−ξ is not a unit in Z[ζ,ξ ]. A subset
Z ′⊂Z is deﬁned to be open if, for each ζ∈Z ′, all but ﬁnitely many elements
adjacent to ζ is contained inZ ′. In this topology, an element ξ∈Z is a limit point
of a subset Z ′⊂Z (i.e., (U\{ξ})∩Z ′⁄=∅ for all neighborhood U ofξ) if and only
if there are inﬁnitely many ζ∈Z ′ adjacent to ξ. We have the following.
Proposition 1.1 ([18, Theorem 6.3]) . IfZ ′⊂Z has a limit point, then the ring
homomorphism
evZ ′ : ˆZ[q]→
∏
ζ∈Z ′
Z[ζ], f (q)↦→(f (ζ))ζ∈Z,(1.3)
is injective.
IfZ ′⊂Z has no limit point, then ev Z ′ is not injective, i.e., there is a non-zero
“analytic function” f∈ ˆZ[q] vanishing on Z ′, see Proposition 12.2.
The above-explained properties of ˆZ[q] are closely related to the integrality of
ˆZ[q]. In fact, the completion ˆQ[q] = lim←−nQ[q]/((q)n) does not behave like ˆZ[q], see
[18, Section 7.5].
