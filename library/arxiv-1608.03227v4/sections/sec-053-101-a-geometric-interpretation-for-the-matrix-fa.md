---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-053-101-a-geometric-interpretation-for-the-matrix-fa
section_title: "A geometric interpretation for the matrix factorization"
section_number: 10.1
pages: 54-56
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
X =


x11
x12
x13
0
x22
x23
0
0
x33

,
a =
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

We assume in this section that all group elements have determinant 1.
Proposition 10.1. If the the following equations hold
a31 = 0
(10.35)
(x11 −x22)a11 + x12a21 = 0
(10.36)
(a−1)33(x11 −x33) −(a−1)32x23 −(a−1)31x13 = 0.
(10.37)
then
Ad−1
a (X) ∈b.
Proof. The ﬁrst two equations (10.35,10.36) imply ((X −x22I3)a)•1 = 0 and hence
(a−1(X −x22I3)a)•1 = 0.
The equation (a−1(X −x11I3))3• = 0 is equivalent to the system consisting of the equation (10.37) and
equation:
(10.38)
(a−1)31x12 + (a−1)32(x22 −x11) = 0.
54
Now let us observe that if a31 = 0 then (a−1)31 = a12a32 and (a−1)32 = −a11a32 thus the equation (10.38)
is equal to a32 times (10.36) modulo a31 and the statement follows.
✷
Let us denote the LHS of (10.36) by f and LHS of (10.37) by g.
Proposition 10.2. The elements a31, f, g form a regular sequence in C[b × G].
Proof. We use the Bruhat cover of the group to show it. Indeed, if a31 = 0 then either a11̸ = 0 or a21̸ = 0.
Let’s treat the case a11̸ = 0 ﬁrst. then either (a−1)32̸ = 0 and a31, f/a11, g/(a−1)32 is regular or (a−1)33̸ = 0
and a31, f/a11, g/(a−1)33 is regular. The second case a21̸ = 0 is analogous since then either (a−1)31̸ = 0 and
a31, f/a21, g/(a−1)31 is regular or (a−1)33̸ = 0 and a31, f/a21, g/(a−1)33 is regular. Since we show regularity
in each aﬃne chart the statement follows.
✷
Let us point out that the proof of the proposition 10.1 implies that the ideal I′
12 = (a31, f, g) ⊂C[g × G]
deﬁnes the subvariety that consists of pairs (X, g) such that
Adg(X) −diag(X22, X33, X11) ∈n.
The later matrix equation if B2-invariant hence the ideal I′
12 is B2-invariant too.
The ideal I12 = (a31, f, g) ⊂C[X 2] contains the potential W and because of regularity of the sequence
and of B2-invariance we have, according to the Lemma 3.4 the following well-deﬁned matrix factorization
¯C12 = KW (I12) ∈MFsc
B2(X 2, W).
Indeed, the regularity of (a31, f, g) implies that the Koszul complex K(a31, f, g) is homotopic to C[X 2]/I12
supported in the zeroth homological degree. Thus the conditions of the Lemma 3.4 are satisﬁed and there is
a unique matrix factorization KW (I12) that extends K(a31, f, g).
Let us deﬁne the following elements of C[b × G]:
h = (a−1)32x23 + (a−1)33(x33 −x22),
k = a11(x11 −x33) + a21x12 + a31x13.
Proof of the proposition below is parallel to the propositions above and we leave them for reader to check
Proposition 10.3. We have
(1) The conditions (a−1)31 = 0, h = 0, k = 0 imply Ad−1
a (X) ∈b.
(2) The sequence (a−1)31, h, k is regular in C[b × G].
Let I21 = ((a−1)31, h, k) ⊂C[X 2] the ideal. Then analogously to the previous case we can deﬁne complex
¯C21 := KW (I21) ∈MFsc
B2(X 2, W).
The main result of this section is the formula for the matrix factorization for the braid on three strands
with two crossings:
Lemma 10.4. We have
¯C(1)
+ ¯⋆¯C(2)
+ = ¯C12,
¯C(2)
+ ¯⋆¯C(1)
−= ¯C21.
55
