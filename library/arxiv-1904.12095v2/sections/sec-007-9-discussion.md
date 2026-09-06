---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-007-9-discussion
section_title: "Discussion"
section_number: 9
pages: 21-25
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
Let T be a ﬁnite, orientable triangulation with o vertices and m edges. We have proven
that T admits a hyperbolic structure if the checks in each step of the algorithm in Sec-
tion 7 pass. But are there hyperbolic structures which the algorithm cannot verify —
even as we increase the precision and give the algorithm better and better approxima-
tions of the edge lengths of the hyperbolic structure as input?
We conjecture that such hyperbolic structures are special and can always be avoided
by a random perturbation. We state this in the following conjecture where “generic”
means that a statement is true except for a closed measure zero set of hyperbolic struc-
tures on T (we will see later that a natural measure exists on the space of all hyperbolic
structures in Theorem 9.4):
Conjecture 9.1. Let T be a ﬁnite, orientable triangulation with o vertices and m edges
admitting a hyperbolic structure. Then a generic hyperbolic structure on T gives rise
to edge lengths le1, ... ,lem > 0 or equivalently edge parameters νe1, ... ,νem ≤ −1 such
that
(a) M in (7.1) has rank m − 3o and
(b) any choice of m − 3o linearly independent rows from M avoids gimbal lock.
More precisely, for any partition E(T ) = E ∼ ∪ E = into 3o and m − 3o edges, we
have that
1. the rows of M corresponding to the edges in E = are linearly independent
implies that
2. the derivative Dg of the gimbal function in Deﬁnition 5.1 is invertible.
Note that if Part (b) were false, the choice of the partitionE(T ) = E ∼ ∪E = made in Step I
22
could be such that Step II passes but the algorithm fails later in Step V.
Remark 9.2. Numerically, we found that the converse of Part (b) is not true, i.e., we
found examples where the gimbal function is invertible even though the chosen rows of
M are linearly dependent.
Remark 9.3. Compare the conjecture to the ideal case where we do not know in general
whether every cusped, ﬁnite volume hyperbolic 3-manifold has a geometric triangula-
tion (see [PW00, LST08, Goe17]).
9.1 The space of hyperbolic structures
Let T be a ﬁnite, orientable triangulation with o vertices and m edges admitting a hy-
perbolic structure. We are able to prove that the solution set of the edge equations has
dimension 3o. This is weaker than Part (a) of Conjecture 9.1 since it implies that the
rank of M is at most m − 3o (for example, x3 = 0 yields a 0-dimensional submanifold of
the 1-dimensional R, yet the Jacobian has rank 0 at 0 instead of the expected 1− 0 = 1).
Earlier, we deﬁned a hyperbolic structure on T as a compatible assignment of an isom-
etry class of ﬁnite simplices in H3 to each simpex in T . The space of hyperbolic struc-
tures on T can be described in the following ways:
(a) Sol( T ) ⊂ Rm
>0, the set of all tuples ( le1,. .. ,lem ) fulﬁlling the conditions of Theo-
rem 2.3 (since the edge lengths of a hyperbolic structure yield a point in Sol( T )
and determine the hyperbolic structure uniquely).
(b) The space of geodesic homeomorphisms T → M in a ﬁxed homotopy class in
[T , M ] where M is a hyperbolic 3-manifold homeomorphic to T . By Mostow
rigidity, this yields all hyperbolic structures. By ﬁxing the homotopy class, a hy-
perbolic structure gives a unique geodesic homeomorphism, instead of multiple
related by the isometries of M .
(c) The space of all developing homeomorphisms, i.e., ρ-equivariant homeomor-
phisms d : ˜T → H3 where p is a ﬁxed vertex of T and ρ : π1(T , p) → PSL2(C) is
a ﬁxed geometric representation. This gives the homeomorphism T → M in (b)
when letting M = H3/Γ where Γ = Im(ρ).
Theorem 9.4. Let T be a ﬁnite, orientable triangulation with o vertices and m edges
admitting a hyperbolic structure. The space Sol(T ) of hyperbolic structures on T is
a 3o-dimensional smooth submanifold of Rm
>0, is (non-canonically) diffeomorphic to
an open subset U ⊂
(
H3)o, and has a canonical measure induced from
(
H3)o.
Proof. We call a ρ-equivariant geodesic map d : ˜T → H3 a developing map.
Claim: Fix a vertex p of T and a geometric representation ρ : π1(T , p) → PSL2(C). Then
developing maps are in 1-1 correspondence to (H3)o.
Pick a lift ˜v1, .. ., ˜vo in ˜T of each vertex of v1, .. .,vo of T . By ρ-equivariance, the images
23
of all vertices of ˜T are determined by ( d( ˜v1), .. .,d( ˜vo)) ∈ (H3)o. A geodesic map is de-
termined uniquely by the image of all the vertices.
Claim: Under the above assumptions, the homeomorphisms among the developing
maps form an open subset U ⊂ (H3)o. We have a bijection l : U → Sol(T ).
By invariance of domain, a developing map is a homeomorphism if and only if it is an
embedding. A developing map is an embedding if and only if the image of each simplex
is positively oriented. The condition on a single simplex in ˜T to be positively oriented is
open in the four vertex positions of the simplex. As a function of (x1, .. .,xo) ∈ (H3)o, each
of these four vertex positions is given by some mx k where m is a hyperbolic isometry in
Γ = Im(ρ). Thus, the condition is also open in ( H3)o. By ρ-equivariance, it is sufﬁcient
to check this for one lift ˜∆ of each of the ﬁnitely many simplices ∆ of T , so U is open.
Claim: The map L = i ◦ l : U → Rm
>0 is smooth where i : Sol(T ) ,→ Rm
>0 is the inclusion.
The distance function H3 × H3 → R≥0 is smooth for all (x, y) with x ⁄= y.
Claim: The inverse l −1 : Sol(T ) → U is continuous.
Fix a simplex ˜∆ in ˜T and σ ∈ A4. Given a point in Sol(T ), let us consider the developing
map d ′ : ˜T → H3 obtained by starting with ˜∆ in σ-standard position (see Deﬁnition 3.2)
and developing simplex by simplex. Note that d ′ is equivariant with respect to a con-
jugate but different representation ρ′ : π1(T , p) → PGL2(C). In other words, there is
a unique element h ∈ PGL2(C) such that ρ(γ) = h ◦ ρ′(γ) ◦ h−1 for all γ ∈ π1(T , p) and
d = h ◦ d ′ is ρ-equivariant. We can compute h as follows: ﬁx γ1, γ2, γ3 ∈ π1(T , p) such
that the attractive ﬁxed points pi ∈ ∂H3 of ρ(γi ) are distinct. Let p ′
i ∈ ∂H3 be the attrac-
tive ﬁxed points of ρ′(γi ). Then h is the unique Moebius transformation withpi = h(p ′
i ).
Note that the all d ′( ˜vk) as well as all ρ′(γi ) and thus h depend continuously on the point
in Sol(T ). Thus, ( d( ˜v1),. .. ,d( ˜vo)) ∈ U ⊂ (H3)o depends continuously on the point in
Sol(T ).
Claim: The differential DL of L : U → Rm
>0 is injective at every point in U .
Assume that DL has non-trivial kernel. That is, there is a path γ : (−1, 1) → U with
(d γ(t)/d t)|t =0 ⁄= 0 but ( d(L ◦ γ)(t)/d t)|t =0 = 0. In other words, we have a 1-parameter
family of developing maps d : ˜T → H3 where at least one of the points d( ˜vk) is moving
with non-zero velocity but the derivatives of all the edge lengths is zero. As we shall see,
this cannot happen.
From the edge lengths (L ◦ γ)(t) ∈ Sol(T ), we can construct a 1-parameter family of de-
veloping maps d ′ as above. Since the derivatives of the lengths is zero, the verticesd ′( ˜vk)
all have velocity zero. It is not hard to see that the entries of theh ∈ PGL2(C) from above
also have zero derivative. Thus, the points d( ˜vk) have zero velocity.
Claim: The measure on Sol(T ) induced from
(
H3)o is independent of the above choices.
A different choice of lifts ˜v1, .. ., ˜vo of vertices corresponds to the action of ( H3)o by an
element in Γo and thus does not change the induced measure. A different choice of
ρ′ : π1(T , p) → PGL2(C) is conjugate to ρ by an element h ∈ PGL2(C). The measure on
(H3)o is invariant under the action of h.
24
9.2 1-vertex triangulations
Consider a 1-vertex triangulation T admitting a hyperbolic structure. Let p be the ver-
tex of T and ρ : π1(T , p) → PSL2(C) be a geometric representation. Note that each edge
e of T forms a loop in π1(T , p) and denote by Fe = {x ∈ CP 1 : x = ρ(e)(x)} the set of the
corresponding ﬁxed points.
Theorem 9.5. Let E ∼ = {e∼
1 ,e∼
2 ,e∼
3 } and E = be a partition of the edges of T . Gimbal
lock occurs for every hyperbolic structure on T if there are i ⁄= j with Fe∼
i
= Fe∼
j
. Oth-
erwise, gimbal lock is generically avoided.
Remark 9.6. It is imaginable that there is a 1-vertex triangulation such that |{Fe : e ∈
E(T )}| = 2 and gimbal lock occurs for each choice of E ∼ giving a counterexample to
Conjecture 9.1.
action by ρ(e ∼
i )
d(p)
ρ(e ∼
i )d(p)ρ(e ∼
i )−1d(p)
ai
− →a 1
i
− →a 0
i
gi
Figure 11. Edge in 1-vertex triangulation.
Proof. The edges e∼
i become geodesics with a potential kink at the image of p in M .
Let − →a 0
i and − →a 1
i be the directions (of unit length) in which the two ends of e∼
i approach
d(p) ∈ H3 in the developing embedding d : ˜T → H3. We can identify the tangent space
at d(p) with Euclidean 3-space such that the gimbal matrix mΓ is the product of six
rotations (the order depending on the choice of gimbal loop Γ)
R
− →a 0
1
T1
, R
− →a 1
1
T1
, R
− →a 0
2
T2
, R
− →a 1
2
T2
, R
− →a 0
3
T3
, and R
− →a 1
3
T3
where R
− →v
ω ∈ SO3 denotes the rotation about − →v by angle ω. Let − →a j
i ,k denote the k-th
component of − →a j
i . At the point where all Ti = 2π, we have
∂mΓ
∂Ti
=
R
− →a 0
i
Ti
∂Ti
+
R
− →a 1
i
Ti
∂Ti
=


0 −− →a 0
i ,2
− →a 0
i ,1− →a 0
i ,2 0 −− →a 0
i ,0
−− →a 0
i ,1
− →a 0
i ,0 0

 +


0 −− →a 1
i ,2
− →a 1
i ,1− →a 1
i ,2 0 −− →a 1
i ,0
−− →a 1
i ,1
− →a 1
i ,0 0

,
so ∂g
∂Ti
=
(
−
(− →a 0
i ,2 + − →a 1
i ,2
)
,
(− →a 0
i ,1 + − →a 1
i ,1
)
, −
(− →a 0
i ,0 + − →a 1
i ,0
))
=
(
−ai ,2, ai ,1, −ai ,0
)
where ai = − →a 0
i + − →a 1
i . Thus, Dg =
(
∂g /∂T1, ∂g /∂T2, ∂g /∂T3
)
is invertible if a1, a2, and a3
are linearly independent. Figure 11 shows that ai is pointing from d(p) to the geodesic
gi spanned by Fe∼
i
(respectively pointing to Fe∼
i
if |Fe∼
i
| = 1) and ai = 0 if it lies on that
geodesic.
25
Claim: Given a point x ∈ H3, consider the directions ai from x to the point on gi closest
to x (respectively pointing to Fe∼
i
if |Fe∼
i
| = 1). The set V of x where these directions lie
in a plane is closed and has measure zero if all sets Fe∼
i
are distinct. Otherwise V = H3.
Let f : H3 \ ∪i gi → R, x 7→ ω(a1, a2, a3) where ω is the volume form on H3. Since ai is the
Hodge dual to the gradient of the distance of x to gi , f is analytic. It is not hard to see
that there is some x with f (x) ⁄= 0 as long as no two Fe∼
i
and Fe∼
j
are equal. Thus f −1(0)
and V = f −1(0) ∪ ∪i gi have measure zero.
