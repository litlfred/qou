---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-006-35-the-character-varieties-of-twist-knots-a-recu
section_title: "The character varieties of twist knots: a recursive description"
section_number: 3.5
pages: 8-12
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
a recursive description of the SL 2(C)-character variety of two–bridge knots and apply it
to obtain an explicit description of the SL 2(C)-character variety of torus knots. Here we
apply his method to obtain an explicit recurrent descriptio n of the SL 2(C)-character va-
riety of twist knots. This is the main di ﬀerence with the description given by Hoste and
Shanahan [HS04].
Let n = 2m or 2m + 1, recall that Π(J(2, n)) =⟨x, y| Ωmx = yΩm⟩, where Ωm is a word
in x, y (see Facts 1–2).
Notation. Let γ∈ Π(J(2, n)). Following a notation introduced in [CGLS87], we let
Iγ : X(Π(J(2, n)))→ C
be the trace–function deﬁned by Iγ : ρ↦→tr(ρ(γ)).
Let a = Ix, b = Ixy and recall the following useful formulas for A, B, C∈ SL2(C):
(13) tr( A−1) = tr(A) and tr(AB) = tr(BA),
(14) tr( AB) + tr(A−1B) = tr(A)tr(B),
(15) tr( ABA−1B−1) =−2− tr(A)tr(B)tr(AB) + (tr(A))2 + (tr(B))2 + (tr(AB))2.
As x and y are conjugate elements in Π(J(2, n)), we have Iy = a = Ix. If γ is a word
in the letters x and y, then Iγ can always be expressed as a polynomial function in a and
8
b. For example, combining the usual Formulas (13), (14) and (15), one can easily observe
that for w = [y, x−1] = yx−1y−1x, we have
(16) Iw =−2− a2b + 2a2 + b2.
The character variety of Π(J(2, n)) is thus parametrized by a and b. Here is a practical
description of it:
(1) We ﬁrst consider the abelian part of the character variet y. It is easy to see that the
equation a2− b− 2 = 0 determines the abelian part of the character variety of any
knot group.
(2) Next, consider the non-abelian part of the character var iety of Π(J(2, n)), suppose
that the length of the word Ωm is 2k + 2 (we know that the length of Ωm is even).
According to [Le94, Theorem 3.3.1], the non–abelian part of the character variety
of Π(J(2, n)), for n = 2m or 2m + 1, is determined by the polynomial equation:
Φm(a, b) = 0,
where
Φm(a, b) = IΩm− IΩ′
m +··· + (−1)kIΩ(k)
m
+ (−1)k+1.
Here we adopt the following notation: if Λis a word then Λ′ denotes the word
obtained from Λby deleting the two end letters.
Let us give the two simplest examples to illustrate this gene ral result and ﬁnd again
some well–known facts.
Example 1. The trefoil knot 31 is the twist knot J(2, 2). With the above notation, one has
Ω1 = x−1y−1. Thus applying Le’s method, the non–abelian part of the char acter variety is
given by the polynomial equation:
Φ1(a, b) = Ix−1y−1− 1 = 0,
which reduces to
b = 1.
Example 2. The ﬁgure eight knot 4 1 is the twist knot J(2,−2). With the above notation,
one has Ω−1 = x−1yxy−1. Thus, the non–abelian part of the character variety of the g roup
of the ﬁgure eight knot is given by the polynomial equation:
Φ−1(a, b) = Ix−1yxy−1− Iyx + 1 = 0,
which reduces, using Equation (16), to:
2a2 + b2− a2b− b = 1.
Now, we turn back to the general case and only consider the twi st knot J(2, 2m) (see
Item (2) of Remark 2). Recall that (see Remark 1):
(17) Π(J(2, 2m)) =⟨x, y| Ωmx = yΩm⟩, where Ωm =







wm if m < 0,
x−1(
w)m−1y−1 if m > 0.
Here w = [y, x−1] and w = [y−1, x] and observe that the length of the word Ωm is 4m, if
m < 0, and 4m− 2, if m > 0.
Our method is based on the fact that the wordΩm in the distinguished Wirtinger presen-
tation (17) of Π(J(2, 2m)) presents a particularly nice “periodic” property. This property is
discussed in the following obvious claim.
Claim 6. For m∈ Z∗, we have
Ω(4)
m =







wm+2 if m ⩽−2,
x−1(
w)m−3y−1 if m /greaterorequalslant3.
9
Based on Claim 6, for m /greaterorequalslant0, we adopt the following notation:
S +
m = IΩm+2, T +
m = I(Ωm+2)′, U +
m = I(Ωm+2)′′ and V +
m = I(Ωm+2)′′′,
and similarly, for m ⩽0,
S−
m = IΩm−2, T−
m = I(Ωm−2)′, U−
m = I(Ωm−2)′′ and V−
m = I(Ωm−2)′′′.
The Cayley–Hamilton identity applied to the matrix A2∈ SL2(C) gives
Am (
A4− (tr A2)A2 + 1
)
= 0.
Write c(a, b) = IΩ2; thus for m /greaterorequalslant0, we have
S +
m+4− c(a, b)S +
m+2 + S +
m = 0
and same relations for T +
m, U +
m and V +
m hold. Similarly, we have
S−
m−4− c(a, b)S−
m−2 + S−
m = 0
and same relations for T−
m, U−
m and V−
m also hold.
If we write R±
m = S±
m− T±
m + U±
m− V±
m for m∈ Z, then above computations can be
summarized in the following claim which give us a recursive relation for (R±
m)m∈Z.
Claim 7. The sequence of polynomials(R±
m(a, b))
m∈Z satisﬁes the following recursive rela-
tion:
(18) R±
m±4− c(a, b)R±
m±2 + R±
m = 0.
In Equation (18), using Formula (14) and Equation (16), we have:
c(a, b) = Iw2 = (Iw)2− 2 = 2 + 4a2b− 8a2− 4b2 + a4b2− 4a4b− 2a2b3 + 4a4 + 4a2b2 + b4.
Let v be such that:
(19) v + v−1 = c(a, b).
For m∈ Z∗, we distinguish four cases to derive helpful formulas for Φm in the case of
twist knots.
• Case 1: m > 0 is even.
Let m = 2l, with l > 0, and set ri = R2i. Then
ri+2 = c(a, b)ri+1− ri, for i /greaterorequalslant0.
As we have supposed that v + v−1 = c(a, b) and following a standard argument in
combinatorics (see e.g. [Mer03, p. 322]), we have the general formula (which can
also be proved by induction) ri = Mvi + Nv−i, where M and N are determined by
the initial conditions: 






r0 = R+
0 = M+
0 + N+
0
r1 = R+
2 = M+
0 v + N+
0 v−1
Further observe that:
r0 = IΩ2− IΩ′
2 + IΩ′′
2− IΩ′′′
2 = Ix−1
wy−1− Iw + b− 1.
So, we have
Φm+2 = R+
m + R+
m−2 +··· + R+
0
= rl +··· + r0
=
l∑
i=0
(M+
0 vi + N+
0 v−i)
= M+
0
vl+1− 1
v− 1 + N+
0
v−l−1− 1
v−1− 1 .
10
• Case 2: m < 0 is even.
Let m =−2l, with l > 0, and set ri = R−
−2i, i /greaterorequalslant0. Similar to the ﬁrst case,
ri+2 = c(a, b)ri+1− ri, for i /greaterorequalslant0.
The initial conditions are







r0 = R−
0 = M−
0 + N−
0
r1 = R−
−2 = M−
0 v + N−
0 v−1
Further observe that:
r0 = IΩ−2− IΩ′
−2 + IΩ′′
−2− IΩ′′′
−2 = Iw2− Iy(
w)−1x + Iw− b.
Thus, we have
Φm−2 = R−
m + R−
m+2 +··· + R−
0 + 1
= rl +··· + r0 + 1
=
l∑
i=0
(M−
0 vi + N−
0 v−i) + 1
= M−
0
vl+1− 1
v− 1 + N−
0
v−l−1− 1
v−1− 1 + 1.
• Case 3: m > 0 is odd.
Let m = 2l + 1, with l > 0, and set ri = R+
2i+1, i /greaterorequalslant0. Similar to the ﬁrst case,
ri+2 = c(a, b)ri+1− ri, for i /greaterorequalslant0.
The initial conditions are







r0 = R+
1 = M+
1 + N+
1
r1 = R+
3 = M+
1 v + N+
1 v−1
Further observe that:
r0 = IΩ3− IΩ′
3 + IΩ′′
3− IΩ′′′
3 = Ix−1(
w)2y−1− I(w)2 + Ixwy− Iw.
Thus,
Φm+2 = R+
m + R+
m−2 +··· + R+
1 + b− 1
= rl +··· + r0 + b− 1
=
l∑
i=0
(M+
1 vi + N+
1 v−i) + b− 1
= M+
1
vl+1− 1
v− 1 + N+
1
v−l−1− 1
v−1− 1 + b− 1.
• Case 4: m < 0 is odd.
Let m =−2l− 1, with l > 0, and set ri = R−
−2i−1, i /greaterorequalslant0. Similar to the ﬁrst case,
ri+2 = c(a, b)ri+1− ri, for i /greaterorequalslant0.
The initial conditions are







r0 = R−
−1 = M−
1 + N−
1
r1 = R−
−3 = M−
1 v + N−
1 v−1
Further observe that:
r0 = IΩ−3− IΩ′
−3 + IΩ′′
−3− IΩ′′′
−3 = Iw3− Iy(
w)−2 x + Iw2− Iy−1w−1x−1.
11
Similarly to the previous case, we have:
Φm−2 = R−
m + R−
m+2 +··· + R−
−1 + Iw− b + 1
= rl +··· + r0 + Iw− b + 1
=
l∑
i=0
(M−
1 vi + N−
1 v−i) + Iw− b + 1
= M−
1
vl+1− 1
v− 1 + N−
1
v−l−1− 1
v−1− 1 − a2b + 2a2 + b2− b− 1.
If we adopt the following notation:
(20) M±
j (v, l) = M±
j
vl+1− 1
v− 1 and N±
j (v, l) = N±
j
v−l−1− 1
v−1− 1 , j = 0, 1,
then we summarize our computations in the following proposition.
Proposition 8. The polynomial equation which describes the character vari ety of the
group of the twist knot J (2, n), for n = 2m or 2m + 1, is given by Φm(a, b) = 0 where
the sequence (Φm(a, b))m∈Z is recursively deﬁned as follows:
Φ0(a, b) = 1, Φ1(a, b) = b− 1, Φ−1(a, b) =−a2b + 2a2 + b2− b− 1,
and for m > 1
(21) Φm+2(a, b) =







M+
0 (v, l) + N+
0 (v, l) if m = 2l is even,
M+
1 (v, l) + N+
1 (v, l) + b− 1 if m = 2l + 1 is odd,
and
(22) Φ−m−2(a, b) =







M−
0 (v, l) + N−
0 (v, l) + 1 if m = 2l is even,
M−
1 (v, l) + N−
1 (v, l)− a2b + 2a2 + b2− b− 1 if m = 2l + 1 is odd.
Here v is deﬁned in Equation (19) and M±
k (v, l), N±
k (v, l) in Equation (20).
Remark 8. Observe that in Equations (21) and (22), the part M±
k (v, l) + N±
k (v, l) is the “re-
cursive” part. In Equation (21) the part b− 1 corresponds to Φ1(a, b), and in Equation (22)
the part−a2b + 2a2 + b2− b− 1 corresponds to Φ−1(a, b), see Examples 1 and 2.
4. R eview on the non –abelian Reidemeister torsion and twisted polynomial torsion
