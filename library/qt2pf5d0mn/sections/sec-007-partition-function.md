---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-007-partition-function
section_title: "Partition Function"
section_number: null
pages: 43-51
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
invariant reduces to the twisted Dijkgraaf-Witten invariant as a special case.
3.1
Partition Function
An ordered triangulation of a manifold is a triangulation with an ordering of its
vertices by 0, 1, 2, · · · . Let T be an ordered triangulation of a closed oriented 4-manifold
M, and for k = 0, 1, 2, 3, 4, let T k be the set of k-simplicies of the triangulation. The
restriction of the ordering on each k-simplex σ ∈T k induces a relative ordering of the
vertices of σ. Under this relative ordering, we write σ as (0 1 · · · k −1). For each
σ ∈T 4, we deﬁne the sign, ϵ(σ), of σ to be + if the orientation on σ induced from that
of M coincides with that coming from the ordering of its vertices; ϵ(σ) is deﬁned to be
−otherwise.
Let D = C×
G = L
g∈G
Cg be a G-BSFC, and let L(D) be the set of isomorphism classes
of simple objects.
Deﬁnition 3.1.1 A D-coloring of T is a pair of maps F = (g, f), g : T 1 →G, f :
T 2 →L(D), such that for any simplex β = (012) ∈T 2 with the induced ordering on its
vertices,
f(012) ∈Cg(02)−1g(01)g(12).
Given a D-coloring F = (g, f), for each β = (012) ∈T 2, we arbitrarily choose a
representative in the class f(012) and denote it by f012 or just 012 when no confusion
arises. For an edge (ij), we also write g(ij) as gij or ij, g(ij)−1 as ¯gij or ij.
Remark 3.1.2 Since the representative for each triangle color is chosen arbitrarily, it is
possible that even if two triangles are assigned the same color, their representatives could
still be diﬀerent. Our approach is thus more general than the common one, where a rep-
resentative for each isomorphism class is ﬁxed at the beginning and these representatives
34
Section 3.1
Partition Function
are assigned as triangle colors. The approach here is necessary and will become clear in
Section 4.2 where we prove the partition function does not depend on the ordering of the
triangulation.
Assume now a representative for each triangle has been chosen. For any τ = (0123) ∈
T 3 with the induced ordering on its vertices, consider the boundary map:
∂(0123) = (123) −(023) + (013) −(012).
We assign to (0123) two vector spaces:
V +
F (0123) := Hom(f023 ⊗
f
¯g23
012, f013 ⊗f123),
V −
F (0123) := Hom(f013 ⊗f123, f023 ⊗
f
¯g23
012).
Note that by the properties of a coloring, the objects f023 ⊗
f
¯g23
012 and f013 ⊗f123 are
both in the sector C¯g03g01g12g23. This is necessary since otherwise the spaces V +
F (0123) and
V −
F (0123) would always be trivial.
Recall that for any two objects X, Y ∈D, the pairing on Hom(X, Y ) × Hom(Y, X) is
deﬁned as follows:
⟨, ⟩: Hom(X, Y ) × Hom(Y, X) −→C
(φ, ψ)
7→Tr(φψ)
The pairing ⟨, ⟩is non-degenerate, and thus there is a natural isomorphism between
V +
F (0123) and V −
F (0123)∗, V −
F (0123) and V +
F (0123)∗induced by the pairing.
Finally for any 4-simplex σ = (01234) ∈T 4 with the induced ordering on its vertices,
35
Section 3.1
Partition Function
the partition function Zϵ(σ)
F
(σ) is deﬁned as follows. Note that the boundary map is given
by:
∂(01234) = (1234) −(0234) + (0134) −(0124) + (0123).
If ϵ(σ) = +, we ﬁrst deﬁne the functional ˜Z+
F (01234) : V +
F (0234) ⊗V +
F (0124) ⊗
V −
F (1234) ⊗V −
F (0134) ⊗V −
F (0123) →C by the picture shown in Figure 3.1 (Left). The
meaning of the picture is interpreted in the following way. Given an element φ0 ⊗φ1 ⊗
φ2 ⊗φ3 ⊗φ4, each φi is to be inserted in the corresponding box, and the resulting
graph represents a morphism in Hom(1, 1), which is a scalar multiple of Id1.
Then
˜Z+
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4) is deﬁned to be that scalar. Note that the label ¯g34
to the left top corner of the box containing V −
F (0123) in the picture means the action of
¯g34 on the space V −
F (0123). It is direct to ﬁgure out the object labels on each edge of the
picture and check that all the compositions of morphisms make sense.
Using the non-degenerate pairing ⟨, ⟩, this deﬁnes a linear map Z+
F (01234):
Z+
F (01234) : V +
F (0234) ⊗V +
F (0124) −→V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123),
such that ⟨Z+
F (01234)(φ0 ⊗φ1), φ2 ⊗φ3 ⊗φ4⟩= ˜Z+
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4).
Note that the domain of Z+
F (01234) corresponds to the negative boundaries, and the
codomain corresponds to the positive boundaries. Thus we can think of Z+
F (01234) as a
map from negative boundaries to positive boundaries.
Similarly, if ϵ(σ) = −, consider instead the functional ˜Z−
F (01234) : V −
F (0234) ⊗
V −
F (0124) ⊗V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123) →C by the picture shown in Figure 3.1
(Right), which is obtained by reﬂecting the picture in Figure 3.1 (Left) along a horizon
line. In the same way we get a linear map:
Z−
F (01234) : V +
F (1234) ⊗V +
F (0134) ⊗V +
F (0123) −→V +
F (0234) ⊗V +
F (0124),
36
Section 3.1
Partition Function
V +
F (0234)
V +
F (0124)
V −
F (1234)
V −
F (0134)
V −
F (0123)
¯g34
V +
F (0123)
¯g34
V +
F (0134)
V +
F (1234)
V −
F (0124)
V −
F (0234)
Figure 3.1: (Left): ˜Z+
F (01234); (Right): ˜Z−
F (01234)
by ⟨φ0 ⊗φ1, Z−
F (01234)(φ2 ⊗φ3 ⊗φ4)⟩= ˜Z−
F (01234)(φ0 ⊗φ1 ⊗φ2 ⊗φ3 ⊗φ4). Noting that
∂(−01234) = −(1234) + (0234) −(0134) + (0124) −(0123),
we can also think of Z−
F (01234) as a map from negative boundaries to positive boundaries.
Each 3-simplex τ is the intersection of exactly two 4-simplices σ1 and σ2. If τ is a
negative boundary in σ1, it must be a positive boundary in σ2. Thus, V +
F (τ) appears
exactly once in the domain and codomain for some 4-simplex. Thus we have
O
σ∈T 4
Zϵ(σ)
F
(σ) :
O
τ∈T 3
V +
F (τ) −→
O
τ∈T 3
V +
F (τ).
37
Section 3.1
Partition Function
Deﬁnition 3.1.3 Given a G-BSFC D and an ordered triangulation T of a closed ori-
ented 4-manifold M, the partition function ZD(M; T ) of the pair (M, T ) is deﬁned by:
ZD(M; T ) =
X
F=(g,f)
(D2/|G|)|T 0|( Q
β∈T 2 df(β)) Tr( N
σ∈T 4 Zϵ(σ)
F
(σ))
(D2)|T 1|
,
(3.1)
where F runs through all D-colorings of T .
Theorem 3.1.4 (Main Theorem) The partition function ZD(M; T ) is an invariant
of closed oriented 4-manifolds.
To prove the Main Theorem, we need to show that ZD(M; T ) is independent on:
1. the choice of representatives for each triangle color,
2. the ordering of vertices of a triangulation,
3. the choice of a triangulation.
These will be proved in Section 4.1, Section 4.2, and Section 4.4, respectively.
Below we derive two other formulas for the partition function, which will be used in
the invariance proof.
For any two objects X, Y , the non-degenerate pairing ⟨, ⟩X,Y induces canonical
isomorphisms Hom(X, Y ) ≃Hom(Y, X)∗and Hom(Y, X) ≃Hom(X, Y )∗. Deﬁne ⟨, ⟩∗
X,Y
to be the dual map of ⟨, ⟩X,Y :
⟨, ⟩∗
X,Y : C −→Hom(X, Y )∗⊗Hom(Y, X)∗≃Hom(Y, X) ⊗Hom(X, Y ),
and let φX,Y = ⟨, ⟩∗
X,Y (1).
If {vi}i∈I and {wj}j∈I are a basis of Hom(X, Y ) and Hom(Y, X), respectively, such
that ⟨vi, wj⟩= diδi,j for some non-zero numbers di, then it is direct to check that φX,Y =
38
Section 3.1
Partition Function
P
i∈I
d−1
i wi ⊗vi.
Now assume an coloring F = (g, f) and a representative for each triangle color have
been chosen. For each 3-simplex τ = (0123) ∈T 3, there is thus the element
φF;τ := φf023⊗
f
¯g23
012 ,f013⊗f123 ∈V −
F (0123) ⊗V +
F (0123).
Let VF = N
τ∈T 3 V −
F (τ) ⊗V +
F (τ).
From the deﬁnition of ˜Zϵ(σ)
F
(σ) for each σ ∈T 4, again it is not hard to see that if
τ ∈T 3 is the intersection of two 4-simplices σ1, σ2, then V +
F (τ) ⊗V −
F (τ) appears as a
component in the domain of ˜Zϵ(σ1)
F
(σ1)⊗˜Zϵ(σ2)
F
(σ2). And therefore, the map N
σ∈T 4
˜Zϵ(σ)
F
(σ)
is a functional on VF.
Proposition 3.1.5 Let φF = N
τ∈T 3 φF;τ ∈VF, then ZD(M; T ) is given by the following
formula:
ZD(M; T ) =
X
F=(g,f)
(D2/|G|)|T 0|( Q
α∈T 2 df(α))
(D2)|T 1|
(
O
σ∈T 4
˜Zϵ(σ)
F
(σ))(φF)
(3.2)
We will give a third formulation of the partition function as a state sum model. For
simplicity, we assume that the category D is multiplicity free. The more general case can
be considered in a similar way.
Let ˜L(D) be an arbitrary complete set of representatives, one for each isomorphism
of simple objects. Recall for each triple (a, b, c) of simple objects such that N c
ab = 1,
namely, (a, b, c) is admissible, we have chosen a basis element Bab
c ∈Hom(c, a ⊗b), and a
basis element Bc
ab ∈Hom(a ⊗b, c), such that for any c, c′ ∈˜L(D), Bc′
abBab
c = δc,c′Idc, and
that
P
c∈˜L(D)
Bab
c Bc
ab = Ida⊗b. These identities are also illustrated in Figure 3.2.
39
Section 3.1
Partition Function
a
b
c
a
b
c
(I)
(II)
c
d
e
a
b
(III)
a
b
c
c′
= δc,c′
c
(IV)
P
c
a
b
c
a
b
=
a
b
(V)
Figure 3.2: Some identities
For simple objects (a, b, c, d), let Be
ab,cd = Bcd
e Be
ab, thus
{Be
ab,cd : e ∈˜L(D), (a, b, e), (c, d, e) admissible}
is a basis of Hom(a ⊗b, c ⊗d), and moreover, we have ⟨Be
ab,cd, Be′
cd,ab⟩= δe,e′de.
Deﬁnition 3.1.6 An extended D-coloring on the ordered triangulation T is a triple ˆF =
(g, f, t), g : T 1 →G, f : T 2 →L(D), t : T 3 →L(D), such that,
1. for any β = (012) ∈T 2, f(012) ∈C¯g02g01g12;
2. for any τ = (0123) ∈T 3, t(0123) ∈C¯g03g01g12g23.
As before, we choose arbitrarily a representative for each f(012) and t(0123), and
denote these representatives as f012, t0123 or 012, 0123. Then, for each σ ∈T 4, the 25j-
symbol ˆZϵ(σ)
ˆF
(σ) is deﬁned to be the evaluation of the graph in Figure 3.3 (Left) if ϵ = +,
and Figure 3.3 (Right) if ϵ = −.
Proposition 3.1.7 The partition function has the state sum model:
ZD(M; T ) =
X
ˆF=(g,f,t)
(D2/|G|)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)
ˆF
(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
(3.3)
40
Section 3.1
Partition Function
034
023
¯
34
012
¯
34· ¯
23
0234
024
234
0124
014
124
1234
134
123
¯
34
0134
013
¯
34
0123
¯
34
¯
34
0123
0134
013
¯
34
1234
134
123
¯
34
0124
014
124
0234
034
023
¯
34
012
¯
34· ¯
23
024
234
Figure 3.3: (Left): ˆZ+
ˆF (01234); (Right): ˆZ+
ˆF (01234)
41
