---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-014-5-invariance-of-index-under-the-02-move
section_title: "Invariance of index under the 0–2 move"
section_number: 5
pages: 29-32
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
Let M be a cusped 3-manifold and consider the 0–2 move on a pairT and ~T of ideal
triangulations ofM with N and N + 2 tetrahedra, as shown in Figure 14.
Theorem 5.1.Suppose thatT and~T are ideal triangulations related by a 0–2 move and both
admit an index structure. Then, for any[ϖ]∈H1(∂M ; Z), IT([ϖ]) =I~T([ϖ]).
Proof. Our assumptions imply that bothIT and I~T exist. We now compare these indices
using the alternative deﬁnition (25) and quadratic identity (23).
We use the labelling of the two bigons and triangles on~T shown in Figure 14. LetTi for
i = 3,...,N +2 denote the tetrahedra inT, and letT1,T 2 be the additional tetrahedra added
in ~T. Note that the edgee in T splits into two edgese′,e′′ in ~T, and there is another new
edge~e in~T. We abuse notation by identifying the symbols for the corresponding remaining
edges in T and~T. We denote these ase1,...,e N−1.
Let~k∈ ZN+2 be a weight function on the edges of~T and write~k = (k′,k′′,~k,k 1,...,k N−1)
where k′,k′′,~k,ki are the values of ~k on e′,e′′,~e and ei respectively. Similarly, let k =
(k,k 1,...,k N−1)∈ ZN be a corresponding weight function onT. We choose label¯aj on the
edge~e on tetrahedronTj for j = 1, 2; then the location of labels¯bj, ¯cj are determined using
the orientation onM.
Let ϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂ of ∂M induced by T, and let ~ϖ an oriented multi-curve which is normal with re-
spect to~T∂ and represents the same homology class[ϖ]∈ H1(∂M ; Z). Let J(Tj,k,ϖ ) =
J∆(¯aj(k,ϖ ),¯bj(k,ϖ ), ¯cj(k,ϖ )) denote the contribution of tetrahedronTj to the index with
weight functionk on its edges and peripheral curveϖ on its truncated ends, and similarly
let J(Tj,~k,~ϖ) be contribution with weight function~k and peripheral curve~ϖ.
To computeIT we use Theorem 4.3 to choose an excluded setX of r edges in a maximal
tree with 1- or 3-cycle inT to be omitted from the summation in (25).
30 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
e e
e2 e4
e1 e3
e2 e4
e1 e3
e′
e′′
~e
¯a2 ¯a1
¯c2
¯b2
¯b1
¯c1
¯a1 ¯a2
¯c1
¯b1
¯b2
¯c2
¯a1¯c1 ¯b1
¯a2¯b2 ¯c2
¯a2¯c2 ¯b2
¯a1¯b1 ¯c1
Figure 14. The 0–2 move shown with truncated tetrahedra. The four trian-
gulated ends of the new pair of tetrahedra are shown. All of the “zoomed in”
pictures are as seen from viewpoints outside of the pair of tetrahedra. The
labels at the corners of the triangles in the “zoomed in” pictures are explained
in Section 4.4.
Case 1: Ife /∈ X we can order the edges ofT so that X ={eN−r,...,e N−2,eN−1}. Then
we can computeI~T by omitting the same edge set~X = X.
Case 2: Ife∈ X we can order the edges soX ={e,eN−r+1,...,e N−2,eN−1}. Then we can
compute I~T by omitting the edge set~X ={e′′,eN−r+1,...,e N−2,eN−1}.
Then
(30) I~T(~ϖ) =
∑
~k∈ ~S
qk′+k′′+~k+∑N−1
i=1 kiJ(T1,~k,~ϖ)J(T2,~k,~ϖ)
N+2∏
j=3
J(Tj,~k,~ϖ),
where
~S =
{
~k = (k′,k′′,~k,k 1,...,k N−1)∈ ZN+2 :kN−i = 0 for i = 1,...,r
}
in case 1
and
~S =
{
~k = (k′,k′′,~k,k 1,...,k N−1)∈ ZN+2 :k′′ = 0,kN−i = 0 for i = 1,...,r − 1
}
in case 2.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 31
Note that in both cases, the new edge˜e is included in the set of basic edges so˜k varies over
Z in the sum.
Now we look at the contribution toI~T coming from the tetrahedraT1,T 2 and summed
over the weight~k on ˜e, namely
(31)
∑
~k∈Z
q
~kJ(T1;~k,~ϖ)J(T2;~k,~ϖ)
where
J(T1;~k,~ϖ) =J∆(k′ +~k + ¯a ~ϖ,1,k 2 +k3 + ¯b ~ϖ,1,k 1 +k4 + ¯c ~ϖ,1)
and
J(T2;~k,~ϖ) =J∆(k′′ +~k + ¯a ~ϖ,2,k 1 +k4 + ¯b ~ϖ,2,k 2 +k3 + ¯c ~ϖ,2).
Recall thatϖ be an oriented multi-curve which is normal with respect to the triangulation
T∂ of∂M induced byT. Since the index only depends on the homology class of a peripheral
curve, we can calculateI~T([ϖ]) by using for~ϖ a corresponding curve on∂M which is normal
with respect to~T∂ and goes “straight through” each pair of added triangles on∂M. See
Figure 15.
¯a2 ¯a1
¯c2
¯b2
¯b1
¯c1
¯a2¯c2 ¯b2
¯a1¯b1 ¯c1
Figure 15. Changes in peripheral curve fromϖ in T∂ to ~ϖ in~T∂. Note that
the curve in the top diagram could go either way around the new vertex.
Then we have
¯a ~ϖ,1 = ¯a ~ϖ,2 = 0, ¯b ~ϖ,1 = ¯c ~ϖ,2 =x, ¯b ~ϖ,2 = ¯c ~ϖ,1 =y,
for somex,y∈ Z, and
¯a ~ϖ,j = ¯aϖ,j, ¯b ~ϖ,j = ¯bϖ,j, ¯c ~ϖ,j = ¯cϖ,j for j = 3,...,N + 2.
32 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Using the invariance ofJ∆ under all permutations of its arguments and the quadratic
identity (23), the sum (31) becomes
∑
~k∈Z
q
~kJ∆(k′ +~k,k 2 +k3 +x,k 1 +k4 +y)J∆(k′′ +~k,k 1 +k4 +y,k 2 +k3 +x) =q−k′
δk′,k′′.
This means that in the sum (30) we can remove the summation over~k and putk′ =k′′ =k.
Hence J(Tj,~k,~ϖ) =J(Tj,k,ϖ ) for j = 3,...,N + 2, and
I~T(~ϖ) =
∑
k∈S
qk+∑N−1
i=1 ki
N+2∏
j=3
J(Tj,k,ϖ ) =IT(ϖ),
where
S =
{
k = (k,k 1,...,k N−1)∈ ZN :kN−i = 0 for i = 1,...,r
}
in case 1
and
S =
{
k = (k,k 1,...,k N−1)∈ ZN :k = 0,kN−i = 0 for i = 1,...,r − 1
}
in case 2.
This completes the proof of invariance of the index under the 0–2 move. □
6. The XEP
M class of triangulations
