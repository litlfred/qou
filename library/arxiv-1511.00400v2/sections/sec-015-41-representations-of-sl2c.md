---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-015-41-representations-of-sl2c
section_title: "Representations of SL2(C)"
section_number: 4.1
pages: 26-27
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Let Vk+1 be the space of degree k homogeneous polynomials in two variables:
Vk+1 ∶= {P ∈C[X, Y ] /divid⟩s.alt0 P is homogeneous of degree k}.
The group SL 2(C) acts naturally on Vk+1 by precomposition on polynomials:
SL2(C) × Vk+1 → Vk+1
(A, P) ↦ P ○ At
We consider the transpose matrix At so that the action is on the left. We
could also have considered the inverse instead of the transpose, a s there exist a
matrix B ∈SL2(C) such that A−1 = BAtB−1 for every A ∈SL2(C). This deﬁnes
a representation
Symk∶ SL2(C) → SLk+1(C).
Not only Sym k has determinant 1, but preserves a non-degenerate bilinear form
that is symmetric for k even, and skew-symmetric for k odd. So
Symk∶ SL2(C) → /brac⟩l⟩ft.alt4 SO(2l + 1, C) for k = 2l
Sp(2l + 2, C) for k = 2l + 1
For k = 1, Sym is the standard representation and the bilinear form is the
determinant of the 2 × 2 matrix obtained from two vectors. Then the form
invariant for Sym k is the k-th symmetric product of this determinant.
We shall also consider the complex conjugate Symk, which is antiholomor-
phic.
Proposition 4.1. Classiﬁcation of irreducible representations of SL2(C), cf. [8].
(a) Any irreducible holomorphic representation of SL2(C) is equivalent to Symk
for a unique k ≥0.
(b) Any irreducible representation of SL2(C) is equivalent to
Symk1,k2 ∶= Symk1 ⊗
Symk2
for a unique pair of integers k1, k2 ≥0.
Notice that Sym k = Symk,0 and that Sym 0 = Sym0,0 is the trivial represen-
tation in C. The adjoint representation Ad ∶ SL2(C) → SO(sl2(C)) is equivalent
to Sym 2, the invariant form being the Killing form.
The representation Sym k,k takes values in SL (k+1)2 (R). More precisely, the
image of Sym k,k is contained in SO (p, q), with
p = k2 + 3k + 2
2 and q = k2 + k
2 .
26
For instance, Sym 1,1∶ PSL2(C) → SO0(3, 1) is the canonical isomorphism be-
tween diﬀerent presentations of the group of orientation preser ving isometries
of hyperbolic 3-space. This representation is used to study inﬁnite simal defor-
mations of conformally ﬂat structures on a hyperbolic 3-manifold. T he rep-
resentation Sym 2,2∶ PSL2(C) → SO0(6, 3) is used in the study of inﬁnitesimal
deformations of projective structures on a hyperbolic 3-manifold .
Let ̺σ∶ π1M 3 → SL2(C) denote a lift corresponding to a spin structure σ,
we shall denote its composition with Sym k1,k2 by
̺k1,k2
σ ∶= Symk1,k2 ○̺σ, (25)
and ̺k
σ = ̺k,0
σ .
Theorem 4.2 ([84]). Let M 3 be a compact hyperbolic orientable 3-manifold and
/tild⟩comb.alt1hol a lift of its holonomy. If k1 ≠k2 then
H ∗(M 3; ̺k1,k2
σ ) = 0 .
This theorem, due to Raghunathan, is commented in Appendix B, with other
facts about cohomology.
