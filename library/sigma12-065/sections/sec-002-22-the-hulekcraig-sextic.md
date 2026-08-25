---
doc_id: sigma12-065
doc_title: ""
section_id: sec-002-22-the-hulekcraig-sextic
section_title: "The Hulek–Craig sextic"
section_number: 2.2
pages: 3-4
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
Hulek and Craig both introduce the sextic
C(¯x, ¯y, ¯z) := ¯x
(
¯y5 + ¯z5)
+ (¯x¯y¯z)2− ¯x4¯y¯z− 2(¯y¯z)3 = 0. (2.1)
This curve is also of genus 4 and admits A5 as a symmetry group 2. In this case an order five
symmetry is obvious and we may take
ab : (¯x, ¯y, ¯z)↦→
(
ζ2¯x,ζ 4¯y, ¯z
)
,
where ζ = e2πi/5. There is also a corresponding order two symmetry
a :


¯x
¯y
¯z

↦→


1 2 2
1 ζ +ζ−1 ζ2 +ζ−2
1 ζ2 +ζ−2 ζ +ζ−1




¯x
¯y
¯z

.
Together these generate A5 again since aab =: b has order three (hence the slightly unusual
choice of notation for ab above).
In fact the sextic (2.1) is also a model for Bring’s curve using Dye’s result and the following
theorem.
Theorem 1. WithA =


j 1 1
0 −i√2 +j i√2 +j
1 −j −j

 thenD(Ax) =−960(9+4
√
5)C(x) and hence
D(x) = 0 ⇐⇒ C(A−1x) = 0.
This may be directly verified. The choice of the matrix A follows upon consideration of the
conjugacy classes of automorphisms of both models (see [15] for further details).
We observe that the antiholomorphic involution [¯x, ¯y, ¯z]↦→ [¯x∗, ¯y∗, ¯z∗] (where ∗ is complex
conjugation) is a symmetry ofC though it is orientation-reversing and so not a conformal auto-
morphism. This involution endows C with a real structure. The fixed point set of such a real
structure is either empty or the disjoint union of simple closed curves, known as ovals following
Hilbert’s terminology [4]. A classical result of Harnack for a Riemann surface of genus g with
real structure says there are at most g + 1 ovals. We shall show the the HK curve has one oval
with this real structure.
3 Details of the Hulek–Craig curve
The representation (2.1) will turn out to be the most convenient for later work so it is worth
spending some time on its detail, particularly its desingularisation.
2Here a bar over variables is used to distinguish them from the Dye curve, rather than to denote complex con-
jugation. Craig notes the results of Ramanujan [1, Chapter 19, Entry 10(iv), 10(vii)] entail the parameterization
(¯x, ¯y, ¯z) =
( ∞∑
n=−∞
q(5n)2
,
∞∑
n=−∞
q(5n+1)2
,
∞∑
n=−∞
q(5n+2)2
)
.
4 H.W. Braden and T.P. Northover
