---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-008-222-proof-of-part-a-of-theorem-discrete-dantzig
section_title: "Proof of part (a) of Theorem ??: Discrete Dantzig descent."
section_number: 2.2.2
pages: 12-12
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
In order to avoid
zig-zagging (see example in Section 4 of [19] and the details of how to avoid this), we must augment
to a vertex with lower objective-function value after each discrete Dantzig-descent augmentation.
For this, we need at most n discrete Dantzig-descent augmentations within smaller and smaller
faces of P. Let xk be a vertex of the given polyhedron. Again we observe that
0 > c⊺(xmin −xk) = c⊺X
αigi =
X
αic⊺gi ≥−∆0
X
αi ≥−n∆αmax,
where ∆0 > 0 is the greatest value of −c⊺z over all z ∈C(A) for which xk + λz is feasible for
suﬃciently small λ > 0 and where αmax = max{αi }. Rewriting this, we get
∆0 ≥c⊺(xk −xmin)
nαmax
.
Now, let αz be the discrete Dantzig-descent augmentation applied to xk, leading to xk+1 := xk +αz.
As xk is a vertex and z an edge direction, we have xk,z ∈1
δZn. As xk+1 is lies on the intersection
of the half-line {x = xk + λz : λ ≥0} with some facet of the polyhedron, we get that xk+1 ∈1
δ2 Zn.
Consequently, α ≥1/δ.
Thus, we get
c⊺(xk −xk+1) = −αc⊺z = α∆0 ≥1
δ∆0 ≥c⊺(xk −xmin)
nδαmax
≥c⊺(x0 −xmin)
nδγ
,
where γ is the maximum entry in any feasible solution (or, equivalently, in any vertex). Thus, we
have a factor of β = 1/(nδγ) of objective-function decrease at each augmentation. Applying Lemma
3 with ǫ = 1/δ then yields the desired bound on the number of augmentations 2n2δγ log(δ c⊺(x0 −
xmin))) to reach a vertex ¯x with |c⊺(¯x −xmin)| < 1/δ. This vertex must be optimal.
