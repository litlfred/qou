---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-010-3-the-extended-bloch-group
section_title: "The extended Bloch group"
section_number: 3
pages: 11-12
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
We use the conventions of Zickert [ 29]; the original reference is Neumann [ 20].
Deﬁnition 3.1. The pre-Bloch group P(C) is the free abelian group on C \ {0, 1} modulo the ﬁve
term relation
(3.1) x − y + y
x − 1 − x−1
1 − y−1 + 1 − x
1 − y = 0, for x ⁄= y ∈ C \ {0, 1}.
The Bloch group is the kernel of the map ν : P(C) → ∧ 2(C∗) taking z to z ∧ (1 − z).
12 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Deﬁnition 3.2. The extended pre-Bloch group ˆP(C) is the free abelian group on the set
(3.2) ˆC =
{
(e, f) ∈ C2⏐⏐ exp(e) + exp(f ) = 1
}
modulo the lifted ﬁve term relation
(3.3) (e0, f0) − (e1, f1) + (e2, f2) − (e3, f3) + (e4, f4) = 0
if the equations
(3.4)
e2 = e1 − e0, e 3 = e1 − e0 − f1 + f0, f 3 = f2 − f1
e4 = f0 − f1, f 4 = f2 − f1 + e0
are satisﬁed. The extended Bloch group is the kernel of the map ˆν : ˆP(C) → ∧ 2(C) taking (e, f) to
e ∧ f .
An element (e, f) ∈ˆC with exp(e) = z is called a ﬂattening with cross-ratio z. Letting µC denote
the roots of unity in C∗, we have a commutative diagram.
(3.5)
0
/d15/d15
0
/d15/d15
0
/d15/d15
0 /d47/d47 µC
2 log /d47/d47
χ
/d15/d15
C/4πiZ /d47/d47
χ
/d15/d15
C∗/µC /d47/d47
/d15/d15
0
/d15/d15
0 /d47/d47 ˆB(C) /d47/d47
π
/d15/d15
ˆP(C) ˆν /d47/d47
π
/d15/d15
∧2(C) /d47/d47
/d15/d15
K2(C) /d47/d47 0
0 /d47/d47 B(C) /d47/d47
/d15/d15
P(C) ν /d47/d47
/d15/d15
∧2(C∗)
/d15/d15
/d47/d47 K2(C) /d47/d47
/d15/d15
0
0 0 0 0
The map π is induced by the map taking a ﬂattening to its cross-ratio, a nd χ is the map taking
e ∈ C/4πiZ to (e, f + 2πi) − (e, f), where f ∈ C is any element such that (e, f) ∈ˆC.
