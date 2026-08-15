---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-005-221-mayer-vietoris
section_title: "Mayer-Vietoris"
section_number: 2.2.1
pages: 7-8
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
considered, in particular instead of just the torsion it is more conve nient to
consider the twisted Alexander polynomial, which is a torsion by [53]. T he
subsection ﬁnishes with examples.
7
2.2.1 Mayer-Vietoris
Let K be a CW-complex, with subcomplexes K1, K 2 ⊂K so that K = K1 ∪ K2.
Let ρ∶ π1K → SLn(F ) be a representation. Consider the diagram of inclusions
K1 ∩ K2
i2
/d15/d15
i1 /d47/d47 K1
j1
/d15/d15
K2
j2 /d47/d47 K.
There is a Mayer-Vietoris exact sequence in homology with twisted co eﬃcients,
if the representations on π1K1, π1K2 and π1L are the restrictions:
⋯ → /uni2295.big.disp
L
Hi(L; ρ)
i1∗⊕i2∗
/leftrightline /leftrightline /leftrightline /leftrightline → Hi(K1; ρ) ⊕ Hi(K2; ρ)
j1∗−j2∗
/leftrightline /leftrightline /leftrightline /leftrightline → Hi(K; ρ)
→ /uni2295.big.disp
L
Hi−1(L; ρ) → ⋯ (8)
where L runs on the connected components of K1 ∩ K2. Notice that diﬀer-
ent choices of base-points yield canonical isomorphisms between th e homology
groups, hence we can consider K1 ∩ K2 not connected,
Choose a basis for each of these cohomology groups h∗ for H∗(K; ρ), h1∗ for
H∗(K1; ρ), h2∗ for H∗(K2; ρ), and hL∗ for H∗(L; ρ). The long exact sequence
(8) is viewed as a complex. Its torsion is denoted by tor (H, h∗∗).
Proposition 2.10 (Mayer-Vietoris). Let K be a CW-complex, with subcom-
plexes K1 ∩ K2 so that K = K1 ∪ K2. Let ρ∶ π1K → SLn(F ) be a representation
and choose basis in homology. Then
tor(K, h∗; ρ) = tor(K1, h1∗; ρ) tor(K2, h2∗; ρ)
∏
L
tor(L, hL∗; ρ) tor(H, h∗∗)
where L runs on the connected components of K1 ∩ K2.
This is used in surgery formulas (e.g. Proposition 3.25) or for the map ping
torus (Proposition 2.14). The proof can be found in [65] or in [82, Se ction 0.4].
