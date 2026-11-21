---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-015-51-the-yang-baxter-equation-and-quasi-triangular
section_title: "The Yang-Baxter equation and quasi-triangular bialgebras"
section_number: 5.1
pages: 22-26
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
The Yang-Baxter equation and quasi-triangular bialgebras
The Yang-Baxter equation was originally introduced in the ﬁeld of statistical mechanics. Solu-
tions to this equation provide a systematic way to construct representations of the braid groups
Bn. We will introduce the notion of quasi-triangular bialgebra, and explain that these are alge-
braic structures with the property that their modules are naturally endowed with solutions to
the Yang-Baxter equation.
Deﬁnition 5.1. Let V be a complex vector space. An automorphism R of V ⊗V is called an
r-matrix if it satisﬁes the Yang-Baxter equation:
(R ⊗id) ◦(id ⊗R) ◦(R ⊗id) = (id ⊗R) ◦(R ⊗id) ◦(id ⊗R) ∈End(V ⊗3).
Lemma 5.2. Given an r-matrix R ∈Aut(V ⊗V ), there is a representation
ρR : Bn →Aut(V ⊗n),
deﬁned by:
σi 7→idi−1 ⊗R ⊗idn−i−1.
Proof. The identity
ρ(σi)ρ(σi+1)ρ(σi) = ρ(σi+1)ρ(σi)ρ(σi+1),
follows from the fact that R satisﬁes the Yang-Baxter equation. The relation σiσj = σjσi if
|i −j| > 2 is clear from the form of the map ρR.
□
Let us now introduce some algebraic deﬁnitions.
Deﬁnition 5.3. A bialgebra is a tuple (A, µ, η, ∆, ϵ) where:
• A is a vector space over C.
• µ is map A ⊗A →A, called the product.
• η is a map C →A, called the unit.
• ∆is a map ∆: A →A ⊗A, called the coproduct.
• ϵ is a map A →C, called the counit.
Satisfying the conditions:
• (A, µ, η) is a unital associative algebra.
• (A, ∆, ϵ) is a counital coassociative coalgebra.
• ∆: A →A ⊗A is a morphism of associative algebras.
Of course, we will abuse the notation and simply say that A is a bialgebra.
Example 5.4. We have already encountered an important example of a bialgebra, the universal
enveloping algebra U(g) of a Lie algebra g. Recall that the coproduct is the unique algebra
homomorphism ∆: U(g) →U(g) ⊗U(g), with the property that ∆(x) = 1 ⊗x + x ⊗1, for any
x ∈g. The bialgebra U(g) is cocommutative but in general it is not commutative.
Given modules V, W of a bialgebra A, the vector space V ⊗W, is also a module of A with
action given by:
a(v ⊗w) := ∆(a)(v ⊗w).
Thus, bialgebras are algebras for which the category of modules admits a tensor product. In
general, the modules V ⊗W and W ⊗V need not be isomorphic. In case the coproduct ∆is
cocommutative, the linear map
τV,W : V ⊗W →W ⊗V,
v ⊗w 7→w ⊗v,
is an isomorphism of A-modules.
The condition that A is cocommutative is suﬃcient, but
not necessary in order to have consistent isomorphism of A-modules V ⊗W ∼= W ⊗V . This
consideration leads to the following deﬁnition:
Deﬁnition 5.5. An almost-cocommutative bialgebra is a bialgebra (A, µ, η, ∆, ϵ) together with
an invertible element R ∈A ⊗A, called the universal r-matrix, such that for any a ∈A:
τA,A ◦∆(a) = R∆(a)R−1,
where τA.A : A ⊗A →A ⊗A is given by a ⊗b 7→b ⊗a.
Given an almost-cocommutative bialgebra, and modules V, W the map
τR,V,W := τV,W ◦R : V ⊗W →W ⊗V,
is an isomorphism of A-modules. Thus, an almost-cocommutative bialgebra is a bialgebra for
which there are natural isomorphisms of A-modules V ⊗W ∼= W ⊗V .
Let us now consider A-modules V, W, Z. There are several ways to obtain isomorphisms of A-
modules between V ⊗W ⊗Z and W ⊗V ⊗Z, and it is natural to expect that these isomorphisms
should coincide. Namely, one would expect the following diagrams to commute:
V ⊗W ⊗Z
τR,V,W ⊗Z
/
τR,V,W ⊗id

W ⊗Z ⊗V
id

W ⊗V ⊗Z
id⊗τR,V,Z
/ W ⊗Z ⊗V
(1)
V ⊗W ⊗Z
τR,V ⊗W,Z
/
id⊗τR,W,Z

Z ⊗V ⊗W
id

V ⊗Z ⊗W
τR,V,Z⊗id / Z ⊗V ⊗W
(2)
The commutativity of these diagrams can be assured by imposing conditions on the universal
r-matrix R. This leads to the following deﬁnition.
Deﬁnition 5.6. A quasi-triangular bialgebra is an almost-cocommutative bialgebra A such that
the universal r-matrix R ∈A ⊗A satisﬁes the equations:
(∆⊗id)R = R13R23.
(id ⊗∆)R = R13R12.
Here R12 = R ⊗1, R23 = 1 ⊗R and R13 = (τA,A ⊗id)(R23) = (id ⊗τA,A)(R12).
Example 5.7. The simplest example of a quasi-triangular bialgebra is a cocommutative bial-
gebra, with r-matrix R = 1 ⊗1. Thus, the universal enveloping algebra U(g) of a Lie algebra g
is a quasi-triangular bialgebra.
Remark 5.8. The deﬁnition of a quasi-triangular bialgebra is designed to guarantee that the
category of modules has a well behaved tensor product. Namely, a tensor product with natural
isomorphisms
CV W : V ⊗W ∼= W ⊗V,
for which the diagrams (1) and (2) commute. This kind of category is known as a braided
monoidal category. Observe that in diagrams (1) and (2) expressions of the type V ⊗W ⊗Z
appear. This notation is using implicitly that the natural isomorphisms of vector spaces:
(V ⊗W) ⊗Z ∼= V ⊗(W ⊗Z)
are isomorphism of representations. In more generality, one may consider the case where there
are natural isomorphisms of representations
(V ⊗W) ⊗Z ∼= V ⊗(W ⊗Z),
which are not the obvious isomorphisms of vector spaces.
This corresponds to the general
deﬁnition of braided monoidal category. The algebraic structure on A that guarantees that the
category of modules is a braided monoidal category is that of a quasi-triangular quasi-bialgebra.
Note that the fact that for a bialgebra the obvious linear isomorphism (V ⊗W)⊗Z ∼= V ⊗(W ⊗Z)
is a morphism of modules corresponds to the fact that the coproduct is coassociative. Thus, in
a quasi-triangular quasi-bialgebra one does not require ∆to be strictly coassociative. Instead,
there is an element φ ∈A ⊗A ⊗A, called the Drinfeld associator, which controls the lack of
associativity much in the same way in which R controls the lack of commutativity. We will not
discuss the details of these elegant structures here. The interested reader may consult Kasssel’s
book [16].
Proposition 5.9. Let A be a quasi-triangular bialgebra with universal r-matrix R ∈A ⊗A.
Given A-modules V, W, Z there are isomorphisms of A-modules:
τR,V,W : V ⊗W →W ⊗V,
deﬁned by:
τR,V,W := τV,W ◦R,
satisfying the equations:
(τR,V ⊗W,Z) = (τR,V,Z ⊗id) ◦(id ⊗τR,W,Z),
(3)
(τR,V,W⊗Z) = (id ⊗τR,V,Z) ◦(τR,V,W ⊗id),
(4)
(τR,W,Z ⊗id) ◦(id ⊗τR,V,Z) ◦(τR,V,W ⊗id) = (id ⊗τR,V,W ). ◦(τR,V,Z ⊗id) ◦(id ⊗τR,W,Z). (5)
Proof. Let us ﬁrst check that τR,V,W is an isomorphism of A-modules. Since R is invertible,
τR,V,W is an invertible linear map. Let us check that it is A-linear:
τR,V,W (a(v ⊗w))
=
τR,V,W (∆(a)(v ⊗w)) = τV,W ◦R ◦∆(a)(v ⊗w)
=
τV,W ◦τA,A(∆(a)) ◦R(v ⊗w) = ∆(a) ◦τV,W ◦R(v ⊗w)
=
a ◦τR,V,W (v ⊗w).
Equations (3) and (4) are analogous. Let us prove equation (3). For this we use the fact that
(∆⊗id)(R) = R13R23, and compute:
(τR,V,Z ⊗id) ◦(id ⊗τR,W,Z)
=
(τV,Z ◦R ⊗id) ◦(id ⊗τW,Z ◦R)
=
(τV,Z ⊗id) ◦R12 ◦(id ⊗τW,Z) ◦R23
=
(τV,Z ⊗id) ◦(id ⊗τW,Z)(id ⊗τA,A)(R12) ◦R23
=
(τV,Z ⊗id) ◦(id ⊗τW,Z)R13 ◦R23
=
(τV,Z ⊗id) ◦(id ⊗τW,Z)(∆⊗id)R
=
(τV ⊗W,Z) ◦(∆⊗id)R
=
τR,V ⊗W,Z.
Let us now prove equation (5). We compute:
(τR,W,Z ⊗id)
◦
(id ⊗τR,V,Z) ◦(τR,V,W ⊗id) =
=
(τW,Z ⊗id) ◦R12 ◦(id ⊗τV,Z) ◦R23 ◦(τV,W ⊗id) ◦R12
=
(τW,Z ⊗id) ◦R12 ◦(id ⊗τV,Z) ◦(τV,W ⊗id) ◦R13 ◦R12
=
(τW,Z ⊗id) ◦(id ⊗τV,Z) ◦R13 ◦(τV,W ⊗id) ◦R13 ◦R12
=
(τW,Z ⊗id) ◦(id ⊗τV,Z) ◦(τV,W ⊗id) ◦R23 ◦R13 ◦R12
=
(τW,Z ⊗id) ◦(id ⊗τV,Z) ◦(τV,W ⊗id) ◦R23 ◦R13 ◦R12.
On the other hand:
(id ⊗τR,V,W )
◦
(τR,V,Z ⊗id) ◦(id ⊗τR,W,Z) =
=
(id ⊗τV,W ) ◦R23 ◦(τV,Z ⊗id) ◦R12 ◦(id ⊗τW,Z) ◦R23
=
(id ⊗τV,W ) ◦R23 ◦(τV,Z ⊗id) ◦(id ⊗τW,Z) ◦R13 ◦R23
=
(id ⊗τV,W ) ◦(τV,Z ⊗id) ◦R13 ◦(id ⊗τW,Z) ◦R13 ◦R23
=
(id ⊗τV,W ) ◦(τV,Z ⊗id) ◦(id ⊗τW,Z) ◦R12 ◦R13 ◦R23.
Clearly,
(τW,Z ⊗id) ◦(id ⊗τV,Z) ◦(τV,W ⊗id) = (id ⊗τV,W ) ◦(τV,Z ⊗id) ◦(id ⊗τW,Z).
Therefore, it suﬃces to prove that:
R23R13R12 = R12R13R23.
For this we compute:
R12R13R23
=
R12(∆⊗id)R
=
(R ⊗1)(∆⊗id)R
=
(τA,A ⊗id)(∆⊗id)(R)R12
=
(τA,A ⊗id)(R13R23)R12
=
R23R13R12.
This completes the proof.
□
Corollary 5.10. Let A be a quasi-triangular bialgebra with universal r-matrix R, and V a
module over A. Then τR,V,V ∈AutA(V ) is a solution of the Yang-Baxter equation. In particular,
the vector space V ⊗n is a representation of the braid group Bn.
