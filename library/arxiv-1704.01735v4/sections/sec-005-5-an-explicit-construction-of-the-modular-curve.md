---
doc_id: arxiv-1704.01735v4
doc_title: "Modular curves, invariant theory and E8 Lei Yang"
section_id: sec-005-5-an-explicit-construction-of-the-modular-curve
section_title: "An explicit construction of the modular curve X(13)"
section_number: 5
pages: 1-8
source_pdf: 1704.01735v4.pdf
source_sha256: 3935747ae9291f76
doc_brief: "Modular curves, invariant theory and E8 Lei Yang — The E8 root lattice can be constructed from the modular curve X(13) by the invariant theory for the simple group PSL(2 , 13)."
---
1. Introduction
The E8 root lattice (see [14]) occurs in: the equation of the E8-singularity
(theory of singularities), the Barlow surface, which is homeomorph ic but not
diﬀeomorphic to CP2#8CP
2
(diﬀerential topology of 4-manifolds), and the
automorphism group of the conﬁguration of 120 tritangent planes of Bring’s
curve (representation theory and classical algebraic geometry) (see section
two for more details).
In the present paper, we will give a diﬀerent relation which connects E8
with the modular curve X(13). We will show that the E8 root lattice can be
constructed from the modular curve X(13) by the invariant theory for the
simple group PSL(2 , 13).
Let us begin with the invariant theory for PSL(2 , 13). Recall that the
six-dimensional representation (the Weil representation) of the ﬁnite simple
1
group PSL(2 , 13) of order 1092, which acts on the ﬁve-dimensional projec-
tive space P5 = {(z1, z2, z3, z4, z5, z6) : zi ∈ C (i = 1 , 2, 3, 4, 5, 6)}. This
representation is deﬁned over the cyclotomic ﬁeld Q(e
2πi
13 ). Put
S = − 1√
13








ζ 12 − ζ ζ 10 − ζ 3 ζ 4 − ζ 9 ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 6 − ζ 7
ζ 10 − ζ 3 ζ 4 − ζ 9 ζ 12 − ζ ζ 2 − ζ 11 ζ 6 − ζ 7 ζ 5 − ζ 8
ζ 4 − ζ 9 ζ 12 − ζ ζ 10 − ζ 3 ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 2 − ζ 11
ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 6 − ζ 7 ζ − ζ 12 ζ 3 − ζ 10 ζ 9 − ζ 4
ζ 2 − ζ 11 ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 3 − ζ 10 ζ 9 − ζ 4 ζ − ζ 12
ζ 6 − ζ 7 ζ 5 − ζ 8 ζ 2 − ζ 11 ζ 9 − ζ 4 ζ − ζ 12 ζ 3 − ζ 10








and
T = diag(ζ 7, ζ11, ζ8, ζ6, ζ2, ζ5)
where ζ = exp(2πi/13). We have
S2 = T 13 = (ST )3 = 1. (1.1)
Let G = ⟨S, T ⟩, then G ∼
= PSL(2, 13). We construct some G-invariant poly-
nomials in six variables z1, . . . , z6. Let
w∞ = 13A2
0, w ν = (A0 +ζ νA1 +ζ 4νA2 +ζ 9νA3 +ζ 3νA4 +ζ 12νA5 +ζ 10νA6)2
(1.2)
for ν = 0, 1, . . . ,12, where the senary quadratic forms (quadratic forms in six
variables) Aj (j = 0, 1, . . . ,6) are given by























A0 = z1z4 + z2z5 + z3z6,
A1 = z2
1 − 2z3z4,
A2 = −z2
5 − 2z2z4,
A3 = z2
2 − 2z1z5,
A4 = z2
3 − 2z2z6,
A5 = −z2
4 − 2z1z6,
A6 = −z2
6 − 2z3z5.
(1.3)
Then w∞, wν for ν = 0 , . . . ,12 are the roots of a polynomial of degree
fourteen. The corresponding equation is just the Jacobian equat ion of degree
fourteen (see [23], pp.161-162). On the other hand, set
δ∞ = 13 2G0, δ ν = −13G0 + ζ νG1 + ζ 2νG2 + · · · + ζ 12νG12 (1.4)
2
for ν = 0 , 1, . . . ,12, where the senary sextic forms (i.e., sextic forms in six
variables) Gj (j = 0, 1, . . . ,12) are given by















































































































G0 =D2
0 + D2
∞,
G1 = − D2
7 + 2D0D1 + 10D∞D1 + 2D2D12+
− 2D3D11 − 4D4D10 − 2D9D5,
G2 = − 2D2
1 − 4D0D2 + 6D∞D2 − 2D4D11+
+ 2D5D10 − 2D6D9 − 2D7D8,
G3 = − D2
8 + 2D0D3 + 10D∞D3 + 2D6D10+
− 2D9D7 − 4D12D4 − 2D1D2,
G4 = − D2
2 + 10D0D4 − 2D∞D4 + 2D5D12+
− 2D9D8 − 4D1D3 − 2D10D7,
G5 = − 2D2
9 − 4D0D5 + 6D∞D5 − 2D10D8+
+ 2D6D12 − 2D2D3 − 2D11D7,
G6 = − 2D2
3 − 4D0D6 + 6D∞D6 − 2D12D7+
+ 2D2D4 − 2D5D1 − 2D8D11,
G7 = − 2D2
10 + 6D0D7 + 4D∞D7 − 2D1D6+
− 2D2D5 − 2D8D12 − 2D9D11,
G8 = − 2D2
4 + 6D0D8 + 4D∞D8 − 2D3D5+
− 2D6D2 − 2D11D10 − 2D1D7,
G9 = − D2
11 + 2D0D9 + 10D∞D9 + 2D5D4+
− 2D1D8 − 4D10D12 − 2D3D6,
G10 = − D2
5 + 10D0D10 − 2D∞D10 + 2D6D4+
− 2D3D7 − 4D9D1 − 2D12D11,
G11 = − 2D2
12 + 6D0D11 + 4D∞D11 − 2D9D2+
− 2D5D6 − 2D7D4 − 2D3D8,
G12 = − D2
6 + 10D0D12 − 2D∞D12 + 2D2D10+
− 2D1D11 − 4D3D9 − 2D4D8.
(1.5)
Here, the senary cubic forms (cubic forms in six variables) Dj (j = 0, 1, . . .,
3
12, ∞) are given as follows:

























































D0 = z1z2z3,
D1 = 2z2z2
3 + z2
2z6 − z2
4z5 + z1z5z6,
D2 = −z3
6 + z2
2z4 − 2z2z2
5 + z1z4z5 + 3z3z5z6,
D3 = 2z1z2
2 + z2
1z5 − z4z2
6 + z3z4z5,
D4 = −z2
2z3 + z1z2
6 − 2z2
4z6 − z1z3z5,
D5 = −z3
4 + z2
3z5 − 2z3z2
6 + z2z5z6 + 3z1z4z6,
D6 = −z3
5 + z2
1z6 − 2z1z2
4 + z3z4z6 + 3z2z4z5,
D7 = −z3
2 + z3z2
4 − z1z3z6 − 3z1z2z5 + 2z2
1z4,
D8 = −z3
1 + z2z2
6 − z2z3z5 − 3z1z3z4 + 2z2
3z6,
D9 = 2z2
1z3 + z2
3z4 − z2
5z6 + z2z4z6,
D10 = −z1z2
3 + z2z2
4 − 2z4z2
5 − z1z2z6,
D11 = −z3
3 + z1z2
5 − z1z2z4 − 3z2z3z6 + 2z2
2z5,
D12 = −z2
1z2 + z3z2
5 − 2z5z2
6 − z2z3z4,
D∞ = z4z5z6.
(1.6)
Then δ∞, δν for ν = 0, . . . ,12 are the roots of a polynomial of degree fourteen.
The corresponding equation is not the Jacobian equation. Now, a fa mily of
invariants for G is given as follows: put
Φ 4 =
12∑
ν=0
wν + w∞, Φ 8 =
12∑
ν=0
w2
ν + w2
∞, (1.7)
Φ 12 = − 1
13 · 52
( 12∑
ν=0
δ2
ν + δ2
∞
)
, Φ ′
12 = − 1
13 · 30
( 12∑
ν=0
w3
ν + w3
∞
)
, (1.8)
Φ 16 =
12∑
ν=0
w4
ν + w4
∞, Φ 18 = 1
13 · 6
( 12∑
ν=0
δ3
ν + δ3
∞
)
, (1.9)
Φ 20 = 1
13 · 25
( 12∑
ν=0
w5
ν + w5
∞
)
, Φ 30 = − 1
13 · 1315
( 12∑
ν=0
δ5
ν + δ5
∞
)
, (1.10)
4
and xi(z) = η(z)ai(z) (1 ≤ i ≤ 6), where













































a1(z) := e− 11πi
26 θ
[ 11
13
1
]
(0, 13z),
a2(z) := e− 7πi
26 θ
[ 7
13
1
]
(0, 13z),
a3(z) := e− 5πi
26 θ
[ 5
13
1
]
(0, 13z),
a4(z) := −e− 3πi
26 θ
[ 3
13
1
]
(0, 13z),
a5(z) := e− 9πi
26 θ
[ 9
13
1
]
(0, 13z),
a6(z) := e− πi
26 θ
[ 1
13
1
]
(0, 13z)
(1.11)
are theta constants of order 13 and η(z) := q
1
24
∏ ∞
n=1(1 − qn) with q = e2πiz
is the Dedekind eta function which are all deﬁned in the upper-half pla ne
H = {z ∈ C : Im(z) > 0}. Our main theorem is the following:
Theorem 1.1. The G-invariant polynomials Φ 4, . . ., Φ 30 in x1(z), . . .,
x6(z) can be identiﬁed with modular forms as follows :





























Φ 4(x1(z), . . . , x6(z)) = 0 ,
Φ 8(x1(z), . . . , x6(z)) = 0 ,
Φ 12(x1(z), . . . , x6(z)) = ∆( z),
Φ ′
12(x1(z), . . . , x6(z)) = ∆( z),
Φ 16(x1(z), . . . , x6(z)) = 0 ,
Φ 18(x1(z), . . . , x6(z)) = ∆( z)E6(z),
Φ 20(x1(z), . . . , x6(z)) = η(z)8∆( z)E4(z),
Φ 30(x1(z), . . . , x6(z)) = ∆( z)2E6(z).
(1.12)
Theorem 1.1 has many consequences. The ﬁrst one comes from the theory
of singularities: there exists at least two kinds of constructions of the equation
of the E8-singularity: one is given by the icosahedral group in the celebrated
book of Klein [23], i.e., the icosahedral singularity (see [5], p. 107), the other
is given by the group PSL(2 , 13).
5
Theorem 1.2 (A diﬀerent construction of the E8-singularity: from X(13)
to E8). The equation of the E8-singularity can be constructed from the mod-
ular curve X(13) as follows :
Φ 3
20 − Φ 2
30 = 1728Φ 5
12, (1.13)
where Φ j = Φ j(x1(z), . . . , x6(z)) for j = 12, 20 and 30. As polynomials in six
variables z1, . . . , z6, Φ 12, Φ 20 and Φ 30 are G-invariant polynomials.
In fact, in his talk at ICM 1970 [4], Brieskorn showed how to construc t
the singularity of type ADE directly from the simple complex Lie group of
the same type. At the end of that paper [4] Brieskorn says:“Thus we see that
there is a relation between exotic spheres, the icosahedron and E8. But I still
do not understand why the regular polyhedra come in.” (see also [16], [17]
and [6]). As a consequence, Theorem 1.2 shows that the E8 root lattice is
not necessarily constructed from the icosahedron. That is, the ic osahedron
does not necessarily appear in the triple (exotic spheres, icosahed ron, E8)
of Brieskorn [4]. The group PSL(2 , 13) can take its place and there is the
other triple (exotic spheres, PSL(2 , 13), E8). The higher dimensional liftings
of these two distinct groups and modular interpretations on the eq uation of
the E8-singularity give the same Milnor’s standard generator of Θ 7.
The second consequence of Theorem 1.1 comes from diﬀerential to pol-
ogy of 4-manifolds. The manifold CP2#8
CP
2
has two distinct diﬀerentiable
structures, both of which come from algebraic surfaces: one is th e eight-fold
blow-up of the projective plane carrying the standard smooth str ucture, the
other is the Barlow surface [2], which is a simply connected minimal surf ace
of general type with q = pg = 0 and K 2 = 1. In fact, up to now, only two
kinds of such surfaces are known: the ﬁrst example is the Barlow su rface
[2], the second examples are given by Lee and Park in the appendix of [2 9],
both of them are simply connected, minimal, complex surfaces of gen eral
type with pg = 0 and K 2 = 1. The Barlow surface comes from a certain
Hilbert modular surface associated to the icosahedral group (see [15]). On
the other hand, the Lee-Park surfaces are constructed by a ra tional blow-
down surgery and a Q-Gorenstein smoothing theory (see [29]). The Barlow
surface is homeomorphic but not diﬀeomorphic to CP2#8CP
2
(see [28]). We
prove the following:
Theorem 1.3 (A diﬀerent construction of the Barlow surface: from
X(13) to E8). The Barlow surface can be constructed from the modular
curve X(13).
6
The third consequence of Theorem 1.1 comes from representation theory
and classical algebraic geometry: the automorphism group of the c onﬁgu-
ration of 120 tritangent planes of Bring’s curve is the quotient of th e Weyl
group W (E8) of the root system of type E8 by the normal subgroup {±1}
with order 2 13 · 35 · 52 · 7, which is just the group G8, 2 studied by Coble in p.
356 of his paper [7]. Note that Bring’s curve has an analogue: Fricke’s oc-
tavic curve, both of them arise from the resolution of the equation of the ﬁfth
degree (see [23]). Hence, they are intimately connected with the ico sahedron.
As a consequence of Theorem 1.1, we prove the following:
Theorem 1.4 (A diﬀerent construction of Bring’s curve and Fricke’s
octavic curve: from X(13) to E8). Both Bring’s curve and Fricke’s octavic
curve can be constructed from the modular curve X(13).
Theorem 1.2, Theorem 1.3 and Theorem 1.4 show that there exist two
distinct constructions of the E8 root lattice from its three diﬀerent appear-
ances. Hence, the fact that the E8 root lattice is not necessarily constructed
from the icosahedron, can be realized not only from the theory of s ingular-
ities and exotic spheres, but also from diﬀerential topology of 4-ma nifolds,
representation theory and classical algebraic geometry.
The fourth consequence of Theorem 1.1 comes from the explicit con struc-
tion of modular curves, which is a classical problem studied by Klein (se e
[24], [25], [26] and [27]).
Problem 1.5. Let p ≥ 7 be a prime number. Give an explicit con-
struction of the modular curve X(p) of level p from the invariant theory for
PSL(2, p) using projective algebraic geometry.
For p = 7, the modular curve X(7) is given by the celebrated Klein quartic
curve (see [24])
x3y + y3z + z3x = 0.
For p = 11, the modular curve X(11) leads to the study of the Klein cubic
threefold (see [25])
v2w + w2x + x2y + y2z + z2v = 0.
Following Klein’s method for the cubic threefold, Adler and Ramanan (s ee
[1]) studied Problem 1.5 when p is a prime congruent to 3 modulo 8 by some
cubic hypersurface invariant under PSL(2 , p). However, their method can
not be valid for p = 13. As a consequence of Theorem 1.1, we ﬁnd an explicit
construction of the modular curve X(13). Let
φ12(z1, . . . , z6) = Φ 12(z1, . . . , z6) − Φ ′
12(z1, . . . , z6). (1.14)
7
Theorem 1.6 (An explicit construction of the modular curve X(13)).
There is a morphism
Φ : X(13) → C ⊂ CP5
with Φ( z) = ( x1(z), . . . , x6(z)), where C is an algebraic curve given by a
family of G-invariant equations









Φ 4(z1, . . . , z6) = 0 ,
Φ 8(z1, . . . , z6) = 0 ,
φ12(z1, . . . , z6) = 0 ,
Φ 16(z1, . . . , z6) = 0 ,
(1.15)
where φ12 is given as in (1.14).
This paper consists of ﬁve sections. In section two, we revisit the s tan-
dard construction of the E8 root lattice by means of the icosahedron. This
includes the E8-singularity, the Barlow surface, Bring’s curve and Fricke’s oc-
tavic curve. In section three, we explain the invariant theory for P SL(2, 13).
In particular, we construct the senary quadratic forms Aj (0 ≤ j ≤ 6),
the senary cubic forms Dj (j = 0 , 1, . . . ,12, ∞) and the senary sextic forms
Gj (0 ≤ j ≤ 12). From Aj we construct the Jacobian equation of degree
fourteen. From Dj and Gj we construct another equation of degree four-
teen. Combining Jacobian equation with that equation, we obtain a fa mily
of polynomials which are invariant under the action of PSL(2 , 13). Together
with theta constants of order thirteen, this gives the modular par ametriza-
tion of these invariant polynomials. Therefore, we obtain Theorem 1 .1. In
section four, we give three constructions of the E8 root lattice, and prove
Theorem 1.2, Theorem 1.3 and Theorem 1.4. In section ﬁve, we give an
explicit construction of the modular curve X(13).
Acknowledgements. The author would like to thank Jean-Pierre Serre
for his very detailed and helpful comments and his patience. The aut hor also
thanks Pierre Deligne for his helpful comments.
2. Standard construction: from the icosahedron to E8
