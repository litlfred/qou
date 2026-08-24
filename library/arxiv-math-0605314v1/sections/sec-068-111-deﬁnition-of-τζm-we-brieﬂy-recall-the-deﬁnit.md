---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-068-111-deﬁnition-of-τζm-we-brieﬂy-recall-the-deﬁnit
section_title: "Deﬁnition of τζ(M ). We brieﬂy recall the deﬁnition of the sl2 WRT invari-"
section_number: 11.1
pages: 36-37
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
antτζ(M ) of a closed 3-manifold M at ζ∈Z . For the details, see [73, 38].
If ζ = 1, then we set τζ(M ) = 1 for any closed 3-manifold M .
Let r≥ 2 and let ζ1/4 be a primitive 4 rth root of unity. Thus ζ is a primitive
rth root of unity. (The following construction depends not on ly on ζ but also ζ1/2
or ζ1/4, but we suppress them from the notation. For integral homolo gy spheres,
τζ(M ) depends only on ζ and M , not on ζ1/4.)
Let
Ar = Z[q1/4,q −1/4](Φ 4r (q1/ 4)),
denote the localization of the ring Z[q1/4,q −1/4] by the principal ideal generated
by the 4rth cyclotomic polynomial Φ 4r(q1/4) in q1/4 (which is equal to Φ 2r(q1/2)).
We have
Ar =
{ f (q1/4)
g(q1/4)∈ Q(q1/4)
⏐
⏐
⏐f (q1/4),g (q1/4)∈ Z[q1/4], g(ζ1/4)⁄= 0
}
.
We extend ev ζ : Z[q,q −1]→ Z[ζ] to the Q-algebra homomorphism
evζ : Ar→ Q(ζ1/4)
deﬁned by ev ζ(f (q1/4)) = f (ζ1/4).
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 37
Set
Ω r =
r−2∑
i=0
[i + 1]Vi∈R Z[v,v−1].
LetL be an m-component link in S3. Set
Ir(L) = JL(Ω r,... , Ω r)∈ Z[q1/4,q −1/4],
Iζ (L) = ev ζ (Ir(L))∈ Z[ζ1/4,ζ −1/4].
For an unknot U± of framing±1, we have Iζ (U±)⁄= 0. Set
τζ (L) = Iζ (L)
Iζ (U+)σ+(L)Iζ (U−)σ−(L)∈ Q(ζ1/4),(11.2)
where U± denotes an unknot with framing ±1, and σ+(L) (resp. σ−(L)) denotes
the number of positive (resp. negative) eigenvalues of the l inking matrix of L. It
is known that τζ(L) is invariant under Kirby moves, i.e., stabilization and ha ndle
slides. Hence, by setting τζ (M ) = τζ(L) for a 3-manifold M with S3
L∼
= M , we
obtain a 3-manifold invariant τζ (M ).
