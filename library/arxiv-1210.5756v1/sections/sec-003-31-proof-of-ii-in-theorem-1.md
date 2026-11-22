---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-003-31-proof-of-ii-in-theorem-1
section_title: "Proof of (ii) in Theorem 1"
section_number: 3.1
pages: 6-7
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Proof of (ii) in Theorem 1
Let us imagine that we generate packings of n unit balls in E3 in such a special way that each and every
center of the n unit balls chosen, is a lattice point of some ﬁxed lattice Λ (resp., of the face-centered cubic
lattice Λfcc) with shortest non-zero lattice vector of length 2. (Here, a lattice means a (discrete) set of points
having position vectors that are integer linear combinations of three ﬁxed linearly independent vectors of
E3.) Then let CΛ(n) (resp., Cfcc(n)) denote the largest possible number of touching pairs for all packings
of n unit balls obtained in this way.
In order to prove (ii) in Theorem 1 it is suﬃcient to show that
CΛ(n) ≤Cfcc(n) and recall from [2] that Cfcc(n) < 6n −3 3√
18π
π
n
2
3 = 6n −3.665 . . . n
2
3 . So, we are left to
show that CΛ(n) ≤Cfcc(n). The details are as follows.
6
Recall Voronoi’s theorem (see [3]) according to which every 3-dimensional lattice is of the ﬁrst kind
i.e., it has an obtuse superbase. Thus, for the lattice Λ (resp., Λfcc) we have a set of vectors v0, v1, v2, v3
(resp., w0, w1, w2, w3 ) such that v1, v2, v3 (resp., w1, w2, w3) is an integral basis for Λ (resp., Λfcc) and
v0 + v1 + v2 + v3 = o (resp., w0 + w1 + w2 + w3 = o), and in addition vi · vj ≤0 (resp., wi · wj ≤0) for
all i, j = 0, 1, 2, 3, i̸ = j. Here · refers to the standard inner product of E3. Let P (resp., Q) denote the
Voronoi cell for the origin o ∈Λ (resp., o ∈Λfcc) consisting of points of E3 that are at least as close to o
as to any other lattice point of Λ (resp., Λfcc). A vector v ∈Λ (resp., w ∈Λfcc) is called a strict Voronoi
vector of Λ (resp., Λfcc) if the plane {x ∈E3 | x · v = 1
2v · v} (resp., {x ∈E3 | x · w = 1
2w · w} ) intersects
P (resp., Q) in a face. We need the following claim proved in [3]. The list of 14 lattice vectors of Λ (resp.,
Λfcc) consisting of
±v1, ±(v0 + v1), ±(v1 + v2), ±(v1 + v3),
±(v0 + v1 + v2), ±(v0 + v1 + v3), ±(v1 + v2 + v3)
(resp., ± w1, ±(w0 + w1), ±(w1 + w2), ±(w1 + w3),
±(w0 + w1 + w2), ±(w0 + w1 + w3), ±(w1 + w2 + w3))
includes all the strict Voronoi vectors of Λ (resp., Λfcc). As is well known (and in fact, it is easy check)
at most 12 (resp., exactly 12) of the above 14 vectors has length 2 and the others are of length strictly
greater than 2. Thus, it follows that without loss of generality we may assume that whenever vi · vi = 4
holds we have wi · wi = 4 as well. This implies the exisctence of a map f : Λ →Λfcc with the property
that if dist(x, y) = 2 with x, y ∈Λ, then also dist(f(x), f(y)) = 2 holds. Indeed, f can be deﬁned via
f(αv1 + βv2 + γv3) = αw1 + βw2 + γw3 with α, β, γ being arbitrary integers. As a result we get the
following: if P is a packing of n unit balls with centers c1, c2, . . . , cn ∈Λ, then the packing Pf of n unit balls
centered at the points f(c1), f(c2), . . . , f(cn) ∈Λfcc possesses the property that C(P) ≤C(Pf), where C(P)
(resp., C(Pf)) stands for the number of touching pairs in P (resp., Pf). Thus, indeed, CΛ(n) ≤Cfcc(n)
ﬁnishing the proof of (ii) in Theorem 1.
