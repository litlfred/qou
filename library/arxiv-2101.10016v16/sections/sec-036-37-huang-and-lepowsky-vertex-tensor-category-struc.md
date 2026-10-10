---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-036-37-huang-and-lepowsky-vertex-tensor-category-struc
section_title: "Huang and Lepowsky (vertex) tensor category structure"
section_number: 37
pages: 224-239
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
37. Huang and Lepowsky (vertex) tensor category structure
37.1. Intertwining operators for vertex operator algebras and P(z)-intertwining
maps. In Sect. 23 we briefly mentioned the main results by Huang and Lepowsky on the
construction of the modular vertex tensor category structure on Rep(V ). Every vertex
tensor category has a naturally associated tensor category as described in Sect. 4 of [84].
In this section we describe this tensor category structure in more detail.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 225
P
For a complex vector space U, let U{x} denote the vector space of formal power series
n∈R
unx
n with generalized series over R, and coefficients in un ∈ U. We recall the
definition of intertwining operator from [59].
Definition 37.1. Let (V, Y, 1, ν) be a vertex operator algebra, see Sect. 22, and let W1,
W2, W3 be V -modules, Def. 22.2. An intertwining operator of type  W3
W1 W2

is a linear map
Y : W1 → Hom(W2, W3){x}, Y(w
(1), x) = X
r∈R
w
(1)
(r)
x
−r−1
satisfying the following axioms (note that we use a suffix e.g. w
(1) to indicate the space
where the vector lies and an index w
(1)
(r)
to indicate a coefficient of the intertwining operator
Y)
a) (lower truncation condition): w
(1)
(r)w
(2) = 0 for r sufficiently large,
b) L−1-derivative (or translation) property
d
dxY(w
(1), x) = Y(L
W1
−1w
(1), x), (37.1)
c) (Jacobi identity) for v ∈ V , w
(1) ∈ W1,
x
−1
0
δ(
x1 − x2
x0
)YW3(v, x1)Y(w
(1), x2) − x−1
0
δ(
x2 − x1
−x0
)Y(w
(1), x2)YW2
(v, x1) = (37.2)
x
−1
2
δ(
x1 − x0
x2
)Y(YW1(v, x0)w
(1), x2)).
The module W1 is called the charge, W2 the source and W3 the target.
Definition 37.2. The dimension of the vector space MW1,W2
W3 of intertwining operators
of a given type  W3
W1 W2

is called the fusion rule.
For a V -module W, let W denote the algebraic completion of W,
W = Πr∈RWr,
P
W
r
: W → Wr, (37.3)
the natural projection maps for r ∈ R. We recall the definition of P(z)-intertwining map
from [84], [85], [86], [87].
Definition 37.3. Fix z ∈ C
×, and let W1, W2, W3 be V -modules. A P(z)-intertwining
map of type  W3
W1 W2

is a linear map
F : W1 ⊗ W2 → W3 (37.4)
satisfying for w
(1) ∈ W1, w(2) ∈ W2, v ∈ V ,
a) (lower truncation) P
W3
r−nF(w
(1) ⊗ w(2)) = 0 for n ∈ Z large,

226 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
b) (intertwining relation)
x
−1
0
δ(
x1 − z
x0
)YW3(v, x1)F(w
(1) ⊗ w(2)) = (37.5)
z
−1
δ(
x1 − x0
z
)F(YW1(v, x0)w
(1) ⊗ w(2)) + x−1
0
δ(
z − x1
−x0
)F(w
(1) ⊗ YW2
(v, x1)w
(2)).
Intertwining operators and P(z) intertwining maps are closely related. Roughly speaking, a P(z)-intertwining map results from an intertwining operator by evaluation on a
nonzero complex number z. Along this procedure, the charge and source spaces do not
change, but the range is replaced by W3. The following is a more precise description.
Let log(z) be the principal branch of the complex logarithm function with the complex
plane cut along the positive real axis, that is
log(z) = log(|z|) + i arg(z), 0 ≤ arg(z) < 2π,
and for p ∈ Z, define the branches
lp(z) = log(z) + 2πpi.
Proposition 37.4. (Prop. 12.2 in [87]) Given z ∈ C, a fixed branch lp induces a canonical
isomorphism from the space of intertwining operator of type  W3
W1 W2

onto the space of P(z)-
intertwining maps of the same type.
a) The isomorphism from intertwining operators to P(z)-intertwining maps is given
by specification of the formal variable x associated to lp,
Y → F, F(w
(1) ⊗ w(2)) = Y(w(1), elp(z)
)w
(2)
, (37.6)
b) The inverse isomorphism is given by
F → Y, Y(w
(1), x)w(2) =
X
r∈R
e
(r+1)lp(z)P∆w(1)+∆w(2)−r−1F(w
(1) ⊗ w(2))x−r−1
, (37.7)
with w
(i) homogeneous with conformal weight ∆w(i) , in the sense of (22.8).
In particular, the dimension of the vector space of P(z)-intertwining maps of type  W3
W1 W2

equals the fusion rule associated to the same V -modules.
Note that the series at the right hand side of (37.6)converges in the product topology of
W3 of the discrete topological spaces (W3)(m) by (37.10).
Prop. 37.4 plays a central role in the connection between affine vertex operator algebras
and weak Hopf algebras.
Similarly to Def. 23.5, from now on we shall use the following convenient change of
notation for modes of intertwining operators.
Definition 37.5. (New grading notation for modes intertwining operators) We set
∆Y = ∆W1 + ∆W2 − ∆W3, (37.8)
with ∆Wiis the conformal weight of Wi, as in (22.12). We also set
w
(1)
n = w
(1)
(n−1+∆Y) (37.9)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 227
Similarly to the case of modules, the translation and Jacobi properties for intertwining
operators imply for w
(1) homogeneous,
w
(1)
n : (W2)(m) → (W3)(m+deg(w(1))−n)
, (37.10)
where for M irreducible and n ∈ Z≥0, M(n) has been defined in (22.13) and deg(w
(1)) =
k ∈ Z means that w
(1) ∈ (W1)(k) ([59], see also Prop. 1.5.1 in [61] for details)
We assume for convenience that Rep(V ) is semisimple as a linear category (e.g. V is
rational in the sense of [85]). Then, similarly to the case of the vertex operators YM(a, x)
cf. Sect. 22, when Wi are all simple, i = 1, 2, 3, the defining series of an intertwining
operator Y of type  W3
W1 W2

is over the countable set,
Y(w
(1), x) = X
n∈Z
w
(1)
nx
−nx−∆Y
. (37.11)
Definition 37.6. Let W1 and W2 be V -modules. A P(z)-tensor product is a V -module
(W1 ⊠P(z) W2, YW1⊠P (z)W2) with a P(z)-intertwining map
F : W1 ⊗ W2 → W1 ⊠P(z) W2 (37.12)
of type W1⊠P (z)W2
W1 W2

such that for any other V -module (W3, YW3) and a P(z)-intertwining
map
F
′
: W1 ⊗ W2 → W3 (37.13)
of type  W3
W1 W2

there is a unique morphism of V -modules
η : W1 ⊠P(z) W2 → W3
defined in Def. 22.3 such that the following diagram commutes
W1 ⊗ W2 W1 ⊠P(z) W2
W3
F
F
′
η
where η is the natural extension of η to the algebraic completions.
The above universality property implies that a P(z)-tensor product V -module is unique
up to isomorphism.
A P(z)-tensor product space is constructed as follows. Let V be rational in the sense of
[85], that is 1) V admits only finitely many inequivalent irreducible V -modules, 2) every
V -module is completely reducible, 3) the fusion rules associated to triples of irreducible
modules are finite. Then by Prop. 12.5 [85]
W1 ⊠P(z) W2 =
M
i
(M[P(z)]Mi
W1,W2
)
∗ ⊗ Mi (37.14)

228 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
is a P(z)-tensor product module, with (M[P(z)]Mi
W1,W2
)
∗
the dual space of the space of P(z)-
interwining maps of type  Mi
W1 W2

and {Mi} is a complete family of irreducible V -modules.
The vertex operator YW1⊠P (z)W2is the direct sum of the corresponding vertex operators.
Definition 37.7. (Products and iterates of intertwining operators) Intertwining operators Y1 and Y2 associated to different triples of V -modules of types  W4
W1 W5

and  W5
W2 W3

respectively, may be composed in a way similar to composition of elements of a category,
Y1(w
(1), x1)Y2(w(2), x2), (37.15)
(i.e. with the only requirement that the target of Y2 equals the source of Y1.) This
composition is called the product of intertwining operators.
Similarly, intertwining operators Y3 and Y4 of types  W6
W1 W2

and  W4
W6 W3

may be composed along the charge space
Y4(Y3(w
(1), x1 − x2)w(2), x2). (37.16)
This composition is called the iterate.
The product and iterate of intertwining operators give rise to the triple tensor products
W1 ⊠HL (W2 ⊠HL W3) and (W1 ⊠HL W2) ⊠HL W3, respectively, in the following way.
A central property for intertwining operators, called associativity of intertwining operators, a property relating products with iterates. Associativity is very important, and
draws its origin from the Operator Product Expansion, introduced by Belavin, Polyakov
and Zamolodchikov in 2-dimensional conformal field theory [12].
Remark 37.8. Associativity of intertwining operators is referred the (Non-meromorphic)
Operator Product Expansion (OPE) of chiral vertex operators, in the works by Huang and
Lepowsky. Note that in physics literature one often meets OPE for primary fields. Since
primary fields are of main interest for our purposes, to avoid possible confusion, we shall
refer to Huang-Lepowsky associativity as OPE of intertwining operators. See also Def.
37.12 for a reformulation in terms of irreducible modules.
Definition 37.9. (Theorem 14.8 in [88]) Associativity of intertwining operators holds when
for any pair of intertwining operators Y1, Y2 of types  W4
W1 W5

and  W5
W2 W3

respectively there
are W6 and intertwining operators Y3, Y4 of types  W6
W1 W2

and  W4
W6 W3

respectively such
that for any two nonzero complex numbers z1 and z2 satisfying
|z1| > |z2| > |z1 − z2| > 0, (37.17)
and vectors w
(i)
in the corresponding charge spaces we have
Y1(w
(1), z1)Y2(w(2), z2) = Y4(Y3(w(1), z1 − z2)w(2), z2). (37.18)
Moreover, given Y3 and Y4 as above there are W5 and Y1 and Y2 as above such that (37.18)
holds in the same domain.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 229
Remark 37.10. A term of the form of the left hand side of (37.18) is a series with the
summation developed over the graded subspaces of the target of Y2 (or the source of Y1),
and converges absolutely in the weak topology defined by the source of Y2 and the restricted
dual of the target of Y1 if and only if the series at the right hand side of (37.18) converges
absolutely weakly as well. A property implying these equivalent conditions is developed
in [88] and called convergence and extension property. The property is also formulated in
Def. 3.4 in [91]. In that paper, the convergence and extension property has been derived
under certain conditions. In particular in the same paper the author showed that it holds
under the rationality conditions a), b) c) of Sect. 23. Moreover, it was shown in [88] that
associativity of intertwining operators follows from the convergence and extension property.
Thus the convergence and extension property is a main analytical step to construct the
structure of a braided tensor (in fact a braided vertex tensor) category on the category
of modules of a vertex operator algebra. The detailed discussion and derivation of this
property and its connection to systems of differential equations may be found in [91]. We
shall only be concerned with some simple aspects of convergence properties that will be
useful for us to expose the connection between Huang-Lepowsky associativity morphisms
and that arising from quantum groups (cf. Theorem 2.8) in the case of affine vertex
operator algebras.
Definition 37.11. The (W1 ⊗ W2 ⊗ W3 ⊗ (W4)
′
)
′
-valued functions defined by evaluating
the left hand side of (37.18) on vectors of the source space and the restricted dual of the
target space are called 4-point correlation functions.
37.2. Huang-Lepowsky (vertex) tensor category associativity morphisms of Rep(V )
(OPE of intertwining operators and OPE constants F
β
′
,α′
α,β ). As already mentioned,
associativity of intertwining operators has the important consequence, together with some
other properties, that the conditions of Huang and Lepowsky tensor product theory are
verified, and therefore their theory may be applied [85], [86], [87], [84], [89], [88]. It follows
that the P(z)-tensor product module (37.14) extends to vertex tensor category structure
by Theorem 3.7 in [91], which is in fact modular by [90], [93]. To describe this tensor
structure, we follow the exposition given by Gui, Sect. 2.4 in [73].
Let W1, W2, W3 be V -modules and let MMs
W1,Mr
and MMr
W2,W3
be the vector spaces of
intertwining operators of type  Ms
W1 Mr

and  Mr
W2 W3

respectively, with {Mr} a complete
family of irreducible V -modules. Let
Yα ∈ MMs
W1,Mr
Yβ ∈ MMr
W2,W3
(37.19)
be bases for these spaces, respectively, with r varying.
When |z1| > |z2| are nonzero fixed complex numbers, the collection of products {Yα ↾z1
Yβ ↾z2 } is linearly independent. A proof may be found in Prop. 2.3 in [73]. When
the modules Wi are irreducible and the arg-function is chosen continuously then these
intertwining operators are single valued functions. If in addition
|z1| > |z2| > |z1 − z2| > 0

230 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
then there is a basis development of products of intertwining operators with respect to
iterates of intertwining operators independent of the choice of the points, corresponding
as said to the notion of OPE in physics.
Definition 37.12. Given Yα ∈ MMs
W1,Mr
and Yβ ∈ MMr
W2,W3
bases as in (37.19) with r
varying, let
Yα′ ∈ MMi
W1 W2
, Yβ′ ∈ MMs
Mi W3
be bases of the vector spaces MMi
W1 W2
and MMs
Mi W3
respectively, with i varying. The basis
basis development
Yα(w
(1), z1)Yβ(w(2), z2) = X
α′,β′
F
β
′
,α′
α,β Yβ′(Yα′(w
(1), z1 − z2)w(2), z2), (37.20)
is called OPE of intertwining operators. We shall refer to F
β
′
,α′
α,β as the (OPE) structure
constants.
In Huang-Lepowsky theory, the vertex tensor category gives rise to a tensor category.
We shall omit the description of this passage in their work. It will be important for us
to notice that the structure constants F
β
′
,α′
α,β will also be the structure constants for the
associativity morphisms of the associated tensor category structure. We summarize this
passage in the following result, following the exposition in [74].
The OPE of intertwining operators determines the tensor category structure of Rep(V )
as follows. We define the linear map
B = B(W1, W2, W3; s) (37.21)
to emphasize the dependance of B on the variables.
B :
M
r
MMs
W1,Mr ⊗ MMrW2,W3 →
M
i
MMs
Mi W3 ⊗ MMiW1 W2
Yα ⊗ Yβ →
X
α′,β′
F
β
′
,α′
α,β Yβ′ ⊗ Yα′.
Given finite dimensional vector spaces X, Y , we identify the dual space of a direct sum
and a tensor product with
(X ⊕ Y )
∗ ≃ X∗ ⊕ Y∗
, (X ⊗ Y )
∗ ≃ Y∗ ⊗ X∗
.
Finally we set
A = B
t
:
M
i
(MMi
W1 W2
)
∗ ⊗ (MMs
Mi W3
)
∗ →
M
r
(MMr
W2,W3
)
∗ ⊗ (MMs
W1,Mr
)
∗
, (37.22)
with Btthe transpose of B. We shall write
A = A(W1, W2, W3; s). (37.23)
The following is a major achievement of Huang-Lepowsky theory.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 231
Theorem 37.13. (Huang-Lepowsky) Let V be a vertex operator algebra satisfying the the
rationality conditions a), b), c) of Sect. 23, let W1, W2, W3 be V -modules, and let MMi
W1,W2
be the vector space interwining operators of type  Mi
W1 W2

with {Mi} a complete family of
irreducible V -modules. Then
1)
W1 ⊠HL W2 := M
i
(MMi
W1,W2
)
∗ ⊗ Mi
, (37.24)
the vertex operator YW1⊠HLW2is defined as the direct sum of the corresponding vertex
operators. Writing
(W1 ⊠HL W2) ⊠HL W3 =
M
i
(MMi
W1,W2
)
∗ ⊗ (Mi ⊠HL W3) = (37.25)
M
i,s
(MMi
W1,W2
)
∗ ⊗ (MMs
Mi,W3
)
∗ ⊗ Ms
and
W1 ⊠HL (W2 ⊠HL W3) = M
r
(MMr
W2,W3
)
∗ ⊗ (W1 ⊠HL Mr) = (37.26)
M
r,s
(MMr
W2,W3
)
∗ ⊗ (MMs
W1,Mr
)
∗ ⊗ Ms.
then the associativity morphism is given by
αW1,W2,W3 = ⊕sA(W1, W2, W3; s) ⊗ 1Ms.
2) There are natural identifications of the following spaces of intertwining operators
and their duals with corresponding morphism spaces in Rep(V ):
MMi
W1,W2 ≃ HomV (W1 ⊠HL W2, Mi), (MMiW1,W2
)
∗ ≃ HomV (Mi
, W1 ⊠HL W2).
We comment on 2). After the tensor category structure of Rep(V ) has been constructed
then an element φ ∈ (MMi
W1,W2
)
∗
induces a morphism in HomV (Mi, W1 ⊠HL W2) via left
tensor product with φ; and an element T ∈ HomV (Mi, W1 ⊠HL W2) induces a linear
functional on HomV (W1 ⊠HL W2, Mi) via left composition by T in Rep(V ).
37.3. Transporting Huang-Lepowsky vertex tensor category structure to the
Zhu algebra. In this subsection we describe the first step mentioned in Sect. 36, useful
to construct the first tensor equivalence in (2.4). Recall that the first step aims to transport
the vertex tensor category structure of Rep(Vgk) to the Zhu algebra, and preserves all the
structure by construction.
To study associativity morphisms of module categories of vertex operator algebras and
the transported structure to the Zhu algebra, we find it very clarifying the following passage
from composition of intertwining operators to composition of Huang-Lepowsky intertwining maps. This passage is analogous to the case of intertwining operators, see Prop. 37.4,
and an important step to the construction of vertex tensor product theory. We next sketch
Huang-Lepowsky associativity morphisms αHL of the vertex tensor category.

232 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Remark 37.14. In what follows, our notation αHL will correspond to
αHL := (A
P(z1−z2),P(z2)
P(z1),P(z2)
)
−1
of Theorem 14.10 in [88].
Given a branch of the complex logarithm and distinct nonzero complex numbers z1, z2
satisfying (37.17), if associativity of intertwining operators holds as in Def. 37.9 then the
associativity equation (37.18) can be written as
F1 ◦ 1 ⊗ F2 = F4 ◦ F3 ⊗ 1, (37.27)
where F1 and F2 are P(z1)- and P(z2)- intertwining maps corresponding to Y1 and Y2
respectively, and F3 and F4 are P(z1 −z2)- and P(z2)- intertwining maps corresponding to
Y3 and Y4 respectively. The definition of both sides of (37.18) is as series obtained inserting
in the middle projection maps onto the homogeneous subspaces, and is well defined under
convergence conditions. Note indeed that the inner maps have targets in the algebraic
completions of modules. In the construction of their tensor product theory, the study of
products and iterates of intertwining maps is the starting point. For an overview we refer
the reader to [95], and for complete explanations to [88], and references to previous papers
of the same series. In Subsect. 38.3 we discuss in more detail significative examples of
these series for the model V = Vgk.
In terms of decomposition into irreducible modules, with the same notation as in Def.
37.12, equation (37.20) becomes
Fα ◦ 1 ⊗ Fβ =
X
α′,β′
F
β
′
,α′
α,β Fβ′ ◦ Fα′ ⊗ 1, (37.28)
where recall Fα and Fβ are linear bases P(z1)- and P(z2)- intertwining maps of type  Ms
W1 Mr

and  Mr
W2 W3

respectively and Fα′, Fβ′ bases of P(z1 − z2)- and P(z2)- intertwining maps
of type  Mi
W1 W2

and  Ms
Mi W3

respectively. Let
FW2,W3: W2 ⊗ W3 → W2 ⊠P(z2) W3 (37.29)
be the universal P(z2)-intertwining map of type W2⊠P (z2)W3
W2 W3

and
ηβ : W2 ⊠P(z2) W3 → Mr (37.30)
the unique morphism of V -modules derived from Fβ by universality of the P(z2)-tensor
product, see Def. 37.6,
Fβ = ηβ ◦ FW2,W3
. (37.31)
Similarly, we have universal maps and associated V -module morphisms for the various
intertwining maps composing (37.28) as follows;
FW1,Mr: W1 ⊗ Mr → W1 ⊠P(z1) Mr, (37.32)
the universal P(z1)-intertwining of type W1⊠P (z1)Mr
W1 Mr

, and the V -module morphism
ηα : W1 ⊠P(z1) Mr → Ms (37.33)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 233
such that
Fα = ηα ◦ FW1,Mr
; (37.34)
the universal P(z1 − z2)-intertwining
FW1,W2: W1 ⊗ W2 → W1 ⊠P(z1−z2) W2 (37.35)
of type W1⊠P (z1−z2)W2
W1 W2

and the V -module morphism
ηα′ : W1 ⊠P(z1−z2) W2 → Mi (37.36)
such that
Fα′ = ηα′ ◦ FW1,W2
(37.37)
and finally the universal P(z2)-intertwining
FMi,W3: Mi ⊗ W3 → Mi ⊠P(z2) W3 (37.38)
of type Mi⊠P (z2)W3
Mi W3

, the V -module morphism
ηβ′ : Mi ⊠P(z2) W3 → Ms (37.39)
such that
Fβ′ = ηβ′ ◦ FMi,W3
. (37.40)
The following formula gives Huang-Lepowsky associativity morphisms in terms of the
OPE coeffiecients F
β
′
,α′
α,β .
Theorem 37.15. Let ηα, ηβ, ηα′, ηβ′ be the V -module morphisms defined as in (37.30),
(37.31), (37.33), (37.34), (37.36), (37.37), (37.39), (37.40).
Let ξα, ξβ be V -module morphisms with source (range) the range (source) of ηα and ηβ
respectively, and such that such that
X
α
ξαηα = 1,
X
β
ξβηβ = 1. (37.41)
Then Huang-Lepowsky vertex tensor category associativity morphisms are given by
αHL := XF
β
′
,α′
α,β (1W1 ⊠P(z1) ξβ) ◦ ξα ◦ ηβ′ ◦ (ηα′ ⊠P(z2) 1W3
).
The morphisms ξα, ξβ exist by semisimplicity. The naturality of the universal intertwining maps gives the following form of αHL in terms of the universal P(z)-intertwining maps
on distinct points (cf. Theorem 14.10 in [88]).
Theorem 37.16. The associativity equation (37.28) in turn becomes
FW1,W2⊠P (z2)W3 ◦ 1W1 ⊗ FW2,W3 = αHL ◦ FW1⊠P (z1−z2)W2,W3 ◦ FW1,W2 ⊗ 1W3
, (37.42)
where αHL is the extension of αHL to the algebraic completion, FW1,W2
, FW2,W3 are the
universal P(z1 − z2)- and P(z2)- intertwining maps defined in (37.35) and (37.29) respectively and FW1⊠P (z1−z2)W2,W3 and FW1,W2⊠P (z2)W3 are the universal P(z2)-, P(z1)- intertwining maps
FW1⊠P (z1−z2)W2,W3: (W1 ⊠P(z1−z2) W2) ⊗ W3 → (W1 ⊠P(z1−z2) W2) ⊠P(z2) W3, (37.43)

234 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
FW1,W2⊠P (z2)W3: W1 ⊗ (W2 ⊠P(z2) W3) → W1 ⊠P(z1) (W2 ⊠P(z2) W3) (37.44)
defined by naturality in the first and second variable from (37.38), (37.32) respectively.
We next define pointed tensor products on the representation category of the Zhu algebra
Rep(A(V )) with irreducible objects labelled by objects of Rep(V ) by Zhu theorem [197],
inspired by the methods of Prop. 12.5 in [87].
Definition 37.17. Consider the vertex tensor category structure of Rep(V ) transported
to A(V ) as follows. For a non-zero z ∈ C, and irreducible V -modules W1 and W2, set
(W1)(0) ⊠P(z) (W2)(0) := (W1 ⊠P(z) W2)(0),
and let
F0 = F
HL
0
: (W1)(0) ⊗ (W2)(0) → (W1)(0) ⊠P(z) (W2)(0)
be the composition of Huang-Lepowsky universal P(z)-intertwining map
F = F
HL : W1 ⊗ W2 → W1 ⊠P(z) W2
with inclusion and projection onto top level subspaces. Let
Z : Rep(V ) → Rep(A(V ))
be Zhu functor. Let us endow Rep(A(V )) with associativity morphisms
Z(αHL) = XF
β
′
,α′
α,β (1W1 ⊠P(z1) Z(ξβ)) ◦ Z(ξα) ◦ Z(ηβ′) ◦ (Z(ηα′) ⊠P(z2) 1W3
). (37.45)
Let us endow A(V ) with the transported structure as above.
Remark 37.18. Consider the natural transformation associated to Z given by the identity
on the pointed tensor products of irreducible objects. This setting has been described in
Sect. 6 in an abstract form in the case of tensor categories. Theorem 8.25 gives conditions
under which this natural transformation becomes a tensor equivalence. On the other
hand, these conditions are met by an extension of the methods of Sect. 15, regarding the
transport of tensor structure from a tensor category Rep(V ) to the Zhu algebra Rep(A(V ))
to the case of vertex tensor categories. In the following, we shall keep in mind the form of
the associativity morphisms explained in the proof of Theorem 15.7, which is conceptually
more useful than (37.45), although the relevance of the latter resides in the possibility of
defining the OPE coeffiecients F
β
′
,α′
α,β .
Theorem 37.19. Z : (Rep(V ), ⊠P(z), αHL) → (Rep(A(V )), ⊠P(z), Z(αHL)) becomes an
equivalence of vertex tensor categories.
Remark 37.20. An approach to the construction of Def. 37.17 emphasizing Zhu functor
Z and its right inverse has been considered in [127].

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 235
37.4. An equivalence between the tensor category structure on Rep(A(Vgk
)) from
quantum groups as in Theorem 2.8 and from Huang-Lepowsky (vertex) tensor
category. In this subsection we construct an identification of (quasi-tensor equivalence
between) the pre-tensor structure of the transported structure and that arising from quantum groups following Theorem 2.8 and conclude with the second step mentioned in Sec.
36, that is an identification of the two associativity morphisms, one arising from HuangLepowsky theory and the other from Theorem 2.8.
For each nonzero z ∈ C there is a unique isomorphism depending on z
η
z
Z(W1),Z(W2) ∈ HomA(Vgk
)(Z(W1) ⊠ Z(W2), Z(W1) ⊠P(z) Z(W2))
such that the following diagram commutes,
Z(W1) ⊗ Z(W2) Z(W1) ⊠ Z(W2)
Z(W1) ⊠P(z) Z(W2)
F0
F HL
0
η
z
Z(W1),Z(W2)
(37.46)
The map η
z
exists by universality of ⊠-tensor product, see Theorem 33.3. We give a
direct description of η
z
.
In the case of rational vertex operator algebras, Prop. 12.5 in [87] describes P(z)-tensor
product of V -modules. It follows that for a non-zero complex number z, and irreducible
V -modules Wi,
Z(W1) ⊠P(z) Z(W2) = ⊕j (M(z)
Mj
W1,W2
)
∗ ⊗ Z(Mj ) (37.47)
is a V -module, where Mjis a complete family of irreducible V -modules and M(z)
Mj
W1,W2
is
the space of P(z)-intertwining maps of type  Mj
W1 W2

.
Consider the case V = Vgk. Then by Theorem 2.8, Rep(A(Vgk)) is a tensor category.
Recall that the tensor product bifunctor is denoted by ⊠. Thus we have a decomposition
into isotypic components,
Z(W1) ⊠ Z(W2) = ⊕j (HomA(Vgk
)(Z(W1) ⊠ Z(W2), Z(Mj )))∗ ⊗ Z(Mj ). (37.48)
Recall from Sect. 34 the notion of primary field ϕ and initial term Tϕ in the setting of
affine Lie algebras, first introduced in [114] in conformal field theory. See also Sect. 38
for an exposition in the setting of vertex operator algebras. For the affine vertex operator
algebra associated to an affine Lie algebra, the corresponding notions correspond in a
natural way.
The initial term corresponds to the map denoted by fF Z in Theorem 33.3, is a gmorphism satisfying Frenkel-Zhu condition, see also Remark 33.4. (These two properties,
that is faithfulness of f → fF Z and characterization of the image are specific for the case
affine vertex operator algebras at positive integer level.)
By a combination of Prop. 37.4 with Theorem 3.2.3 in [61], M(z)
Mj
W1,W2
is isomorphic to
the space of g-morphisms Z(W1) ⊗ Z(W2) → Z(Mj ) that satisfy Frenkel-Zhu condition.

236 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
An isomorphism is given as follows. Let f ∈ M(z)
Mj
W1,W2
be a P(z) intertwining map.
Consider the corresponding intertwining operator Y, and associate to it the corresponding
primary field ϕ. Consider the initial term T of ϕ and the morphism Tˆ in (Rep(A(Vgk
)), ⊠)
defined in Theorem 34.7.
We obtain an isomorphism by composition
α
Mj
W1,W2
: f ∈ M(z)
Mj
W1,W2 → Tˆ ∈ HomA(Vgk
)(Z(W1) ⊠ Z(W2), Z(Mi)). (37.49)
Consider the dual isomorphism between the dual spaces, rescaled by z
−∆ϕ , with ∆ϕ the
conformal weight of ϕ,
η
z,Z(Mj )
Z(W1),Z(W2)
: ϕ ∈ (HomA(Vgk
)(Z(W1)⊠Z(W2), Z(Mj )))∗ → z
−∆ϕ ϕ◦α
Mj
W1,W2
∈ (M(z)
Mj
W1,W2
)
∗
.
With respect to (37.47), (37.48), set
η
z
Z(W1),Z(W2)
:= ⊕jη
z,Z(Mj )
Z(W1),Z(W2) ⊗ 1Z(Mj )
.
Then η
z
Z(W1),Z(W2)
is an isomorphism in Rep(A(Vgk
)) between the two tensor product representations
η
z
Z(W1),Z(W2)
: Z(W1) ⊠ Z(W2) → Z(W1) ⊠P(z) Z(W2)
and makes the diagram (37.46) commutative.
We extend η
z
to an (invertible) natural transformation on all pairs of objects of Rep(A(Vgk)).
Then η
z
is a natural transformation between the two tensor product bifunctors
(Rep(A(Vgk)), ⊠P(z)) → (Rep(A(Vgk)), ⊠) (37.50)
Theorem 37.21. Let us consider (Rep(A(Vgk)), ⊠P(z), Z(αHL)) as a vertex tensor category as in Def. 37.17. Then (Rep(A(Vgk
)), ⊠) becomes a tensor category with the unique
associativity morphisms (Rep(A(Vgk)), ⊠, αˆHL) making the identity functor with natural
transformation η of (37.50) into a tensor equivalence.
Recall from Theorem 37.19 that
Z : (Rep(Vgk), ⊠P(z), αHL) → (Rep(A(Vgk)), ⊠P(z), Z(αHL))
is an equivalence of vertex tensor categories.
Corollary 37.22. Consider (Rep(Vgk), ⊠HL, αHL) with tensor category structure associated
to the vertex tensor category (Rep(Vgk), ⊠P(z), αHL) of [84], sketched in Theorem 37.13.
Then one obtains a natural equivalence of tensor categories
(Rep(Vgk), ⊠HL, αHL) → (Rep(A(Vgk)), ⊠, αˆHL).
A computation using the definition of tensor equivalence given as a special case of (4.8)
and naturality of η gives the following formula for ˆαHL.
Proposition 37.23. The associativity morphisms of the tensor category (Rep(A(Vgk)), ⊠, αˆHL)
are given by
(ˆαHL)Z(W1),Z(W2),Z(W3) =
X F
β
′
,α′
α,β 1Z(W1) ⊠ ˆξβ ◦
ˆξα ◦ ηˆβ′ ◦ ηˆα′ ⊠ 1Z(W3)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 237
where
ηˆα′ = Z(ηα′)ηZ(W1),Z(W2) ∈ HomA(Vgk
)(Z(W1) ⊠ Z(W2), Z(Mi)),
ηˆβ′ = Z(ηβ′)ηZ(Mi),Z(W3) ∈ HomA(Vgk
)(Z(Mi) ⊠ Z(W3), Z(Ms)),
ˆξα = η
−1
Z(W1),Z(Mr)Z(ξα) ∈ HomA(Vgk
)(Z(Ms), Z(W1) ⊠ Z(Mr)),
ˆξβ = η
−1
Z(W2),Z(W3)Z(ξβ) ∈ HomA(Vgk
)(Z(Mr), Z(W2) ⊠ Z(W3)).
Proof. Writing M in place of Z(M) for all modules of the Zhu algebra,
Zˆ(αHL) = 1W1 ⊠ η
−1
W2,W3
◦ η
−1
W1,W2⊠P (z2)W3
◦ Z(αHL) ◦ ηW1⊠P (z1−z2)W2,W3 ◦ ηW1,W2 ⊠ 1W3 =
XF
β
′
,α′
α,β 1W1 ⊠ η
−1
W2,W3
◦ η
−1
W1,W2⊠P (z2)W3
◦ (1W1 ⊠P(z1) Z(ξβ)) ◦ Z(ξα) ◦ Z(ηβ′)◦
(Z(ηα′) ⊠P(z2) 1W3
)) ◦ ηW1⊠P (z1−z2)W2,W3 ◦ ηW1,W2 ⊠ 1W3 = XF
β
′
,α′
α,β 1W1 ⊠ (η
−1
W2,W3
Z(ξβ)) ◦ (η
−1
W1,Mr
Z(ξα)) ◦ (Z(ηβ′)ηMi,W3
) ◦ (Z(ηα′)ηW1,W2
) ⊠ 1W3 = X F
β
′
,α′
α,β 1W1 ⊠ ˆξβ ◦
ˆξα ◦ ηˆβ′ ◦ ηˆα′ ⊠ 1W3
.
□
To describe the associativity morphisms ˆαHL of (Rep(A(Vgk
)), ⊠) we need to describe
the tensor equivalence of Theorem 37.22.
This tensor equivalence is built on the following important two constructions on the
Zhu algebra A(Vgk), among the number of constructions that we have outlined. The
representation category of this algebra is endowed with the structure of a vertex tensor
category induced by Huang-Lepowsky theory, a family of tensor product bifunctors and
associativity morphisms that depend on the variable z, as in Def. 37.17.
Huang-Lepowsky associativity morphisms αHL are morphisms in Rep(Vgk),
αHL : (W1 ⊠P(z1−z2) W2) ⊠P(z2) W3 → W1 ⊠P(z1) (W2 ⊠P(z2) W2)
such that the extension αHL is determined by the universal intertwining maps defined from
complete tensor products of vector spaces ⊗ as in Theorem 37.16. By Theorem 37.13,
FW1⊠P (z1−z2)W2,W3 ◦ FW1,W2 ⊗ 1W3
:
W1 ⊗ W2 ⊗ W3 →
M
i,s
(M(P(z1 − z2))Mi
W1 W2
)
∗ ⊗ (M(P(z2))Ms
Mi W3
)
∗ ⊗ Ms,
FW1,W2⊠P (z2)W3 ◦ 1W1 ⊗ FW2,W3:
W1 ⊗ W2 ⊗ W3 →
M
r,s
(M((P(z2))Mr
W2,W3
)
∗ ⊗ (M(P(z1))Ms
W1,Mr
)
∗ ⊗ Ms.
Using the indicated decomposition into irreducible V -modules, the top level subspace of
the domain of αHL is obtained in two stages as the direct sum of the top level subspaces
of the decomposition of W1 ⊠P(z1−z2) W2 and Mi ⊠P(z2) W3. The top level subspace of
W1⊠P(z1−z2)W2 that we are interested in for the Zhu algebra only arises from the restriction
of the universal P(z1 − z2)-intertwining map FW1,W2to Z(W1) ⊗ Z(W2), and similarly for
the top level subspace of Mi ⊠P(z2) W3.

238 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The result is
M
i,s
(M(P(z1 − z2))Mi
W1 W2
)
∗ ⊗ (M(P(z2))Ms
Mi W3
)
∗ ⊗ Z(Ms).
By definition, Z(αHL) is the restriction of αHL to the top level subspace of the triple tensor
product, see Remark 37.18 and the indicated reference therein to the proof of Theorem
15.7 for the associativity morphisms. Thus Z(αHL) acts on vectors of the kind
(F
0
HL)W1⊠P (z1−z2)Z(W2),Z(W3) ◦ (F
0
HL)Z(W1),Z(W2) ⊗ 1Z(W3)(w
(1) ⊗ w(2) ⊗ w(3)),
with w
(i) ∈ Z(Wi). As before, F0
HL denotes the restriction of the P(ζ)-intertwining map F
to the tensor product of top level subspaces for the suitable ζ.
We have a connection between the two structure maps the variable dependent F
HL
0
and
the constant F0, given by the natural transformation η
z
in (37.46).
Using the natural transformation η
ζ
for the suitable ζ, it follows that ˆαHL acts on vectors
of the kind
(F
0
)W1⊠Z(W2),Z(W3) ◦ (F
0
)Z(W1),Z(W2) ⊗ 1Z(W3)(w
(1) ⊗ w(2) ⊗ w(3)),
where F
0
is part of the weak quasitensor structure of Zhu functor constructed in Theorem
2.8. In terms of the irreducible decomposition, these are vectors of the space
M
i,s
(HomA(Vgk
)(W1 ⊠ W2, Mi))∗ ⊗ (HomA(Vgk)(Mi ⊠ W3, Ms))∗ ⊗ Z(Ms).
The action of ˆαHL is defined by a formula similar to (37.42) with F0, Z(Wi), ˆαHL in place
of F, Wi αHL respectively. We ask whether this is of CFT-type. By Remark 8.5, we need
to show that the inclusion map G0 of weak-quasi-tensor structure constructed in Theorem
2.8, is compatible with ˆαHL. Recall from Sect. 30 that the weak tensor structure associated
to Wenzl functor is non-unique, and correspondingly G0 is non-unique. One may then try
to choose accordingly G0 and try to construct a weak tensor structure for Zhu functor. We
shall avoid to go into these details, and we restrict to the specific situation where
(Z(W1), Z(W2), Z(W3)) ∈ V,
where as before V is constituted by the triples of the form
(Vλ, V, V ), (V, Vλ, V ), (V, V, Vλ)
with V the fundamental representation of g and Vλ an irreducible representation of g in
the open Weyl alcove. By the results of Sects. 8, 2 we shall content ourselves of showing
that ˆαHL arises from V-pre-associator of CFT-type. This is a simpler situation, in that
in this case G0 is uniquely determined for all Lie type for g ̸= E8 by the work of Wenzl
already widely used in the first part of this paper. For pairs of the first two kinds, we shall
use the analogue (37.42) previously described, while for pairs of the third kind we shall
use an equation derived from (37.42) multiplying in the left by αHL
−1
. In the case g = E8
Wenzl give a construction of (F, G) in the setting of quantum groups, and accordingly also
for (F0, G0), in the proof at the Proposition at page 274 in [185]. Then one may work in
the same way in the setting of affine Lie algebras.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 239
Theorem 37.24. We have that αˆHL is an associativity morphism of Rep(A(Vgk
)) corresponding to a V-pre-associator of CFT-type for the triple (Z, F0, G0).
It follows from Theorem 8.21 that the proof of the two steps described in Sect. 36 is
complete, and with them the proof of part c) of Theorem 2.8 and 2.11.
Remark 37.25. The induced Huang-Lepowsky vertex tensor category construction on
Rep(A(Vgk
) with the vertex tensor category structure may be regarded as associated to a
variable dependent family of weak quasi-bialgebra construction on A(Vgk
), a variable dependent family of coproducts and associators (∆z, Φ
z1,z2
(z1−z2),z2
). It is natural to ask whether
this is related to Moore-Seiberg conjecture on a quantum group interpretation in conformal
field theory in Section 9 of [130]. We shall come back to this in more detail in Remark
38.8.
