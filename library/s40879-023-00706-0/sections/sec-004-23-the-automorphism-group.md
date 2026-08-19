---
doc_id: s40879-023-00706-0
doc_title: "RESEARCH ARTICLE"
section_id: sec-004-23-the-automorphism-group
section_title: "The automorphism group"
section_number: 2.3
pages: 14-17
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
As previously noted, the P4-model of Bring’s curve shows that the automorphism
group Aut (B) contains S5. Hurwitz’s theorem on the automorphism group G =
Aut(C) of a curve of genus g /greaterorequalslant2 yields that |G|∈{ 84(g − 1), 48(g − 1),
40(g − 1) ,... } and that if p is a prime where p || G|, then p ∈{ 2,..., g, g + 1,
2 g + 1}. For genus 4 this means p ∈{ 2, 3, 5} and so the maximal automorphism
group of a genus 4 curve has order strictly less than 84 (g − 1). In 1895, Wiman
showed10
Proposition 2.11 ([67]) Aut (B) = S5. This is the maximal possible automorphism
group for a genus 4 surface, and Bring’s curve is the only curve to achieve it.
Wiman’s proof was enumerative and produced equations for the curves with a
given automorphism group. He had previously dealt with the hyperelliptic curves
and their automorphism groups and for non-hyperelliptic curves C of genus 4 he
began with the canonical embedding of the curve in P
3 which meant that their
automorphisms could be taken to be collineations, and so forming a subgroup of
PGL
4(C). Wiman’s approach then used the fact (see [33, IV .5.2.2]) that the canonical
embedding of a non-hyperelliptic curve of genus 4 is the complete intersection of an
irreducible cubic surface and a unique quadric surface (which is either irreducible,
or a cone). The uniqueness of the quadric Q means that automorphisms of the curve
become automorphisms of Q. In the case where Q is of full rank we have that it
is isomorphic to P
1× P1, hence we know Aut (C) is isomorphic to a ﬁnite subgroup
of Aut (P1× P1) = C2 ⋉ (PGL2(C)× PGL2(C)) and that using the coordinates of
P1 ×P1 Wiman could express the curve C as an equation of bidegree (3, 3) in terms
of these. In the singular case Q is a quadric cone and by projecting from a point of the
cone meant that C could be expressed as a plane sextic. In both cases Wiman could
write equations for possible genus 4 curves and his strategy was to look at the restric-
tions on these imposed by symmetries of orders 2, 3 and 5. For curves without an order
5 element the maximal order of symmetry group was 72 for Q either a smooth quadric
or cone. Including an order 5 element yielded a maximal symmetry group of order 120
only in the case of the smooth quadric with the resulting curve being Bring’s. In the
case of Bring’s curve the quadric Q is the quadric Q we determined earlier. Different
proofs of Wiman’s result may be found in [ 43, 49].
It is clear from the P4-model that Aut(B) may be realised as projective transforms
via the permutation representation of S5 acting on the subspace ∑
i xi = 0; it is also
clear that it may be be realised as a subgroup of PGL 4(C) via the induced action on
the differentials or equivalently the La ’s. What is non-trivial is the following fact.
Theorem 2.12 ([22]) The A 5 subgroup of Aut(B) can be realised as a group of
collineations in the HC-model, that is, can be realised as a subgroup of PGL3(C).
Proof. We will be explicit about the construction here as this will be proﬁtable later; [8]
explains how this representation follows from [22]. The group A5 has two inequivalent
irreducible three-dimensional representations, one of which is given by ⟨R, S⟩where
10 An English translation of Wiman’s paper has been produced [ 18].
123
Bring’s curve: old and new Page 15 of 46 3
R ..= 1√
5
⎛
⎝
12 2
1 ζ 2 + ζ−2 ζ + ζ−1
1 ζ + ζ−1 ζ 2 + ζ−2
⎞
⎠ , R2 = I,
S ..=
⎛
⎝
1
ζ
ζ−1
⎞
⎠ , S5 = I,( RS)3 = I.
Note the other inequivalent irreducible 3-dimensional representation comes from
replacing ζ in the above with ζ 2 or ζ 3. The invariants of the representation ⟨R, S⟩
(when acting on (X, Y, Z)T via left multiplication) are
i2 =
( X
2
) 2
+
4∑
k=0
( X/2 + Yζ k + Zζ−k
√
5
)2
= 1
2 X 2 + 2YZ ,
i6 =
( X
2
) 6
+
4∑
k=0
( X/2 + Yζ k + Zζ−k
√
5
)6
,
i10 =
( X
2
) 10
+
4∑
k=0
( X/2 + Yζ k + Zζ−k
√
5
)10
,
i15 =
⏐⏐
⏐
⏐
∂{i
2, i6, i10}
∂{X, Y, Z}
⏐⏐
⏐
⏐.
There is a polynomial relation between i
2
15 and i2, i6, i10. In particular the vanishing
of i6 − λi3
2 gives us Dye’s one-parameter family of A5-invariant sextics in P2;t h i s
pencil appears to have ﬁrst been studied by Winger [ 68]. This pencil yields genus 10
curves for generic λ [22].11 The special value of λ = 13/10012 yields a genus 4 curve,
namely Bring’s curve, as we have that
1
12 (100i6 − 13i3
2) = X(Y 5 + Z 5) + (XYZ )2 − X 4YZ − 2(YZ )3 = F(X, Y, Z).
To complete our picture, we use the following result.
Proposition 2.13 The map
U : (x, y) ↦→
(
− y5 + x3 y − 3xy 2 + 1
(y − x2)(y3 − x) ,− y2x − 1
y3 − x
)
is an automorphism of the HC-model, and together with R and S generates the entire
automorphism group S5.
11 A variation on this pencil has been used to explain why Bring’s curve is uniquely deﬁned as an A5-
invariant curve of genus 4, but there is a 1-parameter family of dimension 4A5-invariant principally polarised
abelian varieties, deforming Jac B [48, 69]. The paper [51] gives further interesting representation theoretic
perspectives on Bring’s curve.
12 For λ = 17/180 the curve is of genus 0; for λ = 1/10 the curve is reducible.
123
3 Page 16 of 46 H.W. Braden, L. Disney-Hogg
Proof The proof that U is an automorphism is a simple algebraic veriﬁcation. In order
to ﬁnd this map, we adapted the methods of [10]. To see that⟨R, S, U⟩∼= S5, note that
U is of order 4, for example by checking that it has the orbit a ↦→ c ↦→ b ↦→ d ↦→ a.
As such, U corresponds to an odd permutation under the isomorphism Aut (B) ∼= S5,
and a single odd permutation and all of A5 together generate S5.
By ﬁxing a map from (the normalisation of) the HC-model to theP4-model as we did
in the proof of Proposition 2.9, we have ﬁxed an isomorphism from the automorphism
group of the curve (in the HC-model) toS5, which we shall denoteψ :⟨R, S, U⟩→ S5.
For example, it is simple to verify that we have U 2([X : Y : Z]) =[ X : Z : Y].W es e e
U 2([L1 : L2 : L3 : L4]) =[ L2 : L1 : L4 : L3], and so
U 2([x1 : x2 : x3 : x4 : x5]) =[ x2 : x1 : x4 : x3 : x5],
that is (12)(34). Through similar calculation we can ﬁnd
ψ( R) = (13)(24), ψ( S) = (13425), ψ( U) = (1324).
There are myriad choices that can be made in constructing the birational transformation
(such as the labelling of the coordinates in P3 and the ordering of the rows of A,o r
indeed composing with any automorphism of theP4-model), and changing these would
give different isomorphisms to S5.
As we have previously described, the uniqueness of the quadric Q whose intersec-
tion with a cubic yields the canonical model of the curve leads to an isomorphism of
the automorphism group of the curve and a subgroup of Aut (Q). For Bring’s curve
Q ∼= P1× P1 and we obtain an isomorphism from S5 to a subgroup of Aut(P1× P1) =
Z2 ⋉ (PGL2(C)× PGL2(C)) which we now write down. Let ([u : v],[z : w]) be the
coordinates on P1× P1, then using the birational map constructed in Proposition 2.9
one can conjugate the standard irreducible 4-dimensional representation of S5 on
[x1 : x2 : x3 : x4] to an action on [v1 : v2 :v3 : v4]. The resulting action of (12) is (pro-
jectively)
( v
u
)
↦→
( j −1
−1 − j
)( w
z
)
..= A
( w
z
)
,
( w
z
)
↦→
( −1 j − 1
j − 11
)( v
u
)
..= B
( v
u
)
,
(9)
where j =− ζ 3 − ζ 2 satisﬁes j2 − j − 1 = 0; that is it is the j deﬁned by Dye. One
can show that (34) has the same action, where the other root j′= ζ 3 +ζ 2 + 1 is taken.
One can check that AB = 1 ∈ PGL2(C), consistent with the fact that (12)2 = 1 ∈ S5.
Note the transposition interchanges the two copies of P1, which is the action of the
semi-direct product with Z2. Combining the two transforms one gets that (12)(34)
acts as
[u : v] ↦→[ −v : u], [z : w] ↦→[ −w : z].
123
Bring’s curve: old and new Page 17 of 46 3
This ﬁxes each copy ofP1 and is the antipodal map on each. Moreover, we can calculate
the action of (145) on the copies to be
( v
u
)
↦→
( ζ − ζ 3 − ζ
− ζ 2 − 1 −ζ 2
)( v
u
)
,
( w
z
)
↦→
( ζ 3 + 1 ζ 2
ζ 4 − ζ 3 − ζ
)( w
z
)
.
(10)
As ⟨(12)(34), (145)⟩∼= A5, we discover that the action of A5 does not interchange the
two copies of P1, but odd-parity elements in S5 do. Here A5 is given by the diagonal
embedding in PGL 2(C)× PGL2(C).
