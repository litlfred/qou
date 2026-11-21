---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-025-b1-volume-estimates-for-bundles
section_title: "B.1 Volume estimates for bundles"
section_number: null
pages: 40-41
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Volume estimates for bundles
Theorem B.1 Let Vϕ be a once-punctured torus bundle deﬁned by the cyclic word
Ω= Ra1Lb1 · · · RanLbn . Then
2n v3 ≤Vol(Vϕ) < 2n v8,
where v3 ≈1.0149 is the volume of a regular ideal tetrahedron and v8 ≈3.6638 is the
volume of a regular ideal octahedron. Both of these bounds are sharp.
This is a sharp, quantitative version of Brock’s result in [8], in the special case of
punctured torus bundles. The upper bound is not new; it is a special case of [2, Corollary
2.4].
Proof To prove the lower bound on volume, we exhibit a particular angle structure.
It follows from the proof of Theorem 1.1 that the volume of the complete hyperbolic
structure on Vϕ is the global maximum of V over the closed polytope ¯P. Thus, for any
w ∈¯P, V(w) ≤Vol(Vϕ).
We choose w in the simplest possible manner: by letting wi = π
3 for all i. It is easy to
check that this choice of parameters satisﬁes at least the weak form of all the inequalities
of (3). In other words, all angles are nonnegative, and w ∈¯P. Any nonhinge tetrahedron
∆i will have one vanishing angle and will therefore have volume 0. However, every
hinge tetrahedron ∆i will be a regular tetrahedron, with all angles π
3 and volume v3.
Thus V(w) = 2nv3.
When Ω= (RL)n, and thus all tetrahedra are hinges, this choice of angles will in fact
give the complete structure on Vϕ. These bundles, which are n–fold cyclic covers of the
ﬁgure–8 knot complement, have volume exactly 2nv3. On the other hand, the bundles
that contain some nonhinge tetrahedra have Vol(Vϕ) > 2nv3, because V is maximized
at a point where all tetrahedra have positive angles.
To prove the upper bound, we employ a Dehn surgery construction. For every Farey
vertex s which corresponds to a fan RL∗R or LR∗L (with ∗> 0), drill a closed curve of
Geometry & Topology 10 (2006)
Canonical triangulations
1279
slope s out of the ﬁber at the corresponding level. (These are exactly the closed curves
whose length was estimated in Section 10.) The resulting drilled bundle turns out to be
an n–fold cyclic cover of the Borromean rings complement, with volume 2nv8.
We can recover Vϕ by Dehn ﬁlling the extra cusps of the drilled bundle. Because
volume goes down under Dehn ﬁlling, Vol(Vϕ) < 2nv8. If we pick a word Ωwith very
long syllables, as in Section 10, the resulting bundle Vϕ has volume arbitrarily close to
the volume of this surgery parent.
Corollary B.2 Let Vϕ be a 4–punctured sphere bundle deﬁned by the cyclic word
Ω= Ra1Lb1 · · · RanLbn . Then
4n v3 ≤Vol(Vϕ) < 4n v8.
