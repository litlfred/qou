---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-013-33-chevalley-eilenberg-complex
section_title: "Chevalley-Eilenberg complex"
section_number: 3.3
pages: 14-15
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Suppose that h is a Lie algebra. Chevalley-Eilenberg complex CEh is the complex (V•(h), d) with Vp(h) =
U(h) ⊗C Λph and diﬀerential dce = d1 + d2 where:
d1(u ⊗x1 ∧· · · ∧xp) =
p
X
i=1
(−1)i+1uxi ⊗x1 ∧· · · ∧ˆxi ∧· · · ∧xp,
d2(u ⊗x1 ∧· · · ∧xp) =
X
i<j
(−1)i+ju ⊗[xi, xj] ∧x1 ∧· · · ∧ˆxi ∧· · · ∧ˆxj ∧· · · ∧xp,
For h module V we deﬁne CEh(V ) := HomU(h)(CEh, V ). The homology of this complex is called Chevalley-
Eilenberg cohomology of V : H∗
Lie(h, V ). Consider a group H such that Lie(H) = h, Z is an aﬃne variety with
H-action and H-invariant function F. Suppose we are given F ∈MFh(Z, F), that is, we have a Z2-graded
C[Z] module M with diﬀerential D such that D2 = F · Id and D(h · m) = h · D(m) for any h ∈H. The
complex HomU(h)(CEh, M) is a Z × Z2-graded module and we collapse the ﬁrst Z-grading to Z2-grading.
The map D + dce respects Z2-grading and the direct computation shows that D and dce anti-commute.
Hence (D + dce)2 = F and we deﬁne CEh(F) := (HomUh(CEh, M), D + dce). The diﬀerential dce commutes
with the elements of the ring invariants C[Z]h, thus the complex CEh(F) ∈MF(Z/H, F) where Z/H =
Spec(C[Z]h).
14
