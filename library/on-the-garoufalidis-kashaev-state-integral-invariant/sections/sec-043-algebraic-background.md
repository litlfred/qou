---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "On the Garoufalidis-Kashaev state-integral invariant"
section_id: sec-043-algebraic-background
section_title: "Algebraic Background"
section_number: null
pages: 49-51
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
doc_brief: "On the Garoufalidis-Kashaev state-integral invariant — 61 sections: ACKNOWLEDGMENTS; ABSTRACT; LIST OF TABLES"
---
Definition 11 (Cochains on an Ordered Ideal Triangulation). Let X be an ordered
ideal triangulation of a compact 3-manifold M, and let G be an abelian group.
A k-cochain on X with coefficients in G is a function defined on the set of
combinatorialk-simplices of X, respecting orientation. We denote:
Ck(X;G) :={ϕ: Xor
k →G},
where Xor
k is the set of oriented k-simplices in the triangulation X, with orientation
induced by the global vertex ordering.
These cochains form an abelian group under pointwise addition.
The coboundary operator δ : Ck(X;G)→Ck+1(X;G) is defined by:
(δϕ)(σk+1) =
k+1X
i=0
(−1)iϕ(σk+1
i ),
where σk+1
i denotes the i-th oriented face of the (k + 1)-simplexσk+1.
A cochain ϕ∈Ck(X;G) is:
• a cocycle if δϕ = 0,
• a coboundary if ϕ =δψ for some ψ∈Ck−1(X;G).
40
The cohomology group is:
Hk(X;G) := ker(δ : Ck→Ck+1)
im(δ : Ck−1→Ck).
Definition 12 (Gauge group and gauge shifts) . Let X be an ordered ideal triangu-
lation of an oriented pseudo 3-manifold M. Let Eint(X)⊂ X1 be its set of internal
edges and letC = R×F×.
1. Gauge group. Denote by
GX :=C1
int(X;C) ={λ :Eint(X)−→C}
the abelian group of C-valued 1-cochains supported on internal edges.
2. Gauge shift of angles. Given an angle structure θ :X3,1→C , its gauge-shift
by λ∈G X is the map
θλ(T,e) := θ(T,e) +





λ(e) if e is opposite e in T,
− 1
2λ(e′) for the remaining four edges e′⊂T,
0 if e⊂∂M.
(Inside each tetrahedron the two opposite edges get +λ, the other four get− 1
2λ;
if an edge lies on ∂M there is no shift.)
check that for every T θλ(T,e 1) +θλ(T,e 2) +θλ(T,e 3) = (1,−1), so θλ is again
an angle structure.
41
3. Gauge equivalence. Two angle structures are gauge-equivalent if θ′ =θλ for
some λ∈G X.
