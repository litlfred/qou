---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-022-10-examples
section_title: "Examples"
section_number: 10
pages: 35-40
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
In the examples below, all computations of Ptolemy varietie s are exact, whereas the computations
of complex volume are numerical with at least 50 digits precision.
Example 10.1 (The 52 knot complement). Consider the 3-cycle K obtained from the simplices in
Figure 8 by identifying the faces via the unique simplicial attachin g maps preserving the arrows.
The space obtained from K by removing the 0-cell is homeomorphic to the complement of the 52
knot, as can be veriﬁed by SnapPy [ 9].
0
3
1
2
a0
a1
b0 b1
b0
b1a1
a0
c1 c0
c0
c1
x2
x0x1
x3
1
3
2
0
b0
b1
b0 b1
a1
a0c1
c0
a1 a0
c1
c0
x3
x0y2
y3
0
1
2
3
a0
a1
b0 b1
a0
a1c1
c0
b1 b0
a0
a1
x1
y3y2
x2
Figure 8. A 3-cycle structure on the 52 knot complement, and Ptolemy coordinates for n = 3.
Labeling the Ptolemy coordinates as in Figure 8, the Ptolemy variety for n = 3 is given by the
equations
(10.1)
a0x3 + b0x1 = b0x2, a 0y3 + a0x0 = c0y2, a 0x2 + b0y2 = a0x1
x2c0 + b1x0 = x3a0, y 2b0 + a1x3 = y3b0, x 1a0 + b1y3 = x2c0
x1c1 + x3c0 = b1x0, x 0b1 + y3c0 = c1x3, y 2a1 + x2b0 = a1y3
a1x0 + x2c1 = x1a1, a 1x3 + y2c1 = x0b1, a 1y3 + x1b1 = y2c1
together with an extra equation (involving an additional va riable t)
(10.2) a0a1b0b1c0c1x0x1x2x3y2y3t = 1,
making sure that all Ptolemy coordinates are non-zero. By Rem ark 4.5, the diagonal matrices act on
the decorations, and one easily checks that the action by a ma trix diag(x, y, z) with determinant 1
multiplies a Ptolemy coordinate on an edge by x2y and a Ptolemy coordinate on a face by x3. Since
we are not interested in the particular decoration, we may th us assume e.g. that a0 = y3 = 1. Using
Magma [3], one ﬁnds that the Ptolemy variety, after setting a0 = y3 = 1, has three zero-dimensional
components with 3, 4 and 6 points respectively. One of these is given by
(10.3)
a0 = a1 = y3 = 1, x 1 = −1, c 0 = c1 = x2
0 + 2x0 + 1
y2 = x2
0 + 2 = −x2, x 3 = −x2
0 − x0 − 1
x3
0 + x2
0 + 2x0 + 1 = 0
Thus, this component gives rise to 3 representations, one for each solution to x3
0 + x2
0 + 2x0 + 1 = 0 .
Using the fact that R(λ(c)) = i VolC(ρ), the complex volumes of these can be computed to be
(10.4) 0.0 − 4.453818209 . . . i ∈ C/4π2iZ, ±11.31248835 . . . + 12.09651350 . . . i ∈ C/4π2iZ
corresponding to the values x0 = −0.5698 . . . and x0 = −0.2150 ∓ 1.3071 . . . i, respectively.
36 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
In Zickert [ 30, Section 6], the complex volumes of the Galois conjugates of the geometric repre-
sentation are computed to be
(10.5) 0.0 − 1.113454552 . . . i ∈ C/π2iZ, ±2.828122088 . . . + 3.024128376 . . . i ∈ C/π2iZ.
Notice that ( 10.4) is (approximately) 4 times ( 10.5). It thus follows from Theorem 1.6 that the
representations given by ( 10.3) are φ3 composed with the geometric component of PSL(2, C)-
representations and that the factor of 4 is exact.
Another component is given by
(10.6)
a0 = a1 = y3 = 1, x 1 = −1, b 1 = −x0
b0 = 1/4x3
0 − 1/4x2
0 + 3/4x0 − 1/2
c0 = c1 = 1/4x3
0 − 1/4x2
0 − 1/4x0 + 1/2
y2 = −x2 = 1/4x3
0 + 3/4x2
0 + 7/4x0 + 3/2
x3 = −x2
0 − x0 − 1
x4
0 + x3
0 + x2
0 − 4x0 − 4 = 0 .
In this case there are two distinct complex volumes given by:
(10.7) 0.0 + 2.631894506 . . . i = 4
15 π2i ∈ C/4π2iZ, 0.0 + 10.527578027 . . . i = 16
15 π2i ∈ C/4π2iZ.
The third component has somewhat larger coeﬃcients, but aft er introducing a variable u with
u6 + 5u4 + 8u2 − 2u + 1 = 0 , the deﬁning equations simplify to
(10.8)
a0 = y3 = 1, a 1 = 1/4u5 + 1/4u4 + 5/4u3 + 1/2u2 + 2u − 3/4
b0 = b1 = −1/4u4 − 3/4u2 − 1/4u − 3/4,
c1 = −1/4u5 − 3/4u3 − 1/4u2 − 3/4u,
c0 = 1/2u5 + 9/4u3 + 1/4u2 + 7/2u − 1/4,
y2 = −8/17u5 − 1/34u4 − 79/34u3 − 3/17u2 − 105/34u + 26/17,
x3 = 1/17u5 − 1/17u4 + 6/17u3 − 6/17u2 + 14/17u − 16/17,
x2 = 9/34u5 + 4/17u4 + 37/34u3 + 31/34u2 + 75/34u + 13/17,
x1 = 8/17u5 + 1/34u4 + 79/34u3 + 3/17u2 + 139/34u − 9/17,
x0 = 15/34u5 + 1/17u4 + 73/34u3 + 29/34u2 + 125/34u − 1/17,
u6 + 5u4 + 8u2 − 2u + 1 = 0 .
In this case, there are 3 distinct complex volumes:
(10.9) 0.0 + 1.241598704 . . . i, ±6.332666642 . . . + 1.024134714 . . . i
According to Conjecture 1.16, 6.33 · · · + 1.02 . . . i should (up to rational multiples of π2i) be an
integral linear combination of complex volumes of hyperbol ic manifolds. Using e.g. Snap [ 17], one
checks that the complex volume of the manifold m034 is given by
(10.10) 3.166333321 . . . + 2.157001424 . . . i,
and we have
(10.11) 6.332666642 . . . + 1.024134714 . . . i = 2 VolC(m034) − 1
3 π2i ∈ C/4π2iZ.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 37
Example 10.2 (The ﬁgure 8 knot complement). Let K be the 3-cycle in Figure 9. Then M = M (K)
is the ﬁgure 8 knot complement, and H 2(K; Z/2Z) = H 2(M, ∂M ; Z/2Z) = Z/2Z.
2
3
1
0
y y
y
x
xx
0
3
1
2
x y
x
x
yy
Figure 9. A 3-cycle structure on the ﬁgure 8 knot complement and Ptolemy coordinates
for n = 2. The signs indicate the non-trivial second Z/2Z cohomology class.
For the trivial obstruction class, the Ptolemy variety for n = 2 is given by
(10.12) yx + y2 = x2, xy + x2 = y2,
and is thus empty since x and y are non-zero. In fact, the only boundary-unipotent represe ntations in
SL(2, C) are reducible, so this is not surprising. The non-trivial ob struction class can be represented
by the cocycle indicated in Figure 9, and the Ptolemy variety is given by
(10.13) yx − y2 = x2, xy − x2 = y2.
As in Example 10.1, we may assume y = 1 . Hence, the Ptolemy variety detects two (complex
conjugate) representations corresponding to the solution s to x2 − x + 1 = 0 . The extended Bloch
group elements are
(10.14) − (−~x, −2~x) + (~x, 2~x) ∈ ˆB(C)PSL,
with complex volume
(10.15) ± 2.029883212 . . . + 0.0i.
We thus recover the well known complex volume of the ﬁgure 8 knot complement.
For n = 3 , similar calculations as those in Example 10.1 show that the Ptolemy variety detects
3 zero-dimensional components, but the only one with non-zer o volume is the one induced by
the geometric representation. For n = 4 , lots of new complex volumes emerge. For the trivial
obstruction class, the non-zero complex volumes are
(10.16) ± 7.327724753 . . . + 0.0i = 2 VolC(52
1) + π2i/4,
where the manifold 52
1 is the whitehead link complement. For the non-trivial obstr uction class, the
complex volumes are
(10.17)
±20.29883212 . . . + 0.0i = 10 VolC(41) ∈ C/π2iZ
±4.260549384 . . . ± 0.136128165 . . . i
±3.230859569 . . . + 0.0i
±8.355502146 . . . + 2.428571615 . . . i = VolC(−93
15) + 2π2i/3
±3.276320849 . . . + 9.908433886 . . . i.
38 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Example 10.3 (S1 × S2). Figure 10 shows a triangulation of M = S1 × S2 taken from the Regina
census [ 4]. Since π1(S1 × S2) = Z, all representations in PSL(2, C) lift to SL(2, C), so we expect
the Ptolemy variety for the non-trivial class in H 2(M ; Z/2Z) to be zero. This class is represented
by the cocycle shown in Figure 10, and the Ptolemy variety is given by
(10.18) − zx + x2 = y2, x 2 + zx = y2,
which indeed has no solutions in C∗. For the trivial cohomology class, all signs are positive, a nd
the two equations are equivalent. The extended Bloch group el ement is
(10.19) (~z +~x − 2~y, 2~x − 2~y) − (~z +~x − 2~y, 2~x − 2~y) = 0 ∈ ˆB(C).
In fact, the extended Bloch group element of a Ptolemy assignm ent is trivial for all n, as one easily
veriﬁes (the subsimplices cancel out in pairs).
We wish to ﬁnd out which representations are detected by P2(K). A choice of fundamental
domain F for K in L determines a presentation of π1(M ) with a generator for each face pairing of
F and a relation for each 1-cell of K (to see this consider the standard presentation for the dual
triangulation of K). Letting F be the fundamental domain of S1 × S2 given by gluing the bottom
faces of the two simplices together, one easily checks that t he generator of π1(M ) = Z is given by
the self gluing of the ﬁrst simplex taking the face opposite t he third vertex to the face opposite the
zeroth. For α ∈ SL(2, C), the representation given by taking the generator to α has a decoration as
in Figure 10. For A =
( a b
c d
)
, let c(A) = c, and note that det(e1, Ae1) = c(A). Letting x, y and z
denote the Ptolemy coordinates, we have
(10.20) x = c(α), y = c(α2) = xTr(α), z = c(α3) = x(Tr(α)2 − 1),
and it follows that the Ptolemy variety detects all represen tations except those where Tr(α) = ±1.
0
1
2
3
α−1N
N
αN
α2N
x x
y
y
xz
0
3
2
1
α−1N
N
αN
α2N
z x
y
y
xx
Figure 10. A triangulation of S1 × S2. Both simplices have self gluings.
Remark 10.4. When n = 2 , examples of Conjecture 1.16 are abundant. E.g. for the 10155 knot
complement (10 simplices), the volumes of the representations detected by the Ptolemy variety are
(numerically)
(10.21) Vol(m032(6, 1)), 2 Vol(41), 3 Vol(10155) − 4 Vol(v3461), Vol(10155).
Remark 10.5. For the hyperbolic census manifolds, most of the components of the Ptolemy va-
rieties (after ﬁxing the action by diagonal matrices) tend t o be zero-dimensional. By a result of
Menal-Ferrer and Porti [ 19], the composition of the geometric representation with φn is isolated
among boundary-unipotent p SL(n, C)-representations. Higher dimensional components also occ ur
(rarely for n = 2, quite often for n > 2), but as mentioned earlier, the complex volume is constant
on components.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 39
Remark 10.6. If the face pairings do not respect the vertex orderings, one can still deﬁne a Ptolemy
variety by introducing more signs. See Garoufalidis–Goern er–Zickert [ 15] for details.
11. The irreducible representations of SL(2, C)
Let φn : SL(2 , C) → SL(n, C) denote the canonical irreducible representation. It is ind uced by
the Lie algebra homomorphism sl(2, C) → sl(n, C) given by
(11.1)
[ 0 1
0 0 ] ↦→diag+(n−1, . . . ,1), [ 0 0
1 0 ] ↦→diag−(1, . . . , n−1),
[1 0
0 −1
]
↦→diag(n−1, n−3, . . . ,−n+1),
where diag+(v) and diag−(v) denote matrices whose ﬁrst upper (resp. lower) diagonal is v and all
other entries are zero. One has
φn
([0 −a− 1
a 0
])
= q(an−1, −an−3, . . . ,(−1)n−1a−(n−1))(11.2)
φn ([ 1 x
0 1 ]) = πn−1(x, . . . , x)πn−2(x, . . . , x) · · · π1(x).(11.3)
Proposition 11.1. Let c be a Ptolemy assignment on ∆ 3
2, and let τ denote the corresponding
cocycle. The assignment
(11.4) φn(c) : ˙∆ 3
n(Z) → C∗, t ↦→φn(c)t =
∏
i<j
ctitj
ij
is a Ptolemy assignment on ∆ 3
n. If c is a PSL(2, C)-Ptolemy assignment with obstruction cocycle
σ, φn(c) is a p SL(n, C)-Ptolemy assignment with obstruction cocycle σ. Moreover, φn(c) is the
Ptolemy assignment corresponding to φn(τ ).
Proof. Let α = (a0, . . . , a3) ∈ ∆ 3
n−2(Z). Letting kα =∏
i<j caiaj
ij , and lα =∏
i<j cai+aj
ij , we have
(11.5)
φn(c)α03 φn(c)α12 = k2
αlαc03c12, φ n(c)α01 φn(c)α23 = k2
αlαc01c23, φ n(c)α02 φn(c)α13 = k2
αlαc02c13.
Hence, the appropriate Ptolemy relations are satisﬁed, pro ving the ﬁrst two statements. The long
and short edges of the cocycle corresponding to φn(c) are given by ( 9.9) and ( 9.20), and we must
prove that these agree with those of φn(τ ). For the long edges, this follows immediately from
(11.2). For the short edges, an easy computation shows that all the diamond coordinates of a
face are equal, and equal to the corresponding diamond coord inate of c. For example, the type 1
diamond coordinate on face 3 whose left vertex is t = (t0, t1, t2, 0) is given by
(11.6)
φn(c)t+(0,−1,1,0)φn(c)t+(−1,1,0,0)
φn(c)tφn(c)t+(−1,0,1,0)
= ct0(t1−1)
01 ct0(t2+1)
02 c(t1−1)(t2+1)
12 c(t0−1)(t1+1)
01 c(t0−1)t2
02 c(t1+1)t2
12
ct0t1
01 ct0t2
02 ct1t2
12 c(t0−1)t1
01 c(t0−1)(t2+1)
02 ct1(t2+1)
12
= c02
c01c12
,
which is a diamond coordinate for c. By ( 11.3) the short edges thus agree with those of φn(τ ),
proving the result. □
Corollary 11.2. If a representation ρ : π1(M ) → PSL(2, C) is detected by P σ
2 (K) then φ2k+1 ◦ ρ
is detected by P2k+1(K) and φ2k ◦ ρ is detected by P σ
2k(K). □
Theorem 11.3. Let ρ be a boundary-unipotent representation in SL(2, C) or PSL(2, C). The ex-
tended Bloch group element of φn ◦ ρ is
( n+1
3
)
times that of ρ. In fact, the shapes of all subsimplices
are equal.
40 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Proof. By reﬁning the triangulation if necessary, we may represent ρ by a Ptolemy assignment c on
K. Then φ = φn(c) is a Ptolemy assignment representing φn ◦ ρ, and the extended Bloch group
element of φn ◦ ρ is given by
(11.7) [φn(ρ)] =
∑
i
ǫi
∑
α∈∆ 3
n− 2(Z)
(~φi
α03 +~φi
α12 −~φi
α02 −~φi
α13 ,~φi
α01 +~φi
α23 −~φi
α02 −~φi
α13).
By Proposition 7.7, we may choose the logarithms independently as long as we use the same loga-
rithm for identiﬁed points. Deﬁning ~φi
t =∑
j<k tjtk~ci
jk , we see that
(11.8) (~φi
α03 +~φi
α12 −~φi
α02 −~φi
α13,~φi
α01 +~φi
α23 −~φi
α02 −~φi
α13) = (~c03+~c12 −~c02−~c13,~c01 +~c23−~c02−~c13),
which means that the ﬂattenings assigned to each subsimplex of ∆ i
n are equal. By Lemma 5.6,
|∆ 3
n−2(Z)| =
( n+1
3
)
, and the result follows. □
