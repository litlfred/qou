---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-001-31-the-automorphism-group-f4-of-the-exceptional
section_title: "The automorphism group F4 of the exceptional Jordan algebra and its Lie algebra f4"
section_number: 3.1
pages: 6-8
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
algebra and its Lie algebra f4
About the same time Pascual Jordan introduced his algebras Ruth Moufang
studied her non-Desarguian (octonionic) projective plane P O2. Sixteen years
later, in 1949, Jordan noticed that the points of P O2 are given by the one-
dimensional (trace-one) idempotents of the exceptional Jordan algebra J which
are also the pure states of J.
A glimpse on the automorphism group F4 ={g :J→J;g(X◦Y ) =gX◦gY}
is provided by displaying the stability subgroup of one such idempotent
E1 =


1 0 0
0 0 0
0 0 0



or E2 =


0 0 0
0 1 0
0 0 0

, or E3 =


0 0 0
0 0 0
0 0 1



. (3.1)
Noting that F4 should preserve the unit element 1 I = E1 +E2 +E3 of J we
deduce that this stability subgroup should also preserve E2 +E3 and hence the
square of any traceless element of H2(O),
X 2 = (ξ2 +|x|2)


0 0 0
0 1 0
0 0 1

 for X =


0 0 0
0 ξ x
0 ¯x −ξ

 (3.2)
6
and coincides with Spin (9) (the simply connected double covering of the orthog-
onal group SO(9) in nine dimensions). It follows that the octonionic projective
(Moufang) plane2 coincides with the homogeneous space
PO2 =F4/Spin(9). (3.3)
This allows to ﬁnd, in particular, the dimension of F4 (over the reals):
dim (F4) = dim (Spin(9)) + dim (PO2) = 36 + 16 = 52. (3.4)
With a little more work one recovers the Lie algebra f4 as a direct sum of the
Lie algebra so(9) and its 16-dimensional spinor representation S9:
f4≃so(9) ˙+S9 (S9 =S+
8 ˙+S−
8 ) (3.5)
which yields (1.1) and can be interpreted in “purely octonionic” terms:
f4∼=so (O⊕ R) ˙+ O2 =so (O) ˙+ O3. (3.6)
Finally, we turn to a description that will also apply to higher rank excep-
tional Lie algebras. According to [BS] the Lie algebra of derivations on H3(K)
– the set of hermitian 3 × 3 matrices over any alternative composition algebra
K – can be presented as a sum
Der (H3(K))∼= Der (K) ˙+sa3(K) (3.7)
wheresa3(K) is the set of antihermitean traceless 3× 3 matrices with entries in
K:
sa3(K) ={X∈ K [3]; X∗ =−X, trX = 0}. (3.8)
Given an element X∈sa3(K) there is a derivation adX of H3(K) given by
adX(Y ) = [X,Y ] for ∀Y ∈H3(K). (3.9)
The subspace Der (K) in the right-hand side of (3.7) is always a Lie algebra, but
sa3(K) is not unless K is commutative and associative (in which case Der ( K)
vanishes). Nevertheless, there is a formula for the bracket in Der [H3(K)] which
applies in every case. Given D,D′∈ Der [H3(K)] and X,Y ∈sa3(K) it reads:
[D,D′] =DD′−D′D, [D,adX] =adDX,
[adX,adY ] =ad[X,Y ]0 + 1
3
3∑
i,j=1
Dxij,yij (3.10)
where D acts on
X =


x11 x12 x13
x21 x22 x23
x31 x32 x33


2The octonionic quantum mechanics in the Moufang plane is studied in [GPR].
7
componentwise, [X,Y ]0 is the trace-free part of the commutator [ X,Y ], and
Dx,y is the derivation deﬁned by (2.4).
Summarizing, we have the following expressions for the compact form of f4
(which also appears as the isometry algebra of the Riemannian manifold PO2):
f4∼= DerH3(O)∼= Der (O) ˙+sa3(O) (3.11)
(a special case of (3.7)). Here Der ( O) is the 14-dimensional exceptional Lie
algebra g2.
