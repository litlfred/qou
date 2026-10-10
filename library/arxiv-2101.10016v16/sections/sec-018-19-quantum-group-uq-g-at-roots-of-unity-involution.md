---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-018-19-quantum-group-uq-g-at-roots-of-unity-involution
section_title: "Quantum group Uq(g) at roots of unity, ∗-involution, classical limit"
section_number: 19
pages: 121-129
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
19. Quantum group Uq(g) at roots of unity, ∗-involution, classical limit
Let g be a complex simple Lie algebra and q a primitive complex root of unity. We denote
by ℓ the order of q
2
. Let Uq(g) be the quantized universal enveloping algebra in the sense
of Lusztig, see below for a definition and references. It is known that the category of finite
dimensional representations of Uq(g) is not semisimple, but it gives rise to a semisimple
ribbon fusion category that we denote by C(g, q, ℓ) following [158]. Moreover, the categories
C(g, q, ℓ) are known to be modular for certain values of q see [2, 3, 70, 155, 158, 161] and
references therein, see also Subsects. 19.1–19.3.
Furthermore, by work of Kirillov, Wenzl, Xu one can construct a unitary ribbon category
C
+(g, q, ℓ) equivalent to C(g, q, ℓ) for certain primitive roots of unity, that we call the
minimal roots and precisely define in the following Def. 20.2. [111, 185, 194].
In this section we construct semisimple weak quasi-Hopf algebras associated to C(g, q, ℓ)
and unitary weak quasi-Hopf algebras associated to C
+(g, q, ℓ) when q is a minimal root.
Our approach may broadly be summarized as follows.
From the categories C(g, q, ℓ), we construct weak quasi-tensor functors to the category
of vector spaces and then we use Tannaka-Krein reconstruction to obtain our examples.
We shall do this following two alternative approaches, and both turn out useful for us
in the study of unitary tensor categories. The first approach goes back to [125, 166, 82].
It consists in identifying a certain integral valued weak dimension function D on C(g, q, ℓ),
and then we apply the abstract reconstruction result, Theorem 7.9. This leads to the
construction of a ribbon weak quasi-Hopf algebra A(g, q, ℓ) corresponding to C(g, q, ℓ) which
is defined up to twist and isomorphism. Moreover, when q is a minimal root, we apply

122 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Theorem 13.5 and we obtain a unitary structure A+(g, q, ℓ) on A(g, q, ℓ). By the results of
Sect. 15 this general approach addresses the study of unitary structures via the associator.
It follows that this viewpoint will turn out fruitful for the construction of unitary ribbon
structures for representation categories of affine VOA in Sect. 23. It perhaps conveys the
idea of the amount of information needed to obtain these unitary structures from other
sources for which they are known to exist.
A second approach consists in identifying a natural functor W : C(g, q, ℓ) → Vec associated to the same dimension function D as before, and thus it is a particular case of the
former, and will be studied in Sect. 32.
When q is a minimal root, the work of [185] shows that Uq(g) is a Hermitian coboundary
Hopf algebra with compatible involution (in a topological sense). We shall introduce this
notion in Sect. 32 and summarize this result in Theorem 31.9. However, in this section we
shall not need to go into these details.
19.1. Quantum groups at roots of unity, the real form U
†
A′(g) and ribbon structure. We briefly recall the basic results on quantum groups at roots of unity that we shall
need. For a complete presentation we refer to [24, 120].
Let g be a f.d. complex simple Lie algebra, and q a complex root of unity whose order
we denote by ℓ
′
. (Thus the order ℓ of q
2
is given by ℓ = ℓ
′
if ℓ
′
is odd and ℓ = ℓ
′/2 if
ℓ
′
is even.) Note that our ℓ has the same meaning in [158], our ℓ corresponds to ℓ
′
(and
conversely) in [161], [174]. We anticipate an important lower bound condition that we
require on ℓ, that will be briefly explained immediately after the introduction of background
material on Drinfeld-Jimbo quantum group, their specialization at a root of unity and their
representation theory.
Definition 19.1. We shall say that the order ℓ of q
2
is large enough if ℓ > h when ℓ is
not divisible by d and ℓ > dh∨ otherwise, with h the Coxeter number and h
∨
the dual
Coxeter number of g. We define the positive integer k by ℓ = d(h
∨ +k) if d|ℓ and ℓ = h+k
otherwise, and refer to k as the level associated to ℓ. We define ℓ = k = ∞ if q is not a
root of unity.
The level k introduced in Def. 19.1 is an important parameter for its relation with affine
Lie algebras or affine vertex operator algebras. We are mainly interested in the case ℓ
divisible by d, but also the case of other type of larger orders of roots of unity (possibly
also of infinite order) will be important for us to connect modules of Uq(g) with modules
of a corresponding vertex operator algebra at fixed level k.
Provided q
2 has finite order ℓ large enough, we shall recall in Theorem 19.6 that the corresponding Weyl alcove Λ+(q) labels the irreducible objects of the fusion category C(g, q, ℓ).
The dominant weights belonging to the alcove will correspond to simple modules with
positive quantum dimension.
In particular, quantised Weyl modules Vλ(q) with λ in Λ+(q) are simple, with a positive
definite hermitian form, by Prop. 2.4 in [185].
The category of tilting modules was first introduced by Andersen [2]. This category
admits an alternative definition as noted by Wenzl in [185], as the category of direct sums of

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 123
direct summands of full tensor powers of a specific generating representation V (q) for each
Lie type, for convenience we recall this fact in Theorem 31.12. This is the definition that
we will also adopt. It gives the category C(g, q, ℓ) a perhaps non-commutative geometric
aspect, that will be crucial to connect with the fusion categories of the corresponding
vertex operator algebra.
As noted in [185], the basic requirement that makes the mentioned alternative definition
work, is that ℓ be sufficiently large so that V (q) belongs to the Weyl alcove Λ+(q) corresponding to q. So we need to determine the minimal order ℓ of q
2 divisible by d so that
V (q) belongs to the Weyl alcove Λ+(q) for each Lie type. We shall see in Prop. 31.13 that
this requirement on V (q) puts essentially no lower bound on the level k (and that ℓ will
automatically satisfy Def. 19.1) for all the Lie types (with the only exception of E8, for
which the minimum allowed level is 2).
Let h a Cartan subalgebra, α1, . . . , αr a set of simple roots, and A = (aij ) the associated
Cartan matrix. Consider the unique invariant symmetric and bilinear form on h
∗
such that
⟨α, α⟩ = 2, for a short root α (19.1)
and let θ denote the highest root. Let E be the real vector space generated by the roots
endowed with its euclidean structure ⟨x, y⟩. Let Λ be the weight lattice of E and Λ+ the
cone of dominant weights.
Consider the complex ∗–algebra A = C[x, x−1] of Laurent polynomials with involution
x
∗ = x−1
, and let C(x) be the associated quotient field, endowed with the involution
naturally induced from C[x, x−1]. We consider Drinfeld-Jimbo quantum group Ux(g), i.e.
the algebra over C(x) defined by generators Ei, Fi, Ki, K−1
i
, i = 1, . . . , r, and relations
KiKj = KjKi, KiK−1
i = K−1i Ki = 1,
KiEjK−1
i = x
⟨αi,αj ⟩Ej
, KiFjK−1
i = x
−⟨αi,αj ⟩Fj
,
EiFj − FjEi = δij
Ki − K−1
i
x
di − x−di
,
1
X−aij
0
(−1)kE
(1−aij−k)
i EjE
(k)
i = 0,
1
X−aij
0
(−1)kF
(1−aij−k)
i FjF
(k)
i = 0, i ̸= j,
where di = ⟨αi, αi⟩/2, and, for k ≥ 0, E
(k)
i = E
k
i
/[k]di!, F
(k)
i = F
k
i
/[k]di!. Note that di
is an integer, hence so is every inner product ⟨αi, αj ⟩. Quantum integers and factorials
are defined in the usual way, [k]x =
x
k−x−k
x−x−1
; [k]x! = [k]x . . . [2]x, [k]di = [k]x
di
, and result
selfadjoint scalars of C(x). There is a unique ∗–involution on Ux(g) making it into a
∗–algebra over C(x) such that
K∗
i = K−1
i
, E∗
i = Fi
.
This algebra becomes a Hopf algebra, with coproduct, counit, and antipode defined, as
follows, see e in [185], where his K˜
i corresponds to our Ki
, see also [24, 161],
∆(Ki) = Ki ⊗ Ki,
∆(Ei) = Ei ⊗ Ki + 1 ⊗ Ei, ∆(Fi) = Fi ⊗ 1 + K−1
i ⊗ Fi
,

124 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
S(Ki) = K−1
i
, S(Ei) = −EiK−1
i
, S(Fi) = −KiFi,
ε(Ki) = 1, ε(Ei) = ε(Fi) = 0.
One has the following relations between coproduct, antipode and involution for a ∈
Ux(g),
∆(a
∗
) = ∆op(a)
∗
(19.2)
ε(a
∗
) = ε(a), S(a
∗
) = S(a)
∗
, S2(a) = K−1
2ρ aK2ρ, (19.3)
where 2ρ the sum of the positive roots, and, for an element α =
P
i
kiαi of the root lattice,
Kα := K
k1
1
. . . Kkr
r
.
Remark 19.2. Let us regard the universal enveloping algebra U(g) as the classical limit
of Ux(g), that is with generators Ei, Fi, Hi such that Ki = x
diHi
, for a rigorous explanation
of this equality see e.g. [24] pag. 304. Since (Ki)
∗ = Ki
−1
(x
∗ = x−1
), the classical limit
of the ∗-involution of Ux(g) is given by
E
∗
i = Fi
, F∗
i = Ei H
∗
i = Hi
.
This is the same as the classical limit arising from the usual †–involution of Ux(g) making
it into a Hopf ∗-algebra (E
†
i = Fi
, F
†
i = Ei
, K∗
i = Ki
, x
∗ = x) we refer to Sect. 13.1 [24]
and Sect. 2.4 [141] for more details. In both cases the real form gR of g corresponding
to the classical limit is the usual compact real form, the real Lie subalgebra of skeweak
adjoint elements a
∗ = −a.
Let G be the connected simply connected complex Lie group with Lie algebra g. Then
the Lie subgroup K of G with Lie algebra gR is compact. Moreover for any λ ∈ Λ
+,
the Weyl module Vλ of U(g) is unitarizable, thus for a given highest weight vector vλ, Vλ
admits a unique positive Hermitian form (ξ, η) such that (vλ, vλ) = 1, (aξ, η) = (ξ, a∗η)
for ξ, η ∈ Vλ, a ∈ U(g), and it follows that Vλ defines a unitary representation of K. At
the level of specialization to a complex number q, we recall that U(g) is isomorphic to the
quotient of U1(g) by the ideal generated by the elements Ki − 1.
Remark 19.3. Note that the ∗-involution of U(g) is related to the order 2-antilinear
automorphism T of g defining the compact real form by a
∗ = T(S(a)), a ∈ U(g), where
S is the antipode. The presence of the antipode S is necessary because the conjugation
T extends to an antilinear multiplicative map on U(g), but the ∗-involution needs to be
antimultiplicative.
Lusztig form U
res
A
(g) is the algebra over A generated by E
(k)
i
, F
(k)
i
, Ki. It is an integral
form of Ux(g) in that Ux(g) = U
res
A
(g)C(x) and U
res
A
(g) is free over A. The algebraic relations
among the generators only involve coefficients in A, thus this form may be specialized at
roots of unity. To construct an R-matrix, that we briefly recall in the next subsection, we
need to embed U
res
A
(g) into a larger algebra. By [161], we need to extend the ring of scalars
from A to
A
′
:= C[x
1/L, x−1/L],
with L the smallest positive integer such that L⟨λ, µ⟩ ∈ Z for all dominant weights λ, µ.
The values of L for all Lie types are listed in [161]. For example, L = N for g = slN .

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 125
We define the integral form UA′(g) as the A′–subalgebra generated by the elements E
(k)
i
,
F
(k)
i
and Ki. This is known to be a ∗–invariant Hopf A′–algebra with the structure inherited
from Ux(g). Applying the construction in Sect. 1 of [161] to the modified polynomial ring,
we associate to UA′(g) an extended Hopf algebra U
†
A′(g) in a topological sense, that is the
coproduct takes values in a topological completion of U
†
A′(g) ⊗ U
†
A′(g).
Sawin gives a detailed construction of the R-matrix of U
†
A′(g). To develop this, considers
among other things a definition of U
†
A′(g) containing the function algebra Map(Λ, A′
) as a
Hopf subalgebra. Moreover U
†
A′(g) has the structure of a topological ribbon Hopf algebra.
Another relevant aspect of this construction that also plays an important tole for us is that
U
†
A′(g) embeds faithfully in the discrete algebra given by the direct product
U
†
A′(g) → ΠV End(V ) (19.4)
of linear endomorphism algebras on weight modules V . A weight module is defined as
an A′-free U
†
A′(g)-module which is a finite direct sum of finitely generated λ-weight A′
-
modules Vλ associated to an integral weight λ ∈ Λ. In turn, the λ-weight A′-submodule
is defined by Vλ = {v ∈ V : Kiv = x
⟨λ,αi⟩
v, fv = f(λ)v}. Thus elements of U
†
A′(g) act as
matrices with entries in A′ on basis elements. The coproduct
∆ : U
†
A′(g) → ΠV,W End(V ) ⊗ End(W) (19.5)
has range the closure of U
†
A′(g) ⊗ U
†
A′(g) in ΠV,W End(V ) ⊗ End(W).
19.2. The R-matrix of U
†
A′(g) and ribbon structure. The formula for the R-matrix R
of U
†
A′(g) may be found by the end of Sect. 1 in [161]. The ribbon element v is constructed
from ω = K2ρ which is a pivot (or charmed) element and Drinfeld element u via ω = uv−1
as described in the remark following Cor. 10.11.
Our R-matrix corresponds to R
−1
21 in [161] and agrees with [185]. We shall need to recall
a characterization of R following [185] and going back to to Lusztig, Chapter 32 [119].
Consider r-ples of non negative integers (ν1, . . . , νr) and U
+
ν
the span of products of E
(k)
i
where νiis the sum of all the k occurring in a monomial for a fixed i. One similarly defines
U
−
ν
. Consider
X =
M
ν
U
−
ν ⊕ U
+
ν
.
Moreover, consider the unique antilinear (involutive) automorphism T → T of U
†
A′(g)
that fixes the generators E
(k)
i
, F
(k)
i
and such that x = x
−1
, Ki = (Ki)
−1
. This automorphism induces a new coproduct ∆ on U
†
A′(g) by conjugation.
Then there is a unique element Θ ∈ X such that Θ0 = I ⊗ I and ∆(a) = Θ∆(a)Θ−1,
a ∈ U
†
A′(g). The following result summarizes properties of the R-matrix, which go back to
ideas of Drinfeld. Our approach follows Ch. 32 in [119], the computation of the action (c)
of the ribbon element may be found in [46], compatibility properties (a) and (b) with the
∗
-involution are in were proved by Wenzl in Prop. 1.4.1 in [185].

126 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Theorem 19.4. The R-matrix of U
†
A′(g) is given by R = ΠΘ, where Π acts on a tensor
product V ⊗ W of A′-free weight modules by
Πv ⊗ w = x
⟨µ,ν⟩
v ⊗ w
where µ and ν are weights of the weight vectors v and w respectively. Moreover we have
(a) ∆(a
∗
) = ∆(op)(a)
∗
,
(b) R∗ = (R21)
−1
,
(c) v acts as the scalar x
−⟨λ,λ+2ρ⟩ on an irreducible highest weight module with highest
weight λ.
Note that our Π denotes Π−1in [185]. Moreover Π belongs to a certain topological
completion of U
†
A′(g) ⊗ U
†
A′(g), see e.g. [161], hence the same holds for R.
Definition 19.5. The ribbon element v ∈ U
†
A′(g) is called the (formal) quantum Casimir
operator.
19.3. Weyl modules for U
†
A′(g) and Lusztig and Kashiwara bases. Let λ be a dominant integral weight and Vλ(x) an the irreducible representation of Ux(g) with highest
weight λ, and let vλ be the highest weight vector of Vλ(x) (unique up to a nonzero scalar
multiple), that is Kivλ = x
⟨αi,λ⟩
vλ and λ is maximal with this property. This module is
called a Weyl module, it is direct sum of weight spaces. Tensor product of Weyl modules decomposes into a direct sum of Weyl modules with the same multiplicities as in the
classical case,
Vλ(x) ⊗ Vµ(x) = ⊕γmλ,µ
γ Vγ(x),
and multiplicities mλ,µ
γ
involve the Weyl group and rely on the classical Racah formula,
We shall not need these multiplicities in detail, and we refer the interested reader to [98],
Sect. 10 in [24].
A canonical basis B for the C(x
1/L)-subalgebra Ux(g)− of Ux(g) generated by the Fi has
been constructed by Lusztig and Kashiwara [121], [104].
Set Bλ = {b ∈ B : bvλ ̸= 0}. Then b ∈ Bλ → bvλ ∈ Vλ(x) is a bijection of Bλ onto a
finite basis of Vλ(x), and this is the canonical basis of Vλ(x). Moreover, Vλ(x) has a free
A′-submodule Vλ,A′ such that C(x)Vλ,A′ = Vλ(x) with basis Bλvλ for a suitable choice of
vλ. This is a basis of weight vectors. (in particular Vλ,A′ is a weight module for U
†
A′(g)
in the sense of the previous subsection.) In other words the generators of U
†
A′(g) act on
Bλvλ as matrices with coefficients in A′. Canonical bases plays an important role in Wenzl
construction of the unitary structure of the fusion category C(g, q, ℓ), (see also the following
Subsect. 19.6.). Loosely speaking, a canonical basis vi of Vλ,A′ specialized in a complex
number q which varies continuously on an arch, is a basis on Vλ(q), and certain analytic
properties that hold at one extreme of the arc may be carried to the other extreme by
continuity. We shall recall this more precisely in Theorem 31.2 and Cor. 31.4.
For the same motivations canonical bases will play a role in the motivation of our abstract
Drinfeld-Kohno theorem in Sect. 30 and our main result in Sect. 33.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 127
If µ is another dominant integral weight then following [185] we endow Vλ,A′ ⊗A′ Vµ,A′
with the tensor product of the canonical bases bvλ ⊗ b
′
vµ, b, b
′ ∈ B. This tensor product
decomposes into a direct sum of Weyl modules, with their canonical bases,
Vλ,A′ ⊗A′ Vµ,A′ = ⊕γmλ,µ
γ Vγ,A′,
and multiplicities mλ,µ
γ with the same multiplicities as in the classical case.
19.4. Specialization Uq(g) at a complex primitive root of unity q of order ℓ
′
. We
next describe a specialization of U
†
A′(g) which differs slightly from the specialization given
in Sect. 2 of [161], in that we work with a complex root of unity, combining with the
presentation of [185], and references therein among them Drinfeld and Lusztig work. See
also the restricted specialization in Sect. 11.2 in [24].
We fix q ∈ T a primitive root of unity of order ℓ
′
(see the beginning of the section for
our notation as compared to [161]) and we set ℓ
′ = ∞ if qn ̸= 1 for all n ∈ N. We consider
the ∗–homomorphism A′ → C which evaluates x
1/L to a specified complex L-root q1/L of
q. We form the tensor product ∗–algebra,
Uq(g) := U
†
A′(g) ⊗A′ C.
The algebra Uq(g) becomes a ribbon complex Hopf algebra with a ∗–involution, and is
topological in the sense of [161]. Let V be a weight module (as in the last part of Subsect.
19.1). We set
V (q) = V ⊗A′ C.
By (19.4), we have a faithful embedding into a direct product of full matrix algebras over
C
Uq(g) → ΠV End(V (q)) (19.6)
and by (19.5) the coproduct has range
∆ : Uq(g) → ΠV (q),W(q)End(V (q)) ⊗ End(W(q)) (19.7)
in a direct product of full matrix algebras.
Note that the R-matrix R and the ribbon element v ∈ Uq(g) depend (only) on the choice
of q
1/L, see Sect. 1 in [161], Sect. 1.4 in [185]. This variability of R-matrices and ribbon
elements will be useful in Sect. 25.
On the other hand, in Sect. 32 in connection with the study of unitary structure and
construction of a Drinfeld twist, it will be important to follow Wenzl [185] and specify the
value of q (of possibly infinite order) written in the form q = e
iπt by t ∈ (−1, 1] and the
L-root q
1/L = eitπ/L
.

128 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
19.5. Specialization of Weyl modules Vλ(q) and simplicity in the closed Weyl
alcove Λ+(q). Let Vλ(x) be the irreducible representation of Ux(g) with highest weight λ
and let vλ be the highest weight vector of Vλ(x) and Vλ,A′ the associated free A′
-module
with basis Bλ introduced in Sect. 19.3. Then we have a specialized complex Uq(g)-modules
at a complex number q
Vλ(q) := Vλ,A′ ⊗A′ C.
This is a cyclic module for Uq(g) generated by vλ(q) = vλ ⊗ 1, simple if q is not a root of
unity, but it is not always so if q is a root of unity.
Let as before ℓ
′ be the order of q and ℓ the order of q2
. The linkage principle gives
information on irreducibility of Vλ(q) at primitive roots of unity. We consider the affine
Weyl group Wℓ
′, and its translated action on the real vector space E spanned by the roots,
defined by w.x = w(x + ρ) − ρ. Let d denote the ratio between the squared lengths of the
longest to the shortest root, so d = 1 for Lie types ADE, d = 2 for BCF and d = 3 for
G2. The structure of Wℓ
′ depends on the parity and divisibility by d of the order ℓ
′ of q.
We recall that affine Weyl group Wℓ
′ is the group of isometries of h
∗ generated by
reflections in the hyperplanes {x ∈ E : ⟨x, αi⟩ = kℓidi}, where k ∈ Z, ℓ
′
i
is the order of q
di
,
and ℓiis ℓ
′
i
or ℓ
′
i
/2 according to whether ℓ
′
i
is odd or even. The translated action admits
a fundamental domain, called the principal Weyl alcove. The open Weyl alcove is defined
by
Λ
+(q) := {λ ∈ Λ+ : ⟨λ + ρ, θ⟩ < ℓ},
if d divides ℓ or
Λ
+(q) := {λ ∈ Λ+ : ⟨λ + ρ, θs⟩ < ℓ},
if d does not divide ℓ, with θ the highest root and θs the highest short root in the root
system. The element ρ denotes the Weyl vector, defined as the sum of the fundamental
weights. The linkage principle then implies that Vλ(q) is simple for λ ∈ Λ+(q). The
following result is well known see [24, 161] and references therein.
Theorem 19.6. The quantized Weyl modules Vλ(q) with λ ∈ Λ
+(q) have positive quantum
dimension provided q satisfies Def. 19.1. The indecomposable tilting modules Tλ with λ not
in Λ
+(q) are negligible. The open Weyl alcove Λ+(q) labels the simple objects of C(g, q, ℓ).
The quantum dimension can be defined using the rigidity equations. The explicit computation for quantized Weyl modules Vλ(q) has roots in the classical Weyl dimension formula
and is given by
dimq(Vλ(q)) = Πλ∈Φ+
q
⟨λ+ρ,α⟩ − q−⟨λ+ρ,α⟩
q
⟨ρ,α⟩ − q−⟨ρ,α⟩
.
The lower bound on the order ℓ of q
2
required in Def. 19.1 is exactly that each of the
denominators in the above formula does not vanish. We recall the notion of tilting modules
and negligible modules in the following subsection 19.6, and the construction of C(g, q, ℓ)
in the following section 20, see also Prop. 2.4 in [185], see also [2, 161, 24].

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 129
19.6. The tilting category T(g, q, ℓ). In this subsection we assume ℓ
′ < ∞. Constructions due to [2, 3, 70, 155], give rise to a semisimple, ribbon, fusion category, T(g, q, ℓ) that
we briefly outline. Notice that the constructions impose no restriction on the order ℓ
′ of
q, and depend on the order ℓ of q
2
.
Since a Weyl module Vλ(q) may fail to be irreducible, Andersen developed the notion of
tilting module, see Sect. 1, 3 [161], Ch. 11.2 [24] and references to the original papers.
A tilting module is a finite dimensional representation W of Uq(g) admitting together
with its dual, a Weyl filtration, i.e. a sequence of modules {0} ⊂ W1 ⊂ · · · ⊂ W such
that Wi+1/Wiis isomorphic to a Weyl module Vλi
(q) with λi ∈ Λ
+. Weyl filtrations are
non-unique, but for all filtrations of W the number of factors isomorphic to a given Vλ(q)
is unique, and it is in fact given by the multiplicity of Vλ(x) in W(x) if W is obtained from
a specialisation x → q of a module W(x) of Ux(g), see Prop. 3 and Remark 2 in [161] for
a precise statement.
By Sect. 11.3 [24] or Cor. 5 in [161], every tilting module decomposes into a direct sum
of indecomposable tilting modules, and every indecomposable tilting module is isomorphic
to a unique indecomposable tilting module Tλ with maximal vector of weight λ, with
λ ∈ Λ
+. Thus Tλ has a filtration by submodules 0 ⊂ Vλ ⊂ V2 ⊂ V3 ⊂ · · · ⊂ Tλ such that
V2/Vλ ≃ Vµ(q), V3/V2 ≃ Vν(q), . . . with λ > µ > ν . . . , [24] p. 363, and the dual T
∗
λ has a
similar filtration and is isomorphic to T−w0λ. Moreover tensor products of tilting modules
is tilting, thus the category T(g, q, ℓ) of tilting modules becomes a tensor category with
duals [24, 161].
It is important for us that every Weyl module Tλ = Vλ(q) for λ ∈ Λ+(q), by e.g. [4]
Subsect. 1.1. This in particular implies that the multiplicities of the dominant weights of
the factors in the Weyl filtrations of tensor products Vλ1(q) ⊗ · · · ⊗ Vλn(q) with λi ∈ Λ+(q)
are the same as those determined by decomposition into irreducibles of the corresponding
tensor product in the classical (or generic) case.
It follows from Sebsect. 19.1, see also Theorems 3, 4 in [161], that the category of tilting
modules over Uq(g) is a ribbon category. For a fixed choice of q
1/L, the corresponding
R-matrices define corresponding braided symmetries for the representation category, for
more details on the classification in the type A case, and references see Sect. 25.
Proposition 19.7. Properties (a), (b), of Theorem 19.4 hold for the coproduct and Rmatrix of Uq(g). The ribbon element v of Uq(g) acts as the constant vλ = q
−⟨λ,λ+2ρ⟩
for
λ ∈ Λ+(q), with Λ+(q) := {λ ∈ Λ
+ : ⟨λ + ρ, θ⟩ ≤ ℓ} the closed Weyl alcove.
