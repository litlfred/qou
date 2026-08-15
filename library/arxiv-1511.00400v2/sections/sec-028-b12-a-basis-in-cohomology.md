---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-028-b12-a-basis-in-cohomology
section_title: "B.1.2 A basis in cohomology"
section_number: null
pages: 48-49
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
To describe a basis for Hi(M 3; ̺k1,k2 ) when i = 1, 2, recall the cap product
deﬁned in Equation (31).
∩∶ H 0(T 2; ̺k1,k2) × Hi(T 2; C) → Hi(T 2; ̺k1,k2).
Let i∶ T 2 → M 3 denote the inclusion, and i∗∶ Hj(T 2; ̺k1,k2 ) → Hj(M 3; ̺k1,k2),
the induced map.
Proposition B.8. Let M 3 and T 2 be as above, k1 ≠k2, k1 + k2 even. Choose
a ∈H 0(T 2; ̺k1,k2), a ≠0. Then:
(a) i∗(a ∩ [T 2]) is a basis for H2(M 3; ̺k1,k2), where [T 2] ∈H2(T 2; Z) is a
fundamental class.
(b) i∗(a ∩ [γ]) is a basis for H1(M 3; ̺k1,0) or H1(M 3; ̺0,k2 ), for any [γ] ∈
H1(T 2; Z), [γ] ≠0.
(c) If ̺ denotes a lift of the holonomy of the complete structure, for any pair of
peripheral curves 0 ≠[γ1], [γ2] ∈H 1(T 2; Z) and for a ∈H 0(T 2; ̺k,0)
a ∪ [γ2] = cs(γ2, γ1)a ∩ [γ1]
in H1(T 2; ρk,0).
(d) When k1k2 ≠0, the cap product
∩∶ H 0(T 2; ̺k1,k2 ) × H1(T 2; C) → H1(T 2; ̺k1,k2)
is the trivial map (i.e. identically zero).
Proof. For Item (a), a ∩ [T 2] is a basis for H2(T 2; ̺k1,k2), by Poincar´ e duality
and Lemma B.5. Item (b) is proved in [60] for k2 = 0. It holds true for k1 = 0
by complex conjugation.
To prove the other two items, we choose a cell decomposition of the torus
from a square with opposite edges identiﬁed. Namely there is a 2-cell e2 repre-
sented by a square, whose sides are two copies of the 1-cells: e1
1 and e1
2 (with
respective homology classes [e1
1] = [m] and [e1
2] = [l] respectively) and the ver-
tices are four copies of the 0-cell. Choose lifts to the universal cov ering so that
∂˜e2 = (1 − l)˜e1
1 + (m − 1)˜e2
1, (59)
where m and l generate π1T 2. We may assume that
̺(m) = ± /par⟩nl⟩ft.alt41 1
0 1 /par⟩nright.alt4 and ̺(l) = ± /par⟩nl⟩ft.alt41 η
0 1 /par⟩nright.alt4
where η = cs(l, m) ∈C − R.
We prove now (c). Sym k acts on the space of degree k homogeneous polyno-
mials on X and Y ; the one dimensional space invariant by ̺k = ̺k,0 is generated
by a = X k (Lemma B.5). By (59):
∂(X k−1Y ⊗ ˜e2) = −η a ⊗ ˜e1
1 + a ⊗ ˜e2
1
48
which in cohomology translates to −η a ∩ [m] + a ∩ [l] = 0. This proves (c) for a
system of generators {[m], [l]} of H1(T 2; Z), and it holds in general by linearity.
We prove ﬁnally (d). Sym k1 ⊗Symk2 acts on the space of degree k1 homoge-
neous polynomials on X and Y , multiplied by degree k2 homogeneous polyno-
mials on ¯X and ¯Y ; the one dimensional space invariant by ̺k1,k2 is generated
by a = X k1 ¯X k2. By (59):
∂(X k1−1Y ¯X k2 ⊗ ˜e2) = −η a ⊗ ˜e1
1 + a ⊗ ˜e2
1
∂(X k1 ¯X k2−1Y ⊗ ˜e2) = −¯η a ⊗ ˜e1
1 + a ⊗ ˜e2
1
Namely, in homology −η a ∩ [m] + a ∩ [l] = −¯η a ∩ [m] + a ∩ [l] = 0. As η /slash.l⟩ft∈R, the
claim follows.
