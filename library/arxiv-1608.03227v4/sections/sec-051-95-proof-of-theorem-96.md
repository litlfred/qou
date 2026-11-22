---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-051-95-proof-of-theorem-96
section_title: "Proof of theorem 9.6"
section_number: 9.5
pages: 52-54
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
g12 = ||aij||, g23 = ||bij|| and g13 = ||cij|| so that
δ1a11 = a21,
δ1a12 = a22,
δ2a12 = −a11,
δ2a22 = −a21,
(9.31)
δ2b11 = b21,
δ2b12 = b22,
δ3b12 = −b11,
δ3b22 = −b21,
(9.32)
δ1c11 = c21,
δ1c12 = c22,
δ3c12 = −c11,
δ3c22 = −c21.
(9.33)
We also introduce X′ = Adg−1
12 X:
x′
−1 = −2a11a21x0 −a2
21x1 + a2
11x−1
x′
0 = (a12a21 + a11a22)x0 + a21a22x1 −a11a12x−1,
x′
1 = 2a12a22x0 + a2
22x1 −a2
12x−1.
For computation of convolution C+ ⋆C−we need to analyze the pull-back matrix factorization:
C+−:= π◦∗
12(C+) ⊗π◦∗
23(C−) =


x−1
y1 −y2a2
11
θ1
2x0a11 + x1a21
a21y2
θ2
x′
−1
y2 −y3b2
11
θ3
2x′
0b11 + x′
1b21
b21y3
θ4


′
δ1θ1 = −2a11θ2,
δ2θ3 = −2b11θ4,
we used a shortcut notation [−]′ = [−]⟨0, −1, −1⟩, and [−]⟨0, −1, −1⟩stands for the shift of the action of the
torus (C∗)3 = T (1) × T (2) × T (3).
Next we get rid of y2, that is, we need to ﬁnd a matrix factorization on g × G × n that is homotopy
equivalent to C+−as the matrix factorization over π◦∗
13(C[X ◦
2 ]). We use the row transformations together
with the contraction of the injective diﬀerential to do that. The result of the row transformation is the LHS
of the equation below:


x−1
y1 −y3a2
11b2
11
θ′
1
2x0a11 + x1a21
a21b2
11y3
θ′
2
0
y2 −y3b2
11
θ3
2x′
0b11 + x′
1b21
b21y3
θ4


′
∼


x−1
y1 −y3a2
11b2
11
θ′
1
2x0a11 + x1a21
a21b2
11y3
θ′
2
2x′
0b11 + x′
1b21
b21y3
θ4


′
,
where
θ′
1 = θ1 + a2
11θ3,
θ′
2 = θ2 −a21θ3,
so that
δ1θ′
1 = −2a11θ′
2,
δ2θ′
1 = −2b11a2
11θ4,
δ2θ′
2 = 2b11a21θ4.
After performing two row operations with the help of the relation
2x′
0b11 + x′
1b21 = −x−1(b11a11a12 + c11a12) + c21(2x0a12 + x1a22) + b11a22(2x0a11 + x1a21).
we ﬁnd
C+−∼


x−1
y1 −y3c2
11
θ′′
1
2x0a11 + x1a21
c21b11y3
θ′′
2
(2x0a12 + x1a22)c21
b21y3
θ4


′
=


x−1
y1 −y3c2
11
θ′′
1
˜x0
c21b11y3
θ′′
2
˜˜x0 c21
b21y3
θ4


′
where
θ′′
1 = θ′
1 −(b11a11a12 + c11a12)θ4,
θ′′
2 = θ′
2 + a22b11θ4,
52
so that
δ1θ′′
1 = −2a11θ′′
2 −2a12c21θ4,
δ2θ′′
2 = c21θ4.
(9.34)
The Borel group B(2) acts trivially on the ﬁrst line of the last matrix factorization thus to complete our
computation of C+ ⋆C−we need to analyze the complex composed of the last two lines of the above Koszul
complex:
C =
ñ
˜x0
c21b11y3
θ′′
2
˜˜x0 c21
b21y3
θ4
ô
More precisely, we need to study the C∗-invariant part of the complex CE(2)
n (C). First let us notice that
the ring R := C[X 3] factors as R′ × ¯π∗
13(C[X 2]) where R′ = C[G] and the second factor is B(2)-invariant
and thus CE(2)
n (C) = CE(2)
n (C′) ⊗¯π13(X 2) where C′ is the matrix factorization C consider as the matrix
factorization over R′. Let us depict the complex CE(2)
n (C′)T (2) below
[θ′′
2; 0]
[1; 1]
[θ′′
2θ4; 1]
[θ4; 2]
[θ′′
2; −2] e∗
[1; −1] e∗
[θ′′
2θ4; −1] e∗
[θ4, 0] e∗
where e∗is the basis of n∗= Hom(n, C) and [α; k] stands for R[k]α which is the part of the ring of C∗
weight k . In the picture the dashed arrows are the Chevalley-Eilenberg diﬀerentials for H∗(n, •).
Note that H∗(b, R⟨1⟩) = 0 hence the blue and red dashed arrows in the diagram are isomorphisms and
we can contract them but some new morphisms would appear after we perform the contraction.
Indeed, if we contract red dashed arrow we obtain four correction morphisms. The ﬁrst correction mor-
phism d1 is obtained by following blue arrows (dashed arrow in reverse direction) starting at R[0]θ4e∗and
ending at R[0]θ′′
2:
d1 = b21y3δ−1
2 (2x0a11 + x1a21) = b21y3(2x0a12 + x1a22).
Thus we obtained the diﬀerential that goes in the direction opposite of the diagonal green dashed arrow.
The another corrections diﬀerentials have the following origins and destinations:
d2 : R[0]θ4e∗→R[2]θ4,
d3 : R[−2]θ′′
2e∗→R[0]θ′′
2,
d4 : R[−2]θ′′
2e∗→R[2]θ4.
Similarly, contraction of the blue dashed arrow results yields four correction morphisms. The ﬁrst cor-
rection morphism d5 is obtained by following red arrows (dashed arrow in reverse direction) starting at at
R[0]θ4e∗and ending at R[0]θ′′
2:
d5 = (2x0a11 + x1a21)δ−1
2 (b21y3) = b11y3(2x0a11 + x1a21).
53
Thus we obtained another diﬀerential that goes in the direction opposite of the direction of diagonal dashed
green arrow. The another corrections diﬀerentials have the following origins and destinations:
d6 : R[0]θ4e∗→R[2]θ4,
d7 : R[−2]θ′′
2e∗→R[0]θ′′
2,
d8 : R[−2]θ′′
2e∗→R[2]θ4.
Finally, let us notice that since H0(b, R⟨2⟩) = H1(b, R) = 0, H1(b, R⟨2⟩) = H0(b, R) = C[c, x, y] we see that
Chevalley-Eilenberg diﬀerential: d10 : R[2]θ4 →R[0]θ4e∗is injective and Chevalley-Eilenberg diﬀerential:
d11 : R[0]θ′′
2 →R[−2]θ′′
2e∗is surjective. Thus we can perform contraction along these diﬀerentials and obtain
two term complex consisting of H1(b, R⟨2⟩) = C[c, x, y], H0(b, R) = C[c, x, y] and diﬀerentials between them.
Let us point out that the diﬀerentials d2, d3, d4, d6, d7, d9 do not result in any correction diﬀerential after the
contraction since none of these diﬀerentials ends on the target of the arrows d10, d11.
Thus the only diﬀerentials in our ﬁnal complex are the following. The diﬀerential that starts at H1(b, R⟨2⟩)
and ends at H0(b, R) is the sum of d2 and d5:
d2 + d5 = y3(2x0c11 + x1c21).
The diﬀerential going in the reverse direction is the green arrow diﬀerential caused by (9.34) that is it is just
a multiplication by c21. Thus we have shown that
CEn(2)(C+−)T (2) ∼C∥.
