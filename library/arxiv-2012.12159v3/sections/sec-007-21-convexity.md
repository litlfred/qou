---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-007-21-convexity
section_title: "Convexity"
section_number: 2.1
pages: 7-8
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
---
will henceforth assume to have non-empty interior. We write|K| for the Euclidean
volume of K, andHn−1 for the Hausdorﬀ measure on ∂K.
The Euclidean unit ball is Bn, and ωn :=|Bn| = π
n
2
Γ(n
2 +1). The support function
of K ⊂ V is hK(ξ) = sup x∈K⟨x,ξ⟩ : V∗→ R, which is a convex function. We
say that K is smooth and strictly convex if ∂K is C2-smooth of strictly positive
gaussian curvature.
ByK0(V ) we denote the class of convex bodies with 0∈ int(K). ForK∈K 0(V ),
the Minkowski functional of K is‖x‖K = inf{t >0 : x
t ∈K}. If K =−K, it is a
norm for which K is the unit ball. The cone measure on ∂K is denoted µK, and
has
∫
KdµK =n|K|. If ∂K isC1 smooth, it is given by dµK(x) =⟨x,νx⟩dHn−1(x),
where νx is the outward unit normal.
The polar (or dual) convex body is Ko ={ξ∈ V∗ :⟨ξ,x⟩≤ 1}∈K 0(V∗). It
holds that‖ξ‖Ko =hK(ξ). For z∈ int(K), we write Kz = (K−z)o.
For a Borel function φ :V → R∪{ +∞}, its Legendre transform is
Lφ(ξ) = sup
x∈Rn
(⟨x,ξ⟩− φ(x)) :V∗→ R∪{ +∞}. (1)
If φ is deﬁned on a subset of V , we ﬁrst extend it by +∞.
The function Lφ is always convex, and if φ is convex then L2φ = φ. An easy
computation shows thatL( 1
p‖x‖p
K) = 1
q‖ξ‖q
Ko forp−1 +q−1 = 1. This includes the
case p =∞,q = 1 which readsL(− log 1 K)(ξ) =‖ξ‖Ko =hK(ξ).
Writingφz =φ(z +•), one immediately ﬁnds that
Lφz(ξ) = sup
x
(⟨x,ξ⟩− φ(x +z)) =Lφ(ξ)−⟨z,ξ⟩.
For much more information on convexity, we refer to [27].
2.2. Projective geometry. Denote V = Rn+1. We often write P = RPn = P(V )
for then-dimensional real projective space when the dimension is clear from context,
and P∨ = P(V∗) for the dual projective space. The group of isomorphisms of the
projective space is PGL(n + 1) = GL(n + 1)/R∗, and its elements are the invertible
projective maps, also known as homographies. Projective duality establishes a
bijection between the points of P and the hyperplanes of P∨, by assigning to a
point x∈ P the hyperplane P(x⊥)⊂ P∨, also denoted x⊥. This allows to identify
P∨ with the set of hyperplanes of P, and vice versa.
A convex bodyK⊂ P is the image of a closed proper convex cone inRn+1, namely
one that does not contain a line. Equivalently, for any hyperplane H ⊂ P\K,
K⊂ P\H = Rn is a convex body. We will often use the same notation for both
the body and the cone it deﬁnes inV . The polar (or dual) convex body isK∨⊂ P∨,
which is the closure of the set of all hyperplanes disjoint from K. K∨ is a convex
body, and if K is smooth and strictly convex, then so is K∨. The normal map ,
also called the Legendre transform, is the bijection LK : ∂K → ∂K∨, given by
x↦→Tx∂K. The linear and projective polar bodies are closely related, see Lemma
3.3.
Let a,b,c,d lie on a line in P, in that order. Their cross ratio is [a,b,c,d ] :=
|ac||bd|
|ab||cd|. It is invariant under PGL(n + 1). A pencil of hyperplanes in P is the image
under projective duality of a line in P∨. The cross ratio of four hyperplanes on
8 A Funk perspective on billiards, projective geometry and Mahler volume
a pencil is deﬁned as their cross ratio in P∨. It can be computed by intersecting
the hyperplanes with a generic line, and taking the cross ratio of the respective
intersection points.
A quadric E = [A]⊂ P is given by the homogeneous quadratic equation {x :
⟨Ax,x⟩ = 0}, for some symmetric matrix A = AE. A linear pencil of quadrics is
any family of quadrics of the form [ tA1 +sA2], t,s∈ R. A dual pencil is a family
of the form [(tA−1
1 +sA−1
2 )−1], t,s∈ R.
Given two non-degenerate quadrics E1,E 2 ∈ RPn, the projective map A =
E−1
1 E2∈ PGL(n + 1) is deﬁned as follows. Let Q1,Q 2 be quadratic forms on Rn+1
such thatEj ={Qj = 0}, which are uniquely deﬁned up to a scalar multiple. Then
A is represented by the endomorphism A given by settingQ2(x,y ) =Q1(Ax,y ) for
all x,y∈ Rn+1.
Deﬁnition 2.1. Four quadrics Q1,Q 2,Q 3,Q 4⊂ P form a nic quadruplet if
Q−1
2 Q1 =Q−1
4 Q3.
We refer to e.g. [25] for an overview to projective geometry, and to [4] for an
introduction to convexity in projective geometry.
