---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-019-remarks-on-wilson-loops
section_title: "Remarks on Wilson Loops"
section_number: null
pages: 24-25
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
In the previous subsections, we have studied partition functions of the chiral Yang-Mills theory.
We have shown that in the absence of boundaries, the partition functions are reproduced
by a deformed Gromov-Witten theory of the target space. Furthermore, we have argued
that boundaries with prescribed holonomies may be thought of as operator insertions, and
that their correlation functions match the corresponding Gromov-Witten correlators. In this
subsection, we study correlators of Wilson lines in chiral Yang-Mills theory. As an opening
remark, we observe that the expectation value of a Wilson loop depends on the area it encloses.
Therefore, the area deformation of the Gromov-Witten theory of the target space must be
patch-dependent: we view the parameter t as an operator which associates its area to the
patch under consideration.
Wilson lines on a manifold of genus G and area t are computed by gluing manifolds of
genus G and zero, with respective area t1 and t2 = t−t1, along a boundary with an extra
character insertion:
⟨sµ⟩G =
Z
dUZ +
G,t1(U)sµ(U)Z+
0,t2(U−1). (5.28)
As we explained in section 2.3, one should think of the functions Z+
G,t1(U) and Z+
0,t2(U−1)
as Gromov-Witten invariants relative to the boundary with prescribed holonomy U. If we
rewrite such Wilson line expectation values in terms of symmetric group quantities, we find:
⟨sµ⟩G = dµ
d!
X
d1,d2
gd1(2G−1)
s g−d2
s e−t1d1+t2d2
2
X
λ⊢d1
ρ⊢d2
dλ
d1!
2−2Gdρ
d2!
2
Ωgs(λ)1−2G
Ωgs(ρ) e−gs(t1f2(λ)+t2f2(ρ))
X
α⊢d1
β⊢d
zα∪βfα(λ)fβ(µ)fα∪β(ρ)δd1+d,d2, (5.29)
23
where µ is a partition of d and α∪β denotes the concatenation of the conjugacy classes α
and β. This expression may be simplified to render the gluing method more manifest on the
symmetric group side of the equation:
⟨sµ⟩G =
 
e−t2
2
gs
!d
X
β⊢d
χµ(β)
 X
d1
gd1(2G−2)
s e−td1
2
X
α⊢d1
zα∪β
zβ
⟨Cα⟩t1,u
d1,G⟨Cα∪β⟩t2,u
d+d1,0
!
. (5.30)
Equation (5.30) provides a generic gluing prescription for how to incorporate a Wilson line
in the Hurwitz formulation of the Yang-Mills theory. This prescription involves a sum over
a basis of intermediate states corresponding to conjugacy classes. A direct string theoretic
interpretation of the gluing procedure would be interesting. In particular, it would be neat to
interpret the Wilson lines as an extended object in the dual string theory.
