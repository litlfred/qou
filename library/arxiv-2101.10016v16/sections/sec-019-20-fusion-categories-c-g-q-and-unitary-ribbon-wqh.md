---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-019-20-fusion-categories-c-g-q-and-unitary-ribbon-wqh
section_title: "Fusion categories C(g, q, ℓ) and unitary ribbon wqh via integral wdf"
section_number: 20
pages: 129-131
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
20. Fusion categories C(g, q, ℓ) and unitary ribbon wqh via integral wdf
20.1. The open Weyl alcove Λ
+(q) and negligible tilting modules. We follow Gelfand
and Kazhdan for the construction of the quotient category [70]. Every object of T(g, q, ℓ)
decomposes into a direct sum of indecomposable submodules, and this decomposition is
unique up to isomorphism. One can form two full linear subcategories, T
0
, and T
⊥ of
T(g, q, ℓ), with objects, respectively, those representations which can be written as direct
sums of Vλ, with λ ∈ Λ
+(q) only, and those which have no such Vλ as a direct summand.

130 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The objects of T
⊥ and T0 are called negligible and non-negligible, respectively. A morphism T : W → W′ of T(g, q, ℓ) is called negligible if it is a sum of morphisms that factor
through W → N → W′ with N negligible.
The category T
⊥ of negligible modules satisfies the following properties, [2, 70], that we
call Gelfand-Kazhdan properties,
(1) Any object W ∈ T(g, q, ℓ) is isomorphic to a direct sum W ≃ W0 ⊕ N with W0 ∈ T
0
and N ∈ T
⊥.
(2) For any pair of morphisms T : W1 → N, S : N → W2 of T(g, q, ℓ), with N ∈ T
⊥,
Wi ∈ T
0
, then ST = 0.
(3) For any pair of objects W ∈ Tℓ(g), N ∈ T
⊥, then W ⊗ N and N ⊗ W ∈ T⊥.
We shall extensively use the previous properties to construct the weak Hopf algebras
AW (g, q, ℓ) in Sect. 32.
Property (1) follows easily from the mentioned decomposition of objects of T(g, q, ℓ),
while property (2) means that no non-negligible module can be a summand of a negligible
one (however, it can be a factor of a Weyl filtration of a negligible).
We recall that negligible indecomposable tilting modules are characterized by the property of having zero quantum dimension. A morphism T : W → W′
is negligible if and only
if TrW (ST) = 0 for all morphisms S : W′ → W.
Remark 20.1. In particular, for λ, µ ∈ Λ
+(q),
Vλ(q) ⊗ Vµ(q) = ⊕γ∈Λ+(q)m˜
λ,µ
γ Vγ(q) ⊕ N
with N ∈ T
⊥. The multiplicities ˜mλ,µ
γ
are given by the quantum Racah formula, Sect.
5 [161]. In particular, ˜mλ,µ
γ depends on the affine Weyl group Wℓ
′. It follows from the
description of Wℓ
′ given in Lemma 1 of [161] that this group depends only on g and the
order ℓ of q
2
, thus the same holds for ˜mλ,µ
γ
.
20.2. The quotient category C(g, q, ℓ). Let Neg(W, W′) be the subspace of negligible
morphisms of (W, W′). Then the quotient category, C(g, q, ℓ), is the category with the same
objects as T(g, q, ℓ) and morphisms between the objects W and W′the quotient space,
(W, W′)C(g,q,ℓ):= (W, W′)/Neg(W, W′).
Gelfand and Kazhdan endow C(g, q, ℓ) with the unique structure of a tensor category such
that the quotient map T(g, q, ℓ) → C(g, q, ℓ) is a tensor functor. The tensor product of
objects and morphisms of C(g, q, ℓ) is usually denoted by W⊗W′ and S⊗T respectively,
and referred to as the truncated tensor product in the physics literature. This is now a
semisimple tensor category and {Vλ, λ ∈ Λ
+(q)} is a complete set of irreducible objects.
In C(g, q, ℓ) we have
Vλ⊗Vµ ≃ ⊕ν∈Λ+(q)m˜
ν
λ,µVν.
Notice that this decomposition of Vλ ⊗ Vν is unique up to isomorphism but not canonical
(cf. [185], and also Sect. 11.3C in [24] and references therein.)
The ribbon structure of C(g, q, ℓ) is induced by that of the tilting category. Also the
formulas for the fusion coefficients and quantum dimensions are well-known, and regulated

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 131
by the affine Weyl group in the sense mentioned in Sect. 19.2, see Sect. 2, 5 of [161], but
we shall only need them in some special cases later on, so we refrain from recalling them in
full generality. Those fusion rules indeed pass to the C(g, q, ℓ) and give the fusion rules for
this category, However, it will be important for us to recall that C(g, q, ℓ) depends on q but
the Grothendieck semiring R(C(g, q, ℓ)) depends only on ℓ. We shall refer to R(C(g, q, ℓ))
as the Verlinde fusion ring.
20.3. Modularity and unitarizability. Further properties of modularity C(g, q, ℓ) depend on on the choice of q
1/L as a primitive root of unity of order ℓ′L and on the order ℓ′
of q. We refer to the papers by Rowell and Sawin [158, 161] for a detailed treatment. For
example the cases where 2d|ℓ
′ give modular categories and this is the case of most physical
interest, and also that meeting the purpose of our paper.
More in particular, we shall mostly be interested in the“minimal roots” .
Definition 20.2. Let q be a complex root of unity and let ℓ be the order of q
2
. We shall
say that q is a minimal root if q is of the form
q = e
iπ/ℓ, q1/L = eiπ/ℓL, d|ℓ.
Indeed if q is a minimal root and if in addition ℓ is large enough as in Def. 19.1, then
C(g, q, ℓ) becomes a unitary ribbon fusion category (that we sometimes denote by C
+(g, q, ℓ)
to stress the unitary structure) for all levels k = ℓ/d − h
∨ ≥ 1 for g ̸= E8 and k ≥ 2 for
g = E8 by [185].
20.4. A general construction, the wqh algebras A(g, q, ℓ). We introduce the function
D on the Grothendieck ring of C(g, q, ℓ), which assigns the vector space dimension of the
corresponding representation of g to each irreducible λ ∈ Λ
+(q). It follows easily from the
quotient construction and from the fact that every tilting module decomposes uniquely
up to isomorphism into a direct sum of indecomposable tilting modules, that D is indeed
a weak dimension function on C(g, q, ℓ). We shall refer to it as the classical dimension
function. We may then apply Theorem 7.9 and we have, up to isomorphism and twist, a
finite dimensional weak quasi-Hopf C
∗
-algebra A(g, q, ℓ). We next fix a root of unity of
the form q = e
iπ/ℓ with d|ℓ. Then by [185, 193], and Theorem 13.10 A(g, q, ℓ) becomes a
unitary weak quasi-Hopf algebra.
We shall return to specific constructions of weak Hopf algebras associated to C(g, q, ℓ)
in Sects. 31 and 32.
