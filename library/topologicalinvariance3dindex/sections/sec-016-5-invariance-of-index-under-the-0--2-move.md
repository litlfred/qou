---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-016-5-invariance-of-index-under-the-0--2-move
section_title: "Invariance of index under the 0--2 move"
section_number: 5
pages: 29-32
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
Let M be a cusped 3-manifold and consider the 02 move on a pair T and eT of ideal
triangulations of M with N and N + 2 tetrahedra, as shown in Figure 14.
Theorem 5.1. Suppose that T and eT are ideal triangulations related by a 02 move and both
admit an index structure. Then, for any [ϖ] ∈H1(∂M; Z), IT([ϖ]) = IeT([ϖ]).
Proof. Our assumptions imply that both IT and IeT exist. We now compare these indices
using the alternative de
nition (25) and quadratic identity (23).
We use the labelling of the two bigons and triangles on eT shown in Figure 14. Let Ti for
i = 3, . . . , N +2 denote the tetrahedra in T, and let T1, T2 be the additional tetrahedra added
in eT. Note that the edge e in T splits into two edges e′, e′′ in eT, and there is another new
edge e in eT. We abuse notation by identifying the symbols for the corresponding remaining
edges in T and eT. We denote these as e1, . . . , eN−1.
Let ek ∈ZN+2 be a weight function on the edges of eT and write ek = (k′, k′′, ek, k1, . . . , kN−1)
where k′, k′′, ek, ki are the values of ek on e′, e′′, e and ei respectively.
Similarly, let k =
(k, k1, . . . , kN−1) ∈ZN be a corresponding weight function on T. We choose label ¯aj on the
30 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
e
e2
e4
e1
e3
e2
e4
e1
e3
e′
e′′
e
¯a2
¯a1
¯c2
¯b2
¯b1
¯c1
¯a1
¯a2
¯c1
¯b1
¯b2
¯c2
¯a1
¯c1
¯b1
¯a2
¯b2
¯c2
¯a2
¯c2
¯b2
¯a1
¯b1
¯c1
Figure 14. The 02 move shown with truncated tetrahedra. The four trian-
gulated ends of the new pair of tetrahedra are shown. All of the zoomed in
pictures are as seen from viewpoints outside of the pair of tetrahedra. The
labels at the corners of the triangles in the zoomed in pictures are explained
in Section 4.4.
edge e on tetrahedron Tj for j = 1, 2; then the location of labels ¯bj, ¯cj are determined using
the orientation on M.
Let ϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂of ∂M induced by T, and let eϖ an oriented multi-curve which is normal with re-
spect to eT∂and represents the same homology class [ϖ] ∈H1(∂M; Z). Let J(Tj, k, ϖ) =
J∆(¯aj(k, ϖ),¯bj(k, ϖ), ¯cj(k, ϖ)) denote the contribution of tetrahedron Tj to the index with
weight function k on its edges and peripheral curve ϖ on its truncated ends, and similarly
let J(Tj, ek, eϖ) be contribution with weight function ek and peripheral curve eϖ.
To compute IT we use Theorem 4.3 to choose an excluded set X of r edges in a maximal
tree with 1- or 3-cycle in T to be omitted from the summation in (25).
Case 1: If e /∈X we can order the edges of T so that X = {eN−r, . . . , eN−2, eN−1}. Then
we can compute IeT by omitting the same edge set eX = X.
Case 2: If e ∈X we can order the edges so X = {e, eN−r+1, . . . , eN−2, eN−1}. Then we can
compute IeT by omitting the edge set eX = {e′′, eN−r+1, . . . , eN−2, eN−1}.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
31
Then
(30)
IeT(eϖ) =
X
ek∈eS
qk′+k′′+ek+PN−1
i=1 ki J(T1, ek, eϖ)J(T2, ek, eϖ)
N+2
Y
j=3
J(Tj, ek, eϖ),
where
eS =
n
ek = (k′, k′′, ek, k1, . . . , kN−1) ∈ZN+2 : kN−i = 0 for i = 1, . . . , r
o
in case 1
and
eS =
n
ek = (k′, k′′, ek, k1, . . . , kN−1) ∈ZN+2 : k′′ = 0, kN−i = 0 for i = 1, . . . , r −1
o
in case 2.
Note that in both cases, the new edge ˜e is included in the set of basic edges so ˜k varies over
Z in the sum.
Now we look at the contribution to IeT coming from the tetrahedra T1, T2 and summed
over the weight ek on ˜e, namely
(31)
X
ek∈Z
q
ekJ(T1; ek, eϖ)J(T2; ek, eϖ)
where
J(T1; ek, eϖ) = J∆(k′ + ek + ¯a eϖ,1, k2 + k3 + ¯b eϖ,1, k1 + k4 + ¯c eϖ,1)
and
J(T2; ek, eϖ) = J∆(k′′ + ek + ¯a eϖ,2, k1 + k4 + ¯b eϖ,2, k2 + k3 + ¯c eϖ,2).
Recall that ϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂of ∂M induced by T. Since the index only depends on the homology class of a peripheral
curve, we can calculate IeT([ϖ]) by using for eϖ a corresponding curve on ∂M which is normal
with respect to eT∂and goes straight through each pair of added triangles on ∂M. See
Figure 15.
Then we have
¯a eϖ,1 = ¯a eϖ,2 = 0,
¯b eϖ,1 = ¯c eϖ,2 = x,
¯b eϖ,2 = ¯c eϖ,1 = y,
for some x, y ∈Z, and
¯a eϖ,j = ¯aϖ,j, ¯b eϖ,j = ¯bϖ,j, ¯c eϖ,j = ¯cϖ,j for j = 3, . . . , N + 2.
Using the invariance of J∆under all permutations of its arguments and the quadratic
identity (23), the sum (31) becomes
X
ek∈Z
q
ekJ∆(k′ + ek, k2 + k3 + x, k1 + k4 + y)J∆(k′′ + ek, k1 + k4 + y, k2 + k3 + x) = q−k′ δk′,k′′.
This means that in the sum (30) we can remove the summation over ek and put k′ = k′′ = k.
Hence J(Tj, ek, eϖ) = J(Tj, k, ϖ) for j = 3, . . . , N + 2, and
IeT(eϖ) =
X
k∈S
qk+PN−1
i=1 ki
N+2
Y
j=3
J(Tj, k, ϖ) = IT(ϖ),
32 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
¯a2
¯a1
¯c2
¯b2
¯b1
¯c1
¯a2
¯c2
¯b2
¯a1
¯b1
¯c1
Figure 15. Changes in peripheral curve from ϖ in T∂to eϖ in eT∂. Note that
the curve in the top diagram could go either way around the new vertex.
where
S =

k = (k, k1, . . . , kN−1) ∈ZN : kN−i = 0 for i = 1, . . . , r
	
in case 1
and
S =

k = (k, k1, . . . , kN−1) ∈ZN : k = 0, kN−i = 0 for i = 1, . . . , r −1
	
in case 2.
This completes the proof of invariance of the index under the 02 move.
□
