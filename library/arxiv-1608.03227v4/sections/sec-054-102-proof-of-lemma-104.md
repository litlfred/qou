---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-054-102-proof-of-lemma-104
section_title: "Proof of Lemma 10.4"
section_number: 10.2
pages: 56-59
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
The second equation is
obtained from the ﬁrst by applying the involution D.
Since ¯C(2)
+ = Ind1,2( ¯C+) we can use the proposition 8.4 and the corrections for the B2 equivariant structure
from the subsection 8.3 to proceed with our computation of ¯C(1)
+ ¯⋆¯C(2)
+ .
First we introduce the matrices
g12 =


a11
a12
a13
a21
a22
a23
a31
a32
a33

,
g23 =


1
0
0
0
b22
b23
0
b23
b33


g13 =


c11
c12
c13
c21
c22
c23
c31
c32
c33

.
They satisfy the relation
g13 = g12g23.
Polynomials of the entries of the matrices a, c, X and Y span the space of regular functions on the space
X3(G3, G2,3).
By the proposition 8.3 ¯C(1)
+ ¯⋆¯C(2)
+ = ¯π13∗(CEn(2)
2 ((¯π∗
12 ⊗B2 ¯π∗
23)(( ¯C(1)
+ ) ⊠¯C(2)
+ ))) where
¯π12 : X 3(G3, G2,3) →X 2(G3),
¯π23 : X 3(G3, G2,3) →X 2(G2),
¯π13 : X 3(G3, G2,3) →X 2(G3).
We introduce the matrices
˜X2 = Adg−1
12 X = ||˜xij||,
˜Y2 = Adg23Y = ||˜yij||.
The tensor product (¯π12 ⊗B2 ¯π23)∗( ¯C(1)
+ ⊠¯C(2)
+ ) in the above tensor product is the Koszul complex:
C12 =


a31
∗
θ0
(x11 −x22)a11 + x12a21
∗
θ1
a32
∗
θ2
(˜x22 −˜x33)b22 + ˜x23b32
∗
θ3


Since
g−1
23 =


1
0
0
0
b33
−b23
0
−b23
b22

,
it turns out that a31 = c31. Thus we can use the row operations to remove c31 from the other rows of
C12. After completing the process we obtain the matrix factorization C′
12 with last last three rows equal
to the rows of C12 with c31 = a31 = 0 and the ﬁrst row matching with the row of C12 that contains the
relation (10.35). The last row is B(2)
2
invariant hence for our computation of CEn(2)
2 (C12) we only need to
analyze the part of the complex C′
12 that consists of the last three lines:
C′′
12 =


(x11 −x22)a11 + x12a21
∗
θ1
a32
∗
θ2
(˜x22 −˜x33)b22 + ˜x23b32
∗
θ3

=


(x11 −x22)c11 + x12c21
∗
θ1
b33c32 −b32c33
∗
θ2
(˜x22 −˜x33)b22 + ˜x23b32
∗
θ3


The ﬁrst two rows come from the (1,2)-crossing and the second row comes from the (2,3)-crossing. It turns
out that the ﬁrst row of C′′
12 matches the row of C12 that contains the relation (10.36) and it is B(2)
2 -invariant.
So complete our computation of CEn(2)
2 (C12)T (2) we have to simplify only the remaining two rows:
C =
ñ
b33c32 −b32c33
∗
θ2
(˜x22 −˜x33)b22 + ˜x23b32
∗
θ3
ô
=
ñ
κ2
∗
θ2
κ3
∗
θ3
ô
56
where
κ2 = a32 = b33c32 −b32c33,
κ3 = (˜x22 −˜x33)b22 + ˜x23b32.
To write out our Chevalley-Eilenberg complex we need to explain the B2-equivariant structure on C and
it is done below. Denote the elements of Borel group B(2)
2
as
h2 =


1
0
0
0
β22
β23
0
0
β−1
22


Its action is
g12 7→g12h−1
2 ,
g23 7→h2g23,
˜X2 7→Adh2 ˜X2.
The weights of the action of diag(0, 1, −1) ∈Lie(B(2)
2 ) on the r.h.s. elements in the Koszul rows of C are -1
and 1 respectively, hence the weights of θ2 and θ3 are 1 and -1.
It remains to establish the action of β23 denoted by δ2. One way to ﬁgure out this action is to use formulas
(8.29) and (8.30) to ﬁx the equivariant structure on C12 and then follow up the changes of this equivariant
structure as do our reduction from C12 to C. However, we choose a diﬀerent method: we just show that
there is a unique strongly B2-equivariant structure on C and compute it explicitly.
The element κ2 is δ2-invariant. The variation δ2κ3 can be computed by brute force, but since we are
interested in it being proportional to the second element, we use an indirect computation. Present ˜X2 as a
sum of the upper-triangular and strictly lower-triangular parts:
˜X2 = ˜X2,+ + ˜X2,−−.
Note that
κ3b32 = −(Adg−1
23
˜X2,+)32.
while δ2b32 = 0, so
δ2κ3 = −δ2(Adg−1
23
˜X2,+)32/b32.
The matrix
Adg−1
23
˜X2 = Adg−1
23 Adg−1
12
˜X1 = Adg−1
13
˜X1
is Borel-invariant, hence
δ2κ3 = δ2(Adg−1
23
˜X2,−−)32/b32.
A direct computation shows that
(Adg−1
23
˜X2,−−)32 = b2
22( ˜X2,−−)32 = b2
22˜x32.
The formulas for action of B(2) imply that δ2˜x32 = 0, while δ2b22 = b32, so
δ2κ3 = 2˜x32b22,
while
˜x32 = a32 ((x11 −x22)a12a21 + a21a22x12
+(x33 −x22)(a11a22 −a12a21) + a32(a21x13 −a11x23))
Since the Koszul diﬀerential κ2θ2 + κ3θ3 must remain Borel-invariant, it follows that
(10.39)
δ2θ2 = −2b22 ((x11 −x22)a12a21 + a21a22x12
+(x33 −x22)(a11a22 −a12a21) + a32(a21x13 −a11x23)) θ3
57
Similarly to the case of two strands we have tensor product decomposition R = X 3 = R′ ⊗¯π∗
13(C[X 2])
where R′ = C[G2,3] = C[G2] is the factor with non-trivial B(2)
2 -action.
Thus we can use the equality
CEn(2)
2 (C)T (2) = CEn(2)
2 (C′)T (2) ⊗¯π∗
13(C[X3]) were C′ is the complex C considered as the matrix factorization
of R′-modules.
The complex of T (2)-invariant part of the complex CEn(2)
2 (C′) has the following shape:
[θ2; 0]
[1; 1]
[θ2θ3; 1]
[θ3; 2]
[θ2; −2] e∗
[1; −1] e∗
[θ2θ3; −1] e∗
[θ3, 0] e∗
The shape of the complex is identical to the shape of the complex from the proof of the theorem 9.6. Thus
we can perform the same sequence of contractions as in the proof of the theorem 9.6. As we have seen in the
proof of theorem 9.6, at the end of our contraction process, all vertices of the complex except two connected
by the green dashed arrow can be contracted to 0 and the vertices R[0]θ3e∗
3 to H1(P1, O(−2)) ⊗¯π∗
13(C[X2]),
R[0]θ2 to H0(P1, O) ⊗¯π∗
13(C[X2]).
Thus at the end we obtain a two term Koszul complex and as we have seen previously all of the new
correction diﬀerentials in the ﬁnal complex will be running in the direction opposite to the direction of the
green arrow. Let’s study the diﬀerential that induced by the green arrow in our ﬁnal complex.
The target of our diﬀerential is H1(P1, O(−2)) ⊗¯π∗
13(C[X2]) = H1
Lie(n, R⟨−2⟩) ⊗¯π∗
13(C[X2]), hence we
can replace the coeﬃcients of the diﬀerential by the expressions that are homologous with respect to the
diﬀerential δ2. Below we take advantage of this observation. Indeed, note that
δ2b22 = b32,
δ2b23 = b33,
so, ﬁrst, δ2(b2
22) = 2b22b32, hence b22b32 is exact and, second, δ2(b22b23) = b32b23 + b22b33, hence in view of
b22b33 −b23b32 = 1 we ﬁnd b22b33 ∼1
2. As a result,
(10.40)
b22


a11
a12
a13
a21
a22
a23
a31
a32
a33

= g13b22g−1
23 ∼g13


1
0
0
0
1
2
∗
0
0
∗

=


c11
1
2c12
∗
c21
1
2c22
∗
c31
1
2c32
∗


Note that in the expression (10.39) each term has a product of an element from the ﬁrst column and the
second column of the matrix g12, also the ﬁrst column of g13 = c is equal to the ﬁrst column of g12 = a. Thus
we can combine the last observation with (10.40) to see that the diﬀerential induced by the green arrow is
homologous to
−

(x11 −x22)c12c21 + c21c22x12 + (x33 −x22)(c11c22 −c12c21) + c32(c21x13 −c11x23)

58
Since this is the third condition of (10.37) we have shown that the matrix factorization ¯C(1)
+ ¯⋆¯C(2)
+ is actually
an element of MFsc
B2(X 2, W) and its positive part in the sense of Lemma 3.4 is a Koszul complex for the
regular sequence (c31, f, g). Hence by the lemma 3.6 there is an isomorphism between ¯C(1)
+ ¯⋆¯C(2)
+
and ¯C12.
